# Handoff

## Status

| Item | State |
|---|---|
| Repo | johnrbeckett/jbsprites, PUBLIC (John's call, 2026-10-15: "I don't care if it's seen"). Skill, scripts, originals and sprites in one repo; jsDelivr serves from tags. |
| Family tumnus | 17 sheets (06 to 08, 10 to 23), 388 sprites. v5 added 20 meetings and deep focus, 21 research and inbox, 22 mobile, travel and waiting, 23 small wins and holidays (new rows: Meetings, Deep focus, On the go, Sent; new Holidays table; the rest folded into existing rows). De-dup: 23_03, 23_06, 23_13, 23_21 repeat 14_02, 14_03, 13_02, 13_20 in a new outfit and are left out of the tables. The cutter now finds uneven row bands from the figures and keeps loose pieces whole. v4 added 19 image and design work (20 poses, the Image row) and a de-dup pass: four near-identical repeats dropped from the tables (16_06, 15_07, 16_19, 07_27); files stay in the repo. v3 added 15 mishaps and message edges, 16 working and discoveries, 17 after hours and seasonal (new Seasons table), 18 visitors and playful tech; the cutter now groups by grid cell when a sheet has a JSON index. (v2 added 13 icons/hands/busts and 14 calendar/money/tech: small Done, Signing off, calendar, invoices, technical, image, long-wait rows), moved here from the private tumnus repo. Sheet 11 (office props) cut but unmapped. |
| Callers | tumnus and jbwriting each carry one line ("use jbsprites, family tumnus"). Replaces tumnus Appendix G and the old public tumnus-sprites repo, which John deleted on 2026-10-15. |
| Skill | Package via scripts/package.sh. Installed and working in chat since 2026-10-15. Current package ~/Developer/Outputs/jbsprites_2026-10-15.skill points at tag v5; John reinstalls it after each tag. |
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
- Next commit: sheets 20 to 23, tag v5. See git log for push state.
