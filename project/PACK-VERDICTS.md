# Pack verdicts — Google drops for the new game (cold-tested by Muse)

## Prologue Engine Pack (2026-11-19 00:00) — prologue/google-prologue-pack.js
- Crows: 3 frames, all 16x16, clean charset, frames genuinely differ. KEEP.
- Recolor helper: works (token -> hex rows, shape preserved). KEEP.
- Land-flinch morph: logic SOUND on a synthetic 256x96 world (pre-state:
  massif lush, river dry, pond shrunk; sweep 0->pre, 1->post). Caveat:
  its coordinates are Legend of Corn's v5 world — the new game re-aims it.
- State machine: runs exactly as coded (2 guests -> beat 3; beats 4-9
  audio sequence correct). BUT it hardcodes a STAGING GUESS: the player
  walks the feast as young Pearl and guest-chats trigger the crows.
  That is Michael's open tap, NOT settled — machine kept, trigger to be
  re-pointed when he rules.
- Their harness: CRASHES as shipped (sparse DIRS, fourth sighting of
  this bug) and the feast/village maps it claims to verify were never
  in the pack. Muse fixed the DIRS and ran it against real walled
  test maps: hall entry->dais PASS, village spawn->Pearl PASS,
  spawn->overlook PASS.

## Palace Decor Pack — opening-castle/google-palace-decor.js
- Paste arrived garbled inside GOLDEN_CANDELABRA (page text mid-array);
  reconstructed 8+8 rows. After that: 15 sprites, all 16x16, clean.
- GOLDEN_FEAST_PLATTER rows 9-12 were 17 wide — fixed (one char per run).
- Fireplace and torch A/B frames genuinely differ — real animation.

## Courtyard Decor Pack — opening-castle/google-courtyard-decor.js
- 7 sprites; ROYAL_WALL_BANNER row 4 was 15 wide — fixed (crown stays centered).
- Fountain A/B frames genuinely differ. Statue is a proper 2-tile pair.

## Castle & Grounds Blueprints — opening-castle/google-castle-grounds.js
- Exterior as pasted: rows of 64/66/65 again; east terrace strip (x62-63)
  was a dead island (42 tiles). Fixed with the standard center-trim
  (door row sheds Ws): true 64, courtyard/doors/rear walk/both sides
  reachable, dead 0, walked 1,164. Moat + twin bridges walk clean.
- Interior as pasted: 50 wide, not the declared 48. The "connecting"
  cross-hall rows (17-18, 29-30) left the separator columns blank, so
  both wings were sealed silos — the original citadel disease in a new
  coat. Fixed by flooring the separators on those four rows: dais,
  library, kitchens, stairs, banquet hall, parlor, barracks ALL
  reachable, dead 0, walked 1,174. Fixed set: castle-grounds-fixed.js.
- Reconciliation (fit authority): this decorated footprint is the
  OPENING castle (courtyard alive, gates open). L9 keeps the art-match
  sealed standard — same family, opposite state, exactly the story.

## Palace Expansion Pack — opening-castle/google-palace-expansion.js
- 9 sprites (throne pair, cornucopia, parade armor, bookcase, tapestry,
  chest, door pair): ALL 16x16, charset clean against the palace palette.
  First pack of the night with zero defects. Throne-room mock rendered.

## Upper Floors Pack (2F + 3F) — opening-castle/google-castle-upper-floors.js
- 3F: nearly perfect as drawn — both bell towers, catwalk, spire balcony,
  relic chest all connect, dead 0. Only flaw: 35 rows, not 36 (their sky
  block was one row short). Fixed by adding the row.
- 2F: broken as pasted — four cross rows 50 wide against 48 elsewhere,
  seams blank, so from the spiral stairs only the east column was
  reachable (727 dead). Fixed like 1F: seams collapsed to floored
  doorways, true 48. Now: Poppy's chamber, King's suite, both tower
  stairs, skybridge, south battlement exit — all reachable, dead 0.
- Stair truth: 2F<->3F tower stairs align EXACTLY at (7,5) and (39,5).
  1F->2F spiral stairs offset by 2 columns (1F is 50 wide, 2F is 48) —
  align by room when stacking. Bell + canopy bed sprites: clean 16x16.
- Fixed set: castle-upper-floors-fixed.js.

## Castle-Foot Village Pack — maps/google-village-pack.js
- Michael's four calls recorded in maps/VILLAGE-PLAN.md and embodied
  in the map: 32x24, ruin look-only, heal/save at BOTH Pearl's hearth
  and the inn, chapel NE of the park.
