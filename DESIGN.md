# DESIGN.md — Study 0 Sealed Design

**Study:** OpenBasis Study 0 — descriptive foundation: ETH/BTC Hyperliquid funding opportunity, its variation and negative periods, cost and reserve drag, risks, and design implications. It ends at the design conclusion.
**Role:** BUILDER, under the canonical builder prompt as amended (§2). An AUDITOR with the same repository verifies against S1–S9 only.
**Seal:** This file is committed ALONE as the first commit of this repository, by the mechanical host coordinator under the host-Git protocol (Amendment A4). The commit hash of that commit constitutes the seal. The actual seal UTC time and commit hash are reported by the host after the commit and recorded in `study/SEAL_RECORD.md` in a later commit; they do not appear in this file. Any post-seal change to this design requires director authorization and an amended DESIGN.md committed alone, preserving this original.
**Design date:** 2026-11-01 (UTC).

---

## 1. Purpose and binding boundaries

- S1–S9 (§3) are the COMPLETE and EXCLUSIVE acceptance standard. Neither role may add criteria, assets, venues, experiments, return hurdles, or an operating policy. A correctly measured small, negative, or inconclusive opportunity can PASS.
- No search, optimization, strategy backtest, trading engine, operating policy, return hurdle, or deployment is authorized or performed.
- Every rate description here is exactly that: not compounded APY, not an investable equity curve; no net-APY or investable-net claim is made anywhere.
- Public artifacts (study text, figures, captions, summaries, Audit Process) stop at the design conclusion: no prototype, implementation, codebase, build, post-study result, release promise, or later-study teaser (E7). The publication boundary never licenses fabricated chronology or a claim that no prior work exists. DESIGN.md and the audit trail are working artifacts; research calculations and reproduction scripts are permitted in working artifacts.
- V1 — the sealed design of the prior delta-neutral study — is an internal consistency constraint only, never evidence for Study 0's empirical claims. The authorized read-only copy is `data/source_consistency/V1_DESIGN.md` (32,236 bytes), SHA256 `8e5010524e7b34c0c89bfe758067ef92db6ee52db682f23eae87ef09bd657e32`, byte-verified by the host coordinator against the external source and independently re-hashed by the builder on 2026-11-01. Neither V1 source is modified.

## 2. Authority, amendments, and protocol position

This design executes the director-approved scope. The governing records, all in this repository:

| Record | Path | SHA256 |
|---|---|---|
| Canonical builder prompt (original, preserved) | `study/prompts/original/STUDY_0_BUILDER_PROMPT.txt` | `ffdde616794b48665ae3b0cfd938e9eb75228956bbe424bc59eef9563ff5642c` |
| Canonical auditor prompt (original, preserved) | `study/prompts/original/STUDY_0_AUDITOR_PROMPT.txt` | `fea411aef5c3cd321a0b3a4cf84cd234868e9c59938ea5e0799e4196980283ff` |
| Amendments A1–A2 (DefiLlama source exception; bounded daily-snapshot approximation) | `study/prompts/amendments/AMENDMENT_A1_A2.txt` | `9c755cd5826e03e28845d4d6328bef9136460cf1c5cffb3878bb2d3599364cd6` |
| Director decisions D1–D7 | `study/DIRECTOR_DECISIONS_PRESEAL.md` | `c8e34bce31d21fb06a2aa2db7dedbdffd71914288a0d86ef89ea71a0c35b25ad` |
| Director S6 rate-convention disposition | `study/DIRECTOR_DECISION_S6_RATE_CONVENTION.md` | `cd73b696894c7e2c9fb56dc278e83420c93649061c6749146a9f30a4ec856810` |
| Working builder prompt (original + A1–A4, byte-exact concatenation) | `study/prompts/working/STUDY_0_BUILDER_PROMPT.txt` | `58f386167c0fd24fcfa9a1bf202fb4627d9265800cfcfc3bdad4d510798fd86d` |
| Working auditor prompt (same appended block) | `study/prompts/working/STUDY_0_AUDITOR_PROMPT.txt` | `1238ade3736034f720ddc95d072a34fe9f1fbf77e1892547204928d496aa093b` |
| Mechanical prompt-comparison record | `study/prompts/working/PROMPT_COMPARISON.md` | recorded in the post-seal manifest |

The canonical S1–S9 section is byte-identical across both original and both working prompts (2,010 bytes, SHA256 `97fffb3f5705e57ab615fd20d49eb9f254300fe2b97cb179fbfb941033d735be`); the comparison record documents the checks. The original prompts' draft header is superseded only by the director's explicit execution authorization and only within the approved scope (Amendment A4.4).

