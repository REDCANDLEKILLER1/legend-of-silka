# Michael's method (2026-11-19 01:05 CST): the statue is MY King — same drawing,
# colors changed to stone. Fixes in the living pass: staff IN his hand (fingers
# wrapped on the shaft), three separated cobs, ink definition throughout.
from PIL import Image, ImageDraw
W, H = 64, 88
img = Image.new('RGB', (W, H), (38, 48, 66))
d = ImageDraw.Draw(img)
K = (20, 18, 24)
def R(x, y, w, h, c): d.rectangle([x, y, x + w - 1, y + h - 1], fill=c)
def P(x, y, c): d.point((x, y), fill=c)
def OUT(x, y, w, h): d.rectangle([x, y, x + w - 1, y + h - 1], outline=K)
SK1, SK2, SK3 = (240, 192, 140), (214, 158, 104), (168, 116, 72)
BD1, BD2 = (74, 62, 54), (52, 44, 40)
GR1, GR2, GR3 = (46, 110, 52), (34, 84, 40), (74, 150, 66)
AU1, AU2 = (255, 210, 30), (200, 152, 10)
G1, G2 = (255, 217, 26), (224, 170, 0)
# ---- robe first (staff and hands layer over it) ----
d.polygon([(18, 42), (46, 42), (54, 84), (10, 84)], fill=GR2)
d.polygon([(18, 42), (32, 42), (26, 84), (10, 84)], fill=GR1)
d.polygon([(18, 42), (46, 42), (54, 84), (10, 84)], outline=K)
for fx in (22, 42): d.line([(fx, 46), (fx - 2, 80)], fill=(26, 64, 30), width=1)
P(23, 50, GR3); P(41, 56, GR3); P(24, 66, GR3)
R(29, 42, 6, 42, AU2); R(30, 42, 2, 42, AU1)                    # center trim
R(12, 80, 40, 4, AU2); R(12, 80, 40, 1, AU1)                    # hem band
# ---- staff: shaft, then cobs, then the gripping hand OVER it ----
d.line([(8, 86), (10, 30)], fill=(46, 140, 60), width=3)
d.line([(5, 86), (7, 32)], fill=(34, 110, 46), width=2)
for (cxk, cyk, lean) in [(1, 12, -1), (7, 8, 0), (13, 12, 1)]:  # three SEPARATED cobs
    for ky in range(6):
        for kx in range(3):
            R(cxk + kx * 2 + (lean if ky < 2 else 0), cyk + ky * 2, 2, 2, G1 if (kx + ky) % 2 == 0 else G2)
    OUT(cxk + (lean if True else 0), cyk, 6, 12)
    P(cxk + 2, cyk - 2, (250, 240, 200)); P(cxk + 3, cyk - 3, (250, 240, 200))   # silk
    d.line([(cxk + 1, cyk + 12), (cxk - 2, cyk + 17)], fill=(92, 196, 106), width=1)  # husk leaf
    d.line([(cxk + 5, cyk + 12), (cxk + 8, cyk + 17)], fill=(46, 158, 68), width=1)
R(5, 33, 9, 3, (190, 40, 40))                                   # harvest-red tie
# the grip: hand wrapped ON the shaft — palm block + three finger segments + thumb
R(4, 44, 12, 9, SK2); OUT(4, 44, 12, 9)
for fy in (47, 50): d.line([(5, fy), (15, fy)], fill=SK3)        # finger separations
R(13, 45, 4, 6, SK1)                                            # thumb on the far side
# ---- left hand cupping the gem ----
R(40, 62, 10, 8, SK2); OUT(40, 62, 10, 8)
d.line([(41, 66), (49, 66)], fill=SK3)
# ---- the emerald at his belly, faceted + outlined ----
d.polygon([(32, 58), (39, 65), (32, 74), (25, 65)], fill=(46, 190, 90))
d.polygon([(32, 58), (36, 65), (32, 74)], fill=(30, 150, 66))
d.polygon([(32, 58), (39, 65), (32, 74), (25, 65)], outline=K)
P(29, 62, (190, 255, 210))
# ---- head ----
R(20, 13, 24, 27, SK1); R(38, 13, 6, 27, SK2); OUT(20, 13, 24, 27)
R(20, 19, 24, 4, SK3)                                           # brow band (forehead shortened 3px)
for ex in (24, 35):
    R(ex, 24, 6, 4, (245, 240, 230)); R(ex + 2, 25, 3, 3, K)    # eyes with whites
    d.line([(ex, 23), (ex + 5, 23)], fill=BD2)                  # brow line
