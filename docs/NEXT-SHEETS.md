# Next sheets: closing the Narnia book gaps

**Historical brief.** Sheets 44 to 51 were made from this plan and delivered on 2026-10-16 alongside sheets 52 to 58. The delivered sheet JSONs in `jbsprites-art/narnia/originals/` are the authority. Several cells changed in delivery: no Dufflepuds, no lion costume on 51, and Jewel was kept separate from `unicorn`.

Eight sheets, 44 to 51, 25 cells each. Each one fills a gap against the books and also targets the thin rows in `reports/coverage.md` (offline, timed-out, not-found, sent, handoff, the tracker starts, the seasons, and guests in endings).

Paste the Prompt from `docs/SHEET-BRIEF.md` once for each sheet. Set the theme line to the sheet's theme and the cells line to its cell list below. Attach two existing sheets as style references, and for later sheets attach one that already shows the same characters.

House rules carried over from the existing sheets:

- Children from the books are drawn as adults in business casual, as Jill already is.
- Nothing violent or frightening. Villains are stern or comic, never menacing. There is no Tash, no battle scenes, and no Stone Table death.
- No words anywhere, so seals, signs and forms stay blank.

## New character names for `scripts/vocab.py`

Add these when each sheet is accepted (37 in all):

| Book | New names |
|---|---|
| Magician's Nephew | `digory`, `polly`, `fledge`, `frank` (Helen appears beside him, tagged as `frank`) |
| Last Battle | `tirian`, `jewel`, `puzzle`, `shift`, `poggin`, `farsight` |
| Horse and His Boy | `shasta`, `aravis`, `corin`, `lasaraleen`, `rabadash`, `king-lune`, `hermit` |
| Dawn Treader | `drinian`, `coriakin`, `dufflepud`, `gumpas`, `ramandu`, `ramandus-daughter`, `sea-serpent` |
| Silver Chair | `rilian`, `green-lady`, `golg` (every Earthman is Golg, as every wolf is Maugrim), `father-time` |
| Prince Caspian | `trufflehunter`, `nikabrik`, `pattertwig`, `miraz`, `bulgy-bear` |
| Lion, Witch & Wardrobe | `professor-kirke`, `mrs-macready`, `rumblebuffin` |

Open question: should `jewel` absorb the existing `unicorn` tag ("every unicorn is Jewel")? It would make the one generic unicorn count towards The Last Battle.

Jadis in Charn is tagged `white-witch`, since she is the same character.

Cell format below: **row,col** · description · characters · view · moments · activity (start only) · energy · season.

---

## 44 · magicians-nephew-at-work

Theme: Digory, Polly, the rings, Charn, Fledge and the first king and queen, as office life. New characters, so cell 1,1 and cell 1,2 set their look.

1,1 · Digory, tousled hair, shirt and tie, waving · digory · full-body · hello · · moderate
1,2 · Polly, neat bob, cardigan, holding a notebook · polly · full-body · start · writing · moderate
1,3 · Digory and Polly shaking hands over a garden wall · digory, polly · scene · hello · · moderate
1,4 · Polly crawling through an attic tunnel with a lantern · polly · full-body · start · research · moderate
1,5 · Digory turning a yellow ring over in his fingers, thinking · digory · portrait · your-turn · · subdued
2,1 · Polly slipping on a green ring to pass the job along · polly · hands · start · handoff · moderate
2,2 · Digory and Polly jumping hand in hand into a pool · digory, polly · scene · start, sent · handoff · moderate
2,3 · Digory dozing at the edge of a quiet woodland pool · digory · full-body · timed-out, waiting-long · · subdued
2,4 · Digory, hand hovering over a small golden bell and hammer · digory · full-body · your-turn · · subdued
2,5 · Digory wincing as the bell rings · digory · full-body · oops · · moderate
3,1 · Polly holding Digory back by the sleeve · digory, polly · scene · blocked · · moderate
3,2 · Jadis, tall queen of Charn, at a grand stone desk · white-witch · full-body · start · meetings · moderate
3,3 · Jadis scowling at a bent lamppost crossbar in her hand · white-witch · full-body · oops · · moderate
3,4 · Uncle Andrew stuck upside down in a sapling, flustered · uncle-andrew · full-body · tangled · · moderate
3,5 · Frank the cabby in a bowler hat beside his horse · frank · scene · start · travel · moderate
4,1 · Frank, newly crowned, reading petitions at a plain desk · frank · full-body · start · tracker-review · subdued
4,2 · Frank and Helen crowned side by side, waving · frank · scene · big-win · · celebratory
4,3 · Fledge, the winged horse, spreading new wings · fledge · full-body · big-win · · celebratory
4,4 · Fledge flying with Digory and Polly on his back · fledge, digory, polly · scene · start · travel · moderate
4,5 · Fledge grazing beside an empty bench · fledge · full-body · waiting-long · · subdued
5,1 · Digory carrying a silver apple carefully in both hands · digory · full-body · sent · · subdued
5,2 · Digory planting a seedling in fresh soil · digory · full-body · done · · moderate · spring
5,3 · Polly adding small potted saplings to a tidy shelf · polly · full-body · start · tracker-add · moderate
5,4 · Digory searching an empty attic cupboard by candlelight · digory · full-body · not-found · · subdued
5,5 · Polly, thumbs up beside a tray of rings · polly · portrait · done-small · · moderate

