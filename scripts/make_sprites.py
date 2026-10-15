#!/usr/bin/env python3
"""Cut the Tumnus sprite sheets in art/originals/ into single sprites.

Writes art/sprites/<sheet>_<NN>.webp: transparent, longest side 160 px,
lossy WebP (quality 80, alpha quality 80), about 7 KB each.

How the cut works: pixels with alpha >= 240 (eroded by one pixel) form the
solid core of each figure; cores of 2,500 px or more are sprites. Every other
pixel goes to its nearest core, and is kept only if it is fairly opaque
(alpha >= 128) within 70 px of it, or faint within 6 px. That keeps props
(question marks, umbrellas) and drops stray haze. Sprites are numbered in
reading order, row by row.

Usage: python3 art/make_sprites.py   (needs numpy, scipy, Pillow)
"""
import glob
import json
import os

import numpy as np
from PIL import Image
from scipy import ndimage

import sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FAMILY = sys.argv[1] if len(sys.argv) > 1 else "tumnus"
OUT = os.path.join(ROOT, FAMILY)
SRC = os.path.join(OUT, "originals")
SIZE = 160


def cut(path):
    im = np.array(Image.open(path).convert("RGBA"))
    a = im[:, :, 3]
    core = ndimage.binary_erosion(a >= 240, iterations=1)
    lab, n = ndimage.label(core)
    areas = ndimage.sum(core, lab, range(1, n + 1))
    keep = [i + 1 for i in range(n) if areas[i] >= 2500]
    seeds = np.where(np.isin(lab, keep), lab, 0)
    dist, (iy, ix) = ndimage.distance_transform_edt(seeds == 0, return_indices=True)
    owner = seeds[iy, ix]
    centres = ndimage.center_of_mass(core, lab, keep)
    grid = None
    idx = os.path.splitext(path)[0] + ".json"
    if os.path.exists(idx):
        meta = json.load(open(idx))
        grid = (meta["columns"], meta["rows"])
    if grid:
        cols, rows = grid
        h, w = a.shape
        cells = {}
        for (cy, cx), k in zip(centres, keep):
            cell = (min(int(cy * rows / h), rows - 1), min(int(cx * cols / w), cols - 1))
            cells.setdefault(cell, []).append(k)
        groups = [cells[c] for c in sorted(cells)]
    else:
        groups = [[k] for _, k in sorted(zip(centres, keep),
                                         key=lambda z: (round(z[0][0] / 200), z[0][1]))]
    for g in groups:
        m = np.isin(owner, g) & (((a >= 128) & (dist <= 70)) | ((a > 0) & (dist <= 6)))
        c = im.copy()
        c[:, :, 3] = np.where(m, a, 0)
        c[c[:, :, 3] == 0, :3] = 0
        ys, xs = np.where(m)
        yield Image.fromarray(c[ys.min():ys.max() + 1, xs.min():xs.max() + 1])


def main():
    os.makedirs(OUT, exist_ok=True)
    for path in sorted(glob.glob(os.path.join(SRC, "*.png"))):
        base = os.path.basename(path)[:-4]
        count = 0
        for k, sprite in enumerate(cut(path), 1):
            sprite.thumbnail((SIZE, SIZE), Image.LANCZOS)
            sprite.save(os.path.join(OUT, f"{base}_{k:02d}.webp"), "WEBP",
                        quality=80, alpha_quality=80, method=6)
            count = k
        print(f"{base}: {count} sprites")


if __name__ == "__main__":
    main()
