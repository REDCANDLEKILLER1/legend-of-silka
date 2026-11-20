#!/usr/bin/env python3
"""Part 1 sprites — drawn to the 16x24 standard (clustered shading, ink
#181010, eyes low, curved hems). King + Wizard come from the approved
archive files; the rest debut here, anchored on the family portrait.
Validates every matrix, writes game/sprites-data.js + a contact sheet."""
import json
from PIL import Image

PAL = {'K':'#181010','W':'#FFF8E8','s':'#9C522B','S':'#DE8E58','H':'#F7C294',
       'b':'#4A2814','B':'#8C4E24','a':'#9E620C','Y':'#F5BD1F','y':'#FFF066',
       'g':'#144A24','G':'#28823E','L':'#5EC956','R':'#C42838','C':'#F3E5C0',
       'r':'#A34A28','e':'#B8B4A8','E':'#E4E0D4','u':'#2456A8','U':'#3E78D8',
       'd':'#5A6B84','D':'#8496B0'}
KING_PAL = {'K':'#181010','W':'#FFF8E8','s':'#9C522B','S':'#DE8E58','H':'#F7C294','b':'#4A2814','B':'#8C4E24','a':'#9E620C','Y':'#F5BD1F','y':'#FFF066','g':'#144A24','G':'#28823E','L':'#5EC956','R':'#C42838'}
STATUE_PAL = {'K':'#181010','W':'#ECE8DA','s':'#59574E','S':'#8C897D','H':'#C4C0B2','b':'#4A4840','B':'#757268','a':'#8C6214','Y':'#D4A424','y':'#F2D45C','g':'#244A24','G':'#467048','L':'#6CB84E','R':'#8A2E36'}
KING = [".....aYaYaYa....",".....yYyyYyyK...","....aYYYYYYYaK..",".yYa.bBBBBBBbK..","yYaYabHHHHHHBbK.","yYaYaBHKKSHKKBK.",".gLg.BHWKSHWHBK.",".KRK.bBWWBBWWbK.",".gGg.bBBBBBBBbK.","..g..KKbbbbbbKK.",".gLLGGGGYYYYGGLg","gLSHGGGGYYYYGGGL","gLHHGGGaYYYYaGGG","gGGGGGGaYLLYaGGG","gGGGGGaYLLLLYaGG","gGGGGGGaYLLYaSHg","gGGgGGGaYYYYaHHg","gGGgGGGaYYYYaGGg","gGGgGGGGYYYYGGGg",".gGgGGGGYYYYGGgK",".gGGYYYYYYYYYYgK","..ggaaaaaaaaaagK","....bBBb..bBBbK.","....KKKK..KKKK.."]

SILKA = [
".....yyyyyy.....",
"....yYYYYYYy....",
"...yYYYYYYYYy...",
"...yYHHHHHHYy...",
"...yYHHHHHHYy...",
"...yYHKHHKHYy...",
"...yYHHHHHHYy...",
"....yHHHHHHy....",
"...yYCCCCCCYy...",
"..yYCCCYCCCYy...",
"..yYCCCCCCCYy...",
".yYCCCCCCCCYy..",
".yYRRRRRRRRYy..",
".yYCCCCCCCCYy..",
"..yCCCCCCCCy...",
"..yCCCCCCCCy...",
"..yCCCCCCCCy...",
"..yCCCCCCCCy...",
"..yCCCCCCCCy...",
"..yCRRRRRRRCy..",
"...yCCCCCCy....",
"....SSSSSS.....",
"....bb..bb.....",
"...bbb..bbb...."]

PEARL_Y = [
"....bbbbbb......",
"...bBBBBBBb.....",
"...bBHHHHBb.....",
"...bHHHHHHb.....",
"...bHKHHKHb.....",
"...bHHHHHHb..b..",
"....HHHHHH..bB..",
"....bHHHHb..Bb..",
"...bCCCCCCb.b...",
"..bBCCWCCCBb....",
"..bCCCCCCCCb....",
".bBCCCCCCCCBb...",
".bWWWWWWWWWWb...",
".bWWWWWWWWWWb...",
"..brrrrrrrrb....",
"..brrrrrrrrb....",
"..brrrrrrrrb....",
"..brrrrrrrrb....",
"..brrrrrrrrb....",
"...rrrrrrrr.....",
"...SSSSSSSS.....",
"....SSSSSS......",
"....bb..bb......",
"...bbb..bbb....."]

