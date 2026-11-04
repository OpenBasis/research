#!/usr/bin/env python3
"""Study 0 - Coinbase Exchange hourly candles retrieval (raw pages pinned verbatim).

Window buckets 2023-06-23T00:00:00Z .. 2026-10-31T23:00:00Z (bucket starts, UTC).
Chunks of 300 hourly buckets per request (venue page limit). Responses are pinned
exactly as returned (newest-first, may include out-of-range candles; trimming
happens only in processing). Resumable from the per-product page log.
"""
import hashlib, json, os, sys, time, urllib.request

BASE = "https://api.exchange.coinbase.com/products/{}/candles"
START = 1687478400              # 2023-06-23T00:00:00Z (s)
LAST  = 1793487600              # 2026-10-31T23:00:00Z (s), last bucket start
OUT   = "data/raw/coinbase"
UA    = "openbasis-study0-retrieval/1.0"

def iso(t): return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(t))

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503) and attempt < 4:
                time.sleep(2.0 * (attempt + 1)); continue
            raise
    raise RuntimeError("unreachable")

def run(product: str) -> str:
    d = os.path.join(OUT, product); os.makedirs(d, exist_ok=True)
    log_path = os.path.join(OUT, f"{product}_pages.ndjson")
    page = 0
    if os.path.exists(log_path):
        with open(log_path) as f:
            lines = [json.loads(l) for l in f if l.strip()]
        done = {l["page"] for l in lines}
        page = max(done) + 1 if done else 0
    while True:
        c0 = START + page * 300 * 3600
        if c0 > LAST: return f"complete, pages 0..{page-1}"
        c1 = min(c0 + 299 * 3600, LAST)
        url = f"{BASE.format(product)}?granularity=3600&start={iso(c0)}&end={iso(c1)}"
        t_utc = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        raw = get(url)
        rec = json.loads(raw)
        if not isinstance(rec, list):
            raise SystemExit(f"UNEXPECTED RESPONSE {product} page {page}: {raw[:200]!r}")
        fname = os.path.join(d, f"page_{page:04d}.json")
        with open(fname, "wb") as f: f.write(raw)
        ts = [r[0] for r in rec]
        entry = {"page": page, "url": url, "retrieval_utc": t_utc,
                 "sha256": hashlib.sha256(raw).hexdigest(), "file": fname,
                 "n_records": len(rec),
                 "t_min": min(ts, default=None), "t_max": max(ts, default=None),
                 "chunk": [c0, c1]}
        with open(log_path, "a") as f: f.write(json.dumps(entry) + "\n")
        page += 1
        time.sleep(0.35)

if __name__ == "__main__":
    for prod in sys.argv[1:] or ["ETH-USD", "BTC-USD"]:
        print(prod, "->", run(prod))
