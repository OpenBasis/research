# Study 0 — Execution Environment and Rebuild Commands (decision D4)

**Host (mechanically verified 2026-11-01, pre-seal):** macOS 26.6.2 (build 25G83), Darwin arm64.
**Interpreter (pinned, explicit path):** `/opt/homebrew/bin/python3.13` — CPython **3.13.15** (Homebrew). The host's `/usr/bin/python3` (3.9.6) is **not** used; no PATH-resolved `python3` appears in any rebuild command.
**Dependencies:** Python standard library only. No third-party packages; nothing to install.
**Determinism:** every command runs with `TZ=UTC PYTHONHASHSEED=0` from the repository root; deterministic outputs use sorted JSON keys, fixed numeric formats (funding rates `%.12f`, returns `%.8f`, bps `%.2f`, exact decimals as strings), `\n` line endings, and contain no timestamps.

**Division of labor (sealed DESIGN §13, Amendment A4):** the builder authors scripts, rules, fixtures and output specifications; the mechanical host coordinator executes the exact commands below on this host without editing substantive code, and returns logs and output hashes as repository artifacts, which the builder inspects. The builder never computes Study 0 results in its cloud shell, and no cloud run is ever described as Mac reproduction.

## Rebuild commands (run from the repository root, in this order)

```
# 1. Synthetic fixtures (signs, quantiles, mapping, censoring, A2 rule, completeness)
env TZ=UTC PYTHONHASHSEED=0 /opt/homebrew/bin/python3.13 study/src/test_fixtures.py

# 2. Sealed analysis pipeline (reads data/raw/** and data/COVERAGE.json; writes
#    reports/results_study0.json and reports/tables/*.md)
env TZ=UTC PYTHONHASHSEED=0 /opt/homebrew/bin/python3.13 study/src/compute_study0.py

# 3. Clean-directory reproduction and byte comparison
env TZ=UTC PYTHONHASHSEED=0 /opt/homebrew/bin/python3.13 study/src/compute_study0.py --out reports/repro_check
diff -r reports/tables reports/repro_check/tables
shasum -a 256 reports/results_study0.json reports/repro_check/results_study0.json

# 4. Independent recomputation (no shared functions with the pipeline): full-window
#    funding sums/annualized rates and the 29 bps worksheet, compared to the
#    pipeline's results JSON
env TZ=UTC PYTHONHASHSEED=0 /opt/homebrew/bin/python3.13 study/src/independent_check.py
```

**Expected inputs:** `data/raw/hyperliquid/{ETH,BTC}/page_*.json`, `data/raw/coinbase/{ETH-USD,BTC-USD}/page_*.json`, `data/raw/defillama/chart_{native_usdc,usdc_e}.json`, `data/COVERAGE.json` (cross-check target). All frozen by `data/MANIFEST.json`.
**Expected outputs:** `reports/results_study0.json`, `reports/tables/T01…T11*.md`, `reports/repro_check/**` (step 3 only). Every command exits non-zero on any failed internal check (conflicting duplicates, COVERAGE mismatch, fixture failure, reproduction or recomputation mismatch).

The reproduction claim is scoped to this pinned environment only.
