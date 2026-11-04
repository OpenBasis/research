> **REDACTED COPY — published with the Study 0 release**
> This is a redacted copy of the auditor's written verdict. The original is
> withheld because it contains local filesystem paths that identify the host
> machine. Redactions replace only path strings, marked `[REDACTED:…]` — 
> 2 replacement(s) in this file; no finding, command, hash or number
> changed. The original's SHA256, as pinned in the committed audit record
> before redaction: `a84b0cf9a17d123393faf4640fa7356c99c71994e2464745ada82e06125a881e`.
> The redaction procedure is `tools/redact_verdicts.py` in this repository;
> a party with a legitimate verification need can be shown the original
> against that hash.

# Study 0 — Auditor verdict, Round 1

**Submitted commit:** `85d24990293a36a858530f406c8ee1217ce0a7b5` (parent `7dba8b654ab955b3348a96d249512c0571ba8960`).
**Verdict:** **FAIL**. This is written verdict **1 of at most 5**. The submitted study has **one open BLOCKER, two open MAJOR findings and one MINOR finding**. S1, S3, S4, S6 and S9 pass; S2, S5 and S8 are partial; S7 fails. There is no conditional pass. Details and minimum fixes are in `audit/findings_round1.md` (R1-01 through R1-04).

## Verification actually performed

The auditor read `git show --stat 85d2499`, `git log`, `study/CHANGELOG.md`, `study/SUBMISSION_ROUND1.md`, `DESIGN.md`, the director decisions, the frozen rules, all public report sections and tables, figure source/SVG text, the V1 matrix, source manifests, receipts and run records. No mutating Git command was run. The existing untracked `study/commit_requests/COMMIT_REQUEST_004_SUBMISSION.md` and `study/host_receipts/HOST_RECEIPT_005_SUBMISSION.md` were left untouched.

Commands run from `[REDACTED:study-repo-root]` unless a temporary work directory is noted:

