# The King IN his plaza — the game's actual view (sheet perspective), not an icon.
# Composition from Michael's ref crop: wall + cliff behind, grass band, round trees,
# concentric cobble plaza, flower ring, statue center with a cast shadow.
from PIL import Image, ImageDraw
import math, random
random.seed(9)
W, H = 640, 480
img = Image.new('RGB', (W, H), (186, 177, 164))
d = ImageDraw.Draw(img)
K = (26, 24, 28)
S1 = (196, 188, 174); S2 = (172, 163, 148); S3 = (146, 138, 124); S4 = (118, 110, 98)
GOLD = (216, 178, 58); GOLD_D = (172, 136, 42); GOLD_L = (240, 205, 100)
MOSS = (74, 138, 72); MOSS_D = (52, 108, 56)

# --- sky + castle wall with crenellations + broken tower ---
d.rectangle([0, 0, W, 26], fill=(168, 178, 196))
d.rectangle([268, 2, 300, 30], fill=(120, 122, 136)); d.rectangle([336, 6, 362, 30], fill=(120, 122, 136))
d.rectangle([0, 26, W, 62], fill=(150, 152, 164))
for x in range(0, W, 32):
    d.rectangle([x, 18, x + 18, 30], fill=(150, 152, 164))
    d.line([(x, 44), (x + 32, 44)], fill=(128, 130, 142))
# --- cliff face: striated rock ---
d.rectangle([0, 62, W, 148], fill=(168, 128, 78))
for _ in range(240):
    x, y = random.randrange(0, W), random.randrange(66, 140)
    d.line([(x, y), (x + random.choice((-3, 3)), y + random.randrange(6, 16))], fill=random.choice([(140, 100, 56), (190, 148, 92), (116, 80, 44)]))
d.rectangle([0, 60, W, 66], fill=(120, 122, 136))
d.rectangle([0, 144, W, 152], fill=(110, 78, 44))
# --- grass band + trees ---
d.rectangle([0, 152, W, H], fill=(62, 142, 65))
for _ in range(260):
    x, y = random.randrange(2, W - 2), random.randrange(156, H - 2)
    d.line([(x, y), (x, y - 3)], fill=(110, 201, 91))
def tree(cx, cy, r=26):
    d.rectangle([cx - 3, cy + r - 4, cx + 3, cy + r + 10], fill=(92, 58, 33))
    for ox, oy, rr in [(-14, 6, r - 6), (14, 6, r - 6), (0, -8, r)]:
        d.ellipse([cx + ox - rr, cy + oy - rr, cx + ox + rr, cy + oy + rr], fill=(46, 130, 60))
        d.arc([cx + ox - rr + 5, cy + oy - rr + 5, cx + ox + rr - 5, cy + oy + rr - 5], 200, 320, fill=(110, 201, 91), width=3)
tree(84, 176); tree(556, 176); tree(140, 200, 20); tree(500, 200, 20)
# --- the plaza: concentric cobble ellipses ---
CX, CY = 320, 348
d.ellipse([CX - 262, CY - 66, CX + 262, CY + 66], fill=(190, 181, 168))
for r, wdt in [(262, 3), (216, 2), (172, 2)]:
    d.ellipse([CX - r, CY - int(r * 0.252), CX + r, CY + int(r * 0.252)], outline=S3, width=wdt)
for a in range(0, 360, 5):
    x0, y0 = CX + int(238 * math.cos(math.radians(a))), CY + int(60 * math.sin(math.radians(a)))
    x1, y1 = CX + int(258 * math.cos(math.radians(a))), CY + int(65 * math.sin(math.radians(a)))
    d.line([(x0, y0), (x1, y1)], fill=S3)
# flower bed ring
for a in range(0, 360, 4):
    fx, fy = CX + int(178 * math.cos(math.radians(a))), CY + int(45 * math.sin(math.radians(a)))
    d.ellipse([fx - 4, fy - 3, fx + 4, fy + 3], fill=MOSS_D)
    d.point((fx, fy), fill=random.choice([(232, 93, 117), (245, 239, 230), (255, 210, 30), (240, 160, 200)]))
