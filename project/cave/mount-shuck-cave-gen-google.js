/**
 * Multi-Floor Mount Shuck Cavern System (4 Floors x 48x24 tiles = 24 Rooms)
 * - Organic drunkard/simplex-carved winding tunnels (2-3 tiles wide)
 * - Irregular cavern "bubbles" (varying radii, never identical boxes)
 * - Vertical Ladders ('H' = up/down link between floors) & true dead-end branches
 * - Cave Map ('M'), 7 Treasure Chests ('C'), Entry ('E'), and Final Ascent to L9 ('U')
 *
 * SOURCE: Google (Gemini), relayed by Michael 2026-11-18 22:45.
 * PASTE REPAIRS (Remy, mechanical, disclosed — the relay garbled 3 spots):
 *  1. The verifier's DIRS array arrived as [[-1, 0],, [0, -1],] — two
 *     directions missing. Restored to the standard 4-dir set.
 *  2. The verifier's throw line arrived with its backticks stripped and a
 *     stray "</CreativeWritingPad>" artifact inside the function; the
 *     closing return/braces were mangled. Reconstructed to the obvious
 *     intended form (same message, same return shape as Google's prose).
 *  3. module.exports added so node can run it.
 * The generator itself (buildWindingMountShuckCave) arrived intact.
 */

const CAVE_W = 48;
const CAVE_H = 24;
const FLOORS = 4;

