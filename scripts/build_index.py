#!/usr/bin/env python3
"""Build the compact runtime index the picker reads: index/<family>.json.

Only live assets (status proposed or reviewed) go in. Each asset is one array:
[id, characters, moments, activities, seasons, energy, view].

Usage: python3 scripts/build_index.py [--family narnia] [--tag v9] [--dir narnia]
  --tag  the jsDelivr tag the URLs pin to (the release being built)
  --dir  the folder the webps live in at that tag (tumnus up to v8, narnia from v9)
"""
import argparse, json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ap = argparse.ArgumentParser()
ap.add_argument("--family", default="narnia")
ap.add_argument("--tag", default="v9")
ap.add_argument("--dir", default=None)
a = ap.parse_args()
cat = json.load(open(os.path.join(ROOT, "catalog", f"{a.family}.json")))
phrases = json.load(open(os.path.join(ROOT, "catalog", "phrases.json")))
live = [x for x in cat["assets"] if x["status"] in ("proposed", "reviewed")]
idx = {
    "family": a.family,
    "base": f"https://cdn.jsdelivr.net/gh/johnrbeckett/jbsprites@{a.tag}/{a.dir or a.family}/",
    "assets": [[x["id"], x["characters"], x["moments"], x["activities"], x["seasons"], x["energy"], x["view"]] for x in live],
    "phrases": phrases,
}
os.makedirs(os.path.join(ROOT, "index"), exist_ok=True)
out = os.path.join(ROOT, "index", f"{a.family}.json")
with open(out, "w") as f:
    json.dump(idx, f, separators=(",", ":"))
print(f"{out}: {len(live)} assets, {os.path.getsize(out)} bytes, base {idx['base']}")
