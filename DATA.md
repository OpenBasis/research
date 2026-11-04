# Study 0 — rebuilding the input data

The raw captures are withheld pending legal review of third-party
redistribution (see `PUBLICATION-NOTES.md`), but every input series is public
and the study pins exactly what it used.

1. **Pins:** `data/MANIFEST.json` records, for each of the 349 raw files, its
   source endpoint, retrieval record and SHA256. `data/COVERAGE.json` records
   the observed/expected hour censuses, duplicates and gaps.
2. **Re-fetch:** the sources are the Hyperliquid public funding API
   (`fundingHistory`), Coinbase Exchange hourly candles, and the DefiLlama
   daily pool series used under the sealed exception (Amendment A1), at the
   endpoints named in the manifest. A re-fetch that matches a pinned hash is
   byte-identical to what the study ran on.
3. **Rebuild:** `study/src/compute_study0.py` rebuilds every result
   deterministically from `data/raw/` (`env TZ=UTC PYTHONHASHSEED=0`, pinned
   interpreter in `study/ENVIRONMENT.md`); `study/src/make_figures.py`
   regenerates the figures byte-identically; `study/src/test_fixtures.py`
   runs the 34 synthetic fixtures. The independent audit scripts
   (`audit/independent_round1.py`, `audit/compare_round1.py`) recompute the
   headline quantities from the raw files without importing the builder's
   aggregation code.

**Caveats, stated plainly:**

- Live sources can revise or trim history, so a fresh fetch may not match
  every pin. A mismatch tells you the source changed, not that the study did:
  the pinned hash still identifies exactly what the study used.
- The DefiLlama reserve series is aggregator evidence used under a sealed,
  disclosed exception, expanded to hours under the sealed bounded
  daily-snapshot rule; it is a modeled approximation, not observed hourly
  returns, and is labeled that way everywhere.
- Hyperliquid's `fundingHistory` depth of history and Coinbase's candle
  availability at the two documented 5-hour gaps are as observed at retrieval
  (2026-11-01); the gaps were absent at source and are disclosed, never
  filled.
