const { FINAL_CASTLE_ROWS: FC, SOVEREIGN_CHAMBER_ROWS: SC } = require('./fixed-pack.js');
const out = [];
out.push(`CITADEL: ${FC.length} rows, lengths ${[...new Set(FC.map(r=>r.length))].join(',')}`);
out.push(`SOVEREIGN: ${SC.length} rows, lengths ${[...new Set(SC.map(r=>r.length))].join(',')}`);
const WALK = new Set(['.','=','U','S','C','H',',','E','A']);
function find(rows,ch){ const p=[]; rows.forEach((r,y)=>[...r].forEach((c,x)=>{ if(c===ch) p.push([x,y]); })); return p; }
function bfs(grid, sx, sy, extraSolid){
  const H=grid.length, W=grid[0].length, vis=new Set([sx+','+sy]), q=[[sx,sy]];
  while(q.length){ const [x,y]=q.shift();
    for (const [dx,dy] of [[1,0],[-1,0],[0,1],[0,-1]]){
      const nx=x+dx, ny=y+dy, k=nx+','+ny;
      if (nx<0||ny<0||nx>=W||ny>=H||vis.has(k)) continue;
      if (extraSolid && extraSolid.has(k)) continue;
      if (WALK.has(grid[ny][nx])){ vis.add(k); q.push([nx,ny]); } } }
  return vis;
}
const reach=(v,pts)=>pts.every(([x,y])=>v.has(x+','+y));
const adj=(v,pts)=>pts.some(([x,y])=>[[1,0],[-1,0],[0,1],[0,-1]].some(([dx,dy])=>v.has((x+dx)+','+(y+dy))));
const U=find(FC,'U'),S=find(FC,'S'),Wz=find(FC,'W'),D=find(FC,'D'),K=find(FC,'K');
out.push(`stairs ${JSON.stringify(U)} switches ${JSON.stringify(S)} wizard ${JSON.stringify(Wz)} doors ${JSON.stringify(D)} gate ${JSON.stringify(K)}`);
const G=()=>FC.map(r=>r.split(''));
let g=G(), v=bfs(g,U[0][0],U[0][1]);
out.push(`LEG1 stairs->both switches: ${reach(v,S)?'PASS':'FAIL'}`);
out.push(`LEG1b wizard sealed pre-switches: ${adj(v,Wz)?'LEAK':'blocked OK'}`);
K.forEach(([x,y])=>g[y][x]='.'); v=bfs(g,U[0][0],U[0][1]);
out.push(`LEG2 post-switches -> wizard: ${adj(v,Wz)||reach(v,Wz)?'PASS':'FAIL'}`);
Wz.forEach(([x,y])=>g[y][x]='.'); D.forEach(([x,y])=>g[y][x]='.');
v=bfs(g,U[0][0],U[0][1]);
out.push(`LEG3 post-wizard -> sovereign doors: ${reach(v,D)?'PASS':'FAIL'}`);
let dead=[]; g.forEach((row,y)=>row.forEach((c,x)=>{ if(WALK.has(c)&&!v.has(x+','+y)) dead.push(c+'@'+x+','+y); }));
out.push(`citadel dead walkable tiles at end state: ${dead.length?dead.join(' '):'none'}`);
const E=find(SC,'E'),X=find(SC,'X'),A=find(SC,'A');
const SG=()=>SC.map(r=>r.split(''));
let sg=SG(), sv=bfs(sg,E[0][0],E[0][1]);
out.push(`LEG4 entry->boss: ${adj(sv,X)?'PASS':'FAIL'}`);
// no-bypass: seal the boss band (rows 9-10) entirely -> altar must be unreachable
const band=new Set(); for(let x=0;x<32;x++){ band.add(x+',9'); band.add(x+',10'); }
const sv2=bfs(sg,E[0][0],E[0][1],band);
out.push(`LEG4b no route to altar that skips the boss chamber: ${reach(sv2,A)?'LEAK':'sealed OK'}`);
X.forEach(([x,y])=>sg[y][x]=','); sv=bfs(sg,E[0][0],E[0][1]);
out.push(`LEG5 post-king -> Poppy's altar: ${reach(sv,A)?'PASS':'FAIL'}`);
let sdead=[]; sg.forEach((row,y)=>row.forEach((c,x)=>{ if(WALK.has(c)&&!sv.has(x+','+y)) sdead.push(c+'@'+x+','+y); }));
out.push(`sovereign dead walkable tiles at end state: ${sdead.length?sdead.join(' '):'none'}`);
console.log(out.join('\n'));
