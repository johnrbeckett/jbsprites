#!/usr/bin/env python3
"""Maintainer-side contact sheet: review/<family>-review.html shows each sprite
with its catalog tags so they can be checked by eye. Never packaged.

Usage: python3 scripts/review_sheet.py [first-sheet last-sheet]   (default 24 31)
"""
import html, json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
lo, hi = (sys.argv[1], sys.argv[2]) if len(sys.argv) > 2 else ("24", "31")
cat = json.load(open(os.path.join(ROOT, "catalog", "narnia.json")))
imgdir = "../tumnus" if os.path.isdir(os.path.join(ROOT, "tumnus")) else "../narnia"
FLAG = {}
rows, sheet = [], None
for a in cat["assets"]:
    if not (lo <= a["id"][:2] <= hi):
        continue
    if a["sheet"] != sheet:
        sheet = a["sheet"]; rows.append(f"<h2>{html.escape(sheet)}</h2>")
    notes = []
    if a["status"] == "removed": notes.append("cut, never published")
    if a["status"] == "proposed" and not a["characters"] and a["view"] in ("portrait", "full-body", "scene"): notes.append("figure with no character")
    for c in a["characters"]:
        if c in FLAG and "maugrim" not in (a["description"] or "").lower(): notes.append(FLAG[c])
    img = "" if a["status"] == "removed" else f'<img src="{imgdir}/{a["file"]}" alt="">'
    cls = "card flag" if notes else "card"
    rows.append(f'''<div class="{cls}">{img}<b>{a["id"][-2:]}</b> {html.escape(a["description"] or "")}
<div><span>who</span> {", ".join(a["characters"]) or "none"}{(" &middot; motif " + ", ".join(a["motifs"])) if a["motifs"] else ""}</div>
<div><span>view</span> {a["view"] or "?"} &middot; <span>energy</span> {a["energy"]}</div>
<div><span>moments</span> {", ".join(a["moments"] + ["start:" + x for x in a["activities"]]) or "none"}</div>
{"<div class=n>" + "; ".join(notes) + "</div>" if notes else ""}</div>''')
css = """body{font:13px/1.4 -apple-system,system-ui,sans-serif;margin:16px;background:#faf8f4;color:#222}
h1{font-size:20px}h2{font-size:16px;margin:24px 0 8px;clear:both}
.grid{display:flex;flex-wrap:wrap;gap:8px}.card{width:200px;background:#fff;border:1px solid #ddd;border-radius:8px;padding:8px}
.card img{display:block;height:110px;margin:0 auto 6px;image-rendering:auto}.card span{color:#888}
.flag{border-color:#d08a00;background:#fff8e8}.n{color:#a05a00;margin-top:4px}
@media (prefers-color-scheme:dark){body{background:#1b1a18;color:#ddd}.card{background:#262522;border-color:#444}.flag{background:#33290f}}"""
out = os.path.join(ROOT, "review", "narnia-review.html")
os.makedirs(os.path.dirname(out), exist_ok=True)
body = "".join(rows).replace("<h2>", '</div><h2>').replace("</h2>", '</h2><div class="grid">')
open(out, "w").write(f"<!doctype html><meta charset=utf-8><title>narnia review {lo}-{hi}</title><style>{css}</style>"
                     f"<h1>Narnia catalog review, sheets {lo} to {hi}</h1><p>Amber cards need a decision. Check who, view and energy; say what to change by number (e.g. 27_12).</p>"
                     f"<div>{body}</div>")
print(out)
