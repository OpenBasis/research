# OpenBasis Study 0 — Final Manifest

## Outcome

- Final written audit outcome: **PASS**.
- Written audit rounds: **2**.
- Round 1: FAIL — one BLOCKER, two MAJOR findings and one MINOR finding.
- Round 2: PASS — all S1–S9 pass; R1-01 through R1-04 closed; no new finding.
- Post-PASS finalization: director-authorized factual Audit Process update, independently verified in `audit/FINALIZATION_ADDENDUM.md`; not a new audit round and not a replacement verdict.

## Canonical deliverables

| Deliverable | Path |
|---|---|
| Public study | `reports/STUDY_0.md` |
| Sealed design | `DESIGN.md` |
| Frozen rules, machine-readable | `frozen_rules/study0.json` |
| Frozen rules, human summary | `frozen_rules/STUDY0_RULES.md` |
| Round 1 findings | `audit/findings_round1.md` |
| Round 1 verdict | `audit/verdict_round1.md` |
| Round 2 findings | `audit/findings_round2.md` |
| Round 2 PASS verdict | `audit/verdict_round2.md` |
| Post-PASS verification | `audit/FINALIZATION_ADDENDUM.md` |
| Complete change record | `study/CHANGELOG.md` |
| Seal record | `study/SEAL_RECORD.md` |
| Input manifest | `data/MANIFEST.json` |
| Coverage record | `data/COVERAGE.json` |
| Result JSON | `reports/results_study0.json` |
| Final artifact hashes | `study/FINAL_ARTIFACT_HASHES.sha256` |

The repository also retains every commit request, host receipt, verification log, deterministic table and figure, frozen input, source-definition record and independent audit calculation required to reproduce or inspect the study.

## Preserved commit chain

1. `9d3ed18144d4cebc2b3c511ad596f3496e833be2` — DESIGN.md committed alone.
2. `9a6212ac726ebd93efec4aff47e0778deb16cfd0` — pinned inputs, evidence, frozen rules, environment and analysis code.
3. `7dba8b654ab955b3348a96d249512c0571ba8960` — results, run records, public study and V1 matrix.
4. `85d24990293a36a858530f406c8ee1217ce0a7b5` — Round 1 submission.
5. `eb6682e031c2add426567774d7150e0b177c24dd` — Round 1 findings and FAIL verdict.
6. `fcd0505b39b57b94bb2b2569453a9c0a66d1e519` — Round 2 fixes and submission.
7. `4cb3c415d87e7be845fb443cb74268b586f98cd5` — Round 2 findings and PASS verdict.
8. `2dc6c3889166e38990fc4deeb2b18424451905f8` — director-authorized factual Audit Process finalization.
9. `5baad591f50d4b53ed21b29934be80f3079188db` — post-PASS finalization addendum.

## Integrity

- Sealed DESIGN.md SHA256: `b4f911187a17593f06e173a014cc923f3ee1708ddb393eaa2338661189eb9c06`.
- Final public study SHA256: `95e29a6068432ad3815b5f5d7470a6adcd070198b39cf620b9a805b56fb28f5d`.
- Round 2 PASS verdict SHA256: `7bee4b7b7988c5f140be5f96678d4bde4b364b3776bf84ecc325f0d641ce5fef`.
- Post-PASS finalization addendum SHA256: `72597f7bd13130830e2790aff9bdfd41fc2414ea7057e4c582637be23cc3dcff`.
- Results JSON SHA256: `f425e2e73b9069f2c8c6101376df02295d44db631cb208f7c0d94f57c6859788`.

See `study/FINAL_ARTIFACT_HASHES.sha256` for the final deliverable hash list and `data/MANIFEST.json` for the complete pinned-input manifest.