PEARL_O = [
"....eeeeee......",
"...eEEEEEEe.....",
"...eEHHHH Ee....".replace(' ',''),
"...eHHHHHHe.....",
"...eHKHKHHe..e..",
"...eHHHHHHe.eE..",
"....HHHHHH..Ee..",
"....eHHHH e..e..".replace(' ',''),
"...errrrrre.e...",
"..erErrWrreE....",
"..errrrrrre..B..",
".ererrrrrre.BB..",
".ererrrrHre.B...",
"..errrrrre..B...",
"..errrrrre..B...",
"..errrrrre..B...",
"..errrrrre..B...",
"..errrrrre..B...",
"..ebbbbbb e..B..".replace(' ',''),
"...bbbbbbb...B..",
"...SSSSSS....B..",
"....SSSS.....B..",
"....bb..bb...B..",
"...bbb..bbb....."]

ELI = [
"....aaaaaa......",
"...aYYYYYYa.....",
"...aYHHHHYa.....",
"....HHHHHH......",
"....HKHKHH......",
"....HHHHHH......",
"....HHHHHH......",
".....HHHH.......",
"...CCCCCCCC.....",
"..bBCCCCCCBb....",
"..bBCBCCCCBb....",
"..bBCCBCCCBb....",
"..bBCCCCBBBb....",
"..bBCCCCCCBb....",
"...bbbbbbbb.....",
"...bbbbbbbb.....",
"...bbb..bbb.....",
"...bbb..bbb.....",
"...bbb..bbb.....",
"...bbb..bbb.....",
"...bbb..bbb.....",
"...bbb..bbb.....",
"....bb..bb......",
"...bbb..bbb....."]

FOLK_A = [
".....bbbb.......",
"....bbbbbb......",
"...bBBBBBBb.....",
"...bHHHHHHb.....",
"...bHHHHHHb.....",
"...bHKHHKHb.....",
"...bHHHHHHb.....",
"....HHHHHH......",
"...CCCCCCCC.....",
"..sSCCCCCCSs....",
"..sSCCCCCCSs....",
".sSGCCCCCCGSs...",
".sSWWWWWWWWSs...",
".sSWWWWWWWWSs...",
"..sGGGGGGGs.....",
"..sGGGGGGGs.....",
"..sGGGGGGGs.....",
"..sGGGGGGGs.....",
"..sGGGGGGGs.....",
"...GGGGGGG......",
"...SSSSSS.......",
"....SSSS........",
"....bb..bb......",
"...bbb..bbb....."]

FOLK_B = [
"....bbbbbb......",
"...bbbbbbbb.....",
"...HHHHHHHH.....",
"...HHHHHHHH.....",
"...HKHHHHKH.....",
"...HHHHHHHH.....",
"...bbbbbbbb.....",
"....bbbbbb......",
"..BBBBBBBBBB....",
".sSBBBBBBBBSs...",
".sSBBBBBBBBSs...",
".sSBBBBBBBBSs...",
".sSBBBKKBBBSs...",
"..sBBBBBBBBs....",
"..sBBBBBBBBs....",
"..sbbbbbbbb.....",
"..sbbb..bbb.....",
"..sbbb..bbb.....",
"..sbbb..bbb.....",
"....bb...bb.....",
"....bb...bb.....",
"....bb...bb.....",
"....bb...bb.....",
"...bbb...bbb...."]

