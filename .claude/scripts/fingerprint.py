#!/usr/bin/env python3
"""Fingerprint files and check them against vault/sources/manifest.md so nothing is processed twice.

Usage: python3 .claude/scripts/fingerprint.py [--manifest vault/sources/manifest.md] FILE [FILE ...]
Prints JSON: [{"file":..., "fingerprint":..., "already_processed": true/false}]
"""
import sys, hashlib, json, argparse, os
ap = argparse.ArgumentParser(); ap.add_argument("files", nargs="+")
ap.add_argument("--manifest", default="vault/sources/manifest.md")
a = ap.parse_args()
seen = open(a.manifest).read() if os.path.exists(a.manifest) else ""
out = []
for f in a.files:
    if os.path.isdir(f): continue
    h = hashlib.sha256(open(f, "rb").read()).hexdigest()[:12]
    out.append({"file": f, "fingerprint": h, "already_processed": h in seen})
print(json.dumps(out, indent=2))
