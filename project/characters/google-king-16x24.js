const LIVING = { K:'#181010', W:'#FFF8E8', s:'#9C522B', S:'#DE8E58', H:'#F7C294', b:'#4A2814', B:'#8C4E24', a:'#9E620C', Y:'#F5BD1F', y:'#FFF066', g:'#144A24', G:'#28823E', L:'#5EC956', R:'#C42838' };
const STATUE = { K:'#181010', W:'#ECE8DA', s:'#59574E', S:'#8C897D', H:'#C4C0B2', b:'#4A4840', B:'#757268', a:'#8C6214', Y:'#D4A424', y:'#F2D45C', g:'#244A24', G:'#467048', L:'#6CB84E', R:'#8A2E36' };
const ROWS = [
".....aYaYaYa....",".....yYyyYyyK...","....aYYYYYYYaK..",".yYa.bBBBBBBbK..","yYaYabHHHHHHBbK.","yYaYaBHKKSHKKBK.",".gLg.BHWKSHWHBK.",".KRK.bBWWBBWWbK.",".gGg.bBBBBBBBbK.","..g..KKbbbbbbKK.",".gLLGGGGYYYYGGLg","gLSHGGGGYYYYGGGL","gLHHGGGaYYYYaGGG","gGGGGGGaYLLYaGGG","gGGGGGaYLLLLYaGG","gGGGGGGaYLLYaSHg","gGGgGGGaYYYYaHHg","gGGgGGGaYYYYaGGg","gGGgGGGGYYYYGGGg",".gGgGGGGYYYYGGgK",".gGGYYYYYYYYYYgK","..ggaaaaaaaaaagK","....bBBb..bBBbK.","....KKKK..KKKK.."];
console.log('rows:', ROWS.length);
console.log('bad widths:', JSON.stringify(ROWS.map((r, i) => [i, r.length]).filter(([, l]) => l !== 16)));
console.log('stray vs living palette:', [...new Set(ROWS.join(''))].filter(c => c !== '.' && !(c in LIVING)).join('') || 'none');
console.log('stray vs statue palette:', [...new Set(ROWS.join(''))].filter(c => c !== '.' && !(c in STATUE)).join('') || 'none');
require('fs').writeFileSync('/tmp/king16.json', JSON.stringify({ ROWS, LIVING, STATUE }));