# cast shadow, down-left
d.ellipse([196, 330, 400, 372], fill=(52, 118, 54))

class T:
    def __init__(self, dr, s, ox, oy): self.d, self.s, self.ox, self.oy = dr, s, ox, oy
    def P(self, pts): return [(x * self.s + self.ox, y * self.s + self.oy) for x, y in pts]
    def polygon(self, pts, fill): self.d.polygon(self.P(pts), fill=fill)
    def rectangle(self, b, fill): self.d.rectangle([b[0] * self.s + self.ox, b[1] * self.s + self.oy, b[2] * self.s + self.ox, b[3] * self.s + self.oy], fill=fill)
    def ellipse(self, b, fill): self.d.ellipse([b[0] * self.s + self.ox, b[1] * self.s + self.oy, b[2] * self.s + self.ox, b[3] * self.s + self.oy], fill=fill)
    def line(self, pts, fill, width=1): self.d.line(self.P(pts), fill=fill, width=max(1, int(width * self.s)))
    def point(self, p, fill): x, y = p[0] * self.s + self.ox, p[1] * self.s + self.oy; self.d.ellipse([x - 1, y - 1, x + 1, y + 1], fill=fill)
# --- the King — v4 anatomy per Michael's zoom ref ---
# BOTH hands cup a BIG green gem at his belly; gold throat clasp above it; eyes OPEN
# and stern under the brow; thick mustache, straight mouth, jaw-frame beard; the sheaf
# is a ground-rest scepter at his right side; moss heavy on the stone.
t = T(d, 0.78, 320 - 240 * 0.78, 306 - 372 * 0.78)
# plinth: two tiers, block joints, grass in the seams
t.ellipse([128, 396, 352, 436], S3); t.ellipse([128, 390, 352, 430], S2)
t.ellipse([152, 372, 328, 404], S3); t.ellipse([152, 366, 328, 398], S1)
for jx in (190, 240, 290): t.line([(jx, 424), (jx, 432)], S4)
for mx, my in [(150, 402), (318, 396), (196, 428)]: t.ellipse([mx, my, mx + 16, my + 6], MOSS)
# wheat tufts planted at the plinth's base corners (from the ref)
for bx in (146, 322):
    for k in range(5):
        t.line([(bx + 6, 398), (bx + k * 3, 372)], (240, 200, 40), width=2)
        t.ellipse([bx + k * 3 - 2, 364, bx + k * 3 + 3, 374], GOLD)
# cloak: wide column, deep side folds
t.polygon([(178, 150), (302, 150), (322, 372), (158, 372)], S2)
t.polygon([(178, 150), (202, 150), (196, 372), (158, 372)], S3)
t.polygon([(278, 150), (302, 150), (322, 372), (284, 372)], S3)
t.line([(176, 200), (172, 340)], S4); t.line([(304, 200), (308, 340)], S4)
t.rectangle([158, 362, 322, 372], S4)
# robe front
t.polygon([(208, 158), (272, 158), (278, 372), (202, 372)], S1)
t.line([(240, 280), (239, 360)], S2)
# gold throat clasp
t.polygon([(240, 168), (250, 178), (240, 188), (230, 178)], GOLD_D)
t.point((240, 178), GOLD_L)
# arms converge: both forearms angle in, hands cupped under the big gem
t.polygon([(186, 168), (216, 232), (232, 224), (204, 156)], S3)
t.polygon([(294, 168), (264, 232), (248, 224), (276, 156)], S3)
t.ellipse([216, 224, 240, 240], S2); t.ellipse([240, 224, 264, 240], S2)   # cupped hands
# THE BIG GEM — green diamond cradled at the belly
t.polygon([(240, 196), (262, 220), (240, 248), (218, 220)], GOLD_D)
t.polygon([(240, 202), (256, 220), (240, 241), (224, 220)], (46, 160, 84))
t.polygon([(240, 202), (248, 220), (240, 228), (232, 220)], (70, 190, 105))
t.point((234, 212), (170, 250, 185))
# belt below the gem
t.rectangle([206, 262, 274, 274], S4)
t.rectangle([232, 260, 248, 276], GOLD_D); t.rectangle([236, 264, 244, 272], S3)
# RIGHT hand + the sheaf-scepter: grip low, stalks rest on the plinth, plume fans high
t.ellipse([146, 208, 166, 226], S2)
for k in range(6):
    t.line([(156, 218), (156, 368)], (196, 150, 60), width=1)
