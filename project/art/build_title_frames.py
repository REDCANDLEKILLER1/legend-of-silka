#!/usr/bin/env python3
"""Build the animated title frames from Michael's uploaded title art:
flowing waterfall streaks + foam, river sparkles, and a wind band
moving through the corn. Emerald glows and star twinkles are live
CSS overlays in the game; these frames carry the water and the corn.
Output: art/title-frames/f0..f3.jpg (1024x768) + a preview GIF."""
import os, random
from PIL import Image, ImageDraw, ImageFilter

random.seed(20261120)
base = Image.open('art/title-screen-final.png').convert('RGB').resize((1024, 768))
W, H = base.size
os.makedirs('art/title-frames', exist_ok=True)

def build_mask(region, cond):
    m = Image.new('L', (W, H), 0)
    mp = m.load(); bp = base.load()
    x0, y0, x1, y1 = region
    for y in range(y0, y1):
        for x in range(x0, x1):
            if cond(bp[x, y]):
                mp[x, y] = 255
    return m

water = build_mask((int(W*.28), int(H*.40), int(W*.64), int(H*.80)),
                   lambda c: c[2] > 140 and c[2] >= c[0] + 35 and c[1] > 110)
water = water.filter(ImageFilter.MaxFilter(3)).filter(ImageFilter.MinFilter(3))
water_soft = water.filter(ImageFilter.GaussianBlur(1.2))
river = build_mask((int(W*.26), int(H*.74), int(W*.74), int(H*.91)),
                   lambda c: c[2] > 105 and c[2] >= c[0] + 18 and c[1] > 85)
corn = build_mask((0, int(H*.78), W, H),
                  lambda c: c[0] > 140 and c[1] > 90 and c[2] < 115 and c[0] > c[2] + 60)
corn_soft = corn.filter(ImageFilter.GaussianBlur(5))

def masked_points(mask, n, region):
    mp = mask.load(); pts = []
    x0, y0, x1, y1 = region
    tries = 0
    while len(pts) < n and tries < n * 60:
        tries += 1
        x = random.randint(x0, x1 - 1); y = random.randint(y0, y1 - 1)
        if mp[x, y] > 0: pts.append((x, y))
    return pts

foam_pts = masked_points(water, 240, (int(W*.30), int(H*.42), int(W*.62), int(H*.79)))
spark_pts = masked_points(river, 130, (int(W*.28), int(H*.75), int(W*.72), int(H*.90)))
# waterfall streak columns: (x, phase hash, length)
cols = []
x = int(W * .315)
while x < int(W * .615):
    cols.append((x + random.randint(-2, 2), random.random(), random.randint(30, 72)))
    x += random.randint(5, 9)

frames = []
for p in range(4):
    fr = base.convert('RGBA')
    # --- corn wind band (under the water light) ---
    band = Image.new('L', (W, H), 0)
    bd = ImageDraw.Draw(band)
    bx = -120 + p * (W + 240) / 4.0
    for yy in range(int(H * .78), H, 3):
        cx = bx - (yy - H * .78) * 0.55
        for dx in range(-110, 111, 6):
            a = int(30 * max(0.0, 1 - abs(dx) / 110.0))
            if a: bd.rectangle([cx + dx, yy, cx + dx + 6, yy + 3], fill=a)
    band = band.filter(ImageFilter.GaussianBlur(14))
    ov = Image.new('RGBA', (W, H), (255, 246, 200, 0))
    ov.putalpha(Image.composite(band, Image.new('L', (W, H), 0), corn_soft))
    fr = Image.alpha_composite(fr, ov)
    # --- waterfall streaks ---
    st = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(st)
    reg_y0, reg_h = int(H * .415), int(H * .365)
    for cx, hsh, ln in cols:
        yy = reg_y0 + int((hsh * 997 + p * 0.27) % 1.0 * reg_h)
        sd.line([cx, yy, cx, yy + ln], fill=(235, 250, 255, 120), width=2)
        sd.line([cx + 2, yy + 9, cx + 2, yy + int(ln * .6)], fill=(255, 255, 255, 70), width=1)
    st.putalpha(Image.composite(st.split()[3], Image.new('L', (W, H), 0), water_soft))
    st = st.filter(ImageFilter.GaussianBlur(1))
    fr = Image.alpha_composite(fr, st)
    # --- foam + river sparkles ---
    sp = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    spd = ImageDraw.Draw(sp)
    import math
    for i, (fx, fy) in enumerate(foam_pts):
        a = int(90 + 90 * (0.5 + 0.5 * math.sin(p * math.pi / 2 + i * 1.7)))
        r = 1 + (i % 3)
        spd.ellipse([fx - r, fy - r, fx + r, fy + r], fill=(255, 255, 255, a))
    for i, (fx, fy) in enumerate(spark_pts):
        if (i + p) % 2 == 0:
            spd.ellipse([fx - 1, fy - 1, fx + 2, fy + 2], fill=(255, 255, 255, 200))
            spd.line([fx - 4, fy, fx + 5, fy], fill=(220, 240, 255, 90), width=1)
    fr = Image.alpha_composite(fr, sp)
    out = fr.convert('RGB')
    out.save(f'art/title-frames/f{p}.jpg', quality=84)
    frames.append(out)
    print('frame', p, 'saved')

frames[0].save('art/title-screen-final.jpg', quality=88)
gif = [f.resize((512, 384)) for f in frames]
gif[0].save('art/title-animated-preview.gif', save_all=True, append_images=gif[1:],
            duration=190, loop=0)
sheet = Image.new('RGB', (1024, 768))
for i, f in enumerate(frames):
    sheet.paste(f.resize((512, 384)), ((i % 2) * 512, (i // 2) * 384))
sheet.save('/tmp/title-frames-sheet.jpg', quality=85)
print('poster + gif + sheet done')
