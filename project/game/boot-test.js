// Boot test: replicate browser script semantics (separate scripts, one shared
// global) on the REAL boot path (location.hash = ''). Catches load-time throws
// that the scene smoke test cannot, because it enters via a #hash preview.
// Usage: node boot-test.js <dir-containing-index.html>
const fs = require('fs');
const vm = require('vm');
const dir = process.argv[2] || __dirname;

function ctxStub(){ return new Proxy({}, { get: (t, k) => {
  if (k === 'createRadialGradient' || k === 'createLinearGradient') return () => ({ addColorStop(){} });
  if (k === 'canvas') return {};
  if (k === 'measureText') return () => ({ width: 10 });
  return typeof k === 'string' ? (() => {}) : undefined; }, set: () => true }); }
function elStub(tag){ const el = { tag: tag || 'div', style: {}, dataset: {}, children: {},
  classList: { add(){}, remove(){}, toggle(){} }, _innerHTML: '', textContent: '',
  addEventListener(){}, removeEventListener(){}, width: 0, height: 0 };
  Object.defineProperty(el, 'innerHTML', { get(){ return el._innerHTML; }, set(v){ el._innerHTML = v; } });
  el.getContext = () => ctxStub();
  el.querySelector = sel => el.children[sel] || (el.children[sel] = elStub(sel));
  el.querySelectorAll = () => [];
  return el; }
const els = {};
const sandbox = {
  console, setTimeout, setInterval, clearInterval, clearTimeout, Promise, Math, JSON,
  document: { getElementById: id => els[id] || (els[id] = elStub('#' + id)),
    createElement: t => elStub(t), querySelectorAll: () => [], addEventListener(){}, removeEventListener(){} },
  location: { hash: '', reload(){} },
  Audio: class { constructor(src){ this.src = src; } play(){ return Promise.resolve(); } pause(){} },
  Image: class { constructor(){ this._src = ''; } set src(v){ this._src = v; } get src(){ return this._src; } },
  requestAnimationFrame: () => {},
  addEventListener(){}, removeEventListener(){},
  matchMedia: () => ({ matches: false, addEventListener(){} }),
  performance: { now: () => 0 },
};
sandbox.window = sandbox; sandbox.globalThis = sandbox;
vm.createContext(sandbox);
let failed = false;
process.on('unhandledRejection', e => { failed = true; console.log('UNHANDLED REJECTION:', e && e.message); });

const html = fs.readFileSync(dir + '/index.html', 'utf8');
// Load scripts in document order, exactly as a browser would: src files and
// inline blocks interleaved. Works for the folder build and the standalone.
const files = {};
let n = 0;
for (const m of html.matchAll(/<script(?:\s+src="([^"]+)")?\s*>([\s\S]*?)<\/script>/g)){
  if (m[1]) files[m[1]] = fs.readFileSync(dir + '/' + m[1], 'utf8');
  else if (m[2].trim()) files['inline-' + (n++)] = m[2];
}
for (const [name, src] of Object.entries(files)){
  try { vm.runInContext(src, sandbox, { filename: name }); console.log(name + ': evaluated OK'); }
  catch (e) { failed = true; console.log(name + ': THREW ->\n' + e.stack.split('\n').slice(0, 4).join('\n')); }
}
setTimeout(() => {
  const card = els['card'];
  const bg = card && card.children['.bgimg'];
  console.log('--- after 800ms ---');
  console.log('card display:', card && card.style.display, '| className:', card && card.className);
  console.log('card innerHTML length:', card ? card._innerHTML.length : 'no card');
  console.log('bgimg backgroundImage:', bg ? bg.style.backgroundImage : '(none)');
  const pass = !failed && card && card.style.display === 'flex' && card._innerHTML.length > 100 &&
    bg && /url\(.+\)/.test(bg.style.backgroundImage || '');
  console.log(pass ? 'BOOT TEST PASS — title card is up with the animated frame' : 'BOOT TEST FAIL');
  process.exit(pass ? 0 : 1);
}, 800);
