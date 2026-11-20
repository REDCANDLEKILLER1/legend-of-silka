# DETAIL PASS lineup — Corn Man, Harvest King, Storm Wizard at the ALttP bar:
# 3-4 tones per surface, textured hair/beards, tailored clothes, one prop each.
# Designs unchanged (Corn Man = canon); this is shading/texture, not redesign.
from PIL import Image, ImageDraw
FW, FH = 76, 92
img = Image.new('RGB', (FW * 3 + 16, FH + 8), (38, 48, 66))
d = ImageDraw.Draw(img)
def R(x, y, w, h, c): d.rectangle([x, y, x + w - 1, y + h - 1], fill=c)
def P(x, y, c): d.point((x, y), fill=c)

# ============ CORN MAN (offset 4) ============
ox = 4
G1, G2, G3 = (255, 217, 26), (224, 170, 0), (255, 233, 112)      # kernel golds
H1, H2, H3 = (46, 158, 68), (30, 110, 46), (92, 196, 106)       # husk greens
# cape behind (sides + hem)
for yy in range(30, 84, 4):
    R(ox + 6, yy, 6, 4, (158, 26, 18)); R(ox + 60, yy, 6, 4, (158, 26, 18))
R(ox + 12, 82, 48, 4, (120, 18, 12))
# head: kernel face with per-kernel shading
R(ox + 16, 6, 40, 38, G2)
for ky in range(0, 6):
    for kx in range(0, 6):
        x, y = ox + 18 + kx * 6, 8 + ky * 6
        R(x, y, 5, 5, G1); P(x, y, G3); P(x + 4, y + 4, G2)
# husk frames with veins
for side, sx in [(0, ox + 10), (1, ox + 56)]:
    R(sx, 4, 8, 44, H2); R(sx + (1 if side == 0 else 3), 6, 4, 40, H1)
    for vy in range(10, 44, 8): P(sx + 3, vy, H3); P(sx + 4, vy + 1, H2)
R(ox + 14, 2, 44, 5, H2); R(ox + 20, 0, 32, 4, H1)               # husk crown
# sunglasses: two lenses, bridge, nose pixel, glint
R(ox + 20, 22, 13, 7, (16, 16, 20)); R(ox + 39, 22, 13, 7, (16, 16, 20))
R(ox + 33, 23, 6, 3, (16, 16, 20)); P(ox + 35, 29, (224, 170, 0))
P(ox + 23, 24, (220, 230, 240)); P(ox + 42, 24, (220, 230, 240))
# suit with shading + belt + C shield
R(ox + 18, 46, 36, 26, (36, 86, 200)); R(ox + 46, 46, 8, 26, (26, 63, 150)); R(ox + 18, 46, 6, 26, (74, 120, 232))
R(ox + 18, 64, 36, 4, (224, 170, 0)); R(ox + 32, 63, 8, 6, (255, 217, 26))
d.polygon([(ox + 30, 49), (ox + 42, 49), (ox + 42, 56), (ox + 36, 61), (ox + 30, 56)], fill=(237, 230, 216))
d.arc([ox + 32, 51, ox + 40, 58], 40, 320, fill=(36, 86, 200), width=2)
# arms + fists (mark glint on his left = image right)
R(ox + 10, 48, 8, 18, (26, 63, 150)); R(ox + 54, 48, 8, 18, (36, 86, 200))
R(ox + 9, 66, 10, 8, G1); R(ox + 53, 66, 10, 8, G1); P(ox + 60, 68, (255, 255, 240)); P(ox + 61, 69, G3)
# legs + boots
R(ox + 22, 72, 11, 10, (26, 63, 150)); R(ox + 39, 72, 11, 10, (36, 86, 200))
R(ox + 20, 82, 14, 5, (40, 32, 26)); R(ox + 38, 82, 14, 5, (40, 32, 26))

# ============ HARVEST KING (offset 84) ============
ox = 84
SK1, SK2, SK3 = (240, 192, 140), (214, 158, 104), (168, 116, 72)   # skin tones
BD1, BD2 = (74, 62, 54), (52, 44, 40)                              # beard charcoal-brown
GR1, GR2, GR3 = (46, 110, 52), (34, 84, 40), (74, 150, 66)         # robe greens
AU1, AU2 = (255, 210, 30), (200, 152, 10)                          # golds
# robe: layered cloak, fold shading, gold trim
d.polygon([(ox + 14, 40), (ox + 58, 40), (ox + 64, 86), (ox + 8, 86)], fill=GR2)
d.polygon([(ox + 14, 40), (ox + 36, 40), (ox + 30, 86), (ox + 8, 86)], fill=GR1)
for fx in (24, 48):
    d.line([(ox + fx, 44), (ox + fx - 3, 84)], fill=GR3, width=1)
R(ox + 33, 40, 6, 46, AU2); R(ox + 34, 40, 2, 46, AU1)             # center gold trim
R(ox + 12, 82, 48, 4, AU2)
# corn scepter OUT at his right side (image left), ground-rest like the statue:
# stalks, three big cobs fanning at the top, leaves, red tie at the grip
d.line([(ox + 4, 86), (ox + 7, 34)], fill=(46, 140, 60), width=3)
d.line([(ox + 1, 86), (ox + 4, 36)], fill=(34, 110, 46), width=2)
for cxk, cyk in [(0, 22), (6, 17), (12, 22)]:
    for ky in range(6):
        for kx in range(3):
            R(ox + cxk + kx * 2, cyk + ky * 2, 2, 2, G1 if (kx + ky) % 2 == 0 else G2)
    P(ox + cxk + 2, cyk - 2, (250, 240, 200)); P(ox + cxk + 3, cyk - 3, (250, 240, 200))
