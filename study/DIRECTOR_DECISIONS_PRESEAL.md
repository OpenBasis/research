# Study 0 — Director Decisions Before Seal

**Status:** Approved by the director.
**Protocol position:** Pre-seal, before Study 0 result computation. Zero written audit verdicts.
**Evidence:** The director replied, “good . go with your recommend,” to the following recommendation package.

## Approved recommendation package

### D1 — Aave reserve-rate source

Choose DefiLlama daily data. Use its dated Aave series, keeping native USDC and USDC.e separate. Do not add a full on-chain event reconstruction plus cross-check pipeline now. Clearly label this as aggregator evidence, subject to coverage and provenance checks. This requires your explicit amendment to the prompt’s “primary dated observations” requirement.

### D2 — Hourly reserve construction

Use a bounded daily-snapshot approximation. Apply each snapshot only after its timestamp, with a maximum validity tied to the documented sampling cadence. Missing updates remain gaps; no indefinite carry. Call the derived hourly rates modeled approximations, not observed hourly returns. This also needs an explicit exception to “no fill.” Before sealing, verify the exact field and APR/APY convention. The current DefiLlama Aave adapter assigns liquidityRate directly to apyBase, so the field name alone does not justify assuming compounded APY. Historical conventions still need checking.

### D3 — Funding settlement-to-bucket mapping

Use the compensated interval’s start: t−1h. That keeps funding aligned with the declared bucket-start convention. Retain the original payment timestamp too. Retrieve the November 1 00:00 settlement to cover the final October 31 hour; that supplies boundary evidence, rather than extending the study window.

### D4 — Execution environment

Approve the existing Mac environment. Pin the actual interpreter, dependencies and rebuild commands. No cross-platform certification project at this stage.

### D5 — Hyperliquid retrieval depth

Approve stop-and-escalate. If the required Hyperliquid history is unavailable, report the exact gap. No silent source substitution, shortened window or endless search for a workaround.

### D6 — Tables and figures

Keep the evidence; simplify its presentation. Retain all required numerical outputs, but put detailed monthly and per-run tables in appendices or data files. Use two main figures: combined ETH/BTC funding time series and monthly totals. Drop the redundant histograms. Keep the V1 consistency matrix internal.

### D7 — Repository scaffold

Keep the existing scaffold. Do not reinitialize Git. Correct the provenance statement: we created it under your instruction after verifying emptiness. Preserve the proposal and stopped-session record. The first commit must still contain DESIGN.md alone; the incidental .DS_Store must not enter that commit.

## Binding execution clarification

This approval permits the proposed scope, with D1–D2 recorded as explicit methodological amendments before sealing, and progression to evidence completion, sealing, and round-1 execution under the existing protocol. It does not authorize arbitrary new sources or unanswered conventions.

Definition/source documentation and raw-data inventory may proceed before the seal. Study result computation may begin only after DESIGN.md is committed alone.

If the exact historical rate convention, base-versus-total field, sampling cadence or validity bound, or required coverage cannot be established from supported sources, stop and escalate before the seal. Do not choose a validity bound by intuition.

The current adapter URL is a source-definition lead only:
https://raw.githubusercontent.com/DefiLlama/yield-server/master/src/adaptors/aave-v3/index.js

No fees or subscriptions are authorized. No prior results or V2/V3 exploration is authorized. The exact V1 seal source remains read-only and binding as a consistency constraint.

Both canonical prompts and DESIGN.md must agree on the approved D1–D2 amendments. Preserve the original approved prompt versions and history. Make no unrelated prompt edits.
