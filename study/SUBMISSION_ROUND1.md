# Study 0 — Round 1 Submission (builder → auditor)

**Submitted commit:** the commit created from `study/commit_requests/COMMIT_REQUEST_004_SUBMISSION.md` — the repository HEAD whose hash the host coordinator records in `study/host_receipts/HOST_RECEIPT_005_SUBMISSION.md` (this file is inside that commit, so it identifies it by construction).
**Commit chain:** seal `9d3ed18144d4cebc2b3c511ad596f3496e833be2` (DESIGN.md alone, 2026-11-01T20:47:51Z) → inputs/spec `9a6212ac726ebd93efec4aff47e0778deb16cfd0` → results/report `7dba8b654ab955b3348a96d249512c0571ba8960` → this submission.
**Round status:** round 1 of a maximum 5. Zero verdicts exist. Only the auditor's written verdict ends the round.

## 1. Deliverables inventory

| Deliverable | Path |
|---|---|
| Sealed design | `DESIGN.md` (SHA256 `b4f91118…9c06`; seal record `study/SEAL_RECORD.md`) |
| Public study incl. data/assumption appendix and Audit Process | `reports/STUDY_0.md` |
| Figures F1, F2 (deterministic SVG, host-generated) | `reports/figures/F1_funding_hourly.svg`, `reports/figures/F2_monthly_totals.svg` |
| Deterministic tables T1–T11 | `reports/tables/` |
| Machine results | `reports/results_study0.json` (= `reports/repro_check/results_study0.json`, byte-identical) |
| Frozen rules | `frozen_rules/study0.json`, `frozen_rules/STUDY0_RULES.md` |
| Pinned inputs + manifests | `data/` (`MANIFEST.json` 349 files, `COVERAGE.json`, raw pulls, V1 copy) |
| Analysis / verification code | `study/src/compute_study0.py`, `test_fixtures.py`, `independent_check.py`, `make_figures.py` (+ retrieval/inventory scripts) |
| Internal V1 matrix (T12; internal per D6) | `study/V1_CONSISTENCY_T12.md` |
| Environment pin + rebuild commands | `study/ENVIRONMENT.md` |
| Changelog | `study/CHANGELOG.md` |
| Run records + mechanical receipts | `study/run_logs/RUN_001…005*.log`, `study/host_receipts/HOST_RECEIPT_001…005*.md`, `study/commit_requests/` |

## 2. Builder verification record (duty → evidence)