for sx, tx in [(132, 122), (140, 134), (148, 146), (156, 156), (164, 168), (172, 178)]:
    t.line([(156, 218), (tx, 104)], (240, 200, 40), width=2)
    t.ellipse([tx - 4, 66, tx + 4, 100], GOLD)
    t.ellipse([tx - 2, 74, tx + 2, 94], GOLD_L)
    for aw in (-3, 0, 3): t.line([(tx + aw, 68), (tx + aw * 2, 54)], GOLD_D)
t.rectangle([148, 210, 166, 222], (146, 62, 78))
# head: light hair band, heavy brow, OPEN stern eyes angled down-in, nose,
# thick mustache over a straight mouth, jaw-frame beard (cheeks stay stone)
t.rectangle([206, 96, 274, 150], S2)
t.ellipse([210, 88, 270, 128], S1)
t.rectangle([208, 78, 272, 90], S1)                                        # hair band
t.rectangle([210, 102, 270, 109], S3)                                     # brow ledge
t.polygon([(220, 116), (233, 113), (233, 118), (221, 119)], K)            # left eye, angled
t.polygon([(260, 116), (247, 113), (247, 118), (259, 119)], K)            # right eye, angled
t.polygon([(240, 112), (235, 123), (245, 123)], S3)                       # nose
t.rectangle([240, 123, 243, 126], S4)
d2 = [(222, 126), (258, 126), (256, 133), (224, 133)]
t.polygon(d2, S2)                                                         # mustache mass
t.line([(232, 136), (248, 136)], K)                                       # straight stern mouth
t.polygon([(210, 118), (220, 118), (222, 152), (212, 156)], S2)           # beard, left jaw
t.polygon([(270, 118), (260, 118), (258, 152), (268, 156)], S2)           # beard, right jaw
t.polygon([(226, 140), (254, 140), (246, 160), (234, 160)], S2)           # chin tuft
for bx in (216, 264): t.line([(bx, 124), (bx, 148)], S3)
# crown: three proud points over the band
t.rectangle([208, 62, 272, 78], GOLD); t.rectangle([208, 73, 272, 78], GOLD_D)
for px, hgt in [(212, 18), (234, 24), (258, 18)]:
    t.polygon([(px, 64), (px + 6, 64 - hgt), (px + 12, 64)], GOLD)
    t.ellipse([px + 4, 62 - hgt, px + 8, 66 - hgt], GOLD_L)
# weathering — heavier: moss on forearm, cloak skirts, robe hem; cracks
t.ellipse([258, 196, 282, 210], MOSS)
t.ellipse([168, 322, 196, 340], MOSS)
t.ellipse([284, 330, 310, 346], MOSS_D)
t.ellipse([222, 348, 246, 358], MOSS_D)
t.ellipse([206, 56, 224, 64], MOSS)
t.line([(262, 292), (256, 312), (261, 330)], S4)

for px in (84, 512):
    d.rectangle([px, 428, px + 44, 446], fill=(90, 130, 70))
    d.rectangle([px - 2, 424, px + 46, 430], fill=S3)
    for rx, ry in [(8, -8), (22, -12), (34, -6)]:
        d.ellipse([px + rx, 428 + ry, px + rx + 12, 438 + ry], fill=GOLD)
        d.arc([px + rx + 2, 430 + ry, px + rx + 10, 436 + ry], 0, 300, fill=GOLD_D, width=2)
# --- foreground heads (the ref crop's depth cue): Pearl + a kid at the bottom edge ---
d.ellipse([128, 452, 160, 484], fill=(240, 230, 220)); d.ellipse([138, 446, 150, 456], fill=(240, 230, 220))
d.ellipse([486, 456, 516, 486], fill=(240, 205, 160)); d.rectangle([486, 452, 516, 462], fill=(110, 66, 38))

img.save('statue-scene-v2.png')
print('scene rendered', img.size)
