# Mechanical host commit request — Round 1 audit record

This request is bookkeeping for the host coordinator under Amendment A4. The auditor has written the Round 1 findings and FAIL verdict; no mutating Git command has been run by the auditor. Verify unchanged bytes and unexpected files, then stage and commit **only** the seven listed paths. The request file itself is not in this commit and may be retained for the next boundary. Do not edit substantive content.

**Expected parent:** submitted commit `85d24990293a36a858530f406c8ee1217ce0a7b5`.
**Suggested commit message:** `Study 0: retain round-1 audit findings and verdict`.

| Exact path to stage | SHA256 |
|---|---|
| `audit/independent_round1.py` | `b4836d198b62be74509f923f38d8ef5c556d98184ee9139b39ddfa25f4178ef9` |
| `audit/compare_round1.py` | `c4ecbf914e609d688da99a0344f08d663ada31265868b51dc2781a5d9ad2815a` |
| `audit/independent_round1_results.json` | `03fee6dad54f2648045b1f86aa6e382afb7b8b924a7a97b70d98b1850e02f610` |
| `audit/findings_round1.md` | `d22818542015ae0b6f781d0affba46578d09198628f36837e73b22dcaf7e2c8f` |
| `audit/verdict_round1.md` | `a84b0cf9a17d123393faf4640fa7356c99c71994e2464745ada82e06125a881e` |
| `study/commit_requests/COMMIT_REQUEST_004_SUBMISSION.md` | `6fe7997b8091477ea80e5d3c45c6172014497970293a38388da945fb75966833` |
| `study/host_receipts/HOST_RECEIPT_005_SUBMISSION.md` | `d5d38c5e4041075182b4c52c06ab29e31f80d5b3c485b0640e43846c7705c9af` |

The host should record the actual audit-record commit hash and UTC time in its receipt. The verdict itself is final for Round 1 regardless of when the mechanical commit is made; the next builder submission is Round 2.
