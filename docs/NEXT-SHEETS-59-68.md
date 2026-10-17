# Next sheets 59 to 68: new characters and the 1940s office

Ten sheets, 25 cells each, 250 cells in all. Planned 2026-10-16 after ChatGPT's feedback.

**The look.** 1940s British office and modern office, mixed freely, with no era tag. Tweed, waistcoats, cardigans, Bakelite phones, typewriters, wireless sets, switchboards, pneumatic tubes, tea trolleys and blank ration books sit alongside laptops, phones and server racks. Use modern kit where it makes the task obvious (a server rack reads "technical" at once). Use period kit everywhere else for charm. Whatever ChatGPT mixes in a given cell is fine.

**The humour.** Character-driven, not generic office poses. Each character has a specialty that becomes a running joke:

| Character | Specialty |
|---|---|
| Mice | Teamwork: chains, relays, carrying things together |
| Trufflehunter | Patient administration: forms, stamps, red tape |
| Pattertwig, Chervy | Dispatch and couriering |
| Ginger, Sopespian | Snooping |
| Puddleglum | Gloomy forecasting that turns out fine |
| Reepicheep | Challenging uncooperative machines to duels |
| Glenstorm, Roonwit | Forecasting and analysis |
| Wimbleweather | Well-meaning mishaps |
| Aunt Letty | Running the office sensibly around Uncle Andrew |
| Sea serpent | Gentle helpfulness, cables, tea |

Paste the Prompt from `SHEET-BRIEF.md` once per sheet. Set the theme line and the cell list from below, and attach two existing sheets as style references (one that shows the same characters, where there is one).

House rules, unchanged:

- Children from the books are drawn as adults in business casual or period office dress.
- Nothing violent or frightening. Villains are stern or comic. No Tash, no battles. Swords point at printers, never at people.
- No words, letters or numbers anywhere. Signs, forms, screens, chalkboards and nameplates stay blank.
- No brand names or logos on modern kit.

## New character names for `scripts/vocab.py`

Add these when each sheet is accepted (23 in all):

| Sheet | New names |
|---|---|
| 59 | `aunt-letty` |
| 60 | `glenstorm`, `wimbleweather`, `glozelle`, `sopespian`, `prunaprismia`, `nurse`, `gwendolen` |
| 61 | `chervy`, `arsheesh`, `dar`, `darrin` |
| 62 | `rhince`, `rynelf`, `pittencream`, `harold-scrubb`, `alberta-scrubb` |
| 63 | `the-head`, `harfang-king`, `harfang-queen` |
| 64 | `roonwit`, `emeth`, `griffle`, `wraggle`, `slinkey` |
| 65 | `ginarrbrick` |

Glenstorm's sons are tagged `centaur`. Slinkey stays separate from the generic `fox`.

Cell format: **row,col** · description · characters · view · moments · activity (start only) · energy · season.

---

## 59 · aunt-letty-runs-the-office

Theme: Uncle Andrew's study as a cluttered 1940s office. Aunt Letty, sensible in tweed and pearls, keeps it running despite him. New character, so cell 1,1 sets her look.