1. **Seal, source and commit order:** `git ls-tree --name-only 9d3ed18`; `git rev-list --reverse HEAD`; `git show --format=fuller --no-patch 9d3ed18 85d2499`; `shasum -a 256 DESIGN.md data/source_consistency/V1_DESIGN.md '[REDACTED:external-prior-work-path]/DESIGN.md'`. Result: root commit has only `DESIGN.md`; sealed hash `b4f911187a17593f06e173a014cc923f3ee1708ddb393eaa2338661189eb9c06`; both V1 copies match required `8e5010524e7b34c0c89bfe758067ef92db6ee52db682f23eae87ef09bd657e32`. The root commit time is 2026-11-01T20:47:51Z; result-producing run receipts follow the inputs/spec commit. No seal rewrite appeared in the commit chain.
2. **Clean output reproduction and fixtures:** `env TZ=UTC PYTHONHASHSEED=0 /opt/homebrew/bin/python3.13 study/src/test_fixtures.py`; `env TZ=UTC PYTHONHASHSEED=0 /opt/homebrew/bin/python3.13 study/src/compute_study0.py --out /private/tmp/study0_audit_round1/reports`; `diff -r reports/tables /private/tmp/study0_audit_round1/reports/tables`; `shasum -a 256 reports/results_study0.json /private/tmp/study0_audit_round1/reports/results_study0.json`. Result: 34/34 synthetic fixtures pass (the deliberate conflicting-duplicate fixture prints its caught `ABORT`); pipeline coverage cross-check passes; table diff exits 0 with no output; both JSON hashes equal `f425e2e73b9069f2c8c6101376df02295d44db631cb208f7c0d94f57c6859788`.
3. **Independent raw recalculation:** `env TZ=UTC PYTHONHASHSEED=0 /opt/homebrew/bin/python3.13 audit/independent_round1.py > audit/independent_round1_results.json`; `env TZ=UTC PYTHONHASHSEED=0 /opt/homebrew/bin/python3.13 audit/compare_round1.py`. Result: 349 listed raw/metadata files, 0 hash or byte mismatches; **331 independent-to-submitted value comparisons pass**. The independent scripts use no builder aggregation functions. They compute funding full-window statistics, sign counts, all 41 monthly subtotals/statuses and four annual subtotals per asset, completed/censored negative runs, spot returns and extrema, bounded reserve accruals, boundary-month records and the 29 bps worksheet.
4. **Raw boundary records:** the independent output reports 720 settlement records for September 2023 and 744 for October 2026 for each asset, the earliest/latest complete funding months (37 complete months per asset). Each of the three missing settlement hours has a source record in both adjacent hours and none at the missing hour. USDC.e's first/last complete derived months are August 2023/August 2026, with 31/31 source snapshots; native's are July 2023/September 2026, with 31/30 source snapshots. No unavailable month was replaced by a favorable month.
5. **Independent funding and cost arithmetic:** ETH 29,445 observed hours, sum `0.4746588125` per $1, arithmetic annualized `0.1412128102394294447274579725`; BTC 29,445, `0.4791731877`, `0.1425558541094243504839531330`. Completed runs: ETH 1,018, median/p95/max 2/13/92 hours, worst `−0.0034279723`; BTC 848, 2/16.65/118 hours, worst `−0.0027990672`. ETH has one gap-censored run; BTC has one boundary-censored and one gap-censored run. Per paired notional, `2 × (4.5 + 10) = 29` bps; `29 × 365/D` is 352.83/117.61/29.00 bps at D=30/90/365 after stated rounding. Doubled values also match T9.
6. **Independent spot/reserve and common coverage:** both Coinbase products have 29,438 closes; valid return counts are 29,435 (1h) and 29,366 (24h). T8's four p1/p99 pairs and eight worst-move values/timestamps match the independent output. Reserve modeled hours, sums and annualizations match T10 exactly. Original funding and reserve coverages differ; the independent shared-hour counts are USDC.e 28,301 and native 29,229 over the window (either asset), 8,755 for each in 2025, and 6,351/7,293 respectively in Jan–Oct 2026. The report's relative-materiality claim did not use or disclose these intersections (R1-02).
7. **Figures:** from `/private/tmp/study0_audit_round1/figure_work`, with only read-only symlinks to the repository's pinned `data/` and `study/` plus a copy of the reproduced results JSON, ran `env TZ=UTC PYTHONHASHSEED=0 /opt/homebrew/bin/python3.13 study/src/make_figures.py`. F1 and F2 hashes match the committed figures exactly: `19822b5d863f81e6ce839aa7eebfcdcd9a2c93713a8dea8644c517cf93e1e075` and `9343813e3365c3109573cab66538617bd86fb6172941c6dd0772f91de8dac49e`.
8. **Source-to-output and E7:** read the report's quantitative statements against T1–T11 and the 331 raw-to-results checks. All quoted funding, run, spot, cost and reserve values round from the underlying tables. Inspected `reports/STUDY_0.md`, `reports/tables/*.md`, and both `reports/figures/*.svg` with a case-insensitive search for prototype/implementation/codebase/build/later-work terms and contextual reading. The public boundary violations are at report lines 16 and 122 (R1-01); the missing-candle causal label is at lines 23 and 105 (R1-04). Public tables and SVGs yielded no additional E7 violation. The internal matrix's 18 rows were traced to the hash-verified V1 clauses; row 18 follows A3's narrow director resolution.

The auditor also checked the live [Hyperliquid funding documentation](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/funding), [Hyperliquid `fundingHistory` documentation](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/info-endpoint/perpetuals), and [Coinbase product-candles documentation](https://docs.cdp.coinbase.com/api-reference/exchange-api/rest-api/products/get-product-candles) for source semantics. These live pages corroborate the hourly funding sign/interval, the funding API fields, and the candle bucket/close and missing-publication semantics. They are audit checks made after the seal; the pinned raw files, not live API responses, underlie every numerical result.

## Error-class disposition

| Class | Result |
|---|---|
| E1 units/signs | No error found in the funding, APR, bps or annualization calculations. |
| E2 time/data | R1-02 MAJOR: unaligned reserve/funding comparison; R1-04 MINOR: unsupported "outage" label. No missing-hour fill or favorable window clipping found. |
| E3 costs/capital | No arithmetic, double-counting, selected-weight or investable-net error found. |
| E4 inference/risk | R1-02 MAJOR: relative-materiality inference lacks sealed common coverage. No forecast, margin certification or strategy safety claim found. |
| E5 seal/reproducibility | R1-03 MAJOR: public audit account lacks the actual verdict; seal order and numeric reproduction pass. |
| E6 evidence honesty | Prior exposure and correction chronology are disclosed. No fabricated observation or hidden adverse period found; R1-04's cause wording must be corrected. |
| E7 anachronism | R1-01 BLOCKER in public report. |
| E8 tone | No severity-bearing tone finding. |

**Next handoff:** the builder must respond to every finding in the changelog, preserve this failed verdict, revise only within the sealed scope, and submit a new commit for Round 2. No director decision is currently required; if a proposed fix would change the sealed analysis, the builder must escalate before doing so. The round counter is now 1.
