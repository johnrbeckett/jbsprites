# Handoff

## Status

| Item | State |
|---|---|
| Repo | johnrbeckett/jbsprites, PUBLIC (John's call, 2026-10-15: "I don't care if it's seen"). Skill, scripts and cut sprites; jsDelivr serves from tags. Full-size sheets moved to `johnrbeckett/jbsprites-art` (~/Developer/jbsprites-art) on 2026-10-16 so tags fit jsDelivr's 50 MB limit; v1-v9 tags still carry them. |
| Family narnia | Renamed from tumnus at v9 (folder `narnia/`; v1-v8 tags keep `tumnus/` links working). 588 cut sprites: 523 live (330 proposed, 193 reviewed: sheets 24-31, checked 2026-10-16), 58 unmapped (mostly sheet 11), 7 cut by John. Tags live in `catalog/narnia.json`; every wolf is Maugrim; beaver paws carry no character. Sheets 06-19 have no `view` yet (no descriptions). History of the tumnus-era sheets: v2-v8 entries below. |
| Callers | tumnus (SKILL.md, resources/morning-brief.md), jbwriting and jbpresentations now say "family narnia" (with an activity where it fits). Edited 2026-10-16, NOT committed in those repos; tumnus also needs its dist rebuilt. "tumnus" still works as an alias in the picker. |
| Skill | v10 (823 sprites, package jbsprites_2026-10-16c.skill, release v10). Was v9: SKILL.md (4.9 KB, no sprite names) + scripts/pick.py + index/narnia.json. Package ~/Developer/Outputs/jbsprites_2026-10-16b.skill points at @v9; release v9 asset. Not yet installed. |
| Open | John reinstalls v9 and updates his preference line. jsDelivr size limit: fixed from v10 by the art-repo split (v1-v9 trees stay ~61 MB and can still 403 cold). Commit the three caller repos. Fill `view` for sheets 06-19. Sheet 11 and 12_01 unmapped. Update the preference line to "family narnia". |

## In flight (2026-10-16, NOT committed)

Sheets 44 to 58 (375 sprites, from the narnia-complete handoff bundle) are imported locally. The sources are in jbsprites-art/narnia/originals (uncommitted there too). They were cut with make_sprites.py, and all 375 match the bundle's own cuts byte for byte. They were added to the catalog as proposed. vocab.py and SHEET-BRIEF.md gained 40 characters, with Jewel kept separate from unicorn and no Dufflepuds. The index was rebuilt with --tag v11 (1198 assets) and test_pick passes, but v11 is not tagged or pushed, so index URLs 404 until then. The bundle's sheets 32-42 and pevensies_02 override were identical to what is already here. Its 43 PNG is the older pre-restyle version, so it was ignored. Bundle zip in ~/Developer/Trash/jbsprites-import-scratch-2026-10-16/. Next: John reviews review/narnia-review.html, then commit both repos, tag v11, push, check URLs, package, release. Open idea from the bundle's REPETITION-AUDIT: composition_group metadata and recency in pick.py.

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
- 10ab9bf v9 (2026-10-16): picker replaces the sprite tables, family tumnus renamed narnia, catalog + index + tests, cutter numbers by grid position, docs/SHEET-BRIEF.md. Pushed 2026-10-16 with tag v9 (78fbc49 HANDOFF on top). All 523 index URLs returned 200 on jsDelivr (cold fetches 403 at first and needed retries, see Open). Release v9 published with asset jbsprites.skill (package jbsprites_2026-10-16b.skill); latest/download serves it.
- Correction (2026-10-16, in v10): 24-pevensies-at-work_02 redrawn (full legs and shoes, transparent; the old cut had a white box and cropped feet). New `narnia/overrides/` (webp + source PNG + README); `make_sprites.py` copies overrides over cut files after cutting. Old webp in ~/Developer/Trash/jbsprites-pevensies-02-old-2026-10-16/. Live in v10; the v9 URL keeps the old art.
- Later-books expansion (2026-10-16, in v10): sheets 32-43 (300 sprites: Reepicheep, Puddleglum, Eustace incl. dragon, Caspian, Trumpkin, Cornelius, repaired Tumnus, Bree and Hwin, Jill, Uncle Andrew, objects, scenes) cut with make_sprites.py, all 25 per sheet, checked by eye on light and dark. Added to the catalog as proposed from the bundle manifest (bundle sidecars rebuilt into full sheet JSONs in originals/). Vocab gains 11 characters plus `centaur` (already in use, was missing). Index rebuilt for v10 (823 assets); test_pick passes. Sheet 43 replaced the same day with a restyled version that matches the other sheets (same layout, ids and tags); re-cut and checked, old sheet and cuts in ~/Developer/Trash/jbsprites-sheet43-v1-2026-10-16/. Glimfeather kept as his own character (John). 
- 53de5ae v10 (2026-10-16): later-books expansion, pevensies_02 fix, originals split to johnrbeckett/jbsprites-art (f19b937, pushed). Pushed with tag v10; tag tree ~10 MB; all 823 index URLs returned 200 on jsDelivr first time (no cold 403s). Release v10 published with asset jbsprites.skill (package jbsprites_2026-10-16c.skill); latest/download serves it. John to reinstall.