1,1 · Aunt Letty in a tweed suit and pearls, waving from behind a typewriter · aunt-letty · full-body · hello · · moderate
1,2 · Aunt Letty typing briskly at a heavy black typewriter · aunt-letty · full-body · start · writing · moderate
1,3 · Aunt Letty sorting the morning post with a brass letter opener · aunt-letty · full-body · morning-brief · · moderate
1,4 · Aunt Letty pouring tea from a big brown teapot · aunt-letty · full-body · done-small · · moderate
1,5 · Aunt Letty, arms folded, barring Uncle Andrew's study door · aunt-letty, uncle-andrew · scene · blocked · · moderate
2,1 · Aunt Letty and Uncle Andrew tugging opposite ends of a ledger · aunt-letty, uncle-andrew · scene · start · money · moderate
2,2 · Uncle Andrew sneaking a biscuit from the tin behind her back · uncle-andrew · full-body · your-turn · · moderate
2,3 · Aunt Letty filing carbon copies into a wooden cabinet · aunt-letty · full-body · start · tracker-add · moderate
2,4 · Aunt Letty on a Bakelite telephone, pencil poised · aunt-letty · full-body · start · scheduling · moderate
2,5 · Aunt Letty peering over her spectacles at a smoking contraption · aunt-letty · portrait · oops · · moderate
3,1 · Uncle Andrew's contraption sparking from a frayed cable · · object · tangled · · moderate
3,2 · Aunt Letty bandaging Uncle Andrew's singed finger · aunt-letty, uncle-andrew · scene · retrying · · subdued
3,3 · Digory delivering a telegram envelope to her desk · digory, aunt-letty · scene · sent · · moderate
3,4 · Polly at a switchboard, plugging in cords · polly · full-body · start · email · moderate
3,5 · Polly hopelessly tangled in switchboard cords · polly · full-body · tangled · · moderate
4,1 · Aunt Letty winding the office clock and frowning at it · aunt-letty · full-body · waiting · · subdued
4,2 · Aunt Letty asleep in an armchair, knitting in her lap · aunt-letty · full-body · waiting-long · · subdued
4,3 · An empty in-tray and a tidy blotter at day's end · · object · done · · subdued
4,4 · Aunt Letty pinning on her hat at the coat stand · aunt-letty · full-body · signing-off · · subdued
4,5 · Aunt Letty knitting one very long scarf for the whole office · aunt-letty · full-body · start · focus · subdued · winter
5,1 · Aunt Letty with a tray of mince pies at the office party · aunt-letty · full-body · big-win · · celebratory · christmas
5,2 · Aunt Letty searching a drawer by torchlight · aunt-letty · full-body · not-found · · subdued
5,3 · Aunt Letty's hand pulling the contraption's plug from the wall · aunt-letty · hands · offline · · subdued
5,4 · Uncle Andrew presenting a chalkboard of shapes and arrows · uncle-andrew · full-body · start · meetings · moderate
5,5 · Aunt Letty raising her teacup in a toast · aunt-letty · portrait · done · · celebratory

## 60 · caspian-court-and-camp

Theme: Prince Caspian's supporting cast. Glenstorm forecasts, Wimbleweather means well, Glozelle and Sopespian scheme comically, Prunaprismia disapproves, the Nurse tells stories, Gwendolen escapes a dull training session.

1,1 · Glenstorm the centaur at a desk with a brass telescope · glenstorm · full-body · morning-brief · · moderate
1,2 · Glenstorm pinning stars onto a big wall chart · glenstorm · full-body · start · scheduling · moderate
1,3 · Glenstorm tapping a chart, quietly proven right · glenstorm · full-body · done · · moderate
1,4 · Glenstorm's three sons standing to attention with folders · centaur · scene · start · tracker-list · moderate
1,5 · Wimbleweather the giant, bashful, holding a tiny teacup · wimbleweather · full-body · hello · · moderate
2,1 · Wimbleweather having knocked over a filing cabinet, mortified · wimbleweather · full-body · oops · · moderate
2,2 · Wimbleweather weeping into a huge handkerchief, a mouse patting his boot · wimbleweather, mouse · scene · retrying · · subdued
2,3 · Wimbleweather typing on a laptop with one enormous finger · wimbleweather · full-body · start · technical · moderate
2,4 · Wimbleweather wedged in an office doorway · wimbleweather · full-body · blocked · · moderate
2,5 · Glozelle and Sopespian whispering behind a pillar · glozelle, sopespian · scene · start · meetings · subdued
3,1 · Sopespian peering through a keyhole · sopespian · full-body · start · research · moderate
3,2 · Glozelle polishing his medals, smug · glozelle · portrait · your-turn · · subdued
3,3 · Glozelle and Sopespian caught red-handed with a memo · glozelle, sopespian · scene · oops · · moderate
3,4 · Queen Prunaprismia at the head of the board table, unimpressed · prunaprismia · full-body · start · meetings · subdued
3,5 · Prunaprismia tapping a closed fan, waiting · prunaprismia · portrait · waiting · · subdued
4,1 · Caspian's Nurse telling a story by the fire · nurse · full-body · start · writing · subdued
4,2 · The Nurse handing Caspian a packed lunch and scarf · nurse, caspian · scene · start · travel · moderate
4,3 · The Nurse dozing over her knitting · nurse · full-body · waiting-long · · subdued
4,4 · Gwendolen in a stuffy training room, gazing out of the window · gwendolen · full-body · timed-out · · subdued
4,5 · Gwendolen climbing cheerfully out of the window · gwendolen · full-body · signing-off · · moderate · summer
5,1 · Gwendolen dancing with dryads in blossom · gwendolen, dryad · scene · big-win · · celebratory · spring
5,2 · Glenstorm galloping with a dispatch case · glenstorm · full-body · sent · · moderate
5,3 · Wimbleweather holding a ladder steady for Pattertwig · wimbleweather, pattertwig · scene · start · handoff · moderate
5,4 · Glenstorm under a cloudy night sky with no stars · glenstorm · full-body · not-found · · subdued
5,5 · Wimbleweather beaming with a gold star on his lapel · wimbleweather · portrait · done-small · · celebratory

