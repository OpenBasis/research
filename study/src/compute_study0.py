#!/opt/homebrew/bin/python3.13
"""Study 0 - sealed analysis pipeline (DESIGN.md, seal commit 9d3ed181...3be2).

Run on the pinned host environment only (study/ENVIRONMENT.md):
    env TZ=UTC PYTHONHASHSEED=0 /opt/homebrew/bin/python3.13 study/src/compute_study0.py [--out DIR]

Standard library only. Deterministic: exact decimal sums, float64 distribution
statistics, type-7 quantiles, sorted keys, fixed numeric formats, no timestamps.
Implements DESIGN.md sections 4-10 exactly; aborts on any data defect or on any
mismatch against the pre-seal coverage census data/COVERAGE.json.
"""
import argparse
import json
import math
import os
import sys
from datetime import datetime, timezone
from decimal import Decimal

H = 3_600_000                     # one hour in ms
W0 = 1_687_478_400_000            # 2023-06-23T00:00Z bucket start
W1 = 1_793_487_600_000            # 2026-10-31T23:00Z bucket start
NB = (W1 - W0) // H + 1           # 29448

RATE_FMT = "%.12f"                # funding rates and accruals (float presentation)
RET_FMT = "%.8f"                  # returns
BPS_FMT = "%.2f"                  # basis points

FUNDING_LABEL = ("Rate description per $1 constant quote notional, short-receives-"
                 "positive. Not compounded APY; not an investable equity curve.")
SPOT_LABEL = ("Reference-market observations (Coinbase hourly closes), not "
              "liquidation or margin tests; marks are not execution proof.")
COST_LABEL = ("Modeled inputs, not empirical findings or current executable "
              "quotes. Unpriced items remain unpriced, neither zero nor included.")
RESERVE_LABEL = ("Modeled approximation from aggregator evidence (DefiLlama "
                 "apyBase, an APR in percent per pinned adapter source); derived "
                 "hourly rates are NOT observed hourly returns. Base rate only; "
                 "apyReward excluded. Segments are separate; never stitched.")


