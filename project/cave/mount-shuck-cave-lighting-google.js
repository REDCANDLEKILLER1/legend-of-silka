/**
 * Flickering Cave Candles & Dynamic Torchlight Renderer
 *
 * SOURCE: Google (Gemini), relayed by Michael 2026-11-18 22:47.
 * Saved verbatim. REMY'S BUILD NOTES (from a cold read, 2026-11-18):
 *  - The pattern is sound: offscreen darkness mask, destination-out light
 *    holes with per-candle phase, then a 'lighter' warm pass.
 *  - The numbers are tuned for a 256x192 viewport (radius ~46px). Corn's
 *    canvas is 768x576 at TILE=48 — scale radii to ~1.5-2 tiles at build.
 *  - lightCanvas is created at module load; in the game, create lazily on
 *    first cave entry. Per-frame radial gradients are fine at room scale.
 *  - The stepped-radius option (snap to 4px) suits the game's crunchy look.
 */

/**
 * 1. Two-Frame Candle / Wall Brazier Sprites (16x16)
 * Alternate between CANDLE_A and CANDLE_B every ~140ms (with a per-candle phase offset
 * so candles don't blink in robotic unison).
 */
const CANDLE_PALETTE = {
  K: '#0B0C10', // Outline
  S: '#636B78', // Iron sconce shadow
  T: '#9BA4B2', // Iron sconce highlight
  W: '#E8DFCA', // Melted tallow wax
  O: '#FF6A1A', // Outer orange flame
  Y: '#FFE033'  // Inner bright gold core
};

const CANDLE_FRAME_A = [
  ".......OO.......",
  "......OOOO......",
  ".....OOYYOO.....",
  ".....OOYYOO.....",
  "......OOOO......",
  ".....KWWWWK.....",
  ".....KWWWWK.....",
  ".....KWWWWK.....",
  "...KKTTTTTTKK...",
  "..KTTTTTTTTTTK..",
  "..KSSSSSSSSSSK..",
  "...KKTTTTTTKK...",
  ".....KTTTTK.....",
  ".....KSSSSK.....",
  "....KKTTTTKK....",
  "....KKKKKKKK...."
];

const CANDLE_FRAME_B = [
  "......OO........", // Flame leans 1px left & narrows at tip
  ".....OOOO.......",
  ".....OOYYO......",
  "......OYYOO.....",
  "......OOOO......",
  ".....KWWWWK.....",
  ".....KWWWWK.....",
  ".....KWWWWK.....",
  "...KKTTTTTTKK...",
  "..KTTTTTTTTTTK..",
  "..KSSSSSSSSSSK..",
  "...KKTTTTTTKK...",
  ".....KTTTTK.....",
  ".....KSSSSK.....",
  "....KKTTTTKK....",
  "....KKKKKKKK...."
];

/**
 * 2. Flickering Cavern Darkness & Warm Candlelight Overlay
 * Call renderCaveLighting() at the end of your room draw loop.
 *
 * @param {CanvasRenderingContext2D} ctx - Main game canvas context
 * @param {number} width - Viewport width in pixels (e.g., 256)
 * @param {number} height - Viewport height in pixels (e.g., 192)
 * @param {Array<{x:number, y:number, id:number}>} candles - Pixel centers of visible candles
 * @param {{x:number, y:number}} player - Pixel center of Corn Man
 * @param {number} timeMs - Current game timestamp (performance.now())
 */
const lightCanvas = document.createElement('canvas');
const lightCtx = lightCanvas.getContext('2d');

function renderCaveLighting(ctx, width, height, candles, player, timeMs) {
  if (lightCanvas.width !== width || lightCanvas.height !== height) {
    lightCanvas.width = width;
    lightCanvas.height = height;
  }

  // Step A: Fill offscreen layer with deep subterranean shadow (82% opacity)
  lightCtx.globalCompositeOperation = 'source-over';
  lightCtx.fillStyle = 'rgba(8, 9, 16, 0.82)';
  lightCtx.fillRect(0, 0, width, height);

  // Step B: Punch holes in the darkness using 'destination-out'
  lightCtx.globalCompositeOperation = 'destination-out';

  // Subtle personal aura around Corn Man so player never loses sight of feet
  const playerGrad = lightCtx.createRadialGradient(player.x, player.y, 4, player.x, player.y, 34);
  playerGrad.addColorStop(0, 'rgba(0, 0, 0, 0.85)');
  playerGrad.addColorStop(1, 'rgba(0, 0, 0, 0)');
  lightCtx.fillStyle = playerGrad;
  lightCtx.beginPath();
  lightCtx.arc(player.x, player.y, 34, 0, Math.PI * 2);
  lightCtx.fill();

  // Flickering radius around every candle ('*')
  for (let i = 0; i < candles.length; i++) {
    const c = candles[i];
    // Deterministic multi-wave flicker unique to each candle position
    const phase = (c.x * 17 + c.y * 31) * 0.1;
    const flicker = Math.sin(timeMs * 0.014 + phase) * 3.5
                  + Math.cos(timeMs * 0.031 + phase * 2) * 2.0;
    const radius = 46 + flicker; // pulses smoothly between ~40px and ~52px

    const grad = lightCtx.createRadialGradient(c.x, c.y, 4, c.x, c.y, radius);
    grad.addColorStop(0, 'rgba(0, 0, 0, 1.0)');   // full clear center
    grad.addColorStop(0.65, 'rgba(0, 0, 0, 0.7)');
    grad.addColorStop(1, 'rgba(0, 0, 0, 0)');
    lightCtx.fillStyle = grad;
    lightCtx.beginPath();
    lightCtx.arc(c.x, c.y, radius, 0, Math.PI * 2);
    lightCtx.fill();
  }

  // Step C: Blit darkness mask onto main canvas
  ctx.drawImage(lightCanvas, 0, 0);

  // Step D: Add a warm golden-amber glow tint over each candle
  ctx.save();
  ctx.globalCompositeOperation = 'lighter';
  for (let i = 0; i < candles.length; i++) {
    const c = candles[i];
    const phase = (c.x * 17 + c.y * 31) * 0.1;
    const pulse = 0.16 + Math.sin(timeMs * 0.018 + phase) * 0.04;
    const warm = ctx.createRadialGradient(c.x, c.y, 2, c.x, c.y, 32);
    warm.addColorStop(0, `rgba(255, 190, 60, ${pulse})`);
    warm.addColorStop(1, 'rgba(255, 120, 20, 0)');
    ctx.fillStyle = warm;
    ctx.beginPath();
    ctx.arc(c.x, c.y, 32, 0, Math.PI * 2);
    ctx.fill();
  }
  ctx.restore();
}
