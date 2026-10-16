#!/usr/bin/env python3
"""Cut sprite sheets in <family>/originals/ into single sprites.

Writes <family>/<sheet>_<NN>.webp: transparent, longest side 160 px,
lossy WebP (quality 80, alpha quality 80), about 7 KB each.

How the cut works: pixels with alpha >= 240 (eroded by one pixel) form the
solid core of each figure; cores of 2,500 px or more are sprites. Every other
pixel goes to its nearest core, and is kept only if it is fairly opaque
(alpha >= 128) within 70 px of it, or faint within 6 px. An opaque piece that
touches only one core goes whole to it, and a loose piece with no core of its
own (a paper airplane, a sparkle) goes whole to its nearest core, so no piece
is split between two sprites. When two touching objects share one core and
leave a grid cell empty, the part of that core inside the empty cell is split off. That keeps props and drops stray haze.

With a <sheet>.json index ("columns", "rows") beside the sheet, pieces are
grouped by grid cell, so a prop that floats apart stays with its figure. Row
bands come from the vertical spans of the big figures when they form that
many rows (rows are often uneven), else the sheet is split evenly. With an
index, NN is the grid position, (row - 1) * columns + column, so a missed cell
leaves a gap and a warning instead of renumbering every later sprite. Without an
index, each core is its own sprite, numbered in reading order (fragile: never
re-cut a published sheet that has no index).

Usage: python3 scripts/make_sprites.py <family> [sheet-prefix ...]
       e.g. python3 scripts/make_sprites.py narnia 20 21   (only sheets 20-*, 21-*)
Needs numpy, scipy, Pillow. Existing sprites are overwritten only for the
sheets processed, so pass prefixes when adding sheets to a published family.
"""
import glob
import json
import os
import sys

import numpy as np
from PIL import Image
from scipy import ndimage

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FAMILY = sys.argv[1] if len(sys.argv) > 1 else "narnia"
ONLY = sys.argv[2:]
OUT = os.path.join(ROOT, FAMILY)
SRC = os.path.join(OUT, "originals")
SIZE = 160
MIN_CORE = int(os.environ.get("MIN_CORE", "2500"))


def bands(lab, areas, n):
    """Row cuts from the vertical spans of the big cores, if they form n rows."""
    sl = ndimage.find_objects(lab)
    spans = sorted((sl[i][0].start, sl[i][0].stop) for i in range(len(areas)) if areas[i] >= 10000)
    rows = []
    for s, e in spans:
        if rows and s < rows[-1][1]:
            rows[-1] = (rows[-1][0], max(rows[-1][1], e))
        else:
            rows.append((s, e))
    if len(rows) != n:
        return None
    return [(rows[i][1] + rows[i + 1][0]) / 2 for i in range(n - 1)]


def cut(path):
    im = np.array(Image.open(path).convert("RGBA"))
    a = im[:, :, 3]
    h, w = a.shape
    core = ndimage.binary_erosion(a >= 240, iterations=1)
    lab, n = ndimage.label(core)
    areas = ndimage.sum(core, lab, range(1, n + 1))
    keep = [i + 1 for i in range(n) if areas[i] >= MIN_CORE]
    seeds = np.where(np.isin(lab, keep), lab, 0)
    grid = None
    idx = os.path.splitext(path)[0] + ".json"
    if os.path.exists(idx):
        meta = json.load(open(idx))
        cols, rows = meta["columns"], meta["rows"]
        cuts = bands(lab, areas, rows) or [h * (i + 1) / rows for i in range(rows - 1)]
        edges_y = [0] + [int(c) for c in cuts] + [h]
        edges_x = [int(w * i / cols) for i in range(cols + 1)]

        def cell_of(cy, cx):
            return (sum(cy > c for c in cuts), min(int(cx * cols / w), cols - 1))

        def group(keep):
            cells = {}
            for (cy, cx), k in zip(ndimage.center_of_mass(seeds > 0, seeds, keep), keep):
                cells.setdefault(cell_of(cy, cx), []).append(k)
            return cells

        cells = group(keep)
        # two touching objects can share one core; split off the part in an empty cell
        for r, c in [(r, c) for r in range(rows) for c in range(cols) if (r, c) not in cells]:
            box = seeds[edges_y[r]:edges_y[r + 1], edges_x[c]:edges_x[c + 1]]
            ids, counts = np.unique(box[box > 0], return_counts=True)
            if len(ids) and counts.max() >= MIN_CORE:
                new = seeds.max() + 1
                box[box == ids[counts.argmax()]] = new
                keep.append(new)
        cells = group(keep)
        empty = [(r, c) for r in range(rows) for c in range(cols) if (r, c) not in cells]
        if empty:
            print(f"  warning: no sprite in cells {[r * cols + c + 1 for r, c in empty]} (numbers left as gaps)")
        grid = [(r * cols + c + 1, cells[(r, c)]) for r, c in sorted(cells)]
    dist, (iy, ix) = ndimage.distance_transform_edt(seeds == 0, return_indices=True)
    owner = seeds[iy, ix]
    # each opaque piece (alpha >= 128) that touches one core goes whole to it;
    # a loose piece with no core (a paper airplane) goes whole to its nearest core
    comp, nc = ndimage.label(a >= 128)
    for c, box in enumerate(ndimage.find_objects(comp), 1):
        sel = comp[box] == c
        ids = np.unique(seeds[box][sel])
        ids = ids[ids > 0]
        if len(ids) > 1:
            continue
        if len(ids) == 1:
            k = ids[0]
        else:
            d = np.where(sel, dist[box], np.inf)
            k = owner[box][np.unravel_index(np.argmin(d), d.shape)]
        owner[box][sel] = k
        dist[box][sel] = 0
    if grid:
        groups = grid
    else:
        centres = ndimage.center_of_mass(core, lab, keep)
        groups = list(enumerate(([k] for _, k in sorted(zip(centres, keep),
                                         key=lambda z: (round(z[0][0] / 200), z[0][1]))), 1))
    for nn, g in groups:
        m = np.isin(owner, g) & (((a >= 128) & (dist <= 70)) | ((a > 0) & (dist <= 6)))
        c = im.copy()
        c[:, :, 3] = np.where(m, a, 0)
        c[c[:, :, 3] == 0, :3] = 0
        ys, xs = np.where(m)
        yield nn, Image.fromarray(c[ys.min():ys.max() + 1, xs.min():xs.max() + 1])


def main():
    os.makedirs(OUT, exist_ok=True)
    for path in sorted(glob.glob(os.path.join(SRC, "*.png"))):
        base = os.path.basename(path)[:-4]
        if ONLY and not any(base.startswith(p) for p in ONLY):
            continue
        count = 0
        for k, sprite in cut(path):
            sprite.thumbnail((SIZE, SIZE), Image.LANCZOS)
            sprite.save(os.path.join(OUT, f"{base}_{k:02d}.webp"), "WEBP",
                        quality=80, alpha_quality=80, method=6)
            count = k
        print(f"{base}: {count} sprites")


if __name__ == "__main__":
    main()
