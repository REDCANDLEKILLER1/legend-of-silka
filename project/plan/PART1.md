# PART ONE — "The Feast and the Telling" (locked 2026-11-20, Michael's word)

## THE GAME'S NAME (Michael, 2026-11-20 09:02 CST)
**THE LEGEND OF SILKA** — subtitle: **The Adventure of CornMan.**
His logic, verbatim in substance: "Zelda was the princess, so it's the
legend of whatever the princess's name is." The princess is Silka, so
the game carries her name; CornMan carries the adventures line.
(The project folder keeps its working label `black-castle-game`.)
CANON SPELLING (Michael, 2026-11-20 09:04 CST): the hero is **CornMan**
— ONE word, cap C cap M, same pattern as XRPMan. Never "Corn Man".
Supersedes the "THE BLACK CASTLE" working title on the title screen.

Michael's direction: finish the first part, best I can, no check-ins —
he playtests when it's set up. Structure follows his own words:
"you play as one character, you play as another character, and then
you watch."

## The shape
1. TITLE — new key art, NO characters (Michael: the old cover made the
   hero look like "a version of Zelda with a corn hat"). Working title
   on screen: THE BLACK CASTLE — Part One. Title music: the main theme
   he already gave us (music/main-theme.mp3). Remembered, standing.
2. ACT 1 — PLAY as young Pearl at the harvest feast (King's castle,
   feast hall). Walk, talk, run one small errand of the feast. The talk
   plants the secret: the sealed Great Barn, the towers in the north
   nobody passes. Ends as the light changes — crows at the windows.
3. CARD — "A hundred harvests later."
4. ACT 2 — PLAY as CornMan. He walks in the village south gate on a
   quiet morning. Village is safe: talk to everyone, see the statue,
   the chapel, the overlook (the ruin is look-only). Objective: old
   Pearl's cottage, NW corner.
5. ACT 3 — WATCH: the Telling. At old Pearl's hearth she tells it, and
   the incident plays as her telling: crows first, the Storm Wizard's
   demand, Silka's refusal, the sleep and the taking in one motion,
   the King spending his last strength sealing the Great Barn, the
   land flinching. The reveal — where Silka sleeps, and the only way
   in is UNDER — lands with the secret chime.
6. END CARD — Part One complete. The road south, and the long road
   north, are Part Two's business.

## Rulings this build follows
- Whose feet at the feast: young Pearl (the witness) — Muse's lean,
  adopted by Michael's "whatever you said" + "just get it the best
  you can" (2026-11-20).
- Who takes Silka: the Storm Wizard, vanguard of the Blight King
  (the working two-tier frame).
- The King's death: told by Pearl in the Telling, never shown.
- Village = the ruled 32x24 standard (village-fixed.js data).
- Statue = the King himself recolored to stone (Michael's method).
- Sprites: King 16x24 + Wizard 24x32 standards from the archive;
  Silka / Pearl young+old / Eli / folk drawn to the same standard —
  the portrait debuts are the design anchors (Silka gold corn-silk
  hair, cream + silka red; Pearl's ONE white bead holds young to old,
  braid on the same shoulder).
- Music: title = main theme (his). Section themes REQUESTED from
  Michael (he makes them): feast, village morning, the Telling.
  Until they land, sections play silent rather than fake it.

## Files
- game/part1.html (+ game/sprites-data.js) — the playable build.
- art/title-keyart.webp — the new cover.

## SILKA + THE TITLE SCREEN (2026-11-20, Michael's picks)
- The princess is **Silka** — Michael's "Silk, maybe Silka with an A"
  (corn silk = her golden hair). Renamed everywhere; game title is now
  THE LEGEND OF SILKA. (Was Poppy until this morning.)
- Title screen rebuilt as ANIMATED PIXEL ART drawn in-engine
  (art/design_title_screen.py -> game/title-scene.js; proof render
  art/title-screen.png): Zelda 1 grammar — framed emblem over cliffs,
  animated waterfall, PUSH START, no Nintendo line — with a WRENCH
  under the name where a sword would sit. Two-tap start: first tap
  wakes the title music, second tap / A begins. The painted key art
  still backs the Part One Complete card.

## TITLE GRAPHICS — CORRECTED (Michael, 2026-11-20 09:25 CST)
Michael rejected the 8-bit canvas title: "we are in the future, go
16-bit or something." The HD title is the standard now:
art/title-screen-hd.jpg — generated 16-bit valley art (castle, eye
tower, waterfall, corn) + emblem composited in PIL
(art/composite_title_hd.py): gold SILKA, the wrench, adventure line
inside a leaf-framed plaque; PUSH START blinks live in-game over a
slow zoom. The 8-bit canvas version (title-scene.js /
art/title-screen.png) is SUPERSEDED — kept on file as a draft only.

## TITLE ART — MICHAEL'S VERSION IS THE STANDARD (2026-11-20 09:36 CST)
Michael supplied the final title art himself (art/title-screen-final.png):
ornate gold emblem, emerald-set double wrench, PUSH START in its own
plaque. It supersedes both of Muse's title builds. At his word the
same morning it is ANIMATED in-game: 4 pre-rendered frames cycle at
190ms (waterfall streaks + foam, river sparkles, a wind band moving
through the corn — art/build_title_frames.py) plus live overlays:
pulsing emerald glows on all seven gems, a breathing glow on the
PUSH START plaque, twinkling stars. Preview: art/title-animated-preview.gif.
