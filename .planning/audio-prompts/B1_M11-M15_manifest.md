# B1 Mock 11–15 Audio SSML Manifest

Generated: 2026-05-01
Branch: b1-upgrade/audio-ssml-m11-m15

## Voice Assignments (B1 — rate=0.95 target)

All prosody rates in the scripts use SSML named rates (`slow` = ~0.85, `medium` = ~0.95) rather than
numeric values, consistent with the M01–M10 convention in this repo.

| Voice | Role |
|-------|------|
| de-DE-Wavenet-B | Narrator / Announcer — instructions, task labels |
| de-DE-Wavenet-C | Female speaker (primary) — main female character in dialogues |
| de-DE-Wavenet-D | Male speaker (primary) — main male character in dialogues |
| de-DE-Wavenet-A | Female speaker (secondary) — used for interview guests where distinct voice needed |
| de-DE-Wavenet-F | Male speaker (secondary) — statistics/data voice, older male characters |

---

## File Inventory

### Mock 11 — Topic: Arbeit und Beruf (job ads, homeoffice, workplace)

| File | Part | Questions | Voices Used | Play Count | Transcript Source | Est. Duration |
|------|------|-----------|-------------|------------|-------------------|---------------|
| B1_mock11_listening_part1.ssml | Teil 1 | 5 T/F | B (narrator), C (female), D (male) | 1x | Full — derived from JSON explanations | ~2.5 min |
| B1_mock11_listening_part2.ssml | Teil 2 | 10 T/F | B (narrator), C (moderatorin), D (Dr. Mertens) | 1x | Full — derived from JSON explanations | ~5 min |
| B1_mock11_listening_part3.ssml | Teil 3 | 5 MCQ | B (narrator), C (female), D (male) | 2x each | PLACEHOLDER — see note below | ~4 min |

**Mock 11 Part 3 note:** The mock_11.json on branch `b1-upgrade/mock-11-new` does not contain a
`parts[2]` (Teil 3) entry — the JSON ends after Teil 2. Dialogues in Part 3 were constructed from
the interview and workplace context of Mock 11. A content reviewer should verify the 5 dialogues
align with the intended questions before audio generation.

---

### Mock 12 — Topic: Gesundheit und Ernährung (Arztpraxis, Fitnessstudio, Frau Koch interview)

| File | Part | Questions | Voices Used | Play Count | Transcript Source | Est. Duration |
|------|------|-----------|-------------|------------|-------------------|---------------|
| B1_mock12_listening_part1.ssml | Teil 1 | 5 T/F | B (narrator), C (female), D (male) | 1x | Full — derived from JSON explanations | ~2.5 min |
| B1_mock12_listening_part2.ssml | Teil 2 | 10 T/F | B (narrator), C (moderatorin), A (Frau Koch) | 1x | Full — derived from JSON explanations | ~5 min |
| B1_mock12_listening_part3.ssml | Teil 3 | 5 MCQ | B (narrator), C (female), D (male) | 2x each | PLACEHOLDER — see note below | ~4 min |

**Mock 12 Part 3 note:** No Teil 3 data in `mock_12.json` on branch `b1-upgrade/mock-12-new`.
Dialogues constructed to match the health/nutrition theme of Mock 12. Content reviewer should
confirm dialogue topics before production. Suggested topics used: Arzt empfiehlt Bewegung,
Intervallfasten, Magenschmerzen Kind, Supermarkt laktosefrei, Kochkurs.

---

### Mock 13 — Topic: Reisen und Verkehr (sustainable travel, Nachtzüge, Fahrrad)

| File | Part | Questions | Voices Used | Play Count | Transcript Source | Est. Duration |
|------|------|-----------|-------------|------------|-------------------|---------------|
| B1_mock13_listening_part1.ssml | Teil 1 | 5 T/F | B (narrator), C (female), D (male) | 1x | Full — sourced directly from JSON explanations | ~2.5 min |
| B1_mock13_listening_part2.ssml | Teil 2 | 10 T/F | B (narrator), D (moderator), C (Frau Steiner), F (data) | 1x | Full — sourced directly from JSON explanations | ~5 min |
| B1_mock13_listening_part3.ssml | Teil 3 | 5 MCQ | B (narrator), C (female), D (male) | 2x each | Full — sourced directly from JSON explanations | ~4 min |