function buildWindingMountShuckCave(seed = 1337) {
  // Deterministic PRNG
  let s = seed >>> 0;
  const rand = () => {
    s = (Math.imul(s, 1664525) + 1013904223) >>> 0;
    return s / 4294967296;
  };

  // Initialize 4 solid rock floors ('#')
  const floors = Array.from({ length: FLOORS }, () =>
    Array.from({ length: CAVE_H }, () => Array(CAVE_W).fill('#'))
  );

  // Carve an irregular organic "bubble" chamber (noise-warped ellipse, never a rectangle)
  function carveBubble(f, cx, cy, rx, ry, hasChasm = false) {
    const phase = rand() * Math.PI * 2;
    for (let y = Math.max(2, Math.floor(cy - ry - 3)); y <= Math.min(CAVE_H - 3, Math.ceil(cy + ry + 3)); y++) {
      for (let x = Math.max(2, Math.floor(cx - rx - 3)); x <= Math.min(CAVE_W - 3, Math.ceil(cx + rx + 3)); x++) {
        const ang = Math.atan2(y - cy, x - cx);
        const wobble = 1 + 0.24 * Math.sin(ang * 3 + phase) + 0.14 * Math.cos(ang * 5 - phase);
        const norm = ((x - cx) / (rx * wobble)) ** 2 + ((y - cy) / (ry * wobble)) ** 2;
        if (norm <= 1.0) {
          floors[f][y][x] = '.';
        }
      }
    }
    // Optional central abyss island inside large bubbles
    if (hasChasm && rx >= 5 && ry >= 4) {
      for (let dy = -1; dy <= 1; dy++) {
        for (let dx = -2; dx <= 2; dx++) {
          if (Math.abs(dx) === 2 && Math.abs(dy) === 1) continue;
          if (dx === 0) floors[f][cy + dy][cx + dx] = '='; // stone bridge across chasm
          else floors[f][cy + dy][cx + dx] = ' ';          // pit chasm
        }
      }
    }
  }

  // Carve a long, snaking, wandering tunnel between (x0,y0) and (x1,y1)
  function carveWindingTunnel(f, x0, y0, x1, y1, width = 2) {
    let cx = x0, cy = y0;
    let perpAngle = Math.atan2(y1 - y0, x1 - x0) + Math.PI / 2;
    let steps = 0;

    while ((Math.abs(cx - x1) > 1 || Math.abs(cy - y1) > 1) && steps < 400) {
      steps++;
      const dx = x1 - cx, dy = y1 - cy;
      const dist = Math.hypot(dx, dy);
      // Strong sine meander + random jitter so tunnels snake organically
      const wave = Math.sin(steps * 0.28) * 1.35 + (rand() - 0.5) * 1.4;
      const vx = (dx / dist) + Math.cos(perpAngle) * wave * 0.65;
      const vy = (dy / dist) + Math.sin(perpAngle) * wave * 0.65;

      cx = Math.max(2, Math.min(CAVE_W - 3, Math.round(cx + Math.sign(vx) * (Math.abs(vx) > 0.35 ? 1 : 0))));
      cy = Math.max(2, Math.min(CAVE_H - 3, Math.round(cy + Math.sign(vy) * (Math.abs(vy) > 0.35 ? 1 : 0))));

      for (let oy = 0; oy < width; oy++) {
        for (let ox = 0; ox < width; ox++) {
          const tx = Math.min(CAVE_W - 2, cx + ox);
          const ty = Math.min(CAVE_H - 2, cy + oy);
          if (floors[f][ty][tx] === '#') floors[f][ty][tx] = '.';
        }
      }
    }
  }

  // --- FLOOR 0 (Entry at X -> 2 Bubbles + Dead-End Grotto + Ladder A up to F1) ---
  carveBubble(0, 8,  18, 4, 3);               // Entry cavern near X (7, 22)
  carveBubble(0, 26, 15, 6, 4, true);         // Wide southern chasm bubble
  carveBubble(0, 41, 19, 3, 3);               // Dead-end SE treasure grotto (no ladder!)
  carveBubble(0, 39, 6,  4, 3);               // NE climb chamber
  carveWindingTunnel(0, 7, 22, 8, 18, 2);     // South mouth X -> Entry bubble
  carveWindingTunnel(0, 8, 18, 26, 15, 2);    // Long snaking west->center tunnel
  carveWindingTunnel(0, 26, 15, 41, 19, 2);   // Branch 1: Dead-end grotto (Chest 1)
  carveWindingTunnel(0, 26, 15, 39, 6, 2);    // Branch 2: Winding north tunnel to Ladder A

  // --- FLOOR 1 (3 Irregular Bubbles + Drop-Down Pit Pocket to F0 + Ladder B up to F2) ---
  carveBubble(1, 39, 6,  4, 3);               // Arrival bubble from Ladder A
  carveBubble(1, 21, 8,  5, 4, true);         // Central Map Shrine bubble
  carveBubble(1, 8,  6,  4, 3);               // NW secret drop-shaft bubble
  carveBubble(1, 14, 18, 5, 3);               // SW boulder vault bubble
  carveWindingTunnel(1, 39, 6, 21, 8, 2);     // Long east->center tunnel
  carveWindingTunnel(1, 21, 8, 8, 6, 2);      // Center -> NW drop shaft (Ladder D down to F0 pocket)
  carveWindingTunnel(1, 21, 8, 14, 18, 2);    // Center -> SW Ladder B up to Floor 2

  // Secret isolated pocket on Floor 0 (only reachable by climbing DOWN Ladder D from Floor 1!)
  carveBubble(0, 8, 6, 4, 3);
  carveWindingTunnel(0, 8, 6, 15, 5, 2);

  // --- FLOOR 2 (The Dead-End Maze! Grand North Hall is a false trail; West Switchback goes to F3) ---
  carveBubble(2, 14, 18, 4, 3);               // Arrival from Ladder B
  carveBubble(2, 34, 16, 5, 3);               // SE crossroads bubble
  carveBubble(2, 36, 5,  6, 4, true);         // GRAND NORTH DEAD-END HALL (2 chests, NO ladder up!)
  carveBubble(2, 7,  11, 3, 3);               // Hidden western switchback pocket (Ladder C up to F3)
  carveWindingTunnel(2, 14, 18, 34, 16, 2);   // Long southern tunnel
  carveWindingTunnel(2, 34, 16, 36, 5, 2);    // Broad tempting path to Dead-End North Hall
  carveWindingTunnel(2, 14, 18, 7, 11, 2);    // Narrow winding west switchback to Ladder C

  // --- FLOOR 3 (High Mountain Ridge -> Final Ascent Stairs/Ladder to L9!) ---
  carveBubble(3, 7,  11, 4, 3);               // Arrival from Ladder C
  carveBubble(3, 24, 17, 4, 3);               // Southern ridge overlook (dead-end Chest 6)
  carveBubble(3, 27, 6,  5, 3, true);         // High chasm crossing
  carveBubble(3, 41, 5,  4, 3);               // Sanctum Ascent Chamber (UU -> L9!)
  carveWindingTunnel(3, 7, 11, 24, 17, 2);    // Snaking climb south-east
  carveWindingTunnel(3, 7, 11, 27, 6, 2);     // High ridge tunnel to chasm
  carveWindingTunnel(3, 27, 6, 41, 5, 2);     // Final approach to L9 Ascent Stairs

  // --- Place Vertical Ladders ('H'), Entry ('E'), Final L9 Stairs ('U'), Map ('M'), & 7 Chests ('C') ---
  const ladders = [
    { id: 'ladder_A', from: { f: 0, x: 39, y: 6  }, to: { f: 1, x: 39, y: 6  } }, // F0 <-> F1
    { id: 'ladder_B', from: { f: 1, x: 14, y: 18 }, to: { f: 2, x: 14, y: 18 } }, // F1 <-> F2
    { id: 'ladder_C', from: { f: 2, x: 7,  y: 11 }, to: { f: 3, x: 7,  y: 11 } }, // F2 <-> F3
    { id: 'ladder_D_drop', from: { f: 1, x: 8, y: 6 }, to: { f: 0, x: 8, y: 6 } } // F1 -> F0 secret pocket
  ];

  for (const l of ladders) {
    floors[l.from.f][l.from.y][l.from.x] = 'H';
    floors[l.to.f][l.to.y][l.to.x] = 'H';
  }

  // Overworld Entry at X (Floor 0, bottom-left) & Final Ascent to L9 (Floor 3, top-right)
  floors[0][22][7] = 'E';
  floors[0][21][7] = '.';
  floors[3][2][41] = 'U';
  floors[3][3][41] = '.';

  // Cave Map Pedestal (Floor 1 central bubble)
  floors[1][7][21] = 'M';

  // 7 Treasure Chests placed across main bubbles, dead-end floors, and secret drop pockets
  const chests = [
    { id: 'chest_1_f0_deadend', f: 0, x: 41, y: 19 }, // Dead-end SE grotto on F0
    { id: 'chest_2_f1_maproom', f: 1, x: 21, y: 10 }, // Central bubble on F1
    { id: 'chest_3_f0_secret',  f: 0, x: 15, y: 5  }, // Secret pocket reached only via F1 drop ladder
    { id: 'chest_4_f2_hall_w',  f: 2, x: 33, y: 4  }, // Grand Dead-End Hall West Chest on F2
    { id: 'chest_5_f2_hall_e',  f: 2, x: 39, y: 4  }, // Grand Dead-End Hall East Chest on F2
    { id: 'chest_6_f3_ridge',   f: 3, x: 24, y: 17 }, // Southern ridge dead-end bubble on F3
    { id: 'chest_7_f3_sanctum', f: 3, x: 43, y: 6  }  // Side alcove beside L9 ascent stairs
  ];
  for (const c of chests) floors[c.f][c.y][c.x] = 'C';

  // Decorative wall torches flanking entry & final L9 stairs
  floors[0][20][6] = '*'; floors[0][20][8] = '*';
  floors[3][3][39] = '*'; floors[3][3][43] = '*';

  return {
    floors,
    ladders,
    chests,
    entrance: { f: 0, x: 7, y: 22 },
    mapItem:  { f: 1, x: 21, y: 7 },
    ascentToL9: { f: 3, x: 41, y: 2 }
  };
}

