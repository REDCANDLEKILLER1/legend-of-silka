# Houses close-up sheet — 2x2, scene standard: upper-left light, shadows, detail.
# General Store, open-air Blacksmith Forge, Pearl's Cottage, Harvest Inn.
from PIL import Image, ImageDraw
import random
random.seed(7)
W, H = 480, 380
img = Image.new('RGB', (W, H), (62, 142, 65))
d = ImageDraw.Draw(img)
ov = Image.new('RGBA', (W, H), (0, 0, 0, 0)); od = ImageDraw.Draw(ov)
K = (26, 24, 28)
SH = (20, 30, 22, 70)
GRASS_L = (110, 201, 91)

def ground(x0, y0, w, h):
    for _ in range(90):
        x, y = random.randrange(x0 + 2, x0 + w - 2), random.randrange(y0 + 4, y0 + h - 2)
        d.line([(x, y), (x, y - 3)], fill=GRASS_L)
    for cx, cy in [(x0 + 30, y0 + h - 14), (x0 + w - 40, y0 + h - 8)]:
        d.point((cx, cy), fill=(245, 239, 230)); d.point((cx + 2, cy + 1), fill=(232, 93, 117))
def roof_scallop(x0, y0, x1, color, dark, light):
    d.rectangle([x0 - 3, y0 + 3, x1 + 3, y0 + 16], fill=color)
    d.rectangle([x0 - 3, y0, x1 + 3, y0 + 3], fill=light)
    for ry in range(y0 + 6, y0 + 15, 4):
        for sx in range(x0, x1, 8):
            d.arc([sx, ry, sx + 8, ry + 5], 0, 180, fill=dark)
    d.rectangle([x0 - 3, y0 + 15, x1 + 3, y0 + 17], fill=dark)
    od.rectangle([x0 - 3, y0 + 17, x1 + 3, y0 + 20], fill=SH)   # eave shadow on the wall
def door(cx, y0, crest=True):
    d.rectangle([cx - 8, y0, cx + 8, y0 + 24], fill=K)
    d.rectangle([cx - 7, y0 + 1, cx + 7, y0 + 24], fill=(194, 185, 173))
    d.rectangle([cx - 5, y0 + 3, cx + 5, y0 + 24], fill=(110, 66, 38))
    d.line([(cx, y0 + 4), (cx, y0 + 24)], fill=(92, 58, 33))
    if crest:
        d.polygon([(cx, y0 + 7), (cx + 3, y0 + 10), (cx, y0 + 14), (cx - 3, y0 + 10)], fill=(255, 210, 30))
    d.rectangle([cx - 7, y0 + 24, cx + 7, y0 + 27], fill=(140, 133, 123))
def window(cx, y0, warm=True):
    d.rectangle([cx - 7, y0, cx + 7, y0 + 12], fill=K)
    d.rectangle([cx - 6, y0 + 1, cx + 6, y0 + 11], fill=(255, 210, 30) if warm else (140, 180, 210))
    d.line([(cx, y0 + 1), (cx, y0 + 11)], fill=K); d.line([(cx - 6, y0 + 6), (cx + 6, y0 + 6)], fill=K)
    d.rectangle([cx - 8, y0 + 12, cx + 8, y0 + 14], fill=(158, 104, 56))
    for fx in range(cx - 6, cx + 7, 4):
        d.point((fx, y0 + 11), fill=(232, 93, 117)); d.point((fx + 1, y0 + 12), fill=(245, 239, 230))
def timber(x0, y0, x1, y1):
    d.rectangle([x0, y0, x1, y1], fill=(245, 239, 230))
    for tx in range(x0 + 12, x1 - 4, 24):
        d.rectangle([tx, y0, tx + 3, y1], fill=(92, 58, 33))
    d.rectangle([x0, y0, x1, y0 + 3], fill=(92, 58, 33)); d.rectangle([x0, y1 - 3, x1, y1], fill=(92, 58, 33))
    d.rectangle([x0, y0, x0 + 3, y1], fill=(92, 58, 33)); d.rectangle([x1 - 3, y0, x1, y1], fill=(92, 58, 33))
    d.line([(x1 - 3, y0 + 4), (x1, y1)], fill=(70, 46, 26))   # right-side shade

