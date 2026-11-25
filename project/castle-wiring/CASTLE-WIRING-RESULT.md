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

## Correction (later that evening) — castle entry was broken, now fixed
The Castle_TowerStairs build above had a flaw Remy introduced at the embed
step: the castle document was packed into the village build with a plain
JSON string, which left literal "</script>" sequences inside it. The
browser cut the castle-door wiring script at the first one, so the door
never opened — you could not enter the castle at all in that build (nor in
the first back-fix copy, which inherited it). The original pipeline escaped
those sequences ("<\/script>"); the fix re-embeds the same castle document
with that escaping restored. Nothing else changed.
Current build: Castle_TowerStairs_BackFix_REMY.html (md5
6493c2c5f3d2048e48b83e9fbc613190) — new maps + tower wiring + CornMan's
back view fixed (below) + working entry. Verified in the real file: entered
through the actual castle-door trigger, walked the hall, exited back to
the village.

## CornMan's back view (Michael approved 2026-11-24)
The potted-plant back frames are replaced with the back row from Michael's
approved v3 sprite pack (green silk hair, red cape). Michael's verdict:
"I like the new back view — he did look like a potted plant for sure."
The plant question is closed.

## v2 (2026-11-24, later) — Michael's two playtest fixes
Castle_TowerStairs_v2_REMY.html (md5 0374d1297b3faa1d1c023d29e6688c2e)
supersedes the BackFix build. Michael, playing the BackFix build, reported:
1. "On the second floor you can't walk past this ribbon or banner" at BOTH
   flight tops. Measured: the passage through the balustrade line at each
   flight top was a 26px slot in feet terms — passable in tests, a wall on
   a phone drag. Widened both passages (paint-only, +1,608 mask cells) to
   a 49px channel centered on each flight.
2. Tower entrances teleported with no choice. Now every NW/NE tower
   entrance (ground and upper floors) opens a chooser with named
   destinations: "Up to NW/NE Tower · Floor I", "Up to the Throne Room",
   "Down to the Ground Floor". The tower spirals' upper-floor option is
   relabeled "Down to the Throne Room" to match.
Verified: full walk suite in the real build (all passages at three offsets
each, all four entrance choosers, tower loop, dungeon/kitchen/main-door
regressions), entry through the real castle-door trigger and exit back to
the village in the delivered file, and the castle selftest now reads
74/74 (the old chest-test artifact is gone — the random teleport that used
to trip it now opens a chooser instead of traveling mid-test).
