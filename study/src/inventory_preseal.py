#!/usr/bin/env python3
"""Study 0 - pre-seal coverage inventory. COVERAGE METADATA ONLY: counts,
timestamps, duplicates, gaps, unit check. No funding/return/rate statistics."""
import json, os, collections, datetime

H = 3600_000
W0 = 1687478400000            # 2023-06-23T00:00:00Z bucket start (ms)
W1 = 1793487600000            # 2026-10-31T23:00:00Z bucket start (ms)
NBUCKETS = (W1 - W0) // H + 1

def iso(ms): return datetime.datetime.utcfromtimestamp(ms/1000).strftime("%Y-%m-%dT%H:%MZ")

out = {"window": {"first_bucket": iso(W0), "last_bucket": iso(W1), "expected_buckets": NBUCKETS}}

# --- Hyperliquid ---
for coin in ["ETH", "BTC"]:
    recs = []
    d = f"data/raw/hyperliquid/{coin}"
    for fn in sorted(os.listdir(d)):
        recs += json.load(open(os.path.join(d, fn)))
    times = [r["time"] for r in recs]
    jitter = [t % H for t in times]
    by_hour = collections.defaultdict(list)
    for r in recs:
        by_hour[(r["time"] // H) * H].append((r["fundingRate"], r["premium"]))
    ident_dup = sum(len(v) - len(set(v)) for v in by_hour.values())
    confl_dup = sum(1 for v in by_hour.values() if len(set(v)) > 1)
    # D3 mapping: settlement hour h -> bucket h - 1h
    buckets = {h - H for h in by_hour}
    inw = {b for b in buckets if W0 <= b <= W1}
    missing = [b for b in range(W0, W1 + H, H) if b not in inw]
    rate_mode = collections.Counter(r["fundingRate"] for r in recs).most_common(3)
    out[f"hyperliquid_{coin}"] = {
        "records": len(recs), "unique_settlement_hours": len(by_hour),
        "payment_t_min": iso(min(times)), "payment_t_max": iso(max(times)),
        "jitter_ms_max": max(jitter), "jitter_ms_over_60s": sum(1 for j in jitter if j > 60000),
        "identical_duplicates": ident_dup, "conflicting_duplicates": confl_dup,
        "in_window_buckets_observed": len(inw), "expected": NBUCKETS,
        "missing_buckets": len(missing), "missing_list": [iso(b) for b in missing[:50]],
        "boundary_settlement_20261101T00_present": any(t // H * H == 1793491200000 for t in times),
        "pre_window_payment_20230623T00_present": any(t // H * H == 1687478400000 for t in times),
        "fundingRate_top3_exact_strings": rate_mode,
    }

# --- Coinbase ---
for prod in ["ETH-USD", "BTC-USD"]:
    cand = {}
    ident = confl = 0
    d = f"data/raw/coinbase/{prod}"
    for fn in sorted(os.listdir(d)):
        for row in json.load(open(os.path.join(d, fn))):
            t = row[0] * 1000
            if t in cand:
                if cand[t] == row: ident += 1
                else: confl += 1
            else: cand[t] = row
    inw = {t for t in cand if W0 <= t <= W1}
    missing = [b for b in range(W0, W1 + H, H) if b not in inw]
    runs = []
    for b in missing:
        if runs and b - runs[-1][1] == H: runs[-1][1] = b
        else: runs.append([b, b])
    out[f"coinbase_{prod}"] = {
        "unique_candles": len(cand), "identical_duplicates": ident,
        "conflicting_duplicates": confl, "in_window_observed": len(inw),
        "expected": NBUCKETS, "missing_buckets": len(missing),
        "missing_runs": [[iso(a), iso(b)] for a, b in runs[:40]],
        "out_of_window_candles": len(cand) - len(inw),
    }

# --- DefiLlama segments: derived hourly coverage under sealed bound rule ---
def boundary_after(ms):           # first hour boundary strictly after ms
    return (ms // H + 1) * H
for seg, f, scope0 in [("usdc_e", "data/raw/defillama/chart_usdc_e.json", W0),
                       ("native", "data/raw/defillama/chart_native_usdc.json", None)]:
    data = json.load(open(f))["data"]
    snaps = []
    for x in data:
        ts = datetime.datetime.fromisoformat(x["timestamp"].replace("Z", "+00:00"))
        snaps.append((int(ts.timestamp() * 1000), x["apyBase"], x.get("apyReward")))
    snaps.sort()
    seg0 = scope0 if scope0 is not None else boundary_after(snaps[0][0])
    covered = set()
    for i, (tms, base, rew) in enumerate(snaps):
        b0 = boundary_after(tms)
        b1 = b0 + 23 * H                      # ≤ 24 buckets (one documented cadence)
        if i + 1 < len(snaps):
            b1 = min(b1, boundary_after(snaps[i + 1][0]) - H)
        b = max(b0, seg0, W0)
        while b <= min(b1, W1):
            covered.add(b); b += H
    seg_expected = (W1 - max(seg0, W0)) // H + 1
    out[f"aave_{seg}"] = {
        "snapshots_total": len(snaps),
        "first_snapshot": iso(snaps[0][0]), "last_snapshot": iso(snaps[-1][0]),
        "segment_scope_first_bucket": iso(max(seg0, W0)),
        "derived_hourly_buckets_covered_in_window": len(covered),
        "segment_expected_buckets_in_window": seg_expected,
        "derived_gap_buckets": seg_expected - len(covered),
        "apyBase_null_in_scope": sum(1 for t, b, r in snaps if b is None),
        "apyReward_nonnull_days": sum(1 for t, b, r in snaps if r is not None),
    }

json.dump(out, open("data/COVERAGE.json", "w"), indent=1)
print(json.dumps(out, indent=1))