## 61 · horse-and-his-boy-staff

Theme: Chervy the stag as Narnia's fastest courier, Arsheesh the stingy fisherman as payroll clerk, Dar and Darrin as King Lune's dutiful committee, and more of Bree's vanity.

1,1 · Chervy the stag skidding in with a message pouch · chervy · full-body · sent · · moderate
1,2 · Chervy panting beside a stopwatch · chervy · full-body · done · · moderate
1,3 · Chervy bounding over a hedge with a parcel · chervy · full-body · start · handoff · moderate
1,4 · Chervy waiting at a garden gate, ears up · chervy · full-body · waiting · · subdued
1,5 · Chervy with his antlers caught in a coat stand · chervy · full-body · tangled · · moderate
2,1 · Arsheesh the fisherman counting coins at a rickety desk · arsheesh · full-body · start · money · moderate
2,2 · Arsheesh grumbling over an empty net · arsheesh · full-body · not-found · · subdued
2,3 · Arsheesh refusing a request with a raised palm · arsheesh · portrait · blocked · · subdued
2,4 · Arsheesh dozing in his boat · arsheesh · full-body · waiting-long · · subdued · summer
2,5 · Arsheesh dropping his ledger in surprise · arsheesh · full-body · oops · · moderate
3,1 · Lord Dar and Lord Darrin bowing in unison · dar, darrin · scene · hello · · moderate
3,2 · Dar reading the morning dispatches to King Lune · dar, king-lune · scene · morning-brief · · moderate
3,3 · Darrin taking minutes with a fountain pen · darrin · full-body · start · tracker-add · moderate
3,4 · Dar and Darrin carrying a long table between them · dar, darrin · scene · start · general · moderate
3,5 · Dar and Darrin arguing over which way up a map goes · dar, darrin · scene · tangled · · moderate
4,1 · King Lune, Dar and Darrin raising mugs · king-lune, dar, darrin · scene · big-win · · celebratory
4,2 · Darrin checking a pocket watch at the castle gate · darrin · portrait · timed-out · · subdued
4,3 · Bree admiring his mane in a car's wing mirror · bree · full-body · start · design · moderate
4,4 · Bree posing on a video call · bree · full-body · start · meetings · moderate
4,5 · Hwin quietly finishing the work Bree is boasting about · hwin, bree · scene · done · · moderate
5,1 · Corin vaulting a stack of in-trays · corin · full-body · start · general · moderate
5,2 · Aravis typing a crisp reply · aravis · full-body · start · email · moderate
5,3 · Shasta asleep at his desk under a pile of maps · shasta · full-body · timed-out · · subdued
5,4 · Lasaraleen with a dozen shopping bags and a phone · lasaraleen · full-body · start · mobile · moderate
5,5 · Chervy and Pattertwig racing to deliver the same letter · chervy, pattertwig · scene · sent · · celebratory

## 62 · dawn-treader-crew-and-the-scrubbs

Theme: the ordinary crew (Rhince, Rynelf, and Pittencream who stayed behind), Eustace's earnest modern parents, and more of the friendly sea serpent.

