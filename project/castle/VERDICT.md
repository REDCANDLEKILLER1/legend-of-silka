# Final Castle (L9) — Google's production pack, cold-tested by Muse
Date: 2026-11-18 · Source: Google (Gemini) via Michael, this chat · Status: FIXED REVISION PASSES

## Google's pack as pasted — DOES NOT RUN, DOES NOT CONNECT
- Its own Node harness crashes on the first BFS: the direction table is a
  sparse array (`[[-1,0],, [0,-1],]` — right and down missing, one hole),
  and iterating it throws `TypeError: .for is not iterable`. The victory
  checks (`!vis1 || !vis1`) never inspect a single tile, so even a running
  version would prove nothing. "Tested" does not survive contact.
- `onWizardDefeated` contains `citadel = 'H';` twice (assigning a string
  over the whole grid const — a crash), and `onBlightKingDefeated` does
  `sovereign[y] = ','` (replaces whole rows with one character).
- Coordinates are off: east switch is at (46,3), not (44,3); the Sanctum
  Gate tiles sit at x24–25, but the unlock loop opens x23–24 (leaves a
  gate tile standing, opens a wall). Doors at (24,0), not (23,0).
- Row 32 (the entry stairs row) is 48 wide; the other 35 rows are 50.
  Its stair tiles don't stack with row 33's.
- THE WINGS ARE SEALED ISLANDS: the room-separator spaces on the two
  cross-bridge rows (17, 29) are impassable, so nothing connects the
  center column to the side wings. From the cavern stairs you can reach
  only the foyer + center hall — both wing switches are unreachable.
  The whole endgame path fails at leg 1.
- THE GATE HANGS OVER SOLID ROCK: rows 11–12 under the Sanctum Gate are
  solid wall in the center room, so even an opened gate leads nowhere.
- SOVEREIGN BYPASS: 2-wide floor lanes run up both outer edges of the
  chamber (x2–3, x28–29), outside the chasm ring — you can stroll from
  the entry straight to Poppy's altar without ever entering the arena.
- Healing springs are pre-printed in all three top rooms (14 tiles),
  contradicting the "spawn in the Throne Hall alcove after the Wizard
  falls" design.
- Clean bills: all three sprites are exact 16×16; the sovereign chamber
  is a uniform 32×24; the citadel's bones (wings/gate/two-stage flow)
  are a sound design — the failures are in the joints, not the idea.

## Muse's fixed revision (`fixed-pack.js`, `fixed-test.js`) — ALL PASS
Took away:
- Side-room healing springs (center alcove only, as designed).
- Google's broken harness and state hooks (rewritten intent-true:
  switches open the gate tiles wherever they are; wizard fall opens
  W/D; king fall converts his 2×2 to runner, cell by cell).
Added:
- `==` bridges across the separator gaps on rows 17 and 29 — the
  cross-bridges the comments always claimed were there.
- A 2-wide shaft under the Sanctum Gate (rows 11–12, x24–25) so the
  gate is a door, not a decoration.
- Row 32 rebuilt to 50 wide; stairs now a true 2×2 block at (24–25,
  32–33), stacking with row 33.
