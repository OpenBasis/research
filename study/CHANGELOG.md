# Study 0 — CHANGELOG

All times UTC. Builder entries; the mechanical host coordinator performs all Git operations (Amendment A4).

## 2026-11-01 — pre-seal evidence assembly (permitted source-definition/manifest/hash/coverage work)

- Raw retrievals pinned 19:13–19:27 (Hyperliquid fundingHistory ETH/BTC incl. the 2026-11-01T00:00 boundary settlement; Coinbase hourly candles; DefiLlama pools snapshot and the two Aave v3 Arbitrum USDC pool charts; DefiLlama yield-server adapter evidence: master + 14 dated versions, commit history, README, serverless.yml, triggerAdaptor.js, controller_yield.js).
- Coverage inventory `data/COVERAGE.json` (metadata only; no funding/return/rate statistics) via `study/src/inventory_preseal.py`; manifest `data/MANIFEST.json` built 19:27:07 (349 files), independently re-verified by the builder with zero mismatches.
- Host coordinator byte-copied the external V1 seal source to `data/source_consistency/V1_DESIGN.md`; builder independently re-hashed it to the required SHA256 `8e5010…57e32`.
- Working prompts created under `study/prompts/working/` as byte-exact concatenations: original + A1–A2 (verbatim) + A3 (S6 rate-convention disposition) + A4 (host-Git protocol and fresh-restart authorization); mechanical checks in `study/prompts/working/PROMPT_COMPARISON.md` — all PASS, canonical S1–S9 byte-identical across both roles.
- DESIGN.md authored. A first revision (SHA256 `b07ad201…ed04`) was withdrawn before any commit on the coordinator's stop: it pinned the cloud builder shell instead of the approved Mac host environment (D4). §13 corrected; all pre-seal checks re-run; commit request replaced.

## 2026-11-01 20:47:51 — DESIGN SEALED

- `DESIGN.md` (SHA256 `b4f911…9c06`) committed ALONE as the repository's first commit `9d3ed18144d4cebc2b3c511ad596f3496e833be2` by the host coordinator; receipt `study/host_receipts/HOST_RECEIPT_001_DESIGN_SEAL.md`; builder verification and disclosure in `study/SEAL_RECORD.md`.

## 2026-11-01 — post-seal apparatus (no results computed yet)

- `study/SEAL_RECORD.md`; `frozen_rules/study0.json` + `frozen_rules/STUDY0_RULES.md`; `study/ENVIRONMENT.md` (pinned host: macOS 26.6.2 arm64, CPython 3.13.15 at `/opt/homebrew/bin/python3.13`; explicit-interpreter rebuild commands).
- Analysis apparatus authored: `study/src/compute_study0.py` (sealed pipeline: exact decimal sums, float64 distribution stats, type-7 quantiles, D3 mapping, A2 reserve rule, calendar completeness, negative-run censoring, COVERAGE cross-check, deterministic outputs, `--out` reproduction mode), `study/src/test_fixtures.py` (synthetic fixtures only), `study/src/independent_check.py` (independent recomputation of funding sums and the 29 bps worksheet; no shared functions).
- Builder dev-checked the fixtures on synthetic data in its authoring shell (syntax/logic only). Per sealed DESIGN §13/A4, no Study 0 result is computed outside the pinned host: all official runs (fixtures, pipeline, clean-directory reproduction, independent check) execute host-side; logs and hashes return as repository artifacts.
- Commit request 002 issued (`study/commit_requests/COMMIT_REQUEST_002_INPUTS_SPEC.md`): full evidence + spec + code set, every path with SHA256. Builder stopped at the boundary.

## 2026-11-01 21:02:39 — COMMIT 002 (inputs, evidence, frozen rules, analysis code)

- All 378 requested paths committed byte-exactly: commit `9a6212ac726ebd93efec4aff47e0778deb16cfd0`, parent = seal commit `9d3ed181…3be2`, tree `39332793…4aef6`; receipt `study/host_receipts/HOST_RECEIPT_002_INPUTS_SPEC.md` (SHA256 `bec3e55b…718f49`). Builder re-verified the receipt hash and the ref by read-only `.git` file inspection. No result-producing command was executed at this boundary.

## EXECUTION GATE — OPENED, THEN RESOLVED

