# Content Roadmap — Fastrack Deutsch
> Last updated: 2026-05-08 (B1 upgrade complete — 15 mocks, 25 grammar topics, 2,739 vocab) | Maintained by `content-strategist`

---

## Current State

| Level | Mocks (real) | Target | Vocab | Target | Grammar | Audio | Pedagogy | Status |
|-------|-------------|--------|-------|--------|---------|-------|----------|--------|
| **A1** | **10/10** | 10 | **~723** | 650 | **14** | **100%** (60 MP3s) | Standards-audit 2026-04-27 (P0/P1 closed) | **Shipped** |
| **A2** | **10/10** | 10 | **~1,338** | 1,300 | **20** | **100%** (60 MP3s) | Standards-audit 2026-04-27 (P0/P1 closed) | **Shipped** |
| **B1** | **15/15** | 15 | **2,739** | 2,700 | **25** | **45 SSML scripts** (M01-M10 MP3 rendered; M11-M15 pending GCP render) | B1 upgrade 2026-05-01–08: Hueber-rigour rewrite + 5 new mocks | **Shipped (v2)** |
| **B2** | **10/10** | 10 | **4,097** | 4,000 | **27** | **100%** (30 MP3s + 30 SSML, #83) | Standards-audit 2026-04-27 — Argumentation + FVG + 2024-26 added | **Shipped** |
| **C1** | **10/10** | 10 | **~1,430** | 6,000 | **33** | 0 MP3s (SSML not yet authored) | Batch pedagogy review complete | **Content in, audio pending** |

**Note (2026-05-08):** B1 fully upgraded. 15 mocks (10 rewritten v2 + 5 new), 25 grammar topics (+4 net from 21), 2,739 vocab entries (+109 net from 2,630 baseline, 32 B2-leaks archived to graveyard). Master plan that drove this wave: `.planning/B1-upgrade-plan-2026-05-01.md`. Audit reports: `.planning/reports/B1-*-2026-05-01.md`.

---

## A1 / A2 / B1 — Shipped Reference

All three levels are production-ready:

- A1/A2: 10 real mocks each with all required sections (4 sections each).
- B1: 15 real mocks with all 5 sections including Sprachbausteine.
- Vocab and grammar at or above Goethe target counts.
- Listening audio: A1/A2/B1 M01-M10 rendered via GCP WaveNet. B1 M11-M15 SSML scripts ready (pending MP3 render).
- Pedagogy review passes complete.

Renderer components in `apps/web/src/components/exam/`:
- `ListeningExam.tsx`, `ReadingExam.tsx`, `WritingExam.tsx`, `SpeakingExam.tsx`
- `SprachbausteineExam.tsx` (shipped PR #40 — covers B1 + B2)
- Audio player shipped PR #34.

Speaking recorder with mic + playback + retry shipped PR #46.

---

## B1 — Upgrade Complete (2026-05-08)

Full upgrade executed against [B1 upgrade plan](.planning/B1-upgrade-plan-2026-05-01.md), anchored on Hueber *Zertifikat Deutsch — 15 Modelltests* as the gold-standard reference.

### What changed from baseline (2026-04-27)

| Dimension | Before | After | Delta |
|-----------|--------|-------|-------|
| Mocks | 10 | 15 | +5 new (M11-M15) |
| Vocab entries | 2,630 | 2,739 | +109 net (+141 added, -32 B2-leaks archived) |
| Grammar topics | 21 | 25 | +4 new (Negation, Zweiteilige Konnektoren, Imperativ, Pronominaladverbien) |
| PEDAGOGY-REWRITE flags resolved | 3 open (id=1,2,9) | 3 resolved (id=1,2,9) | Konjunktiv II, Passiv, Modalverben cleared via PR #223 |
| PEDAGOGY-REWRITE remaining | — | 1 | id=21 Plusquamperfekt — topic-level explanation only; separate follow-up PR |
| Sprachbausteine register split | Monoculture (all du-form) | Diversified | 4 both-formal, 3 inverse, 8 canonical du/Sie |
| Schreiben prompt variety | 10/10 private letter | Distributed per Hueber | 6 private, 2 semi-formal inquiry, 1 formal complaint, 1 arrangement-change |
| Listening T3 stems | Templated (same 3 patterns) | Unique per mock | Drawn from Hueber stem repertoire |
| Sprechen T3 archetypes | 5/10 party/festival | Distributed | 4 party, 3 trip/Ausflug, 1 gift, 1 community event, 1 Stadtbummel |

### Grammar inventory — all 25 topics (B1)

| id | Topic | New in B1 upgrade? |
|----|-------|--------------------|
| 1 | Konjunktiv II — würde-Form, hätte und wäre | — (PEDAGOGY-REWRITE cleared PR #223) |
| 2 | Passiv — Vorgangspassiv und Zustandspassiv | — (PEDAGOGY-REWRITE cleared PR #223) |
| 3 | Relativsätze — der, die, das in allen Kasus | — |
| 4 | Konnektoren — weil, da, denn, obwohl, trotzdem | — (restructured PR #223) |
| 5 | Temporale Nebensätze — wenn, als, nachdem, bevor, während | — |
| 6 | Finale Nebensätze — damit und um...zu | — |
| 7 | Wechselpräpositionen und feste Präpositionen — Dativ/Akkusativ/Genitiv | — (upgraded PR #205) |
| 8 | Reflexive Verben mit Präpositionen | — |
| 9 | Modalverben im Perfekt und in der Vergangenheit | — (PEDAGOGY-REWRITE cleared PR #223) |
| 10 | Futur I — Zukunft und Vermutung | — |
| 11 | Infinitiv mit und ohne zu | — |
| 12 | Adjektivdeklination — alle Artikel, alle Kasus | — |
| 13 | Indirekte Rede — Konjunktiv I (Grundlagen) | — |
| 14 | Komparativ und Superlativ — Sonderformen | — |
| 15 | Pronomen — Personal, Possessiv, Demonstrativ, Indefinit | — |
| 16 | Verben mit festen Präpositionen | — |
| 17 | n-Deklination — schwache Maskulina | — (renamed, Nominalisierung dropped PR #223) |
| 18 | Partizip I und Partizip II als Adjektiv | — |
| 19 | Trennbare und untrennbare Verben | — |
| 20 | Je...desto und andere Vergleichskonstruktionen | — |
| 21 | Plusquamperfekt — hatte/war + Partizip II | — (PEDAGOGY-REWRITE in explanation: pending fix) |
| 22 | Negation — nicht vs. kein vs. nichts/niemand/nie/kaum | **NEW** (PR #153) |
| 23 | Zweiteilige Konnektoren — zwar...aber, sowohl...als auch, weder...noch etc. | **NEW** (PR #158) |
| 24 | Imperativ — du/ihr/Sie + irregular stems + trennbare Verben | **NEW** (PR #164) |
| 25 | Pronominaladverbien — darauf, daran, dafür, davon, dazu / worauf, woran etc. | **NEW** (PR #195) |

### Mock Distribution — all 15 (v2)

| Mock | Theme | Schreiben Type | SB Register | SP3 Archetype |
|------|-------|----------------|-------------|---------------|
| 01 | Freizeit & Hobbys | Private letter | Canonical (du/Sie) | Party/Geburtstag |
| 02 | Arbeit & Praktikum | Private letter | Inverse (Sie/du) | Trip/Ausflug |
| 03 | Wohnen & Umzug | Private letter | Canonical (du/Sie) | Trip/Ausflug |
| 04 | Bildung & Kurse | Semi-formal inquiry | Inverse (Sie/du) | Party/Geburtstag |
| 05 | Gesundheit | Private letter | Both formal | Housing planning |
| 06 | Reisen | Formal complaint | Inverse (Sie/du) | Community event |
| 07 | Umwelt & Natur | Private letter | Both formal | Community event |
| 08 | Technologie | Private letter | Canonical (du/Sie) | Gift planning |
| 09 | Kultur & Kunst | Semi-formal inquiry | Inverse (Sie/du) | Stadtbummel |
| 10 | Feste & Feiern | Arrangement-change | Both formal | Party/Feiern |
| 11 | Arbeit und Karriere (NEW) | Private letter | Canonical (du/Sie) | Trip/Stadtbummel |
| 12 | Gesundheit und Lebensstil (NEW) | Private letter | Inverse (Sie/du) | Gift planning |
| 13 | Reisen & Mobilität (NEW) | Private letter | Canonical (du/Sie) | Trip/Ausflug |
| 14 | Familie und Generationen (NEW) | Private letter | Both formal | Party/Geburtstag |
| 15 | Medien und digitales Leben (NEW) | Private letter | Inverse (Sie/du) | Community event |

### PR History — B1 Upgrade Wave (2026-05-01 to 2026-05-08)

| Workstream | PR | Merged |
|------------|----|--------|
| Planning: Hueber OCR refs + audit reports + upgrade plan | #167 | 2026-05-01 |
| Grammar: Negation topic (id=22) | #153 | 2026-05-01 |
| Grammar: Zweiteilige Konnektoren (id=23) | #158 | 2026-05-01 |
| Grammar: Imperativ (id=24) | #164 | 2026-05-01 |
| Grammar: Pronominaladverbien (id=25) | #195 | 2026-05-01 |
| Grammar: Präpositionen upgrade (G6-G10 finalised) | #205 | 2026-05-01 |
| Grammar: Konnektoren + Konjunktiv II/Passiv/Modalverben + n-Dekl finalize | #223 | 2026-05-03 |
| Mock 01 — rewrite v2 | #156 | 2026-05-01 |
| Mock 02 — rewrite v2 | #154 | 2026-05-01 |
| Mock 03 — rewrite v2 | #160 | 2026-05-01 |
| Mock 04 — rewrite v2 | #162 | 2026-05-01 |
| Mock 05 — rewrite v2 | #166 | 2026-05-01 |
| Mock 06 — rewrite v2 + formal complaint | #169 | 2026-05-01 |
| Mock 07 — rewrite v2 + community-event SP3 | #197 | 2026-05-01 |
| Mock 08 — rewrite v2 + secondhand R3 | #200 | 2026-05-01 |
| Mock 09 — rewrite v2 + pets R3 + Stadtbummel SP3 | #207 | 2026-05-03 |
| Mock 10 — rewrite v2 + weddings R3 + arrangement-change | #209 | 2026-05-03 |
| Mock 11 NEW — Arbeit und Karriere | #229 | 2026-05-06 |
| Mock 12 NEW — Gesundheit und Lebensstil | #227 | 2026-05-04 |
| Mock 13 NEW — Reisen & Mobilität | #231 | 2026-05-07 |
| Mock 14 NEW — Familie und Generationen | #226 | 2026-05-03 |
| Mock 15 NEW — Medien und digitales Leben | #235 | 2026-05-07 |
| Vocab: batches B1-B10 (discourse + core verbs + register + B2-leak prune) | #234 | 2026-05-04 |
| Audio SSML: M11-M15 (15 scripts) | #236 | 2026-05-04 |

### B1 — Remaining Follow-Ups

1. **MP3 render for M11-M15 (user task).** 15 SSML scripts in `.planning/audio-prompts/` (B1_mock11-15_listening_part1-3.ssml). Run `render_audio.py` once GCP WaveNet credentials available. Output: `assets/audio/B1/mock{11-15}/listening_part{1,2,3}.mp3`.

2. **M11/M12 Listening Teil 3 content review (separate follow-up PR).** Both mocks carry `PLACEHOLDER` comments in Teil 3 SSML — dialogues were inferred from question explanations rather than explicit JSON content. A reviewer should verify the 5 dialogues per mock match intended questions before GCP render. See `.planning/audio-prompts/B1_M11-M15_manifest.md` for notes.

3. **id=21 Plusquamperfekt PEDAGOGY-REWRITE.** Topic-level explanation field still flagged. Exercises are clean. ~30-min fix PR.

### B1 Reference Artifacts

| File | Purpose |
|------|---------|
| `.planning/B1-upgrade-plan-2026-05-01.md` | Master plan — workstreams WS-A through WS-D |
| `.planning/research/B1-Hueber-15-mocks-inventory-2026-05-01.md` | Per-mock matrix (15×14) + cross-mock patterns |
| `.planning/research/B1-exam-format.md` | telc B1 section spec — confirmed accurate, used as authoring template |
| `.planning/research/B1-pdf-reference/` | OCR'd Hueber mocks (mock-01.txt … mock-15.txt + transcripts) |
| `.planning/reports/B1-existing-mock-audit-2026-05-01.md` | Audit of pre-upgrade 10 mocks — register monoculture diagnosis |
| `.planning/reports/B1-vocab-audit-vs-Hueber-2026-05-01.md` | Vocab gap analysis — coverage + B2-leak identification |
| `.planning/reports/B1-grammar-audit-vs-Hueber-2026-05-01.md` | Grammar gap analysis — 4 missing topics, 3 PEDAGOGY-REWRITE flags |
| `.planning/reports/B1-pedagogy-audit-2026-04-27.md` | Earlier pedagogy review — still valid, complements Hueber audit |
| `.planning/reports/B1-final-language-check-2026-05-08.md` | Final language-checker sweep post-upgrade |
| `.planning/B1-vocab-graveyard-2026-05-03.md` | Archived B2-leak entries removed from B1_vocabulary.json |
| `.planning/audio-prompts/B1_M11-M15_manifest.md` | SSML manifest (voice assignments, durations, T3 placeholder notes) |

---

## B2 — Shipped (2026-04-21)

All 12 content PRs merged. MP3 audio rendered via GCP WaveNet (PR #83).

### PR Status by Mock

| Mock | Theme | PR | Status |
|------|-------|----|--------|
| mock_01 | Beruf & Arbeitswelt | #61 | **Merged** |
| mock_02 | Bildung & Studium | #74 | **Merged** |
| mock_03 | Gesundheit & Medizin | #72 | **Merged** |
| mock_04 | Medien & Kommunikation | #73 | **Merged** |
| mock_05 | Umwelt & Nachhaltigkeit | #76 | **Merged** |
| mock_06 | Reisen & Mobilität | #75 | **Merged** |
| mock_07 | Technologie & Digitalisierung | #81 | **Merged** (1 rewrite applied) |
| mock_08 | Gesellschaft & Integration | #79 | **Merged** |
| mock_09 | Kultur & Kunst | #78 | **Merged** |
| mock_10 | Wirtschaft & Konsum | #80 | **Merged** |
| B2_vocabulary.json (4,016 entries) | — | #77 | **Merged** |
| B2_grammar.json (25 topics) | — | #62 | **Merged** (3 reorder-exercise fixes applied) |
| B2 audio MP3s (30 files) | — | #83 | **Merged** |
| B2 SSML mocks 01-06 | — | embedded in mock PRs | Shipped |
| B2 SSML mocks 07-10 | — | #82 | **Merged** |

### B2 Topic Distribution (actual)

| Mock | Theme | Hören T2 Guest | Schreiben Prompts |
|------|-------|----------------|-------------------|
| 01 | Beruf & Arbeitswelt | Dr. Sabine Richter (Berufsbildungsforschung Bonn) | Beschwerdebrief / Homeoffice-Stellungnahme |
| 02 | Bildung & Studium | — | — |
| 03 | Gesundheit & Medizin | — | — |
| 04 | Medien & Kommunikation | — | — |
| 05 | Umwelt & Nachhaltigkeit | — | Kreislaufwirtschaft theme |
| 06 | Reisen & Mobilität | — | Nachtzug/E-Bike/Overtourism |
| 07 | Technologie & Digitalisierung | — | KI & Mittelstand |
| 08 | Gesellschaft & Integration | — | — |
| 09 | Kultur & Kunst | — | — |
| 10 | Wirtschaft & Konsum | — | — |

### B2 — Remaining Follow-Ups

1. **MP3 render (GCP, user task)** — Run `render_audio.py` against all 30 B2 SSML scripts (mocks 01-10, 3 parts each) once GCP WaveNet credentials are available. Output to `assets/audio/B2/mock{01-10}/listening_part{1,2,3}.mp3`. No code changes needed; pipeline validated on A1+A2+B1.

2. **Advisory items from pedagogy review (non-blocking):**
   - mock_02 Lesen T3: instruction text says "Zwei" — verify count matches items authored.
   - mock_05 and mock_06: Sprechen T2 both use "Innerdeutsche Kurzstreckenflüge verbieten" — if a future mock_11+ is ever authored, rotate this topic.
   - mock_09 and mock_10: Dr. Mertens surname appears in both (different first name + field) — consider renaming one before merge.
   - SB T1 gap-position pattern (gap 1=Passiv, gap 5=Genitiv-Präp, gap 8=prädikatives Adj, gap 9=Partizipialattribut) uniform across mocks 02-06; varied in 07-10. Carry the rotation into C1.

---

## B2 Calibration Rules (legacy reference for C1 authoring)

Extracted from mock_01 pedagogy review and `.planning/handoffs/2026-04-20-impl-b2-mock-01.md`. Apply to all future B2-or-higher content:

| # | Rule |
|---|------|
| 1 | Hören: `playCount: 1` throughout. No exceptions at B2+. |
| 2 | Sprachbausteine T1: exactly 4 options per gap (a/b/c/d). B1 uses 3. |
| 3 | Sprachbausteine T2: exactly 15-option word bank, 10 gaps. |
| 4 | Lesen T1: 5 texts, 10 headings (5 distractors). |
| 5 | Lesen T2: 3-option MCQ only (not 4). |
| 6 | Lesen T3: 10 situations → 12 offers, at least 1 `"x"` (no match). |
| 7 | Schreiben: 2 prompts, candidate chooses 1. ~200 words, formal register. |
| 8 | Sprechen: 3 parts — Präsentation (dual topic cards A/B), Diskussion (4 Leitfragen), Gemeinsam Planen (5 dimensions). |
| 9 | Every question must have an `explanation` citing source + grammar rule + ≥1 distractor rationale. |
| 10 | No metalinguistic terms (Nominalisierung, Konjunktiv) in exam-facing question text — explanations only. |

---

## C1 — Active Backlog

C1 mocks (10) and grammar (33 topics) are authored and in the repo. Vocab seed (~1,430 entries across 6 bundles) is in place. Full target is ~6,000 vocab.

### C1 Current State

| Dimension | Shipped | Target | Gap |
|-----------|---------|--------|-----|
| Mocks | 10/10 | 10 | None — all authored, pedagogy reviewed; pending audio |
| Grammar topics | 33 | 30-35 | On target |
| Vocab entries | ~1,430 | 6,000 | ~4,570 entries outstanding |
| Audio SSML | 0 | 30 scripts | Not started |
| Audio MP3 | 0 | 30 files | Blocked on SSML |

### C1 — Remaining Work

1. **Vocab completion** — ~4,570 more entries needed to reach 6,000 target. Bundles 1-6 (Argumentation, Wirtschaft/Recht, Wissenschaft/Bildung, Medien/Politik, Kultur/Philosophie, FVG+Abstracta) are shipped. Additional thematic bundles needed.

2. **Audio SSML authoring** — 30 scripts for mocks 01-10 (3 parts each) not yet written. Unblocked now that mock content is complete and pedagogy-reviewed.

3. **MP3 render (GCP)** — follows SSML authoring.

---

## Reusable Tooling

| Tool | Location | Notes |
|------|----------|-------|
| `render_audio.py` | `.planning/render_audio.py` | GCP WaveNet. Validated on A1+A2+B1 (90 MP3s). Ready for B2/B1-M11-M15/C1 runs. |
| B1 authoring contract | `.planning/research/B1-exam-format.md` | Template reference — confirmed accurate against Hueber. |
| B2 authoring contract | `.planning/research/B2-exam-format.md` | Authoritative B2 spec. Use as C1 template baseline. |
| B2 pedagogy verdict | `.planning/pedagogy-review-b2-batch.md` | All 10 mocks scored. Advisory items listed. |

---

## What's Next for B1

Short list of remaining B1 follow-up items (none block other levels):

1. **MP3 render for M11-M15.** Run `render_audio.py` for the 15 new SSML scripts. User task.
2. **M11/M12 T3 SSML content review.** Both mocks have PLACEHOLDER comments in Teil 3 — dialogues should be verified against JSON questions before GCP render. Separate follow-up PR.
3. **id=21 Plusquamperfekt PEDAGOGY-REWRITE.** Explanation field still flagged. ~30-min fix PR.

Refer to `.planning/B1-upgrade-plan-2026-05-01.md` (WS-D section) for the original Wave 6 / post-ship checklist.

---

## Next Up — Top Items Across All Levels

Scored on 3 axes: Exam Coverage (40%) + Content Quality Gap (35%) + Production Readiness (25%).

### 1. C1 vocab completion — remaining ~4,570 entries (Score: 88)

Bundles 1-6 shipped (~1,430 entries). Additional thematic bundles needed to reach 6,000. Can run in parallel with SSML authoring.

### 2. C1 audio SSML authoring (Score: 80)

30 scripts needed (3 per mock × 10 mocks). Mock content is complete and unblocked. Use `B2 authoring contract` + `render_audio.py` as templates. C1-specific voice guidance: natural speed (1.0x), potentially 2 voices for interview sections.

### 3. B1 M11-M15 MP3 render (Score: 75 — user task)

15 SSML scripts ready in `.planning/audio-prompts/`. Run `render_audio.py` once GCP credentials available.

### 4. B1 id=21 grammar fix (Score: 45 — quick win)

Single PEDAGOGY-REWRITE flag in Plusquamperfekt explanation. ~30-min PR.

### 5. C1 mock audio SSML + MP3 (Score: 40)

Follows SSML authoring. 30 files × GCP WaveNet batch.

---

## Strategic Rules

1. **A1/A2/B1/B2 are fully shipped. No re-opening unless bug-driven.**
2. **B2 mock_01 calibration rules (table above) carry forward to C1 authoring.**
3. **Audio runs as a batch per level.** `render_audio.py` is the only step; do not re-author SSML.
4. **Never count stubs as content.** Placeholder mocks are not exam-ready.
5. **C1 vocab + SSML can run in parallel** — both are unblocked.
6. **Sprachbausteine renderer (PR #40) is level-agnostic — works for B1 and B2.** Sprachbausteine does NOT appear at C1 (telc C1 Hochschule spec confirmed).
7. **No `fs/promises` in app routes or `loadX.ts`.** ESLint guard active (PR #111) — use `@fastrack/content` static accessors. Background: prod hang family #102/#104/#106/#108.

---

## Session History

| Date | Built | PRs |
|------|-------|-----|
| pre-2026-04-10 | A1 mocks 01-10, vocab 650, grammar 12 | Multiple |
| 2026-04-10 | A1 SSML mocks 01-05 (15 scripts) | — |
| 2026-04-13 | Audio player (web) | #34 |
| 2026-04-13 | A1 MP3s mocks 01-05 (WaveNet) | #33 |
| 2026-04-13 | A2 mocks 01-10, vocab 800, grammar 15 | #21-#32 |
| 2026-04-19 | A1+A2 audio complete (60 MP3s); A2 vocab 1,300; A2 pedagogy review (17 rewrites); A1 pedagogy review (40 rewrites); B1 mock_01 | #35, #36, #37, #38, #39 |
| 2026-04-19–20 | Sprachbausteine renderer; B1 grammar 20 topics; B1 mocks 02-10; B1 vocab 2,400; B1 full listening audio | #40, #41, #42, #43, #44, #45, #47 |
| 2026-04-20 | Speaking recorder; rebrand telc-fasttrack → Fastrack Deutsch; UI upgrade phases 1-4 | #46, #48, #50, #51, #52, #53 |
| 2026-04-20 eve | B2 exam format spec; B2 mock_01 (Beruf & Arbeitswelt, worked example, 3 pedagogy rewrites + 3 language fixes); B2_grammar.json 25 topics (3 reorder fixes) | #61, #62 |
| 2026-04-20–21 | B2 mocks 02-10 (all themes, all CI green); B2_vocabulary.json 4,016 entries; B2 SSML mocks 01-10 (30 scripts); B2 pedagogy batch review — all 10 PASS | #72, #73, #74, #75, #76, #77, #78, #79, #80, #81, #82 |
| 2026-04-21 | B2 audio MP3s rendered (30 files, GCP WaveNet) — B2 fully shipped | #83 |
| 2026-04-21–24 | Web feedback FAB + GitHub Issues; Vercel Blob attachments; mobile hamburger menu; grammar level-scoping + dark-mode fixes | #85, #88, #89, #92, #94, #97, #101 |
| 2026-04-26–27 | Prod stability sweep — 4 fs-fanout Lambda hangs (`/exam`, `/exam/[mockId]`, `/grammar/[level]`, exam subroutes) all root-caused, fixed via static `@fastrack/content` imports + SSG. ESLint guard added to prevent regression. | #103, #105, #107, #109, #111 |
| 2026-04-27 | Pedagogy standards-audit batch (A1+A2+B1+B2). 4 research docs + 4 audit reports + 8 fix PRs. Closed all P0 (12) and most P1 across grammar + vocab. B1 vocab re-tagged against canonical 18 themes with word-class rebalance. | #120, #121, #122, #123, #124, #125, #126, #127 |
| 2026-05-01–08 | B1 upgrade wave: 10 mock rewrites (v2) + 5 new mocks (M11-M15) + 4 new grammar topics + G6-G10 finalized + 3 PEDAGOGY-REWRITE flags cleared + vocab +109 net + 15 audio SSML scripts + planning artifacts. | #153–#236 |
