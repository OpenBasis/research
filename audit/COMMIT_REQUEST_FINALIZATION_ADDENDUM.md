# Mechanical host commit request — post-PASS finalization addendum

The auditor has verified the director-approved finalization commit `2dc6c3889166e38990fc4deeb2b18424451905f8` and written `audit/FINALIZATION_ADDENDUM.md`. This is **not a new audit round** and does not alter the Round 2 PASS. No mutating Git command has been run by the auditor.

Verify the parent, unchanged bytes, each listed SHA256 and the absence of unexpected files. Stage and commit **only** the six paths below. Do not edit substantive content. This request file itself is excluded from the commit and may remain untracked for a later bookkeeping boundary.

**Expected parent:** `2dc6c3889166e38990fc4deeb2b18424451905f8`.
**Suggested commit message:** `Study 0: retain post-PASS finalization addendum`.

| Exact path to stage | Bytes | SHA256 |
|---|---:|---|
| `audit/FINALIZATION_ADDENDUM.md` | 4776 | `72597f7bd13130830e2790aff9bdfd41fc2414ea7057e4c582637be23cc3dcff` |
| `study/commit_requests/COMMIT_REQUEST_006_AUDIT_PROCESS_FINALIZATION.md` | 5947 | `f1dfffcc22ef58004f00e2da90c0313ed454dddb4289942b66375ee58fe086cf` |
| `study/host_receipts/HOST_RECEIPT_009_AUDIT_PROCESS_FINALIZATION.md` | 2185 | `4652537359df1d79bef065b52544b96f918ccec0c6ca8d5b1d5ee835bfce6f5f` |
| `study/run_logs/RUN_009_fixtures_final.log` | 1777 | `90eadc3bf7aa01aaecd39903004c845fb91977d81274211f42275e61e703d9f6` |
| `study/run_logs/RUN_010_repro_final.log` | 490 | `31a2277cafe004e4ad04438c8e36e5c86514cf0e287d71fe935de560db4d3fce` |
| `study/run_logs/RUN_011_independent_final.log` | 527 | `144b373fabd48f525703aeba5466ec651c7a30a978a0ee8dacf76f8db34f7e1a` |

After the mechanical commit, record the actual commit hash, UTC time and verified file hashes in the host receipt. Leave `audit/findings_round1.md`, `audit/verdict_round1.md`, `audit/findings_round2.md`, `audit/verdict_round2.md`, the original Round 2 submission and PASS audit-record commits, `DESIGN.md`, and all result-bearing artifacts unchanged.