1,1 · Rhince the first mate saluting · rhince · full-body · hello · · moderate
1,2 · Rhince reading a letter from home, wistful · rhince · portrait · waiting-long · · subdued
1,3 · Rynelf hauling a rope, singing · rynelf · full-body · start · technical · moderate
1,4 · Rynelf tangled in the rigging · rynelf · full-body · tangled · · moderate
1,5 · Rynelf coiling the rope neatly afterwards · rynelf · full-body · done-small · · moderate
2,1 · Pittencream sulking on the dock as the ship sails without him · pittencream · full-body · offline · · subdued
2,2 · Pittencream telling tall tales at a pub table · pittencream · full-body · your-turn · · moderate
2,3 · Pittencream running late with a suitcase · pittencream · full-body · timed-out · · moderate
2,4 · Harold and Alberta Scrubb doing exercises at an open window · harold-scrubb, alberta-scrubb · scene · morning-brief · · moderate
2,5 · Alberta Scrubb with a clipboard of house rules · alberta-scrubb · full-body · start · tracker-review · moderate
3,1 · Harold Scrubb setting off on a bicycle with a briefcase · harold-scrubb · full-body · start · travel · moderate
3,2 · The Scrubbs serving a very plain vegetable lunch · harold-scrubb, alberta-scrubb · scene · done-small · · subdued
3,3 · Alberta Scrubb shivering by an open window in the snow · alberta-scrubb · full-body · waiting · · subdued · winter
3,4 · Harold Scrubb lecturing at a lectern to an empty room · harold-scrubb · full-body · start · meetings · subdued
3,5 · The Scrubbs puzzling over a postcard from Eustace · harold-scrubb, alberta-scrubb · scene · your-turn · · moderate
4,1 · Eustace in a jumper showing his parents a tidy chart · eustace, harold-scrubb, alberta-scrubb · scene · big-win · · celebratory
4,2 · Rhince and Drinian at the chart table · rhince, drinian · scene · start · scheduling · moderate
4,3 · Rhince and Rynelf bailing a dinghy with teacups · rhince, rynelf · scene · retrying · · moderate
4,4 · Reepicheep inspecting the crew in a line · reepicheep, rynelf, rhince · scene · start · tracker-list · moderate
4,5 · The sea serpent offering a cup of tea over the rail · sea-serpent · full-body · hello · · moderate
5,1 · The sea serpent knitting with the tip of its tail · sea-serpent · full-body · start · focus · subdued · winter
5,2 · The sea serpent coiled round a server rack, holding cables · sea-serpent · full-body · start · technical · moderate
5,3 · The sea serpent asleep in coils on a beach · sea-serpent · full-body · waiting-long · · subdued · summer
5,4 · The sea serpent and Rynelf playing draughts · sea-serpent, rynelf · scene · your-turn · · moderate
5,5 · Rhince waving from a rowing boat at sunset · rhince · full-body · signing-off · · subdued

## 63 · experiment-house-and-harfang

Theme: the Head of Experiment House as a hopeless administrator (later an inspector, as in the book), and the King and Queen of Harfang as jolly, oversized hosts. Keep the giants warm and comic, nothing about cooking guests.

