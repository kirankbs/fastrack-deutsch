# B1 Final Language Check — 2026-05-08

**Scope:** Post-upgrade sweep covering all B1 content after the 2026-05-01–08 upgrade wave.
**Files checked:**
- `apps/mobile/assets/content/B1/mock_*.json` (15 mocks)
- `apps/mobile/src/data/grammar/B1_grammar.json` (25 topics)
- `apps/mobile/src/data/vocabulary/B1_vocabulary.json` (2,739 entries)

**Check axes:**
1. Structural compliance — section presence, question counts, option counts
2. Vocab level compliance — no B2+ leaks, all entries tagged B1
3. German accuracy — instruction text, question stems, example sentences
4. English UI text consistency — capitalization and phrasing patterns
5. Grammar topic integrity — PEDAGOGY-REWRITE flag audit

---

## 1. Structural Compliance

### Mocks (all 15)

| Check | Result |
|-------|--------|
| All 15 mocks parse as valid JSON | PASS |
| All 15 have level=B1 | PASS |
| M01-M10 version=2, M11-M15 version=1 | PASS |
| All 15 have exactly 5 sections (listening, reading, sprachbausteine, writing, speaking) | PASS |
| All listening sections have 3 parts | PASS |
| All questions have `explanation` field | PASS |
| SB Part 1: 3 options per gap (all 15 mocks) | PASS |
| SB Part 2: 10 gaps (14/15 mocks) | PASS — 1 issue (see below) |
| SB Part 2 word bank size: 15 options (A-O) | PARTIAL — 8 of 15 mocks have 16 options (see below) |
| Listening T2 playCount=2 | FAIL — 13 of 15 mocks have T2 at playCount=1 (see below) |
| Reading T1: 5 situations + 8 headings | PASS (all 15 consistent) |

**Issue 1 — Listening T2 playCount (P1, all mocks except mock_09 and mock_14):**
The B1 exam format spec states Listening Teil 2 (10 T/F items, radio broadcast) should be heard TWICE. 13 of 15 mocks have `playCount=1` on this part. Only mock_09 and mock_14 are correct at playCount=2. This is a systematic misconfiguration introduced during the v2 rewrite wave. Flag for a dedicated fix PR (1-line change × 13 mocks).

**Issue 2 — SB Part 2 word bank size (8 mocks: 01, 04, 07, 12, 13, 14, 15; also mock_09):**
The B1 spec says SB T2 word bank = 15 options (A-O) with 5 distractors for 10 gaps. Eight mocks use 16 options (A-P). This gives candidates one extra option which makes distractors slightly easier to avoid. Not a blocking correctness issue (all correct answers remain valid) but is a format deviation. Flag for a follow-up PR.

**Issue 3 — mock_09 SB Part 2: 11 gaps instead of 10:**
mock_09 has 11 gaps in SB Part 2 (blankNumbers: 0, 31-40). The extra gap (blankNumber=0) appears to be a data artefact — the IDs suggest gap 0 was an accidentally included item outside the intended 10-gap sequence. Flag for fix.

---

## 2. Vocabulary Level Compliance

| Check | Result |
|-------|--------|
| Total entries | 2,739 |
| All entries tagged level=B1 | PASS |
| No entries missing `german` field | PASS |
| No entries missing `english` field | PASS |
| No entries missing `exampleSentence` | PASS |
| No duplicate `german` values | PASS |
| All entries have `topic` field | PASS |
| 18 canonical themes covered | PASS |

**Theme distribution (top 10):**

| Theme | Count |
|-------|-------|
| Politik und Gesellschaft | 308 |
| Gesundheit und Ernährung | 282 |
| Charaktereigenschaften | 219 |
| Beruf und Arbeit | 202 |
| Wirtschaft | 198 |
| Medien und Technik | 172 |
| Veranstaltungen | 160 |
| Wohnen | 148 |
| Bildung und Ausbildung | 143 |
| Klima und Umwelt | 140 |