- The host-run request embedded in commit request 002 initially awaited the director's approval to extend the mechanical host role beyond Git operations; the builder stopped with no result computation anywhere. The sealed DESIGN §13 / Amendment A4 already specified host-side execution, so the approval operationalized the sealed division without changing it.
- **Director approved** the mechanical host-execution handoff. The exact commands of commit request 002 ran unchanged on the pinned host (macOS 26.6.2 arm64, `/opt/homebrew/bin/python3.13` = 3.13.15, TZ=UTC, PYTHONHASHSEED=0); all exit statuses 0. Receipt: `study/host_receipts/HOST_RECEIPT_003_EXECUTION.md` (SHA256 `07b5f7f7…7e6d8`), logs under `study/run_logs/` (RUN_001…004).

## 2026-11-01/02 — FIRST RESULTS (host-computed), VERIFICATION, AND ANOMALY RESOLUTION

- Fixtures: 34/34 PASS (host). Pipeline: coverage census PASS; ETH 29,445 h, sum 0.4746588125/$1, annualized 0.1412128…; BTC 29,445 h, sum 0.4791731877/$1, annualized 0.1425559…. Reproduction: `diff -r` clean; primary and repro `results_study0.json` byte-identical (`f425e2e7…9788`). Independent recomputation (exact rationals, separate code path): all PASS.
- **Hash-anomaly inspection (resolved, no defect):** the relayed execution report abbreviated `T02_funding_stats.md`'s SHA256 as "e3b0be03…b855", pattern-matching the empty-input SHA256 (`e3b0c442…b855`). Builder inspected the repository bytes: the file is a complete, pure-ASCII 828-byte table; `shasum` and Python `hashlib` independently return `e3b0be03e6d4dd59ff830e64d187f6d44fb2254fc148fcf3d98da8787176fa9b`, which is exactly the full hash recorded in HOST_RECEIPT_003. Only the 2-byte prefix coincides with the empty-input hash (a ~1/65,536 event); the "…b855" tail in the chat relay was a transcription slip. Repository, receipt and recomputed hashes agree; file content verified correct; no code, data, or design issue.
- Builder substantive review of all tables: shares sum to 1; medians equal the venue baseline; annualized figures reconcile with sums/hours; spot extremes land on independently known market dates (2024-08-05, 2025-02-03); calendar completeness labels match the sealed rule (2024 INCOMPLETE by one missing hour; 2025 the only COMPLETE year). No finding.
- Execution side effect: untracked `study/src/__pycache__/` created by the host run — not staged; host asked to delete it (builder cannot delete); `.gitignore` added covering `__pycache__/` and `.DS_Store`.

## 2026-11-02 — report, figures, internal matrix authored (builder)

- `reports/STUDY_0.md` authored from the committed host-computed tables: summary, data/coverage, funding (F1/F2 referenced), negative runs, spot descriptors, cost worksheet, reserve worksheet + symbolic bridge, limitations, design implications (the design conclusion), Audit Process (S1–S9 named; round-1 status; neutral working-role statement), Appendix A data/assumption register, Appendix B table pointers. Public wording uses "linear interpolation" only.
- `study/src/make_figures.py` authored (deterministic SVG, stdlib-only; F1 from frozen raw funding via the committed loaders, F2 from committed monthly results; synthetic smoke-test in the authoring shell only). Figures must be host-generated from committed code: the figure run request is embedded in commit request 003 (`study/commit_requests/COMMIT_REQUEST_003_RESULTS_REPORT.md`); figures and the round-1 submission note follow at boundary 004.
- `study/V1_CONSISTENCY_T12.md` (internal, per D6): final matrix restated against the finished artifacts — 16 CONSISTENT, 1 DISCLOSED-DIFFERENCE (fixed vs dynamic window end), 1 DIRECTOR-RESOLVED (Amendment A3 rate-convention disposition). No unresolved conflict.

## 2026-11-02 — COMMIT 003, figures, pre-handoff verification, ROUND-1 SUBMISSION

