# Legend of Corn — Cast Design Notes

Date: 2026-11-18
Project: Legend of Corn
Status: draft framework — via Michael 2026-11-18 (from his Google (Gemini) session), research running
Summary: The 5 pillars of classic Zelda character design + the 5 cast questions to answer before sprites are designed. Companion to CASTLE-OPENING-PLAN.md. No plot details — design craft only, per Michael's no-spoilers rule for this chat.

---

## The 5 pillars (framework)

1. **Silhouette & 3-color readability.** NES/SNES sprites allow only 3–4
   colors per sprite (plus transparency), so characters cannot rely on
   facial detail. Every main character needs one defining physical prop or
   shape (Link's pointed cap and shield, Zelda's crown and gown, Impa's
   cloak, Malon's kerchief, an Old Man's staff and beard). Test: turn the
   sprite into a solid black silhouette — you should still know who it is.
2. **Color-coded moral & elemental alignment.** Factions get distinct
   color families so allegiance reads in half a second:
   - Heroes / valley folk: warm golds, greens, earthy browns, sky blues.
   - Royalty / keepers: purples, crimsons, whites, gold trim.
   - Storm / blight / villains: sickly violets, charcoal blacks, storm
     grays, harsh magenta / acid-green accents.
3. **The single-trait NPC rule.** Townsfolk and feast guests get 2–3 short
   dialogue boxes. Great Zelda NPCs (Error, Talon, Dampé, the Cucco Lady)
   have one vivid obsession, posture, or verbal tic rather than long
   backstories.
4. **Functional cast roles — no redundant characters.** Every recurring
   character serves a clear mechanical or emotional anchor:
   1. The Silent Vessel (hero) — blank-slate so the player projects.
   2. The Moral Anchor (princess/maiden) — what is worth protecting; not
      passive, defined by one decisive act of courage.
   3. The Witness / Chronicler (elder) — bridges past and present; carries
      the emotional weight of history.
   4. The Mentor / Craft-Teacher — gives the first tool, teaches one core
      verb.
   5. The Foil / Antagonist — mirrors the hero's theme in reverse
      (blight/storm vs harvest/growth).
5. **Distinct dialogue cadence.** No voice acting needed: sentence lengths
   differ — a hurried farmer speaks in clipped fragments, an elder in
   rhythmic proverbs, a Storm Wizard in cold, formal questions.

## The 5 cast questions (Michael's to answer)

1. **Visual vibe & era:** strict 8-bit NES (Zelda 1) — chunky 16×16, 3
   colors per sprite — or 16-bit SNES (A Link to the Past) — 16×24 taller
   proportions, richer shading, expressive hair/cloaks?
2. **Hero silhouette (Corn Man):** what is his unmistakable prop — a wide
   straw farmer's hat, a tunic with a golden tassel, a cloak, or a
   specific tool/weapon carried on his back?
3. **Antagonist contrast (Storm Wizard & Blight King):** should the Storm
   Wizard feel like a towering robed sorcerer (Agahnim / Wizzrobe style)
   or a lean, sharp-angled tempest figure — and how visually distinct
   should he be from the Blight King?
4. **Townsfolk & keepers' personality:** earthy and humorous (Link's
   Awakening / Majora's Mask quirky) or solemn and mythic (A Link to the
   Past's sages and maidens)?
5. **Signature color palettes:** specific accent colors reserved
   exclusively for key characters (e.g. bright gold strictly for the
   Cob/hero; deep crimson/violet strictly for royalty or villains)?

## Google's (Gemini) proposed direction (via Michael, 2026-11-18 — PROPOSAL, not Michael's decision)

- **Era:** 16-bit SNES proportions (16×24) for posture/movement, locked to
  strict 8-bit color discipline — 4 colors per sprite (outline + shadow +
  base + highlight).
- **Corn Man (Google spec):** wide-brimmed straw hat with a V-notch, husk-green
  tunic, golden belt tassel; palette #1A1412 / #4E7A27 / #E6C25A / #FFD700;
  wrench strapped diagonally across the back once acquired; silent hero.
