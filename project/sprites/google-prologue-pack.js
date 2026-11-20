// Google's Prologue Engine Pack, as pasted 2026-11-19 (crow sprites, recolor, morph, state machine, harness).
const CROW_PALETTE = { K:'#0B0C10', D:'#241E33', Y:'#FFD21E', V:'#8E44EC' };
const CROW_SPRITES = {
PERCHED: ["................","................","......KKKK......",".....KKKKKK.....","....KKYKKKKK....","..YYKKKKKKKK....","....KKKKDKKKK...",".....KKKKDKKKK..",".....KKKKKDKKKK.","......KKKKKDKKKK",".......KKKKKK.KK","........KKKK....",".......K..K.....","......KK..KK....","................","................"],
FLY_WING_UP: [".....KK....KK...","....KDDK..KDDK..","...KDDDDKKDDDDK.","...KDDDDKKDDDDK.","....KKKKYYKKKK..","..YYKKKKKKKKKK..","....KKKKKKKK....",".....KKKKKK.....","......KKKK......",".....KK..KK.....","................","................","................","................","................","................"],
FLY_WING_DOWN: ["................","................","................",".....KKKKKK.....","..YYKKYKKKKK....","....KKKKKKKK....","...KDDDDDDDDK...","..KDDDDDDDDDDK..",".KVDDDDDDDDDDVK.","KK..KKKKKKKK..KK","....KK....KK....","................","................","................","................","................"]
};
const VILLAGE_FAMILY_PALETTES = {
  MILLER_CLAN: { G:'#2E6B9E', R:'#D97B29', E:'#4E7A27' },
  ORCHARD_CLAN: { G:'#8C3B5E', R:'#3D8E33', E:'#B85D3B' },
  STONECUTTER_CLAN: { G:'#5C5470', R:'#2E7D6B', E:'#7A4E28' }
};
function recolorSpriteRows(rows, swapMap) { return rows.map(row => row.split('').map(ch => swapMap[ch] || ch).join('')); }
function createLandFlinchMorph(postBand, postWater) {
  const W = 256, H = 96;
  const preBand = new Uint8Array(postBand); const preWater = new Uint8Array(postWater);
  for (let y = 0; y < H; y++) for (let x = 0; x < W; x++) {
    const i = y * W + x;
    if (x >= 130 && x <= 235 && y <= 42 && postBand[i] >= 3) preBand[i] = 2;
    if (postWater[i] === 2) { preWater[i] = 0; preBand[i] = 2; }
    if (x >= 185 && x <= 250 && y >= 58 && y <= 92 && postWater[i] === 1) {
      const d = Math.hypot((x - 216) / 14, (y - 78) / 8);
      if (d > 1.0) { preWater[i] = 0; preBand[i] = 2; }
    }
  }
  return { preBand, preWater,
    getMorphedTile(wx, wy, progress) {
      const i = wy * W + wx; const waveY = progress * (H + 16);
      if (wy <= waveY) return { band: postBand[i], water: postWater[i], justSplit: Math.abs(wy - waveY) < 2 };
      return { band: preBand[i], water: preWater[i], justSplit: false };
    } };
}
function createPrologueController(audioEngine) {
  return {
    currentBeat: 1, guestsSpokenTo: 0, hallDoorsShut: false, candlesBent: false, crowsActive: false, flinchProgress: 0,
    onTalkToFeastGuest(guestId) { this.guestsSpokenTo++; if (this.guestsSpokenTo >= 2 && this.currentBeat < 3) this.triggerBeat3Crows(); },
    triggerBeat3Crows() { this.currentBeat = 3; this.crowsActive = true; this.candlesBent = true; this.hallDoorsShut = true;
      if (audioEngine) { audioEngine.muteChannels(['MELODY_1','MELODY_2','PERCUSSION']); audioEngine.play('SFX_CROW_FLUTTER'); audioEngine.play('SFX_HEAVY_DOOR_SLAM'); } },
    advanceCutsceneBeat(nextBeat) { this.currentBeat = nextBeat; if (!audioEngine) return;
      if (nextBeat === 4) audioEngine.play('SFX_STORM_DOOR_BLAST');
      if (nextBeat === 5) audioEngine.play('SFX_POPPY_CHIME');
      if (nextBeat === 6) audioEngine.play('SFX_VIOLET_SLEEP_SPELL');
      if (nextBeat === 7) audioEngine.play('SFX_SEAL_RESONANCE');
      if (nextBeat === 8) audioEngine.play('SFX_MOUNTAIN_FLINCH_QUAKE');
      if (nextBeat === 9) { audioEngine.unmuteAllChannels(); audioEngine.playMusic('MUS_VILLAGE_MORNING'); } }
  };
}
function verifyPrologueAndVillage(feastRows, villageRows) {
  function canReach(grid, w, h, start, goal, walkChars) {
    const vis = Array.from({ length: h }, () => new Uint8Array(w));
    const q = [[start.x, start.y]]; vis[start.y][start.x] = 1;
    const DIRS = [[-1, 0],, [0, -1],];
    while (q.length) {
      const [cx, cy] = q.shift();
      if (cx === goal.x && cy === goal.y) return true;
      for (const [dx, dy] of DIRS) {
        const nx = cx + dx, ny = cy + dy;
        if (nx < 0 || ny < 0 || nx >= w || ny >= h) continue;
        if (!vis[ny][nx] && walkChars.has(grid[ny][nx])) { vis[ny][nx] = 1; q.push([nx, ny]); }
      }
    }
    return false;
  }
  const hallGrid = feastRows.map(r => r.split(''));
  const hallOk = canReach(hallGrid, 16, 12, { x: 7, y: 9 }, { x: 7, y: 2 }, new Set(['.', 'D']));
  if (!hallOk) throw new Error('Feast Hall path from entry to High Dais blocked');
  const vilGrid = villageRows.map(r => r.split(''));
  const vilWalk = new Set(['.', '=', 'E', 'P', 'N']);
  const pearlOk = canReach(vilGrid, 32, 24, { x: 15, y: 21 }, { x: 7, y: 6 }, vilWalk);
  const overlookOk = canReach(vilGrid, 32, 24, { x: 15, y: 21 }, { x: 15, y: 2 }, vilWalk);
  if (!pearlOk || !overlookOk) throw new Error(`Village path failed: pearl=${pearlOk}, overlook=${overlookOk}`);
  return { ok: true, feastHall: 'PASS', villagePearl: 'PASS', ruinOverlook: 'PASS', beats: 9 };
}
module.exports = { CROW_PALETTE, CROW_SPRITES, VILLAGE_FAMILY_PALETTES, recolorSpriteRows, createLandFlinchMorph, createPrologueController, verifyPrologueAndVillage };
