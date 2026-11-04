#!/opt/homebrew/bin/python3.13
"""Study 0 - independent recomputation (verification duty, sealed DESIGN section 13).

Run on the pinned host (study/ENVIRONMENT.md), AFTER compute_study0.py:
    env TZ=UTC PYTHONHASHSEED=0 /opt/homebrew/bin/python3.13 study/src/independent_check.py

Recomputes, WITHOUT importing or reusing any function of the production pipeline:
  (a) both assets' full-window funding sums and arithmetic annualized rates,
      using exact rational arithmetic (fractions.Fraction) over a separately
      written loader;
  (b) the 29 bps cost worksheet;
and compares them to reports/results_study0.json. Exits non-zero on any mismatch.
"""
import glob
import json
import sys
from decimal import Decimal
from fractions import Fraction


def frac(s):
    """Exact rational from a decimal string (via Decimal, exact)."""
    return Fraction(Decimal(s))

HOUR_MS = 3600000
WIN_FIRST = 1687478400000     # 2023-06-23T00:00Z
WIN_LAST = 1793487600000      # 2026-10-31T23:00Z

failures = []


def note(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ("" if ok else " " + detail))
    if not ok:
        failures.append(name)


def funding_recompute(coin):
    """Separate code path: glob pages, keyed by settlement hour, Fraction sums."""
    seen = {}
    for path in sorted(glob.glob("data/raw/hyperliquid/%s/page_*.json" % coin)):
        with open(path) as fh:
            for rec in json.load(fh):
                hour = rec["time"] - rec["time"] % HOUR_MS
                prev = seen.get(hour)
                if prev is not None and prev != rec["fundingRate"]:
                    note("%s conflicting duplicate at %d" % (coin, hour), False)
                    return None
                seen[hour] = rec["fundingRate"]
    total = Fraction(0)
    nobs = 0
    for hour, rate in seen.items():
        bucket = hour - HOUR_MS
        if WIN_FIRST <= bucket <= WIN_LAST:
            total += frac(rate)
            nobs += 1
    return total, nobs


def main():
    with open("reports/results_study0.json") as fh:
        res = json.load(fh)

    for coin in ("ETH", "BTC"):
        got = funding_recompute(coin)
        if got is None:
            continue
        total, nobs = got
        stats = res["funding"][coin]["stats"]
        note("%s observed hours equal" % coin, nobs == stats["observed_hours"],
             "mine=%d pipeline=%d" % (nobs, stats["observed_hours"]))
        pipe_sum = frac(stats["sum_per_dollar_exact"])
        note("%s full-window funding sum equal (exact)" % coin, pipe_sum == total,
             "mine=%s pipeline=%s" % (total, pipe_sum))
        ann = Fraction(8760) * total / nobs
        pipe_ann = frac(stats["arithmetic_annualized_rate_exact"])
        # pipeline annualization uses 28-significant-digit decimal division
        tol = abs(ann) / Fraction(10) ** 24 + Fraction(1, 10 ** 30)
        note("%s annualized rate equal within decimal-context tolerance" % coin,
             abs(pipe_ann - ann) <= tol, "mine=%s pipeline=%s" % (float(ann), float(pipe_ann)))

    # cost worksheet, recomputed from the sealed constants
    expect = {}
    for mult, case in ((1, "base"), (2, "doubled (sole sensitivity)")):
        rt = Fraction(2) * (Fraction(9, 2) + Fraction(10)) * mult   # 29 bps / 58 bps
        for days in (30, 90, 365):
            drag = rt * 365 / days
            expect[(case, days)] = ("%.2f" % float(rt), "%.2f" % float(drag))
    rows = {(r["case"], r["holding_days"]): (r["roundtrip_bps"], r["annualized_drag_bps"])
            for r in res["cost_worksheet"]["rows"]}
    note("cost worksheet rows present", sorted(rows) == sorted(expect))
    for key in sorted(expect):
        note("cost %s D=%d" % key, rows.get(key) == expect[key],
             "mine=%r pipeline=%r" % (expect[key], rows.get(key)))

    print("independent check: %s" % ("PASS" if not failures else "FAIL (%d)" % len(failures)))
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
