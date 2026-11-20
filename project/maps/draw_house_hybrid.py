# ONE house, drawn as a house — hybrid palette, scene standard.
# (The tile mock was a grid wearing a roof strip. This is the correction.)
from PIL import Image, ImageDraw
import random
random.seed(5)
W, H = 360, 300
img = Image.new('RGB', (W, H), (62, 145, 68))          # ALttP sage grass
d = ImageDraw.Draw(img)
ov = Image.new('RGBA', (W, H), (0, 0, 0, 0)); od = ImageDraw.Draw(ov)
O = (43, 36, 30)                                        # soft brown outline
SH = (20, 30, 22, 66)
for _ in range(420):
    x, y = random.randrange(2, W - 2), random.randrange(2, H - 2)
    d.line([(x, y), (x, y - 3)], fill=random.choice([(107, 194, 89), (46, 110, 52)]))
for _ in range(14):
    x, y = random.randrange(0, W), random.randrange(190, H)
    d.ellipse([x, y, x + 26, y + 7], fill=(56, 132, 62))
# dirt path blob to the door
for pts in [((168, 300), (172, 262), (176, 226), (178, 196))]:
    for i in range(len(pts) - 1): d.line([pts[i], pts[i + 1]], fill=(176, 138, 92), width=15)
    for i in range(len(pts) - 1): d.line([pts[i], pts[i + 1]], fill=(196, 158, 104), width=9)
for _ in range(120):
    x, y = random.randrange(158, 200), random.randrange(196, 298)
    d.point((x, y), fill=(150, 112, 66))
# tree mass, left
d.rectangle([38, 128, 46, 168], fill=(92, 66, 43))
for ox, oy, r in [(-16, 8, 30), (16, 8, 30), (0, -12, 34), (-6, -24, 24)]:
    d.ellipse([70 + ox - r, 108 + oy - r, 70 + ox + r, 108 + oy + r], fill=(46, 110, 52))
    d.pieslice([70 + ox - r, 108 + oy - r, 70 + ox + r, 108 + oy + r], 180, 300, fill=(74, 150, 66))
    d.pieslice([70 + ox - r, 108 + oy - r, 70 + ox + r, 108 + oy + r], 200, 280, fill=(107, 194, 89))
od.ellipse([30, 160, 116, 176], fill=SH)
# log fence, right
for fx in (292, 316, 340):
    d.rectangle([fx, 150, fx + 7, 172], fill=(156, 120, 83))
    d.ellipse([fx - 1, 146, fx + 8, 154], fill=(176, 140, 100))
d.rectangle([290, 156, 350, 161], fill=(120, 88, 56))
# ===== THE HOUSE =====
od.polygon([(104, 196), (268, 196), (250, 214), (92, 210)], fill=SH)      # ground shadow
# walls: warm plaster, timber frame, shaded right edge
d.rectangle([112, 128, 256, 198], fill=(237, 230, 216))
d.rectangle([240, 128, 256, 198], fill=(214, 205, 190))
for tx in (112, 148, 220, 248):
    d.rectangle([tx, 128, tx + 6, 198], fill=(92, 66, 43))
d.rectangle([112, 128, 256, 133], fill=(92, 66, 43))
d.rectangle([112, 192, 256, 198], fill=(92, 66, 43))
# ROOF: pitched mass — ridge, two slopes, scalloped shingles, overhang
d.polygon([(184, 52), (268, 122), (100, 122)], fill=(156, 120, 83))       # shingle field
d.polygon([(184, 52), (268, 122), (184, 122)], fill=(138, 104, 70))       # right slope shade
for ry in range(66, 118, 9):                                              # scallop rows follow the slope
    inset = int((ry - 52) * 1.28)
    for sx in range(100 + inset, 268 - inset, 11):
        d.arc([sx, ry, sx + 11, ry + 7], 0, 180, fill=(92, 66, 43))
d.rectangle([96, 120, 272, 128], fill=(92, 66, 43))                        # eave beam
d.rectangle([96, 120, 272, 123], fill=(176, 140, 100))
od.rectangle([112, 128, 256, 134], fill=SH)                                # eave shadow on wall
d.rectangle([178, 44, 190, 54], fill=(237, 230, 216))                      # ridge cap
d.rectangle([222, 66, 238, 92], fill=(156, 120, 83))                       # chimney
d.rectangle([220, 62, 240, 68], fill=(92, 66, 43))
for sy in (44, 52):
    d.ellipse([226, sy - 8, 238, sy + 2], fill=(228, 228, 228))
# DOOR: stone arch, planks, diamond crest, twin mats
cx = 184
d.rectangle([cx - 15, 138, cx + 15, 196], fill=O)
d.rectangle([cx - 13, 140, cx + 13, 196], fill=(207, 198, 182))
d.pieslice([cx - 13, 132, cx + 13, 152], 180, 360, fill=(207, 198, 182))
d.rectangle([cx - 10, 146, cx + 10, 196], fill=(156, 110, 66))
d.rectangle([cx - 10, 146, cx - 5, 196], fill=(170, 124, 76))
for px in (cx - 3, cx + 2):
    d.line([(px, 148), (px, 194)], fill=(92, 66, 43))
d.polygon([(cx, 156), (cx + 5, 162), (cx, 169), (cx - 5, 162)], fill=(232, 193, 74))   # diamond crest
d.point((cx, 161), fill=(246, 220, 130))
d.point((cx + 7, 176), fill=(232, 193, 74))                               # brass knob
d.rectangle([cx - 13, 194, cx + 13, 198], fill=(143, 135, 123))           # threshold
for mx in (cx - 22, cx + 10):                                             # twin welcome mats
    d.ellipse([mx, 200, mx + 12, 206], fill=(207, 198, 182))
    d.ellipse([mx + 2, 201, mx + 10, 205], fill=(176, 168, 152))
# WINDOWS: shutters, warm panes, flower boxes
for wx in (130, 224):
    d.rectangle([wx - 11, 142, wx + 11, 166], fill=O)
    d.rectangle([wx - 16, 142, wx - 11, 166], fill=(156, 120, 83))
    d.rectangle([wx + 11, 142, wx + 16, 166], fill=(138, 104, 70))
    d.rectangle([wx - 9, 144, wx + 9, 164], fill=(255, 205, 92))
    d.rectangle([wx - 9, 144, wx, 164], fill=(255, 220, 130))
    d.line([(wx, 144), (wx, 164)], fill=O); d.line([(wx - 9, 154), (wx + 9, 154)], fill=O)
    d.rectangle([wx - 12, 166, wx + 12, 171], fill=(92, 66, 43))
    for fx in range(wx - 10, wx + 11, 5):
        d.point((fx, 167), fill=(232, 120, 150)); d.point((fx + 1, 168), fill=(237, 230, 216))
# clay pots + flowers by the wall
for px in (100, 252):
    d.polygon([(px, 184), (px + 10, 184), (px + 8, 196), (px + 2, 196)], fill=(176, 102, 60))
    d.point((px + 5, 182), fill=(232, 120, 150)); d.point((px + 3, 180), fill=(107, 194, 89))
img = Image.alpha_composite(img.convert('RGBA'), ov).convert('RGB')
img = img.resize((W * 2, H * 2), Image.NEAREST)
img.save('house-hybrid-scene.png')
print('house scene rendered', img.size)
