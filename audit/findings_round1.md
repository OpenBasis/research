# Study 0 — Auditor findings, Round 1

**Submitted commit:** `85d24990293a36a858530f406c8ee1217ce0a7b5`.
**Standard:** the sealed S1–S9, with director-approved A1–A4. This is verdict 1 of at most 5. A measured small or negative opportunity is not a defect.
**Independent evidence:** `audit/independent_round1.py` reads pinned raw files without importing builder aggregation code; its output is `audit/independent_round1_results.json`. The full commands and checks are in `audit/verdict_round1.md`.

## Criterion decisions

| Criterion | Status | Evidence and actual values | Minimum change needed |
|---|---|---|---|
| S1 | PASS | `git ls-tree 9d3ed18` returns only `DESIGN.md`; the root seal was committed at 2026-11-01T20:47:51Z, before the inputs/spec and result commits. `DESIGN.md` §§2, 5, 7–13 fixes the universe, conventions, analyses and prior exposure, including V1 overlap and the prior Study 0 incarnation. `study/CHANGELOG.md` lines 5–35 and the receipts support the order. | None. |
| S2 | PARTIAL | `data/MANIFEST.json` lists 349 data files; independent SHA256/byte verification found 0 mismatches. `reports/tables/T01_series_inventory.md` records 29,445/29,448 funding hours per asset, 29,438/29,448 spot closes per product, 28,304/29,448 USDC.e and 29,232/29,304 native modeled reserve hours. `DESIGN.md` §§4–6 seals missingness, segments and the A2 rule. The report's reserve/funding comparison at `reports/STUDY_0.md:112` uses neither exact common timestamps nor disclosed common coverage; see R1-02. Its "outage" label for missing spot candles is unsupported; see R1-04. | Resolve R1-02; correct R1-04 wording. |
| S3 | PASS | Independent raw recalculation: ETH funding sum `0.4746588125`, arithmetic annualization `0.1412128102394294447274579725`, 1,018 completed/1 censored negative runs; BTC `0.4791731877`, `0.1425558541094243504839531330`, 848 completed/2 censored. These match T2/T6/T7. Both spot products have 29,435 valid 1-hour and 29,366 valid 24-hour returns, with T8 quantiles and extrema matching independent recalculation. T3/T4 show all 41 months; T5 shows all four years, marking 2024 incomplete by one missing funding hour. | None. |
| S4 | PASS | Independent `2 × (4.5 + 10) = 29` bps and `29 × 365/D` give 352.83/117.61/29.00 bps for 30/90/365 days; the sole doubled case gives 705.67/235.22/58.00. T9 and report §7 label assumptions and unpriced items. Independent reserve sums/annualized means match T10: USDC.e `0.1465408027968036529680365186`/`0.04535392285542679479932164722`; native `0.1625441396803652968036529096`/`0.04870986123426382047071700493`. T11 and report §8 keep N/C and R/C symbolic. No investable-net claim found. | None. |
| S5 | PARTIAL | Report §§4–6 and 10 retain negative months, completed and censored runs, 2025/2026 compression and reference-market tail moves. The specific materiality comparison at line 112 uses non-aligned coverage; R1-02 applies. No optimization, funding gate, chosen capital weights or return hurdle was found. | Resolve R1-02. |
| S6 | PASS | External V1 and `data/source_consistency/V1_DESIGN.md` both SHA256 `8e5010524e7b34c0c89bfe758067ef92db6ee52db682f23eae87ef09bd657e32`. `study/V1_CONSISTENCY_T12.md` has 18 clause-anchored rows. Row 16 discloses the different sealed window end; row 18 follows the director's narrow A3 disposition without asserting a V1 error. No actual V1 contradiction found. | None. |
| S7 | FAIL | Public report line 16 mentions building a trading engine, even though negated. Line 122 promises a later update. The publication boundary and E7 bar both forms of reference; see R1-01. The rest of the public report, T1–T11 and both SVGs were scanned for E7. | Resolve R1-01, then rescan every public artifact. |
| S8 | PARTIAL | Changelog, source/commit receipts and run logs retain the work so far. Report §11 names S1–S9 and gives the neutral working-role statement. Its line 122 still says no verdict exists and defers the actual round count, outcome and findings; this Round 1 verdict makes that text stale. See R1-03. | Record Round 1 FAIL and the substantive findings/fixes in the public Audit Process as the trail develops. |
| S9 | PASS | Clean-directory reproduction made `results_study0.json` byte-identical (SHA256 `f425e2e73b9069f2c8c6101376df02295d44db631cb208f7c0d94f57c6859788`) and `diff -r` found no table differences. F1/F2 independently regenerated with hashes `19822b5d…e075` / `9343813e…c49e`. `study/commit_requests/COMMIT_REQUEST_003_RESULTS_REPORT.md`, `COMMIT_REQUEST_004_SUBMISSION.md` and receipts record output hashes; Appendix B links claims to T1–T11. No missing numeric or deterministic figure output was found. | None for this criterion. |

