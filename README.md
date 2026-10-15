# jbsprites

Small character sprites shown inline in Claude chats, grouped in families. Each family folder holds 160 px transparent WebP sprites, with the full-size sheets they were cut from in `<family>/originals/`.

Sprites are served by jsDelivr, pinned to a tag:

    https://cdn.jsdelivr.net/gh/johnrbeckett/jbsprites@<tag>/<family>/<name>.webp

`SKILL.md` is the Claude skill that decides which sprite to show and when. `scripts/make_sprites.py <family>` cuts a family's sheets; `scripts/package.sh` builds the installable skill package.

Families: `tumnus`.
