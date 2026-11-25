# Castle circulation wiring — DONE (Remy, 2026-11-24 evening, Michael's correction)

Michael's ruling, restated tonight: the grand stairs on each floor go ONLY
to that floor's balcony — they never change floors. The ONLY way between
floors is the tower staircases, entered at the tower bases on the ground
floor (NW left, NE right). The map swap preserved the old wiring; this build
fixes the wiring to the design.

## Changes vs Castle_NewMaps_REMY.html (data-level diff, exhaustive)
- Ground + upper: the 4 grand-stair links (stairsW/stairsE on both floors)
  REMOVED. The flights are now walked, not teleports.
- Walk masks: bridges painted over all 4 flights (steps + landing, inside
  the balustrades, measured off the plates with grid crops) and small
  patches inside the ground floor's NW/NE tower alcoves. Cells only GAINED
  (ground +12,570, upper +5,936; zero lost); every other area's mask is
  byte-identical.
- Ground: NEW links towerNW [300,250,340,282] and towerNE [1094,250,1134,282]
  on the drawn spiral-stair feet, single option up to tower1_nw/tower1_ne
  pit_arr. NEW arrivals towerNW_arr (322,316) / towerNE_arr (1112,316) on
  the corridor south of each arch.
- tower1_nw / tower1_ne spiral choosers: NEW third option "Down to the
  Ground Floor" -> the ground arrivals above. The staircase now runs
  ground <-> tower I <-> upper <-> tower II <-> lookout with no gaps.
- Plates, pieces, doors, chests, and all other data: identical (deep diff).

## Verification (real engine, headless Chrome)
- Walked, through the real input path: up the ground west flight to the
  balcony, across the corridor, down the east flight (floor never changed);
  ground -> NW tower stairs -> spiral back down to ground; corridor -> NE
  tower stairs -> spiral up to the second floor; second-floor flights up
  and down (floor never changed); second floor -> NW tower -> Floor II ->
  Floor I -> ground, closing the full loop. Regression legs all pass:
  dungeon hatch round trip, kitchen door in/out, main-door exit.
- The castle selftest reads 73/74. The one FAIL is the test harness itself:
  its chest test teleports the hero to a random "far" spot, which now lands
  on the new NE tower stairs — he goes up the tower mid-test (the trigger
  working as designed) and the next chest's search runs in the wrong area.
  Proven by instrumented run (hero found in tower1_ne) and by the affected
  barracks chest passing its full test in isolation. No gameplay impact:
  players don't teleport.

## The build
Castle_TowerStairs_REMY.html (this folder), md5 fa94ec9ab728a621b29069c10dfdf046.
Village side byte-identical to the swap build outside the castle. Live
Pages root untouched — goes live only on Michael's say-so.