// Node.js Multi-Floor Reachability Check (proves Entry -> Map -> All 7 Chests -> L9 Ascent)
function verifyMultiFloorCave(cave) {
  const walk = new Set(['.', '=', 'H', 'E', 'U', 'M', 'C']);
  const vis = Array.from({ length: FLOORS }, () =>
    Array.from({ length: CAVE_H }, () => new Uint8Array(CAVE_W))
  );

  // Build bidirectional ladder lookup ("f,x,y" -> target)
  const ladderMap = new Map();
  for (const l of cave.ladders) {
    ladderMap.set(`${l.from.f},${l.from.x},${l.from.y}`, l.to);
    ladderMap.set(`${l.to.f},${l.to.x},${l.to.y}`, l.from);
  }

  const q = [[cave.entrance.f, cave.entrance.x, cave.entrance.y]];
  vis[cave.entrance.f][cave.entrance.y][cave.entrance.x] = 1;

  const DIRS = [[-1, 0], [1, 0], [0, -1], [0, 1]]; // REPAIR 1: arrived garbled
  while (q.length) {
    const [cf, cx, cy] = q.shift();

    // Check vertical ladder transition
    const warp = ladderMap.get(`${cf},${cx},${cy}`);
    if (warp && !vis[warp.f][warp.y][warp.x]) {
      vis[warp.f][warp.y][warp.x] = 1;
      q.push([warp.f, warp.x, warp.y]);
    }

    for (const [dx, dy] of DIRS) {
      const nx = cx + dx, ny = cy + dy;
      if (nx < 0 || ny < 0 || nx >= CAVE_W || ny >= CAVE_H) continue;
      if (!vis[cf][ny][nx] && walk.has(cave.floors[cf][ny][nx])) {
        vis[cf][ny][nx] = 1;
        q.push([cf, nx, ny]);
      }
    }
  }

  const mapOk = vis[cave.mapItem.f][cave.mapItem.y][cave.mapItem.x] === 1;
  const stairsOk = vis[cave.ascentToL9.f][cave.ascentToL9.y][cave.ascentToL9.x] === 1;
  const chestsOk = cave.chests.every(c => vis[c.f][c.y][c.x] === 1);

  // REPAIR 2: throw/return reconstructed (backticks + closing braces)
  if (!mapOk || !stairsOk || !chestsOk) {
    throw new Error(`Multi-floor cave check failed: map=${mapOk}, stairs=${stairsOk}, chests=${chestsOk}`);
  }
  return { ok: true, floors: FLOORS, chests: cave.chests.length, ascentToL9: cave.ascentToL9 };
}

module.exports = { buildWindingMountShuckCave, verifyMultiFloorCave, CAVE_W, CAVE_H, FLOORS };
