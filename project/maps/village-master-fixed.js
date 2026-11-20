const MASTER_VILLAGE_ROWS = [
"######^^##########^^^^^^^^^^^^##########^^######",
"#####X##X########X############X########X##X#####",
"###==========================================###",
"##TT++++++++++++++++++++++++++++++++++++++++TT##",
"##TT..RRRRRh....++....b..b....++....hRRRRR..TT##",
"##....rrrrrr....++............++....rrrrrr....##",
"##....WWWWWW.!..++....f..f....++..!.WWWWWW....##",
"##....WWDWWW....++............++....WWDWWW....##",
"##......P.......++++++++++++++++......N.......##",
"CCCCCCCCCCCCCCCCSSSSCCCCCCCCCCCCSSSSCCCCCCCCCCCC",
"CCCCCCCCCCCCCCCCSSSSCCCCCCCCCCCCSSSSCCCCCCCCCCCC",
"##TT..f.........++++..ffff..++++.........f..TT##",
"##TT..........++++++ffffffff++++++..........TT##",
"##....*.....++++..ff..KKKK..ff..++++.....*....##",
"##..........++++..ff..KKKK..ff..++++..........##",
"##..........++++..ff..KKKK..ff..++++..........##",
"##..........++++++..u.++++.u..++++++..........##",
"##..RRRRRh......++++++....++++++......RRRRRh..##",
"##..rrrrrr..o...++++++....++++++...F..rrrrrr..##",
"##..WWWWWW..o...++....N..N....++...a..WWWWWW..##",
"##..WWDWWW..!.........................WWDWWW..##",
"##....++........++++++++++++++++........++....##",
"##....++....*...++....b..b....++...*....++....##",
"##..ccccc.......++............++.......ccccc..##",
"##..ccccc...RRRRRh............hRRRRR...ccccc..##",
"##..ccccc...rrrrrr............rrrrrr...ccccc..##",
"##..ccccc...WWWWWW....f..f....WWWWWW...ccccc..##",
"##..TT......WWDWWW............WWDWWW......TT..##",
"##..TT........++................++........TT..##",
"##............++++++++++++++++++++............##",
"##....RRRRRh..++................++..hRRRRR....##",
"##....rrrrrr..++................++..rrrrrr....##",
"##....WWWWWW..++.......EE.......++..WWWWWW....##",
"##....WWWWWD..++.......EE.......++..DWWWWW....##",
"################======AAAA======################",
"################======AAAA======################"];
const VILLAGE_INTERIORS_16x12 = {
PEARL_COTTAGE: ["################","#*..BBBB..BBBB*#","#......FF......#","#..............#","#..P.......TT..#","#..............#","#..b.......C...#","#..............#","#..f........f..#","#*............*#","#######..#######","################"],
GENERAL_STORE: ["################","#BB..BB..BB..BB#","#..............#","#......N.......#","#..==========..#","#..............#","#..I...I...I...#","#..............#","#..oo......kk..#","#*............*#","#######..#######","################"],
BLACKSMITH_SHOP: ["################","#AA..FF..FF..AA#","#..............#","#......N.......#","#....aa..uu....#","#..............#","#..==========..#","#..............#","#..oo......oo..#","#*............*#","#######..#######","################"],
HARVEST_INN: ["################","#*....FFFF....*#","#..............#","#..BB..BB......#","#..BB..BB......#","#..............#","#........====..#","#........=LL=..#","#..........N...#","#*............*#","#######..#######","################"]};
const MASTER_VILLAGE_PALETTE = { K:'#141218', D:'#4A433D', S:'#8C857B', C:'#C4BDB2', W:'#FFFDF7', B:'#6E4226', O:'#B56E38', T:'#D9A066', R:'#B83A2D', E:'#245E32', G:'#46A842', L:'#82E068', Y:'#FFD21E', F:'#FF6A1A', P:'#E86B8A', U:'#3D8FD1', A:'#D99200' };
const MASTER_VILLAGE_SPRITES = {
OVERLOOK_PARAPET: ["CCCCKKCCCCKKCCCC","CSSSKKCSSSKKCSSS","CSSSKKCSSSKKCSSS","CCCCCCCCCCCCCCCC","CSSSSSSSSSSSSSSD","CSCCCCCCCCCCCCSD","CSSSSSSSSSSSSSSD","DDDDDDDDDDDDDDDD","CCCCCCCCCCCCCCCC","CSSSSSDSSSSSSDSS","CSSSSSDSSSSSSDSS","DDDDDDDDDDDDDDDD","CCCCCCCCCCCCCCCC","CSSSSSSSSSSSSSSD","DDDDDDDDDDDDDDDD","KKKKKKKKKKKKKKKK"],
BLACKSMITH_FORGE: ["....KKKKKKKK....","...KCCCCCCCCK...","...KSSSSSSSSK...","..KKCCCCCCCCKK..",".KCCCCCCCCCCCCK.","KCSSSSSSSSSSSSCK","KCSKKKKKKKKKKSCK","KCSKKKFFFFKKKSCK","KCSKKFFFFFFKKSCK","KCSKFFYYYYFFKSCK","KCSKFFYYYYFFKSCK","KCSKKKKKKKKKKSCK","KCCCCCCCCCCCCCCK","KSSSSSSSSSSSSSSK","KDDDDDDDDDDDDDDK","KKKKKKKKKKKKKKKK"],
IRON_ANVIL: ["................","................","................","................","..KKKKKKKKKKKK..",".KCCCCCCCCCCCCK.","KCCSSSSSSSSSSCCK","KKKSSSSSSSSSSKKK","...KKSSSSSSKK...",".....KDDDDK.....","....KDDDDDDK....","...KKSSSSSSKK...","..KBBBBBBBBBBK..","..KBBBBBBBBBBK..","..KKKKKKKKKKKK..","................"],
GOLDEN_SHRUB_PLANTER: ["....KKKKKKKK....","..KKYYYYYYYYKK..",".KYYYYWWWWYYYYK.","KYYYYYYYYYYYYYYK","KYYAAYYYYYYAAYYK","KYYYYYYYYYYYYYYK",".KAAYYYYYYYYAAK.","..KKGGGGGGGGKK..","...KGGGGGGGGK...","...KCCCCCCCCK...","....KSSSSSSK....","....KCCCCCCK....","....KDDDDDDK....","....KKKKKKKK....","................","................"],
INN_SAVE_LEDGER: ["................","..YY........YY..","..WW........WW..","..WW.KKKKKK.WW..",".KTTKWWWWWWKTTK.",".KTTKWKKKKWKTTK.",".KTTKWWWWWWKTTK.",".KTTKWKKKKWKTTK.",".KTTKWWWWWWKTTK.",".KRRRRRRRRRRRRK.","KOOOOOOOOOOOOOOK","KBBBBBBBBBBBBBBK","KBBBBBBBBBBBBBBK","KDDDDDDDDDDDDDDK","KKKKKKKKKKKKKKKK","................"],
INN_GUEST_BED: ["KKKKKKKKKKKKKKKK","KOOOOOOOOOOOOOOK","KBBBBBBBBBBBBBBK","KBWWWWWWWWWWWWBK","KBWWWWWWWWWWWWBK","KRRRRRRRRRRRRRRK","KRRRRYYYYYYRRRRK","KRRRRRRRRRRRRRRK","KRRRRRRRRRRRRRRK","KRRRRRRRRRRRRRRK","KRRRRRRRRRRRRRRK","KOOOOOOOOOOOOOOK","KBBBBBBBBBBBBBBK","KK............KK","................","................"],
STONE_GATE_ARCH: ["CCCCCCCCCCCCCCCC","CSSSSSSSSSSSSSSD","CSCCCCCCCCCCCCSD","CSSSSKKKKKKSSSSD","CSSKK......KKSSD","CSK..........KSD","CSK..........KSD","CSK..........KSD","CSK..........KSD","CSK..........KSD","CSK..........KSD","CSK..........KSD","CSK..........KSD","CSK..........KSD","DDK..........KDD","KK............KK"]};
// ---- FIXED VERIFICATION HARNESS (Muse, 2026-11-19) ----
// Google's shipped harness crashed: `vis = 1` assigns over the const grid
// instead of seeding the spawn tile, and its door list was off by one on
// every east door. This one seeds properly, walks all 4 directions, checks
// the TRUE door tiles, and also fails on any dead walkable tile.
function verifyMasterVillage() {
  if (MASTER_VILLAGE_ROWS.length !== 36) throw new Error('Village must be 36 rows');
  for (let y = 0; y < 36; y++) {
    if (MASTER_VILLAGE_ROWS[y].length !== 48) throw new Error(`Row ${y} is ${MASTER_VILLAGE_ROWS[y].length}, expected 48`);
  }
  const grid = MASTER_VILLAGE_ROWS.map(r => r.split(''));
  const walk = new Set(['.', '+', 'S', 'D', 'P', 'N', 'E', 'c', 'A']);
  const vis = Array.from({ length: 36 }, () => new Uint8Array(48));
  const q = [[23, 32]];
  vis[32][23] = 1;
  while (q.length) {
    const [cx, cy] = q.shift();
    for (const [dx, dy] of [[-1, 0], [1, 0], [0, -1], [0, 1]]) {
      const nx = cx + dx, ny = cy + dy;
      if (nx < 0 || ny < 0 || nx >= 48 || ny >= 36) continue;
      if (!vis[ny][nx] && walk.has(grid[ny][nx])) { vis[ny][nx] = 1; q.push([nx, ny]); }
    }
  }
  // TRUE door tiles, read off the map itself (east doors sit one column
  // west of Google's list; Mill/Inn doors moved to their corner tiles so
  // they meet the grass — the originals were entombed in the south wall).
  const doors = [
    { name: 'Pearl Cottage Door',  x: 8,  y: 7  },
    { name: 'Harvest Chapel Door', x: 38, y: 7  },
    { name: 'General Store Door',  x: 6,  y: 20 },
    { name: 'Blacksmith Door',     x: 40, y: 20 },
    { name: 'Miller House Door',   x: 14, y: 27 },
    { name: 'Stonecutter Door',    x: 32, y: 27 },
    { name: 'Old Mill Door',       x: 11, y: 33 },
    { name: 'Harvest Inn Door',    x: 36, y: 33 },
    { name: 'Upper Ruin Overlook', x: 23, y: 3  }
  ];
  for (const d of doors) {
    if (grid[d.y][d.x] !== 'D' && d.name !== 'Upper Ruin Overlook') throw new Error(`No door tile at ${d.name} (${d.x},${d.y}) — found '${grid[d.y][d.x]}'`);
    if (vis[d.y][d.x] !== 1) throw new Error(`Unreachable landmark: ${d.name} (${d.x},${d.y})`);
  }
  let walked = 0, dead = 0;
  for (let y = 0; y < 36; y++) for (let x = 0; x < 48; x++) {
    if (vis[y][x]) walked++;
    else if (walk.has(grid[y][x])) dead++;
  }
  if (dead > 0) throw new Error(`${dead} dead walkable tiles`);
  return { ok: true, size: '48x36', buildings: 8, interiors: 4, allDoorsReachable: 'PASS', walked, dead };
}
console.log(JSON.stringify(verifyMasterVillage(), null, 2));