1. **Full reproduction from frozen inputs in a clean output directory** — host-executed `compute_study0.py --out reports/repro_check` on the pinned environment: `diff -r` clean, results JSON byte-identical (`f425e2e7…9788` both). Evidence: `study/run_logs/RUN_003_repro.log`, `HOST_RECEIPT_003_EXECUTION.md`.
2. **Synthetic fixtures (signs, rates, missingness, run censoring, D3 mapping, A2 rule, completeness, quantiles)** — 34/34 PASS, host-executed: `RUN_001_fixtures.log`. (The log's leading `ABORT` line is the deliberately caught conflicting-duplicate fixture.)
3. **Independent recomputation without production aggregation functions** — `independent_check.py` (exact rationals, separate code path): both assets' full-window sums exact-equal, annualized rates within decimal-context tolerance, all six 29 bps worksheet rows equal. Host-executed: `RUN_004_independent.log`.
4. **Source-record checks of boundary months (absence documented, nothing substituted)** — builder records-presence check (coverage metadata only, no rate statistics; builder shell, re-runnable anywhere from the frozen raw files):
   - Funding, both assets: the 3 missing buckets' settlement records (2023-07-02T20:00Z, 2023-08-23T20:00Z, 2024-08-15T13:00Z) are **absent at source with both neighboring settlements present**; earliest complete calendar month **2023-09**, latest **2026-10**, 37 complete months each (41 window months − June 2023 window-partial − the three one-hour-short months).
   - Reserve segments (A2-derived coverage): USDC.e first/last complete months **2023-08 / 2026-08** (27 complete; Sep–Oct 2026 have derived gaps); native **2023-07 / 2026-09** (32 complete). Source snapshots present in each boundary month (31/31 USDC.e, 31/30 native).
5. **Source-to-output trace of every public quantitative claim** — every number in `reports/STUDY_0.md` is a committed table value or a fixed-format conversion of one (percent = value×100; bp/h = value×1e4; rounded to displayed precision): §1/§4 funding statistics → T2; §4 calendar figures → T3/T4/T5; §5 runs → T6/T7; §6 spot → T8; §7 costs → T9 (sealed constants, DESIGN §9); §8 reserve → T10/T11; §3 coverage → T1/`data/COVERAGE.json`; figures → `RUN_005_figures.log` hashes. Tables trace to `data/raw/**` via `compute_study0.py` under `data/MANIFEST.json` hashes.
6. **V1 consistency recheck** — `study/V1_CONSISTENCY_T12.md`: 16 CONSISTENT, 1 DISCLOSED-DIFFERENCE (fixed vs dynamic window end, sealed), 1 DIRECTOR-RESOLVED (Amendment A3 apyBase/apy disposition). No unresolved conflict; nothing rerun.
7. **E7 scan of every public artifact** (`reports/STUDY_0.md`, both figures, all tables) — wordlist scan; all hits adjudicated benign: "Aave v3" (protocol name) and explicit scope negations ("runs no strategy backtest, builds no trading engine"). No prototype/implementation/codebase/build reference, no post-study result, no coming-soon or later-work promise.
8. **Figure inspection** — builder visually inspected rendered F1/F2 against T2–T4 (extremes, compression, INCOMPLETE markers, negative months); staged bytes re-hashed equal to committed hashes.

## 3. S1–S9 evidence map

| Criterion | Primary evidence |
|---|---|
| S1 seal + prior-exposure disclosure | Seal commit `9d3ed181…` (DESIGN.md alone, before any result); `study/SEAL_RECORD.md`; DESIGN §12 disclosure (incl. prior-incarnation seal `86a5dc9c…` and V1 exposure) |
| S2 provenance/hashes/units/coverage | `data/MANIFEST.json` (349 files, builder re-verified), `data/COVERAGE.json` = pipeline censuses (RUN_002 cross-check PASS), DESIGN §5 conventions, T1 |
| S3 funding/run/spot completeness & correctness | T2–T8, `results_study0.json`, fixtures RUN_001, independent RUN_004 |
| S4 worksheets reconcile, no investable-net claim | T9/T10/T11; RUN_004 worksheet checks; report §§7–8 labels; no net-APY anywhere |
| S5 conclusions from evidence, adverse visible | report §10 ↔ §§4–8; negative months/runs and compression prominent (§1, §4, §5, F2) |
| S6 V1 consistency | `study/V1_CONSISTENCY_T12.md` + Amendment A3 record |
| S7 publication boundary | E7 scan record above; report ends at design conclusion (§10) |
| S8 audit trail | `study/CHANGELOG.md`, commit requests + host receipts chain, run logs; report §11 Audit Process (updated each round) |
| S9 reproducibility | RUN_003 byte-identical rebuild; `study/ENVIRONMENT.md`; hashes in receipts; this inventory |

## 4. Notes for the auditor

- **T02 hash prefix**: `T02_funding_stats.md`'s true SHA256 (`e3b0be03…76fa9b`) shares its first 2 bytes with the empty-input SHA256; the file is a complete 828-byte table and the receipt records the full correct hash. Documented in CHANGELOG; no defect.
- The withdrawn pre-commit DESIGN revision (`b07ad201…`, wrong environment pin) is disclosed in `study/SEAL_RECORD.md`; no commit was amended.
- `study/src/__pycache__/` is a host-run side effect, ignored via `.gitignore`, never staged.
- Reproduction and all result computation are host-executed on the pinned environment (DESIGN §13 / Amendment A4); builder-side activity was authoring, synthetic fixtures, byte inspection, and the coverage-metadata records checks in §2.4.

The builder hands off. Per protocol, the round ends only with the auditor's written verdict (`audit/findings_round1.md`, `audit/verdict_round1.md`); the builder will answer every finding.
