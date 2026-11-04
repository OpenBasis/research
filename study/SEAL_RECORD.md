# Study 0 — Seal Record

- Sealed design: `DESIGN.md`, 36,423 bytes, SHA256 `b4f911187a17593f06e173a014cc923f3ee1708ddb393eaa2338661189eb9c06`
- Seal commit (first/root commit of this repository; `DESIGN.md` alone, 228 insertions): `9d3ed18144d4cebc2b3c511ad596f3496e833be2`
- Committer timestamp: `2026-11-01T12:47:51-08:00` — **seal time UTC `2026-11-01T20:47:51Z`**
- Tree: `44679fc40065047db5a02b84ea48be8026b495c3`
- Host receipt (mechanical coordinator): `study/host_receipts/HOST_RECEIPT_001_DESIGN_SEAL.md`, SHA256 `fa351fc02737a14193bd9d8ff5209fdd25deeb42609975eb444e1ead9de01170`
- Host pre-commit verification: staged path set exactly `DESIGN.md`; staged-blob and working-file SHA256 both equal to the sealed hash; zero prior commits.
- Builder read-only verification, 2026-11-01, by raw `.git` file reads (no Git commands, per Amendment A4): `.git/HEAD` → `refs/heads/master`; `refs/heads/master` contains `9d3ed18144d4cebc2b3c511ad596f3496e833be2`; the commit and tree objects are present as loose objects; no `.git/*.lock` or `tmp_obj_*` files; working-tree `DESIGN.md` re-hashes to the sealed value.

## Withdrawn pre-commit revision (disclosure)

A DESIGN.md revision at SHA256 `b07ad201388afd938bdd8933a0d881763c0491a39814ff1e3c99a51466aeed04` (35,792 bytes) was withdrawn on the coordinator's stop **before any commit existed**, because its §13 pinned the cloud builder shell instead of the director-approved host environment (decision D4). The sealed revision above replaced it; the only differences are the §13 environment pin and the commit request. No commit was amended or rewritten; the repository's first commit is the seal commit above.

## Effect

Study 0 result computation is authorized from the seal time onward. Per sealed DESIGN §13 and Amendment A4, every result-producing or reproduction command executes on the pinned host environment (macOS arm64, CPython 3.13.15 at `/opt/homebrew/bin/python3.13`), run by the mechanical host coordinator; the builder authors code and inspects returned logs and hashes.
