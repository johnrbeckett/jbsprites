# jbsprites

Small character sprites shown inline in Claude chats, grouped in families. Each family folder holds 160 px transparent WebP sprites, with the full-size sheets they were cut from in `<family>/originals/`.

Sprites are served by jsDelivr, pinned to a tag:

    https://cdn.jsdelivr.net/gh/johnrbeckett/jbsprites@<tag>/<family>/<name>.webp

`SKILL.md` is the Claude skill that decides which sprite to show and when. `scripts/make_sprites.py <family>` cuts a family's sheets; `scripts/package.sh` builds the installable skill package.

Families: `tumnus` (a faun in business casual, with Narnia guests mixed in).

**Get it:** download `jbsprites.skill` from the [latest release](https://github.com/johnrbeckett/jbsprites/releases/latest), upload it in Claude (Settings > Capabilities > Skills), and add the one-line preference from [`docs/SETUP.md`](docs/SETUP.md) so every chat uses it.

The Narnia guest sprites are non-commercial fan art. The Chronicles of Narnia and its characters belong to their rights holders.

**Setting it up** (installing the skill, the one-line preference, hooking it into other skills, adding a family): see [`docs/SETUP.md`](docs/SETUP.md).
