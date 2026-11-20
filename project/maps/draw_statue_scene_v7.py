# The King — v3 COLOR pass. Michael: "It's the colors. Look at the shadows and
# subtle things." Light from the UPPER LEFT, everything shaded against it:
# 5-tone stone, crown shadow on the brow, fold grooves with lit edges, the gem's
# facets + its shadow on the robe, per-stone plaza variation, cast shadows.
from PIL import Image, ImageDraw
import math, random
random.seed(21)
W, H = 640, 480
img = Image.new('RGB', (W, H), (190, 182, 170))
d = ImageDraw.Draw(img)
ov = Image.new('RGBA', (W, H), (0, 0, 0, 0)); od = ImageDraw.Draw(ov)
K = (30, 26, 28)
# stone, warm grey, five tones lit->deep
S0 = (214, 206, 190); S1 = (196, 188, 172); S2 = (172, 163, 146); S3 = (142, 133, 118); S4 = (110, 101, 90)
G0 = (246, 214, 110); G1 = (222, 182, 66); G2 = (196, 152, 48); G3 = (158, 116, 34)
M0 = (110, 180, 96); M1 = (78, 142, 74); M2 = (54, 110, 56)
SH = (20, 30, 22, 66)   # soft shadow overlay

# ---------- environment ----------
d.rectangle([0, 0, W, 26], fill=(172, 182, 200))
d.rectangle([0, 26, W, 62], fill=(158, 160, 172))
for x in range(0, W, 32):
    d.rectangle([x, 18, x + 18, 30], fill=(166, 168, 180))
    d.rectangle([x, 56, x + 32, 62], fill=(138, 140, 152))          # shadow under wall walk
for bx in range(4, W, 46):
    d.rectangle([bx, 30, bx + 20, 58], outline=(140, 142, 154))      # block joints
# cliff: strata with a shadow line under every ledge, warm light on top edges
d.rectangle([0, 62, W, 148], fill=(172, 132, 82))
y = 66
while y < 146:
    hh = random.randrange(8, 15)
    d.rectangle([0, y + hh - 3, W, y + hh], fill=(128, 92, 52))       # ledge shadow
    d.line([(0, y), (W, y)], fill=(196, 156, 100))                    # ledge light
    y += hh
for _ in range(200):
    x, yy = random.randrange(0, W), random.randrange(66, 142)
    d.line([(x, yy), (x + random.choice((-3, 3)), yy + random.randrange(5, 13))], fill=random.choice([(146, 106, 60), (188, 148, 94), (118, 82, 46)]))
d.rectangle([0, 144, W, 152], fill=(104, 72, 40))
# grass: mid base, lit patches upper-left, darker toward the plaza rim
d.rectangle([0, 152, W, H], fill=(66, 146, 70))
for _ in range(46):
    x, y = random.randrange(0, W), random.randrange(156, 300)
    d.ellipse([x, y, x + random.randrange(24, 60), y + random.randrange(6, 12)], fill=(76, 158, 78))
for _ in range(500):
    x, y = random.randrange(2, W - 2), random.randrange(156, H - 2)
    d.line([(x, y), (x, y - 3)], fill=random.choice([(116, 206, 96), (52, 120, 56)]))
def tree(cx, cy, r=26):
    od.ellipse([cx - r, cy + r - 2, cx + r + 16, cy + r + 12], fill=SH)   # ground shadow
    d.rectangle([cx - 3, cy + r - 4, cx + 3, cy + r + 10], fill=(96, 62, 36))
    d.rectangle([cx - 3, cy + r - 4, cx, cy + r + 10], fill=(120, 84, 48))
    for ox, oy, rr in [(-14, 6, r - 6), (14, 6, r - 6), (0, -8, r)]:
        d.ellipse([cx + ox - rr, cy + oy - rr, cx + ox + rr, cy + oy + rr], fill=M1)
        d.pieslice([cx + ox - rr, cy + oy - rr, cx + ox + rr, cy + oy + rr], 180, 300, fill=M0)
        d.pieslice([cx + ox - rr, cy + oy - rr, cx + ox + rr, cy + oy + rr], 300, 360, fill=M2)
tree(84, 176); tree(556, 176); tree(140, 200, 20); tree(500, 200, 20)
# plaza: every stone its own tone, dark grout, rings in perspective
CX, CY = 320, 348
d.ellipse([CX - 262, CY - 66, CX + 262, CY + 66], fill=(150, 141, 126))
for yy in range(CY - 60, CY + 62, 11):
    for xx in range(CX - 250, CX + 250, 22):
        if ((xx - CX) / 258) ** 2 + ((yy - CY) / 64) ** 2 < 1:
            d.rounded_rectangle([xx + 1, yy + 1, xx + 21, yy + 10], 2, fill=random.choice([S0, S1, S1, S2]))