1,1 · The Head juggling a flurry of loose papers · the-head · full-body · tangled · · moderate
1,2 · The Head as a school inspector with a clipboard · the-head · full-body · start · tracker-review · moderate
1,3 · The Head trying to chair a very noisy meeting · the-head · full-body · start · meetings · moderate
1,4 · The Head peering into an empty filing cabinet · the-head · full-body · not-found · · subdued
1,5 · The Head beaming beside a blank new nameplate · the-head · portrait · big-win · · celebratory
2,1 · The Head chasing papers blown off the desk · the-head · full-body · oops · · moderate
2,2 · The Head at a typewriter with a mug of cocoa · the-head · full-body · start · writing · subdued
2,3 · Jill peeking out from a gym cupboard, playing hide and seek · jill · portrait · your-turn · · moderate
2,4 · Jill and Eustace slipping out of a classroom door · jill, eustace · scene · signing-off · · moderate
2,5 · A brass school bell beside an unanswered stack of post · · object · waiting · · subdued
3,1 · The King of Harfang, jolly, with an enormous teacup · harfang-king · full-body · hello · · celebratory
3,2 · The Queen of Harfang fussing over guest towels · harfang-queen · full-body · start · scheduling · moderate
3,3 · The King and Queen of Harfang at a giant dining table · harfang-king, harfang-queen · scene · start · meetings · moderate
3,4 · A giant's hot-water bottle on a giant armchair · · object · waiting-long · · subdued · winter
3,5 · Jill, Eustace and Puddleglum lost in a giant's hallway · jill, eustace, puddleglum · scene · not-found · · moderate
4,1 · Jill camped under a giant's napkin like a tent · jill · full-body · waiting · · subdued
4,2 · The King of Harfang laughing until he cries · harfang-king · portrait · done · · celebratory
4,3 · The Queen of Harfang dozing over knitting needles like poles · harfang-queen · full-body · waiting-long · · subdued
4,4 · A giant snowman at the castle gate · · environment · morning-brief · · subdued · winter
4,5 · Puddleglum on a ladder reading a giant's wall calendar · puddleglum · full-body · start · scheduling · moderate
5,1 · The giants' great hall lit for Christmas · · environment · big-win · · celebratory · christmas
5,2 · The King of Harfang sitting on the in-tray by accident · harfang-king · full-body · oops · · moderate
5,3 · Puddleglum with an umbrella in the castle doorway in snow · puddleglum · full-body · signing-off · · subdued · winter
5,4 · A tiny dispatch box on a giant's table · · object · sent · · moderate
5,5 · The Queen of Harfang waving a huge handkerchief from a tower · harfang-queen · full-body · done-small · · moderate

## 64 · last-battle-sentinels-and-schemers

Theme: Roonwit the centaur analyst whose warnings get ignored, Emeth the earnest new hire, and the small comic schemers Griffle, Wraggle, Slinkey and Ginger.

1,1 · Roonwit the centaur presenting a star chart, grave · roonwit · full-body · start · research · moderate
1,2 · Roonwit warning with a raised finger while a busy room ignores him · roonwit · scene · blocked · · moderate
1,3 · Roonwit galloping in with a report · roonwit · full-body · sent · · moderate
1,4 · Roonwit at a window at dawn · roonwit · full-body · morning-brief · · subdued
1,5 · Roonwit nodding, satisfied · roonwit · portrait · done-small · · moderate
2,1 · Emeth arriving with a box of desk things, eager · emeth · full-body · hello · · moderate
2,2 · Emeth at a crossroads of corridors, asking the way · emeth · full-body · your-turn · · moderate
2,3 · Emeth reading the staff handbook with total sincerity · emeth · full-body · start · research · subdued
2,4 · Emeth and Tirian shaking hands warmly · emeth, tirian · scene · big-win · · celebratory
2,5 · Emeth bowing politely to a vending machine · emeth · full-body · oops · · moderate
3,1 · Griffle the dwarf hugging the good stapler, refusing to share · griffle · full-body · blocked · · moderate
3,2 · Griffle sulking in a corner, arms folded · griffle · full-body · waiting · · subdued
3,3 · Griffle counting rations into tins · griffle · full-body · start · money · moderate
3,4 · Wraggle the satyr dancing on a desk, papers flying · wraggle · full-body · oops · · moderate
3,5 · Wraggle playing pipes in the break room · wraggle · full-body · done-small · · celebratory
4,1 · Slinkey the fox sweet-talking the receptionist · slinkey · full-body · start · email · moderate
4,2 · Slinkey with a too-good-to-be-true smile, offering a deal · slinkey · portrait · your-turn · · moderate
4,3 · Ginger and Slinkey plotting over a map, caught by Jewel · ginger, slinkey, jewel · scene · oops · · moderate
4,4 · Wraggle and Slinkey carrying a crate far too big for them · wraggle, slinkey · scene · start · handoff · moderate
4,5 · Ginger snooping through a filing cabinet by torchlight · ginger · full-body · start · research · moderate
5,1 · Ginger listening at a door with an ear trumpet · ginger · full-body · waiting · · subdued
5,2 · Ginger frozen in a desk lamp's spotlight · ginger · full-body · oops · · moderate
5,3 · Ginger with a magnifying glass on a trail that stops · ginger · full-body · not-found · · subdued
5,4 · Roonwit and Farsight comparing notes · roonwit, farsight · scene · start · meetings · moderate
5,5 · Emeth and Tirian sharing tea at sunset · emeth, tirian · scene · signing-off · · subdued