# ================= STORE (top-left, 0..240 x 0..190) =================
ground(0, 120, 240, 70)
timber(28, 76, 196, 130)
roof_scallop(28, 58, 196, (184, 58, 45), (140, 40, 34), (210, 80, 62))
d.rectangle([196, 76, 210, 86], fill=(158, 104, 56))   # chimney
door(70, 104)
window(150, 84)
d.rectangle([120, 62, 150, 76], fill=(158, 104, 56))   # hanging sign board
d.line([(126, 58), (126, 62)], fill=K); d.line([(144, 58), (144, 62)], fill=K)
d.point((135, 70), fill=(255, 210, 30))
d.polygon([(132, 66), (135, 73), (138, 66)], fill=(255, 210, 30))
for bx, by in [(188, 122), (196, 126), (30, 124)]:    # barrels + crate
    d.rectangle([bx, by, bx + 12, by + 10], fill=(158, 104, 56))
    d.line([(bx, by + 3), (bx + 12, by + 3)], fill=(92, 58, 33))
    d.line([(bx, by + 7), (bx + 12, by + 7)], fill=(92, 58, 33))
# ================= FORGE (top-right, 240..480) =================
ground(240, 120, 240, 70)
d.rectangle([288, 76, 340, 130], fill=(168, 160, 148))  # stone furnace
d.rectangle([288, 76, 292, 130], fill=(196, 188, 172))
d.rectangle([300, 92, 330, 118], fill=K)
d.polygon([(302, 116), (306, 98), (312, 112), (315, 96), (322, 116)], fill=(255, 106, 26))
d.polygon([(306, 116), (312, 100), (318, 116)], fill=(255, 210, 30))
d.rectangle([300, 118, 330, 122], fill=(140, 133, 123))
d.rectangle([288, 70, 340, 76], fill=(120, 112, 100))
for sy in (58, 64): d.ellipse([312, sy, 324, sy + 10], fill=(220, 220, 220))
# open roof on posts + anvil
d.rectangle([352, 70, 356, 132], fill=(92, 58, 33)); d.rectangle([440, 70, 444, 132], fill=(92, 58, 33))
d.polygon([(344, 58), (452, 58), (446, 70), (350, 70)], fill=(140, 46, 38))
d.rectangle([376, 118, 420, 126], fill=(90, 90, 100))  # anvil body
d.polygon([(376, 118), (368, 112), (376, 112)], fill=(140, 140, 150))
d.rectangle([392, 126, 404, 138], fill=(92, 58, 33))
d.rectangle([348, 132, 362, 140], fill=(158, 104, 56))  # ingots
d.line([(352, 136), (358, 136)], fill=(240, 200, 40))
# ================= COTTAGE (bottom-left) =================
ground(0, 310, 240, 70)
d.rectangle([40, 268, 184, 320], fill=(245, 239, 230))
d.rectangle([40, 268, 44, 320], fill=(92, 58, 33)); d.rectangle([180, 268, 184, 320], fill=(92, 58, 33))
roof_scallop(40, 246, 184, (214, 178, 90), (170, 140, 60), (240, 210, 130))  # golden thatch
d.rectangle([150, 240, 164, 250], fill=(158, 104, 56))   # chimney + smoke
d.ellipse([154, 228, 164, 238], fill=(230, 230, 230))
door(84, 292)
window(146, 276)
d.rectangle([196, 312, 208, 322], fill=(158, 104, 56)); d.rectangle([196, 312, 208, 314], fill=(92, 58, 33))
# ================= INN (bottom-right) =================
ground(240, 310, 240, 70)
d.rectangle([288, 250, 452, 320], fill=(245, 239, 230))
d.rectangle([288, 250, 292, 320], fill=(92, 58, 33)); d.rectangle([448, 250, 452, 320], fill=(92, 58, 33))
d.rectangle([288, 276, 452, 280], fill=(190, 178, 160))
roof_scallop(288, 228, 452, (122, 48, 64), (94, 36, 50), (146, 62, 78))
door(372, 292)
window(316, 258); window(428, 258); window(316, 290)
d.rectangle([400, 238, 428, 246], fill=(158, 104, 56)); d.line([(404, 242), (424, 242)], fill=(60, 38, 20))
d.ellipse([296, 308, 316, 318], fill=(240, 200, 40))     # hay bale
d.rectangle([292, 296, 298, 302], fill=(255, 210, 30))   # lantern by the door

img = Image.alpha_composite(img.convert('RGBA'), ov).convert('RGB')
img = img.resize((W * 2, H * 2), Image.NEAREST)
img.save('houses-closeup.png')
print('houses sheet rendered', img.size)
