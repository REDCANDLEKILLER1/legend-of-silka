# ALIVENESS + FURNISHED ROOMS — work order (Michael's direction, 2026-11-20 10:39 CT)

Date: 2026-11-20
Project: THE LEGEND OF SILKA — Part One
Author: Muse (Remy)
Status: in build
Summary: Michael's ruling — characters look better but not right; sprites must
face all four directions and walk; NPCs must live, not stand; rooms must be
furnished like people live in them; fire must look like fire. "This is not a
half job." This file is the contract for the pass.

## Audit findings (measured in game/part1.html, 2026-11-20)
1. `e.dir` is tracked on every step but NEVER used when drawing — one front
   sprite is drawn for all directions. Walking backwards shows the face.
2. No walk frames exist. Movement is a 130 ms tile slide of a static image.
3. NPCs move only inside scripted cutscene paths. In free play nothing turns,
   wanders, or works. People stand like posts.
4. The cottage fireplace is ONE static tile: stacked orange/yellow rectangles
   (Michael: "stock market bars"). Hall candelabra flames are static blocks.
   The village fountain is one frozen frame.
5. Rooms are sparse: cottage = hearth, table, bed, rug and bare floor; the
   hall reads as tiles, not a feast in progress.

## The pass — requirements
### A. Directional sprites (study: research_notes/character-sprite-craft-20261120)
- Every cast member gets down / up / right views at 16x24, redrawn to the
  study's per-character specs (lit eyes for named cast, 3 tones per material,
  selective outline, curved hems, individual boots, one asymmetry each).
  Left = mirror of right (standard economy). King fixes must survive the
  STATUE_PAL swap. Wizard + crows untouched (settled standards).
- Walk frames derived per study §4.1: feet swap 1 px, arm counter-swing 1 px,
  engine bob 1 px on the walk frame. Idle = frame A.
- CornMan punch set (study §4.2, Michael's shoulder rule): anticipation →
  extension/smear → recover, right arm + left arm (front), side and back
  (right arm; left mirrored). Wired to the B button in free play.
- Engine: render selects sprite by e.dir + moving state; soft ground shadow
  under every grounded entity; NPCs turn to face the player when spoken to.

### B. Ambient life
- Every NPC gets an ambient profile: posts (guards) turn slowly; workers
  (folk, Eli) wander a small home area and turn; royalty turn in place.
  Ambient runs only in free play — never during dialogue or cutscenes —
  and respects collision and each other's tiles.
- Old Pearl turns between the hearth and the room. Village folk move around
  the plaza. Hall folk drift between the tables during the feast.

### C. Furnished rooms + real fire
- Cottage fireplace: 3-frame flame animation drawn as flame tongues (lit
  core, mid flame, deep tips, ember bed, logs, kettle on the centre tile) —
  no stacked-bar flames anywhere. Woodpile beside the hearth, a stocked
  shelf, a stool at the table.
- Hall: candelabra flames flicker (2 frames); banners and feast tables
  already placed stay; flames must move.
- Village fountain: 2-frame water (jet + sparkle shift).
- Animated tiles are frame arrays in the tile system; render picks by tick.

## Acceptance (before anything ships to Pages)
- Boot / smoke / camera harnesses pass on the new build.
- Lineup sheet: every character down/up/right at 1x and 4x on mid-grey and
  on the hall floor colour; black-fill sheet (nameable in <1 s); walk strip
  (CornMan, Silka, old Pearl cycling); punch strip for CornMan.
- Michael's verdict on the lineup + preview BEFORE the repo/Pages push —
  the standing lineup gate. Working-tree integration is not shipping.

## D. NPC minds (Michael, 2026-11-20 10:46 CT)
- People DO their jobs: routines tied to the room's props (the cook cooks in
  the kitchen, Pearl tends her hearth, the stonecutter works his stone).
  Ambient roam/turn (shipped in this pass) is the floor, not the ceiling —
  routines get prop-anchored work loops as each room is furnished.
- Dialogue is low-level smart, never one fixed line forever: repeat asks
  cycle phrasings, and later phrasings POINT you (to the cup, the dais, the
  cottage). Story beats stay scripted; small talk varies. DONE for Part One's
  ten repeat-talk spots via the cyc() helper — extend to every NPC as rooms
  are built. A real language-model layer is a later, bigger decision (cost,
  offline play, canon control) — the variation system is the honest first
  floor of it, not a fake of it.

## E. The castle is a real place (Michael, 2026-11-20 10:46 CT)
The King's castle is not one hall. On the build list as real, furnished,
walkable rooms (the fitted castle-grounds interior + upper floors are the
blueprint): throne room with the long red carpet (the feast hall IS this
room's heart — dais + carpet already in), KITCHEN (cook at work, hearth,
stores), DUNGEON below, royal chambers/archives above, and a TREASURE ROOM
kept secret for later. RULED (Michael, 2026-11-20 11:18 CT): the treasure
room STAYS A LATE SECRET — CornMan does not reach it early and does not
start with anything in hand from it. He starts flat and earns everything.

## F. Tiles — texture like Minecraft (Michael, 2026-11-20 10:47 CT)
- Every material textured; no flat stamped floors. Each much-repeated tile
  gets 3 textured variants chosen by position hash (same tile, same variant
  — texture, never shimmer). DONE this pass: hall stone floor, cottage wood
  floor, village dirt, village stone path (TILEVAR in part1.html).
- Extend variants to the remaining repeaters (grass, cliff, roofs, hall
  walls) as the tile pass continues, and every NEW room ships textured from
  the start.
