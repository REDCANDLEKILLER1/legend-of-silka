# CASTLE-PLAN.md — The King's Castle as a Real Place

Date: 2026-11-20
Project: THE LEGEND OF SILKA
Author: Muse (Remy)
Status: draft (ground floor built; dungeon + upper floors pending)
Summary: Michael's ruling (2026-11-20 10:46 CT) — a castle is a place, not a
backdrop: kitchen, dungeon, throne room with the long red carpet, treasure
room. This is the build contract for it. Treasure room RULED a late secret
(Michael, 2026-11-20 11:18 CT): CornMan never reaches it early.

## Ground floor — BUILT 2026-11-20 (scene 'castle', preview #castle)

Footprint: the fitted castle-grounds interior (50×36), spaces normalized to
walls. Walk-tested cold: 1,082 of 1,082 floor tiles reachable from the south
doors, zero dead tiles, all NPC routine loops connected.

Rooms:
- GREAT HALL (south, full width) — grand doors DD, guard on patrol.
- THRONE ROOM (north-center) — dais, statues, torches, the King and Silka at
  rest. THE LONG RED CARPET runs from the south doors up the great hall,
  across the cross-hall, and (north run) from the banquet hall's north edge
  to the dais itself.
- BANQUET HALL (center) — long tables, the feast's home room.
- LIBRARY (west, both ends) — shelves, a mason on an inspection loop.
- KITCHEN (east-north) — twin hearths (animated fire), work tables, stores;
  the COOK works a real routine: hearth → work table → shelves, pausing at
  each to face the work.
- PARLOR (east-south) — armchairs, quiet room.
- STORES / BARRACKS (west-south) — shelved stores and set tables.

Engine pieces shipped with this block:
- Routine system in ambient(): waypoint loops [x, y, faceDir, pauseMs];
  path blocked = wait and retry; runs only in free play.
- Castle tileset: carpet, banquet tables, shelves, statues, flickering wall
  torches, armchairs, animated hearths, work tables, barrels/sacks, stairs,
  grand doors. Floor uses the hall stone + its texture variants.

## The dungeon — BUILT 2026-11-20 (scene 'dungeon', preview #dungeon)

Authored 32×24. Entry chamber with the stairs, the jailer's post (he holds
keys for three cells and none for the vault), stores, a torch-lit corridor
the WARDEN patrols on a four-point loop, three LOCKED cells — empty for
years, scenery behind bars by design — a service crawlway behind the cells
to a forgotten broken cell (slip through its bent gate), and the vault
antechamber. At its south wall: THE VAULT DOOR — iron over oak, gold-banded,
examinable ("No keyhole on this side"). Sealed. Walk-tested cold: 266 of
266 open tiles reachable, zero dead; cell interiors sealed as designed.

## Next blocks (in order)

1. DOOR SYSTEM — generic scene doors (step on a door tile → fade → arrive),
   so the castle connects: feast hall ↔ castle wings, castle → dungeon,
   castle → 2F. Until then the scenes are entered by their # previews.
2. UPPER FLOORS — the fitted 2F/3F pack: royal chambers, archives; stairs S
   in the throne room and the east wing become real.
3. STORY HOOKUP — which act opens the castle doors to the player is a Part
   Two wiring decision; the rooms are built set-first so the story walks
   into a finished place.
4. Dedicated COOK sprite (she currently wears the orchard wife's proven
   sprite — same apron class; her own face is an art-pass item).

## Rules carried in

- Every room furnished and textured from the start (ALIVENESS-AND-ROOMS.md
  §§B/F); every NPC has a job and varied, pointing dialogue (§D).
- No room ships unwalked: BFS from the entry, zero dead tiles, routine
  loops proven connected before it goes live.