for r in (262, 216, 172):
    d.ellipse([CX - r, CY - int(r * 0.252), CX + r, CY + int(r * 0.252)], outline=S4, width=2)
# flower ring: dark bed, mid leaves, lit blossoms (light pixel upper-left of each)
for a in range(0, 360, 4):
    fx, fy = CX + int(178 * math.cos(math.radians(a))), CY + int(45 * math.sin(math.radians(a)))
    d.ellipse([fx - 4, fy - 3, fx + 4, fy + 3], fill=M2)
    c = random.choice([(232, 93, 117), (245, 239, 230), (255, 210, 30), (240, 160, 200)])
    d.point((fx - 1, fy - 1), fill=c); d.point((fx, fy), fill=c)

# ---------- the King (direct coords; base at plinth top y=306, center x=320) ----------
# CAST SHADOW first: long, low, to the lower-left across the plaza
od.polygon([(268, 330), (352, 330), (300, 372), (196, 366)], fill=SH)
od.ellipse([226, 356, 420, 382], fill=(20, 30, 22, 50))
# plinth tiers: lit tops, shaded fronts, contact shadow under each tier
d.ellipse([208, 316, 432, 356], fill=S3); d.ellipse([208, 310, 432, 350], fill=S2)
d.ellipse([232, 292, 408, 324], fill=S3); d.ellipse([232, 286, 408, 318], fill=S1)
od.ellipse([232, 306, 408, 330], fill=(20, 30, 22, 40))
for jx in (268, 320, 372): d.line([(jx, 336), (jx, 348)], fill=S4)
for mx, my in [(238, 322), (392, 316), (282, 344)]:
    d.ellipse([mx, my, mx + 14, my + 5], fill=M1); d.point((mx + 3, my + 1), fill=M0)
for bx in (222, 404):   # corn offerings at the base corners
    for k, dx in enumerate((-5, 0, 5)):
        cx = bx + 5 + dx
        d.line([(bx + 5, 318), (cx, 302)], fill=(84, 150, 70), width=2)
        d.polygon([(cx - 3, 302), (cx + 3, 302), (cx + 1, 288), (cx, 284), (cx - 1, 288)], fill=G1)
        d.polygon([(cx - 3, 302), (cx, 302), (cx - 1, 288), (cx, 284)], fill=G0)
        for ky in range(290, 300, 3): d.line([(cx - 2, ky), (cx + 2, ky)], fill=G3)
# CLOAK — five tones: lit left ridge, mid panels, deep right; grooves dark + lit lip
d.polygon([(282, 118), (358, 118), (372, 306), (268, 306)], fill=S2)
d.polygon([(282, 118), (300, 118), (296, 306), (268, 306)], fill=S1)       # lit left drape
d.polygon([(338, 118), (358, 118), (372, 306), (344, 306)], fill=S4)       # deep right drape
d.polygon([(304, 122), (310, 122), (306, 300), (298, 300)], fill=S3)       # groove shadow
d.line([(312, 124), (308, 298)], fill=S0)                                   # groove's lit lip
d.rectangle([268, 296, 372, 306], fill=S4)                                  # hem shadow band
# ROBE front — lit center fading to shade at both seams
d.polygon([(300, 128), (340, 128), (344, 306), (296, 306)], fill=S0)
d.polygon([(336, 128), (340, 128), (344, 306), (338, 306)], fill=S2)
d.line([(320, 218), (319, 296)], fill=S2)
# throat clasp — gold, lit top facet
d.polygon([(320, 132), (328, 140), (320, 149), (312, 140)], fill=G2)
d.polygon([(320, 132), (328, 140), (320, 140)], fill=G0)
# arms in, hands cupped — sleeves shaded, hands lit on top, shadowed under
d.polygon([(288, 130), (312, 182), (326, 174), (306, 120)], fill=S3)
d.polygon([(352, 130), (328, 182), (314, 174), (334, 120)], fill=S4)
d.ellipse([304, 174, 322, 188], fill=S1); d.ellipse([318, 174, 336, 188], fill=S2)
od.ellipse([304, 184, 336, 194], fill=(20, 30, 22, 60))                     # hands' shadow on robe
# THE BIG GEM — faceted: bright upper-left, mid heart, deep lower-right, glint
d.polygon([(320, 152), (338, 172), (320, 196), (302, 172)], fill=G3)
d.polygon([(320, 152), (338, 172), (320, 196), (302, 172)], outline=G2)
d.polygon([(320, 157), (333, 172), (320, 189), (307, 172)], fill=(52, 172, 92))
d.polygon([(320, 157), (333, 172), (320, 172), (307, 172)], fill=(96, 214, 128))
d.polygon([(313, 163), (322, 163), (320, 172), (315, 172)], fill=(178, 255, 196))
# belt
d.rectangle([298, 202, 342, 212], fill=S4)
d.rectangle([314, 200, 326, 214], fill=G2); d.rectangle([317, 204, 323, 210], fill=S3)
# CORN-STALK SCEPTER at his right: green stalks resting on the plinth, long
# leaves arching out, golden cobs fanning at the top — kernels, husks, silk.
for k in range(5):   # the stalk bundle below the fist
    d.line([(269 + k * 2, 176), (269 + k * 2, 292)], fill=(74, 140, 66), width=2)