## Findings requiring response

### R1-01 — Public boundary violation

- **Criterion / class / severity:** S7; E7; **BLOCKER**.
- **Evidence:** `reports/STUDY_0.md:16` says the study “builds no trading engine.” E7 bars public build/implementation references, including negated ones. `reports/STUDY_0.md:122` says “Before publication, this section is updated,” a future work promise in the public Audit Process. The report is explicitly public-facing; the publication rule applies to both lines.
- **Required fix:** Remove the build/engine reference without changing the truthful scope or chronology. Replace the forward promise with the actual audit status and findings after this verdict. Rescan the report, all tables and both figures for E7. Do not erase prior research or the failed verdict.

### R1-02 — Reserve/funding comparison lacks common coverage

- **Criterion / class / severity:** S2 and S5; E2/E4; **MAJOR**.
- **Evidence:** `reports/STUDY_0.md:112` calls the full-coverage reserve annualized figures “significant next to recent funding levels.” The reserve rates in T10 are annualized over distinct, gappy 2023–2026 segment coverages; the referenced funding figures in report §§1/4/10.1 are 2025 full-year totals and 2026 ten-month observed subtotals. `DESIGN.md:65,123` requires exact timestamp intersections and both original and common coverage for cross-series comparisons. No intersection or common-coverage disclosure appears in `reports/results_study0.json`, T1–T11, the report or the pipeline. Independent timestamp intersection counts are 28,301 (funding × USDC.e) and 29,229 (funding × native) over the window, for either asset; in 2025 each is 8,755, and in Jan–Oct 2026 they are 6,351 and 7,293 respectively. The original coverages are 29,445 funding, 28,304 USDC.e and 29,232 native hours. The statement's materiality inference is therefore unverified on its stated comparison.
- **Required fix:** Remove the comparison to recent funding levels and any associated relative-materiality inference, keeping the independently supported reserve description and symbolic bridge. If the builder instead retains a quantitative cross-series comparison, it must follow the sealed intersection and coverage rules without adding an unsealed analysis or policy.

### R1-03 — Audit Process has no actual Round 1 outcome

- **Criterion / class / severity:** S8; E5; **MAJOR**.
- **Evidence:** `reports/STUDY_0.md:118-122` lists the criteria and roles, but line 122 explicitly says no verdict exists and promises a later update. This written verdict is Round 1 and its outcome is FAIL. The public Audit Process currently contains neither that outcome nor the substantive findings and their eventual fixes.
- **Required fix:** Update §11 with the actual round count and outcome as the rounds conclude; retain this failed verdict, list the substantive findings and verified fixes, and retain the neutral statement that persona titles denote working roles rather than individual credentials. Do not claim a pass before the auditor writes one.

### R1-04 — Missing spot candles are called exchange outages

- **Criterion / class / severity:** S2; E2; **MINOR** (wording only; the missingness counts and risk calculations are correct).
- **Evidence:** `reports/STUDY_0.md:23,105` calls two five-hour runs of absent Coinbase candles "outages." The pinned raw pages and T1 establish absent candles, but do not establish a Coinbase service outage or its cause. Coinbase's [product-candles documentation](https://docs.cdp.coinbase.com/api-reference/exchange-api/rest-api/products/get-product-candles) says historical rates may be incomplete and that intervals without ticks have no published candle. The builder's `DESIGN.md` §5.2 likewise treats such hours as missing, without a cause claim.
- **Required fix:** Call these two runs missing-candle gaps, or provide dated primary evidence of an actual outage. No numeric recalculation is needed.

No E8 tone finding changes the verdict. No evidence supports a numerical, sign, APR/APY, cost or V1 blocker in the submitted calculations.