- Chasm in the sovereign perimeter lanes (rows 4–17, x2–3 / x28–29).
Result (real BFS, 4-direction, Google's own walk set):
LEG1 stairs→both switches PASS · wizard sealed pre-switches OK ·
LEG2 post-switches→Wizard PASS · LEG3 post-wizard→Sovereign Doors
PASS · LEG4 entry→King PASS · LEG4b no altar route that skips the
boss chamber OK · LEG5 post-king→Poppy's Altar PASS · dead walkable
tiles in either map at end state: NONE.
Grid truth: citadel is 50×36 (three 16-wide rooms + void separators),
sovereign 32×24. Renders: citadel-fixed.png, sovereign-fixed.png.

## Addendum — L9 Overworld Exterior (Google, 2026-11-18 23:22 CST): PASSES AS PASTED
First Google pack to survive the cold walk untouched. Uniform 32×24;
all 3 sprites exact 16×16; doors exactly where claimed (15–16, 15);
4 guards as claimed. BFS from the causeway (15,23), walk set . = G:
rear terrace behind the castle REACHABLE, both mid-terraces REACHABLE,
front-door approach REACHABLE, doors themselves never stepped on
(sealed OK), walkable-but-unreachable tiles: NONE (348 terrace tiles
walked). Their harness this time is honest — complete direction table,
real per-cell assertions. The 360° perimeter is real. Files:
google-exterior.js, exterior-test.js, exterior-render.png.

## Addendum — Massive Castle Exterior 64×36 (Google, 2026-11-18 23:36 CST)
- Their harness is broken a THIRD time: `vis = 1` reassigns a const
  (instant crash), the queue starts empty (start tile never pushed),
  the direction table is sparse again, and the checks compare the whole
  grid variable to 1/0 instead of reading cells. Never ran.
- The MAP, walked at its true drawn width: topology SOUND — full outer
  loop, courtyard, rear bailey, keep-door approach all reachable, doors
  sealed, zero dead walkable tiles, 1,309 tiles walked.
- BUT it is drawn 66 wide, not the declared 64: rows 4–35 are 66 and
  mirror-symmetric at 66; row 3 is 65; rows 0–2 are 64. As drawn it does
  NOT seat on 4×3 fields (needs a symmetric 2-column trim to a true 64,
  then a re-walk). Doors sit at (32–33, 17), not the claimed (31, 17);
  6 guards placed, not the claimed 8. Rows 5–8 and 31 are asymmetric
  (roof-window and ramp drawing slips).
- Scale is Michael's call: verified 32×24 (2×2 fields) vs this 64×36
  (4×3 fields) pending the trim. Files: google-massive-exterior.js,
  massive-test.js, massive-exterior-render.png.

## Addendum — Monumental decision + trim (Michael's tap, 2026-11-18 23:40 CST)
Michael chose the monumental castle. Trim applied to a true 64×36:
center-pair columns removed from the 66-wide body rows (mirror symmetry
preserved), the 65-wide curtain row lost its center tile, and the door
row shed one W per side so the doors land at (31–32, 17) — the exact
center Google claimed. Re-walked: rear loop, both promenades, courtyard,
bailey, door approach all REACHABLE; doors sealed; dead tiles NONE;
1,271 tiles walked; 31/36 rows mirror-symmetric (5 were asymmetric as
drawn). Files: massive-exterior-64.js, massive-64-test.js,
massive-exterior-64-render.png. The 32×24 exterior is superseded.

## Addendum — Art-match revision (Michael, 2026-11-18 23:40 CST)
Michael sent the approved castle art back with "make this match the
generated image." Rebuilt the exterior to the art's architecture: the
sealed grand doors moved OUT of the keep and INTO the south curtain
wall's gatehouse (round turrets + braziers flanking, causeway stops at
their landing); the open gatehouse arch and inner courtyard are GONE —
wings, bell towers, and the spired keep fill the walls solid, exactly
like the painting. The exterior is now promenade-only: circle it, test
the doors, leave for the cave. Walked: gate landing reachable, doors
sealed, full outer circle reachable, zero walkable tiles inside the
walls, zero dead tiles, 36/36 rows mirror-symmetric. This revision
supersedes the trimmed Google layout as the exterior standard.
Files: massive-exterior-artmatch.js, artmatch-test.js,
massive-exterior-artmatch-render.png.

## Gothic Citadel sprite pack (Google, 2026-11-18 23:44 CST) — CLEAN, one tip fails
All 8 sprites verified exactly 16x16; charsets use palette colors only
(+ '.' transparency on gargoyle/spire/brazier). The pack matches the
approved concept art: ashlar + weathered brick (moss flecks), lancet
window, purple slate roof, spire tip, chain gate, violet brazier.
Composed facade mock (gothic-facade-mock.png) reads tall and ornate —
this is the elevation art for the art-match exterior. Two notes:
(1) Google's "flip the chain gate every 6 frames" animation tip is a
no-op — the gate tile is mirror-symmetric, flipping changes zero
pixels (verified); a real second spark frame is needed for crackle.
(2) The gargoyle is the weakest read at 16x16 (eyes merge into a slit).
Files: google-gothic-sprites.js, gothic-sprites-sheet.png,
gothic-facade-mock.png.

## Fitted standard (Michael, 2026-11-18 23:47 CST: "Make everything to fit as you like. Just examples")
Michael granted fit authority over the castle pieces. The fitted set:
art-match exterior (promenade + sealed gatehouse) + fixed citadel +
sovereign chamber + Gothic sprite pack, unified on the Gothic palette.
Muse drew LIGHTNING_CHAIN_GATE frame B (gate-frame-b.js): chains fixed,
spark knot mirrored — the crackle animation now has two real frames.
Full south elevation rendered from the tiles: castle-south-elevation.png.

## Fitted standard (Michael, 2026-11-18 23:47 CST: "Make everything to fit as you like. Just examples")
Michael granted fit authority over the castle pieces. The fitted set:
art-match exterior (promenade + sealed gatehouse) + fixed citadel +
sovereign chamber + Gothic sprite pack, unified on the Gothic palette.
Muse drew LIGHTNING_CHAIN_GATE frame B (gate-frame-b.js): frame A is
symmetric both ways so flips do nothing — frame B keeps the chains
fixed and shifts the spark knot, giving the crackle two real frames.
Full south elevation rendered from the tiles: castle-south-elevation.png.