def iso(ms):
    return datetime.fromtimestamp(ms // 1000, tz=timezone.utc).strftime("%Y-%m-%dT%H:%MZ")


def fail(msg):
    sys.stderr.write("ABORT: %s\n" % msg)
    sys.exit(1)


# ---------------------------------------------------------------- quantiles
def quantile_type7(sorted_vals, p):
    """Linear interpolation, type 7 (numpy default). sorted_vals ascending."""
    n = len(sorted_vals)
    if n == 0:
        raise ValueError("empty sample")
    h = (n - 1) * p
    lo = math.floor(h)
    hi = min(lo + 1, n - 1)
    return sorted_vals[lo] + (h - lo) * (sorted_vals[hi] - sorted_vals[lo])


# ---------------------------------------------------------------- hyperliquid
def map_funding(records, label=""):
    """records: iterable of {'fundingRate': str, 'premium': str, 'time': int ms}.
    Returns (buckets, census). D3 mapping: settlement hour -> bucket - 1h.
    Identical duplicates (same settlement hour, same rate+premium) deduplicated;
    conflicting duplicates abort."""
    by_hour = {}
    ident = 0
    jit_max = 0
    jit_over_60s = 0
    for r in records:
        t = r["time"]
        hour = (t // H) * H
        jit = t - hour
        if jit > jit_max:
            jit_max = jit
        if jit > 60_000:
            jit_over_60s += 1
        key = (r["fundingRate"], r["premium"])
        if hour in by_hour:
            if by_hour[hour] == key:
                ident += 1
            else:
                fail("conflicting duplicate funding record %s at settlement hour %s"
                     % (label, iso(hour)))
        else:
            by_hour[hour] = key
    buckets = {}
    for hour, (rate, _prem) in by_hour.items():
        b = hour - H
        if W0 <= b <= W1:
            buckets[b] = Decimal(rate)
    missing = [b for b in range(W0, W1 + H, H) if b not in buckets]
    census = {
        "records": sum(1 for _ in by_hour) + ident,
        "identical_duplicates": ident,
        "conflicting_duplicates": 0,
        "jitter_ms_max": jit_max,
        "jitter_ms_over_60s": jit_over_60s,
        "observed": len(buckets),
        "expected": NB,
        "missing_buckets": len(missing),
        "missing_list": [iso(b) for b in missing],
    }
    return buckets, census


def load_funding(coin):
    d = os.path.join("data", "raw", "hyperliquid", coin)
    records = []
    for fn in sorted(os.listdir(d)):
        if fn.endswith(".json"):
            with open(os.path.join(d, fn)) as f:
                records += json.load(f)
    return map_funding(records, label=coin)


# ---------------------------------------------------------------- coinbase
def map_candles(rows, label=""):
    """rows: iterable of [time_s, low, high, open, close, volume] (Decimals)."""
    cand = {}
    ident = 0
    for row in rows:
        t = int(row[0]) * 1000
        if t in cand:
            if cand[t] == row:
                ident += 1
            else:
                fail("conflicting duplicate candle %s at %s" % (label, iso(t)))
        else:
            cand[t] = row
    closes = {t: row[4] for t, row in cand.items() if W0 <= t <= W1}
    missing = [b for b in range(W0, W1 + H, H) if b not in closes]
    census = {
        "unique_candles": len(cand),
        "identical_duplicates": ident,
        "conflicting_duplicates": 0,
        "in_window_observed": len(closes),
        "expected": NB,
        "missing_buckets": len(missing),
        "missing_list": [iso(b) for b in missing],
    }
    return closes, census


def load_closes(product):
    d = os.path.join("data", "raw", "coinbase", product)
    rows = []
    for fn in sorted(os.listdir(d)):
        if fn.endswith(".json"):
            with open(os.path.join(d, fn)) as f:
                rows += json.load(f, parse_float=Decimal)
    return map_candles(rows, label=product)


# ---------------------------------------------------------------- reserve (A2)
def boundary_after(ms):
    """First hour boundary strictly after ms."""
    return (ms // H + 1) * H


def parse_ts_ms(s):
    dt = datetime.fromisoformat(s.replace("Z", "+00:00"))
    return int(round(dt.timestamp() * 1000))


def derive_reserve(snaps, scope0_ms):
    """snaps: sorted list of (ts_ms, apyBase Decimal). Amendment A2 rule:
    a snapshot applies from the first hour boundary strictly after its
    timestamp, for at most 24 buckets (documented one-snapshot-per-calendar-
    date cadence), never at/after the next snapshot's first applicable
    boundary; everything else is a gap. Returns (rates, seg0, census)."""
    seg0 = boundary_after(snaps[0][0]) if scope0_ms is None else scope0_ms
    seg0 = max(seg0, W0)
    rates = {}
    for i, (tms, base) in enumerate(snaps):
        b0 = boundary_after(tms)
        b1 = b0 + 23 * H
        if i + 1 < len(snaps):
            b1 = min(b1, boundary_after(snaps[i + 1][0]) - H)
        b = max(b0, seg0)
        end = min(b1, W1)
        while b <= end:
            rates[b] = base
            b += H
    expected = (W1 - seg0) // H + 1
    census = {
        "snapshots_total": len(snaps),
        "first_snapshot": iso(snaps[0][0]),
        "segment_scope_first_bucket": iso(seg0),
        "covered": len(rates),
        "expected": expected,
        "gaps": expected - len(rates),
    }
    return rates, seg0, census


def load_reserve(chart_path, scope0_ms):
    with open(chart_path) as f:
        doc = json.load(f, parse_float=Decimal)
    snaps = []
    for x in doc["data"]:
        ab = x["apyBase"]
        ts = parse_ts_ms(x["timestamp"])
        if ab is None:
            fail("null apyBase at %s in %s" % (x["timestamp"], chart_path))
        snaps.append((ts, ab if isinstance(ab, Decimal) else Decimal(ab)))
    snaps.sort()
    return derive_reserve(snaps, scope0_ms)


# ---------------------------------------------------------------- statistics
def funding_stats(buckets):
    vals = [buckets[b] for b in sorted(buckets)]
    n = len(vals)
    total = sum(vals, Decimal(0))
    annualized = Decimal(8760) * total / Decimal(n)
    fl = sorted(float(v) for v in vals)
    pos = sum(1 for v in vals if v > 0)
    zer = sum(1 for v in vals if v == 0)
    neg = n - pos - zer
    return {
        "label": FUNDING_LABEL,
        "observed_hours": n,
        "sum_per_dollar_exact": str(total),
        "arithmetic_annualized_rate_exact": str(annualized),
        "mean": RATE_FMT % (math.fsum(fl) / n),
        "median": RATE_FMT % quantile_type7(fl, 0.5),
        "p5": RATE_FMT % quantile_type7(fl, 0.05),
        "p95": RATE_FMT % quantile_type7(fl, 0.95),
        "min": str(min(vals)),
        "max": str(max(vals)),
        "share_positive": RET_FMT % (pos / n),
        "share_zero": RET_FMT % (zer / n),
        "share_negative": RET_FMT % (neg / n),
        "quantile_method": "linear interpolation (type 7)",
    }


def iter_months():
    y, m = 2023, 6
    while (y, m) <= (2026, 10):
        start = int(datetime(y, m, 1, tzinfo=timezone.utc).timestamp()) * 1000
        ny, nm = (y + 1, 1) if m == 12 else (y, m + 1)
        nxt = int(datetime(ny, nm, 1, tzinfo=timezone.utc).timestamp()) * 1000
        yield "%04d-%02d" % (y, m), start, nxt - H
        y, m = ny, nm


def iter_years():
    for y in (2023, 2024, 2025, 2026):
        start = int(datetime(y, 1, 1, tzinfo=timezone.utc).timestamp()) * 1000
        nxt = int(datetime(y + 1, 1, 1, tzinfo=timezone.utc).timestamp()) * 1000
        yield "%04d" % y, start, nxt - H


def calendar_table(buckets, periods):
    """Completeness rule of DESIGN section 4: COMPLETE only if every hour of the
    period is inside the window AND observed; else INCOMPLETE with the observed
    subtotal shown separately."""
    rows = []
    for label, p0, p1 in periods:
        period_hours = (p1 - p0) // H + 1
        a, b = max(p0, W0), min(p1, W1)
        in_window = max(0, (b - a) // H + 1) if a <= b else 0
        observed = [x for x in range(a, b + H, H) if x in buckets] if a <= b else []
        subtotal = sum((buckets[x] for x in observed), Decimal(0))
        window_partial = in_window < period_hours
        missing = in_window - len(observed)
        complete = (not window_partial) and missing == 0
        reasons = []
        if window_partial:
            reasons.append("window-partial")
        if missing > 0:
            reasons.append("missing-data")
        rows.append({
            "period": label,
            "period_hours": period_hours,
            "in_window_hours": in_window,
            "observed_hours": len(observed),
            "missing_in_window": missing,
            "status": "COMPLETE" if complete else "INCOMPLETE (%s)" % "+".join(reasons),
            "total_if_complete": str(subtotal) if complete else None,
            "observed_subtotal": str(subtotal),
        })
    return rows


def negative_runs(buckets):
    def status(b):
        if b < W0 or b > W1:
            return "outside"
        if b not in buckets:
            return "missing"
        return "neg" if buckets[b] < 0 else "nonneg"

    raw, cur = [], None
    for b in range(W0, W1 + H, H):
        if status(b) == "neg":
            if cur is None:
                cur = [b, b]
            else:
                cur[1] = b
        elif cur is not None:
            raw.append(tuple(cur))
            cur = None
    if cur is not None:
        raw.append(tuple(cur))

    runs = []
    for s_, e_ in raw:
        before, after = status(s_ - H), status(e_ + H)
        completed = before == "nonneg" and after == "nonneg"
        reasons = []
        if "outside" in (before, after):
            reasons.append("window-boundary")
        if "missing" in (before, after):
            reasons.append("gap-adjacent")
        cum = sum((buckets[b] for b in range(s_, e_ + H, H)), Decimal(0))
        runs.append({
            "start": iso(s_), "end": iso(e_),
            "duration_h": (e_ - s_) // H + 1,
            "cumulative_funding_exact": str(cum),
            "completed": completed,
            "censoring": "+".join(reasons) if reasons else "",
        })
    comp = [r for r in runs if r["completed"]]
    cens = [r for r in runs if not r["completed"]]
    summary = {"completed_count": len(comp), "censored_count": len(cens)}
    if comp:
        dur = sorted(float(r["duration_h"]) for r in comp)
        cfl = sorted(float(Decimal(r["cumulative_funding_exact"])) for r in comp)
        summary.update({
            "duration_median_h": "%.2f" % quantile_type7(dur, 0.5),
            "duration_p95_h": "%.2f" % quantile_type7(dur, 0.95),
            "duration_max_h": max(r["duration_h"] for r in comp),
            "cumulative_funding_median": RATE_FMT % quantile_type7(cfl, 0.5),
            "cumulative_funding_most_negative":
                str(min((Decimal(r["cumulative_funding_exact"]) for r in comp))),
            "note": ("Completed runs only; censored runs listed separately and "
                     "excluded. No persistence inferred across gaps or into the "
                     "future."),
        })
    return runs, summary


def spot_risk(closes, k):
    rets = []
    for t in range(W0 + k * H, W1 + H, H):
        if all((t - j * H) in closes for j in range(k + 1)):
            rets.append((float(closes[t] / closes[t - k * H] - 1), t))
    if not rets:
        fail("no spot returns computable for k=%d" % k)
    vals = sorted(r for r, _ in rets)
    dn, up = min(rets), max(rets)
    return {
        "label": SPOT_LABEL,
        "k_hours": k,
        "n_returns": len(rets),
        "p1": RET_FMT % quantile_type7(vals, 0.01),
        "p99": RET_FMT % quantile_type7(vals, 0.99),
        "worst_down": {"return": RET_FMT % dn[0], "end_bucket": iso(dn[1])},
        "worst_up": {"return": RET_FMT % up[0], "end_bucket": iso(up[1])},
        "quantile_method": "linear interpolation (type 7)",
    }


def cost_worksheet():
    rows = []
    for mult, case in ((1, "base"), (2, "doubled (sole sensitivity)")):
        perp = Decimal("4.5") * mult
        spot = Decimal("10") * mult
        rt = 2 * (perp + spot)
        for D in (30, 90, 365):
            rows.append({
                "case": case, "holding_days": D,
                "perp_fee_bps_oneway": BPS_FMT % perp,
                "spot_fee_impact_bps_oneway": BPS_FMT % spot,
                "roundtrip_bps": BPS_FMT % rt,
                "annualized_drag_bps": BPS_FMT % (rt * 365 / D),
            })
    return {
        "label": COST_LABEL,
        "rows": rows,
        "gas_illustration": "USD 0.50 per assumed leg, illustration only, never measured route cost",
        "unpriced_register": [
            "perp market impact", "gas beyond the illustration", "transfers",
            "top-ups", "settlement", "borrow/custody", "opportunity cost"],
        "prohibited": ["trade-size grid", "optimal holding period",
                       "total-cost certification", "net-APY claim"],
    }


def reserve_summary(rates, census):
    vals = [rates[b] for b in sorted(rates)]
    n = len(vals)
    acc = [(v / 100) / 8760 for v in vals]
    total = sum(acc, Decimal(0))
    annualized = Decimal(8760) * total / Decimal(n)
    return {
        "label": RESERVE_LABEL,
        "coverage": census,
        "derived_hours": n,
        "sum_accrual_per_dollar": str(total),
        "arithmetic_annualized_mean_accrual": str(annualized),
        "hourly_conversion": "(apyBase/100)/8760, simple accrual",
    }


# ---------------------------------------------------------------- cross-check
def crosscheck(results):
    with open(os.path.join("data", "COVERAGE.json")) as f:
        cov = json.load(f)
    errs = []

    def eq(name, a, b):
        if a != b:
            errs.append("%s: pipeline=%r coverage=%r" % (name, a, b))

    for coin in ("ETH", "BTC"):
        c = cov["hyperliquid_%s" % coin]
        r = results["funding"][coin]["census"]
        eq("%s observed" % coin, r["observed"], c["in_window_buckets_observed"])
        eq("%s missing" % coin, r["missing_buckets"], c["missing_buckets"])
        eq("%s missing list" % coin, r["missing_list"], c["missing_list"])
        eq("%s dup" % coin, r["conflicting_duplicates"], c["conflicting_duplicates"])
    for prod in ("ETH-USD", "BTC-USD"):
        c = cov["coinbase_%s" % prod]
        r = results["spot"][prod]["census"]
        eq("%s observed" % prod, r["in_window_observed"], c["in_window_observed"])
        eq("%s missing" % prod, r["missing_buckets"], c["missing_buckets"])
    for seg, key in (("usdc_e", "aave_usdc_e"), ("native", "aave_native")):
        c = cov[key]
        r = results["reserve"][seg]["coverage"]
        eq("%s snapshots" % seg, r["snapshots_total"], c["snapshots_total"])
        eq("%s covered" % seg, r["covered"], c["derived_hourly_buckets_covered_in_window"])
        eq("%s expected" % seg, r["expected"], c["segment_expected_buckets_in_window"])
        eq("%s gaps" % seg, r["gaps"], c["derived_gap_buckets"])
        eq("%s scope0" % seg, r["segment_scope_first_bucket"], c["segment_scope_first_bucket"])
    if errs:
        fail("coverage cross-check failed:\n  " + "\n  ".join(errs))
    return "PASS: pipeline censuses equal data/COVERAGE.json"


# ---------------------------------------------------------------- tables (md)
def md_table(rows, cols):
    out = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    for r in rows:
        out.append("| " + " | ".join("" if r.get(c) is None else str(r.get(c)) for c in cols) + " |")
    return "\n".join(out) + "\n"


def write_tables(res, tdir):
    os.makedirs(tdir, exist_ok=True)

    def w(name, text):
        with open(os.path.join(tdir, name), "w", newline="\n") as f:
            f.write(text)

    inv = []
    for coin in ("ETH", "BTC"):
        c = res["funding"][coin]["census"]
        inv.append({"series": "Hyperliquid funding %s" % coin, "observed": c["observed"],
                    "expected": c["expected"], "missing": c["missing_buckets"],
                    "duplicates (identical/conflicting)": "%d/%d" % (c["identical_duplicates"], c["conflicting_duplicates"]),
                    "notes": "missing: " + "; ".join(c["missing_list"])})
    for prod in ("ETH-USD", "BTC-USD"):
        c = res["spot"][prod]["census"]
        inv.append({"series": "Coinbase close %s (reference mark)" % prod,
                    "observed": c["in_window_observed"], "expected": c["expected"],
                    "missing": c["missing_buckets"],
                    "duplicates (identical/conflicting)": "%d/%d" % (c["identical_duplicates"], c["conflicting_duplicates"]),
                    "notes": "missing: " + "; ".join(c["missing_list"])})
    for seg in ("usdc_e", "native"):
        c = res["reserve"][seg]["coverage"]
        inv.append({"series": "Aave v3 Arbitrum USDC reserve [%s] (modeled approximation, aggregator evidence)" % seg,
                    "observed": c["covered"], "expected": c["expected"], "missing": c["gaps"],
                    "duplicates (identical/conflicting)": "-",
                    "notes": "A2-derived hourly coverage; scope from %s; %d daily snapshots"
                             % (c["segment_scope_first_bucket"], c["snapshots_total"])})
    w("T01_series_inventory.md", "# T1. Series inventory and coverage\n\n" +
      md_table(inv, ["series", "observed", "expected", "missing",
                     "duplicates (identical/conflicting)", "notes"]) +
      "\n" + res["crosscheck"] + "\n")

    cols2 = ["asset", "observed_hours", "sum_per_dollar_exact",
             "arithmetic_annualized_rate_exact", "mean", "median", "p5", "p95",
             "min", "max", "share_positive", "share_zero", "share_negative"]
    rows2 = [dict(res["funding"][c]["stats"], asset=c) for c in ("ETH", "BTC")]
    w("T02_funding_stats.md", "# T2. Funding descriptive statistics\n\n" +
      FUNDING_LABEL + "\nQuantiles: linear interpolation.\n\n" + md_table(rows2, cols2))

    mcols = ["period", "period_hours", "in_window_hours", "observed_hours",
             "missing_in_window", "status", "total_if_complete", "observed_subtotal"]
    for name, coin in (("T03_monthly_ETH.md", "ETH"), ("T04_monthly_BTC.md", "BTC")):
        w(name, "# %s. Calendar-month funding totals - %s\n\n" % (name[:3], coin) +
          FUNDING_LABEL + "\n\n" + md_table(res["funding"][coin]["monthly"], mcols))
    yr = []
    for coin in ("ETH", "BTC"):
        for r in res["funding"][coin]["yearly"]:
            yr.append(dict(r, asset=coin))
    w("T05_yearly.md", "# T5. Calendar-year funding totals\n\n" + FUNDING_LABEL +
      "\n\n" + md_table(yr, ["asset"] + mcols))

    srows = []
    for coin in ("ETH", "BTC"):
        srows.append(dict(res["funding"][coin]["runs_summary"], asset=coin))
    w("T06_runs_summary.md", "# T6. Negative-run summaries (completed runs) plus censored counts\n\n" +
      md_table(srows, ["asset", "completed_count", "censored_count", "duration_median_h",
                       "duration_p95_h", "duration_max_h", "cumulative_funding_median",
                       "cumulative_funding_most_negative"]) +
      "\nCompleted runs only; censored runs are listed separately in T7 and excluded "
      "from these aggregates. No persistence is inferred across gaps or into the future.\n")

    rcols = ["start", "end", "duration_h", "cumulative_funding_exact", "completed", "censoring"]
    t7 = "# T7. Per-run listing (appendix)\n\n"
    for coin in ("ETH", "BTC"):
        t7 += "\n## %s\n\n" % coin + md_table(res["funding"][coin]["runs"], rcols)
    w("T07_runs_listing.md", t7)

    sp = []
    for prod in ("ETH-USD", "BTC-USD"):
        for k in ("1", "24"):
            r = res["spot"][prod]["risk"][k]
            sp.append({"product": prod, "k_hours": k, "n_returns": r["n_returns"],
                       "p1": r["p1"], "p99": r["p99"],
                       "worst_down": "%s @ %s" % (r["worst_down"]["return"], r["worst_down"]["end_bucket"]),
                       "worst_up": "%s @ %s" % (r["worst_up"]["return"], r["worst_up"]["end_bucket"])})
    w("T08_spot_risk.md", "# T8. Spot risk descriptors\n\n" + SPOT_LABEL +
      "\nQuantiles: linear interpolation.\n\n" +
      md_table(sp, ["product", "k_hours", "n_returns", "p1", "p99", "worst_down", "worst_up"]))

    cw = res["cost_worksheet"]
    w("T09_cost_worksheet.md", "# T9. Cost worksheet\n\n" + COST_LABEL + "\n\n" +
      md_table(cw["rows"], ["case", "holding_days", "perp_fee_bps_oneway",
                            "spot_fee_impact_bps_oneway", "roundtrip_bps", "annualized_drag_bps"]) +
      "\nGas: " + cw["gas_illustration"] + "\n\nUnpriced (visible, neither zero nor "
      "silently included): " + ", ".join(cw["unpriced_register"]) +
      ".\n\nNot produced by design: " + ", ".join(cw["prohibited"]) + ".\n")

    rrows = []
    for seg in ("usdc_e", "native"):
        r = res["reserve"][seg]
        rrows.append({"segment": seg, "derived_hours": r["derived_hours"],
                      "expected": r["coverage"]["expected"], "gaps": r["coverage"]["gaps"],
                      "sum_accrual_per_dollar": r["sum_accrual_per_dollar"],
                      "arithmetic_annualized_mean_accrual": r["arithmetic_annualized_mean_accrual"]})
    w("T10_reserve.md", "# T10. Reserve segment summaries\n\n" + RESERVE_LABEL + "\n\n" +
      md_table(rrows, ["segment", "derived_hours", "expected", "gaps",
                       "sum_accrual_per_dollar", "arithmetic_annualized_mean_accrual"]))

    w("T11_capital_bridge.md", "# T11. Symbolic capital bridge\n\n"
      "With N = matched short notional, R = reserve, C = total capital:\n\n"
      "- funding contribution = (N/C) x sum(funding)\n"
      "- reserve contribution = (R/C) x sum(reserve accrual)\n"
      "- cost contribution = cost dollars / C\n\n"
      "No value of N/C or R/C is selected; no weights are chosen. A yield-bearing\n"
      "reserve is not risk-free cash: calling its return a gain or a drag requires\n"
      "an opportunity-cost comparator that Study 0 does not select. Capital placed\n"
      "in reserve dilutes funding capture per unit of capital and is subject to\n"
      "delayed availability. Unlike return conventions are never summed; the\n"
      "funding sum and the reserve accrual sum remain separate quantities.\n")


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="reports",
                    help="output directory (default: reports). Tables under <out>/tables.")
    args = ap.parse_args()

    res = {"window": {"first_bucket": iso(W0), "last_bucket": iso(W1),
                      "expected_buckets": NB},
           "funding": {}, "spot": {}, "reserve": {}}

    for coin in ("ETH", "BTC"):
        buckets, census = load_funding(coin)
        runs, runs_summary = negative_runs(buckets)
        res["funding"][coin] = {
            "census": census,
            "stats": funding_stats(buckets),
            "monthly": calendar_table(buckets, iter_months()),
            "yearly": calendar_table(buckets, iter_years()),
            "runs": runs,
            "runs_summary": runs_summary,
        }

    for prod in ("ETH-USD", "BTC-USD"):
        closes, census = load_closes(prod)
        res["spot"][prod] = {
            "census": census,
            "risk": {"1": spot_risk(closes, 1), "24": spot_risk(closes, 24)},
        }

    for seg, chart, scope0 in (
            ("usdc_e", os.path.join("data", "raw", "defillama", "chart_usdc_e.json"), W0),
            ("native", os.path.join("data", "raw", "defillama", "chart_native_usdc.json"), None)):
        rates, _seg0, census = load_reserve(chart, scope0)
        res["reserve"][seg] = reserve_summary(rates, census)

    res["cost_worksheet"] = cost_worksheet()
    res["crosscheck"] = crosscheck(res)

    os.makedirs(args.out, exist_ok=True)
    with open(os.path.join(args.out, "results_study0.json"), "w", newline="\n") as f:
        json.dump(res, f, sort_keys=True, indent=1)
        f.write("\n")
    write_tables(res, os.path.join(args.out, "tables"))

    print(res["crosscheck"])
    for coin in ("ETH", "BTC"):
        s = res["funding"][coin]["stats"]
        print("%s: observed=%d sum=%s annualized=%s" %
              (coin, s["observed_hours"], s["sum_per_dollar_exact"],
               s["arithmetic_annualized_rate_exact"]))
    print("OK: outputs written to %s" % args.out)


if __name__ == "__main__":
    main()