- Commit 003 `7dba8b654ab955b3348a96d249512c0571ba8960` (36 paths, byte-exact; parent `9a6212ac…cfd0`). Post-commit figure run executed host-side unchanged, exit 0: `reports/figures/F1_funding_hourly.svg` (852,935 B, `19822b5d…e075`) and `F2_monthly_totals.svg` (11,459 B, `9343813e…c49e`), log `RUN_005_figures.log`; receipt `HOST_RECEIPT_004_RESULTS_FIGURES.md` (`dd08c60c…c4cf`), hashes builder-re-verified; both SVGs re-hashed after staging and visually inspected against T2–T4 (panels, zero lines, INCOMPLETE markers, negative months, extremes) — approved.
- Pre-handoff verification completed and recorded in `study/SUBMISSION_ROUND1.md`: E7 scan of all public artifacts (hits adjudicated benign: "Aave v3", scope negations); boundary-month records checks (funding gap settlements absent at source with neighbors present; earliest/latest complete funding months 2023-09/2026-10, 37 each; reserve segments' first/last complete derived months USDC.e 2023-08/2026-08, native 2023-07/2026-09; source snapshots present in boundary months — absence documented, nothing substituted); source-to-output trace of every public quantitative claim; V1 matrix recheck.
- Round-1 submission assembled: `study/SUBMISSION_ROUND1.md` (deliverables inventory, verification record, S1–S9 evidence map, auditor notes). Commit request 004 issued; the resulting HEAD is the round-1 submitted commit. Builder stopped at the boundary; the round ends only with the auditor's written verdict.

## 2026-11-02 — ROUND 1 VERDICT: FAIL (auditor); audit record committed

- The auditor's written verdict (`audit/verdict_round1.md`) on submitted commit `85d24990293a36a858530f406c8ee1217ce0a7b5` is **FAIL** — verdict 1 of at most 5: R1-01 (BLOCKER, S7/E7), R1-02 (MAJOR, S2+S5/E2+E4), R1-03 (MAJOR, S8/E5), R1-04 (MINOR, S2/E2). S1, S3, S4, S6, S9 pass. The auditor's independent recomputation from the pinned raw files matched all submitted numerical results (331/331 value comparisons; 0 hash mismatches across 349 data files); no numerical, sign, unit, cost or reproducibility error was found.
- Audit record committed by the host coordinator: `eb6682e031c2add426567774d7150e0b177c24dd` (receipt `study/host_receipts/HOST_RECEIPT_006_AUDIT_ROUND1.md`). The failed verdict and findings are retained verbatim; nothing is edited.

## 2026-11-02 — ROUND 2 FIXES (builder answers to R1-01…R1-04; prose-only)

No sealed analysis, data file, code file, frozen rule, table, figure or machine-result file is touched; every change is prose in `reports/STUDY_0.md` plus this trail. The sealed finite analysis list (DESIGN §7) is unchanged; no new analysis, policy or hurdle is added.

- **R1-01 (BLOCKER, S7/E7) — fixed.** §2: the negated public reference barred by the publication boundary was removed; the remaining scope negations (backtest / operating policy / return hurdle / net return) were individually adjudicated benign in the auditor's round-1 scan and are retained. §11: the "no verdict exists / updated before publication" paragraph — a forward promise — was replaced by the factual audit record. Post-edit E7 rescan of every public artifact recorded in `study/SUBMISSION_ROUND2.md`.
- **R1-02 (MAJOR, S2+S5/E2+E4) — fixed by removal.** §10.4 no longer compares reserve yield with funding levels; it now states that Study 0 computes no such comparison (different coverages; no common-timestamp intersection performed). The per-segment reserve description (T10) and the symbolic capital bridge (T11) stand unchanged. The removal path offered in the finding was chosen; no unsealed intersection analysis was added.
- **R1-03 (MAJOR, S8/E5) — fixed.** §11 now records the actual round count and outcome (Round 1: FAIL), per-criterion results, all four findings with their severities and dispositions, the auditor's independent-verification result, the location of the verbatim audit trail, and the neutral working-role statement. It states that Round 2's verdict is unwritten and claims no pass. No forward promise remains.
- **R1-04 (MINOR, S2/E2) — fixed.** All three "outage" occurrences (§3 data table, §9 limitations, §10.6) are relabeled missing-candle gaps, with the cause explicitly not established (consistent with DESIGN §5.2 and the source's documented missing-publication semantics). No number changed.
- Round-2 verification record in `study/SUBMISSION_ROUND2.md`: byte-identity of all result-bearing artifacts vs. the round-1 verified state; post-edit E7 rescan; source-to-output trace of every changed quantitative mention; V1 matrix recheck (no boundary statement changed). Host re-verification runs (fixtures, clean reproduction + diff, independent recomputation) are requested at the commit boundary with expected outcomes stated; deviation stops the commit.
- Commit request 005 issued (`study/commit_requests/COMMIT_REQUEST_005_ROUND2_FIXES.md`): the resulting HEAD is the round-2 submitted commit. Builder stopped at the boundary; only the auditor's written verdict ends the round.
