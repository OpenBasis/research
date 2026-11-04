# COMMIT REQUEST 003 — RESULTS, REPORT, RUN RECORDS (third commit)

**From:** BUILDER (no Git commands run; Amendment A4 host-Git mechanical protocol)
**Written:** 2026-11-02 UTC
**Boundary:** host-computed results and run records, the public study document, the internal
V1 matrix, and audit-trail files. Parent must be commit `9a6212ac726ebd93efec4aff47e0778deb16cfd0`.

## Suggested commit message

    Study 0: results, run records, public study, internal V1 matrix

## Pre-commit verification for the coordinator

1. HEAD is `9a6212ac…cfd0`; `DESIGN.md` still hashes to `b4f91118…9c06` and is not restaged.
2. Stage exactly the 36 paths below; every byte count and SHA256 must match. Note:
   `study/CHANGELOG.md` is a MODIFIED tracked file (new version below); all others are new.
   `reports/results_study0.json`, `reports/tables/**`, `reports/repro_check/**` and the four run
   logs are host-produced bytes from receipt 003 — their hashes below restate the receipt's values.
3. Please DELETE `study/src/__pycache__/` (host-run side effect; the builder cannot delete).
   It is covered by the new `.gitignore` if it regenerates. Do not stage it.
4. After staging, the only remaining untracked path must be
   `study/commit_requests/COMMIT_REQUEST_003_RESULTS_REPORT.md` (this file; queued for the next
   boundary). Anything else is unexpected: report, do not stage.

## After committing — host execution request (figures; sealed DESIGN §7/D6, §13/A4)

Run from the repository root:

```
env TZ=UTC PYTHONHASHSEED=0 /opt/homebrew/bin/python3.13 study/src/make_figures.py \
    > study/run_logs/RUN_005_figures.log 2>&1
```

Inputs: `data/raw/hyperliquid/**`, `reports/results_study0.json`, committed `study/src/compute_study0.py`.
Expected outputs: `reports/figures/F1_funding_hourly.svg`, `reports/figures/F2_monthly_totals.svg`,
and the log (the script prints each figure's byte count and SHA256 and exits non-zero on any
inconsistency with the committed results). Report back: exit status, the log, and both figures'
sizes and SHA256 values. The builder then inspects the figures and issues commit request 004
(figures, figure log, round-1 submission note). Do not edit or re-run on failure; report it.

## Paths to stage and commit — exactly 36

