#!/bin/bash
# Package the jbsprites skill into ~/Developer/Outputs/jbsprites_<date>.skill
# The package holds SKILL.md (and families/*.md when they exist). No images: they load from jsDelivr.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="${OUT:-$HOME/Developer/Outputs}"
STAMP="${STAMP:-$(TZ=America/New_York date +%Y-%m-%d)}"
TMP="$(mktemp -d)"; mkdir -p "$TMP/jbsprites"
cp "$ROOT/SKILL.md" "$TMP/jbsprites/"
[ -d "$ROOT/families" ] && cp -r "$ROOT/families" "$TMP/jbsprites/"
( cd "$TMP" && zip -qr "$TMP/jbsprites_$STAMP.skill" jbsprites )
mkdir -p "$OUT"; cp "$TMP/jbsprites_$STAMP.skill" "$OUT/"
rm -rf "$TMP"; echo "wrote $OUT/jbsprites_$STAMP.skill"
