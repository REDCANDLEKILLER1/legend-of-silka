#!/usr/bin/env python3
"""Title screen for THE LEGEND OF SILKA — Zelda 1 grammar, ours, better.
128x96 pixel scene, recorded as rect lists: the SAME rects render the
proof PNG here and are emitted as game/title-scene.js for the live game
(waterfall phases, star twinkle, PUSH START blink animate in-engine).
No characters. A wrench where a sword would sit."""
import json, random
from PIL import Image

W, H, SC = 128, 96, 4
PAL = {}
def C(name, hexv):
    PAL[name] = hexv
    return name
INK    = C('ink',    '#181010')
SKY1   = C('sky1',   '#1B1035'); SKY2 = C('sky2', '#2A1748'); SKY3 = C('sky3', '#3D2058')
SKY4   = C('sky4',   '#5A2A52'); SKY5 = C('sky5', '#7A3A4A'); SKY6 = C('sky6', '#8A4A3A')
STARW  = C('starw',  '#FFF8E8'); STARG = C('starg', '#E8C86A'); STARP = C('starp', '#B8A8D8')
MOON   = C('moon',   '#F5D67A')
MTN    = C('mtn',    '#241233')
ROCK   = C('rock',   '#4A4258'); ROCKL = C('rockl', '#6A6280'); ROCKD = C('rockd', '#322C40')
CRACK  = C('crack',  '#241F30')
CASTLE = C('castle', '#1E1830'); CASTLE2 = C('castle2', '#14101F')
WINDIM = C('windim', '#8A6A1F'); WINBR = C('winbr', '#F5BD1F'); VIOLET = C('violet', '#8A2ABE')
FACE   = C('face',   '#3A3448'); FACED = C('faced', '#2C2738'); FACEL = C('facel', '#574E6A')
WFALL  = C('wfall',  '#2A4A7A'); WFALL2 = C('wfall2', '#3A6296')
WST1   = C('wst1',   '#CFE8FF'); WST2 = C('wst2', '#8FB8E8'); FOAM = C('foam', '#EAF6FF')
POOL   = C('pool',   '#16263F')
FIELD  = C('field',  '#1E3318'); STALK = C('stalk', '#2E7A34'); LEAF = C('leaf', '#5EC956')
GOLDD  = C('goldd',  '#8A6A1F'); GOLD = C('gold', '#C9A227'); GOLDL = C('goldl', '#FFDF6B')
GOLDM  = C('goldm',  '#F5BD1F'); PALEG = C('paleg', '#E8C86A')
PLAQ1  = C('plaq1',  '#160E26'); PLAQ2 = C('plaq2', '#1E1233')
STEEL  = C('steel',  '#9AA0AA'); STEELL = C('steell', '#D8DCE4'); STEELD = C('steeld', '#6A6E78')
WHITE  = C('white',  '#FFF8E8'); BONE = C('bone', '#E8E4D8')
SHADOW = C('shadow', '#0A0614')

STATIC, PUSH, TWINK = [], [], []
WATER = [[], [], []]
img = Image.new('RGB', (W, H), '#000000')
from PIL import ImageDraw
dr = ImageDraw.Draw(img)
def rect(lst, x, y, w, h, c):
    if w <= 0 or h <= 0: return
    lst.append((x, y, w, h, c))
    dr.rectangle([x, y, x + w - 1, y + h - 1], fill=PAL[c])
def R(x, y, w, h, c): rect(STATIC, x, y, w, h, c)

FONT = {
 'A': ["01110","10001","10001","11111","10001","10001","10001"],
 'C': ["01110","10001","10000","10000","10000","10001","01110"],
 'D': ["11100","10010","10001","10001","10001","10010","11100"],
 'E': ["11111","10000","10000","11110","10000","10000","11111"],
 'F': ["11111","10000","10000","11110","10000","10000","10000"],
 'G': ["01110","10001","10000","10111","10001","10001","01111"],
 'H': ["10001","10001","10001","11111","10001","10001","10001"],
 'I': ["01110","00100","00100","00100","00100","00100","01110"],
 'K': ["10001","10010","10100","11000","10100","10010","10001"],
 'L': ["10000","10000","10000","10000","10000","10000","11111"],
 'M': ["10001","11011","10101","10101","10001","10001","10001"],
 'N': ["10001","11001","10101","10011","10001","10001","10001"],
 'O': ["01110","10001","10001","10001","10001","10001","01110"],
 'P': ["11110","10001","10001","11110","10000","10000","10000"],
 'R': ["11110","10001","10001","11110","10100","10010","10001"],
 'S': ["01111","10000","10000","01110","00001","00001","11110"],
 'T': ["11111","00100","00100","00100","00100","00100","00100"],
 'U': ["10001","10001","10001","10001","10001","10001","01110"],
 'V': ["10001","10001","10001","10001","10001","01010","00100"],
 ' ': ["00000"]*7,
}
def text(lst, s, x, y, scale, color, shade=None):
    """Draw text recording rects. shade: fn(row)->color overrides per glyph row."""
    cx = x
    for ch in s:
        g = FONT[ch]
        for r, row in enumerate(g):
            cc = shade(r) if shade else color
            for i, bit in enumerate(row):
                if bit == '1':
                    rect(lst, cx + i * scale, y + r * scale, scale, scale, cc)
        cx += 6 * scale
    return cx - x - scale  # width drawn
