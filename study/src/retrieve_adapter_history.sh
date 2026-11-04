#!/bin/bash
# Study 0 — adapter formula history: pin aave-v3/index.js at dated commits
# spanning the study window; append to the same retrieval log.
set -u
DIR="data/raw/defillama_adapter_evidence"
LOG="$DIR/RETRIEVAL_LOG.tsv"
SHAS="03b47a004293 3173abeb170b ce9bc01e61f9 7f1523db861f 4d3ff6cb4dd7 22cd411350b3 42ec40d6ddc6 395d7a1a6f21 3b22a52d483b 04bab22e688a a88b70c12f99 d78ab8ae6466 ae16804e6345 6387427c97c5"
for s in $SHAS; do
  u="https://raw.githubusercontent.com/DefiLlama/yield-server/$s/src/adaptors/aave-v3/index.js"
  f="$DIR/aave-v3_index_$s.js"
  t=$(date -u +%Y-%m-%dT%H:%M:%SZ)
  curl -sS -m 60 -o "$f" "$u" || { echo "FETCH_FAIL $s"; continue; }
  printf '%s\t%s\t%s\t%s\n' "$t" "$(shasum -a 256 "$f" | cut -d' ' -f1)" "$(basename "$f")" "$u" >> "$LOG"
done
