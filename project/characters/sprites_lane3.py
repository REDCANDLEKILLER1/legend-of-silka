#!/usr/bin/env python3
"""Lane 3 directional sprites for THE LEGEND OF SILKA — 16x24 string matrices.

CornMan (down/up/right) + Harvest King (down/up/right), plus CornMan's
punch frame sets. Built to the character-craft spec: head mass up, eyes
LOW (rows 5-6), arms in separate seamed columns, hands rows 16-17,
curved hems, boots as separated clusters, 3 tones per material,
highlight clustered upper-left, shadow lower-right, selective ink
outline (ink on shadow side + seams, material-dark on lit edges).

CornMan canon is LOCKED (corn-man-CANON-front/back.png): kernel head,
green husks, shades band with bridge + nose px under it, blue suit,
red cape, C shield, gold MARK glint on his fist (screen-right in front
view, screen-left in back view — same hand). Punches come off the
SHOULDER, alternating arms, never from body centre (Michael's rule).

Punch frames are built from the matching idle view with only the
arm/shoulder/head rows edited, exactly as the spec prescribes.
"""

PAL_CHARS = set('KWsSHbBaYy gGLRCr eEuUdD.'.replace(' ', ''))
KING_CHARS = set('KWsSHbBaYy gGLR.'.replace(' ', ''))