| path | bytes | sha256 |
|---|---|---|
| `.gitignore` | 23 | `9addeec56619685bab330ff2184db9f205a1b4628f551ededcb97800b269ca3e` |
| `reports/STUDY_0.md` | 17910 | `7d9ff2e47c5ce08b2578dc10fe5acfea101ae3b7b0f969fdd45a6fa85efa6e6b` |
| `reports/results_study0.json` | 402590 | `f425e2e73b9069f2c8c6101376df02295d44db631cb208f7c0d94f57c6859788` |
| `reports/tables/T01_series_inventory.md` | 1375 | `f467c2e419bfae0154ebe9a78112923e19cc464cb80e00138cb3241fe89a75ba` |
| `reports/tables/T02_funding_stats.md` | 828 | `e3b0be03e6d4dd59ff830e64d187f6d44fb2254fc148fcf3d98da8787176fa9b` |
| `reports/tables/T03_monthly_ETH.md` | 3437 | `87230f8938cbd261cd3fcf5b8ac8151d2c1cb21f6606f8a4a11457ed63d0bbab` |
| `reports/tables/T04_monthly_BTC.md` | 3437 | `37378914870788ef3ac09535b4041e3dc31ebe8353d4b9aae6bead261b4b58c9` |
| `reports/tables/T05_yearly.md` | 1051 | `91c7e6e3264f3307fb994673ac4f6addf9c54279c873784ff54033288aff8efc` |
| `reports/tables/T06_runs_summary.md` | 569 | `e5f30e78a6e9a3488f9a8c157e5feb95abbc5496471709d624cd0038bf6fb39f` |
| `reports/tables/T07_runs_listing.md` | 134202 | `85ab4ce9f886872f5bbd6aa61f12284c1d1bec5b9d967da04a5f9aa385a87ff5` |
| `reports/tables/T08_spot_risk.md` | 756 | `188da829f76f9b70b349cdb266d0dfe95da882b53e5e696d6c410c47d6b093ee` |
| `reports/tables/T09_cost_worksheet.md` | 988 | `3da4d71d1603deeafb6989978e829ea50540a503c7f0ca15c16014c0732e0e17` |
| `reports/tables/T10_reserve.md` | 611 | `1771bdeb254aabc1242ab1c1ae733231c84d27970cb5a81ac6caad0f8cef6ade` |
| `reports/tables/T11_capital_bridge.md` | 676 | `07e65ad5b9d23cd9947036d72f2da470c84a1804702e9a4d6197cca7c5d9eae3` |
| `reports/repro_check/results_study0.json` | 402590 | `f425e2e73b9069f2c8c6101376df02295d44db631cb208f7c0d94f57c6859788` |
| `reports/repro_check/tables/T01_series_inventory.md` | 1375 | `f467c2e419bfae0154ebe9a78112923e19cc464cb80e00138cb3241fe89a75ba` |
| `reports/repro_check/tables/T02_funding_stats.md` | 828 | `e3b0be03e6d4dd59ff830e64d187f6d44fb2254fc148fcf3d98da8787176fa9b` |
| `reports/repro_check/tables/T03_monthly_ETH.md` | 3437 | `87230f8938cbd261cd3fcf5b8ac8151d2c1cb21f6606f8a4a11457ed63d0bbab` |
| `reports/repro_check/tables/T04_monthly_BTC.md` | 3437 | `37378914870788ef3ac09535b4041e3dc31ebe8353d4b9aae6bead261b4b58c9` |
| `reports/repro_check/tables/T05_yearly.md` | 1051 | `91c7e6e3264f3307fb994673ac4f6addf9c54279c873784ff54033288aff8efc` |
| `reports/repro_check/tables/T06_runs_summary.md` | 569 | `e5f30e78a6e9a3488f9a8c157e5feb95abbc5496471709d624cd0038bf6fb39f` |
| `reports/repro_check/tables/T07_runs_listing.md` | 134202 | `85ab4ce9f886872f5bbd6aa61f12284c1d1bec5b9d967da04a5f9aa385a87ff5` |
| `reports/repro_check/tables/T08_spot_risk.md` | 756 | `188da829f76f9b70b349cdb266d0dfe95da882b53e5e696d6c410c47d6b093ee` |
| `reports/repro_check/tables/T09_cost_worksheet.md` | 988 | `3da4d71d1603deeafb6989978e829ea50540a503c7f0ca15c16014c0732e0e17` |
| `reports/repro_check/tables/T10_reserve.md` | 611 | `1771bdeb254aabc1242ab1c1ae733231c84d27970cb5a81ac6caad0f8cef6ade` |
| `reports/repro_check/tables/T11_capital_bridge.md` | 676 | `07e65ad5b9d23cd9947036d72f2da470c84a1804702e9a4d6197cca7c5d9eae3` |
| `study/run_logs/RUN_001_fixtures.log` | 1777 | `90eadc3bf7aa01aaecd39903004c845fb91977d81274211f42275e61e703d9f6` |
| `study/run_logs/RUN_002_pipeline.log` | 238 | `bed93c2906b84d6b3586750438269f092092a8378e96b848263ab7977f9866ac` |
| `study/run_logs/RUN_003_repro.log` | 450 | `68b5754288c25c2d7f49819da14e2efab506cfecc4768f77dafbacb7842a3f76` |
| `study/run_logs/RUN_004_independent.log` | 527 | `144b373fabd48f525703aeba5466ec651c7a30a978a0ee8dacf76f8db34f7e1a` |
| `study/host_receipts/HOST_RECEIPT_002_INPUTS_SPEC.md` | 1323 | `bec3e55b94ca858ee45e7abf4466b5e66bf3a97b332945d00700f0b75c718f49` |
| `study/host_receipts/HOST_RECEIPT_003_EXECUTION.md` | 4962 | `07b5f7f77ee9ee4226962b1634281336311ba97e955a580b52b4085652b7e6d8` |
| `study/commit_requests/COMMIT_REQUEST_002_INPUTS_SPEC.md` | 49976 | `9bab2e532aae1abf2ef1e76c5aef4c2176ad298fbff2a744312328e3b365874e` |
| `study/CHANGELOG.md` | 7557 | `f98a2e5cf83eaf0152ce771c4fc251cfb15a19f71d0195b2f63e768ae095210c` |
| `study/src/make_figures.py` | 9768 | `a9cf8ca15b0dba6ce679ea880c7675043e9f4ae954f30bbe0c27df1409294609` |
| `study/V1_CONSISTENCY_T12.md` | 5109 | `f603a8073a80b386ab211217623f5d2cb010c0cf916159e042cb3c31d9a6cc81` |

End of request. The builder stops at this boundary.
