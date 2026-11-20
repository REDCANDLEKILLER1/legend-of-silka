// STORM WIZARD — glow renderer (Michael, 2026-11-19: "make sure it glows").
// The sprite frames live in google-wizard-v4.js (A/B, single bolt, RED eye
// dots per Michael's ruling). Glow = pulsing violet aura + 85ms frame swap,
// adapted from Google's renderer; bake skips NOTHING now (charset verified).
function bakeWizardSprite(rows, palette) {
  const c = document.createElement('canvas'); c.width = 24; c.height = 32;
  const ctx = c.getContext('2d');
  for (let y = 0; y < 32; y++) for (let x = 0; x < 24; x++) {
    const ch = rows[y][x];
    if (palette[ch]) { ctx.fillStyle = palette[ch]; ctx.fillRect(x, y, 1, 1); }
  }
  return c;
}
function drawStormWizard(ctx, wx, wy, timeMs, bakedA, bakedB) {
  const flicker = ((timeMs / 85) | 0) % 2;
  const pulse = 0.5 + 0.5 * Math.sin(timeMs * 0.009);
  const cx = wx + 12, cy = wy + 16;
  ctx.save();
  ctx.globalCompositeOperation = 'lighter';
  const radius = 20 + pulse * 6, alpha = 0.24 + pulse * 0.16;
  const aura = ctx.createRadialGradient(cx, cy, 2, cx, cy, radius);
  aura.addColorStop(0.0, `rgba(233, 213, 255, ${alpha})`);
  aura.addColorStop(0.5, `rgba(147, 51, 234, ${alpha * 0.85})`);
  aura.addColorStop(1.0, 'rgba(88, 28, 135, 0)');
  ctx.fillStyle = aura;
  ctx.beginPath(); ctx.arc(cx, cy, radius, 0, Math.PI * 2); ctx.fill();
  ctx.restore();
  ctx.drawImage(flicker === 0 ? bakedA : bakedB, wx, wy);
}
