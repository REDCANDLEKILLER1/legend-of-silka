#!/usr/bin/env python3
"""The Cook — her own sprite (2026-11-20). She was wearing the orchard
wife's sprite in the castle kitchen; Michael's standard is every person
their own person. White kerchief cap, flour-dusted cream apron over a
rust dress, sleeves rolled to the elbow, a steel ladle in her screen-right
hand in every view (the lane rule: signature props hold their screen side
in front and back). Lit eyes, a one-pixel smile — she is the castle's
heart. Views: down/up/right (left = flip, derived by the integrator).
Rows are four 4-char chunks so widths stay exact."""

PAL = {'K':'#181010','W':'#FFF8E8','s':'#9C522B','S':'#DE8E58','H':'#F7C294',
       'b':'#4A2814','B':'#8C4E24','a':'#9E620C','Y':'#F5BD1F','y':'#FFF066',
       'g':'#144A24','G':'#28823E','L':'#5EC956','R':'#C42838','C':'#F3E5C0',
       'r':'#A34A28','e':'#B8B4A8','E':'#E4E0D4','u':'#2456A8','U':'#3E78D8',
       'd':'#5A6B84','D':'#8496B0'}

COOK_DOWN = [
"...." ".WWW" "WW.." "....",
"...W" "WWWW" "WWWW" "....",
"...W" "WWWW" "WWWE" "....",
"..bW" "WWWW" "WWWW" "b...",
"..bb" "HHHH" "HHHH" "bb..",
"...b" "HWKH" "HWKH" "b...",
"...b" "HHHH" "KHHH" "b...",
"...." "bHHs" "HHHH" "b...",
"..rr" "rHHH" "HHHr" "rr..",
".rrr" "rrCC" "CCrr" "rrr.",
".rrr" "rCCC" "CCCr" "rrr.",
"..rr" "CCCC" "CCCC" "rr..",
"..SS" "CCCC" "CCCC" "SD..",
"..SS" "CCCC" "WCCC" "SD..",
"..HS" "CeeC" "CCCC" "SD..",
"..HH" "CeCC" "CCWC" "DDD.",
"..HH" "CCCC" "CCCC" "DWD.",
"..rr" "CCCC" "CCCr" "rr..",
".rrr" "CCCC" "CCCW" "rrr.",
".rrr" "rrrr" "rrrr" "rrr.",
"..rr" "rrrr" "rrrr" "rr..",
"...b" "bb.." "..bb" "b...",
"...b" "bb.." "..bb" "b...",
"..bb" "bb.." "..bb" "bb..",
]
COOK_UP = [
"...." ".WWW" "WW.." "....",
"...W" "WWWW" "WWWW" "....",
"...W" "WWWW" "WWWE" "....",
"..WW" "WWWW" "WWWW" "....",
"..bb" "bbbb" "bbbb" "bb..",
"..bb" "bbbb" "bbbb" "bb..",
"..bb" "bbBB" "BBbb" "bb..",
"...b" "bbbb" "bbbb" "b...",
"..rr" "rrrr" "rrrr" "rr..",
".rrr" "rrCC" "CCrr" "rrr.",
".rrr" "rrrr" "rrrr" "rrr.",
"..rr" "rrrr" "rrrr" "rr..",
"..SS" "rrrr" "rrrr" "SD..",
"..SS" "rrCC" "CCrr" "SD..",
"..HS" "rCCC" "CCCr" "SD..",
"..HH" "rrrr" "rrrr" "DDD.",
"..HH" "rrrr" "rrrr" "DWD.",
"..rr" "rrrr" "rrrr" "rr..",
".rrr" "rrrr" "rrrr" "rrr.",
".rrr" "rrrr" "rrrr" "rrr.",
"..rr" "rrrr" "rrrr" "rr..",
"...b" "bb.." "..bb" "b...",
"...b" "bb.." "..bb" "b...",
"..bb" "bb.." "..bb" "bb..",
]
COOK_RIGHT = [
"...." ".WWW" "W..." "....",
"...W" "WWWW" "WW.." "....",
"...W" "WWWW" "WWE." "....",
"..bW" "WWWW" "WWWb" "....",
"..bb" "bHHH" "HHHH" "....",
"..bb" "bHHH" "HWKH" "....",
"..bb" "bHHH" "HHHH" "H...",
"...b" "bHHH" "HsHH" "....",
"...r" "rrHH" "HHrr" "....",
"..rr" "rrrC" "CCCr" "....",
"..rr" "rrCC" "CCCr" "....",
"..rr" "rCCC" "CCCr" "....",
"..SS" ".CCC" "CCCS" "D...",
"..SS" ".CCC" "CCCC" "D...",
"..HH" ".CCC" "CCCS" "DD..",
"..HH" ".CCC" "CCCC" "DWD.",
"...r" ".CCC" "CCCC" "....",
"..rr" "rCCC" "CCCr" "....",
"..rr" "rrrr" "rrrr" "....",
"..rr" "rrrr" "rrrr" "....",
"...r" "rrrr" "rrr." "....",
"...." ".bb." ".bbb" "b...",
"...." ".bb." ".bbb" "b...",
"...." "bbb." ".bbb" "bb..",
]

SPRITES = {'cook': {'down': COOK_DOWN, 'up': COOK_UP, 'right': COOK_RIGHT}}

if __name__ == '__main__':
    for name, views in SPRITES.items():
        for view, rows in views.items():
            assert len(rows) == 24, (name, view, len(rows))
            for r in rows:
                assert len(r) == 16, (name, view, r)
                assert set(r) <= set(PAL) | {'.'}, (name, view, r)
    print('VALID')