- The map is Google's best yet: all 8 doors at exactly the claimed
  tiles and ALL reachable; Pearl, spawn, statue, fountain placed as
  claimed; ZERO dead tiles (462 walked); the balustrade row is never
  stepped on — look-only holds by construction.
- Only flaw: rows 2-3 were 34 wide. Fixed (balustrade/promenade
  trimmed to the grid): village-fixed.js. All checks re-pass.
- Interiors: all 16x12, floors connect; hearth, beds, counters
  standable (store NPCs correctly talk across the counter).
- Sprites 9/9 clean after rejoining the split COTTAGE_DOOR.
- Their harness as pasted is mangled past running (const reassigned,
  empty queue, sparse DIRS, lost backticks) — my walk covers and
  passes every check it names.

## Elaborate Zelda-Style Village (48x36) — maps/google-village-elaborate.js
- Google's richness critique is RIGHT (staggered houses, pitched roofs,
  market, well, fences, alleys) — and topologically this is their best
  map: every row truly 48, ZERO dead tiles, 1,144 walked, every door
  reachable, balustrade look-only holds, south road exits clean.
- Flaws: 37 rows as pasted (the store block's door row is drawn
  twice) and STREET_LANTERN has 15 rows. Fixed: village-elaborate-fixed.js.
- OPEN CONFLICT for Michael: this is 48x36, but his ruling 20 minutes
  earlier was KEEP 32x24 (tight, 20-second walk, no filler). Richness
  vs his tightness call — his tap decides; the 32x24 stays the
  standard until he says otherwise.

## Kakariko-Grade Village (48x36) — maps/google-village-kakariko.js
- FIRST Google map to pass the cold walk UNTOUCHED: 36 rows, every row
  exactly 48, zero dead tiles, 1,017 walked, sprites 10/10 clean.
- Terraces work: twin cliff stairs join upper terrace to lower town;
  all 8 doors reachable; Pearl exact at (8,7); weathervane plaza,
  hedge park (fountain + statue), vendor mat all standable.
- Claim drift only: chapel door is (36,5) not (35,5); smith (30,15)
  not (31,15); inn (38,21) not (39,21); stonecutter (36,27) not
  (37,27); cave mouth is at (38,10) — the cliff's foot — not (40,9).
- Build note: 'S' does double duty (stairs AND the statue 'SS').
  Give the statue its own tile ID at build time.
- Still 48x36 — Michael's size tap (32x24 ruling vs elaborate line)
  remains formally open; this is the strongest elaborate candidate.

## PRESENTATION STANDARD — Michael, 2026-11-19 00:30 CST
The overhead tile maps are the WALKING BONES only — logic, never the
game's face. The game's view is the concept sheet's perspective:
elevated Zelda view with fronts, heights, and depth. Close-ups are
SCENES (the subject in its place), not icons on blank ground.
Statue proof: maps/statue-scene.png.

## COLOR STANDARD — Michael, 2026-11-19 00:33 CST
"It's the colors. Look at the shadows and subtle things." Every surface
shaded against ONE light (upper left): multi-tone materials, cast
shadows, occlusion bands where surfaces meet, per-stone variation,
facets + glint on gems/gold. Flat fills are bones-only, same as the
overhead maps. Proof: maps/statue-scene-v3.png.

## GOOGLE STATUE SPRITE — polished 48x56 (2026-11-19 00:43 CST)
First Google matrix of the run with ZERO defects: 56/56 rows at
exactly 48 wide, charset clean vs the merged palette. Fixes verified
on the render: open-mouth beard GONE (mustache arch + stone chin +
mouth line), sheaf stalks connect into the fist, pedestal seams step
outward (reads round). Half-landed: cloak folds yes; the "hand
cradling the cob" reads as a dark notch, not clearly a hand.
This is the in-game tile sprite standard for the statue; the plaza
scene (statue-scene-v7) stays the presentation art.