## 45 · last-battle-colleagues

Theme: Tirian, Jewel, Puzzle, Shift, Poggin and Farsight. Puzzle and Shift play the impostor and the con man, which suits security moments. Keep them comic, never sinister.

1,1 · Tirian, hand on Jewel the unicorn's neck, greeting · tirian, jewel · scene · hello · · moderate
1,2 · Tirian at an oak table reading morning dispatches · tirian · full-body · morning-brief · · moderate
1,3 · Jewel trotting with a message pouch · jewel · full-body · sent · · moderate
1,4 · Jewel lying down, head on hooves, patient · jewel · full-body · waiting-long · · subdued
1,5 · Puzzle the donkey in a badly fitting lion-skin costume · puzzle · full-body · oops · · moderate
2,1 · Puzzle shrugging off the lion skin, relieved · puzzle · full-body · done-small · · subdued
2,2 · Shift the ape in an oversized coat offering a sealed envelope · shift · full-body · blocked · · moderate
2,3 · Shift counting nuts into an oversized ledger · shift · full-body · start · money · moderate
2,4 · Puzzle holding a dandelion, asking timidly · puzzle · portrait · your-turn · · subdued
2,5 · Poggin the dwarf arriving with a lantern, cheerful · poggin · full-body · hello · · moderate
3,1 · Poggin carrying a tray of mugs for the team · poggin · full-body · done-small · · moderate
3,2 · Farsight the eagle on a lectern beside a telescope · farsight · full-body · morning-brief · · moderate
3,3 · Farsight scanning an empty horizon · farsight · full-body · not-found · · subdued
3,4 · Tirian on night watch with a lantern · tirian · full-body · waiting · · subdued
3,5 · Tirian, Eustace and Jill around a map table · tirian, eustace, jill · scene · start · meetings · moderate
4,1 · Jill in a green hood slipping through brush with a notebook · jill · full-body · start · research · moderate
4,2 · Eustace sorting letters with a sword-shaped opener · eustace · full-body · start · email · moderate
4,3 · A closed stable door with a lantern hanging beside it · · object · blocked · · subdued
4,4 · The stable door open onto warm sunlight · · object · done · · moderate
4,5 · Tirian closing a book at sunset · tirian · portrait · signing-off · · subdued
5,1 · Jewel and Tirian racing up a green hill · tirian, jewel · scene · big-win · · celebratory
5,2 · Puzzle asleep on his feet beside an hourglass · puzzle · full-body · timed-out · · subdued
5,3 · Jewel's horn with a small cable wound around it · jewel · portrait · tangled · · moderate
5,4 · A huddle of dwarfs, arms folded, refusing · dwarf · scene · blocked · · subdued
5,5 · Tirian handing a sealed scroll to Farsight · tirian, farsight · scene · start · handoff · moderate

## 46 · horse-and-his-boy-colleagues

Theme: the riders Bree and Hwin have been missing (Shasta and Aravis), with Corin, King Lune, Lasaraleen, the Hermit and Rabadash as a donkey.

