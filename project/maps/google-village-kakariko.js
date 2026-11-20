// Google's Kakariko-Grade Village (48x36), as pasted 2026-11-19 00:17.
// CORN_WEATHERVANE arrived split by page text; rejoined 5+11 rows.
const KAKARIKO_VILLAGE_ROWS = [
"######^^##########^^^^^^^^^^^^##########^^######",
"#####X##X########X############X########X##X#####",
"###==========================================###",
"##TT++++++++++++++++++++++++++++++++++++++++TT##",
"##TT..RRRRRR....++....V.....++....RRRRRR....TT##",
"##....WWDWWW.!..++..f...f...++..!.WWDWWW......##",
"##......mm......++..........++......mm........##",
"##......P.....HHHHHHHH..HHHHHHHH..............##",
"CCCCCCCCCCCCCCCSSSSCCCCCCCCCCCCCSSSSCCCCCCCCCCCC",
"CCCCCCCCCCCCCCCSSSSCCCCCCCCCCCCCSSSSCCCCCCCCCCCC",
"##TT..f.......++++++........++++++....O...f.TT##",
"##TT..........++++++..dddd..++++++..........TT##",
"##----.--..HHHHHHHHH..dpNp..HHHHHHHHH..--.----##",
"##.........H........++dddd++........H.........##",
"##..ccccc..H..RRRRRR++++++++RRRRRR..H..ccccc..##",
"##..ccccc.....WWDWWW++....++WWDWWW.....ccccc..##",
"##..ccccc.....!.mm..++....++..mm.!.....ccccc..##",
"##..ccccc...........++....++...........ccccc..##",
"##TT..----.--.++++++++++++++++++++.--.----..TT##",
"##TT..........++..HHHHHHHHHHHH..++..........TT##",
"##....RRRRRR..++..H..f....f..H..++..RRRRRR....##",
"##....WWDWWW..++..H....FF....H..++..WWDWWW....##",
"##......mm....++..H....SS....H..++....mm......##",
"##......++....++..HHHH....HHHH..++....++......##",
"##......++++++++..++++++++++++..++++++++......##",
"##..TT........++.......N........++........TT..##",
"##..TT..RRRRRR++..----....----..++RRRRRR..TT..##",
"##......WWDWWW++................++WWDWWW......##",
"##........mm..++..f..........f..++..mm........##",
"##............++++++++++++++++++++............##",
"##..----.-----++++.....EE.....++++-----.----..##",
"##............++++.....EE.....++++............##",
"##TT..........++++............++++..........TT##",
"####################+++..+++####################",
"####################+++..+++####################",
"####################+++..+++####################"
];
const KAKARIKO_PALETTE = { K:'#181418', D:'#24522E', G:'#3E8E41', L:'#6EC95B', S:'#8C857B', C:'#C2B9AD', W:'#F5EFE6', B:'#5C3A21', O:'#9E6838', T:'#C9935B', R:'#B83A2D', Y:'#FFD21E' };
const KAKARIKO_SPRITES = {
KAKARIKO_COBBLE: ["CCCCCCCCCCCCCCCS","CWWWWWWSCWWWWWWC","CWCCCCCSCWCCCCCS","CWCCCCCSCWCCCCCS","CSSSSSSSCSSSSSSS","CWWWWWWWCWWWWWWC","CWCCCCCCWCWCCCCS","CWCCCCCCWCWCCCCS","CSSSSSSSSCSSSSSS","CWWWWWWSCWWWWWWC","CWCCCCCSCWCCCCCS","CWCCCCCSCWCCCCCS","CSSSSSSSCSSSSSSS","CWWWWWWWCWWWWWWC","CWCCCCCCWCWCCCCS","SSSSSSSSSSSSSSSS"],
BOXWOOD_HEDGE: ["KKLLLLLLLLLLLLKK","KLGGGGGGGGGGGGLK","KGLGGLGGLGGLGGLK","KGGGGGGGGGGGGGGK","KLGGLGGLGGLGGLGK","KGGGGGGGGGGGGGGK","KGLGGLGGLGGLGGLK","KGGGGGGGGGGGGGGK","KDDDDDDDDDDDDDDK","KDGGGGGGGGGGGGDK","KDDDDDDDDDDDDDDK","KBBBBBBBBBBBBBBK","KKKKKKKKKKKKKKKK",".KKKKKKKKKKKKKK.","................","................"],
LOG_POST_FENCE: ["................","................","..KKKK....KKKK..",".KTTTTK..KTTTTK.",".KTOOOK..KTOOOK.",".KOOOOOK.KOOOOOK","KKOOOOOKKOOOOOKK","KBBBBBBBBBBBBBBK",".KOOOOK..KOOOOK.",".KOOOOK..KOOOOK.",".KBBBBK..KBBBBK.",".KBBBBK..KBBBBK.",".KKKKKK..KKKKKK.","................","................","................"],
TERRACE_CLIFF: ["LLLLLLLLLLLLLLLL","GGGGGGGGGGGGGGGG","DDDDDDDDDDDDDDDD","TTTTTTTTTTTTTTTT","OOOOOOOOOOOOOOOO","OOBBOOOOBBOOOOBB","OOBBOOOOBBOOOOBB","BBBBBBBBBBBBBBBB","OOBBOOOOBBOOOOBB","OOBBOOOOBBOOOOBB","BBBBBBBBBBBBBBBB","KKKKKKKKKKKKKKKK","DDDDDDDDDDDDDDDD","GGGGGGGGGGGGGGGG","GGGGGGGGGGGGGGGG","GGGGGGGGGGGGGGGG"],
KAKARIKO_ROOF: ["KKKKKKKKKKKKKKKK","TTTTTTTTTTTTTTTT","OOOOOOOOOOOOOOOO","OOBBOOOOBBOOOOBB","OOOOOOOOOOOOOOOO","BBBBBBBBBBBBBBBB","TTTTTTTTTTTTTTTT","BBOOOOBBOOOOBBOO","OOOOOOOOOOOOOOOO","BBBBBBBBBBBBBBBB","TTTTTTTTTTTTTTTT","OOBBOOOOBBOOOOBB","OOOOOOOOOOOOOOOO","BBBBBBBBBBBBBBBB","KKKKKKKKKKKKKKKK","DDDDDDDDDDDDDDDD"],
KAKARIKO_DOOR: ["BBBBBBBBBBBBBBBB","TTTTTTTTTTTTTTTT","TTLLLLKKKKLLLLTT","TTLKKOOOOOOLLKTT","TLKOOBBBBBBOOKLT","TLKOBBYYYYBBOKLT","TLKOBBYRRBYBOKLT","TLKOBBYYYYBBOKLT","TLKOOBBBBBBOOKLT","TLKOOBBBBBBOOKLT","TLKOOBBYYBBOOKLT","TLKOOBBBBBBOOKLT","TLKOOBBBBBBOOKLT","CCCCCCCCCCCCCCCC","SSSSSSSSSSSSSSSS","KKKKKKKKKKKKKKKK"],
WELCOME_MAT: ["GGGGGGGGGGGGGGGG","GGGGGGGGGGGGGGGG","..KKKKKKKKKKKK..",".KWWWWWWWWWWWWK.",".KWCCCCCCCCCCWK.",".KWCSSSSSSSSCWK.",".KWCSSSSSSSSCWK.",".KWCSSSSSSSSCWK.",".KWCCCCCCCCCCWK.",".KSSSSSSSSSSSSK.","..KKKKKKKKKKKK..","GGGGGGGGGGGGGGGG","GGGGGGGGGGGGGGGG","GGGGGGGGGGGGGGGG","GGGGGGGGGGGGGGGG","GGGGGGGGGGGGGGGG"],
WOOD_SIGNPOST: ["................","..KKKKKKKKKKKK..",".KTTTTTTTTTTTTK.",".KTOOOOOOOOOOTK.",".KTOKKKKKKKOOTK.",".KTOOOOOOOOOOTK.",".KTOKKKKKKKOOTK.",".KTOOOOOOOOOOTK.",".KBBBBBBBBBBBBK.","..KKKKKKKKKKKK..","......KOOOK.....","......KBBBK.....","......KBBBK.....",".....KKBBBKK....",".....KKKKKKK....","................"],
CLAY_POT: ["................","................",".....KKKKKK.....","....KTTTTTTK....",".....KBBBBK.....","...KKOOOOOOKK...","..KOOOOOOOOOOK..","..KOTTOOOOOOOK..","..KOOOOOOOOOOK..","..KBBBBBBBBBBK..","...KBBBBBBBBK...","....KKKKKKKK....",".....KKKKKK.....","................","................","................"],
CORN_WEATHERVANE: [".......YY.......","......KYYK......",".....KGYYGK.....","......KYYK......","...YYYYYYYYYY...","......KYYK......","....KKWWWWKK....","...KWCCCCCCWK...","....KSSSSSSK....",".....KWWWWK.....",".....KCCCCK.....","....KWCCCCWK....","...KWCCCCCCWK...","..KSSSSSSSSSSK..","..KKKKKKKKKKKK..","................"]
};
module.exports = { KAKARIKO_VILLAGE_ROWS, KAKARIKO_PALETTE, KAKARIKO_SPRITES };
