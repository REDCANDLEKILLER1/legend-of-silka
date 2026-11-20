# Mount Shuck Cavern — the cave package, in order

Status (Michael, 2026-11-18 22:47): Google's cave materials are KEEPERS.
This cavern is **the cave before the boss** — the underworld under Mount
Shuck that the player crosses to reach Level 9 / the black castle.
Nothing here is in the game yet; the build waits for Michael's word.

## The design (Michael's rulings, 2026-11-18 evening)
- Cave mouth at the dead-end branch west of L9 (his red X) — the secret
  there is MANDATORY: skip it and you can't enter L9.
- The Eye Towers guard the surface stem (his two blue dots); the surface
  is impassable, so the underworld is the road.
- The same winding-carve pattern makes the caves as made the surface paths.
- The cave comes up at L9 — into the black castle, which is a HUGE level
  of its own (the cave is before the boss, not instead of the castle).

## Files, in order
1. `mount-shuck-cave-google.js` + `mount-shuck-cave-google.png`
   Google's first draft: a hand-drawn 6-room blueprint. PRETTY, DOESN'T
   WALK — its own harness fails (entrance sealed by its own torches;
   columns barely connect; 8 chests, not 7). Kept as the visual idea.
2. `mount-shuck-cave-gen-google.js` + `mount-shuck-cave-gen.png`
   Google's multi-floor GENERATOR (4 floors, ladders, false hall,
   drop-pocket). COLD TEST PASS: deterministic; verifier passes seeds
   1337/42/7/2026 — entry -> map -> 7 chests -> L9 stairs. Paste repairs
   (3, mechanical) are marked in its header. THIS is the keeper engine.
3. `mount-shuck-cave-sprites-google.md` + `mount-shuck-cave-sprites.png`
   Prop pack 1 (brown palette): cave mouth, chests, ascent ladder,
   map pedestal, boulder, torch. All matrices clean 16x16.
4. `mount-shuck-cave-tiles-google.js` + `mount-shuck-cave-tiles.png`
   Tile kit (PURPLE palette): up/down ladders, floor, walls, bevel,
   bridge, cracked wall, crystal, stalagmite, golden kernel. All clean.

5. `mount-shuck-cave-lighting-google.js` + `mount-shuck-cave-lighting.png`
   Candle sprites (2 frames) + dynamic torchlight renderer (darkness
   mask, per-candle flicker phase, warm amber pass). Syntax-checked;
   frames clean 16x16. Numbers tuned for 256x192 — scale radii to
   Corn's 48px tiles at build. The pattern is sound.

## Open joints for build day
- UNIFY THE PALETTES: pack 1 is brown, the tile kit is purple. One wins.
- The ascent lands in a "sanctum" in Google's drafts — per Michael it
  should land in the black castle, with the castle still to cross.
- Enemies in the cave: Google's drafts have none (pure navigation).
  Undecided — cave critters are Michael's call.
- The mandatory secret's identity (weapon / heart / other) and what
  gates reaching the cave until later: Michael's to name.
