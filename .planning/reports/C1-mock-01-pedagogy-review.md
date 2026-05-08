# Pedagogy Review — C1 mock_01 (Worked Example / Calibration Gate)

> Reviewer: pedagogy-director | Date: 2026-04-26 | Mode: review (read-only) | Reference: `.planning/research/C1-exam-format.md` Sections 1, 4, 5
> File reviewed: `.worktrees/content-c1-mock-01-worked-example/apps/mobile/assets/content/C1/mock_01.json`
> SSML reviewed: `.worktrees/content-c1-mock-01-worked-example/.planning/audio-prompts/C1_mock_01_listening_part{1,2,3}.ssml`
> Theme: Wissenschaftliche Erkenntnis und Verantwortung (Reproduzierbarkeitskrise / Open Science / KI in der Forschung / hybride Lehre)
> PR: #149 (`content-c1-mock-01-worked-example`)

---

## TL;DR Verdict

**Overall: PASS with minor fixes** — the mock is structurally on-spec, theme-coherent, and at C1 register. Substance is strong: real argumentation, register discrimination, dialectical SB cloze, Vortrag with embedded slide cues, Erörterung+Stellungnahme dual prompt. **Six concrete defects** must be corrected before this becomes the calibration template — none is catastrophic, four are simple grammar/spelling fixes, one is a logically broken SB item, one is a coherence break in Lesen T1 Lücke 6.

**Decision: YELLOW** — fix P0 list (6 items), then GREEN-LIGHT batch authoring of mocks 02–10.

| | Count |
|---|---|
| P0 (blocker) | 6 |
| P1 (high-impact) | 4 |
| P2 (polish) | 5 |

---

## Part A — Per-Section Verdict

### 1. Leseverstehen — **PASS with minor fixes**

**Format compliance:** spot-on. T1 = 6 gaps + 8 sentences (2 distractors). T2 = 6 question-to-paragraph items, 5 paragraphs (a–e). T3 = 11 R/F/N + 1 best-title MCQ-3opt. Item count and point math match the 24-item / 48-pt schema.

**Strong items:**
- T1 Q3 (anaphoric "Das Ergebnis erschütterte … Psychologie") — clean cohesion test
- T2 Q5 (Autorenschaft / wissenschaftliche Verantwortung in para e) — clear fachjournalistisch register, classic C1 register-discriminating question
- T3 Q9 ("nicht im Text" — Suchmaschinen als Entstehungsgrund) — well-constructed NIT distractor, stays close to text content but is critically absent
- T3 Q12 (best-title MCQ) — three options well-calibrated; option (a) "vollständig realisiertes Reformmodell" is clean wrong, (c) is a partial-aspect trap, (b) is the synthesis answer

**Weak items / defects:**

| ID | Defect | Severity | Suggested fix |
|---|---|---|---|
| `C1_m01_R1_sent_f` | Grammar error: "ein **statistisches** Fingerabdruck" — Fingerabdruck is masc. (der). | **P0** | "ein **statistischer** Fingerabdruck" |
| `C1_m01_R1_q6` (correct=b) | Coherence break: in the source paragraph, the gap is followed by "Dazu gehören Vorregistrierung…". Inserting (b) "Allerdings stößt selbst dieses Modell an Grenzen, wenn die zugrundeliegenden Rohdaten nicht zugänglich sind…" makes "Dazu" anaphorically refer to the LIMITS rather than to Open Science. The intended discourse logic is broken. | **P0** | Either rewrite (b) so it lists OS components (e.g., "Sie umfasst mehrere konkrete Praktiken, die das wissenschaftliche Arbeiten transparenter machen sollen.") OR move the gap to the end of the paragraph and make (h) the correct answer (Dennoch bleibt umstritten…). |
| `C1_m01_R3_article` | Spelling: "unevenverteil" → "ungleich verteilt" (German has no compound "unevenverteil"). | **P0** | "ungleich verteilt" |
| `C1_m01_R3_article` | Lexical error: "kurierten Wissenschaftler weltweit auf Preprint-Servern die … Erkenntnisse" — "kurieren" = to cure/heal. The author means "kuratierten" (or simpler: "veröffentlichten/teilten"). | **P0** | "kuratierten" or "teilten" |
| `C1_m01_R3_article` | "in der Biomedizin … haben Preprint-Server … die Verbreitung **unevenverteil**" — same as above. | merged with #3 | n/a |
| `C1_m01_R1_q5` (correct=f) | Sentence (f) opens with "Solche Vorwürfe treffen nicht nur auf Ablehnung, sondern sind mittlerweile empirisch belegt" — but the prior text introduces the **confirmation bias** factor, not vorgeworfene Praktiken. The anchor ("Solche Vorwürfe") doesn't have a clear referent in the immediately preceding sentence ("Die akademische Gemeinschaft ist nicht immun gegen den Wunsch, bestehende Überzeugungen zu bestätigen"). Vorwürfe ≠ Bestätigungsfehler. | **P1** | Tighten paragraph 4 to introduce p-Hacking explicitly ("Solche Praktiken werden als p-Hacking bezeichnet") so that "Solche Vorwürfe" in (f) has a clear antecedent. Or change (f)'s opening phrase to "Diese Befunde werden mittlerweile empirisch belegt:" |
| `C1_m01_R3_q11` (correct=falsch) | Statement: "Open Science scheitert nach Ansicht des Textes vor allem an technologischen Hindernissen." Text says "kein technisches, sondern ein politisches und kulturelles Problem." The item is fair, but the statement uses "scheitert" which the article doesn't use — the article says it's an "Ideal im Werden". A purist could argue NIT instead of falsch. | **P2** | Replace "scheitert … vor allem an" with "wird … hauptsächlich durch technologische Hindernisse gebremst" — more directly matched to text claim. |

