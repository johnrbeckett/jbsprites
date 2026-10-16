#!/usr/bin/env python3
# RETIRED at v9: the catalog is now the source of truth. This seeded it from the v8 SKILL.md tables
# (which no longer exist in SKILL.md) and is kept only as a record of how the seed was made.
"""One-off: seed catalog/narnia.json from the v8 SKILL.md tables, the sheet
JSON indexes and the webp files on disk, and write reports/parity.md.

Re-runnable. Every proposed tag is marked so review can tell seeded values
from checked ones. After review, the catalog is the source of truth and this
script is retired (it will not overwrite a catalog with reviewed entries
unless --force is passed).

Usage: python3 scripts/seed_catalog.py [--force]
"""
import glob, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(ROOT, "narnia")
OUT = os.path.join(ROOT, "catalog", "narnia.json")
REPORT = os.path.join(ROOT, "reports", "parity.md")

# SKILL.md v8 row label (prefix) -> (moment, activity)
ROWS = {
    "Writing or drafting": ("start", "writing"),
    "Research or reading": ("start", "research"),
    "Email, reconcile, sweep": ("start", "email"),
    "Add (new tracker item)": ("start", "tracker-add"),
    "Waiting on someone": ("waiting", None),
    "Morning brief": ("morning-brief", None),
    "The list": ("start", "tracker-list"),
    "Next": ("start", "tracker-next"),
    "Now": ("start", "tracker-now"),
    "Gaps, stale items": ("start", "tracker-gaps"),
    "Week, quarter, year": ("start", "tracker-review"),
    "Trip": ("start", "travel"),
    "Hand-off": ("start", "handoff"),
    "Hello": ("hello", None),
    "Anything else": ("start", "general"),
    "Calendar, scheduling": ("start", "scheduling"),
    "Invoices, payments": ("start", "money"),
    "Technical": ("start", "technical"),
    "Image or design": ("start", "design"),
    "Waiting on a long job": ("waiting-long", None),
    "Meetings, calls": ("start", "meetings"),
    "Deep focus": ("start", "focus"),
    "On the go": ("start", "mobile"),
    "Retrying": ("retrying", None),
    "Done, small": ("done-small", None),
    "Sent": ("sent", None),
    "Done (real work": ("done", None),
    "Big win": ("big-win", None),
    "Signing off": ("signing-off", None),
    "Oops: general": ("oops", None),
    "Oops: blocked": ("blocked", None),
    "Oops: connection": ("offline", None),
    "Oops: timed out": ("timed-out", None),
    "Oops: nothing found": ("not-found", None),
    "Oops: conflicting": ("tangled", None),
    "Your turn": ("your-turn", None),
}
SEASONS = {"Autumn": "autumn", "Winter": "winter", "Spring": "spring", "Summer": "summer"}
HOLIDAYS = {"Thanksgiving": "thanksgiving", "Christmas": "christmas", "New Year": "new-year"}

# Proposed characters for sheets with descriptions: first match wins per name,
# all matches kept (scenes can hold several).
NAMES = [("tumnus", r"\btumnus\b"), ("lucy", r"\blucy\b"), ("edmund", r"\bedmund\b"),
         ("susan", r"\bsusan\b"), ("peter", r"\bpeter\b"), ("aslan", r"\baslan\b|\blion\b(?! crown| emblem| seal|-shaped| bookends)"),
         ("white-witch", r"white witch|\bwitch\b"), ("mr-beaver", r"mr beaver|mr and mrs beaver|beaver couple"),
         ("mrs-beaver", r"mrs beaver|mr and mrs beaver|beaver couple"), ("father-christmas", r"father christmas"),
         ("centaur", r"centaur"), ("dryad", r"dryad"), ("maugrim", r"maugrim|\bwolf\b"),
         ("fox", r"\bfox\b"), ("robin", r"\brobin\b"), ("owl", r"\bowl\b"), ("dwarf", r"\bdwarf\b"),
         ("unicorn", r"unicorn")]
PEVENSIES = ["lucy", "edmund", "susan", "peter"]
OBJECT_SHEETS = {"11", "28", "29"}       # props and treasures: no figure unless named as present
PLACE_SHEET = "30"
REMOVED = {"25-aslan-and-white-witch_07", "27-narnian-creatures-at-work_01", "27-narnian-creatures-at-work_02",
           "27-narnian-creatures-at-work_03", "27-narnian-creatures-at-work_04", "27-narnian-creatures-at-work_05",
           "31-narnia-workday-scenes_11"}   # cut by John from the v6 contact sheet; never published


# Decisions from the 2026-10-16 contact-sheet review of sheets 24-31.
# Every wolf is Maugrim; beaver paws stay character-less; cut cells stay cut.
OVERRIDES = {"31-narnia-workday-scenes_23": {"view": "hands"}}
REVIEWED_SHEETS = [f"{n}" for n in range(24, 32)]


