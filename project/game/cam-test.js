// Camera math test: load the real game code, place the player at key spots,
// and verify the 16x12 view follows and clamps like Zelda 1.
const fs = require('fs');
const vm = require('vm');
function ctxStub(){ return new Proxy({}, { get: (t, k) => {
  if (k === 'createRadialGradient' || k === 'createLinearGradient') return () => ({ addColorStop(){} });
  if (k === 'canvas') return {};
  return typeof k === 'string' ? (() => {}) : undefined; }, set: () => true }); }
function elStub(){ const el = { style: {}, dataset: {}, children: {},
  classList: { add(){}, remove(){}, toggle(){} }, _innerHTML: '', textContent: '',
  addEventListener(){}, removeEventListener(){}, width: 0, height: 0 };
  Object.defineProperty(el, 'innerHTML', { get(){ return el._innerHTML; }, set(v){ el._innerHTML = v; } });
  el.getContext = () => ctxStub();
  el.querySelector = sel => el.children[sel] || (el.children[sel] = elStub());
  el.querySelectorAll = () => [];
  return el; }
const els = {};
const sandbox = { console, setTimeout, setInterval, clearInterval, clearTimeout, Promise, Math, JSON,
  document: { getElementById: id => els[id] || (els[id] = elStub()),
    createElement: () => elStub(), querySelectorAll: () => [], addEventListener(){}, removeEventListener(){} },
  location: { hash: '#hall', reload(){} },
  Audio: class { play(){ return Promise.resolve(); } pause(){} },
  Image: class {},
  requestAnimationFrame: () => {}, addEventListener(){}, removeEventListener(){},
  matchMedia: () => ({ matches: false, addEventListener(){} }), performance: { now: () => 0 } };
sandbox.window = sandbox; sandbox.globalThis = sandbox;
vm.createContext(sandbox);
const dir = __dirname;
const html = fs.readFileSync(dir + '/part1.html', 'utf8');
const main = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m => m[1]).pop();
vm.runInContext(fs.readFileSync(dir + '/sprites-data.js', 'utf8'), sandbox);
vm.runInContext(fs.readFileSync(dir + '/title-scene.js', 'utf8'), sandbox);
vm.runInContext(main, sandbox);
const checks = vm.runInContext(`
  const out = [];
  function place(build, x, y, label){
    loadScene(build());
    player.x = x; player.y = y; player.px = x * 16; player.py = y * 16;
    updateCam();
    out.push(label + ': cam=(' + camX + ',' + camY + ') view covers tiles x' +
      Math.floor(camX/16) + '-' + Math.floor((camX+255)/16) + ' y' + Math.floor(camY/16) + '-' + Math.floor((camY+191)/16));
  }
  place(buildHall, 16, 21, 'hall, Pearl at south door');
  place(buildHall, 16, 6,  'hall, Pearl at the dais');
  place(buildVillage, 15, 21, 'village, CornMan at south gate');
  place(buildVillage, 5, 7,   'village, CornMan at Pearl cottage door');
  place(buildCottage, 7, 9,   'cottage, CornMan inside');
  loadScene({ set:'hall', rows: HALL, player: null, entities: [], triggers: {}, refs: {} });
  scene.focus = null; updateCam();
  out.push('no-focus fallback: cam=(' + camX + ',' + camY + ')');
  out.join('\\n');
`, sandbox);
console.log(checks);
console.log('CAM TEST DONE');
process.exit(0);