GUARD = [
"....eeeeee......",
"...eEEEEEEe.....",
"...eEEEEEEe...e.",
"...KKKKKKKK...B.",
"....HHHHHH...eB.",
"....HKHKHH...BB.",
"....HHHHHH...B..",
".....HHHH....B..",
"...DDDDDDDD..B..",
"..sSDDDDDDDSsB..",
"..sSDDYYDDDSsB..",
"..sSDDDDDDDS.B..",
"..sSDDDDDDDS.B..",
"...DDDDDDDD..B..",
"...DDDDDDDD..B..",
"...dddddddd..B..",
"...ddd..ddd..B..",
"...ddd..ddd..B..",
"...ddd..ddd..B..",
"...ddd..ddd..B..",
"...ddd..ddd..B..",
"...KKK..KKK..B..",
"...KKK..KKK..K..",
"................"]

CORNMAN = [
"....YYYYYY......",
"...YYyYYyYYy....",
"...YYYYYYYY.....",
"..LLYYYYYYLL....",
"..LGYKYKYKG L...".replace(' ',''),
"..LGKKKKKKKGL...",
"..LGYKYKYKG L...".replace(' ',''),
"..LLYYYYYYLL....",
"....YYYYYY......",
".....HHHH.......",
"..RRUUUUUURR....",
".RRRUYYYYURRR...",
".RRRUYGGYURRR...",
".RRRUYYYYURRR...",
".RRRUUUUUURRR...",
"..RRUUUUUURR....",
"..HHUUUUUUHH....",
"...UUUUUUU......",
"...UUUUUUU......",
"...UUU..UUU.....",
"...UUU..UUU.....",
"...UUU..UUU.....",
"...KKK..KKK.....",
"...KKK..KKK....."]

CROW_A = [
"................",
".....KKK........",
"....KddKKaa.....",
"....KdWKKK......",
".....KKKKKK.....",
"....KddddKKK....",
"...KddddddKKK...",
"...KddddddKK....",
"....KddddK......",
"....KKKKK.......",
".....K.K........",
"....KK.KK.......",
"................",
"................",
"................",
"................"]
CROW_B = [
"..KK........KK..",
"..KddK....KddK..",
"...KddK..KddK...",
"....KKKKKKKK....",
".....KddKKaa....",
".....KdWKKK.....",
"......KKKKKK....",
".....KddddKK....",
".....KddddK.....",
"......KKKK......",
"......K.K.......",
".....KK.KK......",
"................",
"................",
"................",
"................"]


# width repairs (built by segment so the counts are exact)
SILKA[11] = '..yY' + 'C'*8 + 'Yy..'
SILKA[12] = '..yY' + 'R'*8 + 'Yy..'
SILKA[13] = '..yY' + 'C'*8 + 'Yy..'
for _i in range(14, 19): SILKA[_i] = '...y' + 'C'*8 + 'y...'
SILKA[19] = '...yC' + 'R'*6 + 'Cy...'
SILKA[20] = '....y' + 'C'*6 + 'y....'
SILKA[21] = '....' + 'S'*6 + '......'
SILKA[22] = '....' + 'bb' + '..' + 'bb' + '......'
SILKA[23] = '...' + 'bbb' + '..' + 'bbb' + '.....'
PEARL_O[2] = '...eE' + 'H'*5 + 'Ee....'
PEARL_O[7] = '....e' + 'H'*4 + 'e..e...'
PEARL_O[18] = '..e' + 'b'*6 + 'e..B...'
CORNMAN[4] = '..LG' + 'YKYKYK' + 'GL' + '....'
CORNMAN[6] = '..LG' + 'YKYKYK' + 'GL' + '....'