1,1 · Shasta on Bree, waving · shasta, bree · scene · hello · · moderate
1,2 · Aravis riding Hwin, composed and upright · aravis, hwin · scene · start · travel · moderate
1,3 · Shasta with a satchel at a fork in the road · shasta · full-body · your-turn · · subdued
1,4 · Shasta fishing from a small boat · shasta · full-body · start · focus · subdued · summer
1,5 · Aravis writing a letter, perfect posture · aravis · full-body · start · writing · moderate
2,1 · Aravis and Lasaraleen whispering over tea · aravis, lasaraleen · scene · start · meetings · moderate
2,2 · Lasaraleen buried in shopping parcels · lasaraleen · full-body · tangled · · moderate
2,3 · Rabadash turned into a donkey, still wearing his crown, aghast · rabadash · full-body · oops · · moderate
2,4 · Rabadash the donkey refusing to budge · rabadash · full-body · blocked · · subdued
2,5 · Corin vaulting a fence, grinning · corin · full-body · start · general · moderate
3,1 · Shasta and Corin, identical twins, comparing notebooks · shasta, corin · scene · start · tracker-review · moderate
3,2 · King Lune, stout and beaming, arms wide · king-lune · full-body · big-win · · celebratory
3,3 · King Lune carving at a harvest table · king-lune · full-body · done · · moderate · thanksgiving
3,4 · The Hermit looking into his still pool · hermit · full-body · start · research · subdued
3,5 · The Hermit tending goats, calm · hermit · full-body · waiting-long · · subdued
4,1 · Shasta lost in fog on a mountain pass · shasta · full-body · not-found · · subdued
4,2 · Shasta running with an urgent message · shasta · full-body · sent · · moderate
4,3 · Bree rolling on his back in the grass, relieved · bree · full-body · done · · moderate · summer
4,4 · Aravis and Hwin sharing a quiet moment at dusk · aravis, hwin · scene · signing-off · · subdued
4,5 · Miniature of domed Tashbaan on a desk · · object · start · travel · moderate
5,1 · Shasta asleep against a large, warm cat · shasta, aslan · scene · waiting-long · · subdued
5,2 · Shasta and Aravis at a shared desk, both working · shasta, aravis · scene · done · · moderate
5,3 · The Tisroc's cushioned divan · · object · start · meetings · subdued
5,4 · Bree admiring his reflection in a mirror · bree · full-body · start · design · moderate
5,5 · Corin waving from a palace balcony among falling leaves · corin · full-body · hello · · moderate · autumn

## 47 · dawn-treader-crew

Theme: the voyage's colleagues. Drinian, Gumpas the paperwork governor, Coriakin and the Dufflepuds, Ramandu and his daughter, and a small, friendly sea serpent.

1,1 · Drinian at the ship's wheel with a compass · drinian · full-body · start · travel · moderate
1,2 · Drinian writing in the ship's log · drinian · full-body · start · tracker-add · moderate
1,3 · Gumpas behind towering stacks of paperwork · gumpas · full-body · tangled · · moderate
1,4 · Gumpas holding up a blank form, insisting · gumpas · full-body · blocked · · moderate
1,5 · Caspian clearing Gumpas's desk in one sweep · caspian · full-body · done · · moderate
2,1 · A Dufflepud hopping happily on his one big foot · dufflepud · full-body · start · general · moderate
2,2 · Two Dufflepuds nodding in loud agreement · dufflepud · scene · done-small · · moderate
2,3 · A Dufflepud lying back with his foot up as a sunshade · dufflepud · full-body · waiting · · subdued · summer
2,4 · Coriakin turning pages at a lectern · coriakin · full-body · start · research · subdued
2,5 · Coriakin puzzling over a blank page · coriakin · portrait · not-found · · subdued
3,1 · Lucy reading the magician's book by candlelight · lucy · full-body · start · focus · subdued
3,2 · Ramandu holding a glowing berry at dawn · ramandu · full-body · morning-brief · · subdued
3,3 · Ramandu's daughter carrying a lamp, welcoming · ramandus-daughter · full-body · hello · · moderate
3,4 · Aslan's table laid for a feast · · object · done · · moderate · thanksgiving
3,5 · A small friendly sea serpent tangled in ship's rope · sea-serpent · full-body · tangled · · moderate
4,1 · The Dawn Treader under full sail · · object · sent · · moderate
4,2 · Reepicheep paddling a coracle among white lilies · reepicheep · full-body · signing-off · · subdued
4,3 · Edmund and Lucy studying a star chart · edmund, lucy · scene · start · scheduling · moderate
4,4 · Eustace scribbling grumpily in his diary · eustace · full-body · start · writing · subdued
4,5 · A becalmed ship with slack sails · · object · offline · · subdued
5,1 · Drinian waiting out a storm beside an hourglass · drinian · full-body · waiting · · subdued
5,2 · A Lone Islands wharf piled with crates · · environment · start · travel · moderate
5,3 · Coriakin and Lucy laughing over teacups · coriakin, lucy · scene · done · · moderate
5,4 · Caspian handing the helm to Drinian · caspian, drinian · scene · start · handoff · moderate
5,5 · Caspian and Ramandu's daughter greeting the sunrise · caspian, ramandus-daughter · scene · big-win · · celebratory · new-year

