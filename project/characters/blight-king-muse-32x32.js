// THE BLIGHT KING 32x32 — Muse's rebuild from the concept art
// (art/bosses-concept-ref.webp), Michael 2026-11-19 01:21 CST: "do better."
// Fixes vs Google's: crown spikes separated in bone (not a gold bar), face
// narrowed and socketed, chest skull kept SMALL and centered with ember
// cracks radiating on dark plate, scythe carried LOW so its gold never
// crosses the chest. Shared boss palette.
const PAL = { K:'#0B0A10', W:'#F7F3FF', d:'#242B3D', S:'#475573', L:'#7C90B8', v:'#4C1D95', V:'#8B5CF6', E:'#D8B4FE', p:'#2E1447', P:'#5B2C82', M:'#8C4EC2', o:'#9A3412', O:'#F97316', Y:'#FACC15', B:'#5C4028' };
const KING = [
"................W...............",
"............W...W...W...........",
"........W..WW..WWW..WW..W.......",
".......KWWWKWWWKWWWKWWWKWWWK....",
".......KYYYYYYYKOKYYYYYYYK......",
"........KpppppppppppppppK.......",
"........KpPPPPPPPPPPPPpK........",
"........KpPPKKPPPPKKPPpK........",
"........KpPPKOOPKOOPPpK.........",
"........KpPPPPPKPPPPpK..........",
"........KpPPPPKKKKPPpK..........",
"....KK..KKppppppppppKK..KK......",
"...KMMMMKPPPPPPPPPPPPKMMMMK.....",
"..KMMMKPPPPpPPPPPPpPPPPKMMMK....",
"..KMKPPPPPpKWWWWWKpPPPPPKMK.....",
"..KPPPPPoKWWKKWWKoPPPPPPPK......",
"...KPPPPpKWKWWKWKWKpPPPPK.......",
"...KPPPPpPKWKOOKKWKpPPPPK.......",
"...KPPPPPPpKKWWKKpPPPPPPK.......",
"....KPPPPpPKpKKpKPpPPPPK........",
"....KKPPPPKPPPPPPPPKPPPKK.......",
".....KMMKBBPPPPPPPPK.KMMK.......",
".....KPPK.KPBBPPPPPK.KPPK.......",
".....KPPK.KPvYBBYvPK.KPPK.KYK...",
".....KPPK.KPPvvBBPPK.KPPKYYYK...",
"......KK...KPpPPpPK.KK.KYYYK....",
"...........KPpP.KPpPK.KYYK......",
"...........KMMP.KMMPK.KYYK......",
"...........KPpP.KPpPK..KYK......",
"...........KPpP.KPpPK.KYK.......",
"...........KpPP.KPpPK.KK........",
"..........KKKKK..KKKKK.........."];
const bad = KING.map((r, i) => [i, r.length]).filter(([, l]) => l !== 32);
console.log('rows:', KING.length, 'bad widths:', JSON.stringify(bad));
console.log('stray:', [...new Set(KING.join(''))].filter(c => c !== '.' && !(c in PAL)).join('') || 'none');
require('fs').writeFileSync('/tmp/kingmuse.json', JSON.stringify({ KING, PAL }));