# craft fixes: corn kernel shading + true shades band; crows in profile
CORNMAN[1] = '...Y' + 'aY' + 'yY' + 'aY' + 'YY' + '....'
CORNMAN[2] = '...Y' + 'Ya' + 'YY' + 'yY' + 'aY' + '....'
CORNMAN[3] = '..LL' + 'YaYYaYYY' + 'LL' + '..'
CORNMAN[5] = '..LG' + 'K'*6 + 'GL' + '....'
CORNMAN[6] = '..LG' + 'YY' + 'K' + 'YYY' + 'GL' + '....'
CROW_A[:] = [
"................",
"................",
"......KKK.......",
".....KddKKaa....",
".....KdKKKK.....",
"....KKKKKKK.....",
"...KdddddKKK....",
"..KddddddKK.....",
"..KKddddK.......",
"...KKKKK........",
"..KK............",
"..K...KK........",
".....KK.........",
"................",
"................",
"................"]
CROW_B[:] = [
"..KK........KK..",
"..KdK......KdK..",
"...KdK....KdK...",
"....KKKKKKKK....",
".....KddKKaa....",
".....KdKKKK.....",
"....KKKKKKK.....",
"...KdddddKK.....",
"...KddddK.......",
"....KKKK........",
"....K.K.........",
"...KK.KK........",
"................",
"................",
"................",
"................"]

SPRITES = {'king': KING, 'silka': SILKA, 'pearlY': PEARL_Y, 'pearlO': PEARL_O,
           'eli': ELI, 'folkA': FOLK_A, 'folkB': FOLK_B, 'guard': GUARD,
           'cornman': CORNMAN}
CROWS = {'crowA': CROW_A, 'crowB': CROW_B}

ok = True
for name, rows in list(SPRITES.items()) + list(CROWS.items()):
    h = 24 if name not in CROWS else 16
    if len(rows) != h: print(f'{name}: {len(rows)} rows != {h}'); ok = False
    for i, r in enumerate(rows):
        if len(r) != 16: print(f'{name} row {i}: width {len(r)}'); ok = False
        bad = set(r) - set(PAL) - {'.'}
        if bad: print(f'{name} row {i}: stray {bad}'); ok = False
for i, r in enumerate(KING):
    if len(r) != 16: print(f'king row {i}: width {len(r)}'); ok = False
wiz = json.load(open('/tmp/wiz5.json'))
WIZ_A, WIZ_B, WIZ_PAL = wiz['A'], wiz['B'], wiz['PAL']
print('wizard:', len(WIZ_A), 'rows, widths ok:', all(len(r) == 24 for r in WIZ_A + WIZ_B))
print('VALID' if ok else 'FIX NEEDED')

js = []
js.append('// Part 1 sprite data — generated by characters/draw_part1_sprites.py. Do not hand-edit; fix the script.')
js.append('const PAL = ' + json.dumps(PAL) + ';')
js.append('const KING_PAL = ' + json.dumps(KING_PAL) + ';')
js.append('const STATUE_PAL = ' + json.dumps(STATUE_PAL) + ';')
js.append('const WIZ_PAL = ' + json.dumps(WIZ_PAL) + ';')
js.append('const SPRITES = {')
for name, rows in SPRITES.items():
    js.append(f'  {name}: ' + json.dumps(rows) + ',')
for name, rows in CROWS.items():
    js.append(f'  {name}: ' + json.dumps(rows) + ',')
js.append('  wizardA: ' + json.dumps(WIZ_A) + ',')
js.append('  wizardB: ' + json.dumps(WIZ_B))
js.append('};')
open('../game/sprites-data.js', 'w').write('\n'.join(js) + '\n')
print('wrote game/sprites-data.js')

# contact sheet
names = list(SPRITES) + ['crowA', 'crowB']
cell_w, cell_h, scale = 16 * 6, 24 * 6, 6
sheet = Image.new('RGB', (cell_w * 4, cell_h * 3), (40, 44, 58))
def draw(rows, pal, ox, oy, sc):
    for y, row in enumerate(rows):
        for x, ch in enumerate(row):
            if ch == '.': continue
            c = pal[ch]
            rgb = tuple(int(c[i:i+2], 16) for i in (1, 3, 5))
            for dy in range(sc):
                for dx in range(sc):
                    sheet.putpixel((ox + x * sc + dx, oy + y * sc + dy), rgb)
allr = dict(SPRITES); allr.update(CROWS)
for i, n in enumerate(names):
    draw(allr[n], PAL, (i % 4) * cell_w, (i // 4) * cell_h, scale)
sheet.save('part1-sprites-sheet.png')
print('sheet saved')
