#!/usr/bin/env python3
"""Add a newly cut sheet to the catalog as status "proposed".

Reads ../jbsprites-art/<family>/originals/<sheet>.json (the JSON that comes back with a sheet, see
docs/SHEET-BRIEF.md), checks every word against scripts/vocab.py, and adds one catalog
entry per cell that has a webp. Existing ids are left alone. Review with review_sheet.py,
then set status to "reviewed" (or leave "proposed"; both are served).

Usage: python3 scripts/add_sheet.py <NN> [--family narnia]
"""
import argparse, glob, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vocab
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ART = os.environ.get("JBSPRITES_ART", os.path.join(os.path.dirname(ROOT), "jbsprites-art"))
ap = argparse.ArgumentParser(); ap.add_argument("nn"); ap.add_argument("--family", default="narnia")
a = ap.parse_args()
src = glob.glob(os.path.join(ART, a.family, "originals", f"{a.nn}-*.json"))
if len(src) != 1:
    sys.exit(f"need exactly one {a.nn}-*.json in {ART}/{a.family}/originals, found {len(src)}")
meta = json.load(open(src[0])); sheet = os.path.basename(src[0])[:-5]
catp = os.path.join(ROOT, "catalog", f"{a.family}.json"); cat = json.load(open(catp))
have = {x["id"] for x in cat["assets"]}
problems, added = [], 0
for cell in meta["assets"]:
    nn = (cell["row"] - 1) * meta["columns"] + cell["column"]
    i = f"{sheet}_{nn:02d}"
    for field, allowed in (("characters", vocab.CHARACTERS), ("moments", vocab.MOMENTS),
                           ("activities", vocab.ACTIVITIES), ("seasons", vocab.SEASONS)):
        for w in cell.get(field, []):
            if w not in allowed: problems.append(f"{i}: {field} '{w}' not in vocab")
    if cell.get("view") not in vocab.VIEWS: problems.append(f"{i}: view '{cell.get('view')}'")
    if cell.get("energy") not in vocab.ENERGIES: problems.append(f"{i}: energy '{cell.get('energy')}'")
    if i in have:
        continue
    if not os.path.exists(os.path.join(ROOT, a.family, f"{i}.webp")):
        problems.append(f"{i}: no webp (cell empty or not cut yet)"); continue
    cat["assets"].append({"id": i, "file": f"{i}.webp", "sheet": sheet,
        "cell": {"row": cell["row"], "col": cell["column"]},
        "characters": cell.get("characters", []), "motifs": cell.get("motifs", []), "view": cell.get("view"),
        "moments": cell.get("moments", []), "activities": cell.get("activities", []), "seasons": cell.get("seasons", []),
        "energy": cell.get("energy", "moderate"), "description": cell.get("description"), "status": "proposed"})
    added += 1
cat["assets"].sort(key=lambda x: x["id"])
json.dump(cat, open(catp, "w"), indent=1); open(catp, "a").write("\n")
print(f"{sheet}: added {added}")
for p in problems: print("  check:", p)
