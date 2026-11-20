// Runtime smoke test: boot the real game code under a DOM/canvas stub,
// walk every scene, render 120 frames each, exercise the wizard vignette.
const fs = require('fs');
function ctxStub(){ return new Proxy({}, { get: (t, k) => {
  if (k === 'createRadialGradient') return () => ({ addColorStop(){} });
  if (k === 'canvas') return {};
  return typeof k === 'string' ? (() => {}) : undefined; }, set: () => true }); }
function elStub(){ const el = { style: {}, classList: { add(){}, remove(){} }, dataset: {},
  querySelector: () => elStub(), addEventListener(){}, textContent: '', innerHTML: '' };
  el.getContext = () => ctxStub(); el.width = 0; el.height = 0; return el; }
const els = {};
global.document = { getElementById: id => els[id] || (els[id] = elStub()),
  createElement: () => elStub(), querySelectorAll: () => [], addEventListener(){} };
global.addEventListener = () => {}; global.removeEventListener = () => {};
global.location = { hash: '#hall', reload(){} };
global.Audio = class { play(){ return Promise.resolve(); } pause(){} };
global.requestAnimationFrame = () => {};
const data = fs.readFileSync(__dirname + '/sprites-data.js', 'utf8');
const titleData = fs.readFileSync(__dirname + '/title-scene.js', 'utf8');
const html = fs.readFileSync(__dirname + '/part1.html', 'utf8');
const scripts = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m => m[1]);
const src = data + '\n' + titleData + '\n' + scripts[scripts.length - 1] + `
;(async () => {
  await new Promise(r => setTimeout(r, 300));
  const out = [];
  titleOn = true;
  for (let i = 0; i < 90; i++) loop(i * 16.7);
  titleOn = false;
  out.push('title screen: rendered 90 frames (waterfall phases, twinkle, PUSH START blink)');
  for (const [name, build] of [['hall', buildHall], ['village', buildVillage], ['cottage', buildCottage]]){
    loadScene(build());
    for (let i = 0; i < 120; i++) render();
    out.push(name + ': rendered 120 frames, entities=' + scene.entities.length);
  }
  loadScene({ set: 'hall', rows: HALL, player: null, entities: [
    makeEnt(SPR.king, 15, 5, {}), makeEnt(SPR.silka, 17, 5, {}),
    makeEnt(wizSpr, 16, 20, { aura: true }) ], triggers: {}, refs: {} });
  for (let i = 0; i < 120; i++) render();
  out.push('telling vignette (wizard aura): rendered 120 frames');
  console.log(out.join('\\n'));
  console.log('SMOKE TEST PASS');
})().catch(e => { console.error('SMOKE FAIL:', e); process.exit(1); });
`;
eval(src);
setTimeout(() => process.exit(0), 5000); // the game registers a permanent interval; force-exit after the checks
