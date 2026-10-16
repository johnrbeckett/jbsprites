---
name: jbsprites
description: Small character sprites shown inline in chat for personality, in families (default narnia). A start sprite rides along when work begins; a done, oops or your-turn sprite closes it. Use whenever another skill or the user's preferences say to use jbsprites, or when real work starts in a chat the user is present for. Shown with the visual widget tool, or on a phone as a small file card; images load from cdn.jsdelivr.net.
---

# jbsprites

Small sprites that give work some personality. Pure decoration: a sprite never carries information the text does not, and is never mentioned, described or narrated.

A caller (another skill, or the user's preferences) names the family. None named means **narnia** (`tumnus` is an old name for it). A caller may also name a character; otherwise leave it out, and the picker chooses across the whole family.

## When

Every task the user asks for in chat gets two beats, one at each end of the turn, never stacked:

1. **Start**, as the work begins.
2. **End**, at the close of the turn, matching what actually happened:
   - `done-small` for a quick or minor task; `done` for real work; `big-win` when several things finished or a milestone landed; `sent` when an email or message went out; `signing-off` for the last task of the day or a Friday afternoon.
   - `oops` when work failed or could not be finished, or the closer fit: `blocked`, `offline`, `timed-out`, `not-found`, `tangled`. Then say plainly what failed. **Never show a done sprite for work that did not get done.**
   - `your-turn` when the reply ends with a question or a decision for the user.

A reply that needs no work gets one sprite, after the reply. A long task may show `done` after each separate piece. A retry after a failure may carry `retrying`. A tracker skill's first reply in a chat uses `hello`; a morning brief uses `morning-brief` (seasons and holidays are handled by the picker).

Scheduled or unattended runs show no sprites, except a morning brief a caller skill asks for: one `morning-brief` sprite as an image at the top of the output and of any post it writes (`<img>` 120px high in HTML, a markdown image otherwise). In an attended chat with neither a widget tool nor a way to send files, skip sprites silently.

## Picking

Run the picker in this skill's folder. It does the matching and the random draw; never choose a sprite yourself.

```
python3 <this skill's folder>/scripts/pick.py '{"family":"narnia","activity":"<activity>","moment":["start","done-small","done","oops","your-turn"],"avoid":[<ids already shown in this chat>],"phrase":true}'
```

- **activity:** `writing`, `research`, `email`, `scheduling`, `money`, `technical`, `design`, `meetings`, `focus`, `travel`, `mobile`, `handoff`, `general`, or for tracker skills `tracker-add`, `tracker-list`, `tracker-next`, `tracker-now`, `tracker-gaps`, `tracker-review`.
- **moment:** one, or a list to get several at once. Ask for the start and the likely endings in one call at the start of the task; show the start pick now and keep the rest. At the end show only the pick matching the outcome. If the outcome needs a moment you did not ask for (`blocked`, `sent`, `big-win`...), call again alongside the last work call.
- **avoid:** the ids of sprites already shown in this chat (the last two or three are enough).
- Optional: `character` (narrows to that character; the picker falls back across the family when that character has nothing suitable), `date` (`YYYY-MM-DD`).

It prints `{"url":...,"id":...,"character":...}` (keyed by moment for a list), plus `phrase` for end moments. `{}` means skip the sprite. Never let a picker problem slow or stop the real work.

## How (keep sprites off the critical path)

- Load the widget tools (`mcp__visualize__read_me`, `mcp__visualize__show_widget`) in the same ToolSearch call as the other tools the task needs. Call read_me once per chat, silently, alongside the first real work call.
- Run the picker in the same parallel batch as the first real work call, never as a step of its own. Send the start sprite with the next real work call. No real work call to ride with means no start sprite.
- The end sprite goes AFTER the reply, never on top of it:
  - Where text written before a tool call shows in full (claude.ai): write the reply, then call the widget last, and write nothing after it.
  - Where text between tool calls is collapsed (the Cowork desktop app):
    - Right after the start sprite, send a one-line progress note with SendUserMessage, so the two sprites never stack. No note to send means no start sprite.
    - Real work: send the reply with SendUserMessage, then the end sprite, then the pick's `phrase` as the final text (a fresh line in the same spirit is fine; never the one used just before).
    - Quick tasks (a reply of a few lines): the end sprite, then the reply as the final text.
- Widget code, nothing else in it:

`<h2 class="sr-only">Sprite</h2><img alt="" style="height:120px" src="<url>">`

## On a phone

Phone apps do not show widgets, markdown images or SVG; they show only image files sent to the chat, on a solid background. The session cannot tell that the user is on a phone or which colour mode it uses, so:

- **Phone mode** is on when the user says they are on their phone (or "phone mode", "on mobile"), or when the session reports a mobile client. It lasts for the rest of the chat; "desktop" or "back on my computer" turns it off. Never switch on a guess.
- In phone mode, every sprite goes out as a file instead of a widget, at the same moments and in the same order (start, progress note, reply, end sprite, phrase):

```
python3 <this skill's folder>/scripts/flatten.py '<url from the picker>' <outputs folder>/sprites/<moment>-<id>.png
```

  then send the printed path with the file-sending tool, display `render`, no caption. Nothing printed means skip that sprite.
- The background is `#FAF9F5`, the chat's light-mode colour, so the sprite blends in. A caller or the user's preferences may name another (`--bg "#262624"` for dark mode).
