#!/bin/bash
# Study 0 — D1/D2 source-definition evidence retrieval (DefiLlama yield-server).
# Pins: current aave-v3 adapter, its commit history for the window, README, and
# the chart-serving handler. Each file hashed; log appended as TSV:
# retrieval_utc <TAB> sha256 <TAB> filename <TAB> url
set -u
DIR="data/raw/defillama_adapter_evidence"
LOG="$DIR/RETRIEVAL_LOG.tsv"
fetch () { # $1=url $2=outfile
  local u="$1" f="$DIR/$2" t
  t=$(date -u +%Y-%m-%dT%H:%M:%SZ)
  curl -sS -m 60 -o "$f" "$u" || { echo "FETCH_FAIL $u"; return 1; }
  printf '%s\t%s\t%s\t%s\n' "$t" "$(shasum -a 256 "$f" | cut -d' ' -f1)" "$2" "$u" >> "$LOG"
}
fetch "https://raw.githubusercontent.com/DefiLlama/yield-server/master/src/adaptors/aave-v3/index.js" "aave-v3_index_master.js"
fetch "https://api.github.com/repos/DefiLlama/yield-server/commits?path=src/adaptors/aave-v3/index.js&per_page=100&page=1" "commits_aave-v3_p1.json"
fetch "https://api.github.com/repos/DefiLlama/yield-server/commits?path=src/adaptors/aave-v3/index.js&per_page=100&page=2" "commits_aave-v3_p2.json"
fetch "https://raw.githubusercontent.com/DefiLlama/yield-server/master/README.md" "yield-server_README.md"