def textw(s, scale): return len(s) * 6 * scale - scale
def outlined(lst, s, x, y, scale, color, shade=None):
    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
        text(lst, s, x + dx, y + dy, scale, INK)
    text(lst, s, x, y, scale, color, shade)

# ---------- sky ----------
for y, c in [(0,SKY1),(10,SKY2),(20,SKY3),(30,SKY4),(38,SKY5),(44,SKY6)]:
    R(0, y, W, 10 if y < 38 else (6 if y == 38 else 4), c)
rnd = random.Random(7)
stars = []
for _ in range(52):
    sx, sy = rnd.randrange(0, 127), rnd.randrange(1, 30)
    stars.append((sx, sy))
    R(sx, sy, 1, 1, rnd.choice([STARW, STARG, STARP]))
for sx, sy in stars[::8]:  # a few brighter anchors
    R(sx, sy, 1, 1, STARW)
for sx, sy in stars[::9]:  # twinkle set (engine toggles)
    rect(TWINK, sx, sy, 1, 1, STARW)
# moon crescent, top right
for dy in range(-3, 4):
    for dx in range(-3, 4):
        if dx*dx + dy*dy <= 9: R(7 + dx, 5 + dy, 1, 1, MOON)
for dy in range(-2, 3):
    for dx in range(-2, 3):
        if dx*dx + dy*dy <= 5: R(9 + dx, 4 + dy, 1, 1, SKY1)
# ---------- far mountains (center gap) ----------
hts = []
h = 45
for x in range(26, 102):
    h += rnd.choice([-1, 0, 0, 1])
    h = max(42, min(48, h)); hts.append(h)
    R(x, h, 1, 52 - h, MTN)
# ---------- valley floor + pool ----------
R(0, 90, W, 6, FIELD)
R(48, 88, 32, 6, POOL)
for x, y in [(54,90),(63,92),(71,90),(58,93),(75,92)]:
    R(x, y, 3, 1, WFALL2)
# ---------- cliffs ----------
def cliff(x0, x1, top_outer, top_inner):
    for x in range(x0, x1 + 1):
        t = x - x0; span = max(1, x1 - x0)
        top = top_outer + (top_inner - top_outer) * t // span
        R(x, top, 1, 96 - top, ROCK)
        R(x, top, 1, 3, ROCKL)                    # lit rim
        R(x, top + 14, 1, 96 - top - 14, ROCKD)   # shadowed lower mass (left light)
    for _ in range(9):
        cx = rnd.randrange(x0 + 1, x1 - 1); cy = rnd.randrange(58, 84)
        R(cx, cy, 1, rnd.choice([3, 4, 5]), CRACK)
cliff(0, 26, 44, 60)
cliff(101, 127, 60, 44)
R(0, 62, 20, 2, ROCKL); R(108, 58, 19, 2, ROCKL)  # ledges
# ---------- King's castle silhouette (left cliff) ----------
R(8, 34, 8, 12, CASTLE); R(3, 30, 4, 16, CASTLE); R(17, 32, 4, 14, CASTLE)
R(2, 29, 6, 1, CASTLE2); R(16, 31, 6, 1, CASTLE2); R(7, 33, 10, 1, CASTLE2)
R(9, 38, 1, 2, WINDIM); R(13, 40, 1, 2, WINDIM); R(4, 34, 1, 2, WINDIM)
rect(TWINK, 9, 38, 1, 2, WINBR)  # one window comes alive
# ---------- eye tower (right cliff) ----------
R(109, 26, 8, 3, CASTLE2); R(107, 29, 12, 3, CASTLE2); R(108, 32, 10, 14, CASTLE2)
for i, dx in enumerate([0, 1, 2, 3, 4]):  # closed eye: a heavy-lidded curve
    R(110 + dx, 37 + (1 if dx in (0, 4) else 0), 1, 1, ROCKL)
R(112, 41, 2, 3, VIOLET)
# ---------- center rock face + waterfall ----------
R(50, 58, 28, 32, FACE); R(50, 58, 3, 32, FACED); R(75, 58, 3, 32, FACEL)
R(48, 56, 32, 3, FACEL)
R(57, 59, 14, 29, WFALL); R(61, 59, 6, 29, WFALL2)
for p in range(3):
    for i, y0 in enumerate(range(60, 84, 6)):
        yy = y0 + p * 2
        rect(WATER[p], 58 + (i % 2) * 4, yy, 3, 3, WST1)
        rect(WATER[p], 67 - (i % 2) * 3, yy + 3, 2, 2, WST2)
    for fx in range(56, 73, 2):
        if (fx + p) % 3: rect(WATER[p], fx, 87, 2, 1, FOAM)
