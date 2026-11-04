#!/bin/bash
# Study 0 — DefiLlama reserve-rate retrieval (director decision D1).
# Pins: /pools (pool-identity evidence) and /chart/{pool} for the two sealed pools.
set -u
D="data/raw/defillama"
LOG="$D/RETRIEVAL_LOG.tsv"
fetch () { local u="$1" f="$D/$2" t; t=$(date -u +%Y-%m-%dT%H:%M:%SZ); curl -sS -m 120 -o "$f" "$u" || { echo "FETCH_FAIL $u"; return 1; }; printf '%s\t%s\t%s\t%s\n' "$t" "$(shasum -a 256 "$f" | cut -d' ' -f1)" "$2" "$u" >> "$LOG"; }
fetch "https://yields.llama.fi/pools" "pools_snapshot.json"
fetch "https://yields.llama.fi/chart/d9fa8e14-0447-4207-9ae8-7810199dfa1f" "chart_native_usdc.json"
fetch "https://yields.llama.fi/chart/7aab7b0f-01c1-4467-bc0d-77826d870f19" "chart_usdc_e.json"
