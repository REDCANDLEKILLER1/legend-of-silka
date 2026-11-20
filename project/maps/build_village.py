# CASTLE-FOOT VILLAGE — built to the concept sheet (Michael's tap 2026-11-19 00:24).
# 32x24 layout, his four calls in: Pearl NW (hearth), chapel NE, statue plaza center,
# mill + corn W/SW, store & smithy center, inn SE (bed & ledger), south gate,
# ruined castle looming over the cliff, look-only overlook.
from PIL import Image, ImageDraw
import random
random.seed(32)

W, H = 512, 384
img = Image.new('RGB', (W, H), (62, 142, 65))
d = ImageDraw.Draw(img)
K = (20, 18, 20)
GRASS_L = (110, 201, 91); GRASS_D = (36, 96, 46)

# ---------- ground texture ----------
for _ in range(700):
    x, y = random.randrange(2, W - 2), random.randrange(66, H - 2)
    d.line([(x, y), (x, y - 3)], fill=GRASS_L)
    d.line([(x + 2, y), (x + 2, y - 2)], fill=(90, 180, 80))
for cx, cy in [(60, 300), (470, 320), (150, 96), (360, 250), (40, 150)]:
    for dx, dy in [(0, 0), (3, 1), (1, 3)]:
        d.point((cx + dx, cy + dy), fill=(245, 239, 230))