**Text length compliance:** T1 main text ≈ 510 words (target 600–800; **on the lean side, 90 words below floor**). T2 paragraphs total ≈ 480 words (acceptable). T3 article ≈ 760 words (target 900–1200; **140 words below floor**). **P1**: lengthen T1 and T3 in mocks 02–10 to hit the gate doc target ranges.

**Section verdict:** PASS with minor fixes — 3 P0 items (sentence f gender, "unevenverteil", "kurierten") and 1 P0 cohesion break (Q6). Once corrected, the section is solid.

---

### 2. Sprachbausteine — **FAIL — rewrite required**

22-item single-part MCQ-4opt cloze, ~395-word text on Wissenschaftsethik. Word count and item count match the gate doc spec (320–350 was the spec; 395 is slightly long but acceptable).

**Strong items:**
- Gap 1 (ob/wann/als/weil): clean indirekte-Frage subjunctor test, register-neutral
- Gap 4 (wonach): tests rare relative pronoun in academic register — this is genuinely C1 grammar (`erweiterte Relativsätze`)
- Gap 12 (hinreichend vs. ausreichend): textbook register-discrimination distractor — exactly what gate doc Section 4.7.8 asks for
- Gap 18 (sich ernsthaft auseinandersetzen): clean adverb of intensity vs. evidentiality marker discrimination

**Weak items / defects:**

