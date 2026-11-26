# Research — Zelda's Health Systems (Zelda I & Zelda II)

Investigated 2026-11-26 at Michael's direction, for THE LEGEND OF
SILKA's health/magic design (see SYSTEMS.md). Sources: the NES
manuals (archive.org), Zelda Dungeon and Zelda Central mechanics
pages, GameFAQs data guides (TConnolly; TheStarbird), and Frame
Advance's code-level analysis of the ROM.

## Zelda II — The Adventure of Link (the deep one)

**The meter.** Link is the only hero in the series whose life is
square blocks, not hearts. He starts with **4 life bars and 4 magic
bars**. Four Heart Containers and four Magic Containers are hidden
in the world; maximum is **8 bars of each**. Guides count **16
points per bar**: 64 HP at the start, 128 HP at full growth. (The
ROM tracks the same tables at twice that resolution — 32 units per
bar — which is why code-level sources quote doubled spell costs.
Same tables, finer grain.)

**Damage is a table, not a formula.** Every enemy carries a damage
code, 0–7. A hit looks up code × Link's LIFE level (1–8) in an 8×8
table:

- Code 0 (weakest): 16 points at LIFE 1 → 4 points at LIFE 8.
- Code 6: 224 points at LIFE 1 → 80 at LIFE 8 — more than the whole
  starting meter. Late-game hits are meant to terrify.
- Code 7: 255 at every level — the instant-death class (lava, pits).

**SHIELD halves** whatever the table says, for one screen.

**The LIFE spell restores exactly 3 bars (48 points)** — never a
full heal — and it is expensive: 70 magic at MAGIC levels 1–2,
falling to ~50 by level 5. Healing in Zelda II is rationed by
design; you cannot tank and top up forever.

**Leveling is also healing.** Raising LIFE refills the life meter
to full; raising MAGIC refills the magic meter. A level-up at the
right moment is a potion.

**Experience.** Three tracks, three prices — LIFE is cheap, MAGIC
is mid, ATTACK is dear (NES table):

| Level | LIFE | MAGIC | ATTACK |
|---|---|---|---|
| 2 | 50 | 100 | 200 |
| 3 | 150 | 300 | 500 |
| 4 | 400 | 700 | 1,000 |
| 5 | 800 | 1,200 | 2,000 |
| 6 | 1,500 | 2,200 | 3,000 |
| 7 | 2,500 | 3,500 | 5,000 |
| 8 | 4,000 | 6,000 | 8,000 |

- You may **cancel** a level-up and keep banking points toward a
  different track. Spending resets the counter to zero.
- **Placing a palace crystal tops your EXP up to the next
  threshold automatically** — every palace guarantees a level.
- Some enemies **steal** what you carry: Bubbles drain EXP and
  magic on touch; several flyers strip unspent EXP.

**Death and lives.** Three lives to start. A life is lost when the
meter empties *or* Link falls into water, lava, or a pit — and he
respawns at the **start of the current screen**, not at a distant
checkpoint. Game over sends him back to the North Castle (the
sleeping Zelda's palace), **keeping every level, spell, and item —
but all unspent EXP is lost.** Six hidden Link dolls grant extra
lives; once all three stats are maxed, every 9,000 EXP buys another.

**Restoration is people, split in two.** In towns, the young women
in **red restore life**; the older women in **orange restore
magic**. A fairy restores life completely. A blue magic jar
restores one bar of magic; a red jar restores it all.

**Spell costs fall as MAGIC rises** (points, by MAGIC level 1→8):
Shield 32→16 · Jump 48→8 · Life 70→50 · Fairy 80→40 · Fire 120→16 ·
Reflect 120→16 · Spell 120→16 · Thunder 120→64. FIRE's collapse
from 120 to 16 is the steepest curve in the game — a spell that is
a boss-killer's luxury at level 1 becomes a habit at level 8.

## Zelda I — The Legend of Zelda (the ancestor)

- **3 hearts to start, halves are the smallest unit, 16 hearts
  maximum** — 8 containers from dungeon bosses, 5 hidden in the
  overworld.
- Enemy damage comes from a per-enemy table: of 93 entries, 30 deal
  ½ heart, 24 deal 1 heart, 18 deal 2 hearts, 3 deal 4 hearts.
- **The rings are Zelda I's Shield:** the Blue Ring halves all
  damage; the Red Ring quarters it. Permanent equipment, not a
  spell — the same mercy, worn instead of cast.
- Recovery: a dropped heart restores 1; a rescued **fairy restores
  3 hearts**; a Great Fairy's spring restores all; the **Water of
  Life** restores all — blue potion once, red potion twice (it
  turns blue after the first drink).
- Death: Continue restarts Link with **exactly 3 hearts filled**,
  possessions kept, at the overworld start or the dungeon door.

## What this means for Silka (folded into SYSTEMS.md)

1. Damage as an 8×8 table (enemy code × LIFE level), not a formula.
2. MEND restores exactly 3 blocks — healing is rationed.
3. Leveling LIFE or MAGIC refills that meter — growth is mercy.
4. Securing a palace's **Emerald tops EXP to the next level** —
   Zelda II's crystal rule, wearing our canon.
5. Restoration split between two people, Zelda II town law:
   Winnie restores life; the temple restores magic.
6. Game over keeps levels/spells/items but **unspent EXP is
   lost** — the one sting that makes banking a gamble.
7. HUSK (our Shield) halves table damage for one area; Zelda I's
   rings stand as the alternative — a found treasure that halves
   forever. Michael's pick, flagged in SYSTEMS.md.

> **Superseded in part by Michael's ruling, 2026-11-26:** Silka
> has **no lives and no blocks** — hearts only, 3 containers to
> start, growth by Pieces of Heart and whole containers in special
> places, and saving by milestone save points plus pause-and-save.
> Item 6's game-over sting therefore does not carry into Silka;
> death returns him to his last save. The Zelda facts above stand
> as researched; SYSTEMS.md carries the game as ruled.
