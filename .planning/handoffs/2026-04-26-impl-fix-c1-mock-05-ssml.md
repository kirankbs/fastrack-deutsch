## Handoff — #216 — C1 mock_05 SSML: Google voices + remove zweimal

### What was built

Rewrote all three C1 mock_05 SSML files to replace Azure Neural voices with Google Cloud TTS voices (matching the mock_07 gold reference pattern) and removed the illegal "zweimal" play-twice announcement from part3.

### Files changed

- `.planning/audio-prompts/C1_mock_05_listening_part1.ssml` — replaced de-DE-KatjaNeural/ConradNeural with 8 unique Google voices (Wavenet-F/A/E/Neural2-F for female speakers, Wavenet-B/D/Neural2-B/Neural2-D for male speakers); added Wavenet-C announcer; restructured to match mock_07 format with 10s reading pause and 5s inter-speaker gaps
- `.planning/audio-prompts/C1_mock_05_listening_part2.ssml` — replaced KatjaNeural (interviewer) with Wavenet-E, ConradNeural (expert) with Wavenet-B; added Wavenet-C announcer frame matching mock_07 part2 pattern; preserved all interview content
- `.planning/audio-prompts/C1_mock_05_listening_part3.ssml` — replaced ConradNeural with Wavenet-D; removed full second playthrough block and "Sie hören den Vortrag zweimal" / "Sie hören den Vortrag jetzt ein zweites Mal" announcements; announcer now says "Sie hören den Vortrag einmal"; restructured as single continuous lecture per C1 plays-once spec

### Voice mapping pre/post

| File | Before (Azure) | After (Google) |
|------|---------------|----------------|
| part1 — announcer | none (inline prosody) | de-DE-Wavenet-C |
| part1 — Sp1/3/5/7 (female) | de-DE-KatjaNeural (shared) | Wavenet-F / Wavenet-A / Wavenet-E / Neural2-F |
| part1 — Sp2/4/6/8 (male) | de-DE-ConradNeural (shared) | Wavenet-B / Wavenet-D / Neural2-B / Neural2-D |
| part2 — announcer | none | de-DE-Wavenet-C |
| part2 — interviewer | de-DE-KatjaNeural | de-DE-Wavenet-E |
| part2 — expert | de-DE-ConradNeural | de-DE-Wavenet-B |
| part3 — announcer | none | de-DE-Wavenet-C |
| part3 — lecturer | de-DE-ConradNeural | de-DE-Wavenet-D |

### Zweimal instances removed

- part3 line 6: `<s>Sie hören den Vortrag zweimal.</s>` — removed
- part3 line 65: `<s>Sie hören den Vortrag jetzt ein zweites Mal.</s>` — removed
- part3: entire second playthrough block (lines 68–114) — removed
- part3 announcer text changed from "zweimal" to "einmal"

Total: 3 textual "zweimal" references removed, full duplicate lecture block eliminated.

### Tests

- Unit: n/a (SSML content files, no code)
- E2E: none — no observable browser change
- Typecheck: clean (no TypeScript touched)

### Quality gates

- compliance: n/a
- language: PASS — German content preserved verbatim, only structural/voice changes
- spec-tracker: n/a

### Notes

- part1 now uses 8 fully unique voices matching CR-9 spec, same voice assignment pattern as mock_07
- part2 voice gender swap (interviewer = female Wavenet-E, expert = male Wavenet-B) matches mock_07's interviewer/guest gender pattern
- part3 single playthrough aligns with C1-exam-format.md Section 1.4: C1 plays ONCE only
- All files tagged [PEDAGOGY-REWRITE] in header comments