## 48 · silver-chair-colleagues

Theme: Rilian, the Lady of the Green Kirtle (stern and glamorous, never a serpent), Golg and the Earthmen, and Father Time, with Jill, Eustace and Puddleglum.

1,1 · Prince Rilian bowing politely in a dark suit · rilian · full-body · hello · · moderate
1,2 · Rilian stepping free of a silver chair, relieved · rilian · full-body · big-win · · celebratory
1,3 · Rilian searching the horizon for his father's ship · rilian · full-body · not-found · · subdued
1,4 · The Lady of the Green Kirtle offering a tempting green button · green-lady · full-body · blocked · · moderate
1,5 · Puddleglum stamping out a smoky hearth fire · puddleglum · full-body · retrying · · moderate
2,1 · Golg the gnome leaping for joy with a lantern · golg · full-body · big-win · · celebratory
2,2 · Earthmen in single file, each with a lantern · golg · scene · start · tracker-list · subdued
2,3 · An Underland lamp gone out · · object · offline · · subdued
2,4 · Father Time, a huge giant, asleep · father-time · full-body · waiting-long · · subdued
2,5 · Father Time waking and stretching · father-time · full-body · morning-brief · · moderate
3,1 · Jill, Eustace and Puddleglum untangling a long rope · jill, eustace, puddleglum · scene · tangled · · moderate
3,2 · Jill whistling for a messenger owl · jill · full-body · start · email · moderate
3,3 · Glimfeather carrying Jill by night · glimfeather, jill · scene · start · travel · moderate
3,4 · Puddleglum gloomily tapping a barometer · puddleglum · full-body · morning-brief · · subdued
3,5 · Snowy steps of a ruined giant city · · environment · waiting · · subdued · winter
4,1 · The silver chair standing empty · · object · done · · subdued
4,2 · Jill and Eustace slipping through a door in a stone wall · jill, eustace · scene · start · handoff · moderate
4,3 · Old Trumpkin cupping his ear, waiting for an answer · trumpkin · portrait · your-turn · · subdued
4,4 · Rilian, crowned, going through a ledger · rilian · full-body · start · tracker-review · subdued
4,5 · Jill and Puddleglum sharing a flask of tea at night · jill, puddleglum · scene · signing-off · · subdued
5,1 · Puddleglum fishing on a misty autumn marsh · puddleglum · full-body · waiting · · subdued · autumn
5,2 · Earthmen dancing with lanterns · golg · scene · big-win · · celebratory · new-year
5,3 · A parliament of owls meeting in a tower · owl, glimfeather · scene · start · meetings · moderate
5,4 · Jill sliding down a long chute, surprised · jill · full-body · oops · · moderate
5,5 · Puddleglum with a bandaged foot, smiling anyway · puddleglum · full-body · done-small · · subdued

## 49 · prince-caspian-colleagues

Theme: the Old Narnians Caspian's sheets have been missing: Trufflehunter, Nikabrik, Pattertwig, the Bulgy Bears, and Miraz kept comic.

