# Handoff

## Status

| Item | State |
|---|---|
| Repo | johnrbeckett/jbsprites, PUBLIC (John's call, 2026-10-15: "I don't care if it's seen"). Skill, scripts, originals and sprites in one repo; jsDelivr serves from tags. |
| Family narnia | Renamed from tumnus at v9 (folder `narnia/`; v1-v8 tags keep `tumnus/` links working). 588 cut sprites: 523 live (330 proposed, 193 reviewed: sheets 24-31, checked 2026-10-16), 58 unmapped (mostly sheet 11), 7 cut by John. Tags live in `catalog/narnia.json`; every wolf is Maugrim; beaver paws carry no character. Sheets 06-19 have no `view` yet (no descriptions). History of the tumnus-era sheets: v2-v8 entries below. |
| Callers | tumnus (SKILL.md, resources/morning-brief.md), jbwriting and jbpresentations now say "family narnia" (with an activity where it fits). Edited 2026-10-16, NOT committed in those repos; tumnus also needs its dist rebuilt. "tumnus" still works as an alias in the picker. |
| Skill | v9: SKILL.md (4.9 KB, no sprite names) + scripts/pick.py + index/narnia.json. Package ~/Developer/Outputs/jbsprites_2026-10-16b.skill points at @v9. Not yet installed. |
| Open | Push v9 + tag, check all 523 index URLs return 200, publish release v9 with asset jbsprites.skill, John reinstalls. Commit the three caller repos. Fill `view` for sheets 06-19. Sheet 11 and 12_01 unmapped. Update the preference line to "family narnia". |

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
- v8.2 (2026-10-16): scheduled runs may show ONE sprite when a caller skill's unattended morning brief asks for it (Tumnus step 8); image at the top of the output and of the posted digest. Sprites unchanged, widget URL stays @v8. Packaged as jbsprites_2026-10-16.skill. Pushed 2026-10-16 (9d68ed6). No tag yet; tag v8.2 + release asset when John wants it.
- 10ab9bf v9 (2026-10-16): picker replaces the sprite tables, family tumnus renamed narnia, catalog + index + tests, cutter numbers by grid position, docs/SHEET-BRIEF.md. Tag v9 created locally. **Committed, NOT pushed.** Package jbsprites_2026-10-16b.skill.
