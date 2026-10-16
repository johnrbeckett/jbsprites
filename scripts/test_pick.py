#!/usr/bin/env python3
"""Checks for the picker. Run after build_index.py. Exits non-zero on any failure.

Safety: energy rules hold for every moment; character filter respected unless the pick is
marked relaxed; avoid respected when another candidate exists; every id is a live asset.
Also prints the character share per moment and the per-call latency.
"""
import collections, importlib.util, json, os, subprocess, sys, time
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("pick", os.path.join(ROOT, "scripts", "pick.py"))
pick = importlib.util.module_from_spec(spec); spec.loader.exec_module(pick)
idx = json.load(open(os.path.join(ROOT, "index", "narnia.json")))
by_id = {a[0]: a for a in idx["assets"]}
MOMENTS = ["start", "hello", "morning-brief", "waiting", "waiting-long", "retrying", "done-small", "done",
           "big-win", "sent", "signing-off", "oops", "blocked", "offline", "timed-out", "not-found", "tangled", "your-turn"]
CHARS = sorted({c for a in idx["assets"] for c in a[1]})
import datetime
today = datetime.date(2026, 10, 16)
fails = []
N = int(os.environ.get("N", "2000"))


def one(req, m):
    pool, relaxed = pick.pick_one(idx, m, req, today, set())
    return (pick.draw(pool), relaxed) if pool else (None, relaxed)


share = {}
for m in MOMENTS:
    cnt = collections.Counter()
    for _ in range(N):
        a, _r = one({}, m)
        if a is None:
            fails.append(f"{m}: empty"); break
        if a[0] not in by_id: fails.append(f"{m}: unknown id {a[0]}")
        rule = pick.ENERGY.get(m)
        if rule and a[5] not in rule and not (m in pick.SEASONAL):
            fails.append(f"{m}: {a[0]} energy {a[5]}")
        cnt[pick.group(a)] += 1
    share[m] = cnt
for m in MOMENTS:
    for c in CHARS:
        for _ in range(50):
            a, relaxed = one({"character": c}, m)
            if a and not relaxed and c not in a[1]:
                fails.append(f"{m}/{c}: got {a[0]} without relaxed"); break
            rule = pick.ENERGY.get(m)
            if a and rule and a[5] not in rule and m not in pick.SEASONAL:
                fails.append(f"{m}/{c}: energy {a[5]}"); break
# avoid: exclude all but one candidate
pool, _ = pick.pick_one(idx, "offline", {}, today, set())
keep = pool[0][0] if len(pool) > 1 else None
if keep:
    for _ in range(50):
        a, _ = one({"avoid": [x[0] for x in pool if x[0] != keep]}, "offline")
        if a[0] != keep: fails.append("avoid ignored")
# relaxed flag never set when the exact pool exists
for m in MOMENTS:
    if m in pick.SEASONAL: continue
    exact = [a for a in idx["assets"] if m in a[2] and (pick.ENERGY.get(m) is None or a[5] in pick.ENERGY[m])]
    _, relaxed = one({}, m)
    if exact and relaxed: fails.append(f"{m}: relaxed with exact pool")
# latency
t = time.time()
for _ in range(20):
    subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "pick.py"),
                    '{"moment":["start","done-small","done","oops","your-turn"],"activity":"research","phrase":true}'],
                   capture_output=True)
ms = (time.time() - t) / 20 * 1000

print("character share (% of draws):")
for m in ("start", "done", "done-small", "oops", "your-turn", "big-win", "signing-off"):
    tot = sum(share[m].values())
    print(f"  {m:12} " + ", ".join(f"{g} {100*n/tot:.0f}" for g, n in share[m].most_common(6)))
print(f"latency per call (5 moments, incl. python start): {ms:.0f} ms")
print(f"index: {os.path.getsize(os.path.join(ROOT, 'index', 'narnia.json'))} bytes, {len(idx['assets'])} assets")
print("FAIL\n  " + "\n  ".join(sorted(set(fails))[:30]) if fails else "ALL CHECKS PASSED")
sys.exit(1 if fails else 0)