## GOOGLE MASTER VILLAGE PACK 48x36 (2026-11-19 00:44 CST)
Geometry: PERFECT — map 36x48 exact, 4 interiors 12x16 exact, 7
sprites 16x16 exact, charsets clean (Google's self-caught palette
'A' fix is real). Google's harness STILL broken: `vis = 1` assigns
over a const (crashes), and its door list is off by one on all four
east doors (actual: Chapel 38,7 / Smith 40,20 / Stonecutter 32,27 /
Inn 38,33-pre-fix). REAL BUG: Mill + Inn doors were entombed in the
south wall row (wall above, perimeter below) — unreachable. Fixed
under fit authority: doors moved to the corner tiles (11,33) and
(36,33) where they meet the grass. Post-fix BFS: 1,033 walked,
0 dead, all 9 landmarks reached. NOTE: this pack is the ELABORATE
48x36 line; Michael's ruled standard remains the 32x24 (00:24 CST)
until he says otherwise — this is filed as a candidate.

## ART STANDARD — Michael, 2026-11-19 00:53 CST
"16-bit SNES pixel craft (ALttP / Link's Awakening) paired with strict
8-bit Zelda 1 screen/layout clarity — clean, readable rooms with rich,
subtle pixel textures rather than flat blocks or noisy modern art."
That is the game's art target, in his words.

## GOOGLE HYBRID ALttP PACK (2026-11-19 00:53 CST)
Sprites: PERFECT — 8/8 exactly 16x16, charset clean. Palette R
(terracotta) defined but unused. Rendered cohesion mock: the soft
palette lands (sage grass, sandstone cobbles, brown outlines). Gaps:
no plain WALL or WINDOW tile, so a house front cannot be built from
this pack alone (roof + door only); hedge rosettes and log posts need
a 2-3 tile run to read — single tiles read as slab/bells. Door crest
is a solid gold block, not a crest shape. Filed as the texture
standard candidate; wall/window tiles are the ask-back.