d.line([(ox + 2, 46), (ox + 12, 40)], fill=(92, 196, 106), width=2)   # leaf
R(ox + 2, 50, 8, 3, (190, 40, 40))                                    # harvest-red tie
R(ox + 10, 52, 9, 7, SK2)                                             # his right hand on the shaft
# left hand + the great green gem cupped at his belly
R(ox + 42, 62, 10, 8, SK2)
d.polygon([(ox + 36, 58), (ox + 43, 64), (ox + 36, 72), (ox + 29, 64)], fill=(46, 190, 90))
d.polygon([(ox + 36, 58), (ox + 39, 64), (ox + 36, 72)], fill=(30, 150, 66)); P(ox + 33, 61, (190, 255, 210))
# head: warm face, brow band, eyes BELOW it with whites, nose, mustache wings, jaw beard
R(ox + 20, 14, 32, 26, SK1); R(ox + 44, 14, 8, 26, SK2)
R(ox + 20, 23, 32, 4, SK3)                                          # brow shadow band
for ex in (27, 40):
    R(ox + ex, 28, 6, 4, (245, 240, 230)); R(ox + ex + 2, 29, 3, 3, (30, 24, 20))
R(ox + 34, 31, 4, 6, SK2); P(ox + 37, 36, SK3)                      # nose + shade
d.polygon([(ox + 28, 36), (ox + 35, 36), (ox + 33, 39), (ox + 28, 38)], fill=BD1)   # mustache wings
d.polygon([(ox + 37, 36), (ox + 44, 36), (ox + 44, 38), (ox + 39, 39)], fill=BD1)
d.line([(ox + 33, 39), (ox + 39, 39)], fill=(120, 60, 50), width=1)  # grim mouth
R(ox + 20, 36, 4, 8, BD1); R(ox + 48, 36, 4, 8, BD1)                # jaw-frame beard
R(ox + 26, 42, 20, 3, BD1)
for bx in range(27, 45, 3): P(ox + bx, 43, BD2)
# crown: chunky gold, points, green jewel
R(ox + 18, 6, 36, 8, AU2); R(ox + 18, 6, 36, 3, AU1)
for px_ in (20, 30, 40, 48): d.polygon([(ox + px_, 6), (ox + px_ + 4, 0), (ox + px_ + 8, 6)], fill=AU1)
P(ox + 35, 9, (46, 190, 90)); P(ox + 36, 9, (46, 190, 90)); P(ox + 35, 10, (30, 150, 66))

# ============ STORM WIZARD (offset 164) ============
ox = 164
S1, S2, S3 = (84, 104, 138), (58, 72, 96), (38, 48, 66)             # slate tones
V1, V2 = (160, 106, 232), (122, 63, 212)                            # violets
# robe with fold shading + torn hem
d.polygon([(ox + 16, 34), (ox + 56, 34), (ox + 62, 86), (ox + 10, 86)], fill=S2)
d.polygon([(ox + 16, 34), (ox + 34, 34), (ox + 28, 86), (ox + 10, 86)], fill=S1)
for fx in (26, 46): d.line([(ox + fx, 40), (ox + fx - 2, 82)], fill=S3, width=2)
for tx_ in range(12, 60, 8): d.polygon([(ox + tx_, 86), (ox + tx_ + 4, 80), (ox + tx_ + 8, 86)], fill=(38, 48, 66))
R(ox + 33, 34, 6, 50, V2); R(ox + 34, 34, 2, 50, V1)                # violet center trim
d.polygon([(ox + 36, 44), (ox + 41, 49), (ox + 36, 55), (ox + 31, 49)], fill=V1)   # chest gem
P(ox + 34, 47, (240, 220, 255))
# sleeves + pale hands
R(ox + 8, 40, 9, 22, S3); R(ox + 55, 40, 9, 22, S2)
R(ox + 9, 62, 7, 6, (216, 206, 196)); R(ox + 56, 62, 7, 6, (216, 206, 196))
# staff: grained shaft, fork, violet spark
d.line([(ox + 62, 84), (ox + 60, 26)], fill=(110, 78, 48), width=3)
d.line([(ox + 61, 60), (ox + 60, 30)], fill=(84, 58, 36), width=1)
d.line([(ox + 60, 26), (ox + 55, 16)], fill=(110, 78, 48), width=2)
d.line([(ox + 60, 26), (ox + 65, 16)], fill=(110, 78, 48), width=2)
for sx, sy, c in [(60, 12, V1), (58, 9, V2), (62, 8, V1), (60, 5, (240, 220, 255)), (57, 13, V2), (63, 13, V2)]:
    P(ox + sx, sy, c); P(ox + sx, sy + 1, c)
# hood: spire with folds; face void; pale eyes with glints
d.polygon([(ox + 36, 0), (ox + 54, 30), (ox + 18, 30)], fill=S2)
d.polygon([(ox + 36, 0), (ox + 44, 30), (ox + 18, 30)], fill=S1)
d.line([(ox + 32, 8), (ox + 28, 28)], fill=S3); d.line([(ox + 42, 10), (ox + 46, 28)], fill=S3)
R(ox + 24, 26, 24, 14, (8, 8, 16))
for ex in (29, 39):
    R(ox + ex, 31, 4, 3, (207, 232, 255)); P(ox + ex + 1, 31, (255, 255, 255))
img = img.resize((img.width * 4, img.height * 4), Image.NEAREST)
img.save('detail-lineup.png')
print('detail lineup rendered', img.size)