## 65 · the-witchs-household

Theme: the White Witch's office, entirely comic. Ginarrbrick the dwarf as her harried PA and driver, the thermostat war, Turkish Delight in the break room, Maugrim as a bumbling security guard.

1,1 · Ginarrbrick the dwarf in a fur hat, polishing sledge bells · ginarrbrick · full-body · hello · · moderate
1,2 · Ginarrbrick driving a reindeer sledge through snow · ginarrbrick · full-body · start · travel · moderate · winter
1,3 · Ginarrbrick buried behind a towering appointment book · ginarrbrick · full-body · start · scheduling · moderate
1,4 · Ginarrbrick hurrying with a tray of Turkish Delight · ginarrbrick · full-body · sent · · moderate
1,5 · Ginarrbrick and the sledge stuck in a snowdrift · ginarrbrick · full-body · blocked · · moderate · winter
2,1 · The White Witch turning the office thermostat right down · white-witch · full-body · start · technical · moderate · winter
2,2 · Tumnus and Mr Beaver in scarves and mittens at frosted desks · tumnus, mr-beaver · scene · waiting · · subdued · winter
2,3 · Tumnus sneaking the thermostat back up · tumnus · full-body · retrying · · moderate
2,4 · Edmund eyeing a box of Turkish Delight in the break room · edmund · portrait · your-turn · · moderate
2,5 · An empty Turkish Delight box with powdered-sugar crumbs · · object · not-found · · subdued
3,1 · The office water cooler frozen solid · · object · offline · · subdued · winter
3,2 · Maugrim as a gruff security guard checking passes · maugrim · full-body · blocked · · moderate
3,3 · Maugrim asleep in the guard's chair · maugrim · full-body · waiting-long · · subdued
3,4 · Maugrim holding a telephone receiver upside down, confused · maugrim · full-body · oops · · moderate
3,5 · The Witch dictating a letter to Ginarrbrick · white-witch, ginarrbrick · scene · start · writing · moderate
4,1 · The Witch reviewing a very long list with a quill · white-witch · full-body · start · tracker-review · subdued
4,2 · Icicles hanging off an overflowing in-tray · · object · timed-out · · subdued · winter
4,3 · The thaw dripping from the office ceiling into buckets · · environment · retrying · · moderate · spring
4,4 · Father Christmas striding into the Witch's office with presents · father-christmas · full-body · big-win · · celebratory · christmas
4,5 · Ginarrbrick wound up in the reindeer's reins · ginarrbrick · full-body · tangled · · moderate
5,1 · The Witch's sledge with a blank parking ticket on it · · object · oops · · moderate
5,2 · Ginarrbrick yawning at the end of a long winter · ginarrbrick · full-body · signing-off · · subdued · winter
5,3 · The Witch glaring at a cheerful robin on her windowsill · white-witch, robin · scene · oops · · moderate
5,4 · The Witch tapping a calendar that never reaches Christmas · white-witch · full-body · waiting · · subdued · winter
5,5 · A snow globe of the Witch's castle on a desk · · object · done-small · · subdued · winter

## 66 · the-1940s-office

Theme: the Professor's house as a busy 1940s office. Familiar cast with period kit: switchboard, typing pool, tea trolley, pneumatic tubes, wireless, carbon paper, blackout curtains.

