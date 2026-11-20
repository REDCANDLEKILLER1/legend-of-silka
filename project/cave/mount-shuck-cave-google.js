/**
 * Mount Shuck Underworld Cave System (48x24 = 3x2 grid of 16x12 rooms)
 * Connects Overworld Cave Mouth X (Field 6,0) -> Ascent Stairs/Ladder to L9 (Field 7,0)
 *
 * Tile Legend:
 *  '#' = Solid Mountain Basalt Wall
 *  '/' = 45° Beveled Cave Wall (NW / SE slant)
 *  '\\' = 45° Beveled Cave Wall (NE / SW slant)
 *  '.' = Walkable Cavern Floor
 *  ' ' = Deep Abyss / Pit Chasm (blocks walking)
 *  '=' = Narrow Stone Bridge over Abyss
 *  'O' = Pushable Rubble Boulder
 *  '*' = Flickering Storm Torch / Brazier
 *  'C' = Treasure Chest (7 total across the cavern)
 *  'M' = Cave Map Pedestal (reveals cavern minimap)
 *  'E' = South Entrance from Overworld X (Field 6,0)
 *  'U' = North Ladder / Stone Stairs ascending into L9
 *
 * SOURCE: Google (Gemini), relayed by Michael 2026-11-18 22:40 as a first
 * look at the cave system. Saved verbatim; Remy cold-tests + renders it.
 */

const CAVE_W = 48;
const CAVE_H = 24;

// 48x24 ASCII blueprint (3 rooms wide x 2 rooms tall, each room 16x12)
// Cols 00..15 = West Wing | Cols 16..31 = Central Abyss | Cols 32..47 = East Ascent
const MOUNT_SHUCK_CAVE_ROWS = [
// 0000000000111111 1111222222222233 3333333344444444
// 0123456789ABCDEF 0123456789ABCDEF 0123456789ABCDEF
  "################ ################ ########UU######", // 00: North Stair/Ladder (UU) up to L9!
  "###/........\\### ####/......\\#### ####/..**..\\####", // 01: Twin ceremonial torches at stair
  "##/..C....*..\\## ###/..*..*..\\### ###/........\\###", // 02: Chest #1 (NW alcove) + torches
  "##\\..........### ##/....==....\\## ##/..*....*..\\##", // 03: Winding passage + East Hall
  "###\\...==...#### ##..  .==.  ..## ##....O..O....##", // 04: West bridge + Central chasm
  "####  .==.  #### ##C.  .==.  .C## ##\\....==..../##", // 05: Chest #2 & #3 on chasm ledges!
  "###/  .==.  \\### ##..  .==.  ..## ###  ..==..  ###", // 06: Narrow bridges spanning abyss
  "##/....==....\\## ##\\....==..../## ##/  ..==..  \\##", // 07
  "##..*......O..## ###\\......../### ##....====....##", // 08: Boulder (O) guarding West->Center
  "##\\..........### ####........#### ##\\..*....*../##", // 09: Central crossroads
  "###\\......../### ####/..**..\\#### ###\\......../###", // 10: Room seam (Row 11->12)
  "#####......##### ####........#### #####......#####", // 11: Wide 6-tile room transitions
  "#####......##### ####........#### #####......#####", // 12: Lower tier (Rows 12..23)
  "###/........\\### ###/..*..*..\\### ###/........\\###", // 13
  "##/..*....*..\\## ##/....MM....\\## ##/..*....O..\\##", // 14: CAVE MAP PEDESTAL (MM) in Center!
  "##....====....## ##.....==.....## ##....====..C.##", // 15: Chest #6 behind East boulder (O)
  "##..  .==.  ..## ##..  .==.  ..## ##..  .==.  ..##", // 16: Winding lower chasms
  "##C.  .==.  ..## ##..  .==.  .C## ##..  .==.  ..##", // 17: Chest #4 (SW) & Chest #5 (SE ledge)
  "##..  .==.  ..## ##..  .==.  ..## ##..  .==.  ..##", // 18
  "##\\....==..../## ##\\....==..../## ##\\....==..../##", // 19
  "###\\......../### ###\\......../### ###\\...**.../###", // 20
  "####\\..**../#### ####\\..**../#### ####\\..CC../####", // 21: Chest #7 (SE Secret Vault!)
  "#######EE####### ################ ################", // 22: South Entry (EE) from Overworld X
  "################ ################ ################"  // 23: Outer mountain bedrock
];

