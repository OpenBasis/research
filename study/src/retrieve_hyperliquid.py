#!/usr/bin/env python3
"""Study 0 - Hyperliquid fundingHistory retrieval (raw pages pinned verbatim).

Retrieval span: payments 2023-06-23T00:00:00Z .. 2026-11-01T00:00:00Z inclusive.
(The 2026-11-01T00:00:00Z settlement is boundary evidence for the final window
bucket 2026-10-31T23:00 under the sealed t-1h mapping; it does not extend the
study window.) Resumable: continues from the per-coin page log.
"""
import hashlib, json, os, sys, time, urllib.request

URL = "https://api.hyperliquid.xyz/info"
START = 1687478400000           # 2023-06-23T00:00:00Z (ms)
END   = 1793491260000           # 2026-11-01T00:01:00Z (ms): settlement timestamps
                                # carry small positive jitter past the hour (e.g. +44ms),
                                # so the bound sits 60s past the required final
                                # 2026-11-01T00:00:00Z boundary settlement.
OUT   = "data/raw/hyperliquid"

def post(body: bytes) -> bytes:
    req = urllib.request.Request(URL, data=body,
        headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()

def run(coin: str) -> str:
    d = os.path.join(OUT, coin); os.makedirs(d, exist_ok=True)
    log_path = os.path.join(OUT, f"{coin}_pages.ndjson")
    cur, page = START, 0
    if os.path.exists(log_path):
        with open(log_path) as f:
            lines = [json.loads(l) for l in f if l.strip()]
        if lines:
            last = lines[-1]
            if last.get("complete") and last["t_max"] >= 1793491200000:
                return "already-complete"
            # resume (also reopens a run marked complete under the earlier
            # end bound that missed the jittered boundary settlement)
            cur, page = last["t_max"] + 1, last["page"] + 1
    while True:
        body = json.dumps({"type": "fundingHistory", "coin": coin,
                           "startTime": cur, "endTime": END}).encode()
        t_utc = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        raw = post(body)
        rec = json.loads(raw)
        if not isinstance(rec, list):
            raise SystemExit(f"UNEXPECTED RESPONSE for {coin}: {raw[:200]!r}")
        fname = os.path.join(d, f"page_{page:04d}.json")
        with open(fname, "wb") as f: f.write(raw)
        n = len(rec)
        t_min = min((r["time"] for r in rec), default=None)
        t_max = max((r["time"] for r in rec), default=None)
        complete = (n < 500) or (t_max is not None and t_max >= END)
        entry = {"page": page, "request": json.loads(body), "retrieval_utc": t_utc,
                 "sha256": hashlib.sha256(raw).hexdigest(), "file": fname,
                 "n_records": n, "t_min": t_min, "t_max": t_max,
                 "complete": complete, "empty_stop": n == 0}
        with open(log_path, "a") as f: f.write(json.dumps(entry) + "\n")
        if n == 0:
            return f"EMPTY-RESPONSE-STOP at startTime={cur} (page {page})"
        if complete:
            return f"complete at page {page}, t_max={t_max}"
        cur, page = t_max + 1, page + 1
        time.sleep(0.15)

if __name__ == "__main__":
    for coin in sys.argv[1:] or ["ETH", "BTC"]:
        print(coin, "->", run(coin))
