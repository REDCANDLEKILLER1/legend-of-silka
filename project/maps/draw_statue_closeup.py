# The Weathered Harvest King — plaza statue close-up, house-v2 detail standard.
# Canon beats in the stone: dull gold crown, wheat sheaf in hand, moss + cracks
# (100 harvests), and the violet gem in his chest — the storm's color, the wrong note.
from PIL import Image, ImageDraw
import random
random.seed(11)
W, H = 200, 200
img = Image.new('RGB', (W, H), (178, 169, 158))
d = ImageDraw.Draw(img)
K = (24, 22, 26)
STONE = (168, 158, 144); STONE_D = (140, 132, 120); STONE_L = (196, 188, 174)
GOLD = (212, 175, 55); GOLD_D = (168, 134, 40)

# --- plaza cobbles: beveled stones with grout arcs
for y in range(0, H, 14):
    for x in range((y // 14 % 2) * 8, W, 16):
        d.rounded_rectangle([x + 1, y + 1, x + 15, y + 13], 3, fill=(186, 177, 164))
        d.arc([x + 2, y + 2, x + 14, y + 12], 180, 360, fill=STONE_L)
# flower ring at the statue's foot
import math
for a in range(0, 360, 9):
    fx, fy = 100 + int(72 * math.cos(math.radians(a))), 178 + int(10 * math.sin(math.radians(a)))
    d.point((fx, fy), fill=(232, 93, 117)); d.point((fx + 1, fy), fill=(245, 239, 230)); d.point((fx, fy + 1), fill=(76, 175, 80))

# --- plinth: two cracked, mossy tiers + inscription plaque
d.rectangle([52, 168, 148, 180], fill=STONE_D); d.rectangle([52, 168, 148, 170], fill=STONE_L)
d.rectangle([60, 154, 140, 168], fill=STONE); d.rectangle([60, 154, 140, 156], fill=STONE_L)
d.rectangle([86, 158, 114, 166], fill=(120, 112, 100))                    # plaque
for lx in range(90, 112, 5): d.line([(lx, 162), (lx + 3, 162)], fill=(70, 64, 56))
d.line([(64, 156), (72, 164), (70, 168)], fill=(90, 84, 76))              # crack
for mx, my in [(58, 170), (138, 172), (66, 160)]:
    d.ellipse([mx, my, mx + 8, my + 4], fill=(62, 130, 66))               # moss

# --- the King ---
# robe: broad trapezoid with fold lines and a hem of square cuts
d.polygon([(78, 154), (84, 84), (116, 84), (122, 154)], fill=STONE)
d.polygon([(78, 154), (84, 84), (92, 84), (90, 154)], fill=STONE_L)
for fx in (94, 100, 106):
    d.line([(fx, 96), (fx - 1, 150)], fill=STONE_D)
for hx in range(80, 120, 8):
    d.rectangle([hx, 148, hx + 4, 154], fill=STONE_D)
d.rectangle([84, 108, 116, 112], fill=STONE_D)                            # belt
d.rectangle([96, 107, 104, 113], fill=GOLD_D)                             # buckle
# chest gem — violet, faintly lit
d.polygon([(100, 92), (105, 97), (100, 103), (95, 97)], fill=(148, 90, 220))
d.point((100, 96), fill=(210, 180, 255))
# left arm (viewer right) holding the wheat sheaf high
d.polygon([(114, 88), (126, 78), (130, 84), (118, 98)], fill=STONE)
d.ellipse([124, 72, 132, 80], fill=STONE)                                  # fist
for gx, tx in [(120, 112), (124, 120), (128, 128), (132, 136), (136, 143)]:
    d.line([(128, 76), (tx, 46)], fill=(240, 200, 40), width=1)           # stalks fan from the fist
    d.ellipse([tx - 2, 34, tx + 2, 47], fill=GOLD)                         # grain head
    d.line([(tx, 47), (tx, 40)], fill=(255, 226, 110))
    d.line([(tx - 2, 38), (tx + 2, 42)], fill=GOLD_D)                      # awn ticks
d.rectangle([124, 72, 133, 77], fill=(146, 62, 78))                        # sheaf tie — harvest red
# right arm (viewer left) open, palm down in blessing
d.polygon([(86, 88), (72, 96), (70, 90), (84, 80)], fill=STONE)
d.ellipse([64, 92, 74, 98], fill=STONE)
# shoulders + head: beard, brow, closed eyes (a king at rest, not dead)
d.rectangle([88, 70, 112, 84], fill=STONE)
d.ellipse([89, 52, 111, 74], fill=STONE_L)
d.polygon([(92, 68), (108, 68), (104, 82), (96, 82)], fill=STONE)         # beard
for bx in range(94, 107, 3): d.line([(bx, 72), (bx, 80)], fill=STONE_D)
d.line([(93, 61), (98, 61)], fill=K); d.line([(102, 61), (107, 61)], fill=K)   # closed eyes
d.rectangle([92, 57, 108, 59], fill=STONE_D)                               # heavy brow
# the crown: five spikes, dull gold, one chipped, moss on the band
d.rectangle([89, 46, 111, 53], fill=GOLD)
d.rectangle([89, 51, 111, 53], fill=GOLD_D)
for sx, sh in [(90, 8), (95, 11), (100, 12), (105, 10), (109, 5)]:
    d.polygon([(sx, 47), (sx + 2, 47 - sh), (sx + 4, 47)], fill=GOLD)
d.point((100, 49), fill=(148, 90, 220))                                    # crown jewel — violet too
d.ellipse([90, 44, 97, 48], fill=(62, 130, 66))                            # moss on the crown
# weathering: cracks across robe + a chip off the shoulder
d.line([(108, 118), (104, 128), (107, 138)], fill=(90, 84, 76))
d.line([(90, 130), (94, 140)], fill=(90, 84, 76))
d.polygon([(116, 84), (122, 88), (117, 92)], fill=(178, 169, 158))
d.ellipse([80, 120, 88, 126], fill=(62, 130, 66))                          # moss on the robe

img = img.resize((W * 3, H * 3), Image.NEAREST)
img.save('statue-closeup.png')
print('statue rendered', img.size)
