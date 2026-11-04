#!/opt/homebrew/bin/python3.13
"""Study 0 - synthetic fixtures (no Study 0 data touched; no results computed).

Run on the pinned host (study/ENVIRONMENT.md):
    env TZ=UTC PYTHONHASHSEED=0 /opt/homebrew/bin/python3.13 study/src/test_fixtures.py

Checks the sealed definitions against hand-constructed cases: type-7 quantiles,
D3 settlement-to-bucket mapping, duplicate handling, negative-run completion and
censoring (zero breaks, window boundary, gap adjacency), the Amendment A2
bounded reserve-snapshot rule, calendar completeness labels, spot-return span
requirement, sign shares, and the cost worksheet constants.
"""
import os
import sys
from decimal import Decimal

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import compute_study0 as cs  # noqa: E402

H, W0, W1 = cs.H, cs.W0, cs.W1
PASS = 0
FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
        print("PASS %s" % name)
    else:
        FAIL += 1
        print("FAIL %s %s" % (name, detail))


# 1. type-7 quantiles -------------------------------------------------------
q = cs.quantile_type7
check("q7 median [1,2,3,4] = 2.5", q([1.0, 2.0, 3.0, 4.0], 0.5) == 2.5)
check("q7 p25 [1,2,3,4] = 1.75", q([1.0, 2.0, 3.0, 4.0], 0.25) == 1.75)
check("q7 p0 = min", q([1.0, 2.0, 3.0, 4.0], 0.0) == 1.0)
check("q7 p100 = max", q([1.0, 2.0, 3.0, 4.0], 1.0) == 4.0)
check("q7 single element", q([7.0], 0.95) == 7.0)
check("q7 p95 [0..19] = 18.05", abs(q([float(i) for i in range(20)], 0.95) - 18.05) < 1e-12)

# 2. D3 mapping, jitter, duplicates ----------------------------------------
recs = [
    {"fundingRate": "0.0000125", "premium": "0.0001", "time": W0},            # settles pre-window bucket W0-H: excluded
    {"fundingRate": "-0.0000063", "premium": "-0.0002", "time": W0 + H + 65_000},  # jitter 65s -> bucket W0
    {"fundingRate": "-0.0000063", "premium": "-0.0002", "time": W0 + H + 65_000},  # identical duplicate
    {"fundingRate": "0.0000125", "premium": "0.0003", "time": W1 + H},        # 2026-11-01T00:00 settlement -> final bucket W1
]
b, c = cs.map_funding(recs, label="FIX")
check("D3: settlement t maps to bucket floor_hour(t)-1h", set(b) == {W0, W1},
      "got %r" % sorted(b))
check("D3: pre-window payment excluded, boundary settlement included",
      b[W1] == Decimal("0.0000125") and b[W0] == Decimal("-0.0000063"))
check("jitter census", c["jitter_ms_max"] == 65_000 and c["jitter_ms_over_60s"] == 2)
check("identical duplicate deduplicated and counted",
      c["identical_duplicates"] == 1 and c["records"] == 4)
try:
    cs.map_funding(recs + [{"fundingRate": "0.9", "premium": "0", "time": W0 + H}], "FIX")
    check("conflicting duplicate aborts", False)
except SystemExit:
    check("conflicting duplicate aborts", True)

# 3. negative runs ----------------------------------------------------------
D1, M1 = Decimal("1"), Decimal("-1")
runs, s = cs.negative_runs({W0: D1, W0 + H: M1, W0 + 2 * H: M1, W0 + 3 * H: D1})
check("run A: one completed run, duration 2",
      len(runs) == 1 and runs[0]["completed"] and runs[0]["duration_h"] == 2
      and runs[0]["cumulative_funding_exact"] == "-2" and s["completed_count"] == 1)

runs, s = cs.negative_runs({W0: M1, W0 + H: D1})
check("run B: window-start run censored",
      len(runs) == 1 and not runs[0]["completed"] and runs[0]["censoring"] == "window-boundary")

runs, s = cs.negative_runs({W0: D1, W0 + H: M1, W0 + 3 * H: D1})  # gap at W0+2H
check("run C: gap-adjacent run censored",
      len(runs) == 1 and not runs[0]["completed"] and runs[0]["censoring"] == "gap-adjacent")

runs, s = cs.negative_runs({W0: D1, W0 + H: M1, W0 + 2 * H: Decimal("0"),
                            W0 + 3 * H: M1, W0 + 4 * H: D1})
check("run D: zero breaks a run; two completed runs of duration 1",
      len(runs) == 2 and all(r["completed"] and r["duration_h"] == 1 for r in runs))

runs, s = cs.negative_runs({W1 - H: D1, W1: M1})
check("run E: window-end run censored",
      len(runs) == 1 and runs[0]["censoring"] == "window-boundary")

# 4. Amendment A2 bounded snapshot rule -------------------------------------
day = 24 * H
t0 = W0 + 23 * H + 30 * 60_000          # day0 23:30
r, seg0, cov = cs.derive_reserve([(t0, Decimal("2")), (t0 + day, Decimal("3"))], None)
check("A2: applies from first boundary strictly after ts; scope0 derived",
      seg0 == W0 + day and min(r) == W0 + day)
