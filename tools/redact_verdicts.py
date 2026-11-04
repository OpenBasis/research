#!/usr/bin/env python3
"""Reproduce the published redacted verdict copies from the withheld originals.

Usage: python3 tools/redact_verdicts.py <original.md> > redacted_body.md

The published copies consist of a fixed header (stating the replacement count
and the original's SHA256) followed by the original text with local filesystem
paths replaced. The replacement patterns are structural, so this script does
not itself contain the redacted strings:

  /Users/<account>/Desktop/study 0                  -> [REDACTED:study-repo-root]
  /Users/<account>/Desktop/delta neutral research   -> [REDACTED:external-prior-work-path]

Given the withheld original (available to a verifying party against its
published SHA256), this script regenerates the redacted body byte-for-byte;
prepending the published header yields the published file.
"""
import re, sys

PATTERNS = [
    (re.compile(r"/Users/[A-Za-z0-9._-]+/Desktop/study 0"), "[REDACTED:study-repo-root]"),
    (re.compile(r"/Users/[A-Za-z0-9._-]+/Desktop/delta neutral research"), "[REDACTED:external-prior-work-path]"),
]

def redact(text: str):
    total = 0
    for pat, repl in PATTERNS:
        text, n = pat.subn(repl, text)
        total += n
    return text, total

if __name__ == "__main__":
    body = open(sys.argv[1], encoding="utf-8").read()
    out, n = redact(body)
    sys.stderr.write(f"replacements: {n}\n")
    sys.stdout.write(out)