def parse_tables(md):
    tables = {}
    for line in md.splitlines():
        if not line.startswith("| ") or line.startswith("|---"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) != 2:
            continue
        label, sprites = cells
        ids = re.findall(r"\b\d\d-[a-z-]+_\d\d\b", sprites)
        if ids:
            tables[label] = ids
    return tables


def row_key(label, table):
    for k in table:
        if label.startswith(k):
            return k
    return None


def characters_for(sheet, desc):
    d = (desc or "").lower()
    if "four siblings" in d or "four pevensies" in d:
        return list(PEVENSIES)
    found = [n for n, rx in NAMES if re.search(rx, d)]
    return found


def view_for(sheet, meta_type, desc, chars):
    d = (desc or "").lower()
    if meta_type:
        return {"close-up": "portrait", "full-body": "full-body", "object": "object"}.get(meta_type, meta_type)
    if sheet == PLACE_SHEET:
        return "environment"
    if "closeup" in d or "close-up" in d or "paws" in d and "hands" not in d and "holding mug" in d:
        return "hands" if ("hands" in d or "paw" in d) else "portrait"
    if "hands" in d:
        return "hands"
    if re.search(r"\bhead\b", d) and "headset" not in d.replace("head and", ""):
        return "portrait"
    if any(w in d for w in ("portrait", "head-and-shoulders", "head and shoulders", "waist-up", "complete head")):
        return "portrait"
    if len(chars) > 1:
        return "scene"
    if not desc and sheet in OBJECT_SHEETS:
        return "object"
    if sheet in OBJECT_SHEETS and not chars:
        return "object"
    if desc and not chars:
        return "object"
    return "full-body" if desc else None