Thinner themes (Sport: 25, Biografien und Geschichte: 26, Kommunikation und Sprache: 43, Adverbien und Zahlen: 19) reflect the closed-class/niche nature of those clusters — not a gap requiring action.

**English translation capitalization (minor):**
28 entries have English translations starting with a capital letter. Review shows these are all legitimate cases: proper nouns (Christmas, New Year's Eve, YouTube, Wi-Fi, CO2, HR, ID, PCR), institutional names (Federal Council), fixed phrases (Dear Sir or Madam, Kind regards, Best wishes), and single-word phrases that are standard capitalized in English. No inconsistency — all 28 are correctly capitalized. PASS.

---

## 3. German Accuracy

**Instruction text:** Sampled mocks 01, 11, 12, 15 across all 5 sections. All instruction texts are grammatically correct, use appropriate Siezen register, and follow consistent telc-style phrasing. No ß/ss errors, no anglicisms, no register mixing within individual instruction texts.

**Question stems:** Sampled 40 questions across listening and reading sections in mocks 01, 11, 12, 15. German grammar and vocabulary is accurate at B1 register. Vocabulary stays within Goethe B1 Wortliste range in question-facing text.

**Minor register note (non-blocking):** The `speaking` instructions in some mocks use "Ihr Partner" while others use "Ihr Partner / Ihre Partnerin" for gender-inclusive phrasing. This is an internal style inconsistency rather than an accuracy error. The Hueber reference texts from 2002 do not use gender-inclusive phrasing; current telc materials do. Flagged for style alignment if a future editing pass is done — not a blocking issue.

---

## 4. Grammar File

| Check | Result |
|-------|--------|
| 25 topics present | PASS |
| All topics have `id`, `topic`, `explanation`, `exercises` fields | PASS |
| All topics have ≥ 3 exercises | PASS |
| PEDAGOGY-REWRITE flags — resolved | id=1 Konjunktiv II, id=2 Passiv, id=9 Modalverben — CLEARED |
| PEDAGOGY-REWRITE flags — remaining | id=5 (exercise-level explanation only), id=13 (exercise-level explanation only), id=21 (topic-level explanation — primary concern) |

**id=21 Plusquamperfekt:** The topic-level `explanation` field begins with `[PEDAGOGY-REWRITE]`. This is the one remaining topic-level flag. Exercises and question text for id=21 are clean. Fix is straightforward (rewrite the explanation paragraph) — tracked as a separate ~30-min PR.

**id=5 and id=13:** Flags appear only in exercise `explanation` fields, not in topic-level explanations or question text. Lower priority than id=21. Still worth clearing in a follow-up.

---

## 5. Overall Assessment

| Area | Status | Action |
|------|--------|--------|
| Vocab (2,739 entries) | PASS | None |
| Grammar structure (25 topics) | PASS | id=21 explanation fix in follow-up PR |
| Mock structural compliance | MOSTLY PASS | 3 issues flagged (see below) |
| German accuracy | PASS | Minor gender-inclusive phrasing inconsistency — non-blocking |
| English UI text | PASS | None |

### Issues Flagged for Follow-Up PRs (not fixed in this PR — would balloon scope)

| Priority | Issue | Affected | Effort |
|----------|-------|----------|--------|
| P1 | Listening T2 playCount should be 2, not 1 | 13 of 15 mocks (all except mock_09, mock_14) | ~1 hr |
| P2 | SB Part 2 word bank has 16 options; spec says 15 | 8 of 15 mocks | ~30 min |
| P2 | mock_09 SB Part 2 has 11 gaps; spec says 10 | mock_09 only | ~15 min |
| P3 | id=21 Plusquamperfekt PEDAGOGY-REWRITE in topic explanation | grammar file, 1 field | ~30 min |
| P4 | id=5 and id=13 PEDAGOGY-REWRITE in exercise explanations | grammar file, 2 exercises | ~20 min |
| P5 | Speaking instructions gender-inclusive phrasing inconsistency | ~8 of 15 mocks | ~1 hr |

None of the above are blocking — the content is correct and learnable. The P1 playCount issue is the most exam-rigor-affecting and should be the first follow-up PR.
