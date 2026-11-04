# COMMIT REQUEST 005 — ROUND-2 FIXES AND SUBMISSION (fifth commit)

**From:** BUILDER (no Git commands run; Amendment A4 host-Git mechanical protocol)
**Written:** 2026-11-02 UTC
**Boundary:** round-2 fixes to the public report (answers to R1-01…R1-04), changelog, the round-2
submission note, and the round-1 bookkeeping pair. Parent must be the round-1 audit-record commit
`eb6682e031c2add426567774d7150e0b177c24dd`. **The commit created here is the round-2 submitted
commit** handed to the auditor.

## Suggested commit message

    Study 0: round-2 fixes and submission (answers R1-01..R1-04)

## Pre-commit verification and re-verification gate for the coordinator

1. HEAD is `eb6682e0…24dd`; `DESIGN.md` still hashes to
   `b4f911187a17593f06e173a014cc923f3ee1708ddb393eaa2338661189eb9c06` and is not restaged.
2. **Re-verification runs (pinned host, from the repository root; record logs; any deviation:
   stop, do not commit, report to the builder).** These re-execute the standing verification duty
   on the unchanged result artifacts before the handoff completes:

       env TZ=UTC PYTHONHASHSEED=0 /opt/homebrew/bin/python3.13 study/src/test_fixtures.py \
           > study/run_logs/RUN_006_fixtures_r2.log 2>&1

   Expected: 34/34 PASS (the leading caught `ABORT` line is the deliberate conflicting-duplicate
   fixture).

       env TZ=UTC PYTHONHASHSEED=0 /opt/homebrew/bin/python3.13 study/src/compute_study0.py \
           --out /private/tmp/study0_round2_check/reports > study/run_logs/RUN_007_repro_r2.log 2>&1
       diff -r reports/tables /private/tmp/study0_round2_check/reports/tables \
           >> study/run_logs/RUN_007_repro_r2.log 2>&1
       shasum -a 256 reports/results_study0.json \
           /private/tmp/study0_round2_check/reports/results_study0.json \
           >> study/run_logs/RUN_007_repro_r2.log 2>&1

   Expected: diff exit 0 with no output; both JSON hashes
   `f425e2e73b9069f2c8c6101376df02295d44db631cb208f7c0d94f57c6859788`.

       env TZ=UTC PYTHONHASHSEED=0 /opt/homebrew/bin/python3.13 study/src/independent_check.py \
           > study/run_logs/RUN_008_independent_r2.log 2>&1

   Expected: all checks PASS.
3. Stage exactly the 5 paths below; every byte count and SHA256 must match.
   `reports/STUDY_0.md` and `study/CHANGELOG.md` are MODIFIED tracked files; the other three are
   new/untracked. `audit/COMMIT_REQUEST_ROUND1.md`'s hash equals the value already recorded in
   `study/host_receipts/HOST_RECEIPT_006_AUDIT_ROUND1.md` (unchanged bytes).
4. After staging, the only remaining untracked paths must be this request file and the three
   `RUN_006–008` logs produced by step 2 (all queued for the next boundary — the builder cannot
   pre-hash host-produced bytes under A4.2); `study/src/__pycache__/` stays ignored. Anything
   else: report, do not stage.

## After committing

Write `study/host_receipts/HOST_RECEIPT_007_ROUND2_SUBMISSION.md` recording the commit hash, UTC
time and tree, the three run exit statuses and the SHA256 of each RUN_006–008 log, and report
them to the builder: that commit identifies the round-2 submission for the auditor.

## Paths to stage and commit — exactly 5

| path | bytes | sha256 |
|---|---|---|
| `reports/STUDY_0.md` | 20130 | `4e32062e99806917685c28b595e4ac9c4adc29035b9c0cb43a6825e0a4739522` |
| `study/CHANGELOG.md` | 12667 | `627c0c40103e5aef8b1158cbac970a37036385b97a3685ebdd2fc04be7e54fa2` |
| `study/SUBMISSION_ROUND2.md` | 8308 | `f2f89e3c31218ed67a3102738fbd1b3f23fd060cc250e5d7ea7c553463762abc` |
| `audit/COMMIT_REQUEST_ROUND1.md` | 1670 | `c4db3ebecac38190b1b812b8aaf27009d1e18e37b86549ec2b9bf21efcac0b0d` |
| `study/host_receipts/HOST_RECEIPT_006_AUDIT_ROUND1.md` | 1531 | `539bc8682aa9fe133529af673e0603103ac6043851abb487bcd5b5a85260b415` |

End of request. The builder stops at this boundary; only the auditor's written verdict ends
Round 2.