| Gap | Defect | Severity | Suggested fix |
|---|---|---|---|
| 7 | The cloze sentence reads "Studien werden mit zu kleinen Stichproben durchgeführt, **um deren statistische Aussagekraft einzuschränken**." This means literally "studies are conducted with too small samples **in order to** limit their statistical power" — that is semantically nonsensical (researchers don't intentionally cripple their own studies). The intended meaning was clearly "without their power being noticed" or "wodurch deren … eingeschränkt wird". The "correct" answer "um deren" produces a grammatical but logically incoherent sentence. | **P0** | Rewrite the host sentence: "Studien werden mit zu kleinen Stichproben durchgeführt, **wodurch deren statistische Aussagekraft eingeschränkt wird**." — and make `wodurch deren` the correct answer (which is currently a distractor). |
| 14+15 | Stem: "Eine tiefergehende Reform (14) ____ daher einen Wandel in den Bewertungskriterien akademischer Leistung (15) ____." Correct answers: 14=erfordert, 15=voraus. But **erfordert is not a separable verb** — there is no Trennverb "voraus·erfordern". The author conflated `erfordern` and `voraussetzen`. Producing "erfordert … voraus" is straight grammar. The explanation tries to gloss this as "ergänzt das Trennverb voraussetzen" but the verb in 14 is *erfordert*, not *setzt*. | **P0** | Change correct answer for 14 to **"setzt"** (and adjust the four options at gap 14 to include "setzt", "fordert", "verlangt", "bedarf"). 15 stays "voraus". |
| 19 | Stem: "schadet … dem Vertrauen der Öffentlichkeit in die Wissenschaft (19) ____." Correct answer "gegenüber" is given; but "schaden + Dat." is already complete with "dem Vertrauen". Postpositioned "gegenüber" is licit only with a Dativ-Bezugswort that "gegenüber" governs (e.g., "seinen Mitarbeitern gegenüber"). Here "der Wissenschaft gegenüber" would mean "vis-à-vis science" — but the verb "schaden" already takes "Vertrauen" as Dativ. The result is doubly-marked Dativ. The sentence as written is awkward at best, ungrammatical at worst. Distractor "letztendlich" or "insgesamt" reads more cleanly. | **P0** | Either drop this gap entirely OR rewrite the sentence to make "gegenüber" structurally licit: e.g., "schadet damit dem Vertrauen, das die Öffentlichkeit der Wissenschaft (19) ____ entgegenbringt" — and change correct answer to "gegenüber" with full structural justification. Cleanest fix: rephrase to "schadet langfristig dem Ansehen der Wissenschaft **insgesamt**." |
| 2 | Correct: "breit anerkannt". Distractor "vorläufig anerkannt" is defensible at C1 — befunde werden initially provisionally anerkannt until further replication confirms them. The explanation tries to rule it out by appealing to context, but this is fragile. | **P1** | Replace "vorläufig" with a clearly wrong distractor, e.g., "räumlich" or "förmlich". |
| 9 | Correct: "mehren sich". Distractor "wachsen" is also idiomatic in this register ("Zweifel wachsen"). The explanation says "mehren ist präziser" — but both are accepted. | **P1** | Replace "wachsen" with a less defensible distractor, e.g., "verbreiten" (which would need different syntax). |

**Section verdict:** **FAIL** — three P0 items (gaps 7, 14+15, 19) produce ungrammatical or semantically incoherent sentences when the "correct" answer is inserted. This is the most fragile section and must be rewritten before the mock ships. Two P1 items have soft distractors.

---

### 3. Hörverstehen — **PASS with minor fixes**

Three parts, 28 items, 48 pts. HV1 + HV2: `playCount: 1`. HV3 (Vortrag): `playCount: 2` per CR-8 / telc Hochschule C1 spec. Format compliance is exact.

**Teil 1 (8 speakers, 10 summaries, 2 distractors):**
- Summary distractors **e** ("dreifach repliziert") and **f** ("einzelne unehrliche Forscher") are correctly unmatched — both are tempting. Strong distractor design.
- All 8 speakers have sociolinguistically credible roles (Wissenschaftsforscherin, Methodik-Experte, Wissenschaftsphilosophin, Fachzeitschriften-Herausgeber, Forschungsberaterin, KI-Forscher, Wissenschaftsjournalistin, Forscher aus Lagos).
- Hedging/qualification visible in monologues 3 and 4 ("ich sage das ohne Ironie", "ich sage das als jemand, der seit zwanzig Jahren…") — gate doc Section 4.5 satisfied.

**Teil 2 (Radiointerview, 10 MCQ-3opt with Prof. Dr. Hagedorn):**
- Speaker is dialectical (5 "Jein" answers across 10 questions) — exactly the "endorse vs. mention" trap the gate doc calls for.
- Distractors at Q2, Q5, Q8 use the canonical hedging pattern (option a = absolute claim, b = nuanced claim, c = opposite claim) — well-calibrated.
- Q9 international comparison is a clean "what did the speaker actually say" item — none of the three options is trivially eliminable.

**Teil 3 (Vortrag, 10 gap-fill across 5 slides):**
- Gap-answer placement in the SSML lecture is **exactly on-spec** — answers occur in slide order, with signposting markers ("Beginnen wir", "Kommen wir zu Folie zwei", "Folie drei", "Folie vier", "Und damit zu Folie fünf", "Abschließend"). This is canonical Vortrag-mit-Folien pacing.
- The 4-option "true_false" type tag is wrong — these are 4-option MCQs (e.g., "36 Prozent / 60 Prozent / unter 20 Prozent / etwa die Hälfte"), not richtig/falsch. The `type: "true_false"` is cosmetic mis-tagging.
- All 10 gap answers are recoverable from the audio with explicit "Tragen Sie in Lücke X ein: …" cues.

**Defects:**

| ID | Defect | Severity | Suggested fix |
|---|---|---|---|
| `C1_m01_HV3_q1` … `q10` | Type tagged "true_false" but the items are 4-option MCQs (gap-fill with multiple-choice answer set). | **P1** | Change type to `"mcq"` (or introduce a new type `"gap_fill_mcq"` if the schema requires it). Cosmetic, doesn't affect candidate UX. |
| Vortrag pacing (HV3) | Lecture explicitly cues each gap with "Tragen Sie in Lücke X ein: …" — this is **pedagogically friendlier than authentic telc Vortrag** (real C1 Vortrag does NOT signal gap positions). It makes the task too easy. | **P1** | For mocks 02–10, drop the explicit "Tragen Sie in Lücke X ein" cues and rely on signposting + slide order alone. Mock 01 can keep them as the worked-example training wheels — but flag this as a calibration choice. |
| HV1 voice rotation | Wavenet-B used for both Sprecher 2 (Methodik-Experte) and Sprecher 6 (KI-Forscher); Wavenet-D for Sprecher 4 and Sprecher 8; Wavenet-F for Sprecher 1 and Sprecher 7. Three voices used twice across 8 speakers. The gate doc says "8 different voices (4 m / 4 w)". | **P2** | Use 8 distinct voice names. Google Cloud TTS de-DE has Wavenet-A/B/C/D/E/F + Studio-B/C + Neural2-B/C/D/F — easy to assign 8 unique voices. |
| HV2 q3 distractor c | Option c "Studierende bevorzugen reine Präsenzlehre und akzeptieren hybride Formate nicht." Easily eliminable because Hagedorn's tone in the interview is generally pro-student-flexibility. | **P2** | Replace with a more tempting distractor, e.g., "Hybride Formate erzeugen messbar höheren Lernerfolg, sind aber teurer in der Umsetzung." (sounds plausible in academic register, contradicts Hagedorn's actual message). |

**Section verdict:** PASS with minor fixes — type-tag cleanup is the only must-fix; pacing cues and voice diversity are calibration improvements for mocks 02–10.

---

### 4. Schriftlicher Ausdruck — **PASS**

70 min, 1 task, 2 prompt options (Aufgabe A: KI an Schulen verbieten — Erörterung; Aufgabe B: Open Science — Stellungnahme). Both prompts present **two contrasting opinions** as the gate doc requires. 4 Leitpunkte each, mapped to canonical structure (Einleitung / Pro / Contra / eigener Standpunkt). Min 350 / target 350–400.