d.line([(269, 176), (269, 292)], fill=(110, 180, 96))
for lx, tx, ty in [(270, 232, 128), (274, 312, 122), (271, 244, 104), (273, 300, 100)]:
    d.polygon([(lx, 168), (tx, ty), (tx + 6, ty + 4), (lx + 3, 172)], fill=(84, 150, 70))
    d.polygon([(lx, 168), (tx, ty), (tx + 2, ty + 3), (lx + 1, 170)], fill=(110, 180, 96))
d.ellipse([262, 164, 280, 180], fill=S2)                                    # gripping fist
d.rectangle([264, 168, 280, 178], fill=(146, 62, 78))                       # harvest-red tie
def cob(cx, top, h=58, wdt=11, lean=0):
    bot = top + h
    d.polygon([(cx - wdt // 2, bot), (cx - wdt // 2 + 1, top + 8), (cx + lean, top), (cx + wdt // 2 - 1, top + 8), (cx + wdt // 2, bot)], fill=G1)
    d.polygon([(cx - wdt // 2, bot), (cx - wdt // 2 + 1, top + 8), (cx + lean, top), (cx, bot)], fill=G0)   # lit left half
    for ky in range(top + 8, bot - 2, 5):                                    # kernel rows
        d.line([(cx - wdt // 2 + 1, ky), (cx + wdt // 2 - 1, ky)], fill=G3)
        for kx in range(cx - wdt // 2 + 3, cx + wdt // 2 - 1, 4):
            d.point((kx, ky + 2), fill=G2)
    for sx in (-3, 0, 3):                                                    # silk at the tip
        d.line([(cx + lean + sx // 2, top + 2), (cx + lean + sx, top - 6)], fill=(232, 205, 150))
    d.polygon([(cx - wdt // 2, bot), (cx - 2, bot - 10), (cx - 1, bot + 6)], fill=(140, 190, 110))  # husk peeling
    d.polygon([(cx + wdt // 2, bot), (cx + 2, bot - 10), (cx + 1, bot + 6)], fill=(110, 168, 88))
for cx, top, lean in [(240, 44, -4), (256, 34, -2), (272, 30, 0), (288, 34, 2), (302, 46, 4)]:
    d.line([(272, 170), (cx, top + 56)], fill=(74, 140, 66), width=2)        # stalk rising to each cob
    cob(cx, top, lean=lean)
od.polygon([(282, 130), (296, 130), (292, 240), (280, 240)], fill=(20, 30, 22, 36))  # stalk shadow on cloak
# HEAD — v5 from Michael's face zoom: the beard is DARK charcoal against the pale
# face, eyes sit in a shadowed socket band, mustache is a thick horseshoe over a
# grim downturned mouth, crown chunky and wide over a pale brow band.
d.rectangle([292, 64, 348, 110], fill=S2)                                   # hair mass
d.ellipse([297, 58, 343, 97], fill=S1)                                      # face
d.rectangle([300, 84, 340, 102], fill=S1)                                   # square jaw
d.pieslice([297, 58, 343, 97], 270, 360, fill=S2)                           # right shade
d.rectangle([297, 72, 343, 80], fill=S3)                                    # crown shadow band
od.rectangle([297, 76, 343, 84], fill=(20, 18, 16, 60))                     # socket shadow
d.polygon([(305, 85), (317, 82), (317, 87), (306, 88)], fill=K)             # heavy eyes
d.polygon([(335, 85), (323, 82), (323, 87), (334, 88)], fill=K)
d.line([(305, 82), (317, 80)], fill=S4); d.line([(335, 82), (323, 80)], fill=S4)  # lids
d.polygon([(320, 82), (315, 94), (325, 94)], fill=S2)                       # broad nose
d.point((317, 94), fill=S4); d.point((323, 94), fill=S4)
d.line([(324, 84), (325, 93)], fill=S3)                                     # nose shadow side
d.arc([300, 84, 314, 98], 300, 40, fill=S2); d.arc([326, 84, 340, 98], 140, 240, fill=S3)  # cheek shade
# MUSTACHE — two dark wings under the nose; the mouth shows beneath them
d.polygon([(318, 94), (304, 96), (303, 103), (312, 105), (318, 100)], fill=(96, 88, 82))
d.polygon([(322, 94), (336, 96), (337, 103), (328, 105), (322, 100)], fill=(70, 63, 58))
for mx in (307, 311, 329, 333):
    d.line([(mx, 97), (mx - 1, 102)], fill=(130, 121, 113))
d.arc([313, 99, 327, 109], 200, 340, fill=K)                                # grim mouth, visible
d.point((320, 108), fill=S2)                                                # chin light below the mouth
# BEARD — frame only: jaw edges + a chin crescent; the face stays stone
d.polygon([(297, 86), (306, 86), (307, 120), (299, 126)], fill=(96, 88, 82))
d.polygon([(343, 86), (334, 86), (333, 120), (341, 126)], fill=(70, 63, 58))
d.polygon([(307, 112), (333, 112), (326, 130), (314, 130)], fill=(96, 88, 82))
for bx in (301, 316, 320, 324, 339):
    d.line([(bx, 92), (bx - 1, 120)], fill=(130, 121, 113))
d.line([(320, 114), (320, 128)], fill=(130, 121, 113))                               # grey center strand
# shoulder rolls — big rounded caps like the ref
d.ellipse([276, 112, 310, 138], fill=S1); d.pieslice([276, 112, 310, 138], 0, 90, fill=S2)
d.ellipse([330, 112, 364, 138], fill=S2); d.pieslice([330, 112, 364, 138], 0, 90, fill=S4)
# CROWN — chunky, full head width, dark seat shadow, lit left faces
d.rectangle([294, 56, 346, 62], fill=S4)
for px, hgt in [(296, 16), (313, 22), (330, 16)]:
    d.polygon([(px - 1, 58), (px + 6, 58 - hgt - 1), (px + 13, 58)], fill=K)
    d.polygon([(px, 57), (px + 6, 57 - hgt), (px + 12, 57)], fill=G1)
    d.polygon([(px, 57), (px + 6, 57 - hgt), (px + 6, 57)], fill=G0)
    d.ellipse([px + 4, 55 - hgt, px + 8, 59 - hgt], fill=G0)
d.rectangle([294, 44 + 14, 346, 58], fill=G1); d.rectangle([294, 53, 346, 58], fill=G3)
d.point((320, 50), fill=(52, 172, 92))
d.ellipse([294, 38, 306, 45], fill=M1); d.point((298, 40), fill=M0)

# weathering speckle + cracks on the stone
for _ in range(120):
    x, y = random.randrange(272, 368), random.randrange(110, 300)
    d.point((x, y), fill=random.choice([S1, S3]))
d.line([(338, 226), (333, 244), (337, 260)], fill=S4)
# rose planters, shaded boxes with lit roses
for px in (84, 512):
    d.rectangle([px, 428, px + 44, 446], fill=(84, 122, 64))
    d.rectangle([px, 428, px + 44, 432], fill=M2)
    d.rectangle([px - 2, 422, px + 46, 428], fill=S3)
    for rx, ry in [(8, -8), (22, -12), (34, -6)]:
        d.ellipse([px + rx, 428 + ry, px + rx + 12, 438 + ry], fill=G1)
        d.arc([px + rx + 2, 430 + ry, px + rx + 9, 436 + ry], 180, 330, fill=G0, width=2)
# foreground heads
d.ellipse([128, 452, 160, 484], fill=(240, 230, 220)); d.ellipse([138, 446, 150, 456], fill=(240, 230, 220))
d.ellipse([486, 456, 516, 486], fill=(240, 205, 160)); d.rectangle([486, 452, 516, 462], fill=(110, 66, 38))

img = Image.alpha_composite(img.convert('RGBA'), ov).convert('RGB')
img = img.resize((W * 2, H * 2), Image.NEAREST)
img.save('statue-scene-v7.png')
print('scene v3 rendered', img.size)
