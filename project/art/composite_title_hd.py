#!/usr/bin/env python3
"""Composite the HD title screen: generated 16-bit valley art + a drawn
emblem (framed plaque, gold SILKA, the wrench, the adventure line).
PUSH START is NOT baked in — the game blinks it live."""
import glob
from PIL import Image, ImageDraw, ImageFont, ImageFilter

SRC = sorted(glob.glob('art/media-generation-title-bg-hd-*.webp'))[-1]
img = Image.open(SRC).convert('RGB')
W0, H0 = img.size
# center-crop to 4:3 (the game stage), nudged right to keep the eye tower whole
cw = int(H0 * 4 / 3)
x0 = min(max(0, (W0 - cw) // 2 + 30), W0 - cw)
img = img.crop((x0, 0, x0 + cw, H0))
W, H = img.size
S = W / 1440.0  # design scale (design space is 1440x1080)

def font(sz, bold=True):
    names = ['/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'] if bold else \
            ['/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf']
    return ImageFont.truetype(names[0], int(sz * S))

def text_size(dr, s, f, track=0):
    w = 0
    for ch in s:
        w += dr.textlength(ch, font=f) + track
    return w - track

def draw_tracked(base, xy, s, f, fill_mask_draw, track=0):
    x, y = xy
    dr = ImageDraw.Draw(base)
    for ch in s:
        fill_mask_draw(dr, (x, y), ch, f)
        x += dr.textlength(ch, font=f) + track
    return x

def gold_text(base, center_x, y, s, f, track=0):
    dr = ImageDraw.Draw(base)
    w = text_size(dr, s, f, track)
    x = center_x - w / 2
    # mask of the letterforms
    mask = Image.new('L', base.size, 0)
    md = ImageDraw.Draw(mask)
    cx = x
    for ch in s:
        md.text((cx, y), ch, font=f, fill=255)
        cx += md.textlength(ch, font=f) + track
    # drop shadow
    sh = mask.filter(ImageFilter.GaussianBlur(3 * S))
    base.paste((10, 4, 18), (int(3 * S), int(6 * S)), sh.point(lambda v: int(v * 0.65)))
    # ink outline: dilated mask in near-black
    dil = mask.filter(ImageFilter.MaxFilter(int(5 * S) | 1))
    base.paste((24, 16, 16), (0, 0), dil)
    # gold gradient through the letter mask
    grad = Image.new('RGB', (1, int(220 * S)))
    top, mid, bot = (255, 233, 138), (245, 189, 31), (169, 116, 8)
    for i in range(grad.height):
        t = i / max(1, grad.height - 1)
        c = tuple(int(top[k] + (mid[k] - top[k]) * (t / 0.55)) if t < 0.55 else
                  int(mid[k] + (bot[k] - mid[k]) * ((t - 0.55) / 0.45)) for k in range(3))
        grad.putpixel((0, i), c)
    grad = grad.resize(base.size)
    base.paste(grad, (0, 0), mask)
    return w

# ---------------- the plaque ----------------
PW, PH = int(880 * S), int(432 * S)
PX, PY = (W - PW) // 2, int(64 * S)
ov = Image.new('RGBA', img.size, (0, 0, 0, 0))
od = ImageDraw.Draw(ov)
# soft shadow
od.rounded_rectangle([PX + 10 * S, PY + 14 * S, PX + PW + 10 * S, PY + PH + 14 * S],
                     radius=int(26 * S), fill=(6, 2, 12, 160))
img = Image.alpha_composite(img.convert('RGBA'), ov)
d = ImageDraw.Draw(img)
# plaque body: vertical plum gradient
body = Image.new('RGB', (PW, PH))
for i in range(PH):
    t = i / PH
    c = tuple(int((26 + (16 - 26) * t)) for _ in range(1))  # placeholder, real below
    r = int(24 + (14 - 24) * t); g = int(14 + (8 - 14) * t); b = int(42 + (26 - 42) * t)
    ImageDraw.Draw(body).line([(0, i), (PW, i)], fill=(r, g, b))
mask = Image.new('L', (PW, PH), 0)
ImageDraw.Draw(mask).rounded_rectangle([0, 0, PW - 1, PH - 1], radius=int(24 * S), fill=255)
img.paste(body, (PX, PY), mask)
d = ImageDraw.Draw(img)
# frames: outer bevel gold, dark groove, inner gold line
d.rounded_rectangle([PX, PY, PX + PW, PY + PH], radius=int(24 * S), outline=(138, 106, 31), width=int(10 * S))
d.rounded_rectangle([PX + 9 * S, PY + 9 * S, PX + PW - 9 * S, PY + PH - 9 * S], radius=int(19 * S), outline=(255, 223, 107), width=int(3 * S))
d.rounded_rectangle([PX + 20 * S, PY + 20 * S, PX + PW - 20 * S, PY + PH - 20 * S], radius=int(14 * S), outline=(201, 162, 39), width=int(2 * S))
# leaf ticks along the inner band
import math
def leaf(cx, cy, ang, ln, col):
    pts = []
    for t in [i / 8 for i in range(9)]:
        wdt = math.sin(t * math.pi) * ln * 0.32
        px = cx + math.cos(ang) * ln * (t - 0.5); py = cy + math.sin(ang) * ln * (t - 0.5)
        pts.append((px - math.sin(ang) * wdt, py + math.cos(ang) * wdt))
    for t in [i / 8 for i in range(8, -1, -1)]:
        wdt = math.sin(t * math.pi) * ln * 0.32
        px = cx + math.cos(ang) * ln * (t - 0.5); py = cy + math.sin(ang) * ln * (t - 0.5)
        pts.append((px + math.sin(ang) * wdt, py - math.cos(ang) * wdt))
    d.polygon(pts, fill=col)
gx0, gy0, gx1, gy1 = PX + 34 * S, PY + 34 * S, PX + PW - 34 * S, PY + PH - 34 * S
step = 52 * S
n = 0
x = gx0 + step / 2
while x < gx1:
    leaf(x, gy0, 0.5, 15 * S, (94, 201, 86) if n % 2 else (40, 130, 62))
    leaf(x, gy1, -0.5 + math.pi, 15 * S, (40, 130, 62) if n % 2 else (94, 201, 86))
    x += step; n += 1
y = gy0 + step / 2; n = 0
while y < gy1:
    leaf(gx0, y, 1.1, 15 * S, (94, 201, 86) if n % 2 else (40, 130, 62))
    leaf(gx1, y, 1.1 + math.pi, 15 * S, (40, 130, 62) if n % 2 else (94, 201, 86))
    y += step; n += 1
# corner diamonds
for cx, cy in [(PX + 20 * S, PY + 20 * S), (PX + PW - 20 * S, PY + 20 * S),
               (PX + 20 * S, PY + PH - 20 * S), (PX + PW - 20 * S, PY + PH - 20 * S)]:
    r = 9 * S
    d.polygon([(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)], fill=(255, 223, 107), outline=(138, 106, 31))

CX = PX + PW // 2
# ---------------- the words ----------------
f_small = font(37)
dr = ImageDraw.Draw(img)
s = 'THE LEGEND OF'
w = text_size(dr, s, f_small, track=int(10 * S))
gold_text(img, CX, PY + 44 * S, s, f_small, track=int(10 * S))
f_big = font(118)
gold_text(img, CX, PY + 92 * S, 'SILKA', f_big, track=int(6 * S))

# ---------------- the wrench ----------------
import math as _m
wl = Image.new('RGBA', (int(520 * S), int(104 * S)), (0, 0, 0, 0))
u = S
J = (64 * u, 52 * u); B = (452 * u, 52 * u)
def shaft_poly(inset):
    return [(92*u, (38+inset)*u), (270*u, (34+inset)*u), (424*u, (36+inset)*u),
            (424*u, (68-inset)*u), (270*u, (70-inset)*u), (92*u, (66-inset)*u)]
wd = ImageDraw.Draw(wl)
# silhouette pass (ink)
wd.ellipse([J[0]-43*u, J[1]-43*u, J[0]+43*u, J[1]+43*u], fill=(35, 36, 42, 255))
wd.polygon(shaft_poly(-3), fill=(35, 36, 42, 255))
wd.ellipse([B[0]-45*u, B[1]-45*u, B[0]+45*u, B[1]+45*u], fill=(35, 36, 42, 255))
# steel body via gradient mask
strip = Image.new('RGB', (1, int(104*u)))
for i in range(strip.height):
    t = i / max(1, strip.height - 1)
    c = (219, 223, 231) if t < 0.35 else ((154, 160, 170) if t < 0.75 else (102, 106, 116))
    strip.putpixel((0, i), c)
strip = strip.resize(wl.size)
smask = Image.new('L', wl.size, 0)
sd = ImageDraw.Draw(smask)
sd.ellipse([J[0]-40*u, J[1]-40*u, J[0]+40*u, J[1]+40*u], fill=255)
sd.polygon(shaft_poly(0), fill=255)
sd.ellipse([B[0]-42*u, B[1]-42*u, B[0]+42*u, B[1]+42*u], fill=255)
wl.paste(strip, (0, 0), smask)
wd = ImageDraw.Draw(wl)
def hexpts(c, r, rot=0):
    return [(c[0] + r * _m.cos(_m.radians(rot + 60 * k)),
             c[1] + r * _m.sin(_m.radians(rot + 60 * k))) for k in range(6)]
# open-end mouth: a parallel-faced slot, tilted like a real wrench jaw
ang = _m.radians(192); ux, uy = _m.cos(ang), _m.sin(ang); px, py = -uy, ux
slot = [(J[0] + ux*8*u + px*13*u, J[1] + uy*8*u + py*13*u),
        (J[0] + ux*78*u + px*13*u, J[1] + uy*78*u + py*13*u),
        (J[0] + ux*78*u - px*13*u, J[1] + uy*78*u - py*13*u),
        (J[0] + ux*8*u - px*13*u, J[1] + uy*8*u - py*13*u)]
wd.polygon(slot, fill=(0, 0, 0, 0))
wd.polygon(hexpts(J, 20*u), fill=(0, 0, 0, 0))            # hex socket in the jaw
wd.polygon(hexpts(B, 21*u), fill=(0, 0, 0, 0))            # box end: 12-point hole
wd.polygon(hexpts(B, 21*u, 30), fill=(0, 0, 0, 0))
wd.polygon(hexpts(B, 21*u), outline=(70, 74, 84, 255), width=max(2, int(2*u)))
# highlights: jaw crown, shaft top edge, ring crown
wd.arc([J[0]-40*u, J[1]-40*u, J[0]+40*u, J[1]+40*u], start=195, end=320,
       fill=(240, 244, 250, 220), width=max(2, int(3*u)))
wd.line([100*u, 37*u, 420*u, 35*u], fill=(240, 244, 250, 200), width=max(2, int(3*u)))
wd.arc([B[0]-42*u, B[1]-42*u, B[0]+42*u, B[1]+42*u], start=190, end=330,
       fill=(240, 244, 250, 220), width=max(2, int(3*u)))
# soft shadow, then the wrench itself
sh = Image.new('RGBA', wl.size, (0, 0, 0, 0))
sh.paste((0, 0, 0, 110), (0, 0), wl.split()[3])
img.alpha_composite(sh, (int(CX - 260 * S), int(PY + 236 * S)))
img.alpha_composite(wl, (int(CX - 260 * S), int(PY + 230 * S)))

# adventure line inside the plaque
f_sub = font(33)
s = 'THE ADVENTURE OF CORNMAN'
dr = ImageDraw.Draw(img)
w = text_size(dr, s, f_sub, track=int(5 * S))
x = CX - w / 2
for ch in s:
    dr.text((x + 2 * S, PY + 350 * S + 2 * S), ch, font=f_sub, fill=(16, 10, 10))
    x += dr.textlength(ch, font=f_sub) + int(5 * S)
x = CX - w / 2
for ch in s:
    dr.text((x, PY + 350 * S), ch, font=f_sub, fill=(232, 228, 216))
    x += dr.textlength(ch, font=f_sub) + int(5 * S)

img.convert('RGB').save('art/title-screen-hd.jpg', quality=90)
print('title-screen-hd.jpg written:', img.size)