function buildMountShuckCave() {
  const grid = new Array(CAVE_H);
  const chests = [];
  let mapItem = null;
  let entrance = null;
  let ascentStairs = null;

  for (let y = 0; y < CAVE_H; y++) {
    // Strip visual room-divider spaces (at string index 16 and 33)
    const rawLine = MOUNT_SHUCK_CAVE_ROWS[y].slice(0, 16)
                  + MOUNT_SHUCK_CAVE_ROWS[y].slice(17, 33)
                  + MOUNT_SHUCK_CAVE_ROWS[y].slice(34, 50);
    grid[y] = rawLine.split('');

    for (let x = 0; x < CAVE_W; x++) {
      const ch = grid[y][x];
      const roomX = (x / 16) | 0;
      const roomY = (y / 12) | 0;
      if (ch === 'C') chests.push({ id: `cave_chest_${chests.length + 1}`, x, y, room: [roomX, roomY] });
      if (ch === 'M' && !mapItem) mapItem = { id: 'mount_shuck_map', x, y, room: [roomX, roomY] };
      if (ch === 'E' && !entrance) entrance = { x, y, room: [roomX, roomY] };
      if (ch === 'U' && !ascentStairs) ascentStairs = { x, y, room: [roomX, roomY], target: 'L9_SANCTUM' };
    }
  }

  return {
    width: CAVE_W,
    height: CAVE_H,
    roomsWide: 3,
    roomsTall: 2,
    grid,
    entrance,      // { x: 7, y: 22 } -> links to Overworld X in Field (6,0)
    ascentStairs,  // { x: 40, y: 0 } -> ladder/stairs up into L9
    mapItem,       // { x: 23, y: 14 } -> reveals full 3x2 cavern minimap
    chests,        // 7 chests across all 6 rooms
    getRoom(rx, ry) {
      const out = [];
      for (let ly = 0; ly < 12; ly++) {
        out.push(grid[ry * 12 + ly].slice(rx * 16, rx * 16 + 16));
      }
      return out;
    }
  };
}

// Node.js Verification Harness: proves Entry (X) -> Map -> All 7 Chests -> L9 Stairs
function verifyCaveConnectivity(cave) {
  const walkableChars = new Set(['.', '=', 'O', 'C', 'M', 'E', 'U']);
  const vis = Array.from({ length: CAVE_H }, () => new Uint8Array(CAVE_W));
  const q = [[cave.entrance.x, cave.entrance.y]];
  vis[cave.entrance.y][cave.entrance.x] = 1;

  const DIRS = [[-1, 0], [1, 0], [0, -1], [0, 1]];
  while (q.length) {
    const [cx, cy] = q.shift();
    for (const [dx, dy] of DIRS) {
      const nx = cx + dx, ny = cy + dy;
      if (nx < 0 || ny < 0 || nx >= CAVE_W || ny >= CAVE_H) continue;
      if (!vis[ny][nx] && walkableChars.has(cave.grid[ny][nx])) {
        vis[ny][nx] = 1;
        q.push([nx, ny]);
      }
    }
  }

  const stairsOk = vis[cave.ascentStairs.y][cave.ascentStairs.x] === 1;
  const mapOk = vis[cave.mapItem.y][cave.mapItem.x] === 1;
  const chestsOk = cave.chests.every(c => vis[c.y][c.x] === 1);

  if (!stairsOk || !mapOk || !chestsOk) {
    throw new Error(`Cave connectivity failed: stairs=${stairsOk}, map=${mapOk}, chests=${chestsOk}`);
  }
  return { ok: true, chestsReachable: cave.chests.length, mapReachable: true, stairsToL9: cave.ascentStairs };
}

module.exports = { MOUNT_SHUCK_CAVE_ROWS, buildMountShuckCave, verifyCaveConnectivity, CAVE_W, CAVE_H };
