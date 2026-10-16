# Handoff

## Status

| Item | State |
|---|---|
| Repo | johnrbeckett/jbsprites, PUBLIC (John's call, 2026-10-15: "I don't care if it's seen"). Skill, scripts, originals and sprites in one repo; jsDelivr serves from tags. |
| Family tumnus | 25 sheets (06 to 08, 10 to 31), 581 sprites. v6 added sheets 24 to 31, Narnia-goes-to-work fan art (John's call, 2026-10-15: kept in jbsprites as part of tumnus, not a separate repo), as a Narnia guests table used about one beat in four. v7 (same day): the separate table never got picked (the model stopped at the main table), so the Narnia sprites are now interleaved into the main rows, about one pick in three. John cut 7 from the contact sheet (25-07, 27-01 to 27-05, 31-11); those webps were never added. De-dup clean. Cutter: when two touching objects share one core and leave a grid cell empty, it splits along the grid; MIN_CORE env var overrides the 2,500 px core size. v5 added 20 meetings and deep focus, 21 research and inbox, 22 mobile, travel and waiting, 23 small wins and holidays (new rows: Meetings, Deep focus, On the go, Sent; new Holidays table; the rest folded into existing rows). De-dup: 23_03, 23_06, 23_13, 23_21 repeat 14_02, 14_03, 13_02, 13_20 in a new outfit and are left out of the tables. The cutter now finds uneven row bands from the figures and keeps loose pieces whole. v4 added 19 image and design work (20 poses, the Image row) and a de-dup pass: four near-identical repeats dropped from the tables (16_06, 15_07, 16_19, 07_27); files stay in the repo. v3 added 15 mishaps and message edges, 16 working and discoveries, 17 after hours and seasonal (new Seasons table), 18 visitors and playful tech; the cutter now groups by grid cell when a sheet has a JSON index. (v2 added 13 icons/hands/busts and 14 calendar/money/tech: small Done, Signing off, calendar, invoices, technical, image, long-wait rows), moved here from the private tumnus repo. Sheet 11 (office props) cut but unmapped. |
| Callers | tumnus and jbwriting each carry one line ("use jbsprites, family tumnus"). Replaces tumnus Appendix G and the old public tumnus-sprites repo, which John deleted on 2026-10-15. |
| Skill | Package via scripts/package.sh. Installed and working in chat since 2026-10-15. Current package ~/Developer/Outputs/jbsprites_2026-10-15g.skill points at tag v8 (also release v8 asset jbsprites.skill); John reinstalls it after each tag. |
| Open | Sheet 11 (office props) and 12_01 (dropped papers) are unmapped. John's Claude Code clone of jbwriting (~/.claude/skills/jbwriting) needs a git pull. Image and design work is now covered. Sheet 15's point-down and lean poses are only partly used. |

## Commits

- c723246 Skill, scripts and the tumnus family. Pushed 2026-10-15, tag v1; all mapped sprites verified 200 on jsDelivr.
- 9c0a2ca End sprite goes after the reply (start and end were stacking). Pushed.
- 92ad1c0 HANDOFF: tumnus-sprites repo deleted. Pushed.
- f87b9ea Sheets 13 and 14, tag v2; new rows verified 200 on jsDelivr. Pushed 2026-10-15.
- ab2658a HANDOFF. Pushed.
- 5122d3d Sheets 15 to 18, tag v3, grid-index cutting, Seasons table; all 78 new mapped sprites verified 200 on jsDelivr. Pushed 2026-10-15.
- 353491e HANDOFF. Pushed.
- fb757ff Sheet 19, de-dup pass, tag v4; all 238 mapped sprites verified 200. Pushed 2026-10-15.
- b88409f docs/SETUP.md (install, preference line, hooking other skills, Claude Code limits, adding a family). Pushed.
- 60f2e6d Sheets 20 to 23, tag v5; all 92 new mapped sprites verified 200. Pushed 2026-10-15.
- 3d68aeb Narnia sheets 24 to 31, tag v6; all 523 mapped sprites verified 200. Pushed 2026-10-15.
- Cowork placement fix (2026-10-15): a one-line progress note after the start sprite so the two never stack; for real work the reply goes out as a message, then the end sprite, then a short closing phrase as the final text (the app demands final text and does not render images in text, tested). No new tag; sprites unchanged. Pushed, and packaged as jbsprites_2026-10-15b.skill.
- Closing phrases table (2026-10-15): about 80 short lines across eleven endings, picked at random, never the one just before. Pushed, packaged as jbsprites_2026-10-15c.skill.
- Offers allowed in closing phrases (John, 2026-10-15: "you can make offers to me"). Packaged as jbsprites_2026-10-15d.skill.
- 8a9f220 Narnia interleaved into the main rows (the separate guest table was never picked), tag v7; all 523 verified 200. Pushed 2026-10-15.
- fef50df README and SETUP point at the GitHub release; preference or memory line. Pushed.
- GitHub release v7 published 2026-10-15, asset jbsprites.skill (stable name, so releases/latest/download/jbsprites.skill always works). For each new tag: package, create a release on the tag, upload the asset as jbsprites.skill.
- README Quick start and SETUP put the preference line in a copyable code block with where to paste it; release v7 notes updated to match. Pushed 2026-10-15.
- Contextual random pick, tag v8 (2026-10-15): the model shortlists sprites that fit the moment (at least four, from two sheets, one Narnia guest when the row has one), then a one-line python draw picks. Judgement alone kept landing on the first, plain Tumnus entries. Sprites unchanged; v8 marks the skill change. Widget URL bumped to @v8 before tagging (df42efc still said @v7). Packaged as jbsprites_2026-10-15g.skill; release v8 carries it as jbsprites.skill. Pushed 2026-10-15.
- v8.1 (2026-10-15): the draw example uses placeholders instead of real sprite names, so models do not copy the example list. Widget URL stays @v8 (sprites unchanged). Release v8.1 with asset jbsprites.skill.
- v8.2 (2026-10-16): scheduled runs may show ONE sprite when a caller skill's unattended morning brief asks for it (Tumnus step 8); image at the top of the output and of the posted digest. Sprites unchanged, widget URL stays @v8. Packaged as jbsprites_2026-10-16.skill. Committed from Cowork; push pending.