1,1 · Trufflehunter the badger, kind, by a hearth · trufflehunter · full-body · hello · · subdued
1,2 · Trufflehunter writing names into a ledger · trufflehunter · full-body · start · tracker-add · moderate
1,3 · Trufflehunter dozing in an armchair · trufflehunter · full-body · waiting-long · · subdued
1,4 · Nikabrik the dwarf grumbling, arms folded · nikabrik · full-body · blocked · · subdued
1,5 · Nikabrik squinting suspiciously at a document · nikabrik · portrait · start · tracker-review · moderate
2,1 · Pattertwig the squirrel dashing off with a message · pattertwig · full-body · sent · · moderate
2,2 · Pattertwig chattering into a phone on a branch · pattertwig · full-body · start · mobile · moderate
2,3 · Pattertwig sorting acorns into jars · pattertwig · full-body · start · money · moderate · autumn
2,4 · King Miraz drumming his fingers, out of patience · miraz · portrait · timed-out · · subdued
2,5 · Three Bulgy Bears asleep in a heap · bulgy-bear · scene · offline · · subdued
3,1 · A Bulgy Bear sucking his paw, thinking · bulgy-bear · portrait · your-turn · · subdued
3,2 · Dryads dancing among blossoming trees · dryad · scene · hello · · moderate · spring
3,3 · Aslan's How, a grassy mound with a stone door · · environment · start · focus · subdued
3,4 · Caspian blowing Susan's horn · caspian · full-body · sent · · moderate
3,5 · Lucy pointing while the others shrug, seeing nothing · lucy, peter, susan, edmund · scene · not-found · · moderate
4,1 · Edmund lighting a pocket lamp in old ruins · edmund · full-body · start · research · moderate
4,2 · Peter writing a formal letter · peter · full-body · start · writing · moderate
4,3 · Peter and Caspian shaking hands · peter, caspian · scene · done · · moderate
4,4 · Ruined Cair Paravel among apple trees · · environment · signing-off · · subdued · summer
4,5 · The Pevensies on a station bench as their luggage lifts away · lucy, peter, susan, edmund · scene · start · travel · moderate
5,1 · Reepicheep admiring his restored tail · reepicheep · full-body · big-win · · celebratory
5,2 · Pattertwig and Trufflehunter planning over a map · pattertwig, trufflehunter · scene · start · meetings · moderate
5,3 · Trufflehunter offering a warm loaf · trufflehunter · full-body · done-small · · moderate · thanksgiving
5,4 · Cornelius showing Caspian the stars from a tower · doctor-cornelius, caspian · scene · start · research · subdued
5,5 · A crown on a cushion, ready · · object · big-win · · moderate

## 50 · wardrobe-gaps-and-endings

Theme: the Lion, the Witch and the Wardrobe characters still missing (Professor Kirke, Mrs Macready, Giant Rumblebuffin), plus endings for the thinly covered Lucy, Edmund and Susan.

1,1 · Professor Kirke, bushy beard, gesturing to make a point · professor-kirke · full-body · your-turn · · moderate
1,2 · Professor Kirke at a study desk heaped with books · professor-kirke · full-body · start · research · subdued
1,3 · Mrs Macready, keys in hand, barring a door · mrs-macready · full-body · blocked · · moderate
1,4 · Mrs Macready checking her watch, keys jangling · mrs-macready · full-body · waiting · · moderate
1,5 · Giant Rumblebuffin handing a big parcel down to Lucy · rumblebuffin, lucy · scene · start · handoff · moderate
2,1 · Rumblebuffin mopping his brow with a huge handkerchief · rumblebuffin · full-body · done · · moderate
2,2 · Lucy peeking out between the coats in the wardrobe · lucy · portrait · hello · · moderate
2,3 · Lucy knocking on the wardrobe's plain wooden back · lucy · full-body · not-found · · subdued
2,4 · Lucy giving a drop of cordial to a tired colleague · lucy · full-body · retrying · · subdued
2,5 · Edmund, hat in hand, apologising · edmund · full-body · oops · · subdued
3,1 · Edmund at a frosted desk with a dark screen · edmund · full-body · offline · · subdued · winter
3,2 · Edmund being knighted, sword on his shoulder · edmund, peter · scene · big-win · · celebratory
3,3 · Susan checking her wristwatch, sensible · susan · portrait · timed-out · · subdued
3,4 · Susan aiming her bow at a target, focused · susan · full-body · start · focus · moderate
3,5 · Susan in a raincoat with an umbrella · susan · full-body · waiting · · subdued · autumn
4,1 · Peter waving from a train carriage window · peter · portrait · signing-off · · subdued
4,2 · The four Pevensies playing hide and seek in the spare room · lucy, peter, susan, edmund · scene · hello · · moderate
4,3 · The Pevensies tumbling out of the wardrobe · lucy, peter, susan, edmund · scene · done · · moderate
4,4 · Lucy and Susan riding on Aslan's back · lucy, susan, aslan · scene · big-win · · celebratory
4,5 · Dripping icicles and crocuses in the thaw · · environment · morning-brief · · subdued · spring
5,1 · A picnic blanket in a summer meadow · · environment · signing-off · · subdued · summer
5,2 · Mr Beaver patching a leak in the dam · mr-beaver · full-body · retrying · · moderate
5,3 · Mrs Beaver insisting on packing her sewing machine · mrs-beaver · full-body · timed-out · · moderate
5,4 · A sledge stuck in melting slush · · object · blocked · · subdued · spring
5,5 · Lucy waving goodbye beside the lamppost · lucy · full-body · signing-off · · subdued · winter

