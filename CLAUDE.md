# jbsprites, standing rules for this repo

This repo is PUBLIC. Read `~/Developer/CLAUDE.md` first; it applies here.

- Nothing personal or work-specific goes in this repo: no names of people or employers, no keys, no tracker or mail details. Callers (tumnus, jbwriting, the user's preferences) stay private and only say "use jbsprites, family <name>".
- Never commit a `.env` or any credential. Push with a token from the keyserver, never stored in `.git/config`.
- Sprites are served from a tag via jsDelivr. Changing sprites means: cut, commit, tag the next version, then bump `@vN` in SKILL.md and repackage. Never move or delete a published tag.
- The default family's tables stay inline in SKILL.md (one read). Other families go in `families/<name>.md`.
- Log every commit and push in `docs/HANDOFF.md` in the same reply. Deletions go to `~/Developer/Trash/`.