1,1 · Mrs Macready at a switchboard, headset on, plugging cords · mrs-macready · full-body · start · email · moderate
1,2 · Professor Kirke dictating to Lucy at a typewriter · professor-kirke, lucy · scene · start · writing · moderate
1,3 · The typing pool: Lucy, Susan and Polly at typewriters · lucy, susan, polly · scene · start · focus · moderate
1,4 · Tumnus wheeling a tea trolley · tumnus · full-body · done-small · · moderate
1,5 · Mrs Beaver presenting a cake on the tea trolley · mrs-beaver · full-body · big-win · · celebratory
2,1 · A message capsule whooshing up a pneumatic tube · · object · sent · · moderate
2,2 · Trumpkin catching a pneumatic capsule on the nose · trumpkin · full-body · oops · · moderate
2,3 · Peter tuning a wireless set for the morning news · peter · full-body · morning-brief · · moderate
2,4 · Edmund with carbon paper smudged all over his hands · edmund · full-body · tangled · · moderate
2,5 · Susan filing index cards into a long drawer · susan · full-body · start · tracker-add · moderate
3,1 · Trufflehunter with a rubber stamp and a stack of forms · trufflehunter · full-body · start · tracker-review · subdued
3,2 · Doctor Cornelius searching a huge card catalogue · doctor-cornelius · full-body · start · research · subdued
3,3 · Puddleglum tapping the barometer in the corridor · puddleglum · full-body · waiting · · subdued
3,4 · Reepicheep facing down a jammed typewriter, sword raised · reepicheep · full-body · blocked · · moderate
3,5 · A Bakelite telephone ringing on an empty desk · · object · your-turn · · moderate
4,1 · A blank ration book and coupons on a desk · · object · start · money · subdued
4,2 · Mr Beaver fixing a rattling radiator with a spanner · mr-beaver · full-body · start · technical · moderate · winter
4,3 · Blackout curtains drawn, one desk lamp glowing · · environment · signing-off · · subdued
4,4 · Tumnus with umbrella and parcels at a red pillar box · tumnus · full-body · sent · · moderate
4,5 · Eustace running for a double-decker bus as it pulls away · eustace · full-body · timed-out · · moderate
5,1 · Lucy in a mackintosh at a bus stop in the rain · lucy · full-body · waiting · · subdued · autumn
5,2 · Caspian studying a corkboard map strung with thread · caspian · full-body · start · scheduling · moderate
5,3 · The Pevensies round the wireless, cheering · peter, susan, edmund, lucy · scene · big-win · · celebratory
5,4 · Glimfeather as night watchman with a lantern · glimfeather · full-body · waiting-long · · subdued
5,5 · Coats and hats on a coat stand at dusk · · object · signing-off · · subdued

## 67 · specialists-at-work

Theme: the specialty jokes, mixed era. Character-driven humour first, generic poses never.

1,1 · Reepicheep and four mice carrying a laptop like a sedan chair · reepicheep, mouse · scene · start · handoff · moderate
1,2 · A chain of mice passing envelopes along a desk · mouse · scene · sent · · moderate
1,3 · Mice all hauling on one stuck drawer · mouse · scene · retrying · · moderate
1,4 · Mice cheering on top of a finished stack of reports · mouse · scene · big-win · · celebratory
1,5 · Trufflehunter patiently untangling a ball of red tape · trufflehunter · full-body · tangled · · subdued
2,1 · Trufflehunter approving forms one at a time, unhurried · trufflehunter · full-body · start · tracker-now · subdued
2,2 · Pattertwig zipping between desks on a wheeled chair · pattertwig · full-body · sent · · moderate
2,3 · Pattertwig juggling three phones at once · pattertwig · full-body · start · mobile · moderate
2,4 · Ginger in dark glasses reading someone else's post · ginger · full-body · start · email · moderate
2,5 · Ginger hiding inside a filing cabinet drawer · ginger · full-body · waiting · · subdued
3,1 · Puddleglum presenting a gloomy rain chart to a meeting · puddleglum · full-body · start · meetings · subdued
3,2 · Puddleglum holding an umbrella over a server rack · puddleglum · full-body · start · technical · subdued
3,3 · Puddleglum, mildly astonished that it worked · puddleglum · portrait · done · · moderate
3,4 · Reepicheep fencing a jammed printer · reepicheep · full-body · blocked · · moderate
3,5 · Reepicheep bowing to the printer once it works · reepicheep · full-body · done-small · · moderate
4,1 · Bree preening in a laptop camera before a call · bree · full-body · start · design · moderate
4,2 · Mr Beaver patching a server rack with logs and mud · mr-beaver · full-body · start · technical · moderate
4,3 · Mrs Beaver packing everything, sewing machine included, into a laptop bag · mrs-beaver · full-body · start · travel · moderate
4,4 · Eustace writing a grumpy diary entry about the meeting · eustace · full-body · start · writing · subdued
4,5 · Eustace as a small dragon warming a chilly server room · eustace · full-body · start · technical · moderate · winter
5,1 · The sea serpent untangling the whole office's cables at once · sea-serpent · full-body · done · · moderate
5,2 · The sea serpent holding up a sagging projector screen · sea-serpent · full-body · start · meetings · moderate
5,3 · Father Christmas as IT, handing out new laptops · father-christmas · full-body · start · handoff · celebratory · christmas
5,4 · Glimfeather on the night shift among glowing monitors · glimfeather · full-body · start · technical · subdued
5,5 · Tumnus and the mice sharing cake after a launch · tumnus, mouse · scene · big-win · · celebratory

