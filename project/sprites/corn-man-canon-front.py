from PIL import Image, ImageDraw
S = 16; W, H = 32, 40
K=(18,19,26); Y=(255,217,26); D=(224,170,0); G=(63,143,34); G2=(88,176,44)
SK=(244,184,134); B=(36,86,201); RD=(217,43,31); R2=(176,30,20); W_=(235,245,255)
SEAM=(14,68,153)

def canvas():
    img = Image.new('RGB', (W*S, H*S), (0,0,0))
    return img, ImageDraw.Draw(img)
def mk(d):
    def R(x, y, w, h, c): d.rectangle([x*S, y*S, (x+w)*S-1, (y+h)*S-1], fill=c)
    return R

# ============ FRONT v4 — cape slimmed ============
img, d = canvas(); R = mk(d)
# cape: tucked behind the body, just a flare at the sides + hem below the arms
R(5,16,22,20,RD); R(5,34,22,2,R2)
R(3,20,2,10,RD); R(27,20,2,10,RD)          # slim side flares (was 3px billows at x0/x29)
# arms + fists
R(4,22,5,10,B); R(23,22,5,10,B)
R(4,32,5,3,SK)
R(23,32,5,3,SK); R(24,33,3,1,Y)
# body
R(8,21,16,10,B)
R(8,22,1,9,SEAM); R(23,22,1,9,SEAM)
R(13,22,6,1,RD); R(12,23,8,4,RD); R(13,27,6,1,RD)
R(14,23,4,4,Y); R(15,24,3,2,RD)
R(9,30,14,2,Y); R(9,32,14,3,RD)
# legs + boots
R(10,35,5,3,B); R(17,35,5,3,B)
R(9,38,6,2,RD); R(17,38,6,2,RD)
# cob cap, tapered
R(10,3,12,1,Y); R(9,4,14,9,Y)
for yy in (6,9): R(9,yy,14,1,D)
for xx in (13,18): R(xx,4,1,9,D)
R(14,0,4,4,G2); R(15,0,2,4,G)
# husks
R(6,8,3,14,G); R(5,10,2,8,G); R(23,8,3,14,G); R(25,10,2,8,G)
# face
R(11,12,10,9,SK); R(11,12,10,1,D)
R(10,13,5,3,K); R(17,13,5,3,K)          # two lenses
R(15,13,2,1,K)                          # the bridge between them
R(11,14,2,1,W_)                         # glint on the left lens
R(14,18,4,1,K); R(13,17,1,1,K); R(18,17,1,1,K)
R(15,16,1,1,(214,144,90))   # the nose — one pixel, skin-shadow, under the shades
img.save('remy-corn-man-v6-front.png')