day1 = [W0 + day + i * H for i in range(24)]
day2 = [W0 + 2 * day + i * H for i in range(24)]
check("A2: snapshot covers exactly 24 buckets to the next snapshot",
      all(r.get(x) == Decimal("2") for x in day1) and all(r.get(x) == Decimal("3") for x in day2)
      and len(r) == 48)

r, seg0, cov = cs.derive_reserve([(t0, Decimal("2")), (t0 + 2 * day, Decimal("3"))], None)
check("A2: missing snapshot day stays a gap (24-bucket cap, no indefinite carry)",
      all(x not in r for x in day2) and len(r) == 48 and cov["gaps"] == cov["expected"] - 48)

r, seg0, cov = cs.derive_reserve([(W0 + day, Decimal("2"))], None)
check("A2: snapshot exactly on an hour boundary applies strictly after it",
      min(r) == W0 + day + H and len(r) == 24)

# 5. calendar completeness --------------------------------------------------
jul0 = W0 + 192 * H                      # 2023-07-01T00:00Z (192 h after window start)
full_july = {jul0 + i * H: Decimal("0.001") for i in range(744)}
rows = cs.calendar_table(full_july, cs.iter_months())
jun = next(x for x in rows if x["period"] == "2023-06")
jul = next(x for x in rows if x["period"] == "2023-07")
aug = next(x for x in rows if x["period"] == "2023-08")
check("month: fully observed month is COMPLETE with total",
      jul["status"] == "COMPLETE" and jul["total_if_complete"] == "0.744"
      and jul["observed_subtotal"] == "0.744")
check("month: June 2023 window-partial by construction",
      jun["status"].startswith("INCOMPLETE") and "window-partial" in jun["status"]
      and jun["period_hours"] == 720 and jun["in_window_hours"] == 192)
check("month: unobserved month INCOMPLETE (missing-data), subtotal 0",
      aug["status"] == "INCOMPLETE (missing-data)" and aug["observed_subtotal"] == "0")
partial = dict(full_july)
del partial[jul0 + 100 * H]
jul_p = next(x for x in cs.calendar_table(partial, cs.iter_months()) if x["period"] == "2023-07")
check("month: one missing hour makes it INCOMPLETE; no total shown",
      jul_p["status"] == "INCOMPLETE (missing-data)" and jul_p["total_if_complete"] is None
      and jul_p["observed_subtotal"] == "0.743")
check("month iterator spans 2023-06..2026-10 (41 months)",
      sum(1 for _ in cs.iter_months()) == 41)

# 6. spot-return span requirement -------------------------------------------
closes = {W0 + i * H: Decimal(100 + i) for i in range(61)}
del closes[W0 + 5 * H]
r1 = cs.spot_risk(closes, 1)
r24 = cs.spot_risk(closes, 24)
check("spot k=1: returns dropped only where an endpoint is missing",
      r1["n_returns"] == 58)
check("spot k=24: any missing close inside the span invalidates the return",
      r24["n_returns"] == 31)
two = cs.spot_risk({W0: Decimal("100"), W0 + H: Decimal("110")}, 1)
check("spot: known return value 0.10 with end-bucket timestamp",
      two["worst_up"]["return"] == "0.10000000" and two["worst_up"]["end_bucket"] == cs.iso(W0 + H))

# 7. sign shares and exact sums ---------------------------------------------
st = cs.funding_stats({W0: Decimal("0.001"), W0 + H: Decimal("0"), W0 + 2 * H: Decimal("-0.002")})
check("funding stats: exact decimal sum", st["sum_per_dollar_exact"] == "-0.001")
check("funding stats: arithmetic annualization 8760*S/n",
      Decimal(st["arithmetic_annualized_rate_exact"]) == Decimal("-2.92"))
check("funding stats: three-way sign shares with exact zero",
      st["share_positive"] == st["share_zero"] == st["share_negative"] == "0.33333333")
check("funding stats: exact min/max strings", st["min"] == "-0.002" and st["max"] == "0.001")

# 8. cost worksheet constants ------------------------------------------------
cw = cs.cost_worksheet()
vals = {(r["case"], r["holding_days"]): (r["roundtrip_bps"], r["annualized_drag_bps"])
        for r in cw["rows"]}
check("cost: base 29 bps; 352.83 / 117.61 / 29.00",
      vals[("base", 30)] == ("29.00", "352.83") and vals[("base", 90)] == ("29.00", "117.61")
      and vals[("base", 365)] == ("29.00", "29.00"))
check("cost: doubled 58 bps; 705.67 / 235.22 / 58.00",
      vals[("doubled (sole sensitivity)", 30)] == ("58.00", "705.67")
      and vals[("doubled (sole sensitivity)", 90)] == ("58.00", "235.22")
      and vals[("doubled (sole sensitivity)", 365)] == ("58.00", "58.00"))

# ---------------------------------------------------------------------------
print("fixtures: %d passed, %d failed" % (PASS, FAIL))
sys.exit(1 if FAIL else 0)