## 51 · later-books-objects-and-places

Theme: no characters. Props and places from the later books, aimed at the object rows the picker is short of (offline, sent, tracker-add, seasons).

1,1 · The Wood between the Worlds: quiet pools among trees · · environment · waiting-long · · subdued
1,2 · A golden bell and small hammer on a pillar · · object · your-turn · · subdued
1,3 · Yellow and green rings in two trays · · object · start · handoff · moderate
1,4 · A silver apple on a velvet cushion · · object · done · · subdued
1,5 · A young lamppost sprouting from the ground · · object · start · general · subdued · spring
2,1 · A closed stable door with a lantern · · object · blocked · · subdued
2,2 · A crumpled lion-skin costume on a chair · · object · oops · · subdued
2,3 · Miniature domes of Tashbaan · · environment · start · travel · moderate
2,4 · The Hermit's still pool · · environment · start · research · subdued
2,5 · A mountain pass lost in fog · · environment · not-found · · subdued
3,1 · A ship's log and quill on a chart table · · object · start · writing · moderate
3,2 · A sea of white lilies at the world's end · · environment · signing-off · · subdued · summer
3,3 · Ramandu's long table laid for a feast · · object · done · · moderate · thanksgiving
3,4 · A magician's book glowing on a lectern · · object · start · research · subdued
3,5 · A mountain of paperwork tied with string · · object · tangled · · moderate
4,1 · A burnt-out Underland lantern · · object · offline · · subdued
4,2 · A broken silver chair · · object · done-small · · subdued
4,3 · A wigwam on the marsh with a thread of smoke · · environment · waiting · · subdued · autumn
4,4 · The stone door of Aslan's How · · object · start · focus · subdued
4,5 · A ruined arch with an apple tree in autumn colour · · environment · signing-off · · subdued · autumn
5,1 · Snow on the giant steps of Harfang · · environment · timed-out · · subdued · winter
5,2 · Lanterns strung between trees for a feast · · environment · big-win · · celebratory · new-year
5,3 · A lion-crested hourglass half run through · · object · start · tracker-now · moderate
5,4 · A sealed scroll in a leather message tube · · object · sent · · moderate
5,5 · New notebooks tied with green ribbon · · object · start · tracker-add · moderate

---

## What this adds against coverage.md

Approximate counts across the 200 cells:

| Row | Now | Added |
|---|---|---|
| offline | 3 | +6 |
| timed-out | 5 | +6 |
| not-found | 9 | +8 |
| sent | 8 | +8 |
| start: handoff | 6 | +7 |
| start: tracker-add | 5 | +5 |
| start: tracker-review | 6 | +4 |
| summer / autumn / spring | 2 / 3 / 5 | +6 / +7 / +5 |
| thanksgiving / new-year | 3 / 3 | +4 / +3 |
| big-win | 11 | +12, nearly all guests |

Tumnus appears in none of the new cells, so his share falls from 42% to about 34%.
