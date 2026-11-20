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

# --- THE KING (stocky, ~2.2 heads) ---
# cloak: broad column flaring to the plinth, drape shading on both sides
d.polygon([(196, 128), (284, 128), (306, 372), (174, 372)], fill=S2)
d.polygon([(196, 128), (214, 128), (206, 372), (174, 372)], fill=S3)        # left drape shade
d.polygon([(266, 128), (284, 128), (306, 372), (274, 372)], fill=S3)        # right drape shade
for fx in (188, 296):
    d.line([(fx, 160), (fx - 4, 360)], fill=S4)                             # fold lines
d.rectangle([174, 364, 306, 372], fill=S4)                                  # hem shadow
# robe front panel
d.polygon([(218, 140), (262, 140), (268, 372), (212, 372)], fill=S1)
d.polygon([(218, 140), (240, 168), (262, 140), (258, 128), (222, 128)], fill=S2)  # V opening
for fx in (228, 240, 252):
    d.line([(fx, 190), (fx, 360)], fill=S2)
# belt + buckle
d.rectangle([214, 246, 266, 258], fill=S4)
d.rectangle([232, 244, 248, 260], fill=GOLD_D); d.rectangle([236, 248, 244, 256], fill=S3)
# RIGHT arm (viewer left): forearm up, fist gripping the sheaf at his side
d.polygon([(200, 150), (168, 196), (180, 208), (212, 168)], fill=S2)
d.polygon([(168, 196), (158, 168), (172, 162), (180, 208)], fill=S3)        # forearm
d.ellipse([156, 152, 174, 170], fill=S2)                                    # fist
# THE SHEAF: bound bundle, stalks vertical, grain heads layered at top
for i, sx in enumerate(range(146, 178, 4)):
    top = 66 + (abs(i - 4) * 3)
    d.line([(165, 158), (sx, top + 26)], fill=(240, 200, 40), width=2)
    for gy in range(top, top + 26, 6):
        d.ellipse([sx - 3, gy, sx + 3, gy + 7], fill=GOLD)
        d.point((sx, gy + 2), fill=GOLD_L)
d.rectangle([158, 148, 174, 158], fill=(146, 62, 78))                       # harvest-red tie
# LEFT arm across the belly, hand resting over the gem
d.polygon([(280, 150), (262, 210), (238, 218), (246, 196), (266, 140)], fill=S2)
d.ellipse([232, 206, 250, 220], fill=S2)
# THE GEM — green, gold setting, at the sternum (per the ref)
d.polygon([(240, 176), (252, 188), (240, 202), (228, 188)], fill=GOLD_D)
d.polygon([(240, 180), (248, 188), (240, 197), (232, 188)], fill=(46, 160, 84))
d.point((237, 185), fill=(150, 240, 170))
# head: heavy brow, downcast eyes, nose, mustache, layered beard
d.rectangle([214, 84, 266, 128], fill=S2)                                   # hair mass
d.ellipse([218, 78, 262, 116], fill=S1)                                     # face
d.rectangle([218, 94, 262, 99], fill=S3)                                    # brow ledge
d.line([(226, 103), (236, 103)], fill=K); d.line([(244, 103), (254, 103)], fill=K)  # downcast eyes
d.polygon([(240, 103), (236, 112), (244, 112)], fill=S3)                    # nose
d.pieslice([222, 106, 258, 124], 0, 180, fill=S2)                           # mustache
for bx in range(222, 258, 6):
    d.arc([bx, 112, bx + 8, 136], 0, 180, fill=S3)                          # beard scallops
    d.arc([bx, 122, bx + 8, 142], 0, 180, fill=S3)
# crown: band + five points, ball tips, the middle-right point chipped
d.rectangle([216, 66, 264, 80], fill=GOLD); d.rectangle([216, 76, 264, 80], fill=GOLD_D)
for i, px in enumerate((218, 229, 240, 251, 262)):
    hgt = 20 if i != 3 else 11                                              # chipped point
    d.polygon([(px, 68), (px + 4, 68 - hgt), (px + 8, 68)], fill=GOLD)
    if i != 3: d.ellipse([px + 2, 66 - hgt, px + 6, 70 - hgt], fill=GOLD_L)
d.point((240, 72), fill=(46, 160, 84))                                      # crown stone matches chest
# weathering: moss on crown + left shoulder + cloak hem; fine cracks
d.ellipse([216, 60, 230, 68], fill=MOSS)
d.ellipse([192, 132, 214, 144], fill=MOSS)
d.ellipse([282, 340, 302, 352], fill=MOSS_D)
d.line([(258, 280), (252, 300), (257, 318)], fill=S4)
d.line([(206, 300), (212, 316)], fill=S4)

img = img.resize((W * 2, H * 2), Image.NEAREST)
img.save('statue-closeup-v2.png')
print('statue v2 rendered', img.size)