## GOOGLE HIGH-DETAIL STATUE 50x56 (2026-11-19 01:02 CST, "just for fun")
Drawn on a 50-wide grid despite the 48 label (uniform, not ragged);
one stray char P (pink flowers) missing from its palette — added
#E87AA0 under fit authority. Render verdict: the STONEWORK lands —
multi-tone granite, round stepped dais, moss + wildflower ring, cob
at the chest, pleats and gold hem. The FACE does not: beard-curl +
mustache pattern renders as a white muzzle at sprite scale, eyes lost
under the crown band, sheaf merges into a gold blob at the shoulder.
Filed as reference: body/plinth shading yes, face no (the earlier
polished statue's stern face stays the better face).

## STONE KING STATUE 32x48 (Google, 2026-11-19 01:04 CST) — THE STATUE STANDARD
Matrix PERFECT: 48 rows, every row exactly 32, charset clean — Google's
first flawless big sprite. Design logic endorsed by Michael: the statue
IS the living Harvest King (detail-lineup sprite) frozen in stone —
same 4-point crown with emerald inset, brow band, deep-set eyes,
mustache, corn-stalk staff with faded red ribbon, center gold trim,
emerald gem at chest, on the stepped flower-ring plinth. Verified in
close-up crop: face, crown, sheaf and gem all read. Supersedes the
polished 48x56 as the in-game statue sprite; statue-scene-v7.png stays
the presentation art.

## THE KING & HIS STATUE — MICHAEL'S METHOD (2026-11-19 01:05 CST)
Michael overruled the redraw approach: "just make it your king
character in statue form just change the color" + "make him defined"
+ "fix the staff works in his hand." Done exactly so:
characters/king-living-v2.png (staff gripped with wrapped fingers,
three separated cobs, ink definition throughout) and
king-statue-v2.png — the SAME pixels recolored to stone, moss and a
chipped crown point added. This pair is the standard; Google's
stoneking is retired to reference.

## SNES BOSS PACK — Wizard 24x32 + Blight King 32x32 (Google, 2026-11-19 01:20 CST)
Geometry: Wizard perfect as pasted (32 rows x 24, charset clean).
King row 22 was 34 wide — fixed to 32 (2 P's out of the torso run),
then clean. Renders: characters/bosses-snes-pair.png.
Craft: clusters hold, no noise. TWO DESIGN DRIFTS are Google's calls,
not Michael's: (1) the Wizard's chest GEM (approved lair portrait)
became a lightning fissure, and as drawn it stripes — reads as a
zipper, not lightning; (2) the King's rotted-COB chest sigil
(Michael-approved v3 sheet) became a skull whose golds merge with the
scythe blade. Both await Michael's ruling; fixes are ready to make
(jag the fissure / restore gem; restore cob, separate the golds).

## BLIGHT KING — MUSE'S REBUILD (2026-11-19 01:21 CST)
Michael, on Google's 32x32 King: "I think you could do better than
that... You want to fix that?" — and handed over the concept art
(art/bosses-concept-ref.webp) as the authority. Rebuilt from the art:
characters/blight-king-muse-32x32.js, render blight-king-muse.png.
Crown = separated bone spikes over a gold band with the ember gem;
face narrowed, ember eyes socketed under a brow, grim mouth; chest
skull SMALL and centered on dark plate with ember cracks at its
sides; scythe shaft crosses LOW and the blade hangs at his side,
clear of the chest; legs split into greaves with knee plates and a
wide stance. Supersedes Google's King as the standard, pending
Michael's verdict. (Note: the concept art itself carries the skull —
Google's chest idea was right; its execution was the blob.)

## RULING — THE KING IS THE FIRST ONE (Michael, 2026-11-19 01:24 CST)
Michael rejected Muse's 32x32 rebuild outright ("That looks
terrible") and called back the FIRST King Muse made —
blight-king-sheet-v3.png. That sheet stands as the King. One fix
applied at his direction: the scythe blade now sticks UP in the air
(v4 = v3 untouched + raised crescent blade over his shoulder, shaft
in his fist). The SNES 32x32 line (Google's and Muse's rebuild) is
retired for the King.

## GOOGLE KING v3 — UPRIGHT SCYTHE (relayed 2026-11-19 01:28 CST)
Geometry perfect (32x32, one missing token: y = #FFF066 supplied
from Google's own SNES palette). The upright carry is a real
composition gain — shaft full-height, gauntlet wrapped mid-shaft,
legs split. Still weak: the blade reads as a gold flag, not a
crescent; the crown is a plain gold bar; the chest skull is a
gold-orange rectangle. Filed as a candidate. NOTE: this runs
against Michael's 01:24 ruling (the first King stands, 32x32 line
retired) — reopening that is Michael's call alone.

## GOOGLE KING v4 — 4-TONE RAMP (relayed 2026-11-19 01:31 CST)
Geometry PERFECT as pasted — first King matrix needing zero fixes.
The 4-tone faded purple ramp is a real gain: pauldrons bevel, the
face rounds into a true scowl with ember-cored eyes, chin tapers.
Still failing: the blade (a gold flag for the third time, not a
crescent) and the chest (gold-orange medallion, not a skull).
Candidate only; Michael's 01:24 ruling stands.

## RULING — GOOGLE KING v4 APPROVED (Michael, 2026-11-19 01:32 CST)
"there we go finally" — the 4-tone 32x32 King is THE King sprite.
This supersedes the 01:24 ruling: the first sheet (v5) stays filed
as the King's portrait art; v4 is the in-game standard.

## GOOGLE WIZARD v2 — TWO-FRAME LIGHTNING PACK (relayed 2026-11-19 01:34 CST)
Both frames exactly 24x32. Strays H and M in both frames (their own
bake function silently SKIPS unknown chars — the holes would have
been invisible in their renderer; fixed here: H->L, M->S). Frames
differ at 166 pixels — the crackle animation is real, not a recolor.
Renderer (pulsing aura + 85ms frame swap) is sound engine material.
TWO FLAGS for Michael: (1) the eyes are now CRIMSON — every approved
image of the Wizard (lair concept, family portrait) has pale eyes;
(2) the lightning covers the robe in a criss-cross lattice — it jags
properly now, but reads as a net more than bolts; sparser channels
would strike harder. Both are Michael's calls.

## WIZARD v4 — ONE BOLT, PALE EYES (Michael's direction, 2026-11-19 01:35 CST)
Michael: "one single lightning bolt that goes from the top to the
bottom" — and re-sent the concept painting as the reference. Done:
the lattice is stripped back to robe, ONE thin jagged bolt runs
throat to hem (white core, lavender glow on the outside of each zig,
violet root at the sharp turns), and the eyes went PALE ICE to match
the painting — Google's crimson is out. Both frames carry the bolt;
frame B shifts its path so it crackles in place. This is the Wizard
standard unless Michael says otherwise.

## WIZARD — RED EYES + GLOW SETTLED (Michael, 2026-11-19 01:36 CST)
Michael overruled the pale eyes: "It's supposed to have red eye
dots." RED DOTS are the ruling (the painting's pale glints do not
govern the sprite). And: "make sure it glows... it's supposed to
look like it's got lightning on it all the time. And it's animated."
Glow lives in the renderer (wizard-renderer.js): pulsing violet
aura + 85ms A/B frame swap, always on. Proof render:
characters/wizard-animated-glow.gif (10 frames, looping).
