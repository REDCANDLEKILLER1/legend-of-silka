const { MASSIVE_CASTLE_ROWS: R } = require('./massive-exterior-artmatch.js');
const out = [];
out.push(`ART-MATCH EXTERIOR: ${R.length} rows, lengths ${[...new Set(R.map(r=>r.length))].join(',')}, symmetric rows ${R.filter(r=>r===[...r].reverse().join('')).length}/36`);
const find=(ch)=>{const p=[];R.forEach((r,y)=>[...r].forEach((c,x)=>{if(c===ch)p.push([x,y]);}));return p;};
out.push(`sealed doors K: ${JSON.stringify(find('K'))} · guards: ${find('G').length} · interior walkable tiles: ${find('.').filter(([x,y])=>x>6&&x<57&&y>3&&y<23).length} inside the walls`);
const WALK=new Set(['.','=','G']);
const vis=new Set(['31,35']); const q=[[31,35]];
while(q.length){ const [x,y]=q.shift();
  for (const [dx,dy] of [[1,0],[-1,0],[0,1],[0,-1]]){
    const nx=x+dx, ny=y+dy, k=nx+','+ny;
    if (nx<0||ny<0||nx>=64||ny>=36||vis.has(k)) continue;
    if (WALK.has(R[ny][nx])){ vis.add(k); q.push([nx,ny]); } } }
const has=(x,y)=>vis.has(x+','+y);
out.push(`causeway->gate landing (31,24): ${has(31,24)?'REACHABLE':'FAIL'} · doors stepped on: ${find('K').some(([x,y])=>has(x,y))?'LEAK':'sealed OK'}`);
out.push(`full outer circle — rear (31,1): ${has(31,1)?'OK':'FAIL'} · west (2,13): ${has(2,13)?'OK':'FAIL'} · east (61,13): ${has(61,13)?'OK':'FAIL'} · south-west (6,30): ${has(6,30)?'OK':'FAIL'}`);
let dead=[]; R.forEach((r,y)=>[...r].forEach((c,x)=>{ if(WALK.has(c)&&!vis.has(x+','+y)) dead.push(c+'@'+x+','+y); }));
out.push(`dead walkable tiles: ${dead.length?dead.join(' '):'none'} · tiles walked: ${vis.size}`);
console.log(out.join('\n'));