R(30, 27, 4, 6, SK2); P(33, 32, SK3)                            # nose
d.polygon([(25, 32), (31, 32), (29, 35), (25, 34)], fill=BD1)   # mustache wings
d.polygon([(33, 32), (39, 32), (39, 34), (35, 35)], fill=BD1)
d.line([(30, 35), (34, 35)], fill=(120, 60, 50))                # grim mouth
R(20, 31, 4, 9, BD1); R(40, 31, 4, 9, BD1)                      # jaw beard
R(24, 38, 16, 3, BD1)
for bx in range(25, 39, 3): P(bx, 39, BD2)                      # beard strands
# ---- crown: 4 points, inked, emerald inset ----
R(18, 5, 28, 8, AU2); R(18, 5, 28, 3, AU1); OUT(18, 5, 28, 8)
for px_ in (19, 26, 33, 40):
    d.polygon([(px_, 5), (px_ + 3, 0), (px_ + 6, 5)], fill=AU1)
    d.polygon([(px_, 5), (px_ + 3, 0), (px_ + 6, 5)], outline=K)
P(31, 8, (46, 190, 90)); P(32, 8, (46, 190, 90)); P(31, 9, (30, 150, 66))

# ================= DETAIL PASS (Michael, 2026-11-19 01:08 CST) =================
# Studied from his ALttP screenshots: ears out, hair framing the face, silver
# in the beard, jeweled crown band, patterned trim, textured cloth.
HAIR, HAIR_L = (92, 58, 36), (128, 88, 54)
SILVER = (196, 192, 182)
RUBY = (200, 48, 64)
# ears, sticking out both sides with inner shade
R(17, 25, 4, 6, SK1); R(43, 25, 4, 6, SK2); P(19, 27, SK3); P(44, 27, SK3)
# hair framing: temple wedges + strand highlights
R(20, 13, 5, 10, HAIR); R(39, 13, 5, 10, HAIR)
for hx in (21, 41): P(hx, 15, HAIR_L); P(hx + 1, 18, HAIR_L); P(hx, 21, HAIR_L)
# cheek shading + chin light under the beard line
P(23, 31, SK2); P(24, 32, SK2); P(40, 31, SK3); P(30, 34, SK1)
# silver wisdom strands in the beard
for (sx, sy) in [(22, 36), (26, 40), (31, 42), (36, 40), (41, 36), (28, 43), (34, 43)]:
    P(sx, sy, SILVER)
# crown band jewels: ruby dots in gold settings + emerald glint
for jx in (23, 37): P(jx, 9, RUBY); P(jx, 8, AU1)
P(30, 7, (190, 255, 210))
# collar chain: gold arc from shoulder to the trim
for (chx, chy) in [(22, 43), (25, 45), (28, 46), (36, 46), (39, 45), (42, 43)]:
    P(chx, chy, AU1)
# robe weave texture + patterned trim (amber diamonds down the gold)
for (wx, wy) in [(16, 52), (20, 62), (15, 72), (46, 54), (48, 66), (44, 76), (24, 78), (38, 72)]:
    P(wx, wy, GR2)
for ty in range(46, 78, 6): P(31, ty, (158, 100, 16))
for hx2 in range(15, 50, 6): P(hx2, 82, (158, 100, 16))
# gem gets a gold setting frame
d.polygon([(32, 56), (41, 65), (32, 76), (23, 65)], outline=AU2)
# boot tips peeking under the hem
R(20, 84, 8, 3, (40, 32, 26)); R(36, 84, 8, 3, (40, 32, 26))
# cobs: pale highlight column so kernels read in three tones
for (cxk, cyk, lean) in [(1, 12, -1), (7, 8, 0), (13, 12, 1)]:
    for ky in range(6): P(cxk + (lean if ky < 2 else 0), cyk + ky * 2, (255, 240, 170))

# ================= CRAFT PASS (Michael, 2026-11-19 01:09 CST) =================
# His three lessons off the ALttP sheets: (1) never a solid color — work light
# tones into a surface and it reads as wrinkles; (2) hands are shaped, not
# blocks; (3) round everything pixel-wise — take the corners off.
BG = (38, 48, 66)
DEEP = (26, 64, 30)
# --- (3) corners off: robe hem + shoulders, jaw, crown band ---
for (cx, cy) in [(10, 84), (11, 84), (10, 83), (53, 84), (54, 84), (54, 83),
                 (18, 42), (46, 42), (20, 40), (43, 40), (18, 5), (45, 5),
                 (12, 80), (51, 80)]:
    P(cx, cy, BG)