def main():
    if os.path.exists(OUT) and "--force" not in sys.argv:
        cur = json.load(open(OUT))
        if any(a.get("status") == "reviewed" for a in cur["assets"]):
            sys.exit("catalog has reviewed entries; pass --force to reseed")
    md = open(os.path.join(ROOT, "SKILL.md")).read()
    tables = parse_tables(md)

    tags = {}  # id -> {moments:set, activities:set, seasons:set, rows:[labels]}
    def tag(i):
        return tags.setdefault(i, {"moments": set(), "activities": set(), "seasons": set(), "rows": []})
    unknown_rows = []
    for label, ids in tables.items():
        if label.split(" (")[0] in SEASONS:
            for i in ids:
                tag(i)["seasons"].add(SEASONS[label.split(" (")[0]]); tag(i)["rows"].append(label)
            continue
        h = next((v for k, v in HOLIDAYS.items() if label.startswith(k)), None)
        if h:
            for i in ids:
                tag(i)["seasons"].add(h); tag(i)["rows"].append(label)
            continue
        k = row_key(label, ROWS)
        if not k:
            unknown_rows.append(label); continue
        m, a = ROWS[k]
        for i in ids:
            t = tag(i); t["moments"].add(m); t["rows"].append(label)
            if a:
                t["activities"].add(a)

    metas = {}
    for j in glob.glob(os.path.join(SRC_DIR, "originals", "*.json")):
        m = json.load(open(j)); base = os.path.basename(j)[:-5]
        cols = m["columns"]
        for a in m.get("assets", []):
            nn = (a["row"] - 1) * cols + a["column"]
            metas[f"{base}_{nn:02d}"] = {"row": a["row"], "col": a["column"],
                                        "desc": a.get("description") or a.get("name"),
                                        "type": a.get("type"), "grid": f"{cols}x{m['rows']}"}

    assets = []
    on_disk = sorted(os.path.basename(p)[:-5] for p in glob.glob(os.path.join(SRC_DIR, "*.webp")))
    every = sorted(set(on_disk) | REMOVED)
    for i in every:
        sheet = i[:2]
        meta = metas.get(i, {})
        t = tags.get(i, {"moments": set(), "activities": set(), "seasons": set(), "rows": []})
        desc = meta.get("desc")
        if sheet >= "24":
            chars = characters_for(sheet, desc)
        else:
            # sheets 06-23 are Tumnus sheets; only their props carry no figure
            chars = [] if (sheet in OBJECT_SHEETS or meta.get("type") == "object") else ["tumnus"]
        if sheet in OBJECT_SHEETS | {PLACE_SHEET} and desc and not re.search(r"\btumnus umbrella\b", desc.lower()):
            # objects that only evoke a character carry it as a motif, not a figure
            pass
        motifs = []
        if sheet in OBJECT_SHEETS | {PLACE_SHEET}:
            motifs, chars = chars, []
        view = view_for(sheet, meta.get("type"), desc, chars)
        ms = t["moments"]
        calm = {"done-small", "signing-off", "oops", "blocked", "offline", "timed-out", "not-found", "tangled", "waiting", "waiting-long"}
        if (ms & {"big-win"} or (ms & {"done"} and sheet == "08")) and not ms & calm:
            energy = "celebratory"
        elif ms & {"done-small", "signing-off", "oops", "blocked", "offline", "timed-out", "not-found", "tangled", "waiting", "waiting-long"} and not ms & {"done", "big-win"}:
            energy = "subdued"
        else:
            energy = "moderate"
        if i in REMOVED:
            status = "removed"
        elif not t["rows"]:
            status = "unmapped"
        else:
            status = "proposed"
        if status == "proposed" and sheet in REVIEWED_SHEETS:
            status = "reviewed"
        assets.append({
            "id": i, "file": f"{i}.webp", "sheet": i.rsplit("_", 1)[0],
            "cell": {"row": meta.get("row"), "col": meta.get("col")} if meta else None,
            "characters": chars, "motifs": motifs, "view": view,
            "moments": sorted(ms), "activities": sorted(t["activities"]),
            "seasons": sorted(t["seasons"]), "energy": energy,
            "description": desc, "status": status, "v8_rows": t["rows"],
        })

    for a in assets:
        a.update(OVERRIDES.get(a["id"], {}))
    cat = {"family": "narnia", "legacy_family": "tumnus", "schema": 1,
           "note": "Seeded from jbsprites v8. status: proposed = seeded, needs review; reviewed = checked; unmapped = on disk, in no v8 row; removed = cut, never published.",
           "assets": assets}
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(cat, f, indent=1)
        f.write("\n")

    # ---- parity: rebuild every v8 row from the catalog and diff
    by_id = {a["id"]: a for a in assets}
    lines = ["# Parity report: SKILL.md v8 tables vs catalog/narnia.json", ""]
    bad = 0
    lines += ["| v8 row | sprites in v8 | rebuilt from catalog | missing | extra |", "|---|---|---|---|---|"]
    for label, ids in tables.items():
        base = label.split(" (")[0]
        if base in SEASONS:
            got = {a["id"] for a in assets if SEASONS[base] in a["seasons"]}
        elif any(label.startswith(k) for k in HOLIDAYS):
            h = next(v for k, v in HOLIDAYS.items() if label.startswith(k))
            got = {a["id"] for a in assets if h in a["seasons"]}
        else:
            k = row_key(label, ROWS)
            if not k:
                continue
            m, act = ROWS[k]
            got = {a["id"] for a in assets if m in a["moments"] and (act is None or act in a["activities"])}
            if act is None:
                # rows without an activity: only ids that came from this row (others share the moment)
                got = {a["id"] for a in assets if label in a["v8_rows"]}
        want = set(ids)
        miss, extra = sorted(want - got), sorted(got - want)
        bad += len(miss)
        short = label if len(label) < 45 else label[:42] + "..."
        lines.append(f"| {short} | {len(want)} | {len(got)} | {', '.join(miss) or '0'} | {len(extra) if extra else 0} |")
    not_on_disk = sorted(i for ids in tables.values() for i in ids if i not in set(on_disk))
    lines += ["", f"**Sprites named in v8 but missing on disk:** {', '.join(not_on_disk) or 'none'}",
              f"**Unparsed v8 rows:** {', '.join(unknown_rows) or 'none'}",
              f"**Dropped from v8 rows:** {bad}", ""]
    st = {}
    for a in assets:
        st[a["status"]] = st.get(a["status"], 0) + 1
    lines += ["## Catalog totals", "", " / ".join(f"{k}: {v}" for k, v in sorted(st.items())), ""]
    um = [a["id"] for a in assets if a["status"] == "unmapped"]
    lines += ["## Unmapped (on disk, in no v8 row; not served until tagged)", "", ", ".join(um), ""]
    # coverage: candidates per moment and per start activity, by character
    lines += ["## Coverage (proposed + reviewed only)", "", "| moment / activity | sprites | characters |", "|---|---|---|"]
    live = [a for a in assets if a["status"] in ("proposed", "reviewed")]
    keys = sorted({("m", m) for a in live for m in a["moments"]} | {("a", x) for a in live for x in a["activities"]})
    for kind, key in keys:
        pool = [a for a in live if key in (a["moments"] if kind == "m" else a["activities"])]
        chars = {}
        for a in pool:
            for c in (a["characters"] or ["(object/place)"]):
                chars[c] = chars.get(c, 0) + 1
        top = ", ".join(f"{c} {n}" for c, n in sorted(chars.items(), key=lambda z: -z[1]))
        lines.append(f"| {'start: ' if kind == 'a' else ''}{key} | {len(pool)} | {top} |")
    open(REPORT, "w").write("\n".join(lines) + "\n")
    print(f"assets {len(assets)}; statuses {st}; dropped {bad}; missing-on-disk {len(not_on_disk)}; unparsed rows {unknown_rows}")


if __name__ == "__main__":
    main()