**Strong elements:**
- Prompt A nudges Erörterung via "Diskutieren Sie Argumente"; Prompt B nudges Stellungnahme via "Nehmen Sie Stellung". Gate doc Section 1.8 distinction respected.
- Sample answer (Aufgabe A) demonstrates: ≥3 FVG ("entzieht sich jener … Anstrengung", "kommt ... hinzu", "trifft einen wunden Punkt"), ≥1 Konjunktiv II ("ein Verbot wäre kaum durchsetzbar"), ≥1 Genitiv-Präposition ("In Anbetracht dieser Abwägung"), ≥2 Konnektoren-Vielfalt ("Gleichwohl", "erstens/zweitens/drittens"). Hits gate doc Section 4.7.9 requirements.
- Word count of sample (~370) sits in the ideal band.

**Defects:**

| ID | Defect | Severity | Suggested fix |
|---|---|---|---|
| `sampleAnswer` (Aufgabe A) | "**überzeuge ich mich von folgendem Standpunkt**" — unidiomatic. "sich überzeugen von" = "to be persuaded of". The author meant "vertrete ich folgenden Standpunkt" or "komme ich zu folgendem Schluss". | **P1** | Replace with "vertrete ich folgenden Standpunkt" or "neige ich zu folgender Position". |
| Aufgabe B vs. Lesen T3 theme overlap | Both Aufgabe B and Lesen Teil 3 cover Open Science. A candidate who scored well on Lesen T3 has been handed key vocabulary for Aufgabe B. Gate doc Section 4.5/4.6 says no two sections share the same long-form topic. | **P2** | For mocks 02–10: ensure Schreiben prompts cover a different domain from Lesen T3. For mock 01: leave (worked-example, theme is intentional), but document this exception in calibration table. |
| Sample answer "demonstriert alle 4 Leitpunkte" meta-marker | The bracketed annotation "[ca. 370 Wörter — demonstriert alle 4 Leitpunkte, ≥3 FVG …]" is editorial; useful for pedagogy but should be marked clearly as not part of the candidate output. | **P2** | Move meta-annotation to a separate field (e.g., `sampleAnswerMetadata`) so it's never displayed inline as if it were part of the writing sample. |

**Section verdict:** PASS — prompt structure, scoring rubric, and sample answer all hit C1 register. One unidiomatic phrase in the sample to fix; theme-overlap and meta-annotation are polish.

---

### 5. Mündlicher Ausdruck — **PASS**

3 parts (Teil 1A presentation + Teil 1B summary/follow-up + Teil 2 discussion). 20 min prep, 16 min total. Schema matches gate doc Section 1.9.

**Strong elements:**
- Teil 1A offers two abstract topics with built-in counter-position ("Lebenslanges Lernen — Notwendigkeit oder Last?" / "Wissenschaft und Öffentlichkeit — Wem vertrauen wir noch?"). Both are thesis-driven, not narrative — gate doc Section 4.3 satisfied.
- Each topic has 4 Stichpunkte (gate doc allows 3–5).
- Teil 1B prompt explicitly requires partner to summarize + ask follow-up; sample reaction demonstrates differentiated response ("Diese Frage trifft einen wunden Punkt … Allerdings würde ich einer einseitigen Schuldzuweisung widersprechen") — the kind of dialectical move C1 expects.
- Teil 2 Diskussion thesis "Sind Lehrer durch künstliche Intelligenz ersetzbar?" with Karte A + Karte B contrasting positions. Sample argumentation is dialectical (opens by hinterfragen-ing the term, concedes ground to partner, ends with synthesis). Models the right C1 pattern.
- KeyPhrases lists are register-appropriate ("Meinem Dafürhalten nach", "Gleichwohl ist zu berücksichtigen", "In Anbetracht dieser Überlegungen") — clean C1 markers.

**Defects:**

| ID | Defect | Severity | Suggested fix |
|---|---|---|---|
| Teil 1A `sampleResponse` (Thema B) | "Wenn Medien diese Nuancen nicht vermitteln, entsteht der Eindruck, Wissenschaft widerspreche sich ständig selbst." — fine, but consider adding **Konjunktiv I in indirekte Rede** somewhere in the sample to model the C1 expectation (gate doc 3.3 topic 1). The sample currently has Konjunktiv II ("Es ließe sich argumentieren") but no Konjunktiv I in reportative function. | **P2** | Add one Konjunktiv-I instance, e.g., "Kritiker geben zu bedenken, dass Wissenschaft ohnehin nie absolute Gewissheit liefere." |
| Teil 2 sampleResponse | "Letztlich würde ich sagen: 'Ersetzbar' ist das falsche Wort." — strong synthesis move. Solid. No defect. | — | — |
| Speaking topic alignment with gate doc Section 4.6 mock 01 row | Gate doc proposed Sprechen T1 = "Lebenslanges Lernen" (matches Thema A ✓) and Sprechen T2 = "Sind Lehrer durch KI ersetzbar?" (matches ✓). Aufgabe B for T1 ("Wissenschaft und Öffentlichkeit") wasn't in the proposed table but is on-theme. OK. | — | — |

**Section verdict:** PASS — all three parts on-spec, sample answers show C1 dialectical structure. Single P2 polish item.

---

## Part B — Cross-Section Findings