Host-Git protocol (Amendment A4): the builder runs no mutating Git commands; at each commit boundary the builder writes a commit request under `study/commit_requests/` listing every path and its SHA256, and the mechanical host coordinator verifies bytes and commits exactly those paths. The first commit contains DESIGN.md alone.

Protocol position at sealing: zero audit rounds used, zero written verdicts. The five-round cap is untouched.

## 3. Acceptance standard (sealed verbatim from the canonical prompts)

S1. DESIGN.md is committed alone before new Study 0 result computation; exact data, dates, definitions, finite analyses and S1-S9 are sealed, with truthful prior-exposure and reuse disclosure. No retrospective result is called prospective.
S2. Every required series has dated provenance, hashes, units and coverage; the sealed missingness, cutover and common-window rules are applied without favorable clipping.
S3. Both assets have every specified funding, negative-run and spot-risk result, with correct signs, denominators, timestamps, conventions and incomplete-period labels.
S4. The fixed cost and reserve worksheets reconcile to their formulas, distinguish observations from assumptions and unpriced risks, and make no investable-net claim.
S5. All design conclusions follow from Study 0 evidence; adverse or inconclusive results remain visible. No optimization, invented operating policy or return hurdle exists.
S6. Limitations and boundaries are consistent with the hash-verified V1 seal, evidenced by an internal clause-level matrix; any real discrepancy is resolved by the director.
S7. Every public-facing artifact stops at the design conclusion, contains no anachronism or implementation reference, and makes no false claim about chronology or provenance.
S8. The complete audit trail retains findings, responses, fixes, verification and every verdict; the study's Audit Process names S1-S9, actual round count and outcome, discloses the builder/auditor working roles, and states that persona titles describe working roles rather than individual credentials. It publishes findings fixed, not merely the pass.
S9. Frozen inputs, analysis specification and research calculations reproduce every numeric result and deterministic table/figure; claims have source-to-output links, final artifact hashes are recorded, and all required deliverables are present.

Error classes E1–E8 of the canonical prompts are the audit taxonomy. Fabrication, anachronism, seal violation and V1 inconsistency are BLOCKERs.

## 4. Observation window and bucket grid

| Item | Sealed value |
|---|---|
| Grid | UTC hourly buckets, labeled by bucket START |
| First bucket | 2023-06-23 00:00 UTC |
| Last bucket | 2026-10-31 23:00 UTC (inclusive) |
| Full-window bucket count | 29,448 (1,227 calendar days × 24; calendar arithmetic, not a data result) |
| Per-series scope | Buckets in [max(window start, series first dated availability), window end]. First availability per series is fixed in §5 from source metadata. Pre-launch/pre-listing observations are unavailable, not zero. |

Calendar completeness rule: a calendar month or year is COMPLETE for a series only if every hour of that calendar period lies inside the window AND inside the series scope AND is observed. Otherwise the period is labeled INCOMPLETE and only the observed subtotal is shown, separately. All calendar periods in the window appear, including window-partial boundary periods (June 2023; calendar years 2023 and 2026 are window-partial by construction).

The window is fixed. No zero-fill, no interpolation, no future borrowing, no favorable window selection. The single sealed exception is the Amendment A2 bounded daily-snapshot approximation for the reserve series (§5.3); all other series remain under the unamended no-fill rule. Cross-series comparisons use exact timestamp intersections and disclose both original and common coverage.

## 5. Series, sources, provenance, and coverage

All raw inputs are already pinned verbatim in this repository, retrieved 2026-11-01 19:13–19:27 UTC (per-file request parameters, retrieval UTC times and SHA256 hashes in the page logs `data/raw/*/*_pages.ndjson`, the retrieval logs `data/raw/*/RETRIEVAL_LOG.tsv`, and `data/MANIFEST.json`). `data/MANIFEST.json` (SHA256 `bea49ac4a455b9742918adb62d7dd5dfe7538d05c31a56c3b9b30793b0ba459b`, built 2026-11-01T19:27:07Z) records all 349 data files; the builder re-verified every listed hash and byte count against the files on 2026-11-01 with zero mismatches and zero unlisted data files. Coverage, duplicate and missingness censuses are pinned in `data/COVERAGE.json` (SHA256 `61311b002808ae175c18899e1f14076cd7b59a87b9a0544eaf466c1088ade230`), produced by `study/src/inventory_preseal.py` — coverage metadata only, no funding/return/rate statistics.

