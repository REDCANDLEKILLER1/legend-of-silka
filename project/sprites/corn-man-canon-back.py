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

# ============ BACK v1 — cape spread, back of the cob ============
img, d = canvas(); R = mk(d)
# cape spread across the back (the back view's main event, like the game)
R(3,14,26,22,RD)
R(3,33,26,3,R2)
R(5,20,22,1,R2); R(5,27,22,1,R2)           # cape fold lines
# arms at his sides, fists below the sleeves
R(1,20,4,9,B); R(27,20,4,9,B)
R(1,29,4,3,SK); R(2,30,2,1,Y)              # marked fist — HIS left, so image-left from behind
R(27,29,4,3,SK)
# back of the cob head — full kernels, no face, no shades
R(10,3,12,1,Y); R(9,4,14,16,Y)
for yy in (7,11,15,19): R(9,yy,14,1,D)
for xx in (13,18): R(xx,4,1,16,D)
R(14,0,4,4,G2); R(15,0,2,4,G)              # sprout
# husks wrap the back of the head
R(6,8,3,12,G); R(5,10,2,7,G); R(23,8,3,12,G); R(25,10,2,7,G)
R(7,19,3,3,G); R(22,19,3,3,G)              # husk points at the nape
# boots stepping below the cape hem
R(10,36,5,1,B); R(17,36,5,1,B)
R(9,37,6,3,RD); R(17,37,6,3,RD)
img.save('corn-man-CANON-back.png')
print('saved front v4 + back v1')
