# Study 0 — Round 2 Submission (builder → auditor)

**Submitted commit:** the commit created from `study/commit_requests/COMMIT_REQUEST_005_ROUND2_FIXES.md` — the repository HEAD whose hash the host coordinator records in `study/host_receipts/HOST_RECEIPT_007_ROUND2_SUBMISSION.md` (this file is inside that commit, so it identifies it by construction).
**Commit chain:** seal `9d3ed18144d4cebc2b3c511ad596f3496e833be2` (DESIGN.md alone) → inputs/spec `9a6212ac726ebd93efec4aff47e0778deb16cfd0` → results/report `7dba8b654ab955b3348a96d249512c0571ba8960` → round-1 submission `85d24990293a36a858530f406c8ee1217ce0a7b5` → round-1 audit record `eb6682e031c2add426567774d7150e0b177c24dd` → this submission.
**Round status:** round 2 of a maximum 5. One written verdict exists: **Round 1 — FAIL** (`audit/verdict_round1.md`; R1-01 BLOCKER, R1-02 MAJOR, R1-03 MAJOR, R1-04 MINOR). Only the auditor's written verdict ends this round.

## 1. Responses to the Round 1 findings

| Finding | Response | Where |
|---|---|---|
| **R1-01** (BLOCKER, S7/E7) | Both barred sentences removed. §2 no longer contains the negated out-of-boundary reference; the remaining scope negations (backtest / operating policy / return hurdle / net return) were individually adjudicated benign in the auditor's round-1 scan and are retained, so the scope statement stays truthful. §11's forward-promise paragraph was replaced by the factual audit record. Every public artifact was rescanned for E7 after the edits (§3.7 below). | `reports/STUDY_0.md` §2, §11 |
| **R1-02** (MAJOR, S2+S5/E2+E4) | The removal path offered in the finding was chosen. §10.4 no longer compares reserve yield with funding levels; it now states that Study 0 computes no such comparison (different coverages; no common-timestamp intersection performed). The per-segment reserve description (T10) and the symbolic capital bridge (T11) stand unchanged. No unsealed intersection analysis was added; the sealed finite analysis list (DESIGN §7) is unchanged. | `reports/STUDY_0.md` §10.4 |
| **R1-03** (MAJOR, S8/E5) | §11 now records the actual round count and outcome (Round 1: FAIL, verdict 1 of at most 5), the per-criterion results, all four findings with severities and dispositions, the auditor's independent-verification result, the location of the verbatim audit trail, and the neutral working-role statement. It states that Round 2's verdict is unwritten and claims no pass. No forward promise remains. | `reports/STUDY_0.md` §11 |
| **R1-04** (MINOR, S2/E2) | All three "outage" occurrences relabeled missing-candle gaps, with the cause explicitly not established — consistent with DESIGN §5.2 and the source's documented missing-publication semantics. No number changed. | `reports/STUDY_0.md` §3 table, §9, §10.6 |

The failed round-1 verdict and findings are retained verbatim (`audit/findings_round1.md`, `audit/verdict_round1.md`, committed `eb6682e0…24dd`); nothing was edited or superseded silently. The changelog answers each finding (`study/CHANGELOG.md`, Round 2 entries).

## 2. What changed, what did not

**Changed (prose only):**

| File | Change |
|---|---|
| `reports/STUDY_0.md` | The four fixes above; 20,130 bytes, SHA256 `4e32062e99806917685c28b595e4ac9c4adc29035b9c0cb43a6825e0a4739522` |
| `study/CHANGELOG.md` | Round-1 verdict record and Round-2 response entries; 12,667 bytes, SHA256 `627c0c40103e5aef8b1158cbac970a37036385b97a3685ebdd2fc04be7e54fa2` |
| `study/SUBMISSION_ROUND2.md` | This file (new) |

**Unchanged — builder-verified byte identity against the round-1-audited state:** `git --no-optional-locks diff --stat HEAD` (HEAD = `eb6682e0…24dd`) shows only the two files above modified; the only untracked paths are the round-1 bookkeeping pair staged with this commit and this submission's own request file. Specifically re-hashed: `reports/results_study0.json` = `f425e2e73b9069f2c8c6101376df02295d44db631cb208f7c0d94f57c6859788`; `DESIGN.md` = `b4f911187a17593f06e173a014cc923f3ee1708ddb393eaa2338661189eb9c06`; `F1_funding_hourly.svg` = `19822b5d863f81e6ce839aa7eebfcdcd9a2c93713a8dea8644c517cf93e1e075`; `F2_monthly_totals.svg` = `9343813e3365c3109573cab66538617bd86fb6172941c6dd0772f91de8dac49e` — all equal to the round-1 verified values. No data file, analysis or verification script, frozen rule, table, figure, or machine result changed. No sealed definition, formula, constant, or boundary changed.