SPRITES = {
    'cornman': {
        # FRONT — kernel head rows 0-10 (13-14 wide rows 3-7), shades
        # band row 6 with W glint at its left end, nose px under the
        # bridge row 7, husks framing to pointed tips row 10, cape
        # flare screen-right only, marked fist (yy) screen-right.
        'down': [
            ".....YgGGY......",
            "..LLYYYYYYYYLL..",
            ".GLLYYaYYaYYLLG.",
            ".GLYYYaYYaYYYLG.",
            ".GLYaYYaYYaYYLG.",
            ".GLYYaYYYYaYYLG.",
            ".GLWKKKKKKKKKLG.",
            ".GLGHHHssHHHGLG.",
            ".GLHHHHKKHHHHLG.",
            ".UUUUUUUUUUUUU..",
            "..GUUUUUUUUUuGRr",
            ".UUKUYYYYYUUKURr",
            ".UUKUYRRUYUUKURr",
            ".UUKUYRUUYUUKURr",
            ".UUKUYRRRYUUKURr",
            ".UUKUUUUUUUuKURr",
            ".HHUUUUUUUUUHyyR",
            ".HHUUUUUUUUUHyyr",
            "....UUu..uUU...r",
            "....UUu..uUU....",
            "....UUU..UUU....",
            "....KKK..KKK....",
            "....KKK..KKK....",
            "...KKKK..KKKK...",
        ],
        # BACK — cape FULL spread, kernel back with a-seams, husks from
        # behind, blue sleeves outside the cape, MARK glint at the
        # screen-left fist (his left hand, canon back view).
        'up': [
            ".....YgGGY......",
            "..LLYYaYYaYYLL..",
            ".GLLYYaYYaYYLLG.",
            ".GLYYaYYaYYaYLG.",
            ".GLYaYYaYYaYYLG.",
            ".GLYYaYYaYYaYLG.",
            ".GLYaYYaYYaYYLG.",
            ".GLGYYaYYaYYGLG.",
            ".GLGYaYYaYYaGLG.",
            ".GGRRRRRRRRRRGG.",
            "UUURRRRRRRRRRUUU",
            "UUURRRRRRRrrrUUU",
            "UUURRRRRRRrrrUUU",
            "UUURRRRRRRrrrUUU",
            "UUURRRRRRRrrrUUU",
            "UUURRrrrrrrrRUUU",
            "yHHRRRRRRRRRrHHH",
            "yHHRRRRRRRRRrHHH",
            "..RRRRRRRRRRRr..",
            "..RRRRRRRrrrrr..",
            "...RRUUU..UUURR.",
            "....KKK..KKK....",
            "....KKK..KKK....",
            "...KKKK..KKKK...",
        ],
        # RIGHT PROFILE — husks sweep back (left), shades side-on with
        # glint, nose bump at the right silhouette edge row 7, cape
        # trails behind rows 9-19, shield edge-on (gold column col 11),
        # marked fist forward rows 16-17, boots point right.
        'right': [
            ".....gGGYY......",
            "....LLYYYYYY....",
            "...GLLYYaYYaY...",
            "...GLYYYaYYaYY..",
            "...GLYYaYYaYYY..",
            "...GLYYaYYaYYY..",
            "...GLKKWKKKKK...",
            "...GLHHHsHHHHs..",
            "...GLHHHHKKHH...",
            "..GGgUUUUUUUU...",
            ".RRrGUUUUUUUU...",
            ".RRrGUUUUUUYU...",
            ".RRrGUUUUUUYUU..",
            ".RRrGUUUUUUYU...",
            ".RRrGUUUUUUYU...",
            ".RRrGUUUUUUUUU..",
            ".RRrrUUUUUUUHyy.",
            ".RRrrUUUUUUUyyH.",
            ".RRrrUUu.uUU....",
            ".RRrrUUu.uUU....",
            ".....UUU.UUU....",
            "....KKKK..KKKKK.",
            "....KKKK..KKKKK.",
            "....KKKK...KKKKK",
        ],
    },
    'king': {
        # FRONT — trapezoid robe + crown + lit eyes kept; four fixes:
        # emerald carved into the gold column rows 13-15 (L diamond,
        # G base, W sparkle, gold ring), scepter shifted 1px out with
        # a transparent gap rows 4-8 and a 3px cob fan rows 2-4,
        # mustache re-toned to beard-dark with one cream dip px (row 7)
        # + cream lower-lip light (row 8), hem curved rows 19-20 with
        # dark-gold 'a' trim, shoulder highlight cluster row 9,
        # R jewel at crown centre row 1.
        'down': [
            "......aYaYa.....",
            ".....aYYRYYa....",
            "yYY.aYYYYYYYa...",
            "YyYbHHHHHHHHbb..",
            "yg.BHHHHHHHHBb..",
            ".g.BHWKHHKWHBb..",
            ".g.BHHHsSHHHBb..",
            ".g.bbbbbWbbbbb..",
            ".g.BBBbbWBBBBB..",
            ".gLLLGGGGYGGGG..",
            ".gGLGGGGYYGGGG..",
            ".gGLGGGGYYGGGGG.",
            ".gGLGGGGYYGGGGG.",
            ".gGLGGGYLYGGGGG.",
            ".gGLGGYLWLYGGGG.",
            ".gHLGGGYGYGGGHH.",
            ".gHGGGGGYYGGGGG.",
            ".GGGGGGGYYGGGGG.",
            ".GGGGGGGYYGGGGG.",
            "..GGGGGaaGGGGG..",
            "....GGGaaGGG....",
            "....BB....BB....",
            "....BBB...BBB...",
            "....KKK...KKK...",
        ],
        # BACK — robe back with gold trim spine, crown back, beard/hair
        # mass from behind, scepter at the same screen side (left)
        # with its gap rows 4-8, hand on the shaft rows 15-16.
        'up': [
            "......aYaYa.....",
            ".....aYYYYYa....",
            "yYY.aYYYYYYYa...",
            "YyYbBBBBBBBBbb..",
            "yg.BBBBBBBBBBb..",
            ".g.BBBBBBBBBBb..",
            ".g.BBBBBBBBBBb..",
            ".g.BBBBBBBBBBb..",
            ".g.bBBBBBBBBBb..",
            ".gGLGGGGGYGGGG..",
            ".gGLGGGGGYGGGGG.",
            ".gGLGGGGGYGGGGG.",
            ".gGLGGGGGYGGGGG.",
            ".gGLGGGGGYGGGGG.",
            ".gGLGGGGGYGGGGG.",
            ".gHLGGGGGYGGGHH.",
            ".gHGGGGGGYGGGGG.",
            ".GGGGGGGaGGGGGG.",
            ".GGGGGGGaGGGGGG.",
            "..GGGGGaGGGGGG..",
            "....GGGaaGGG....",
            "....BB....BB....",
            "....BBB...BBB...",
            "....KKK...KKK...",
        ],
        # RIGHT PROFILE — robe trapezoid in profile, crown profile,
        # beard profile mass at the front, one lit eye near the front
        # edge row 5, scepter vertical at the front hand (col 13,
        # cob fan rows 2-4), gem shown edge-on rows 13-14.
        'right': [
            ".....aYaY.......",
            "....aYYYa.......",
            "....aYYYYa.yYY..",
            "...bbHHHHHHbYyY.",
            "...bBHHHHHHBb.g.",
            "...bBHHHWKBb.g..",
            "...bBHHHsSBbbg..",
            "...bBBBBBBBbbg..",
            "...BBBBBBBBBBg..",
            "...LLGGGGGGG.g..",
            "...GLGGGGGGGGg..",
            "..GLGGGGGGGGGg..",
            "..GLGGGGGGGGGg..",
            "..GLGGGGGLYGGg..",
            "..GLGGGGGLWGGg..",
            "..GLGGGGGGGGHg..",
            "..GLGGGGGGGGHg..",
            "..GGGGGGGGGGG...",
            "..GGGGGGGGGGG...",
            "...GGGGGaaGGG...",
            ".....GGGaaGG....",
            "....BB....BBBB..",
            "....BBB...BBBBB.",
            "....KKK...KKKKK.",
        ],
    },
}

