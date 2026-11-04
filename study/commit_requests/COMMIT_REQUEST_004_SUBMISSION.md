# COMMIT REQUEST 004 — FIGURES AND ROUND-1 SUBMISSION (fourth commit)

**From:** BUILDER (no Git commands run; Amendment A4 host-Git mechanical protocol)
**Written:** 2026-11-02 UTC
**Boundary:** figures, figure run record, and the round-1 submission package. Parent must be
commit `7dba8b654ab955b3348a96d249512c0571ba8960`. **The commit created here is the round-1
submitted commit** handed to the auditor.

## Suggested commit message

    Study 0: figures, figure run record, round-1 submission

## Pre-commit verification for the coordinator

1. HEAD is `7dba8b65…8960`; `DESIGN.md` still hashes to `b4f91118…9c06` and is not restaged.
2. Stage exactly the 7 paths below; every byte count and SHA256 must match. `study/CHANGELOG.md`
   is a MODIFIED tracked file; the figures and `RUN_005_figures.log` are the host-produced bytes
   recorded in HOST_RECEIPT_004 (hashes below restate the receipt's values).
3. After staging, the only remaining untracked path must be
   `study/commit_requests/COMMIT_REQUEST_004_SUBMISSION.md` (this file; queued for the next
   boundary). `study/src/__pycache__/` stays ignored. Anything else: report, do not stage.

## After committing

Write `study/host_receipts/HOST_RECEIPT_005_SUBMISSION.md` recording the commit hash, UTC time
and tree, and report them to the builder: that commit identifies the round-1 submission for the
auditor. No execution request accompanies this boundary.

## Paths to stage and commit — exactly 7

| path | bytes | sha256 |
|---|---|---|
| `reports/figures/F1_funding_hourly.svg` | 852935 | `19822b5d863f81e6ce839aa7eebfcdcd9a2c93713a8dea8644c517cf93e1e075` |
| `reports/figures/F2_monthly_totals.svg` | 11459 | `9343813e3365c3109573cab66538617bd86fb6172941c6dd0772f91de8dac49e` |
| `study/run_logs/RUN_005_figures.log` | 269 | `97ea9b202dc9832c8c5716e36b5fcd44f1fa632052c694129b4a0ca5541ca64c` |
| `study/host_receipts/HOST_RECEIPT_004_RESULTS_FIGURES.md` | 1496 | `dd08c60c6ead0ca5275488942b995f616c10b364305f6e57fc41995829c0c4cf` |
| `study/commit_requests/COMMIT_REQUEST_003_RESULTS_REPORT.md` | 6671 | `165efeaba382822fa8ddeed3fca5e3bf314080170ffefb71d83303170ebf69c0` |
| `study/SUBMISSION_ROUND1.md` | 7425 | `06298ecfaad69c4147f39591763539cc97486b820123964829ee9fcd0e6dd81b` |
| `study/CHANGELOG.md` | 9131 | `6ee6bb4c9d1671a7f090fddfce7bf9828271ec73a9c96243bc8c7854109205bd` |

End of request. The builder stops at this boundary; the round-1 clock starts at the auditor's
review of the submitted commit, and only the auditor's written verdict ends the round.
