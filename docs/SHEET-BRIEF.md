# Sheet brief: making new sprite sheets with ChatGPT

Paste the **Prompt** section into ChatGPT along with one or two existing sheets from
`jbsprites-art/narnia/originals/` as style and character references. Ask for one
sheet per request. Every sheet comes back as two files: the PNG and its JSON index.

Before asking, check **What to make next** below. It lists the moments the picker is short of.

## Prompt

> Make one sprite sheet for a set of small chat stickers. Match the attached reference sheets
> exactly in style and in how each character looks.
>
> **Style:** detailed pixel-art illustration, soft painterly shading, a dark outline around every
> figure, a warm palette, slightly large heads, three-quarter view. Office life, business casual.
> Characters keep their own look from the reference sheets in every cell.
>
> **Canvas:** one PNG with a fully transparent background, 1254 x 1254 px, a 5 x 5 grid (25 cells).
> Nothing behind or around the figures: no background, floor, shadow, glow, haze, vignette or frame.
>
> **Cells:** one subject per cell, centred, filling most of the cell. Leave at least 40 px of clear
> space between neighbouring subjects. Nothing crosses into another cell or touches the edge of the
> canvas. A prop a character holds must touch the character. Fill all 25 cells.
>
> **Content:** no words, letters or numbers anywhere (signs and screens stay blank). Nothing violent
> or frightening. Keep scenes with two or more characters to a few cells.
>
> **Theme for this sheet:** <the theme, for example "things going wrong: offline, not found, timed out">.
> Cells I need: <list from What to make next, or describe>.
>
> **Also return a JSON file** describing every cell, using exactly this shape and only the words
> listed in the vocabulary below:
>
> ```json
> {
>   "sheet": "<NN>-<short-name>.png", "columns": 5, "rows": 5,
>   "assets": [
>     {"row": 1, "column": 1,
>      "description": "Tumnus blazer unplugging a tangled cable",
>      "characters": ["tumnus"],
>      "view": "full-body",
>      "moments": ["offline"],
>      "activities": [],
>      "energy": "subdued",
>      "seasons": []}
>   ]
> }
> ```

## Vocabulary

Use only these words in the JSON. Anything else is ignored by the build.

- **characters** (who is visibly in the picture; empty for objects and places): `tumnus`, `lucy`,
  `edmund`, `susan`, `peter`, `aslan`, `white-witch`, `mr-beaver`, `mrs-beaver`, `father-christmas`,
  `dryad`, `maugrim` (every wolf is Maugrim), `fox`, `robin`, `owl`, `dwarf`, `unicorn`, `centaur`,
  `reepicheep`, `puddleglum`, `eustace` (also as a dragon), `caspian`, `trumpkin`, `doctor-cornelius`,
  `glimfeather`, `bree`, `hwin`, `jill`, `uncle-andrew`,
  and from sheets 44 to 58: `ahoshta`, `aravis`, `bulgy-bear`, `coriakin`, `corin`, `digory`, `drinian`, `farsight`, `father-time`, `fledge`, `frank`, `ginger`, `golg`, `green-lady`, `gumpas`, `hermit`, `jewel`, `king-lune`, `lasaraleen`, `miraz`, `mouse`, `mrs-macready`, `nikabrik`, `pattertwig`, `poggin`, `polly`, `professor-kirke`, `puzzle`, `rabadash`, `ramandu`, `ramandus-daughter`, `rilian`, `rishda-tarkaan`, `rumblebuffin`, `sea-serpent`, `shasta`, `shift`, `tirian`, `tisroc`, `trufflehunter`, and from sheets 59 to 72: `alberta-scrubb`, `arsheesh`, `aunt-letty`, `camillo`, `chervy`, `clodsley-shovel`, `dar`, `darrin`, `emeth`, `ginarrbrick`, `glenstorm`, `glozelle`, `griffle`, `gwendolen`, `harfang-king`, `harfang-queen`, `harold-scrubb`, `hogglestock`, `nurse`, `pittencream`, `prunaprismia`, `rhince`, `roonwit`, `rynelf`, `slinkey`, `sopespian`, `the-head`, `wimbleweather`, `wraggle`. Jewel stays separate from `unicorn`; every Earthman is `golg`; Helen is tagged `frank`; Jadis is `white-witch`. A new character needs a new
  lowercase hyphenated name, added here when the sheet is accepted.
- **view:** `full-body`, `portrait` (head and shoulders or waist up), `hands`, `object`,
  `environment` (a place with no figure), `scene` (two or more characters).
- **moments:** `start`, `hello`, `morning-brief`, `waiting`, `waiting-long`, `retrying`,
  `done-small`, `done`, `big-win`, `sent`, `signing-off`, `oops`, `blocked`, `offline`,
  `timed-out`, `not-found`, `tangled`, `your-turn`.
- **activities** (only for `start`): `writing`, `research`, `email`, `scheduling`, `money`,
  `technical`, `design`, `meetings`, `focus`, `travel`, `mobile`, `handoff`, `general`,
  `tracker-add`, `tracker-list`, `tracker-next`, `tracker-now`, `tracker-gaps`, `tracker-review`.
- **energy:** `subdued` (calm, quiet, small), `moderate` (busy, ordinary), `celebratory` (cheering,
  arms up, confetti).
- **seasons:** `autumn`, `winter`, `spring`, `summer`, `thanksgiving`, `christmas`, `new-year`.

**Energy has to fit the moment.** `oops`, `blocked`, `offline`, `timed-out`, `not-found` and
`tangled` are never celebratory. `done-small` and `signing-off` are subdued or moderate.
`big-win` is celebratory. A pose that works for several moments can list them all.

## What to make next

From `reports/coverage.md` (rerun `scripts/coverage.py` to refresh). Ranked by need:

1. **Failures with only a handful of poses:** `offline` (1), `not-found` (4), `timed-out` (5).
2. **Seasons:** `summer` (2), `autumn` (3), `spring` (5). Thanksgiving and New Year have 3 each.
3. **Small start rows:** `tracker-add` (5), `handoff` (6), `tracker-review` (6),
   `tracker-now` (7), `mobile` (8), `sent` (8, half of them objects).
4. **Guests in endings:** the Narnia guests are rare in `done`, `your-turn`, `oops` and
   `waiting`. A sheet of guests finishing, asking and stumbling would balance the draw.

## When a sheet comes back

1. Put the PNG and the JSON in `~/Developer/Incoming/`.
2. Check it before cutting: transparent background, every cell filled, nothing touching.
3. Copy both into `jbsprites-art/narnia/originals/` with the next sheet number, then run
   `python3 scripts/make_sprites.py narnia <NN>`, then `python3 scripts/add_sheet.py <NN>`.
4. The JSON becomes catalog entries with status `proposed`. Review them in the contact sheet
   (`scripts/review_sheet.py <NN> <NN>`) before they go live.
