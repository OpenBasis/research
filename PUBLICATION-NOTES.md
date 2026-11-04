# Publication notes — Study 0

This repository is the publication copy of Study 0. Four groups of working
files are withheld; every withheld file's SHA256 is published here or in the
committed records, so any copy can be verified if ever released. Nothing else
is withheld, and no published file differs from its committed bytes except the
two verdict files below, which are labeled redacted copies.

## The seal and this repository's history

The study design was sealed as the first commit of the study's internal
repository before any result was computed (`study/SEAL_RECORD.md`: design
SHA256 `b4f911187a17593f06e173a014cc923f3ee1708ddb393eaa2338661189eb9c06`,
seal commit `9d3ed18144d4cebc2b3c511ad596f3496e833be2`, 2026-11-01T20:47:51Z).
This published repository is a fresh-history publication copy: its own git
history begins at publication, and the sealed chain's commit and file hashes
are published throughout (SEAL_RECORD, commit requests, audit records). No
claim is made that readers can verify the internal chain itself; the records
state what it pins.

## Redacted copies

`audit/verdict_round1.md` and `audit/verdict_round2.md` are published as
labeled redacted copies: local filesystem paths that identify the host machine
are replaced with `[REDACTED:…]` tokens (2 replacements per file; counts and
the originals' SHA256 values are stated in each file's header, and those
hashes match the pins in `audit/FINALIZATION_ADDENDUM.md`). The redaction is
reproducible with `tools/redact_verdicts.py`. No finding, command, hash or
number was changed. The originals are retained unmodified.

## Withheld files and their hashes

**process mandates (internal briefs):**

- `study/prompts/original/STUDY_0_BUILDER_PROMPT.txt` — SHA256 `ffdde616794b48665ae3b0cfd938e9eb75228956bbe424bc59eef9563ff5642c`
- `study/prompts/original/STUDY_0_AUDITOR_PROMPT.txt` — SHA256 `fea411aef5c3cd321a0b3a4cf84cd234868e9c59938ea5e0799e4196980283ff`
- `study/prompts/working/STUDY_0_BUILDER_PROMPT.txt` — SHA256 `58f386167c0fd24fcfa9a1bf202fb4627d9265800cfcfc3bdad4d510798fd86d`
- `study/prompts/working/STUDY_0_AUDITOR_PROMPT.txt` — SHA256 `1238ade3736034f720ddc95d072a34fe9f1fbf77e1892547204928d496aa093b`
- `study/prompts/working/PROMPT_COMPARISON.md` — SHA256 `8bf4dd7554b8a916445e14fc177361ac5f7ecc45f227818cbc851f7d927d9a0a`
- `study/prompts/amendments/AMENDMENT_A1_A2.txt` — SHA256 `9c755cd5826e03e28845d4d6328bef9136460cf1c5cffb3878bb2d3599364cd6`

**host receipts (machine-identifying bookkeeping):**

- `study/host_receipts/HOST_RECEIPT_001_DESIGN_SEAL.md` — SHA256 `fa351fc02737a14193bd9d8ff5209fdd25deeb42609975eb444e1ead9de01170`
- `study/host_receipts/HOST_RECEIPT_002_INPUTS_SPEC.md` — SHA256 `bec3e55b94ca858ee45e7abf4466b5e66bf3a97b332945d00700f0b75c718f49`
- `study/host_receipts/HOST_RECEIPT_003_EXECUTION.md` — SHA256 `07b5f7f77ee9ee4226962b1634281336311ba97e955a580b52b4085652b7e6d8`
- `study/host_receipts/HOST_RECEIPT_004_RESULTS_FIGURES.md` — SHA256 `dd08c60c6ead0ca5275488942b995f616c10b364305f6e57fc41995829c0c4cf`
- `study/host_receipts/HOST_RECEIPT_005_SUBMISSION.md` — SHA256 `d5d38c5e4041075182b4c52c06ab29e31f80d5b3c485b0640e43846c7705c9af`
- `study/host_receipts/HOST_RECEIPT_006_AUDIT_ROUND1.md` — SHA256 `539bc8682aa9fe133529af673e0603103ac6043851abb487bcd5b5a85260b415`
- `study/host_receipts/HOST_RECEIPT_007_ROUND2_SUBMISSION.md` — SHA256 `6160b777aa16360daef031969ffc463af38486928841a58a816f4708e5890e9c`
- `study/host_receipts/HOST_RECEIPT_008_AUDIT_ROUND2.md` — SHA256 `8886f9d90a7511c934646360fcc7523b057933832f7c9b4b8f30f2a6d7775050`
- `study/host_receipts/HOST_RECEIPT_009_AUDIT_PROCESS_FINALIZATION.md` — SHA256 `4652537359df1d79bef065b52544b96f918ccec0c6ca8d5b1d5ee835bfce6f5f`
- `study/host_receipts/HOST_RECEIPT_010_FINALIZATION_ADDENDUM.md` — SHA256 `b72c056df5aacfb494eed9c9614d19c65d423a570d1864e01ad871e4215f7744`

**auditor verdict originals (published as labeled redacted copies):**

- `audit/verdict_round1.md` — SHA256 `a84b0cf9a17d123393faf4640fa7356c99c71994e2464745ada82e06125a881e`
- `audit/verdict_round2.md` — SHA256 `7bee4b7b7988c5f140be5f96678d4bde4b364b3776bf84ecc325f0d641ce5fef`

**prior-work consistency material (internal):**

- `data/source_consistency/V1_DESIGN.md` — SHA256 `8e5010524e7b34c0c89bfe758067ef92db6ee52db682f23eae87ef09bd657e32`
- `study/V1_CONSISTENCY_T12.md` — SHA256 `f603a8073a80b386ab211217623f5d2cb010c0cf916159e042cb3c31d9a6cc81`

**Raw data captures (349 files):** withheld pending legal review of
third-party redistribution. `data/MANIFEST.json` publishes every file's
source, retrieval record and SHA256; `DATA.md` documents how to re-fetch and
verify. `data/COVERAGE.json` publishes the gap and duplicate censuses.

## Why each group is withheld

- **Process mandates and the prompt-comparison record:** internal staffing and
  process briefs, not study artifacts. Their hashes are pinned in the sealed
  `DESIGN.md` §2 table.
- **Host receipts:** mechanical bookkeeping that identifies the host machine.
  Their hashes are pinned in `study/SEAL_RECORD.md` and the commit requests;
  `study/SEAL_RECORD.md` and the audit records summarize their content.
- **Verdict originals:** identity-bearing paths only; published as redacted
  copies above.
- **Prior-work consistency material:** the sealed design discloses that prior
  internal research exists and pins the consistency source by hash
  (`DESIGN.md` §1); the material itself is internal. Study 0's empirical
  claims never rest on it, by sealed rule.

## What hash verification reports on this tree

Hash lists committed inside the study (`study/FINAL_ARTIFACT_HASHES.sha256`,
the commit requests) include withheld paths; checking them against this tree
reports those paths as missing and the two verdict files as changed — exactly
the set documented above. Every other listed file verifies byte-for-byte.
