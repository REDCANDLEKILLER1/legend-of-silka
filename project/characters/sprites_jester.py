#!/usr/bin/env python3
"""The court JESTER (2026-11-20) — Michael's ask: a jester by the throne
who, when talked to, runs around the room and dances, then comes back and
introduces himself. Motley: tunic split red/gold, three-point fool's cap
with gold bells, white ruff, wide grin, one hand on his hip. Legs split
red/gold to match. Views down/up/right (left = flip)."""

PAL = {'K':'#181010','W':'#FFF8E8','s':'#9C522B','S':'#DE8E58','H':'#F7C294',
       'b':'#4A2814','B':'#8C4E24','a':'#9E620C','Y':'#F5BD1F','y':'#FFF066',
       'g':'#144A24','G':'#28823E','L':'#5EC956','R':'#C42838','C':'#F3E5C0',
       'r':'#A34A28','e':'#B8B4A8','E':'#E4E0D4','u':'#2456A8','U':'#3E78D8',
       'd':'#5A6B84','D':'#8496B0'}

JESTER_DOWN = [
"..y." "...." "..y." "....",
".Ry." ".RR." ".Ry." "....",
"..R." "RRRR" "RRR." "....",
"...R" "RRRR" "RR.." "....",
"...." "HHHH" "HHHH" "....",
"...." "HWKH" "HWKH" "....",
"...." "HHHH" "KHHH" "....",
"...." "HHKK" "KKHH" "....",
"...W" "WWWW" "WWWW" "W...",
"..RR" "RRRR" "YYYY" "YY..",
"..RR" "RRRR" "YYYY" "Y...",
"..RR" "RRRR" "YYYY" "....",
".HRR" "RRRR" "YYYY" ".Y..",
".HH." "RRRR" "YYYY" "....",
"...." "RRRR" "YYYY" "....",
"...." "RRRR" "YYYY" "....",
"...." "RRRR" "YYYY" "....",
"...." ".RRR" "YYY." "....",
"...." ".RR." ".YY." "....",
"...." ".RR." ".YY." "....",
"...." ".RR." ".YY." "....",
"...R" "RR.." "..YY" "Y...",
"..RR" "R..." "...Y" "YY..",
"..RR" "R..." "...Y" "YY..",
]
JESTER_UP = [
"..y." "...." "..y." "....",
".Ry." ".RR." ".Ry." "....",
"..R." "RRRR" "RRR." "....",
"...R" "RRRR" "RR.." "....",
"...." "bbbb" "bbbb" "....",
"...." "bbbb" "bbbb" "....",
"...." "bbbb" "bbbb" "....",
"...." "bbbb" "bbbb" "....",
"...W" "WWWW" "WWWW" "W...",
"..RR" "RRRR" "YYYY" "YY..",
"..RR" "RRRR" "YYYY" "Y...",
"..RR" "RRRR" "YYYY" "....",
".HRR" "RRRR" "YYYY" ".Y..",
".HH." "RRRR" "YYYY" "....",
"...." "RRRR" "YYYY" "....",
"...." "RRRR" "YYYY" "....",
"...." "RRRR" "YYYY" "....",
"...." ".RRR" "YYY." "....",
"...." ".RR." ".YY." "....",
"...." ".RR." ".YY." "....",
"...." ".RR." ".YY." "....",
"...R" "RR.." "..YY" "Y...",
"..RR" "R..." "...Y" "YY..",
"..RR" "R..." "...Y" "YY..",
]
JESTER_RIGHT = [
"...." "..y." "...." "....",
"...." ".Ry." ".R.." "....",
"...." "..R." "RRR." "....",
"...." ".RRR" "RR.." "....",
"...." ".HHH" "HHH." "....",
"...." ".HHH" "WKH." "....",
"...." ".HHH" "HHHH" "H...",
"...." ".HHK" "KHH." "....",
"...." "WWWW" "WWW." "....",
"...." ".RRR" "YYY." "....",
"...." ".RRR" "YY.." "....",
"...." "HRRR" "YY.." "....",
"...." "HHRR" "YY.." "....",
"...." "..RR" "YY.." "....",
"...." "..RR" "YY.." "....",
"...." "..RR" "YY.." "....",
"...." "..RR" "YY.." "....",
"...." "...R" "YY.." "....",
"...." "...R" "Y..." "....",
"...." "...R" "Y..." "....",
"...." "...R" "YY.." "....",
"...." "...." ".YYY" "....",
"...." "...." ".YYY" "Y...",
"...." "...." ".YYY" "YY..",
]

SPRITES = {'jester': {'down': JESTER_DOWN, 'up': JESTER_UP, 'right': JESTER_RIGHT}}

if __name__ == '__main__':
    for name, views in SPRITES.items():
        for view, rows in views.items():
            assert len(rows) == 24, (name, view, len(rows))
            for r in rows:
                assert len(r) == 16, (name, view, r)
                assert set(r) <= set(PAL) | {'.'}, (name, view, r)
    print('VALID')