## 3. Builder verification record (duty → evidence, round 2)

1. **Reproduction from frozen inputs in a clean output directory** — no result-bearing artifact changed (byte identity, §2); the round-1 host reproduction (RUN_003: `diff -r` clean; results JSON byte-identical) and the auditor's independent round-1 reproduction cover these exact bytes. In addition, a fresh host re-verification is a **pre-commit gate** in `COMMIT_REQUEST_005_ROUND2_FIXES.md`: fixtures, clean-directory reproduction + table diff + results-JSON hash, and the independent recomputation, each with its expected outcome stated; any deviation stops the commit and is reported instead of committed.
2. **Synthetic fixtures** — code unchanged since the round-1 34/34 PASS (RUN_001); host re-run requested at the gate (RUN_006 expected 34/34 PASS).
3. **Independent recomputation (funding summaries, 29 bps worksheet; no production aggregation functions)** — code and inputs unchanged since round-1 PASS (RUN_004); host re-run requested at the gate (RUN_008).
4. **Boundary-month source-record checks** — inputs unchanged; the round-1 record stands (`study/SUBMISSION_ROUND1.md` §2.4) and remains re-runnable from the frozen raw files. Nothing was substituted.
5. **Source-to-output trace of changed prose** — §10.4 "~4.5–4.9%/yr" → T10 annualized means `0.04535…`/`0.04871…`; §3/§9/§10.6 gap statements → T01 (10 missing closes per product, in two 5-hour runs 2025-10-25T16:00–20:00Z and 2026-05-08T02:00–06:00Z, duplicates 0/0); §11 audit-record figures → `audit/verdict_round1.md` / `audit/findings_round1.md` (FAIL; one BLOCKER, two MAJOR, one MINOR; S1/S3/S4/S6/S9 pass, S2/S5/S8 partial, S7 fail; 331/331 independent value comparisons; 349 pinned files, 0 hash mismatches). All other public numbers are unchanged text over unchanged tables.
6. **V1 consistency recheck** — no boundary-touching statement changed; `study/V1_CONSISTENCY_T12.md` unchanged. The public report no longer uses the word "outage" anywhere, removing even surface tension with T12 row 12 ("no outage analysis or claim exists in Study 0"). No conflict.
7. **E7 rescan of every public artifact after the edits** (`reports/STUDY_0.md`, T1–T11, both figure SVG texts) — wordlist (prototype / implement / codebase / build / engine / deploy / coming-soon / roadmap / teaser / upcoming / release / later-work / will-be) plus contextual reading. All hits adjudicated benign: "builder" (the S8-required working-role disclosure), "rebuilds" (the reproducibility statement, present and unflagged in round 1), and the quoted historical label "outages" inside §11's R1-04 disposition (it describes the removed defect and makes no cause claim). No prototype/implementation/codebase reference, no post-study result, no promise of later work or of updating any public text.

## 4. Notes for the auditor

- The R1-02 fix is the removal path; if a quantitative cross-series comparison is ever wanted, it would need the sealed intersection/coverage rules (DESIGN §4/§6.4) and is **not** added here.
- §11's quantitative statements about the audit are quotations of the committed round-1 audit record, not new computation.
- The round-1 bookkeeping pair (`audit/COMMIT_REQUEST_ROUND1.md`, `study/host_receipts/HOST_RECEIPT_006_AUDIT_ROUND1.md`) is staged with this commit per the established pattern; `COMMIT_REQUEST_005_ROUND2_FIXES.md` itself remains untracked, queued for the next boundary, as are the RUN_006–008 logs the gate produces (the builder cannot pre-hash host-produced bytes under A4.2).
- The builder ran no mutating Git command; worktree inspection used `git --no-optional-locks` only.

The builder hands off. Per protocol, the round ends only with the auditor's written verdict (`audit/findings_round2.md`, `audit/verdict_round2.md`); the builder will answer every finding.
