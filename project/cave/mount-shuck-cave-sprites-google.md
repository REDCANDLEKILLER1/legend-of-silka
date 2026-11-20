# Mount Shuck Cavern — 16×16 Sprite Pack (Google, relayed by Michael 2026-11-18)

Source: Google (Gemini), relayed verbatim. Matrices are 16×16, drawn with the
shared CAVERN_PALETTE, meant for the same bakeHeroSprite(rows, palette) helper
used for Corn Man in the planning chat. Filed for the cave build; the bake
check happens when the cave is built.

## Shared palette

```js
const CAVERN_PALETTE = {
  K: '#0B0C10', // Pitch-black cave void / shadow / chasm
  D: '#3B281E', // Deep mountain rock shadow
  R: '#6E4A36', // Main mountain cliff rock
  L: '#9E6E4C', // Sunlit rock highlight / wood grain
  W: '#7A4424', // Chest wood / ladder rails
  Y: '#FFD21E', // Gold trim / lock / map scroll / torch core
  O: '#FF7B1C', // Torch outer flame / amber glow
  S: '#636B78', // Stone stair / boulder shadow
  T: '#9BA4B2', // Stone stair / boulder highlight
  C: '#32A852'  // Map emerald seal / moss accent
};
```

## 1. Overworld Cave Mouth (X — carved into cliff face)

```
LLLLRRRRRRRRLLLL
LLRRRRKKKKKKRRLL
LRRRKKKKKKKKKKRL
LRRKKKKKKKKKKKKL
RRKKKKKKKKKKKKKK
RRKKKKKKKKKKKKKK
RDKKKKKKKKKKKKDR
RDKKKKKKKKKKKKDR
RDKKKKKKKKKKKKDR
RDKKKKKKKKKKKKDR
RDKKKKKKKKKKKKDR
RDKKKKKKKKKKKKDR
RDKKKKKKKKKKKKDR
DDKKKKKKKKKKKKDD
DDTTTTTTTTTTTTDD
DDDDDDDDDDDDDDDD
```

## 2. Treasure Chest — Closed (CHEST_CLOSED)

```
................
................
..KKKKKKKKKKKK..
.KYYYYYYYYYYYYK.
.KYLLLLLLLLLLYK.
.KYWWWWWWWWWWYK.
.KYYYYYYYYYYYYK.
.KYWWWWKKWWWWYK.
.KYWWWWYYWWWWYK.
.KYWWWWKKWWWWYK.
.KYWWWWWWWWWWYK.
.KYDDDDDDDDDDYK.
.KYYYYYYYYYYYYK.
..KKKKKKKKKKKK..
...KKKKKKKKKK...
................
```

## 3. Treasure Chest — Open (CHEST_OPEN)

```
..KKKKKKKKKKKK..
.KYYYYYYYYYYYYK.
.KYDDDDDDDDDDYK.
.KYYYYYYYYYYYYK.
.KKKKKKKKKKKKKK.
.KYKKKKKKKKKKYK.
.KYKKKKKKKKKKYK.
.KYYYYYYYYYYYYK.
.KYWWWWWWWWWWYK.
.KYWWWWWWWWWWYK.
.KYDDDDDDDDDDYK.
.KYYYYYYYYYYYYK.
..KKKKKKKKKKKK..
...KKKKKKKKKK...
................
................
```

## 4. Ascent Ladder / Stone Stairs to L9 (U)

```
KKKTTTTTTTTTTKKK
KKTYYYYYYYYYYTKK
KKTWWKKKKKKWWTKK
KKTWWYYYYYYWWTKK
KKTWWKKKKKKWWTKK
KKTWWYYYYYYWWTKK
KKTWWKKKKKKWWTKK
KKTWWYYYYYYWWTKK
KKTWWKKKKKKWWTKK
KKTWWYYYYYYWWTKK
KKTWWKKKKKKWWTKK
KKTWWYYYYYYWWTKK
KKTWWKKKKKKWWTKK
KKTWWYYYYYYWWTKK
KKSTTTTTTTTTTSKK
KKKKKKKKKKKKKKKK
```

## 5. Cave Map Pedestal (M)

```
................
...KKKKKKKKKK...
..KYYYYYYYYYYK..
..KYLLLLLLLLYK..
..KYLCCLLLLLYK..
..KYLLCCLLYYYK..
..KYLLLLLLLLYK..
..KYYYYYYYYYYK..
...KKTTTTTTKK...
....KSSSSSSK....
....KSTTTTSK....
....KSSSSSSK....
...KKTTTTTTKK...
..KSSSSSSSSSSK..
..KKKKKKKKKKKK..
................
```

## 6. Pushable Boulder (BOULDER)

```
................
....KKKKKKKK....
...KTTTTTTTTK...
..KTSSSSSSSSSK..
.KTSSSTTTTSSSSK.
.KTSSSSSSSSSSSK.
.KSSSSSSSSSSSSK.
.KSSSDDDDDDSSSK.
.KSSSSSSSSSSSSK.
.KDDDDDDDDDDDDK.
..KDDDDDDDDDDK..
...KKKKKKKKKK...
....KKKKKKKK....
................
................
................
```

## 7. Wall Torch / Brazier (TORCH_FRAME_1 — flip O/Y columns for frame 2)

```
.......OO.......
......OOOO......
.....OOYYOO.....
.....OOYYOO.....
......OOOO......
....KKKKKKKK....
...KTTTTTTTTK...
...KSSSSSSSSK...
....KKTTTTKK....
......KSSK......
......KSSK......
.....KTTTTK.....
.....KKKKKK.....
................
................
................
```