## 68 · old-tool-new-tool

Theme: 1940s and modern side by side in the same cell. Half characters, half objects.

1,1 · Lucy on a call with a switchboard headset over wireless earbuds · lucy · full-body · start · meetings · moderate
1,2 · Mr Beaver with a typewriter and a laptop side by side · mr-beaver · full-body · start · writing · moderate
1,3 · Mrs Macready holding a pneumatic capsule and a phone, choosing · mrs-macready · full-body · your-turn · · moderate
1,4 · Pattertwig carrying a memory stick like a log · pattertwig · full-body · sent · · moderate
1,5 · Professor Kirke reading the morning paper on a tablet · professor-kirke · full-body · morning-brief · · subdued
2,1 · Tumnus winding a gramophone at a standing desk · tumnus · full-body · start · focus · moderate
2,2 · Puddleglum comparing a barometer with a weather app · puddleglum · full-body · start · research · subdued
2,3 · Caspian with a paper map in one hand and a phone in the other · caspian · full-body · start · travel · moderate
2,4 · Trumpkin fixing a modern printer with an old spanner · trumpkin · full-body · retrying · · moderate
2,5 · Susan comparing her wristwatch with a smartwatch · susan · portrait · timed-out · · subdued
3,1 · Edmund photographing a ledger page with his phone · edmund · full-body · start · tracker-add · moderate
3,2 · Trufflehunter typing a spreadsheet with one claw, ledger beside him · trufflehunter · full-body · start · money · subdued
3,3 · Bree taking a selfie in a gilt-framed mirror · bree · full-body · start · design · moderate
3,4 · Glimfeather flying off with a laptop by its strap · glimfeather · full-body · start · handoff · moderate
3,5 · Peter speaking into an old ribbon microphone on a video call · peter · full-body · start · meetings · moderate
4,1 · A rotary telephone and a smartphone, both ringing · · object · your-turn · · moderate
4,2 · A laptop balanced on top of a typewriter · · object · start · writing · moderate
4,3 · A wooden filing cabinet with a server rack inside · · object · start · technical · moderate
4,4 · A pneumatic tube delivering a phone · · object · sent · · moderate
4,5 · A brown teapot plugged into a charging cable · · object · done-small · · moderate
5,1 · A wireless set and a smart speaker facing each other · · object · morning-brief · · subdued
5,2 · An inkwell spilled across a keyboard · · object · oops · · moderate
5,3 · Old telephone cords knotted with new chargers · · object · tangled · · moderate
5,4 · A burnt-out light bulb beside a dark laptop · · object · offline · · subdued
5,5 · A quill and a stylus side by side in a pen pot · · object · done · · subdued

---

## What this adds

- 23 new characters across all seven books, mostly second-tier figures with built-in jokes.
- Two sheets (66 and 68) that set the 1940s look for the existing cast, and one (67) built purely on the specialty gags.
- Tumnus appears in only a handful of cells, so his share keeps falling.
- Before generating, check `reports/coverage.md` and swap cells towards any moment still thin.
