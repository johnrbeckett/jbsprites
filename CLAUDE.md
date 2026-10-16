# jbsprites, standing rules for this repo

This repo is PUBLIC. Read `~/Developer/CLAUDE.md` first; it applies here.

- Nothing personal or work-specific goes in this repo: no names of people or employers, no keys, no tracker or mail details. Callers (tumnus, jbwriting, the user's preferences) stay private and only say "use jbsprites, family <name>".
- Never commit a `.env` or any credential. Push with a token from the keyserver, never stored in `.git/config`.
- Sprites are served from a tag via jsDelivr. Never move or delete a published tag. Up to v8 the sprites were under `tumnus/`; from v9 under `narnia/`. Old pinned links keep working because the old tags never change.
- `catalog/<family>.json` is the source of truth for every sprite's tags (characters, moments, activities, view, energy, seasons, status). SKILL.md never lists sprites. The picker (`scripts/pick.py`) reads `index/<family>.json`, built from the catalog by `scripts/build_index.py --tag vN`; the index pins URLs to that tag.
- Release: cut (`make_sprites.py`), `add_sheet.py`, review, `build_index.py --tag vN`, `test_pick.py` (must pass), commit, tag vN, push, check every index URL returns 200, `package.sh`, GitHub release with asset `jbsprites.skill`.
- Shared vocabulary lives in `scripts/vocab.py`; keep `docs/SHEET-BRIEF.md` and the picker in step with it.
- File numbers on indexed sheets are grid positions. Never re-cut a published sheet without an index (06 to 14): its numbering is reading order and could shift.
- The package carries only SKILL.md, `scripts/pick.py` and `index/`. Catalog, review pages, reports and originals stay maintainer-side.
- Log every commit and push in `docs/HANDOFF.md` in the same reply. Deletions go to `~/Developer/Trash/`.
