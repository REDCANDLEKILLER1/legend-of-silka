# The Weathered Harvest King — v2, higher pixels, drawn from Michael's ref crop.
# Ref truth: front-facing stocky king, cloak to the ground, wheat sheaf held upright
# at his right side, left hand over a GREEN chest gem in gold, big beard + mustache,
# downcast eyes, gold crown, moss on shoulders/plinth, round stepped plinth,
# flower ring at the base, cobble plaza rings.
from PIL import Image, ImageDraw
import math, random
random.seed(4)
W, H = 480, 480
img = Image.new('RGB', (W, H), (186, 177, 164))
d = ImageDraw.Draw(img)
K = (26, 24, 28)
S1 = (196, 188, 174); S2 = (172, 163, 148); S3 = (146, 138, 124); S4 = (118, 110, 98)
GOLD = (216, 178, 58); GOLD_D = (172, 136, 42); GOLD_L = (240, 205, 100)
MOSS = (74, 138, 72); MOSS_D = (52, 108, 56)

# --- plaza: concentric cobble rings
CX, CY = 240, 428
for r in (330, 268, 208, 152):
    d.ellipse([CX - r, CY - r // 3, CX + r, CY + r // 3], outline=S3, width=3)
for a in range(0, 360, 6):
    x0, y0 = CX + int(300 * math.cos(math.radians(a))), CY + int(96 * math.sin(math.radians(a)))
    x1, y1 = CX + int(322 * math.cos(math.radians(a))), CY + int(104 * math.sin(math.radians(a)))
    d.line([(x0, y0), (x1, y1)], fill=S3)
for _ in range(500):
    x, y = random.randrange(4, W - 4), random.randrange(300, H - 4)
    d.point((x, y), fill=random.choice([S1, S3]))
# flower ring hugging the plinth
for a in range(0, 360, 5):
    fx, fy = CX + int(118 * math.cos(math.radians(a))), 424 + int(20 * math.sin(math.radians(a)))
    if fy < 404: continue
    d.ellipse([fx - 3, fy - 2, fx + 3, fy + 2], fill=MOSS)
    d.point((fx, fy), fill=random.choice([(232, 93, 117), (245, 239, 230), (255, 210, 30)]))

# --- round stepped plinth ---
d.ellipse([128, 396, 352, 436], fill=S3); d.ellipse([128, 390, 352, 430], fill=S2)
d.ellipse([152, 372, 328, 404], fill=S3); d.ellipse([152, 366, 328, 398], fill=S1)
d.line([(170, 420), (186, 410), (182, 402)], fill=S4)                       # crack
for mx, my in [(150, 402), (318, 396), (196, 428)]:
    d.ellipse([mx, my, mx + 16, my + 6], fill=MOSS)

# --- THE KING (stocky like the ref — a chess-king of a statue) ---
# cloak: WIDE column, drape shade both sides
d.polygon([(178, 150), (302, 150), (322, 372), (158, 372)], fill=S2)
d.polygon([(178, 150), (202, 150), (196, 372), (158, 372)], fill=S3)
d.polygon([(278, 150), (302, 150), (322, 372), (284, 372)], fill=S3)
d.line([(172, 190), (168, 356)], fill=S4); d.line([(308, 190), (312, 356)], fill=S4)
d.rectangle([158, 362, 322, 372], fill=S4)
# robe front panel, wider
d.polygon([(208, 158), (272, 158), (278, 372), (202, 372)], fill=S1)
for fx in (222, 240, 258):
    d.line([(fx, 210), (fx - 1, 358)], fill=S2)
# belt + buckle
d.rectangle([204, 258, 276, 272], fill=S4)
d.rectangle([230, 256, 250, 274], fill=GOLD_D); d.rectangle([235, 261, 245, 269], fill=S3)
# RIGHT arm (viewer left): sleeve diagonal, fist up at his side gripping the sheaf
d.polygon([(186, 168), (148, 214), (162, 228), (204, 186)], fill=S3)
d.ellipse([146, 196, 166, 216], fill=S2)
# THE SHEAF: five separated stalks, teardrop heads with air between them
for sx, tx in [(138, 128), (146, 140), (152, 152), (158, 164), (164, 174)]:
    d.line([(156, 202), (tx, 108)], fill=(240, 200, 40), width=2)
    d.ellipse([tx - 4, 78, tx + 4, 106], fill=GOLD)
    d.ellipse([tx - 2, 84, tx + 2, 100], fill=GOLD_L)
    for aw in (-3, 0, 3):
        d.line([(tx + aw, 80), (tx + aw * 2, 68)], fill=GOLD_D)
d.rectangle([148, 192, 166, 204], fill=(146, 62, 78))
# LEFT arm: shaded sleeve band across the belly, mitten hand under the gem
d.polygon([(292, 168), (252, 226), (228, 216), (262, 152)], fill=S3)
d.ellipse([222, 208, 244, 224], fill=S2)
# THE GEM — green, gold setting, sternum (per the ref)
d.polygon([(240, 182), (254, 196), (240, 212), (226, 196)], fill=GOLD_D)
d.polygon([(240, 187), (249, 196), (240, 206), (231, 196)], fill=(46, 160, 84))
d.point((236, 192), fill=(150, 240, 170))
# head: shorter, wider — face, brow, downcast eyes, nose, mustache, STRAND beard
d.rectangle([206, 96, 274, 150], fill=S2)
d.ellipse([210, 88, 270, 128], fill=S1)
d.rectangle([210, 104, 270, 110], fill=S3)
d.line([(220, 114), (232, 114)], fill=K); d.line([(248, 114), (260, 114)], fill=K)
d.polygon([(240, 114), (235, 124), (245, 124)], fill=S3)
d.rectangle([222, 124, 258, 130], fill=S2)                                    # mustache band
d.polygon([(218, 128), (262, 128), (252, 168), (228, 168)], fill=S2)          # beard mass
for bx in (226, 234, 242, 250):
    d.line([(bx, 132), (bx - 1, 162)], fill=S3)
    d.line([(bx + 3, 132), (bx + 2, 158)], fill=S1)
# crown: band + five points, ball tips, second-from-right chipped
d.rectangle([208, 72, 272, 88], fill=GOLD); d.rectangle([208, 83, 272, 88], fill=GOLD_D)
for i, px in enumerate((210, 226, 240, 254, 264)):
    hgt = 22 if i != 3 else 12
    d.polygon([(px, 74), (px + 5, 74 - hgt), (px + 10, 74)], fill=GOLD)
    if i != 3: d.ellipse([px + 3, 72 - hgt, px + 7, 76 - hgt], fill=GOLD_L)
d.point((240, 79), fill=(46, 160, 84))
# weathering
d.ellipse([206, 66, 224, 74], fill=MOSS)
d.ellipse([180, 156, 204, 168], fill=MOSS)
d.ellipse([292, 336, 314, 348], fill=MOSS_D)
d.line([(262, 292), (256, 312), (261, 330)], fill=S4)
d.line([(214, 306), (220, 322)], fill=S4)

img = img.resize((W * 2, H * 2), Image.NEAREST)
img.save('statue-closeup-v3.png')
print('statue v2 rendered', img.size)
