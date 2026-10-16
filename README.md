# jbsprites

Small character sprites shown inline in Claude chats: one as work begins, one after the reply.

## Quick start

1. Download **[`jbsprites.skill`](https://github.com/johnrbeckett/jbsprites/releases/latest/download/jbsprites.skill)** from the latest release.
2. In Claude (desktop app or claude.ai): Settings > Capabilities > Skills, upload it.
3. Paste this line into Settings > Profile > "What personal preferences should Claude consider in responses?"

```
For any task that involves real work in the Claude desktop app or claude.ai, use the jbsprites skill (family narnia) for start and end sprites.
```

4. Start a new chat. A sprite shows as work begins and another after the reply.

The line is what makes every chat use the skill; without it the skill only loads when something asks for it. More in [`docs/SETUP.md`](docs/SETUP.md).

## How it works

Sprites are grouped in families. Each family folder holds 160 px transparent WebP sprites, with the full-size sheets they were cut from in `<family>/originals/`.

Sprites are served by jsDelivr, pinned to a tag:

    https://cdn.jsdelivr.net/gh/johnrbeckett/jbsprites@<tag>/<family>/<name>.webp

`SKILL.md` is the Claude skill that says when to show a sprite. Which sprite is chosen by `scripts/pick.py`, a small picker shipped inside the skill: it reads a compact index built from `catalog/<family>.json` (every sprite's characters, moments, activities, energy and seasons) and draws at random, so Claude never loads the sprite list.

Maintainer tools: `scripts/make_sprites.py` cuts sheets, `scripts/add_sheet.py` adds a cut sheet to the catalog, `scripts/review_sheet.py` builds a contact sheet for review, `scripts/coverage.py` reports gaps, `scripts/build_index.py` builds the index, `scripts/test_pick.py` checks the picker, `scripts/package.sh` builds the skill. `docs/SHEET-BRIEF.md` is the brief for making new sheets with an image model.

Families: `narnia` (Mr Tumnus in business casual, with the Pevensies, Aslan, the White Witch, the Beavers and other Narnians at work). Up to v8 the same sprites lived under `tumnus/`; those pinned links still work.

The Narnia guest sprites are non-commercial fan art. The Chronicles of Narnia and its characters belong to their rights holders.

**Setting it up** (installing the skill, the one-line preference, hooking it into other skills, adding a family): see [`docs/SETUP.md`](docs/SETUP.md).
