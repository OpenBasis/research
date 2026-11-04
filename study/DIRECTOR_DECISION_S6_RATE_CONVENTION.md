# Director Decision — S6 Rate-Convention Disposition

Recorded: 2026-11-01 UTC

## Verbatim decision context

Coordinator:

> I need to qualify the seal update: the commit was mechanically correct, but the builder sealed with an unresolved consistency issue. I’ve stopped it before analysis.
>
> The sealed design records that Study 0’s Aave apyBase evidence supports APR, while V1 treated its DefiLlama apy input as compounded APY. DESIGN.md itself flags this for director resolution under S6. That should have been escalated before sealing.
>
> My recommendation is to preserve the existing seal and evidence, authorize a design amendment using the evidenced Study 0 convention, and explicitly record the V1 issue for later review without changing V1 now. This requires your decision on the strict consistency requirement; I won’t resolve it by wording alone.
>
> Separately, I declined a request for repository-wide permanent-delete permission to clear two Git lock files. I’m checking those exact locks without deleting anything.
>
> Do you approve the proposed handling of the rate-convention discrepancy?

Coordinator clarification:

> One important qualification from the evidence: Study 0 uses apyBase, while V1’s seal refers to apy. We have not established that V1 consumed the same field, so this is an unresolved interpretation mismatch, not yet a demonstrated V1 calculation error. The mapping remains the precise unresolved director issue.

Director:

> yes

## Binding disposition

- Preserve original seal commit `86a5dc9c3ab0ff312f3fd1579f98a032b7519019` and its evidence.
- Study 0 uses the evidenced `apyBase` APR convention.
- Record the unresolved V1 generic `apy` versus `apyBase` mapping as a later-review issue, not as a proven V1 calculation error.
- Do not modify V1.
- The director's S6 disposition is specific to this documented difference and does not relax any other consistency requirement.
- Amend DESIGN.md and commit DESIGN.md alone before analysis, preserving the original and amended hashes and history.
