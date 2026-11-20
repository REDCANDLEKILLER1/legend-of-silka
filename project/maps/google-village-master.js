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
// ---- checks ----
console.log('MAP rows:', MASTER_VILLAGE_ROWS.length);
MASTER_VILLAGE_ROWS.forEach((r, i) => { if (r.length !== 48) console.log(`  map row ${i}: len ${r.length}`); });
for (const [n, rows] of Object.entries(VILLAGE_INTERIORS_16x12)) {
  const bad = rows.map((r, i) => [i, r.length]).filter(([, l]) => l !== 16);
  console.log(`INT ${n}: rows=${rows.length} bad=${JSON.stringify(bad)}`);
}
for (const [n, rows] of Object.entries(MASTER_VILLAGE_SPRITES)) {
  const bad = rows.map((r, i) => [i, r.length]).filter(([, l]) => l !== 16);
  const chars = [...new Set(rows.join(''))].sort().join('');
  const stray = [...new Set(rows.join(''))].filter(c => c !== '.' && !(c in MASTER_VILLAGE_PALETTE));
  console.log(`SPR ${n}: rows=${rows.length} bad=${JSON.stringify(bad)} chars=${chars} stray=${stray.join('') || 'none'}`);
}
// door + anchor audit from the map itself
const G = MASTER_VILLAGE_ROWS.map(r => r.split(''));
const find = ch => { const out = []; G.forEach((row, y) => row.forEach((c, x) => { if (c === ch) out.push([x, y]); })); return out; };
console.log('D tiles:', JSON.stringify(find('D')));
console.log('P:', JSON.stringify(find('P')), 'E:', JSON.stringify(find('E')), 'K statue:', JSON.stringify(find('K')));
// ---- my own BFS (Google's harness still has `vis = 1` — assigns over the const array) ----
const walk = new Set(['.', '+', 'S', 'D', 'P', 'N', 'E', 'c', 'A']);
const vis = Array.from({ length: 36 }, () => new Uint8Array(48));
const q = [[23, 32]]; vis[32][23] = 1;
while (q.length) {
  const [cx, cy] = q.shift();
  for (const [dx, dy] of [[-1, 0], [1, 0], [0, -1], [0, 1]]) {
    const nx = cx + dx, ny = cy + dy;
    if (nx < 0 || ny < 0 || nx >= 48 || ny >= 36) continue;
    if (!vis[ny][nx] && walk.has(G[ny][nx])) { vis[ny][nx] = 1; q.push([nx, ny]); }
  }
}
let walked = 0, dead = [];
for (let y = 0; y < 36; y++) for (let x = 0; x < 48; x++) {
  if (vis[y][x]) walked++;
  else if (walk.has(G[y][x])) dead.push([x, y, G[y][x]]);
}
console.log(`BFS: walked=${walked} dead walkable=${dead.length}`, JSON.stringify(dead.slice(0, 12)));
const doors = [[8, 7, 'Pearl'], [39, 7, 'Chapel'], [6, 20, 'Store'], [41, 20, 'Smith'], [14, 27, 'Miller'], [33, 27, 'Stonecutter'], [8, 33, 'Mill'], [39, 33, 'Inn'], [23, 3, 'Overlook']];
for (const [x, y, n] of doors) console.log(`  ${n} (${x},${y}) tile=${G[y][x]} reached=${vis[y][x] === 1}`);
require('fs').writeFileSync('/tmp/master.json', JSON.stringify({ map: MASTER_VILLAGE_ROWS, sprites: MASTER_VILLAGE_SPRITES, pal: MASTER_VILLAGE_PALETTE, interiors: VILLAGE_INTERIORS_16x12 }));
