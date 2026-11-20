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

# --- the King, drawn through a transform (v3 figure, scaled into the scene) ---
class T:
    def __init__(self, dr, s, ox, oy): self.d, self.s, self.ox, self.oy = dr, s, ox, oy
    def P(self, pts): return [(x * self.s + self.ox, y * self.s + self.oy) for x, y in pts]
    def polygon(self, pts, fill): self.d.polygon(self.P(pts), fill=fill)
    def rectangle(self, b, fill): self.d.rectangle([b[0] * self.s + self.ox, b[1] * self.s + self.oy, b[2] * self.s + self.ox, b[3] * self.s + self.oy], fill=fill)
    def ellipse(self, b, fill): self.d.ellipse([b[0] * self.s + self.ox, b[1] * self.s + self.oy, b[2] * self.s + self.ox, b[3] * self.s + self.oy], fill=fill)
    def line(self, pts, fill, width=1): self.d.line(self.P(pts), fill=fill, width=max(1, int(width * self.s)))
    def point(self, p, fill): x, y = p[0] * self.s + self.ox, p[1] * self.s + self.oy; self.d.ellipse([x - 1, y - 1, x + 1, y + 1], fill=fill)
t = T(d, 0.78, 320 - 240 * 0.78, 306 - 372 * 0.78)
# plinth (from v3)
t.ellipse([128, 396, 352, 436], S3); t.ellipse([128, 390, 352, 430], S2)
t.ellipse([152, 372, 328, 404], S3); t.ellipse([152, 366, 328, 398], S1)
t.line([(170, 420), (186, 410), (182, 402)], S4)
for mx, my in [(150, 402), (318, 396), (196, 428)]: t.ellipse([mx, my, mx + 16, my + 6], MOSS)
# cloak + robe
t.polygon([(178, 150), (302, 150), (322, 372), (158, 372)], S2)
t.polygon([(178, 150), (202, 150), (196, 372), (158, 372)], S3)
t.polygon([(278, 150), (302, 150), (322, 372), (284, 372)], S3)
t.rectangle([158, 362, 322, 372], S4)
t.polygon([(208, 158), (272, 158), (278, 372), (202, 372)], S1)
for fx in (222, 240, 258): t.line([(fx, 210), (fx - 1, 358)], S2)
t.rectangle([204, 258, 276, 272], S4)
t.rectangle([230, 256, 250, 274], GOLD_D); t.rectangle([235, 261, 245, 269], S3)
# right arm + sheaf
t.polygon([(186, 168), (148, 214), (162, 228), (204, 186)], S3)
t.ellipse([146, 196, 166, 216], S2)
for sx, tx in [(138, 128), (146, 140), (152, 152), (158, 164), (164, 174)]:
    t.line([(156, 202), (tx, 108)], (240, 200, 40), width=2)
    t.ellipse([tx - 4, 78, tx + 4, 106], GOLD)
    t.ellipse([tx - 2, 84, tx + 2, 100], GOLD_L)
t.rectangle([148, 192, 166, 204], (146, 62, 78))
# left arm + gem
t.polygon([(292, 168), (252, 226), (228, 216), (262, 152)], S3)
t.ellipse([222, 208, 244, 224], S2)
t.polygon([(240, 182), (254, 196), (240, 212), (226, 196)], GOLD_D)
t.polygon([(240, 187), (249, 196), (240, 206), (231, 196)], (46, 160, 84))
# head + beard + crown
t.rectangle([206, 96, 274, 150], S2)
t.ellipse([210, 88, 270, 128], S1)
t.rectangle([210, 104, 270, 110], S3)
t.line([(220, 114), (232, 114)], K); t.line([(248, 114), (260, 114)], K)
t.polygon([(240, 114), (235, 124), (245, 124)], S3)
t.rectangle([222, 124, 258, 130], S2)
t.polygon([(218, 128), (262, 128), (252, 168), (228, 168)], S2)
for bx in (226, 234, 242, 250):
    t.line([(bx, 132), (bx - 1, 162)], S3); t.line([(bx + 3, 132), (bx + 2, 158)], S1)
t.rectangle([208, 72, 272, 88], GOLD); t.rectangle([208, 83, 272, 88], GOLD_D)
for i, px in enumerate((210, 226, 240, 254, 264)):
    hgt = 22 if i != 3 else 12
    t.polygon([(px, 74), (px + 5, 74 - hgt), (px + 10, 74)], GOLD)
t.ellipse([206, 66, 224, 74], MOSS)
t.ellipse([180, 156, 204, 168], MOSS)
t.ellipse([292, 336, 314, 348], MOSS_D)
# --- foreground heads (the ref crop's depth cue): Pearl + a kid at the bottom edge ---
d.ellipse([128, 452, 160, 484], fill=(240, 230, 220)); d.ellipse([138, 446, 150, 456], fill=(240, 230, 220))
d.ellipse([486, 456, 516, 486], fill=(240, 205, 160)); d.rectangle([486, 452, 516, 462], fill=(110, 66, 38))

img.save('statue-scene.png')
print('scene rendered', img.size)
