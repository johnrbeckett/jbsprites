#!/usr/bin/env python3
"""jbsprites picker. Takes one JSON argument, prints one JSON line. Never fails loudly.

  python3 pick.py '{"family":"narnia","activity":"research","moment":"start"}'
  -> {"url":"https://...webp","id":"21-research-and-inbox_03","character":"tumnus"}

Fields: family (default narnia), character (optional; narrows to that character),
activity (optional), moment (a string, or a list to get several picks at once),
avoid (sprite ids already shown), phrase (true adds a closing line to end moments),
date (YYYY-MM-DD, default today).

A list of moments returns {"<moment>": {...}, ...}. Nothing suitable returns {}.
"relaxed": true marks a pick that needed a fallback.
"""
import datetime, json, math, os, random, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ALIASES = {"tumnus": "narnia"}
PARENT = {"blocked": "oops", "offline": "oops", "timed-out": "oops", "not-found": "oops", "tangled": "oops",
          "big-win": "done", "sent": "done-small", "signing-off": "done-small", "waiting-long": "waiting",
          "waiting": "start", "retrying": "start", "hello": "start", "morning-brief": "start"}
CALM = {"subdued", "moderate"}
ENERGY = {m: CALM for m in ("oops", "blocked", "offline", "timed-out", "not-found", "tangled",
                            "done-small", "signing-off", "waiting", "waiting-long", "retrying", "your-turn")}
ENERGY["big-win"] = {"celebratory"}
ENERGY["done"] = {"moderate", "celebratory"}
SEASONAL = {"hello", "morning-brief"}
END = {"done-small", "done", "big-win", "sent", "signing-off", "oops", "blocked", "offline",
       "timed-out", "not-found", "tangled", "your-turn"}
rng = random.SystemRandom()


def season_tags(d):
    md = (d.month, d.day)
    if (11, 20) <= md <= (11, 30): return ["thanksgiving", "autumn"]
    if (12, 1) <= md <= (12, 26): return ["christmas", "winter"]
    if md >= (12, 27) or md <= (1, 2): return ["new-year", "winter"]
    return [{12: "winter", 1: "winter", 2: "winter", 3: "spring", 4: "spring", 5: "spring",
             6: "summer", 7: "summer", 8: "summer"}.get(d.month, "autumn")]


def group(a):
    chars = a[1]
    return chars[0] if len(chars) == 1 else ("scene" if chars else "objects")


def draw(pool):
    """Character-balanced, square-root weighting: a character with 4x the sprites is picked ~2x as often."""
    sizes = {}
    for a in pool:
        g = group(a); sizes[g] = sizes.get(g, 0) + 1
    weights = [1 / math.sqrt(sizes[group(a)]) for a in pool]
    return rng.choices(pool, weights=weights)[0]


def pick_one(idx, moment, req, today, used):
    """Returns (pool, relaxed). Fallback order: character+activity+moment, character+moment,
    activity+moment, moment, then the same down the moment's parents. Activity only narrows
    start; energy rules hold at every step."""
    assets = idx["assets"]
    char = req.get("character")
    avoid = set(req.get("avoid") or []) | used

    if moment in SEASONAL and rng.random() < 1 / 3:
        for tag in season_tags(today):
            s = [a for a in assets if tag in a[4] and (char is None or char in a[1])]
            if s:
                return [a for a in s if a[0] not in avoid] or s, False

    chain, m = [moment], moment
    while m in PARENT:
        m = PARENT[m]; chain.append(m)
    for m in chain:
        act = req.get("activity") if m == "start" else None
        energy = ENERGY.get(moment)          # the requested moment's rule, kept through fallbacks
        steps = ([(char, act), (char, None)] if char else []) + [(None, act), (None, None)]
        for ch, ac in dict.fromkeys(steps):
            p = [a for a in assets if m in a[2]
                 and (ch is None or ch in a[1])
                 and (ac is None or ac in a[3])
                 and (energy is None or a[5] in energy)]
            if p:
                relaxed = not (m == moment and ch == char and ac == act)
                return [a for a in p if a[0] not in avoid] or p, relaxed
    return [], False


def main():
    try:
        req = json.loads(sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read())
        fam = ALIASES.get(req.get("family") or "narnia", req.get("family") or "narnia")
        idx = json.load(open(os.path.join(HERE, "..", "index", f"{fam}.json")))
        today = datetime.date.fromisoformat(req["date"]) if req.get("date") else datetime.date.today()
        moments = req.get("moment") or "start"
        many = isinstance(moments, list)
        out, used = {}, set()
        for m in (moments if many else [moments]):
            pool, relaxed = pick_one(idx, m, req, today, used)
            if not pool:
                continue
            a = draw(pool)
            used.add(a[0])
            r = {"url": idx["base"] + a[0] + ".webp", "id": a[0], "character": a[1][0] if a[1] else None}
            if relaxed:
                r["relaxed"] = True
            if req.get("phrase") and m in END:
                ph = [p for p in idx["phrases"].get(m) or idx["phrases"].get(PARENT.get(m, ""), [])
                      if not p.endswith("|fri") or today.weekday() == 4]
                if ph:
                    r["phrase"] = rng.choice(ph).split("|")[0]
            out[m] = r
        print(json.dumps(out if many else out.get(moments, {}), separators=(",", ":")))
    except Exception:
        print("{}")


if __name__ == "__main__":
    main()