_CM = SPRITES['cornman']
_D, _U, _R = _CM['down'], _CM['up'], _CM['right']

# Punch frames: [anticipation, extension, recover] per set.
# Anticipation = fist pulled back toward the shoulder, shoulder drops,
# head shifts 1px toward the punching side. Extension = arm straight
# off the shoulder line, fist a 2x2 cluster at full reach, skin-shade
# smear trail. Recover = arm halfway back, shoulder restored.
PUNCH = {
    # Front view, MARKED fist (screen-right) — 2 y px on the fist in
    # extension (and the mark stays on the fist in every frame).
    'down_r': [
        [  # anticipation: head shifted right, fist cocked at row 13
            "......YgGGY.....",
            "...LLYYYYYYYYLL.",
            "..GLLYYaYYaYYLLG",
            "..GLYYYaYYaYYYLG",
            "..GLYaYYaYYaYYLG",
            "..GLYYaYYYYaYYLG",
            "..GLWKKKKKKKKKLG",
            "..GLGHHHssHHHGLG",
            "..GLHHHHKKHHHHLG",
            ".UUUUUUUUUUUUURr",
            "..GUUUUUUUUUuGRr",
            ".UUKUYYYYYUUKURr",
            ".UUKUYRRUYUUKURr",
            ".UUKUYRUUYUUHyyR",
            ".UUKUYRRRYUUKURr",
            ".UUKUUUUUUUuKURr",
            ".HHUUUUUUUUUUURr",
            ".HHUUUUUUUUUUURr",
        ] + _D[18:],
        [  # extension: arm off the right shoulder, smear s/S, fist yy/HH
            *_D[:10],
            "..GUUUUUUUUUsSyy",
            ".UUKUYYYYYUUsSHH",
            *_D[12:16],
            ".HHUUUUUUUUUUURr",
            ".HHUUUUUUUUUUURr",
        ] + _D[18:],
        [  # recover: fist halfway home at rows 14, shoulder restored
            *_D[:14],
            ".UUKUYRRRYUUKHyy",
            _D[15],
            ".HHUUUUUUUUUUURr",
            ".HHUUUUUUUUUUURr",
        ] + _D[18:],
    ],
    # Front view, plain fist (screen-left) — no mark pixels.
    'down_l': [
        [  # anticipation: head shifted left, fist cocked at row 13
            "....YgGGY.......",
            ".LLYYYYYYYYLL...",
            "GLLYYaYYaYYLLG..",
            "GLYYYaYYaYYYLG..",
            "GLYaYYaYYaYYLG..",
            "GLYYaYYYYaYYLG..",
            "GLWKKKKKKKKKLG..",
            "GLGHHHssHHHGLG..",
            "GLHHHHKKHHHHLG..",
            *_D[9:13],
            ".HHHUYRUUYUUKURr",
            *_D[14:16],
            ".UUUUUUUUUUUHyyR",
            ".UUUUUUUUUUUHyyR",
        ] + _D[18:],
        [  # extension: arm off the left shoulder, smear S/s, fist HH
            *_D[:10],
            "HHSsUUUUUUUUUGRr",
            "HHSsUYYYYYUUKURr",
            *_D[12:16],
            ".UUUUUUUUUUUHyyR",
            ".UUUUUUUUUUUHyyR",
        ] + _D[18:],
        [  # recover: fist halfway home at row 14
            *_D[:14],
            ".HHHUYRRRYUUKURr",
            _D[15],
            ".UUUUUUUUUUUHyyR",
            ".UUUUUUUUUUUHyyR",
        ] + _D[18:],
    ],
    # Profile facing right — arm extends right, marked fist forward.
    'right_r': [
        [  # anticipation: fist pulled back to rows 15-17, cols 10-12
            *_R[:15],
            ".RRrGUUUUUUUHH..",
            ".RRrrUUUUUHHH...",
            ".RRrrUUUUUHHH...",
        ] + _R[18:],
        [  # extension: smear s/S cols 12-13, fist yy (mark) / HH
            *_R[:12],
            ".RRrGUUUUUUYsSyy",
            ".RRrGUUUUUUYsSHH",
            *_R[14:16],
            ".RRrrUUUUUUUUU..",
            ".RRrrUUUUUUUUU..",
        ] + _R[18:],
        [  # recover: fist halfway home at rows 14-15, cols 13-14
            *_R[:14],
            ".RRrGUUUUUUYUHy.",
            ".RRrGUUUUUUUUHy.",
            ".RRrrUUUUUUUUU..",
            ".RRrrUUUUUUUUU..",
        ] + _R[18:],
    ],
    # Back view — arm extends screen-right (his right hand, plain fist;
    # the marked left fist keeps its glint at screen-left throughout).
    'up_r': [
        [  # anticipation: right fist cocked at row 13
            *_U[:13],
            "UUURRRRRRRrrrHHH",
            *_U[14:16],
            "yHHRRRRRRRRRrUUU",
            "yHHRRRRRRRRRrUUU",
        ] + _U[18:],
        [  # extension: smear s/S cols 12-13, fist HH at the edge
            *_U[:10],
            "UUURRRRRRRRRsSHH",
            "UUURRRRRrrrrsSHH",
            *_U[12:16],
            "yHHRRRRRRRRRrUUU",
            "yHHRRRRRRRRRrUUU",
        ] + _U[18:],
        [  # recover: fist halfway home at row 14
            *_U[:14],
            "UUURRRRRRRrrrHHH",
            _U[15],
            "yHHRRRRRRRRRrUUU",
            "yHHRRRRRRRRRrUUU",
        ] + _U[18:],
    ],
}


def _validate(rows, charset, label):
    assert len(rows) == 24, f'{label}: {len(rows)} rows != 24'
    for i, row in enumerate(rows):
        assert len(row) == 16, f'{label} row {i}: width {len(row)} != 16'
        bad = set(row) - charset
        assert not bad, f'{label} row {i}: stray chars {bad}'


if __name__ == '__main__':
    for who, views in SPRITES.items():
        chars = PAL_CHARS if who == 'cornman' else KING_CHARS
        for view, rows in views.items():
            _validate(rows, chars, f'{who}.{view}')
            print(f'{who}.{view}: 24 rows x 16, charset OK')
    for name, frames in PUNCH.items():
        assert len(frames) == 3, f'punch.{name}: {len(frames)} frames != 3'
        for j, rows in enumerate(frames):
            _validate(rows, PAL_CHARS, f'punch.{name}[{j}]')
        print(f'punch.{name}: 3 frames x 24 rows x 16, charset OK')
    print('VALID')