# ---------- sky + ruined castle silhouette ----------
d.rectangle([0, 0, W, 40], fill=(168, 178, 196))
d.rectangle([0, 34, W, 44], fill=(150, 158, 178))
def tower(x, y0, w, h, broken=True):
    d.rectangle([x, y0 - h, x + w, y0], fill=(96, 98, 112))
    d.rectangle([x, y0 - h, x + w, y0 - h + 3], fill=(120, 122, 136))
    if broken:
        d.polygon([(x + w - 6, y0 - h), (x + w, y0 - h + 8), (x + w - 2, y0 - h)], fill=(168, 178, 196))
    for wy in range(y0 - h + 8, y0 - 6, 10):
        d.point((x + w // 2, wy), fill=(60, 40, 80))
tower(196, 42, 22, 30); tower(226, 42, 30, 40); tower(264, 42, 20, 26); tower(292, 42, 24, 34)
d.rectangle([210, 30, 306, 42], fill=(96, 98, 112))
d.rectangle([248, 36, 268, 42], fill=(40, 36, 48))  # shattered gate

# ---------- cliff band + promenade ----------
d.rectangle([0, 44, W, 64], fill=(146, 104, 58))
for _ in range(160):
    x, y = random.randrange(0, W), random.randrange(47, 62)
    d.line([(x, y), (x + random.choice((-2, 2)), y + random.randrange(3, 8))], fill=random.choice([(110, 74, 42), (170, 122, 70), (92, 58, 33)]))
d.rectangle([0, 62, W, 64], fill=(110, 74, 42))
d.rectangle([0, 42, W, 46], fill=(76, 160, 84))     # grass lip
d.rectangle([0, 64, W, 74], fill=(194, 185, 173))   # overlook promenade
for x in range(0, W, 12):
    d.line([(x, 64), (x, 74)], fill=(168, 158, 144))
# balustrade posts
for x in range(4, W, 16):
    d.rectangle([x, 60, x + 3, 66], fill=(150, 140, 126))

# ---------- helpers ----------
def roof(x0, y0, x1, color, dark, light):
    d.rectangle([x0 - 3, y0 + 4, x1 + 3, y0 + 16], fill=color)
    d.rectangle([x0 - 3, y0 + 1, x1 + 3, y0 + 4], fill=light)
    for ry in range(y0 + 7, y0 + 15, 4):
        for sx in range(x0, x1, 8):
            d.arc([sx, ry, sx + 8, ry + 5], 0, 180, fill=dark)
    d.rectangle([x0 - 3, y0 + 15, x1 + 3, y0 + 17], fill=dark)
def door(cx, y0, crest=True):
    d.rectangle([cx - 7, y0, cx + 7, y0 + 22], fill=K)
    d.rectangle([cx - 6, y0 + 1, cx + 6, y0 + 22], fill=(194, 185, 173))
    d.rectangle([cx - 4, y0 + 3, cx + 4, y0 + 22], fill=(110, 66, 38))
    d.line([(cx, y0 + 4), (cx, y0 + 22)], fill=(92, 58, 33))
    if crest:
        d.polygon([(cx, y0 + 6), (cx + 3, y0 + 9), (cx, y0 + 13), (cx - 3, y0 + 9)], fill=(255, 210, 30))
    d.rectangle([cx - 6, y0 + 22, cx + 6, y0 + 24], fill=(140, 133, 123))
def window(cx, y0):
    d.rectangle([cx - 6, y0, cx + 6, y0 + 11], fill=K)
    d.rectangle([cx - 5, y0 + 1, cx + 5, y0 + 10], fill=(255, 210, 30))
    d.line([(cx, y0 + 1), (cx, y0 + 10)], fill=K)
    d.line([(cx - 5, y0 + 5), (cx + 5, y0 + 5)], fill=K)
def house(x0, y0, x1, roofc, dark, light, doorx=None, sign=None):
    d.rectangle([x0 - 2, y0 + 28, x1 + 2, y0 + 32], fill=(50, 118, 54))
    d.rectangle([x0, y0 + 14, x1, y0 + 30], fill=(245, 239, 230))
    d.rectangle([x0, y0 + 14, x0 + 3, y0 + 30], fill=(92, 58, 33))
    d.rectangle([x1 - 3, y0 + 14, x1, y0 + 30], fill=(92, 58, 33))
    roof(x0, y0, x1, roofc, dark, light)
    if doorx: door(doorx, y0 + 8)
    for wx in range(x0 + 10, x1 - 6, 22):
        if doorx and abs(wx - doorx) < 12: continue
        window(wx, y0 + 16)
    if sign:
        sx = x1 - 14
        d.rectangle([sx, y0 + 2, sx + 12, y0 + 8], fill=(158, 104, 56))
        d.line([(sx + 2, y0 + 5), (sx + 10, y0 + 5)], fill=(60, 38, 20))
def tree(cx, cy, r=14):
    for ox, oy, rr in [(-7, 4, r - 3), (7, 4, r - 3), (0, -4, r), (-3, -8, r - 5)]:
        d.ellipse([cx + ox - rr, cy + oy - rr, cx + ox + rr, cy + oy + rr], fill=(46, 130, 60))
        d.arc([cx + ox - rr + 3, cy + oy - rr + 3, cx + ox + rr - 3, cy + oy + rr - 3], 200, 320, fill=GRASS_L, width=2)
    d.rectangle([cx - 2, cy + r - 2, cx + 2, cy + r + 4], fill=(92, 58, 33))
def path(pts, w=7):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill=(201, 147, 91), width=w)
    for x, y in pts:
        d.ellipse([x - w // 2, y - 3, x + w // 2, y + 3], fill=(201, 147, 91))

# ---------- dirt spurs (serve doors only) ----------
path([(256, 384), (256, 300), (250, 210), (252, 168)])                 # gate -> plaza south
path([(252, 140), (250, 110), (246, 84)])                               # plaza -> overlook steps
path([(230, 128), (150, 118), (104, 116)])                              # plaza -> Pearl
path([(282, 122), (340, 112), (398, 116)])                              # plaza -> chapel
path([(262, 152), (300, 190), (330, 196)])                              # plaza -> store/smith
path([(268, 168), (340, 230), (404, 252)])                              # plaza -> inn
path([(206, 196), (130, 200), (76, 204)])                               # store -> mill

for _ in range(260):
    x, y = random.randrange(70, 460), random.randrange(80, 380)
    d.point((x, y), fill=(176, 122, 66))
# ---------- PEARL'S COTTAGE (NW) ----------
house(28, 84, 100, (146, 62, 78), (94, 36, 50), (170, 84, 98), doorx=88)
d.rectangle([40, 78, 50, 88], fill=(158, 104, 56)); d.rectangle([39, 76, 51, 79], fill=(92, 58, 33))
# Pearl herself, small figure at her door
d.ellipse([82, 122, 88, 128], fill=(240, 230, 220)); d.rectangle([82, 128, 88, 136], fill=(120, 90, 160))
# ---------- HARVEST CHAPEL (NE) ----------
d.rectangle([404, 96, 468, 132], fill=(178, 169, 158))
d.rectangle([404, 96, 468, 99], fill=(140, 133, 123))
d.polygon([(398, 98), (436, 72), (474, 98)], fill=(90, 90, 104))
d.rectangle([433, 58, 439, 72], fill=(120, 122, 136))
d.line([(436, 52), (436, 62)], fill=(255, 210, 30)); d.line([(432, 56), (440, 56)], fill=(255, 210, 30))
d.rectangle([430, 106, 442, 122], fill=K)
d.pieslice([430, 100, 442, 112], 180, 360, fill=(255, 190, 60))
d.rectangle([431, 107, 441, 122], fill=(255, 190, 60))
door(436, 110)
# ---------- STATUE PLAZA (center) ----------
d.ellipse([206, 84, 306, 156], fill=(194, 185, 173))
d.ellipse([214, 90, 298, 150], fill=(178, 169, 158))
d.ellipse([224, 96, 288, 144], fill=(214, 205, 190))
for a in range(0, 360, 24):
    import math
    fx, fy = 256 + int(40 * math.cos(math.radians(a))), 120 + int(21 * math.sin(math.radians(a)))
    d.point((fx, fy), fill=(232, 93, 117)); d.point((fx + 1, fy), fill=(255, 210, 30))
d.rectangle([244, 124, 268, 130], fill=(130, 122, 110))                  # plinth base
d.rectangle([248, 116, 264, 125], fill=(150, 140, 126))                  # plinth
d.polygon([(250, 116), (253, 94), (259, 94), (262, 116)], fill=(168, 158, 144))  # robe
d.line([(256, 96), (256, 114)], fill=(140, 132, 120))
d.ellipse([252, 86, 260, 94], fill=(178, 169, 158))                       # head
d.polygon([(251, 88), (252, 82), (254, 87), (256, 81), (258, 87), (260, 82), (261, 88)], fill=(255, 210, 30))  # crown
for wx in range(0, 5):
    d.line([(263 + wx, 96), (261 + wx, 108)], fill=(240, 200, 40))        # wheat sheaf
d.point((256, 104), fill=(120, 60, 140))                                 # violet gem — the one wrong note
# ---------- MILL + WATER (W) ----------
d.rectangle([0, 196, 14, 240], fill=(69, 153, 201))
d.rectangle([16, 188, 76, 224], fill=(214, 190, 150))
d.rectangle([16, 188, 76, 192], fill=(140, 110, 70))
roof(16, 174, 76, (110, 66, 38), (80, 46, 24), (140, 92, 52))
door(46, 196)
d.ellipse([2, 204, 30, 232], outline=(92, 58, 33), width=3)
for a in (0, 90, 180, 270):
    import math
    d.line([(16, 218), (16 + int(13 * math.cos(math.radians(a))), 218 + int(13 * math.sin(math.radians(a))))], fill=(92, 58, 33), width=2)
# ---------- CORN FIELD (SW) ----------
for ry in range(252, 316, 12):
    for rx in range(28, 140, 11):
        d.line([(rx, ry + 8), (rx, ry)], fill=(76, 175, 80))
        d.ellipse([rx - 2, ry - 3, rx + 3, ry + 3], fill=(255, 210, 30))
        d.point((rx, ry - 4), fill=(240, 200, 40))
# ---------- GENERAL STORE + BLACKSMITH (center) ----------
house(176, 176, 252, (184, 58, 45), (140, 40, 34), (200, 74, 60), doorx=200, sign='STORE')
house(272, 176, 348, (90, 90, 104), (60, 60, 72), (120, 122, 136), doorx=330)
d.rectangle([286, 196, 300, 208], fill=(60, 56, 60))                     # forge
d.polygon([(288, 196), (293, 186), (298, 196)], fill=(255, 106, 26))
d.point((293, 192), fill=(255, 210, 30))
for bx, by in [(258, 210), (356, 206)]:
    d.rectangle([bx, by, bx + 8, by + 7], fill=(158, 104, 56))           # crates/barrels
# ---------- CLAN COTTAGES (E) ----------
house(392, 148, 444, (184, 58, 45), (140, 40, 34), (200, 74, 60), doorx=404)
house(448, 156, 496, (146, 62, 78), (94, 36, 50), (170, 84, 98), doorx=486)
# ---------- HARVEST INN (SE, two-storey) ----------
d.rectangle([386, 246, 482, 300], fill=(245, 239, 230))
d.rectangle([386, 246, 482, 250], fill=(214, 205, 190))
d.rectangle([386, 268, 482, 270], fill=(190, 178, 160))
d.rectangle([386, 246, 390, 300], fill=(92, 58, 33)); d.rectangle([478, 246, 482, 300], fill=(92, 58, 33))
roof(386, 224, 482, (122, 48, 64), (94, 36, 50), (146, 62, 78))
door(434, 262)
for wx in (402, 434, 466):
    window(wx, 230 + 22)
for wx in (404, 464):
    window(wx, 276)
d.rectangle([452, 240, 476, 247], fill=(158, 104, 56)); d.line([(455, 244), (473, 244)], fill=(60, 38, 20))
d.ellipse([368, 286, 384, 296], fill=(240, 200, 40))                     # hay bale
# ---------- trees, hedges, fences ----------
for tx, ty in [(130, 96), (356, 92), (486, 108), (160, 150), (366, 168), (120, 236), (500, 220), (20, 340), (486, 340), (180, 330), (330, 330)]:
    tree(tx, ty)
for tx, ty in [(118, 88), (142, 100), (344, 84), (368, 98), (30, 120), (492, 128)]:
    tree(tx, ty, r=17)  # canopy masses overlapping the singles
for hx in range(112, 140, 4):
    d.ellipse([hx, 128, hx + 7, 136], fill=(46, 110, 52))
for fx in range(356, 388, 8):
    d.rectangle([fx, 236, fx + 5, 250], fill=(158, 104, 56))
# ---------- SOUTH GATE ----------
for gx in (228, 272):
    d.rectangle([gx, 330, gx + 10, 384], fill=(150, 140, 126))
    d.rectangle([gx, 330, gx + 10, 334], fill=(120, 112, 100))
    for sy in range(338, 380, 10):
        d.line([(gx, sy), (gx + 10, sy)], fill=(130, 122, 110))
d.rectangle([224, 322, 286, 332], fill=(140, 133, 123))
d.rectangle([224, 322, 286, 325], fill=(178, 169, 158))

img = img.resize((W * 2, H * 2), Image.NEAREST)
img.save('village-built.png')
print('village built', img.size)