# ---------- corn clusters at the cliff feet ----------
for base_x in (3, 8, 14, 106, 112, 119):
    sh = rnd.choice([7, 9, 11])
    R(base_x, 95 - sh, 1, sh, STALK); R(base_x, 95 - sh, 1, 2, GOLDM)
    R(base_x + 1, 95 - sh + 3, 1, 1, LEAF)
# ---------- the emblem ----------
EX, EY, EW, EH = 15, 8, 98, 49
R(EX + 2, EY + 2, EW, EH, SHADOW)
R(EX, EY, EW, EH, GOLDD); R(EX + 1, EY + 1, EW - 2, EH - 2, GOLD)
R(EX + 3, EY + 3, EW - 6, EH - 6, FIELD)   # vine band
for lx in range(EX + 4, EX + EW - 5, 4):  # leaf ticks along the vine
    R(lx, EY + 4, 2, 2, LEAF); R(lx + 1, EY + EH - 6, 2, 2, LEAF)
for ly in range(EY + 8, EY + EH - 8, 4):
    R(EX + 4, ly, 2, 2, LEAF); R(EX + EW - 6, ly + 1, 2, 2, LEAF)
R(EX + 6, EY + 6, EW - 12, EH - 12, PLAQ1)
R(EX + 6, EY + 24, EW - 12, EH - 30, PLAQ2)
IX, IW = EX + 6, EW - 12
# THE LEGEND OF
s = 'THE LEGEND OF'
outlined(STATIC, s, IX + (IW - textw(s, 1)) // 2, EY + 8, 1, PALEG)
# SILKA — big, gold shaded by row
def silka_shade(r):
    return GOLDL if r < 2 else (GOLDM if r < 5 else GOLD)
s = 'SILKA'
outlined(STATIC, s, IX + (IW - textw(s, 3)) // 2, EY + 17, 3, GOLDM, shade=silka_shade)
# the wrench (no sword — CornMan's tool), laid under the name
WX, WY = IX + (IW - 46) // 2, EY + 41
R(WX - 1, WY - 1, 48, 9, INK)                       # silhouette
R(WX, WY + 1, 8, 5, STEEL); R(WX, WY, 6, 1, STEELL) # jaw block
R(WX, WY + 2, 4, 3, PLAQ2)                          # jaw mouth (the C opening)
R(WX + 8, WY + 2, 30, 3, STEEL); R(WX + 8, WY + 2, 30, 1, STEELL); R(WX + 8, WY + 4, 30, 1, STEELD)
R(WX + 38, WY, 8, 7, STEEL); R(WX + 38, WY, 8, 1, STEELL)  # box end
R(WX + 40, WY + 2, 4, 3, PLAQ2)                            # box hole
# ---------- subtitle lines over the land ----------
s = 'THE ADVENTURE OF'
outlined(STATIC, s, (W - textw(s, 1)) // 2, 61, 1, BONE)
def corn_shade(r):
    return GOLDL if r < 2 else (GOLDM if r < 5 else GOLD)
s = 'CORNMAN'
outlined(STATIC, s, (W - textw(s, 2)) // 2, 69, 2, GOLDM, shade=corn_shade)
# ---------- PUSH START (blink group) ----------
s = 'PUSH START'
text(PUSH, s, (W - textw(s, 1)) // 2 + 1, 88 + 1, 1, INK)
text(PUSH, s, (W - textw(s, 1)) // 2, 88, 1, WHITE)

# ---------- proof render ----------
img.resize((W * SC, H * SC), Image.NEAREST).save('art/title-screen.png')

# ---------- emit JS ----------
def merge(rects):
    rows = {}
    for x, y, w, h, c in rects:
        rows.setdefault((y, h, c), []).append((x, w))
    out = []
    for (y, h, c), spans in rows.items():
        spans.sort()
        cx, cw = spans[0]
        for x, w in spans[1:]:
            if x == cx + cw: cw += w
            else: out.append((cx, y, cw, h, c)); cx, cw = x, w
        out.append((cx, y, cw, h, c))
    return out
def js_rects(rects):
    pal = list(PAL.keys())
    return json.dumps([[x, y, w, h, pal.index(c)] for x, y, w, h, c in merge(rects)])
js = ("// Title scene for THE LEGEND OF SILKA — generated by art/design_title_screen.py.\n"
      "// Rects are [x, y, w, h, paletteIndex] on a 128x96 grid, drawn x4.\n"
      f"const TITLE_PAL = {json.dumps(list(PAL.values()))};\n"
      f"const TITLE_RECTS = {js_rects(STATIC)};\n"
      f"const TITLE_WATER = [{', '.join(js_rects(w) for w in WATER)}];\n"
      f"const TITLE_PUSH = {js_rects(PUSH)};\n"
      f"const TITLE_TWINK = {js_rects(TWINK)};\n")
open('game/title-scene.js', 'w').write(js)
print('static rects:', len(merge(STATIC)), '| water phases:', [len(merge(w)) for w in WATER],
      '| push:', len(merge(PUSH)), '| twink:', len(merge(TWINK)), '| title-scene.js bytes:', len(js))
