# Handoff — #241 — C1 CR-8 adoption: mock_01 playCount=2 + SSML + calibration doc + mock_07 R2 cleanup

**Issue:** #241
**Branch:** `fix-c1-cr8-playcount-mock01-and-mock07-r2`
**Date:** 2026-05-08

---

## What was built

4 targeted edits across 4 files:

1. **mock_01 HV3 `playCount` 1 → 2** — adopts CR-8 / telc Hochschule C1 spec. Also updated the inline `instructions` and `instructionsTranslation` strings which said "nur einmal" / "only once" to match.
2. **SSML intro for mock_01 part 3** — changed "Sie hören den Vortrag nur einmal" to "Sie hören den Vortrag zweimal"; updated header comment from `playCount=1 / played ONCE` to `playCount=2 / played TWICE (CR-8)`.
3. **Calibration doc CR-8 row** — rewrote CR-8 from the old "Hörverstehen total items / all playCount:1" entry to the definitive rule: `HV Teil 3 (Vortrag) playCount = 2 per telc Hochschule C1 spec`. Also corrected the Part 3 narrative sentence (line 81) that said "All parts playCount: 1" to reflect HV3 = 2.
4. **mock_07 R2 "x" option cleanup** — removed `"x"` from the `options` array of all 6 Lesen Teil 2 questions. Verified: no `correctAnswer` was `"x"` before removal. Post-fix pattern `["a","b","c","d","e"]` matches gold standard from mock_09 (PR #243).

---

## Files changed

- `apps/mobile/assets/content/C1/mock_01.json` — `listening.parts[2].playCount` 1→2; `instructions` / `instructionsTranslation` text updated to "zweimal" / "twice"
- `apps/mobile/assets/content/C1/mock_07.json` — `reading.parts[1].questions[0..5].options`: removed `"x"` from each (6 removals)
- `.planning/audio-prompts/C1_mock_01_listening_part3.ssml` — announcer line updated to "zweimal"; header comment updated
- `.planning/reports/C1-mock-01-pedagogy-review.md` — CR-8 row rewritten; HV section narrative corrected (new file to git — was untracked in main)
- `.planning/handoffs/2026-05-08-impl-fix-c1-cr8-mock01-mock07.md` — this file

---

## Per-file before/after

| File | Field | Before | After |
|---|---|---|---|
| mock_01.json | `listening.parts[2].playCount` | `1` | `2` |
| mock_01.json | `listening.parts[2].instructions` (end) | "Sie hören den Vortrag nur einmal." | "Sie hören den Vortrag zweimal." |
| mock_01.json | `listening.parts[2].instructionsTranslation` (end) | "You will hear the lecture only once." | "You will hear the lecture twice." |
| SSML part3 header | comment | `playCount=1`, `played ONCE` | `playCount=2`, `played TWICE (CR-8)` |
| SSML part3 announcer | line 23 | "Sie hören den Vortrag nur einmal." | "Sie hören den Vortrag zweimal." |
| calibration doc | CR-8 row | "Hörverstehen total items / all playCount: 1 ✓ schema." | "HV Teil 3 (Vortrag) playCount = 2 per telc Hochschule C1 spec — heard twice (no slowing, no pedagogical aids). HV1 and HV2 remain playCount: 1. Total: 28 items, 48 pts." |
| calibration doc | HV section narrative | "All parts playCount: 1." | "HV1 + HV2: playCount: 1. HV3 (Vortrag): playCount: 2 per CR-8 / telc Hochschule C1 spec." |
| mock_07.json | R2 Q1–Q6 options | `["a","b","c","d","e","x"]` (each) | `["a","b","c","d","e"]` (each) |

---

## Tests

- **Unit:** no new tests (content-only edits, no code logic changed)
- **E2E:** none — no observable browser change (JSON content + SSML planning asset)
- **Typecheck:** clean (`pnpm typecheck` — 2 tasks successful)
- **Pre-existing failures:** mobile test suite has pre-existing failures unrelated to this change (confirmed by running tests on clean main and on branch — identical failure set)

---

## Quality gates

- **compliance:** n/a — no auth/PII touched
- **language-checker (SSML German):** PASS — "Sie hören den Vortrag zweimal." is grammatically correct; only adverb changed, sentence structure preserved
- **pedagogy-director:** PASS — 0 P0 issues
  - CR-8 adoption: playCount=2 aligns with telc Hochschule C1 spec; HV1/HV2 remain playCount=1
  - mock_07 R2: all 6 correctAnswers (d, a, c, b, e, c) contained in trimmed [a,b,c,d,e] arrays
  - Calibration doc CR-8 row: unambiguous, no uncertainty language
- **exam-tester Layer A:** PASS — JSON valid, playCount is integer, options arrays are valid string arrays
- **exam-tester Layer B:** PASS — all correctAnswers present in options after x removal
- **spec-tracker:** n/a — no specs/ cross-reference to CR-8 found

---

## Notes

- The `C1-mock-01-pedagogy-review.md` file was untracked in main (not yet committed). This PR commits it for the first time along with the CR-8 row update.
- mock_07 R2 instructions text intentionally retains "Wenn kein Absatz passt, schreiben Sie 'x'" — this mirrors mock_09's post-fix state (PR #243 preserved the instructions text; only the `options` array entry was removed).
- Other mocks (02–06, 08) with HV3 `playCount=1` are out of scope for this PR — separate cleanup if desired.