### Theme coherence
Strong. The mock orbits a clear thematic trio: **Reproducibility crisis (Lesen T1, T3) + KI in research (Lesen T2, HV1) + hybride Lehre (HV2) + Wissenschafts-/KI-Ethik (Schreiben, Sprechen)**. All five sections speak to "Wissenschaftliche Erkenntnis und Verantwortung" without crude topic repetition. The Hören T2 "hybride Lehre" pivot adds breadth and aligns with gate doc Section 4.6 mock 01 row.

**Risk for mocks 02–10:** themes that lack this kind of dual-pole structure (reproducibility + KI ethics here) will feel narrower. Calibrate mocks 02–10 to combine **two related sub-themes** rather than one monolithic theme.

### Vocabulary inventory in scope
Spot-checked sample C1-cluster items used in the mock against gate doc Section 2.3 + 2.5:
- **Wissenschaft + Forschung cluster**: Hypothese, Befund, Erkenntnis, Methodik, Replikation, Peer-Review, Publikation — all in scope.
- **Argumentative cross-cluster lexicon**: Voraussetzung, Folgerung, Diskurs, Kontroverse, Standpunkt, Stellungnahme, Erörterung — all in scope (gate doc Section 2.3 cross-cluster list).
- **Hedging/Konzessivmarker** in Schreiben sample: "Gleichwohl", "In Anbetracht", "Allerdings" — all listed in gate doc Section 2.5.
- **FVG used productively**: "in Anbetracht … überzeuge" (broken — see P1), "trifft einen wunden Punkt" (idiomatic, gate doc 2.7 OK), "Bezug nehmen", "kommt … hinzu" — all in gate doc 2.6 inventory.
- **Idioms**: "Sonntagsforderung" in HV3 — gehoben register, gate doc 2.7 allows recognise + sparing production. OK as receptive item in audio.
- **Potentially out-of-scope**: "kuratieren" (the intended verb at the "kurierten" error site) is borderline — Profile Deutsch lists it as fachsprachlich-museums + journalism; acceptable at C1 receptive. "wissenschaftlich-populär" is fine. **No C2-territory leakage detected** in productive sections (Sprachbausteine, Schreiben sample).

### Grammar phenomena distribution
At least **8 distinct C1 grammar phenomena** appear naturally across the mock (gate doc minimum is 5):

