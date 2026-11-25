# Castle map swap — DONE (Remy, 2026-11-24 evening)

Michael's call: Remy did the swap instead of Grok (Grok would have been
coming in blind; Remy wired this castle in and knows where everything sits).

## What changed vs the save point — and nothing else
- Ground floor plate -> NEW-first-floor-from-michael.png (byte-identical to
  Michael's file, md5 a7d7c1b89e8034ef1f5771805561e1c0)
- Second floor plate -> NEW-second-floor-from-michael.png (byte-identical,
  md5 ddd7977095dc2f2a0707824117c43a71)
- One line in the castle exit hook: it now checks the hero is on the GROUND
  floor before firing (Michael's standing order from earlier today — in the
  save point, standing in that spot on the second floor also triggered the
  exit). Proven by diff: swap the plates back and remove that one condition
  and the castle is byte-identical to the save point's castle. The village
  side of the build is untouched, byte for byte.

## Why no re-mapping was needed
The redraws kept the layout geometry. Verified feature by feature against
the new art: all 17 doors, 32 furniture pieces, 10 stair/tower/hatch links,
13 arrivals, 3 chests, and both walk masks (overlaid on the new plates) land
where they belong. Walk masks and all link/door data are unchanged, so the
game plays exactly as the save point did — on the new art.

## Verification (all in the real engine, headless Chrome)
- The castle's built-in selftest: 74 passed, 0 failed — and its log is
  byte-identical to the same selftest run on the unmodified save point.
- Full round trip walked through the real input path (keyboard walker):
  village-side spawn -> west stairs -> second floor -> NE tower -> back
  down -> east stairs -> ground -> hatch -> dungeon -> back up -> kitchen
  door in and out -> out the main doors. Every leg OK.
- Exit hook A/B: hero held in the exit spot, walking down — second floor:
  0 exits fired (was the bug); ground floor: 11 fired (exit still works).
- Screenshots of both floors in-engine: new art renders, pieces and doors
  sit on their drawn twins.

## The build
Castle_NewMaps_REMY.html (this folder) — md5 below in the commit. The repo
root live build is untouched; this goes live only on Michael's say-so.

Open item carried over, unrelated to the swap: CornMan's back view is a
potted plant in the save point too — Michael's call pending on fixing it
from the sprite shelf.
