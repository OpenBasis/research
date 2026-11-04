#!/usr/bin/env python3
"""Study 0 - freeze data/MANIFEST.json: SHA256 + bytes for every file under
data/ (excluding MANIFEST.json itself), cross-checked against retrieval logs."""
import hashlib, json, os

def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for ch in iter(lambda: f.read(1 << 20), b""): h.update(ch)
    return h.hexdigest()

entries = []
for root, dirs, files in os.walk("data"):
    dirs.sort()
    for fn in sorted(files):
        p = os.path.join(root, fn)
        if p == "data/MANIFEST.json" or fn == ".DS_Store": continue
        entries.append({"file": p, "bytes": os.path.getsize(p), "sha256": sha(p)})

# cross-check against logged hashes
logged = {}
import glob
for lp in glob.glob("data/raw/*/RETRIEVAL_LOG.tsv"):
    base = os.path.dirname(lp)
    for line in open(lp):
        t, h, fn, u = line.rstrip("\n").split("\t")
        logged[os.path.join(base, fn)] = h
for lp in glob.glob("data/raw/*/*_pages.ndjson"):
    for line in open(lp):
        e = json.loads(line)
        logged[e["file"]] = e["sha256"]
mism = [e["file"] for e in entries if e["file"] in logged and logged[e["file"]] != e["sha256"]]
roots = {}
for e in entries:
    key = "/".join(e["file"].split("/")[:3]) if e["file"].startswith("data/raw") else e["file"]
    roots.setdefault(key, []).append(e["sha256"])
root_hashes = {k: hashlib.sha256("\n".join(sorted(v)).encode()).hexdigest() for k, v in sorted(roots.items())}
man = {"built_utc": __import__("time").strftime("%Y-%m-%dT%H:%M:%SZ", __import__("time").gmtime()),
       "n_files": len(entries), "logged_hash_mismatches": mism,
       "source_root_hashes": root_hashes, "files": entries}
with open("data/MANIFEST.json", "w") as f:
    json.dump(man, f, indent=1, sort_keys=False)
print("files:", len(entries), "mismatches:", mism)
print("MANIFEST.json sha256:", sha("data/MANIFEST.json"))
for k, v in root_hashes.items():
    if not k.startswith("data/raw") or True: pass
print(json.dumps(root_hashes, indent=1))