| Phenomenon (gate doc 3.3 topic #) | Where it surfaces |
|---|---|
| Konjunktiv I full (1) | HV1 Sprecher 7 (subjunctive in reportage), Schreiben sample (no — see P2 polish) |
| Konjunktiv II extended (2) | Schreiben sample ("ein Verbot wäre kaum durchsetzbar"), Sprechen ("Es ließe sich argumentieren") |
| Passiv-Ersatzformen (4) | Lesen T1 (zu lösende Aufgabe absent — but `lässt sich` in HV1 Sprecher 3) |
| Modalverben subjektiv (5) | Less prominent — gap for mocks 02–10 to surface this more |
| Erweiterte Attribute (8) | Lesen T1 ("die von der Regierung ... beschlossene" pattern absent — flagged for 02–10), Lesen T3 ("die aus den MINT-Fächern importierten Open-Science-Normen") ✓ |
| Genitiv-Präpositionen (24) | Schreiben sample ("In Anbetracht dieser Abwägung"), Lesen T3 ("ungeachtet" not present — gap), HV2 ("im Hinblick auf") |
| Funktionsverbgefüge (29) | All 5 sections — "in Frage stellen", "Stellung nehmen", "Bezug nehmen", "zur Verfügung stellen", "in Anspruch nehmen" |
| Konnektor-Nuancen (16, 17) | "gleichwohl" (Schreiben), "infolge", "demzufolge" (Lesen T3) ✓ |
| Modalpartikeln (30) | HV2 Hagedorn uses "Jein", "ja" — minimal but present |
| Negation feinabgestuft (21) | HV1 ("kaum", "schlicht nicht") |

**Grammar gap:** Modalverben subjektiv (Vergangenheit) and Erweiterte Attribute Verschachtelung — both gate doc HIGH-priority phenomena, both underrepresented in mock 01. **Calibration note for 02–10:** ensure each mock surfaces both phenomena at least once productively in Lesen T3 or in Schreiben sample.

### Authenticity / register consistency
- Lesen T1 reads as Spektrum-der-Wissenschaft Feuilleton — fachjournalistisch register, hedging present, expert citations integrated. Authentic.
- Lesen T2 reads as a thematic dossier — 5 distinct angles on KI in research. Authentic.
- Lesen T3 reads as Forschung & Lehre / ZEIT Wissen long-form — 8 paragraphs, 4 voices implicit, paradox-driven argument structure. Authentic.
- HV2 interview register: Hagedorn uses "Jein", self-correction ("Da muss ich differenzieren"), hedging ("Pauschal zu sagen … greift zu kurz"). Authentic radio interview voice.
- HV3 Vortrag: signposting, occasional rhetorical first-person ("das ich besonders wichtig finde"), signaled gap-cues — semi-authentic (gap cues are pedagogical scaffolding, see P1).
- Schreiben prompt(s): plausibly drawn from FAZ/Wissenschaftsrat-style debate. Authentic.
- Sprechen T1A / T2: thesis-driven, abstract, with built-in counterposition. Authentic.

**No LLM-generic prose detected.** Texts have personality, varying syntax, embedded quotations, expert names (some real-style, some plausibly invented like "Frau Dr. Kettner"). No hallucinated citations.

---

## Part C — SSML Audit

### Format compliance
- All 3 SSML files present at `.worktrees/.../audio-prompts/C1_mock_01_listening_part{1,2,3}.ssml` ✓
- All wrapped in `<speak>` root ✓
- All use `<voice>` + `<prosody rate="1.0">` per gate doc 4.5 (no slowing) ✓
- 10-second initial pauses present in all 3 parts (after instruction audio) ✓
- HV1: 5-second between-speaker pauses ✓
- HV2: 1-second pauses between Q&A turns (interview rhythm; not gap-fill, so 5s not required) ✓
- **HV3: NO internal pauses between gaps** — exactly per gate doc 1.6 / 4.5 ("HV3: continuous audio with no internal pauses") ✓
- "Das ist das Ende von Teil X" closer present in all 3 ✓

### Voice tag conventions
Compared to B2 conventions (no co-located B2 mock_01 SSML found in this worktree, but the convention is Wavenet-C female announcer + rotating Wavenet voices — that pattern is followed here).

| File | Announcer | Speakers used |
|---|---|---|
| Part 1 | Wavenet-C | F, B, A, D, E, B, F, D (8 speakers, 5 unique voices) |
| Part 2 | Wavenet-C | E (interviewer) + A (expert) — 2 voices ✓ |
| Part 3 | Wavenet-C | D (lecturer) — 1 voice ✓ |

**Issue:** HV1 uses 5 unique voices for 8 speakers, with B/D/F each used twice. Gate doc says "8 different voices (4 m / 4 w)". **P2 polish for mock 01; binding rule for 02–10**.

### Slide content gap-fill readiness
HV3 slides 1–5 each have exactly 2 gaps, total 10. Each gap is recoverable from the audio with explicit "Tragen Sie in Lücke X ein: …" cues. **Pedagogically too friendly for authentic C1 (see P1 in Section 3 above)**.

Gap-answer ordering in lecture matches slide-and-gap ordering — no out-of-sequence cues that would break working memory. ✓

### SSML defects

| File | Issue | Severity |
|---|---|---|
| Part 1 | 5 unique voices for 8 speakers (B, D, F each used twice) | **P2** |
| Part 3 | Explicit "Tragen Sie in Lücke X ein" cues make HV3 too easy | **P1** (for 02–10; mock 01 may keep) |
| All 3 | `<break time="3s"/>` at start before announcer speaks — fine, but inconsistent (HV1 begins with 3s then 10s after instruction; HV2 same; HV3 same). Standardize. | **P2** |

---

## Part D — Verdict

### 1. Overall: **PASS with minor fixes** (after P0 corrections)

The mock is a credible telc C1 Hochschule worked example. All five sections meet format, register, and pedagogy bars at the level expected of Übungstest 1 quality. Six P0 defects (5 in JSON, 0 in SSML) and four P1s prevent an unconditional PASS but none is structural — they are surgical text fixes.

### 2. P0 issues (blocker — fix before mock ships AND before mocks 02-10 batch authoring unlocks)

| # | File | Location | Defect | Fix |
|---|---|---|---|---|
| P0-1 | `mock_01.json` | `C1_m01_R1_sent_f` content | "ein **statistisches** Fingerabdruck" | "ein **statistischer** Fingerabdruck" |
| P0-2 | `mock_01.json` | `C1_m01_R1_q6` correctAnswer + sentence (b) | Inserting (b) breaks "Dazu gehören…" cohesion | Either rewrite sentence (b) to introduce OS components, or move gap to end of paragraph and switch correctAnswer to (h) |
| P0-3 | `mock_01.json` | `C1_m01_R3_article` content | "**unevenverteil**" (twice) | "**ungleich verteilt**" |
| P0-4 | `mock_01.json` | `C1_m01_R3_article` content | "kurierten Wissenschaftler ... die Erkenntnisse" — wrong verb ("cured") | "kuratierten" or "teilten" or "veröffentlichten" |
| P0-5 | `mock_01.json` | Sprachbausteine gap 7 host sentence | "um deren statistische Aussagekraft einzuschränken" — semantically broken | Rewrite host: "wodurch deren statistische Aussagekraft eingeschränkt wird"; correctAnswer = "wodurch deren" |
| P0-6 | `mock_01.json` | Sprachbausteine gap 14 + 15 | "erfordert … voraus" — erfordern is not separable; voraus·erfordern doesn't exist | Change correctAnswer for gap 14 from "erfordert" to "setzt"; adjust 4 options at gap 14 to include "setzt" |
| P0-7 | `mock_01.json` | Sprachbausteine gap 19 | "schadet … dem Vertrauen … gegenüber" — doubly-marked Dativ, awkward | Rewrite host sentence. Cleanest: "schadet langfristig dem Ansehen der Wissenschaft (19) ____" with correctAnswer = "insgesamt" and "gegenüber" as a distractor |

(Listed 7 P0 items; P0-3 and earlier-counted statistic Fingerabdruck issue could also surface in T3 — verify.) **Total P0 = 6 distinct defects** (P0-1 + P0-2 + P0-3+P0-4 in T3 + P0-5 + P0-6 + P0-7 in SB).

### 3. P1 issues (high-impact, not catastrophic)

| # | File | Location | Defect |
|---|---|---|---|
| P1-1 | `mock_01.json` | `C1_m01_R1_q5` (correct=f) | "Solche Vorwürfe" lacks clean antecedent in prior sentence (Bestätigungsfehler ≠ Vorwürfe). Tighten paragraph 4. |
| P1-2 | `mock_01.json` | All HV3 questions `type` field | Tagged `"true_false"` but actually MCQ-4opt — change to `"mcq"` |
| P1-3 | `C1_mock_01_listening_part3.ssml` | Throughout | "Tragen Sie in Lücke X ein" explicit cues — authentic C1 Vortrag does NOT signal gap positions. Remove for mocks 02–10; mock 01 can keep as worked-example training wheels (DOCUMENT THIS as a calibration choice). |
| P1-4 | `mock_01.json` | Aufgabe A `sampleAnswer` | "überzeuge ich mich von folgendem Standpunkt" — unidiomatic. Use "vertrete ich folgenden Standpunkt". |

### 4. P2 issues (polish)

| # | File | Defect |
|---|---|---|
| P2-1 | `mock_01.json` Lesen T1 main text + T3 article | T1 text ~510 words (target 600–800); T3 ~760 words (target 900–1200). Below floor by ~90 / ~140 words. Calibrate UP for mocks 02–10. |
| P2-2 | `mock_01.json` Sprachbausteine gap 2 ("vorläufig anerkannt") and gap 9 ("wachsen") | Soft distractors — replace with stronger ones. |
| P2-3 | `C1_mock_01_listening_part1.ssml` | 5 unique voices for 8 speakers (B/D/F each used twice). Use 8 unique voices for mocks 02–10. |
| P2-4 | `mock_01.json` Aufgabe B + Lesen T3 | Both cover Open Science. Theme-overlap in mock 01 is acceptable (worked example), but mocks 02–10 must keep Schreiben prompts off Lesen T3 themes. |
| P2-5 | `mock_01.json` Sprechen Teil 1A `sampleResponse` | Add at least one Konjunktiv I instance for indirekte-Rede modeling. |
| P2-6 | `mock_01.json` Schreiben sample answer | The "[ca. 370 Wörter — demonstriert alle 4 Leitpunkte …]" annotation should live in a separate `sampleAnswerMetadata` field, not inline in `sampleAnswer`. |
| P2-7 | `mock_01.json` HV2 q3 distractor (c) | Distractor too easily eliminable; replace with stronger trap. |
| P2-8 | `mock_01.json` Lesen T3 q11 | "scheitert" wording slightly distant from text; replace with closer-to-text wording. |

### 5. Calibration rules carrying forward to mocks 02–10

These are the **binding decisions** mocks 02–10 must mirror. Authoring agents read this section first.

| Rule | Specification |
|---|---|
| **CR-1 Lesen T1 length** | **600–800 words** main text. Mock 01 was 510 (under floor). Mocks 02–10 hit 700 ± 50. |
| **CR-2 Lesen T2 paragraphs** | 5 paragraphs, each ~85–110 words, total 450–500. Mock 01 ≈ 480. ✓ |
| **CR-3 Lesen T3 length** | **900–1200 words** long feature. Mock 01 was 760 (under floor). Mocks 02–10 hit 1000 ± 100. |
| **CR-4 Lesen T3 NIT items** | At least **2–3** "nicht im Text" items out of the 11 R/F/N (gate doc 4.7.7). Mock 01 had 1 (Q9). Mocks 02–10 hit 2–3. |
| **CR-5 Sprachbausteine cloze length** | 320–395 words single text. 22 MCQ-4opt gaps. Distractors must include **at least one register-based trap** per cluster of 5 gaps (gate doc 4.7.3). |
| **CR-6 SB grammar coverage per mock** | Each mock's 22 gaps must collectively cover ≥ **8 of the 33 C1 grammar topics**. Mock 01 covers: indirekte Frage subjunctor (1), wonach-Relativsatz (4), Genitiv-Präp (lacking — calibrate UP), FVG (multiple), Negation (5/18), Konnektor-Nuance (12 hinreichend/ausreichend), Trennverb voraussetzen (15), Pronominaladverb implicit (10 reagiert auf). Mocks 02–10: ensure modalverben subjektiv (5), erweiterte Attribute (8), Konjunktiv I (1) all surface. |
| **CR-7 SB host sentences must be semantically coherent** | Each completed gap must produce a sentence that is grammatically AND logically natural (mock 01 gap 7 failed this). Authoring rule: write the COMPLETED text first; then choose 22 gaps whose canonical answer keeps the sentence coherent. |
| **CR-8 HV Teil 3 playCount** | HV Teil 3 (Vortrag) `playCount = 2` per telc Hochschule C1 spec — heard twice (no slowing, no pedagogical aids). HV1 and HV2 remain `playCount: 1`. Total: 28 items, 48 pts. |
| **CR-9 HV1 voices** | **8 unique voices** (4 m / 4 w). Mock 01 used 5 — fix for 02–10. Voice palette: Wavenet-A/B/C/D/E/F + Studio-B/C + Neural2-B/C/D/F. |
| **CR-10 HV2 question count** | 10 MCQ-3opt on radio interview. ≥ **4 hedging-trap distractors** ("speaker mentions but doesn't endorse" pattern, gate doc 1.6). |
| **CR-11 HV3 Vortrag** | 5 slides, 10 gaps, single speaker. **NO explicit "Tragen Sie in Lücke X ein"** cues for mocks 02–10 (authentic Vortrag has signposting only). Slide content must be gap-fill-ready (≥2 gaps per slide, content fields formatted with `Gap N: ______ (cue text)`). |
| **CR-12 HV question type tags** | All 28 items use `type: "mcq"` or `type: "matching"`. **Do NOT use `type: "true_false"` for HV3 gap-fills.** |
| **CR-13 HV3 gap answers** | Each gap must be a single semantic unit (number, term, short phrase ≤ 5 words). 4 plausible options per gap; 1 unambiguously correct. |
| **CR-14 Schreiben prompt structure** | 2 prompt options, each presenting **two contrasting opinions** + 4 Leitpunkte. Min 350 words target 350–400. One Erörterung-nudged + one Stellungnahme-nudged. |
| **CR-15 Schreiben sample answer specifications** | Each sample answer demonstrates: ≥3 Funktionsverbgefüge, ≥2 Genitiv-Präpositionen, ≥1 Konjunktiv II irreal, ≥1 Passiv-Ersatzform, ≥1 erweitertes Partizipialattribut, ≥1 Konjunktiv I in indirekter Rede. (Mock 01 was missing Konjunktiv I — flag for 02–10.) Words: 350–400. Idiomatic register; no LLM-flat prose. |
| **CR-16 Schreiben theme** | Differs from Lesen T3 theme. Aligns with gate doc Section 4.6 mock-row assignment. |
| **CR-17 Sprechen T1A topics** | 2 abstract thesis-driven topics, each with 3–5 Stichwortartige Aspekte. NOT narrative. NOT B1/B2 Erfahrungs-based. |
| **CR-18 Sprechen T1B prompt** | Partner role explicit: 2–3 sentence summary + 1 follow-up question (provided as 2–3 examples). |
| **CR-19 Sprechen T2 thesis** | Single quotation/thesis with 2 contrasting Karten (A + B), 4 discussion sub-prompts. Sample response demonstrates dialectical reasoning (concede partner ground + synthesize). |
| **CR-20 Sample-answer authenticity check** | No LLM-generic phrasing. Spot-check for German idiom errors: "überzeuge ich mich von" → "vertrete ich" (mock 01 sample fix). |
| **CR-21 Theme spread per gate doc Section 4.6** | Mocks 02–10 follow the assigned Lesen T3 / Hören T2 / Hören T3 / Schreiben / Sprechen topic mapping. No two sections within one mock share the same long-form topic. |
| **CR-22 Vocabulary scope** | All productive content (SB distractors, sample writing, sample speaking) within C1 active scope (~6,000 working set) + B2 carry-forward. Receptive content (Lesen + Hören texts) may include C2 lexis only when context renders meaning transparent. |
| **CR-23 Idioms allowed** | 1–3 idiomatic Wendungen per Lesen T3 / Schreiben sample (gate doc 2.7 — receptive recognition + sparing production). |
| **CR-24 Schema validation** | Every mock validates against `packages/types/src/exam.ts` MockExam interface. Pre-PR check: `pnpm typecheck`. |

### 6. Decision

**YELLOW — fix P0/P1 then batch.**

**Action plan:**
1. Apply all 6 P0 fixes to `.worktrees/content-c1-mock-01-worked-example/apps/mobile/assets/content/C1/mock_01.json` (5 surgical text edits + 1 sentence rewrite for Lesen T1 Q6).
2. Apply 4 P1 fixes (HV3 type tag rename, Schreiben sample idiom fix, Lesen T1 Q5 antecedent tighten, document HV3-cue training-wheel exception).
3. Re-run pedagogy review on the corrected file (focused 30-min pass — no full re-audit needed).
4. After PR #149 merges with corrections: GREEN-LIGHT batch authoring of mocks 02–10 with the 24 calibration rules above as the binding spec.

P2 items can be tracked in a follow-up issue and addressed during the mocks 02–10 review pass — they do not block anything.

---

## Reviewer Notes (one paragraph)

This is a strong worked example. The substance — Reproducibility crisis + Open Science + KI in research — is genuinely C1 territory and reads like authentic German academic journalism. The dialectical interview register in HV2, the Vortrag pacing in HV3, the contrasting-opinion Schreiben prompts, and the thesis-card Sprechen T2 all model the right C1 patterns. The defects are all surgical — most are typos (statistisches Fingerabdruck, unevenverteil, kurierten) that any proofreader would catch. The two structurally important issues are SB gap 7 (semantically broken) and gap 14+15 (broken Trennverb fusion); both indicate the SB cloze text was authored under time pressure and not re-read against canonical answers. Lesen T1 Q6 cohesion is the only deep-think fix — the discourse logic of "Open Science Antwort. [GAP] Dazu gehören…" demands a sentence that sets up "Dazu", not one that pivots to limits. Given the worked-example role, I'd recommend the implementation lead spend a focused 90-minute fix pass before this mock ships.

— pedagogy-director