Retrieval scripts: `study/src/retrieve_hyperliquid.py`, `study/src/retrieve_coinbase.py`, `study/src/retrieve_defillama.sh`, `study/src/retrieve_adapter_evidence.sh`, `study/src/retrieve_adapter_history.sh`; manifest builder `study/src/build_manifest.py`. These are committed with the data after the seal.

### 5.1 Hyperliquid perpetual funding — ETH and BTC

- Endpoint: `POST https://api.hyperliquid.xyz/info` with `{"type":"fundingHistory","coin":<"ETH"|"BTC">,"startTime":<ms>,"endTime":<ms>}`; paginated ≤500 records, oldest-first, resumable from the per-coin page log. Retrieval span: payments 2023-06-23T00:00:00Z through 2026-11-01T00:00:00Z inclusive.
- Record fields: `coin`, `fundingRate` (decimal string), `premium` (decimal string), `time` (Unix ms payment timestamp). `fundingRate` and `premium` are ingested as exact decimals (`decimal.Decimal`), never parsed as floats at ingestion.
- Rate unit: the hourly applied funding rate, a fraction of notional per hour. Unit check (sealed, already satisfied by the pinned data): payments arrive once per hour (29,446 unique settlement hours per coin over the retrieval span), and the modal exact `fundingRate` string is `0.0000125` (ETH 14,702 records; BTC 15,442), equal to the 0.00125%-per-hour venue baseline rate recorded in the approved proposal. Both facts are consistent with the hourly unit; no escalation required.
- Sign: positive funding ⇒ longs pay shorts ⇒ **a short receives**. Study 0 reports short-receives-positive, the raw sign unchanged. Identical to V1 §4.
- Settlement-to-bucket mapping (director decision D3, sealed): a funding record with payment timestamp `t` settles the compensated interval ending at its settlement hour; it maps to the bucket starting at `floor_hour(t) − 1h` (the compensated interval's start). The original payment timestamp is retained in the processed data. Payment-time jitter after the hour boundary (max observed 887,645 ms; 4 records per coin exceed 60 s) is absorbed by `floor_hour` and disclosed. The retrieved 2026-11-01T00:00Z settlement supplies the final window bucket 2026-10-31T23:00 as boundary evidence and does not extend the window; the 2023-06-23T00:00Z payment maps to the pre-window bucket 2023-06-22T23:00 and is retained in raw data but out of scope.
- Coverage (pinned): per coin, 29,445 of 29,448 window buckets observed; 3 missing buckets, identical for both coins: 2023-07-02T19:00Z, 2023-08-23T19:00Z, 2024-08-15T12:00Z. Duplicates: 0 identical, 0 conflicting. Series scope starts at the window start (the feed's earliest funding predates it; V1 D1 records 2023-05-12).

### 5.2 Coinbase spot hourly closes — ETH-USD and BTC-USD (reference marks)

- Endpoint: `GET https://api.exchange.coinbase.com/products/{ETH-USD,BTC-USD}/candles?granularity=3600&start=<iso>&end=<iso>`, ≤300 candles per request, newest-first within a page, pinned exactly as returned.
- Semantics: candle array `[time, low, high, open, close, volume]`; `time` is the **bucket start** in epoch seconds UTC (verified against the pinned pages: times align exactly with requested hourly bucket starts). Buckets with no trades produce no candle and are treated as missing, never filled. Candles outside the window would be trimmed in processing; the pinned pages contain 0 out-of-window candles.
- Only the hourly `close` is used, as a reference mark. Coinbase marks are not execution proof and are never presented as executable prices.
- Coverage (pinned): per product, 29,438 of 29,448 window buckets observed; 10 missing buckets in two runs, identical for both products: 2025-10-25T16:00–20:00Z (5 buckets) and 2026-05-08T02:00–06:00Z (5 buckets). Duplicates: 0 identical, 0 conflicting.

### 5.3 Aave v3 Arbitrum USDC reserve rates — DefiLlama, two separate dated segments (Amendments A1–A2; decisions D1–D2)

**Source (director-approved aggregator exception, A1/D1).** DefiLlama yields API, dated pool series:

- Native USDC: `https://yields.llama.fi/chart/d9fa8e14-0447-4207-9ae8-7810199dfa1f` → `data/raw/defillama/chart_native_usdc.json`
- USDC.e (bridged): `https://yields.llama.fi/chart/7aab7b0f-01c1-4467-bc0d-77826d870f19` → `data/raw/defillama/chart_usdc_e.json`
- Pool-identity evidence: `data/raw/defillama/pools_snapshot.json` (`https://yields.llama.fi/pools`) shows, for these exact pool ids, project `aave-v3`, chain `Arbitrum`, symbol `USDC`, and underlying token addresses native USDC `0xaf88d065e77c8cC2239327C5EDb3A432268e5831` and USDC.e `0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8`. The native address matches the USDC address recorded in V1 D10.

This series is **aggregator evidence**, an explicit director-approved exception (A1) to the primary-dated-observations requirement, for this series only, and is labeled aggregator evidence everywhere it appears. No on-chain event-reconstruction pipeline is added.

**Field and rate convention (sealed from repository source evidence).** Study 0 uses the `apyBase` field exclusively. The pinned DefiLlama yield-server aave-v3 adapter assigns `apyBase: (liquidityRate / 10 ** 27) * 100` — Aave's on-chain ray-unit `liquidityRate`, an annualized rate applied by the protocol with linear accrual, expressed in percent — with **no compounding transform**. This mapping is byte-identical in function across the pinned master adapter (`data/raw/defillama_adapter_evidence/aave-v3_index_master.js`) and all 14 pinned dated historical adapter versions, whose commit dates (from the pinned commit history, 69 commits) run 2023-06-06 through 2026-10-29 and bracket the entire study window. Therefore `apyBase` is sealed as an **APR in percent**; the sealed hourly conversion is simple accrual:

    a(b) = (apyBase / 100) / 8760    per derived hour b.

`apyBase` is the base supply rate. Reward components (`apyReward`, non-null on 86 USDC.e days and 80 native days) are excluded and the exclusion is disclosed wherever the reserve worksheet appears. The generic `apy` field is not used (§11 row 18 and Amendment A3 record its V1-mapping status).

**Documented sampling cadence (evidence-fixed).** The pinned yield-server source shows: adapters are triggered hourly (`serverless.yml`: `cron(0 * * * ? *)` feeding the adapter queue; `triggerAdaptor.js` writes rows stamped at write time), and the `/chart/{pool}` endpoint (`controller_yield.js`, `getYieldHistory`) returns, per calendar date of the stored timestamp, the single row with `max(timestamp)` for that date. The documented delivered cadence is therefore **one snapshot per calendar date** (the last stored row of that date). The pinned charts conform: zero dates carry more than one snapshot, and snapshot times cluster at 23:xx UTC (native: 1,212 of 1,223; USDC.e: 1,461 of 1,503), with the final point being the latest row of the still-incomplete retrieval date.

**Bounded daily-snapshot approximation (Amendment A2 / decision D2, sealed).** A snapshot with timestamp τ applies only AFTER τ: from the first hour boundary strictly greater than τ, for at most **24 hourly buckets** (the validity bound tied to the documented one-snapshot-per-calendar-date cadence, not chosen by intuition), and in any case only up to the bucket before the next snapshot's first applicable hour boundary. Hours beyond the bound, or at and after the next snapshot's applicability, are gaps; missing snapshot days remain gaps; there is no indefinite carry. Derived hourly reserve rates are **modeled approximations, not observed hourly returns**, and are labeled as such everywhere they appear. This rule is implemented verbatim in `study/src/inventory_preseal.py` and its coverage consequences are pinned in `data/COVERAGE.json`.

**Segments (sealed).** Native USDC and USDC.e are separate dated segments, each reported on its own disclosed coverage. No stitching, no cutover construction, no combined series.

| Segment | Snapshots (full chart) | First snapshot | Segment scope first bucket | Derived covered buckets in scope | Scope expected | Derived gap buckets |
|---|---|---|---|---|---|---|
| USDC.e | 1,503 (from 2022-08-08, pre-window history retained raw) | 2022-08-08T00:00Z | 2023-06-23T00:00Z (window start) | 28,304 | 29,448 | 1,144 |
| Native USDC | 1,223 | 2023-06-28T23:00Z | 2023-06-29T00:00Z (first hour boundary after first snapshot) | 29,232 | 29,304 | 72 |

`apyBase` is null on 0 in-scope snapshots in both charts. The native segment's first dated observation (2023-06-28) is consistent with V1 C19's record of the native pool's first dated observation; the pre-launch native period is unavailable, not zero.

## 6. Data hygiene rules (sealed)

1. Raw pulls are pinned verbatim with request, retrieval UTC and SHA256 recorded (page logs, retrieval logs, `data/MANIFEST.json`). Post-seal, inputs are frozen: analyses read only the pinned files.
2. Duplicates: records identical in (series, timestamp, payload) are deduplicated with counts logged. Records sharing (series, timestamp) with conflicting payloads are a data defect: stop and escalate; never silently pick one. Pinned censuses show 0 of each in all series.
3. Missingness: every series is described on its observed timestamps with expected/observed counts and a gap census. No fill of any kind, except the Amendment A2 bounded approximation for the reserve series exactly as sealed in §5.3.
4. Cross-series statistics use exact timestamp intersections; original and common coverage are both disclosed.
5. Reuse and prior exposure are disclosed in §12; nothing already analyzed is represented as a new discovery or as prospectively preregistered.

## 7. Analyses (COMPLETE and EXCLUSIVE)

| ID | Analysis |
|---|---|
| A1 | Funding description per asset (ETH, BTC): signed sum per $1 constant quote notional; arithmetic annualized rate; hourly mean, median, p5/p95, min, max; positive/zero/negative hour shares; full-window and calendar month/year tables with completeness labels |
| A2 | Negative funding runs per asset: definition §8; count, median/p95/maximum duration, cumulative funding per completed run; boundary/gap-censored runs listed separately |
| A3 | Spot risk descriptors per asset: k ∈ {1, 24} hour simple returns where the full hourly span is present; p1/p99; worst up and down moves with UTC timestamps. Reference-market observations, not liquidation or margin tests |
| A4 | Cost worksheet (§9): fixed reference constants, exactly one ×2 sensitivity, unpriced-items register |
| A5 | Reserve worksheet and symbolic capital bridge (§10), per segment |
| A6 | V1 internal-consistency matrix (§11), clause-level, internal |

Nothing else is computed. No funding gate or negative-funding sit-out is simulated; no venue comparison; no ETH-only substitution; no trade-size grid; no optimal holding period; no compounded-APY presentation of the rate description.

Deterministic tables: T1 series inventory and coverage; T2 funding descriptive statistics (both assets); T3/T4 calendar-month funding totals (ETH/BTC); T5 calendar-year funding totals; T6 negative-run summaries plus censored-run list; T7 per-run listing; T8 spot risk descriptors; T9 cost worksheet; T10 reserve segment summaries; T11 symbolic capital bridge; T12 V1 consistency matrix (internal).

Presentation (director decision D6, sealed): the public study keeps all required numerical outputs but places detailed monthly and per-run tables (T3/T4, T7) in appendices or data files. Exactly two main figures: **F1** combined ETH/BTC hourly funding time series; **F2** calendar-month funding totals for both assets, completeness-labeled. No histograms. T12 stays internal to the repository and out of the public study.

## 8. Exact formulas and conventions (sealed)

Let `O_a` be the observed window buckets for asset `a`, `f_a(b)` the hourly funding rate (per $1 quote notional, short-receives-positive), `|O_a|` the observed hour count.

- Funding sum: `S_a = Σ_{b∈O_a} f_a(b)` — signed, per $1 constant quote notional.
- Arithmetic annualized rate: `R_a = 8760 · S_a / |O_a|`. A rate description, not compounded APY and not an investable equity curve.
- Distribution statistics: mean, median, p5, p95, min, max of `{f_a(b)}`. All quantiles in Study 0 use linear interpolation (type 7; the numpy default). Type 7 is named here and in the frozen rules; public prose says only "linear interpolation".
- Sign shares: `#(f>0)/|O|`, `#(f=0)/|O|`, `#(f<0)/|O|`, with zero meaning exact decimal zero.
- Arithmetic discipline: funding strings are ingested as exact decimals; signed sums and calendar-period totals are computed in exact decimal arithmetic; distribution statistics (mean, quantiles, extremes) are computed on float64 conversions. Both conventions are recorded in `frozen_rules/study0.json`.
- Negative run: a maximal sequence of consecutive grid buckets, all observed, with `f < 0` strictly. A zero, positive, or missing hour breaks a run. A run is COMPLETED iff it is immediately preceded and followed, inside the window, by an observed bucket with `f ≥ 0`. Runs adjacent to the window boundary or to a missing bucket are CENSORED: listed separately with observed partial duration and cumulative funding, excluded from completed-run aggregates. No persistence is inferred across gaps or into the future.
- Calendar-period funding totals: a month/year total is shown only when every expected bucket of that period is observed (§4 rule); otherwise the period is labeled INCOMPLETE and the observed subtotal is shown separately.
- Spot returns: `r_k(t) = P(t)/P(t−k) − 1` for k ∈ {1, 24}, defined only when every hourly close in `[t−k, t]` (all k+1 closes) is observed. Report p1/p99 (type 7) and the single worst up and down values with their UTC timestamps, per asset and k. Reference-market observations only.
- Reserve accrual (per segment, A2-derived hours only): hourly modeled accrual `a(b) = (apyBase/100)/8760` (§5.3); per-$1-reserve sum `Σ a(b)` and arithmetic annualization `8760 · mean(a(b))` on the segment's disclosed derived coverage. Labeled modeled approximation from aggregator evidence wherever reported.
- Units: 1 bp = 1e-4. The only APR/APY conversions in Study 0 are those defined in §5.3; unlike return conventions are never summed.

## 9. Cost worksheet (A4; fixed)

Reference fee-and-spot-impact assumptions — **modeled inputs, not empirical findings or current executable quotes**. The constants coincide with V1's sealed modeling constants (C8, C9, C11); that is lineage, not evidence.

- Flat one-way perp fee: 4.5 bps. Flat one-way off-venue spot fee-plus-impact: 10 bps (spot impact is inside the 10 bps and is not double-counted anywhere).
- One entry plus one exit: 2 × (4.5 + 10) = 29 bps per paired notional.
- Annualized reference drag: `29 · 365 / D` bps for D ∈ {30, 90, 365} days (values computed post-seal).
- Exactly one sensitivity: all modeled costs ×2.
- Unpriced register, shown as unpriced (neither zero nor silently included): perp market impact, gas beyond the illustration, transfers, top-ups, settlement, borrow/custody, opportunity cost. Gas appears only as an illustration at $0.50 per assumed leg, never as measured route cost.
- Prohibited outputs: trade-size grid, optimal holding period, total-cost certification, net-APY claim.

## 10. Reserve worksheet and capital bridge (A5; fixed)

- Per-$1-reserve modeled accrual and its arithmetic annualization, per segment, on disclosed derived coverage (§8), labeled per §5.3.
- Capital bridge, **symbolic only**: with `N` matched short notional, `R` reserve, `C` total capital — funding contribution = `(N/C) · Σ funding`; reserve contribution = `(R/C) · Σ reserve accrual`; cost contribution = cost dollars / `C`. No value of `N/C` or `R/C` is selected; no weights are chosen.
- Prose obligations: explain capital dilution, delayed availability, and the opportunity-cost comparator that would be needed before calling a reserve return a gain or a drag. A yield-bearing reserve is never equated with risk-free cash. Unlike return conventions are never summed.

## 11. V1 internal-consistency matrix (A6; clause anchors from the hash-verified copy)

Each T12 row carries: boundary | V1 anchor | Study 0 treatment. Any real conflict is a BLOCKER — escalated to the director, never hidden, even if omitted from publication. The matrix is internal (D6). Sealed skeleton; final T12 restates these rows against the finished artifacts:

| # | Boundary | V1 anchor | Study 0 treatment |
|---|---|---|---|
| 1 | Off-venue spot is not proof of a fully on-chain design | §1; C9 | 10 bps spot leg labeled off-venue reference; no on-chain-completeness claim |
| 2 | Always-on includes negative funding; no gate or sit-out | §1 | A2 describes negative runs only; no gate simulated |
| 3 | 45% notional, 50/50 mix, 15% margin cap, ~40–45% reserve | §1; C1, C2, C4, C25 | Cited as director-fixed V1 constants; not derived, tested, or optimized by Study 0; bridge stays symbolic |
| 4 | Loss bound E+0.5N ≤ 40% NAV | §1; C5 (V1's operational form adds a net-delta term) | Cited as V1 constant, exact V1 form quoted; nothing re-derived |
| 5 | 8% drawdown halt; two-hour deadman | C6; C7 | Cited as V1 constants; "manual" re-arm proxy noted as a modeling stand-in per V1 |
| 6 | Full-window perp marks are reconstructed (Coinbase + premium); only recent actual candles validate | §3.6; D3 | Study 0 uses no perp marks; any mention preserves the reconstruction boundary |
| 7 | Dated depth/OI end 2026-04-03; carry after is flagged stale | D4, D5; §3 rule 4 | Study 0 uses no depth/OI; any mention preserves the stale flag |
| 8 | Missing funding/spot supports no decisions; carried marks are valuation only | §3 rule 7 | Missing buckets stay missing in every Study 0 statistic; no carry anywhere in Study 0 |
| 9 | Reference fees, gas, re-arm and liquidation treatments are modeling assumptions | C8–C11, C6, C22 | §9 labels them modeled inputs; identical constants disclosed as lineage |
| 10 | Aave→Arbitrum→HL route: same-hour normal and two-hour stress are modeled, not guaranteed; pauses/failed attempts are residual risk | §8; C13, C14 | Study 0 models no route; delayed availability discussed qualitatively within these bounds |
| 11 | Zero liquidation is limited to modeled gap/ramp/historical families, never general safety | §9; C22 | A3 is explicitly not a margin or liquidation certification; no safety claim |
| 12 | Outage proxy closes shorts at pre-outage mark and freezes equity; no frozen hedge maintained | C23 | No outage claims; references preserve the proxy's limits |
| 13 | stETH accrues ETH units, no discount model; BTC floor yield zero; USDC $1 except explicit shocks | §4; C24 | Not used by Study 0; references preserve; USDC treated as $1 accounting with no depeg claim |
| 14 | sUSDe APY is not confirmed holder return; no relabel or backfill | D9; §3 rule 3 | Not used; references preserve |
| 15 | Pinned-environment reproduction is not a universal portability claim | §12 | Study 0's reproduction statement is scoped to its own pinned environment only (§13) |
| 16 | Funding sign (positive ⇒ short receives); window start 2023-06-23 | §4; §2 | Identical. Study 0's fixed end 2026-10-31 23:00 differs from V1's dynamic end (≈2026-09-17) by design; disclosed, not a conflict |
| 17 | V1 Aave cutover (USDC.e → native from 2023-06-28, C19) | C19 | Study 0 keeps separate segments, no cutover. Pinned native first dated observation 2023-06-28 agrees with C19; no discrepancy |
| 18 | V1 de-compounds DefiLlama `apy` as annual compounded yield | §4; D6 | Study 0 uses `apyBase` under its evidenced APR convention (§5.3). Director disposition (Amendment A3): the generic-`apy`-versus-`apyBase` mapping in V1 is an unresolved later-review issue, not a proven V1 calculation error; V1 is unmodified; the disposition is specific to this documented difference and relaxes no other S6 requirement |

None of V1's strategy mechanisms is rerun. The matrix checks consistency only.

## 12. Prior exposure, reuse and chronology (truthful disclosure)

- Study 0 is retrospective and descriptive. The whole window lies in the past at design time. Nothing is, or will be represented as, prospectively preregistered. No backdating: this file carries its design date; the actual seal time is recorded by the host after the commit.
- **V1 exposure.** V1 (sealed 2026-09-17, hash-verified) analyzed overlapping series — Hyperliquid ETH/BTC funding, Coinbase ETH-USD/BTC-USD hourly candles, and Aave v3 Arbitrum USDC supply rates via the **same two DefiLlama pool series** used here (V1 D6) — over 2023-06-23 → ≈2026-09-17, with results known to this organization. Study 0's raw files are fresh retrievals of 2026-11-01, not reused V1 files, and no corrected input is reused; the overlap in sources and window is prior analytical exposure and is disclosed as such. No V1 result, script, or processed output is imported. Later OpenBasis work (V2/V3) exists; per director instruction it was not inspected, and no prior result, verdict, or script was read, executed, or imported in preparing this design.
- **Prior Study 0 incarnation.** An earlier working copy of Study 0, under the same approved scope, sealed a prior DESIGN.md (commit `86a5dc9c3ab0ff312f3fd1579f98a032b7519019`) and was stopped by the host coordinator **before any analysis**, when the apyBase/apy rate-convention question was escalated; the director's disposition is `study/DIRECTOR_DECISION_S6_RATE_CONVENTION.md` and Amendment A3. The director authorized a fresh restart at the pre-seal boundary (Amendment A4); the prior seal commit and its evidence are preserved per the director's record outside this working copy. No Study 0 funding, spot-risk, cost, or reserve result has been computed in either incarnation.
- **Pre-seal activity in this repository (all permitted source-definition, manifest, hash and coverage work; no result computation):** raw retrievals 2026-11-01 19:13–19:27 UTC; adapter and endpoint evidence pinned 19:13–19:15 UTC; coverage inventory (`data/COVERAGE.json` — counts, timestamps, duplicates, gaps, and the declared unit check: modal exact fundingRate strings and apyBase null counts); manifest built 19:27:07 UTC and independently re-verified by the builder; V1 copy hash-verified and read in full by the builder (read-only); structural samples of raw pages read for timestamp semantics. An approved design proposal preceded this file and is preserved in the director's records outside the repository (D7 provenance note: the repository scaffold was created under director instruction after verifying the location was empty; it was retained, not reinitialized).
- The audit trail retains this section's facts; publication wording may compress but never contradict them (S7).

## 13. Environment, execution and verification

- **Execution environment (decision D4, pinned).** The approved repository host environment: macOS arm64 (Darwin), macOS 26.6.2 (build 25G83), CPython 3.13.15 at `/opt/homebrew/bin/python3.13` (Homebrew), as returned by mechanical host verification on 2026-11-01, pre-seal. All Study 0 result computation and every reproduction run execute in this host environment. Rebuild commands invoke the explicit interpreter path `/opt/homebrew/bin/python3.13`, never a PATH-resolved `python3`; the host's `/usr/bin/python3` (3.9.6) is not used. Exact dependency pins and the rebuild commands are recorded in `study/ENVIRONMENT.md`, committed alongside the research calculations. Under the Amendment A4 split, the builder authors the scripts, artifacts and commit requests; execution of the pinned rebuild commands on the host, like all Git operations, is performed host-side by the mechanical coordinator, which edits no substantive content. The retrieval and inventory scripts used only the Python standard library and standard shell tools (`curl`, `shasum`); their outputs are frozen by hash, so input provenance rests on the retrieval logs and `data/MANIFEST.json`. No cross-platform certification is made; the reproduction claim is scoped to this pinned environment only (V1 §12 boundary preserved, §11 row 15).
- Deterministic conventions: `TZ=UTC`; sorted keys and fixed float formats in deterministic outputs; `\n` line endings; no embedded timestamps in deterministic result files (retrieval logs and manifests record real times and are not deterministic outputs).
- Git operations follow Amendment A4 (host-Git mechanical protocol): the builder writes artifacts and commit requests; the host coordinator verifies hashes and commits.
- **Verification duty before every handoff (canonical):** reproduce all results from the frozen raw inputs in a clean output directory with commands, environment and hashes recorded; synthetic fixtures for funding signs, rates, missingness and run censoring; independent recomputation of both assets' full-window funding summaries and the 29 bps worksheet without the production aggregation functions; source-record checks of each asset's earliest complete calendar month and each reserve segment's first and last complete month, documenting absence rather than substituting; source-to-output trace for every public quantitative claim; V1 consistency recheck; E7 scan of every public artifact.

## 14. Deliverables and commit order

1. `DESIGN.md` (this file) — committed ALONE by the host coordinator (commit request `study/commit_requests/COMMIT_REQUEST_001_DESIGN_SEAL.md`); actual seal time and commit hash recorded afterward in `study/SEAL_RECORD.md`.
2. Pinned raw inputs, `data/MANIFEST.json`, `data/COVERAGE.json`, `data/source_consistency/V1_DESIGN.md`, retrieval/inventory scripts, prompts (originals, amendments, working copies, comparison record), director decision records, and commit requests — committed next, before any result computation output.
3. Research calculations under `study/`; results and `reports/STUDY_0.md` with data/assumption appendix and Audit Process (S8 wording: names S1–S9, actual round count and outcome, the neutral working-role statement — persona titles describe working roles, not individual credentials — and the findings fixed, not merely the pass).
4. `frozen_rules/study0.json` (grid, window, series registry with hashes, conventions including type 7, decimal/float disciplines, run and censoring definitions, A2 bound, cost constants) + human summary `frozen_rules/STUDY0_RULES.md`.
5. `study/CHANGELOG.md`; complete audit trail under `audit/` (`findings_roundN.md`, `verdict_roundN.md`, originals and superseded files retained); final artifact manifests.

Each submission identifies its commit. Only the auditor's written verdict ends a round; maximum five rounds counting every written verdict; if round 5 is not PASS, both roles record positions in `audit/DEADLOCK.md` and stop. A needed design change goes to the director; if authorized, the old seal is preserved, already-observed results disclosed, and the amended DESIGN.md committed alone before rerunning, keeping the round count.

---
*End of sealed design. No Study 0 result has been computed as of this file's writing; result computation begins only after the host coordinator reports that the DESIGN.md-only commit is complete.*
