# Study 0 — Post-PASS finalization addendum

**Director-authorized verification of:** finalization commit `2dc6c3889166e38990fc4deeb2b18424451905f8`, parent `4cb3c415d87e7be845fb443cb74268b586f98cd5`.
**Disposition:** VERIFIED. This is a post-PASS finalization check, **not a third audit round or a replacement verdict**. The written Round 2 PASS in `audit/verdict_round2.md` remains unchanged, as does the original Round 2 submitted commit `fcd0505b39b57b94bb2b2569453a9c0a66d1e519`.

## Exact change and retained record

`git diff --name-status 4cb3c415d87e7be845fb443cb74268b586f98cd5 2dc6c3889166e38990fc4deeb2b18424451905f8` yields exactly three paths:

| Path | Change | Verification |
|---|---|---|
| `reports/STUDY_0.md` | Two paragraphs in §11 Audit Process replaced (2 insertions, 2 deletions) | Line 122 now states that two written rounds and verdicts exist; line 129 records Round 2 PASS, all S1–S9 passing and R1-01–R1-04 closed. Those facts agree with the unchanged written Round 1 FAIL and Round 2 PASS. |
| `audit/COMMIT_REQUEST_ROUND2.md` | Added previously untracked audit bookkeeping | Its SHA256 is `8a707a8731f8d1a85039f04f60ffefc5e92ee13477c5f71c66f2076aac6477b3`, the value previously given to the host. No substantive study text. |
| `study/host_receipts/HOST_RECEIPT_008_AUDIT_ROUND2.md` | Added previously untracked host receipt | It records the parent PASS audit-record commit, Round 2 file hashes and mechanical operations. No substantive study text. |

The full report diff is confined to §11. The R1-01–R1-04 findings-fixed bullets and the neutral working-role disclosure are byte-unchanged. The new status follows the written verdict, so the public Audit Process now names the actual two-round count and final PASS without claiming that the builder awarded it. `git diff --check` is clean.

The four original audit files are unchanged from their committed copies and retain these SHA256 values: `audit/findings_round1.md` `d22818542015ae0b6f781d0affba46578d09198628f36837e73b22dcaf7e2c8f`; `audit/verdict_round1.md` `a84b0cf9a17d123393faf4640fa7356c99c71994e2464745ada82e06125a881e`; `audit/findings_round2.md` `966dffdfd8b367a685770b4806bf826bad418adbc227017cc3a64b5811d56b9a`; `audit/verdict_round2.md` `7bee4b7b7988c5f140be5f96678d4bde4b364b3776bf84ecc325f0d641ce5fef`.

`git diff --quiet` between the PASS audit-record commit and finalization commit succeeds for `DESIGN.md`, all `data/`, `frozen_rules/`, `reports/results_study0.json`, `reports/tables/`, `reports/figures/`, `study/src/` and the four audit findings/verdict files. No analysis, numerical result, source, scope or seal changed. Sealed `DESIGN.md` still has SHA256 `b4f911187a17593f06e173a014cc923f3ee1708ddb393eaa2338661189eb9c06`; results JSON remains `f425e2e73b9069f2c8c6101376df02295d44db631cb208f7c0d94f57c6859788`; F1/F2 retain `19822b5d…e075` / `9343813e…c49e`.

## Updated public artifact and boundary

The final `reports/STUDY_0.md` is byte-identical to the file in finalization commit `2dc6c38` and has **20,375 bytes, SHA256 `95e29a6068432ad3815b5f5d7470a6adcd070198b39cf620b9a805b56fb28f5d`**. This matches `study/commit_requests/COMMIT_REQUEST_006_AUDIT_PROCESS_FINALIZATION.md` and `study/host_receipts/HOST_RECEIPT_009_AUDIT_PROCESS_FINALIZATION.md`. The preceding PASS-state report hash is `4e32062e99806917685c28b595e4ac9c4adc29035b9c0cb43a6825e0a4739522`; the changed bytes are precisely the two §11 status paragraphs.

I rescanned `reports/STUDY_0.md`, T1–T11 and both public SVG texts for prototype, implementation, codebase, build/engine, deployment, later-work and release-promise terms, and read the hits in context. The quoted word “outages” at report line 127 describes the corrected Round 1 label and expressly says the cause was not established. “Rebuilds” at line 141 describes reproducibility, and “builder” at line 129 is the required working-role disclosure. Neither is a prohibited implementation or future-work claim. The report still ends its analysis at the design conclusion (line 116), followed only by Audit Process and data appendices. No new E7 or chronology defect appears.

The host's post-finalization check logs (`RUN_009`–`RUN_011`, receipts 009) record 34/34 fixtures passed, byte-identical rebuilt result JSON and tables, and a passing separate funding/cost check. Their listed SHA256 values match the actual untracked log bytes. These runs support the unchanged result-bearing artifacts; they are not a new audit round.

**Conclusion:** the director-authorized finalization changed only the factual public Audit Process status in substance. The sealed scope, numerical outputs, publication boundary, original findings and both written verdicts remain intact. No new finding or verdict is issued.
