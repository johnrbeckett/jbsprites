# Setting up jbsprites

How to get the sprites showing in your own Claude chats, and how to hook them into other skills.

## What you need

- **The Claude desktop app or claude.ai.** Sprites are drawn with Claude's visual widget (the tool that renders charts and diagrams inline). Claude Code in a terminal has no widget, so sprites never show there.
- **Skills enabled** on your account (Settings > Capabilities).
- **Nothing else.** No keys, no server. The images load from jsDelivr, the one image host the widget allows that serves files from GitHub.

## 1. Install the skill

Download **`jbsprites.skill`** from the latest release:

    https://github.com/johnrbeckett/jbsprites/releases/latest/download/jbsprites.skill

Then in Claude: Settings > Capabilities > Skills > upload the `.skill` file. To update, remove the old jbsprites skill first, then upload the new one; an old copy left installed keeps its old rules and sprite list.

To build it yourself instead, run `scripts/package.sh` (writes `jbsprites_<date>.skill` to `~/Developer/Outputs/`; set `OUT=<folder>` to change that), or zip `SKILL.md`, `scripts/pick.py` and `index/` inside a folder named `jbsprites`.

## 2. Tell Claude when to use it

A skill only loads when something asks for it. Pick one or more of these.

### Everywhere: your Claude preferences

**The line:**

```
For any task that involves real work in the Claude desktop app or claude.ai, use the jbsprites skill (family narnia) for start and end sprites.
```

Put it in one of two places:

- **Personal preferences (most reliable):** Settings > Profile > "What personal preferences should Claude consider in responses?" Preferences are read at the start of every chat.
- **Memory:** if memory is on for your account, tell Claude "Remember this as a preference:" followed by the line. Check it was saved by asking "what do you remember about how I like you to work?"

Installing the skill alone is not enough: a skill loads only when something asks for it. Start a new chat afterwards; a chat that is already open does not pick up new preferences.

### Inside another skill

Add one line to that skill's `SKILL.md`, near the top so it is read early:

> Sprites: when the user is in the chat, use the jbsprites skill, family narnia: a start sprite as work begins and a done, oops or your-turn sprite when it ends. Invoke jbsprites alongside the first tool lookup so it adds no extra step. Never in scheduled runs.

The calling skill names the family; jbsprites holds all the rules and its picker chooses the sprite, so callers never carry sprite names of their own. A caller may also name a character ("family narnia, character aslan") to narrow the pick. If two skills that both call jbsprites are active in one turn, only one should run the sprites; say which in the second one ("if the X skill is also active, it already runs the sprites").

### Claude Code projects (CLAUDE.md)

Not useful today: Claude Code has no visual widget, so a `CLAUDE.md` line would load the skill and then find nothing to draw with. If you share a `CLAUDE.md` with Cowork (the desktop app's agent), the same one-line preference above works there, because Cowork has the widget.

## 3. Check it works

Start a new chat and ask for something that takes a few steps. You should see a sprite as the work begins and another after the reply. If none show:

- The skill is not installed, or the preference line is missing.
- The chat has no widget (Claude Code, or a surface without it).
- The chat has no shell: the picker is a Python script, so a surface without code execution shows no sprites.
- A sprite address fails: open `https://cdn.jsdelivr.net/gh/johnrbeckett/jbsprites@<tag>/narnia/08-celebrations_05.webp` in a browser. A new tag can take a minute to appear on jsDelivr.

## 4. What it costs

Each task runs the picker once (about 15 ms, alongside real work) and shows each sprite with one small widget call. The start sprite rides along with real work, so it adds no wait. The end sprite is one short step after the reply. The skill itself is about 1,400 tokens; the sprite list stays out of the chat. The first sprite in a chat also loads the widget's setup guide once.

## 5. Adding your own family

1. Make a sheet with its JSON index, following `docs/SHEET-BRIEF.md` (transparent PNG, a full grid, figures well apart).
2. Put both in `<family>/originals/` and run `python3 scripts/make_sprites.py <family> <NN>` (needs numpy, scipy, Pillow). Sprites come out as `<family>/<sheet>_<NN>.webp`, 160 px, NN = grid position.
3. `python3 scripts/add_sheet.py <NN> --family <family>` adds them to `catalog/<family>.json`; check them with `scripts/review_sheet.py`.
4. `python3 scripts/build_index.py --family <family> --tag vN`, then `scripts/test_pick.py`.
5. Commit, tag `vN`, push, check the links, and repackage. Tags are fixed once published.
6. Callers then say "use jbsprites, family <name>".

To use your own copy, fork the repo and change `johnrbeckett/jbsprites` in `scripts/build_index.py` to your fork.