- **Storm Wizard:** tall, lean, jagged — high windswept collar,
  asymmetrical storm-cloak; slate-blue, charcoal, electric white/violet.
- **Blight King:** massive and grounded — broad horned/crowned shoulders,
  slow crushing posture; rot-purple, black, sickly ember-orange. Wizard =
  fast wind; King = dead weight.
- **Tone:** villagers earthy, warm, quirky (Link's Awakening); solemn
  rhythmic speech reserved for the Old King, Pearl, and the Barn Keepers.
- **Reserved colors:** true bright gold #FFD700 ONLY for the Golden Cob,
  Corn Man's tassel/mark, Poppy's royal crest — never on terrain/props.
  Storm violet + acid blight ONLY for the Wizard, Blight King, and crows.

## Muse's audit of the proposal against the shipped game (2026-11-18)

Checked against `corn-man-sprite-sheet.png` (the live sprite) and Michael's
standing correction of 2026-11-17: **do not change Corn Man's body.**

MATCHES canon:
- Gold reserved for Cob / hero's mark / Poppy's crest — the game already
  runs on this (golden kernel mark, Golden Cob).
- Storm violet/blight colors reserved for Wizard, King, crows — crows are
  already the Blight King's watchers.
- Quirky villagers + solemn King/Pearl/Keepers — matches the cast as built.
- Wizard fast vs King heavy — clean contrast, no canon conflict.

COLLIDES with the locked Corn Man:
- **The straw hat and tunic redesign his body.** The shipped Corn Man has
  no hat and no tunic — his body IS the golden cob (kernel-grid texture,
  green husk shoulders, green sprout on top). Michael locked the body
  2026-11-17. A hat is an ADD-ON question, not a spec assumption.
- **The spec drops his red cape** — a major silhouette element in every
  frame of the shipped sheet — and its palette has no red and no blue,
  though his cape is red and his pants/eye-gem are blue. Google's
  reserved-color split (crimson for royalty) also has to reckon with the
  hero already wearing red.
- The wrench-on-back and 16×24/4-color discipline are compatible as
  refinements; the body swap is not.

Open for Michael: adopt the direction with Corn Man's body kept as-is
(hat as a separate yes/no), or treat the whole sheet as a redesign
proposal that overrides the 2026-11-17 lock — his call, not Google's.

## Code received (via Michael, 2026-11-18 — from the Google (Gemini) session, PROPOSAL)

A `bakeSprite(rows, palette)` canvas renderer plus Google's proposed Corn Man
palette as code:

- K `#1A1412` (dark earth outline), G `#4E7A27` (husk green),
  S `#E6C25A` (straw), Y `#FFD700` (reserved gold).

Notes: (1) It ships no sprite row data — it's a palette + renderer only,
nothing renders from it yet. (2) The palette has **no red and no blue** —
the shipped Corn Man's cape is red and his pants/eye-gem are blue, so
baking with this palette as-is would erase the cape. Filed as part of the
proposal, NOT integrated into the game; the game build waits on Michael's
word in the build lane.

## Google's full Corn Man spec (via Michael, 2026-11-18 — PROPOSAL, verbatim substance)

- Dimensions: 16×24 sprite, 16×16 ground hitbox at the feet.
- Silhouette hook: wide-brimmed straw hat (14px) with a single V-notch on
  the LEFT brim + husk-green tunic + one bright gold tassel at the left hip.
- Secondary hook: after Eli gives the wrench, a 45° steel handle peeks
  above his right shoulder.
- Walk: 1px forward lean; hat brim bobs down 1px on contact frames.
- Palette: K `#1A1412` outline/eyes/boots · G `#4E7A27` tunic/hat band/
  sleeves · S `#E6C25A` hat/skin/cuffs · Y `#FFD700` RESERVED — belt
  tassel & marked-hand glint. Plus transparent.
- Voice: silent protagonist; held-item lifts, head nods, companions react.
- Idle tell: every ~4s standing still, the gold tassel or marked hand
  glints 1 frame.
- A full 16×24 idle-front pixel matrix was supplied (rows 00–23: hat crown,
  husk band, 14px brim with the V-notch at row 05 cols 1–2, face with K
  eyes at row 08, tunic rows 11–18, gold belt row 15, tassel drop row 16,
  boots rows 19–22, empty ground-shadow row 23) — on file in this chat's
  transcript 2026-11-18 22:08 CST; reproduce into a sprite file only on
  Michael's build word.
- STILL A PROPOSAL: it redesigns the locked body (hat + tunic, no cape,
  no blue). Michael's adopt/override call is pending.

## Research brief — headline findings (2026-11-18)

Full brief: `~/workspace/research_notes/legend-of-corn-character-design-20261119-0403/report.md`
(sourced; NES/SNES/GB hardware references checked live).

- **Real color discipline:** NES sprites = 3 colors + transparent per
  palette (Link is two stacked 8×16 sprites); SNES = 15 + transparent.
  Google's "4 colors incl. outline" sits between the two — a fair hybrid rule.
  The brief recommends the SNES-style target overall.
- **Silhouette law confirmed** per character (Link's flopping cap +
  sword/shield asymmetry; Zelda's gown triangle + tiara; Wizzrobe's
  faceless hood, two white eyes; Ganon ~2× hero scale). Fun wrinkle:
  Agahnim's art wears red but his in-game sprite is GREEN — official art
  and sprite can disagree; the sprite is what players remember.
- **Young/old rule (for Pearl):** 3 anchors NEVER change, 4 dials MUST
  change, 1 prop becomes a time-device. Canonical case: Skyward Sword's
  Impa — braid, red eyes, Sheikah eye fixed; height, posture, hair length
  changed; her single braid literally counts the years she waited.
- **NPC formula:** 1 trait + 1 obsession + 1 tic in ≤3 boxes; cadence by
  role (Old Man ≤6-word imperatives; elders formal multi-box; the
  princess's lines are 3–5-word pleas; the final villain gets the longest,
  most courteous sentences in the game).
- **Boss rule:** the boss = the dungeon's noun, animalised, weak to the
  dungeon's item, with a weak point readable at sprite scale.
- **Cast slots:** one giver per verb, each with a different gate + reward —
  that's how Zelda II runs 8 Wise Men and ALttP 7 Maidens with no
  redundancy.
- Couldn't verify: exact per-frame bounding boxes for individual ALttP/LA
  sprites (no single authoritative source); the "ALttP pink hair was a
  palette limit" claim is disputed — flagged, not settled.

## Google's revised Corn Man spec v2 (via Michael, 2026-11-18 — after seeing the real sheet)

Google got the Corn XRPL sheet and rebuilt its spec: 6-color palette
(K `#12131A` shades/outline, Y `#FFD21E` cob, G `#3D8E33` husk,
S `#F4B886` skin, B `#1565D8` suit, R `#D92525` cape) + a new 16×24 matrix
(rendered: `google-corn-man-v2-superhero.png`).

Muse's audit: the family is now RIGHT — cob-crown head, flared husk ears,
black shades, blue suit, red cape. One flag CORRECTED by Michael (2026-11-18, with Corn's own watcher art):
the red-and-gold **"C" chest shield is CANONICAL** — it is all over Corn's
community buy/sell art and videos (blue suit, red cape/trunks/boots, gold
belt, C shield, cob head, husks, shades). Google had seen that art; Muse
had not, and wrongly flagged the C as invented. Remaining real difference:
the spec's 16×24 proportions are slimmer/smaller-headed than his in-game
~32×40 big-head build. Reference still filed: `corn-man-reference-buy-art.jpg`.
Cape: RED in the art and the game; gold only on the CODED sheet.
**Michael ❤️-reacted to the v2 render (2026-11-18)** — the superhero spec
is the approved look for Corn Man as a design standard.

Canonical reference now in the game folder: `corn-xrpl-character-sheet.jpg`
(Corn XRPL, "The Liquidity Mutant" — CODED sheet #10). Note: his cape is
GOLD on the sheet, RED in the game — flagged to Michael 2026-11-18.

Character-sheet library check (2026-11-18): `~/workspace/user/media_library/characters/`
holds the CODED cast only (XRPMan, Boo, Mr Zamn, Lex, Optimystic Prime,
Stone, Lady K, Corn). **Poppy, Pearl, Eli, and the Storm Wizard have NO
reference sheets** — game-original characters, designed fresh when their
turn comes.

## Google's self-debug + v3 matrix (via Michael, 2026-11-18) — Muse's render QC

Google debugged its own v2 (C blob, chin beard, floating arms, flat cob)
and issued a v3 matrix + palette (adds O `#D99200` kernel shade; K now
`#1E1F2B`). Rendered by Muse: `google-corn-man-v3-debugged.png`.
Muse's honest QC: arms FIXED (black seams, fists at hips), jaw FIXED
(no beard), husks improved (sweep up at the temples). NOT fixed: the "C"
still reads as a small red notch in a big gold bib, not a letter — at
16px the C only gets ~2px of red. New trade-off: the shades band grew
into a wide black slab wider than the face, and the cob shrank to a
narrow column. Muse's standing suggestion: at sprite size, either run
the shield edge-to-edge across the chest so the C gets real pixels, or
keep the shield and drop the letter.

## Muse's own take (2026-11-18)

`remy-corn-man.png` — drawn from rectangles on his real 32×40 in-game box,
big head kept, kernel rows in the game's two golds (#ffd91a/#e0aa00),
husks framing the whole face, C shield from Corn's art, and the golden
MARK as a glint across his right fist (both Google takes missed the mark).
Michael: "amazing. That is pretty good." Front-idle sketch only.
Google reviewed Muse's take (via Michael) — praised the kernel grid +
silk tuft, the shades glint + grin, the marked fist and clean C — and
offered 2 polishes, both applied in `remy-corn-man-v3.png`: (1) cob top
tapered (beveled top corners), (2) 1px arm seams in #0E4499. QC'd clean
by Muse before sending.

## ⭐ CANON — Corn Man front & back (Michael, 2026-11-18, 22:26 CST)

Michael declared Muse's take CANON: front v6 (slim cape, tapered cob,
bridged sunglasses with the nose under the bridge, marked fist) and
back v1 (cape spread, full kernel grid, mark on his left = image-left
from behind). Files: `corn-man-CANON-front.png` / `corn-man-CANON-back.png`
+ draw scripts `corn-man-canon-front.py` / `corn-man-canon-back.py` in
this folder; copies in the memory vault `legend-of-corn/` as
`canon-corn-man-front.png` / `canon-corn-man-back.png`.
Next on him: ANIMATION — walk cycle + punches off the shoulder,
alternating arms, never from the chest (his standing rules).

## ⭐ Bosses' lair concept art — APPROVED (Michael, 2026-11-18, 22:56 CST)

`bosses-lair-concept.webp` — full illustrated (non-pixel) art of the
Storm Wizard and the Blight King in the black castle throne room, in the
manual/box-art tradition Michael pointed to. Michael: "that is perfect."
Saved in the game folder + the memory vault (`legend-of-corn/`). This is
the reference look for both villains; the pixel sheets translate it.
(Pixel King v3 still has a small cleanup pending from Michael's note —
"clean him up just a little bit.")

## Status

- **Michael's call (2026-11-18, 22:13 CST): the shipped Corn Man is good —
  he stays.** Google's sheet is a redesign of a character that already
  exists; the live question was never his body. Corn Man is drawn in-game
  from rectangles in a ~32×40 box (head ≈ half his height), NOT a baked
  16×24 pixel sprite — Google's proportions differ from his, too.
- **Michael will supply the canonical character sheet of the real Corn
  Man** ("I need to give you guys the character sheet of the real corn") —
  that sheet becomes the standard Google designs against and Muse audits
  against. Pending his delivery.
- **Final boss jumps the design line (Michael, 2026-11-18):** the final
  boss is who comes in and takes Poppy in the opening, so he is designed
  FIRST. Open tap: does the King himself do the taking (one villain opens
  and closes the game), or does his Wizard take her while the King stays
  withheld? Plan draft currently has the Wizard taking her.
- Deep research launched 2026-11-18 (classic 8-bit/16-bit character design
  + cast architecture: sprite constraints, silhouette/prop language, color
  coding, single-trait NPCs, dialogue cadence, cast roles, young-vs-old
  same-character design). Brief lands in the research notes; the cast
  guide gets built from it + Michael's answers above.
- Nothing designed or built until Michael answers / says go.

## NPC DETAIL STANDARD (Michael, 2026-11-19 00:59 CST)
ALttP's cast is the bar: 3-4 tones per surface, real faces at 16px,
distinct silhouette + palette per person, one identifying prop each.
Reference filed: characters/reference-alttp-npcs/ (9 wiki screenshots
+ REFERENCE.md). Applies to every cast sheet from Poppy onward.

## EVERYTHING GETS THE DETAIL PASS (Michael, 2026-11-19 01:00 CST)
"The statues, everything. The houses. It can all have more detail."
The ALttP detail standard applies across ALL the game's art — cast,
statue, houses, tiles — not just new work. First fruits:
characters/detail-lineup.png (Corn Man detail pass on the canon design,
the Harvest King's first living likeness, Storm Wizard detail pass).
Statue and village houses re-skin at this bar in their turn.

## STATUE = THE LIVING KING IN STONE (Michael, 2026-11-19 01:04 CST)
The town-square statue is literally the living Harvest King's sprite
weathered into stone — same crown, robe, gem, staff — so the prologue
and the present day are the same man, a hundred harvests apart.
Sprite standard: maps/google-statue-stoneking.js (32x48, verified).

## SPRITE CRAFT STANDARD — 16x24 (relayed by Michael, 2026-11-19 01:14 CST)
Google's five-difference analysis, adopted as the working eye:
1. People are 16x24. A giant canvas forces noise; at 16 wide every
   pixel carries structure.
2. Shade in CONNECTED clusters of 2-4 px following the form (top-left
   light -> mid -> bottom-right shadow). Isolated 1px dots = noise.
3. 45-degree top-down camera: top of head/hair visible, eyes LOW on
   the face, hem CURVES (ellipse), never a flat bar.
4. Anti-alias internal corners: a mid-tone bridge pixel where dark
   outline meets bright highlight.
5. One shared ~15-color palette; the same dark ink (#181010) serves
   outline, pupils and deep folds so nothing looks pasted on.
First proof: characters/google-king-16x24.js — matrix perfect, living
+ statue from one matrix by palette swap. The big King stays the
portrait/lineup art; 16x24 is the in-game sprite form.

## OPENING CAST PORTRAIT — the game-book family picture (2026-11-19 01:16 CST)
Michael's call: one real image of the whole beginning cast, full body,
for the game book. art/opening-cast-portrait.webp — Corn Man, Eli,
young Pearl, the Harvest King, Poppy, old Pearl, the Storm Wizard,
before the castle at harvest. DEBUTS in this picture (Michael to
approve as canon for their sheets): Poppy (corn-silk gold hair, cream
+ poppy-red dress, gold crest brooch), young Pearl (brown braid, cream
blouse, rust skirt/apron, ONE pearl bead at her throat), old Pearl
(same woman: gray braid same shoulder, same bead, shawl, staff), Eli
(straw hair, vest, satchel, walking staff). The two Pearls share the
bead and the braid — the time-anchors hold.