# --- (1) wrinkles: light-green strokes worked into the robe, following folds ---
for (wx, wy, ln, cc) in [(20, 50, 3, GR3), (42, 50, 3, GR3), (18, 58, 4, GR3),
                         (44, 60, 3, GR3), (22, 70, 3, GR3), (40, 72, 4, GR3),
                         (26, 56, 2, DEEP), (38, 58, 2, DEEP), (24, 64, 3, DEEP),
                         (42, 46, 2, GR3), (16, 66, 2, GR3), (47, 74, 2, GR3)]:
    for i in range(ln): P(wx + i, wy + (i // 3), cc)
# face wrinkles: crow's feet + cheek folds
P(22, 28, SK3); P(21, 29, SK3); P(41, 28, SK3); P(42, 29, SK3)
d.line([(28, 32), (27, 34)], fill=SK2); d.line([(36, 32), (37, 34)], fill=SK3)
# --- (2) real hands ---
NAIL = (250, 240, 225)
# gripping hand rebuilt: four curled fingers around the shaft + thumb across
R(4, 44, 13, 10, BG)                                            # clear the block
for fi in range(4):                                             # finger segments
    fy = 44 + fi * 2
    R(5, fy, 9, 2, SK1 if fi % 2 == 0 else SK2)
    P(5, fy, BG); P(13, fy + 1, SK3)                            # rounded tips + groove shade
    P(12, fy, NAIL)                                             # nail light
R(13, 46, 4, 5, SK1); P(16, 48, SK3)                            # thumb wedge
d.line([(8, 44), (8, 52)], fill=(46, 140, 60))                  # shaft shows between fingers
# cupping hand rebuilt: palm scoop with fingertip bumps under the gem
R(40, 62, 11, 9, SK2); P(40, 62, GR2); P(50, 62, GR2); P(40, 70, GR1); P(50, 70, GR2)
for fi in range(4): P(42 + fi * 2, 70, SK1)                     # fingertips
d.line([(41, 66), (49, 66)], fill=SK3)                          # palm crease
R(38, 64, 3, 5, SK1)                                            # thumb at the side
img.save('king-living-v3.png')
# ================= STATUE: same drawing, colors changed =================
STONE = {
    SK1: (184, 180, 166), SK2: (150, 146, 134), SK3: (110, 107, 98),
    BD1: (96, 93, 85), BD2: (64, 62, 57),
    GR1: (104, 122, 94), GR2: (76, 92, 68), GR3: (134, 152, 118), (26, 64, 30): (52, 64, 46),
    AU1: (217, 173, 38), AU2: (158, 116, 24),
    G1: (217, 173, 38), G2: (168, 128, 28),
    (46, 140, 60): (88, 110, 76), (34, 110, 46): (64, 84, 58),
    (92, 196, 106): (120, 144, 100), (46, 158, 68): (96, 120, 82),
    (190, 40, 40): (143, 50, 56),
    (46, 190, 90): (62, 140, 70), (30, 150, 66): (44, 104, 54), (190, 255, 210): (150, 190, 150),
    (245, 240, 230): (234, 230, 216), (250, 240, 200): (214, 206, 188),
    (120, 60, 50): (90, 86, 78),
    (92, 58, 36): (100, 97, 90), (128, 88, 54): (128, 124, 114), (196, 192, 182): (206, 202, 192),
    RUBY: (143, 50, 56), (158, 100, 16): (122, 88, 20), (40, 32, 26): (64, 62, 57),
    (255, 240, 170): (226, 196, 110), (250, 240, 225): (234, 230, 216), (38, 48, 66): (38, 48, 66), K: K,
}
st = img.copy(); sp = st.load()
for yy in range(H):
    for xx in range(W):
        c = sp[xx, yy]
        if c in STONE: sp[xx, yy] = STONE[c]
sd = ImageDraw.Draw(st)
M1, M2 = (106, 184, 72), (62, 122, 52)                            # moss
for (mx, my) in [(19, 43), (17, 46), (44, 82), (12, 83), (20, 12), (9, 20), (30, 82)]:
    sp[mx, my] = M1; sp[mx + 1, my] = M2; sp[mx, my + 1] = M2     # moss creep
sd.line([(24, 30), (23, 33)], fill=(64, 62, 57))                  # cheek crack
sd.line([(38, 60), (37, 66)], fill=(52, 64, 46))                  # robe crack
sp[21, 1] = (184, 180, 166); sp[22, 2] = (184, 180, 166)          # chipped crown point
st.save('king-statue-v5.png')
pair = Image.new('RGB', (W * 2 + 6, H), (24, 30, 40))
pair.paste(img, (0, 0)); pair.paste(st, (W + 6, 0))
pair = pair.resize((pair.width * 5, pair.height * 5), Image.NEAREST)
pair.save('king-and-statue-v4.png')
print('living + statue rendered')
