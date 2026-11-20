# One house, up close — hand-drawn at pixel level from Michael's Kakariko screenshots.
# Study notes: the Zelda door is a PROTRUDING arched frame (light stone), rounded arch,
# recessed dark opening, plank door with a crest cutout, stone step + paired welcome
# stones; roofs are slabs with rounded corners that OVERHANG the wall; detail lives in
# tufts, flower dots, pots, shutters, flower boxes — sparse and placed.
from PIL import Image, ImageDraw

W, H = 240, 176
img = Image.new('RGB', (W, H), (62, 142, 65))
d = ImageDraw.Draw(img)
K = (20, 18, 20)

# --- grass texture: tufts + sparse flower dots, clustered like the screenshots
import random
random.seed(7)
for _ in range(90):
    x, y = random.randrange(4, W - 4), random.randrange(4, H - 4)
    if 30 < x < 215 and 20 < y < 120: continue  # keep the house plot clean
    d.line([(x, y), (x - 1, y - 3)], fill=(110, 201, 91))
    d.line([(x + 2, y), (x + 2, y - 4)], fill=(110, 201, 91))
    d.line([(x + 4, y), (x + 5, y - 3)], fill=(90, 180, 80))
for cx, cy in [(18, 130), (205, 142), (40, 158), (222, 60)]:
    for dx, dy in [(0, 0), (3, 1), (1, 3), (5, 3)]:
        d.point((cx + dx, cy + dy), fill=(245, 239, 230))
        d.point((cx + dx + 1, cy + dy), fill=(255, 210, 30))

# --- irregular dirt patch in front of the door (a blob, not a rectangle)
d.ellipse([86, 118, 158, 146], fill=(201, 147, 91))
d.ellipse([96, 112, 148, 138], fill=(201, 147, 91))
for x, y in [(100, 128), (130, 120), (118, 136), (142, 130), (106, 118)]:
    d.point((x, y), fill=(158, 104, 56)); d.point((x + 1, y), fill=(158, 104, 56))

HX0, HX1 = 52, 188          # house span
WY = 78                     # wall top (under eave)
# --- soft shadow under the house
d.rectangle([HX0 - 3, 108, HX1 + 3, 114], fill=(50, 118, 54))

# --- WALL: cream plaster + timber corner posts + base shadow
d.rectangle([HX0, WY, HX1, 110], fill=(245, 239, 230))
d.rectangle([HX0, WY, HX1, WY + 2], fill=(140, 128, 110))        # eave shadow on wall
d.rectangle([HX0, 106, HX1, 110], fill=(214, 205, 190))          # base shading
for px in (HX0, HX1 - 5):
    d.rectangle([px, WY, px + 5, 110], fill=(92, 58, 33))
    d.rectangle([px + 2, WY, px + 2, 110], fill=(110, 66, 38))

# --- WINDOWS with shutters, mullions, flower boxes
def window(cx):
    d.rectangle([cx - 11, WY + 8, cx + 11, WY + 26], fill=K)
    d.rectangle([cx - 10, WY + 9, cx + 10, WY + 25], fill=(255, 210, 30))
    d.rectangle([cx - 10, WY + 9, cx - 1, WY + 16], fill=(255, 226, 110))
    d.line([(cx, WY + 9), (cx, WY + 25)], fill=K)
    d.line([(cx - 10, WY + 17), (cx + 10, WY + 17)], fill=K)
    for sx in (cx - 16, cx + 13):                                 # green shutters
        d.rectangle([sx, WY + 8, sx + 3, WY + 26], fill=(36, 105, 61))
        d.line([(sx, WY + 13), (sx + 3, WY + 13)], fill=(26, 78, 44))
        d.line([(sx, WY + 20), (sx + 3, WY + 20)], fill=(26, 78, 44))
    d.rectangle([cx - 11, WY + 27, cx + 11, WY + 30], fill=(92, 58, 33))  # flower box
    for fx in range(cx - 9, cx + 10, 4):
        d.point((fx, WY + 27), fill=(232, 93, 117)); d.point((fx + 1, WY + 28), fill=(76, 175, 80))
window(78); window(162)

# --- THE DOOR: protruding arched stone frame, recessed opening, plank door, crest
DC = 120                                    # door center x
d.rectangle([DC - 15, WY + 2, DC + 15, 110], fill=K)                       # frame outline
d.rectangle([DC - 14, WY + 3, DC + 14, 110], fill=(194, 185, 173))         # light stone frame
d.pieslice([DC - 14, WY - 6, DC + 14, WY + 14], 180, 360, fill=K)
d.pieslice([DC - 13, WY - 5, DC + 13, WY + 13], 180, 360, fill=(194, 185, 173))
d.rectangle([DC - 10, WY + 6, DC + 10, 110], fill=(30, 20, 14))             # recessed dark opening
d.pieslice([DC - 10, WY - 2, DC + 10, WY + 12], 180, 360, fill=(30, 20, 14))
d.rectangle([DC - 8, WY + 7, DC + 8, 110], fill=(110, 66, 38))              # plank door
for px in (DC - 4, DC, DC + 4):
    d.line([(px, WY + 9), (px, 110)], fill=(92, 58, 33))
