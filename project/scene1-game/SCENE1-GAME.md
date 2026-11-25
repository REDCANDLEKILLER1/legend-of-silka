# Scene 1 — the game file (act + playable village)
`Scene1_Act_And_Village_REMY.html` — one file, two maps:
1. The Scene 1 arrival act (fullscreen build, CornMan back unified,
   inn lady's true walk cycles) plays first, exactly as shipped in
   project/scene1-act/.
2. On the act's fade to black, the parent swaps to the playable
   Scene 1 village (Village_Scene_Playable_v10_WALKFIX, unmodified)
   and places CornMan at the inn door (318,972), facing out — the
   morning after the carry-in. Free play from there.
Parent is a thin shell: two srcdoc stages + a 400ms poll
(__actDone -> swap -> __game.ready() -> teleport/place). The act copy
inside differs from the standalone by ONE line: its end-hold sets
__actDone instead of restarting.
Verified 2026-11-25: act plays inside the shell (fall beat); end-state
-> swap -> placement logged (PLACED hero=433,972 after the test walk);
walked east from the inn door on the real keyboard input path,
collisions live. Headless note: rAF is frozen under virtual time in
this harness, so the act's end-state was stepped in the test copy
only; on device the act's own frame() produces it (line: clock=
DURATION, playing=false) — Michael's phone playback is the proof.
