# COMMIT REQUEST 001 — DESIGN SEAL (first commit; DESIGN.md ALONE) — REVISED

**From:** BUILDER (no Git commands run; Amendment A4 host-Git mechanical protocol)
**Written:** 2026-11-01 UTC
**Boundary:** Study 0 design seal. This must be the FIRST commit of the repository.
**Supersedes:** the earlier 2026-11-01 version of this request (DESIGN.md at SHA256 `b07ad201388afd938bdd8933a0d881763c0491a39814ff1e3c99a51466aeed04`), withdrawn before any commit on the coordinator's stop: that DESIGN.md revision pinned the wrong execution environment. DESIGN.md §13 now pins the approved host environment (macOS arm64, macOS 26.6.2 build 25G83, CPython 3.13.15 at `/opt/homebrew/bin/python3.13`; explicit-interpreter rebuild commands) per decision D4 and the coordinator's mechanical host verification.

## Paths to stage and commit — exactly one

| path | bytes | sha256 |
|---|---|---|
| `DESIGN.md` | 36423 | `b4f911187a17593f06e173a014cc923f3ee1708ddb393eaa2338661189eb9c06` |

No other path may enter this commit: no receipt, prompt, data, manifest, coverage file, script, decision record, working-prompt file, this request file, or any other file. If any `.DS_Store` or other incidental file has appeared, it must not be staged.

## Suggested commit message

    Study 0: seal DESIGN.md (committed alone; first commit)

## Pre-commit verification for the coordinator

1. Repository has zero commits (fresh restart; `.git` contains no objects/refs).
2. `shasum -a 256 DESIGN.md` equals the hash above; byte count equals 36423.
3. Staged set contains exactly one path: `DESIGN.md`.
4. All other working-tree files remain untracked and unchanged. Expected untracked content at this boundary (not staged now; queued for commit 002): `data/**` (raw inputs, `MANIFEST.json`, `COVERAGE.json`, `source_consistency/V1_DESIGN.md`), `study/prompts/**` (originals, amendments, working copies, `PROMPT_COMPARISON.md`), `study/src/**`, `study/DIRECTOR_DECISIONS_PRESEAL.md`, `study/DIRECTOR_DECISION_S6_RATE_CONVENTION.md`, and `study/commit_requests/COMMIT_REQUEST_001_DESIGN_SEAL.md` (this file). No other files are expected; anything else is unexpected and should be reported, not staged.

## Pre-seal checks re-run against the revised DESIGN.md (2026-11-01, all PASS)

- Revised DESIGN.md on host: 36423 bytes, SHA256 `b4f911187a17593f06e173a014cc923f3ee1708ddb393eaa2338661189eb9c06`; no unresolved DIRECTOR/TODO/[SEAL] markers; no residual reference to the cloud builder shell as the execution environment.
- V1 copy `data/source_consistency/V1_DESIGN.md` re-hashed: `8e5010524e7b34c0c89bfe758067ef92db6ee52db682f23eae87ef09bd657e32` (matches required).
- `data/MANIFEST.json`: all 349 entries re-verified, zero missing, zero mismatched.
- Working prompts re-verified: each equals its preserved original plus the shared appended block, byte-exact; canonical S1–S9 byte-identical across both originals and both working copies.

## After committing

Report to the builder: the actual commit hash and the committer UTC timestamp (seal time). The builder records them in `study/SEAL_RECORD.md` in a later commit. Do not amend or rewrite this commit under any circumstances.

The builder stops at this boundary and begins no Study 0 result computation until the coordinator reports this DESIGN.md-only commit is complete.