d.line([(DC - 8, WY + 20), (DC + 8, WY + 20)], fill=(92, 58, 33))
heart = [(0,-2),(1,-3),(3,-3),(4,-2),(4,0),(3,2),(1,4),(0,5),(-1,4),(-3,2),(-4,0),(-4,-2),(-3,-3),(-1,-3)]
d.polygon([(DC + x, WY + 12 + y) for x, y in heart], fill=(255, 210, 30))   # golden crest cutout
d.point((DC + 6, WY + 26), fill=(255, 210, 30))                             # brass knob
# stone step + paired welcome stones (the screenshots' signature)
d.rectangle([DC - 12, 111, DC + 12, 113], fill=(140, 133, 123))
for sx in (DC - 9, DC - 3, DC + 3):
    d.ellipse([sx, 115, sx + 5, 118], fill=(178, 169, 158))

# --- clay pots by the wall
for px, s in [(40, 1), (192, 1)]:
    d.polygon([(px, 100), (px + 9, 100), (px + 7, 110), (px + 2, 110)], fill=(158, 104, 56))
    d.rectangle([px - 1, 97, px + 10, 100], fill=(201, 147, 91))

# --- ROOF: maroon slab, rounded corners, scalloped shingle rows, overhang + ridge
RY0, RY1 = 30, WY + 4
d.rectangle([HX0 - 6, RY0 + 6, HX1 + 6, RY1], fill=(122, 48, 64))
d.pieslice([HX0 - 6, RY0, HX0 + 8, RY0 + 12], 180, 270, fill=(122, 48, 64))
d.pieslice([HX1 - 8, RY0, HX1 + 6, RY0 + 12], 270, 360, fill=(122, 48, 64))
d.rectangle([HX0 - 6, RY0 + 3, HX1 + 6, RY0 + 6], fill=(146, 62, 78))       # ridge light
for ry in range(RY0 + 12, RY1 - 4, 8):                                       # scallop rows
    for sx in range(HX0 - 2, HX1 + 2, 10):
        d.arc([sx, ry, sx + 10, ry + 7], 0, 180, fill=(94, 36, 50))
d.rectangle([HX0 - 6, RY1 - 3, HX1 + 6, RY1], fill=(70, 26, 38))             # eave edge
# chimney with smoke
d.rectangle([150, 14, 162, 34], fill=(158, 104, 56))
d.rectangle([149, 12, 163, 15], fill=(92, 58, 33))
for sx, sy, s in [(154, 8, 2), (158, 4, 3), (163, 1, 2)]:
    d.ellipse([sx, sy, sx + s + 2, sy + s], fill=(245, 245, 245))

# --- hedge run (clover-dense) left, log-post fence right
for hx in range(6, 34, 4):
    d.ellipse([hx, 96, hx + 7, 104], fill=(46, 110, 52))
    d.point((hx + 2, 98), fill=(110, 201, 91)); d.point((hx + 4, 100), fill=(110, 201, 91))
for fx in range(198, 232, 8):
    d.rectangle([fx, 96, fx + 5, 110], fill=(158, 104, 56))
    d.pieslice([fx, 93, fx + 5, 99], 180, 360, fill=(201, 147, 91))
    d.rectangle([fx, 96, fx + 5, 97], fill=(92, 58, 33))
d.rectangle([198, 102, 234, 104], fill=(110, 66, 38))

# --- signpost by the path
d.rectangle([168, 118, 170, 132], fill=(92, 58, 33))
d.rectangle([160, 112, 178, 119], fill=(158, 104, 56))
d.rectangle([161, 113, 177, 118], outline=(92, 58, 33))
d.line([(164, 115), (174, 115)], fill=(60, 38, 20))

# --- one big swirled tree crown, top-left corner
for cx, cy, r in [(22, 18, 17), (38, 24, 13), (10, 26, 12)]:
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(46, 130, 60))
    d.arc([cx - r + 4, cy - r + 4, cx + r - 4, cy + r - 4], 200, 320, fill=(110, 201, 91), width=2)
    d.arc([cx - 6, cy - 4, cx + 7, cy + 8], 180, 330, fill=(36, 96, 46), width=2)
d.rectangle([19, 34, 25, 44], fill=(92, 58, 33))

img = img.resize((W * 3, H * 3), Image.NEAREST)
img.save('house-closeup-v2.png')
print('v2 rendered', img.size)
