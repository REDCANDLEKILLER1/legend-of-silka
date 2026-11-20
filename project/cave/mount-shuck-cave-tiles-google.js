/**
 * Complete 16x16 Cavern Tile & Prop Sprite Kit for Remy
 * All matrices are 16x16 and share CAVERN_MASTER_PALETTE.
 *
 * SOURCE: Google (Gemini), relayed by Michael 2026-11-18 22:45.
 * Saved verbatim. NOTE: this kit's palette is purple-basalt, DIFFERENT from
 * the first prop pack's brown palette (mount-shuck-cave-sprites-google.md) —
 * the two must be unified at build time (Remy's note, not Google's).
 */

const CAVERN_MASTER_PALETTE = {
  K: '#0B0C10', // Pitch-black abyss / outlines / deep shaft
  D: '#2B2233', // Deep basalt shadow / floor mortar
  R: '#564566', // Mid cavern rock / flagstone base
  L: '#88739E', // Lit stone highlight / bevel rim
  W: '#7A4424', // Wooden ladder rails / bridge timber
  B: '#B36B36', // Light wood grain highlight
  Y: '#FFD21E', // Reserved gold (rungs, chest trim, kernel pickup)
  O: '#FF7B1C', // Torch flame / warm amber ore glint
  C: '#2EC4B6', // Glowing subterranean crystal / water seep
  G: '#3D8E33'  // Cavern moss / kernel husk accent
};

