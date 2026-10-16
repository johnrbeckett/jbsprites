#!/bin/bash
# Package the jbsprites skill into ~/Developer/Outputs/jbsprites_<date>.skill
# The package holds SKILL.md, the picker (scripts/pick.py) and its index (index/*.json).
# No images (they load from jsDelivr), no catalog, review or report files (maintainer side only).
# Build the index for the release first: python3 scripts/build_index.py --tag vN
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="${OUT:-$HOME/Developer/Outputs}"
STAMP="${STAMP:-$(TZ=America/New_York date +%Y-%m-%d)}"
TMP="$(mktemp -d)"; mkdir -p "$TMP/jbsprites/scripts" "$TMP/jbsprites/index"
cp "$ROOT/SKILL.md" "$TMP/jbsprites/"
cp "$ROOT/scripts/pick.py" "$ROOT/scripts/flatten.py" "$TMP/jbsprites/scripts/"
cp "$ROOT"/index/*.json "$TMP/jbsprites/index/"
( cd "$TMP" && zip -qr "$TMP/jbsprites_$STAMP.skill" jbsprites )
mkdir -p "$OUT"; cp "$TMP/jbsprites_$STAMP.skill" "$OUT/"
echo "wrote $OUT/jbsprites_$STAMP.skill"; unzip -l "$OUT/jbsprites_$STAMP.skill" | tail -n +4 | head -6
