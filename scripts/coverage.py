#!/usr/bin/env python3
"""Write reports/coverage.md: how many live sprites, from which characters, each moment and
start activity can draw on. The "what to make next" list in docs/SHEET-BRIEF.md comes from it.

Usage: python3 scripts/coverage.py [--family narnia]
"""
import json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fam = sys.argv[sys.argv.index("--family") + 1] if "--family" in sys.argv else "narnia"
live = [a for a in json.load(open(os.path.join(ROOT, "catalog", f"{fam}.json")))["assets"] if a["status"] in ("proposed", "reviewed")]
rows = []
def line(label, pool):
    chars = {}
    for a in pool:
        for c in (a["characters"] or ["(object/place)"]): chars[c] = chars.get(c, 0) + 1
    rows.append(f"| {label} | {len(pool)} | " + ", ".join(f"{c} {n}" for c, n in sorted(chars.items(), key=lambda z: -z[1])) + " |")
for m in sorted({m for a in live for m in a["moments"]}): line(m, [a for a in live if m in a["moments"]])
for x in sorted({x for a in live for x in a["activities"]}): line("start: " + x, [a for a in live if x in a["activities"]])
for s in sorted({s for a in live for s in a["seasons"]}): line("season: " + s, [a for a in live if s in a["seasons"]])
out = os.path.join(ROOT, "reports", "coverage.md")
open(out, "w").write(f"# Coverage: {fam} ({len(live)} live sprites)\n\n| moment / activity | sprites | characters |\n|---|---|---|\n" + "\n".join(rows) + "\n")
print(out)