const CAVERN_SPRITES = {
  // 1. LADDER GOING UP (H_UP) — Wooden rungs ascending into sunlit shaft
  LADDER_UP: [
    "KKKLLLLLLLLLLKKK",
    "KKLYYYYYYYYYYLKK",
    "KKLWWKKKKKKWWLKK",
    "KKLWWBBBBBBWWLKK",
    "KKLWWKKKKKKWWLKK",
    "KKLWWBBBBBBWWLKK",
    "KKLWWKKKKKKWWLKK",
    "KKLWWBBBBBBWWLKK",
    "KKLWWKKKKKKWWLKK",
    "KKLWWBBBBBBWWLKK",
    "KKLWWKKKKKKWWLKK",
    "KKLWWBBBBBBWWLKK",
    "KKLWWKKKKKKWWLKK",
    "KKLWWBBBBBBWWLKK",
    "KKDRRRRRRRRRRDKK",
    "KKKKKKKKKKKKKKKK"
  ],

  // 2. LADDER GOING DOWN (H_DOWN) — Floor hatch descending into dark pit
  LADDER_DOWN: [
    "KKKKKKKKKKKKKKKK",
    "KLLLLLLLLLLLLLLK",
    "KLRRRRRRRRRRRRLK",
    "KLRDDDDDDDDDDRLK",
    "KLRDWWBBBBWWDRLK",
    "KLRDWWKKKKWWDRLK",
    "KLRDWWBBBBWWDRLK",
    "KLRDWWKKKKWWDRLK",
    "KLRDWWBBBBWWDRLK",
    "KLRDWWKKKKWWDRLK",
    "KLRDWWBBBBWWDRLK",
    "KLRDWWKKKKWWDRLK",
    "KLRDDDDDDDDDDRLK",
    "KLRRRRRRRRRRRRLK",
    "KDDDDDDDDDDDDDDK",
    "KKKKKKKKKKKKKKKK"
  ],

  // 3. CAVERN FLAGSTONE FLOOR ('.') — Subtle low-contrast stone so sprites pop
  FLOOR_STONE: [
    "RRRRRRRRRRRRRRRR",
    "RRRRRRRRRRRRRRDR",
    "RRRRRRRRRRRRRRDR",
    "RRRRRRRRRRRRRRDR",
    "RRRRRRRRRRRRRRDR",
    "RRRRRRRRRRRRRRDR",
    "RRRRRRRRRRRRRRDR",
    "DDDDDDDDDDDDDDDD",
    "RRRRRRDRRRRRRRRR",
    "RRRRRRDRRRRRRRRR",
    "RRRRRRDRRRRRRRRR",
    "RRRRRRDRRRRRRRRR",
    "RRRRRRDRRRRRRRRR",
    "RRRRRRDRRRRRRRRR",
    "RRRRRRDRRRRRRRRR",
    "DDDDDDDDDDDDDDDD"
  ],

  // 4. SOLID BASALT WALL ('#') — Chunky 8-bit beveled rock face
  WALL_ROCK: [
    "LLLLLLLLLLLLLLLD",
    "LRRRRRRRRRRRRRRD",
    "LRLLLLLLRRRRRRRD",
    "LRLLLLRRRRRRRRRD",
    "LRRRRRRRRRDDDDDD",
    "LRRRRRRRDDDDDDLD",
    "DDDDDDDDLLRRRRRD",
    "LLLLLLLLLRRRRRRD",
    "LRRRRRRRRRRRRRRD",
    "LRRRRRRLLLLRRRRD",
    "LRRRRRRRRRRRRRRD",
    "LRRRDDDDDDDDDDLD",
    "DDDDLLLLLLLLLLLD",
    "LLLLRRRRRRRRRRRD",
    "LRRRRRRRRRRRRRRD",
    "DDDDDDDDDDDDDDDD"
  ],

  // 5. BEVELED CORNER ROCK ('/' & '\\' — Flip horizontally for '\\')
  WALL_BEVEL_NW: [
    "LLLLLLLLLLLLLLLD",
    "LRRRRRRRRRRRRRRD",
    "LRLLLLLLRRRRRRRD",
    "LRRRRRRRRRRRRRRD",
    "LRRRRRRRRRDDDDDD",
    "LRRRRRRRDDDDKKKK",
    "DDDDDDDDLLDDKKKK",
    "LLLLLLLLRRDKKKKK",
    "LRRRRRRRRDKKKKKK",
    "LRRRRRRRDKKKKKKK",
    "LRRRRRRDKKKKKKKK",
    "LRRRRRDKKKKKKKKK",
    "DDDDDDKKKKKKKKKK",
    "LLLLDKKKKKKKKKKK",
    "LRRDKKKKKKKKKKKK",
    "DDKKKKKKKKKKKKKK"
  ],

  // 6. STONE CHASM BRIDGE ('=') — Planked stone span over pitch-black abyss
  CHASM_BRIDGE: [
    "KKKKKKKKKKKKKKKK",
    "KKKKKKKKKKKKKKKK",
    "LLLLLLLLLLLLLLLL",
    "BBBBBBBBBBBBBBBB",
    "WWWWWWWWWWWWWWWW",
    "DDDDDDDDDDDDDDDD",
    "LLLLLLLLLLLLLLLL",
    "BBBBBBBBBBBBBBBB",
    "WWWWWWWWWWWWWWWW",
    "DDDDDDDDDDDDDDDD",
    "LLLLLLLLLLLLLLLL",
    "BBBBBBBBBBBBBBBB",
    "WWWWWWWWWWWWWWWW",
    "DDDDDDDDDDDDDDDD",
    "KKKKKKKKKKKKKKKK",
    "KKKKKKKKKKKKKKKK"
  ],

  // 7. CRACKED BOMBABLE WALL — Subtle fissure tell for hidden pockets
  WALL_CRACKED: [
    "LLLLLLLLLLLLLLLD",
    "LRRRRRRRRRRRRRRD",
    "LRLLLLLLRRRRRRRD",
    "LRRRRRRKRRRRRRRD",
    "LRRRRRKKRRDDDDDD",
    "LRRRRKKKDDDDDDLD",
    "DDDDDDKKLLRRRRRD",
    "LLLLLLKKKRRRRRRD",
    "LRRRRRRKKRRRRRRD",
    "LRRRRRKKKLLRRRRD",
    "LRRRRKKKRRRRRRRD",
    "LRRRKKDDDDDDDDLD",
    "DDDDKKLLLLLLLLLD",
    "LLLLKKRRRRRRRRRD",
    "LRRRRKRRRRRRRRRD",
    "DDDDDDDDDDDDDDDD"
  ],

  // 8. GLOWING CRYSTAL / ORE VEIN (Environmental landmark for dead-end bubbles)
  CRYSTAL_CLUSTER: [
    "................",
    ".......KK.......",
    "......KCCK......",
    ".....KCCCCK.....",
    ".....KCLCCK.....",
    "....KKCCCCKK....",
    "...KCCKCCKCCK...",
    "..KCCCKCCKCCCK..",
    "..KCLCKCCKCLCK..",
    "..KCCCKCCKCCCK..",
    "..KCCCKCCKCCCK..",
    ".KKCCCKCCKCCCKK.",
    "KDDDDDDDDDDDDDDK",
    "KRRRRRRRRRRRRRRK",
    ".KKKKKKKKKKKKKK.",
    "................"
  ],

  // 9. STALAGMITE / ROCK SPIRE (Decorates wide cavern bubbles)
  STALAGMITE: [
    "................",
    ".......KK.......",
    "......KLLK......",
    "......KLRK......",
    ".....KLLRRK.....",
    ".....KLRRRK.....",
    "....KLLRRRRK....",
    "....KLRRRRRK....",
    "...KLLRRRRRRK...",
    "...KLRRRDRRRK...",
    "..KLLRRRRDRRRK..",
    "..KLRRRRRDRRRK..",
    ".KLLRRRRRRDRRRK.",
    "KDDDDDDDDDDDDDDK",
    ".KKKKKKKKKKKKKK.",
    "................"
  ],

  // 10. GOLDEN KERNEL PICKUP (Chest reward / health & courage boost)
  GOLDEN_KERNEL: [
    "................",
    ".......KK.......",
    "......KGGK......",
    ".....KGYYGK.....",
    "....KYYYYYYK....",
    "....KYLYYYYK....",
    "...KYYYYYYYYK...",
    "...KYLYYYYYYK...",
    "...KYYYYYYYYK...",
    "...KYYYYYYYYK...",
    "....KYYYYYYK....",
    "....KYYYYYYK....",
    ".....KYYYYK.....",
    "......KKKK......",
    ".......KK.......",
    "................"
  ]
};

module.exports = { CAVERN_MASTER_PALETTE, CAVERN_SPRITES };