Mock 13 has the most complete JSON source — all three parts have full question explanations with
verbatim quotes. No placeholders needed.

---

### Mock 14 — Topic: Familie und Gesellschaft (Patchwork-Familien, Elternzeit, Lena + Opa)

| File | Part | Questions | Voices Used | Play Count | Transcript Source | Est. Duration |
|------|------|-----------|-------------|------------|-------------------|---------------|
| B1_mock14_listening_part1.ssml | Teil 1 | 5 T/F | B (narrator), C (female), D (male) | 1x | Full — sourced directly from JSON explanations | ~2.5 min |
| B1_mock14_listening_part2.ssml | Teil 2 | 10 T/F | B (narrator), C (moderatorin), A (Dr. Wendland), F (data) | 2x | Full — sourced directly from JSON explanations | ~10 min (×2) |
| B1_mock14_listening_part3.ssml | Teil 3 | 5 MCQ | B (narrator), C (Lena), F (Heinrich/Großvater) | 2x | Full — sourced directly from JSON explanations | ~5 min (×2) |

**Mock 14 Part 2 note:** The JSON specifies `playCount: 2` for Teil 2. This is unusual for B1 but
has been honoured — the SSML includes a full repeat with the "Sie hören den Text jetzt noch einmal"
marker and a 5-second gap, consistent with the A1 convention.

---

### Mock 15 — Topic: Digitale Medien (Medienkonsum, Doom-Scrolling, Social Media, Digital Detox)

| File | Part | Questions | Voices Used | Play Count | Transcript Source | Est. Duration |
|------|------|-----------|-------------|------------|-------------------|---------------|
| B1_mock15_listening_part1.ssml | Teil 1 | 5 T/F | B (narrator), C (female), D (male) | 1x | Full — sourced directly from JSON explanations | ~2.5 min |
| B1_mock15_listening_part2.ssml | Teil 2 | 10 T/F | B (narrator), C (moderatorin), D (Dr. Kern), F (data) | 1x | Full — sourced directly from JSON explanations | ~5 min |
| B1_mock15_listening_part3.ssml | Teil 3 | 5 MCQ | B (narrator), C (female), D (male) | 2x each | Full — sourced directly from JSON explanations | ~4 min |

---

## Summary

| Mock | Part 1 | Part 2 | Part 3 | Placeholders |
|------|--------|--------|--------|--------------|
| mock_11 | ready | ready | PLACEHOLDER | Part 3 dialogues |
| mock_12 | ready | ready | PLACEHOLDER | Part 3 dialogues |
| mock_13 | ready | ready | ready | none |
| mock_14 | ready | ready | ready | none |
| mock_15 | ready | ready | ready | none |

Total files: 15 SSML scripts
Files requiring content review before audio generation: 2 (mock11 part3, mock12 part3)

## Audio Generation

To generate MP3 files from these scripts, use the `generate-audio` mode with `mock_id` set to
each mock (e.g. `mock_id=B1_mock_11`). The standard curl template is documented in the agent
system prompt. GCP credentials must be configured (`gcloud auth print-access-token`).

Output paths:
- `apps/mobile/assets/audio/B1/mock11/listening_part{1,2,3}.mp3`
- `apps/mobile/assets/audio/B1/mock12/listening_part{1,2,3}.mp3`
- `apps/mobile/assets/audio/B1/mock13/listening_part{1,2,3}.mp3`
- `apps/mobile/assets/audio/B1/mock14/listening_part{1,2,3}.mp3`
- `apps/mobile/assets/audio/B1/mock15/listening_part{1,2,3}.mp3`
