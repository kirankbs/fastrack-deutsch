# B1 Grammar Audit vs. Hueber Modelltests (15 mocks)

> Audited: 2026-05-01 | Source: `apps/mobile/src/data/grammar/B1_grammar.json` (21 topics) vs. `.planning/research/B1-pdf-reference/mock-{01..15}.txt`
> Read-only audit. OCR is imperfect; readings of individual gaps were judgement calls when text was garbled.

---

## 1. Current state — `B1_grammar.json` topic list

21 topics, each with a single explanation block (~600–930 chars) and 6–8 exercises. Three carry `[PEDAGOGY-REWRITE]` flags inside the explanation (Konjunktiv II, Passiv, Plusquamperfekt) plus inline flags on a handful of exercise rationales.

| # | Topic | Expl chars | Ex | Flag |
|--|--|--:|--:|--|
| 1 | Konjunktiv II — würde-Form, hätte und wäre | 616 | 6 | REWRITE |
| 2 | Passiv — Vorgangs- / Zustandspassiv | 617 | 6 | REWRITE |
| 3 | Relativsätze — der/die/das in allen Kasus | 633 | 6 | |
| 4 | Konnektoren — weil, da, denn, obwohl, trotzdem | 767 | 6 | |
| 5 | Temporale Nebensätze — wenn/als/nachdem/bevor/während | 676 | 6 | |
| 6 | Finale Nebensätze — damit / um…zu | 684 | 6 | |
| 7 | Wechselpräpositionen + feste Präpositionen (Dat/Akk/Gen) | 672 | 8 | REWRITE |
| 8 | Reflexive Verben mit Präpositionen | 788 | 6 | |
| 9 | Modalverben im Perfekt / Vergangenheit | 739 | 6 | |
| 10 | Futur I — Zukunft / Vermutung | 677 | 6 | |
| 11 | Infinitiv mit und ohne zu | 753 | 6 | |
| 12 | Adjektivdeklination — alle Artikel, alle Kasus | 740 | 7 | |
| 13 | Indirekte Rede — Konjunktiv I (Grundlagen) | 755 | 6 | |
| 14 | Komparativ und Superlativ — Sonderformen | 781 | 6 | |
| 15 | Pronomen — Personal/Possessiv/Demonstrativ/Indefinit | 898 | 7 | |
| 16 | Verben mit festen Präpositionen | 814 | 6 | |
| 17 | Nominalisierung und n-Deklination | 924 | 6 | |
| 18 | Partizip I und II als Adjektiv | 893 | 6 | |
| 19 | Trennbare und untrennbare Verben | 877 | 6 | |
| 20 | Je…desto und andere Vergleichskonstruktionen | 869 | 6 | |
| 21 | Plusquamperfekt — hatte/war + Partizip II | 730 | 6 | REWRITE |

Coverage shape: explanations are dense single paragraphs (650–900 chars). Median exercises = 6. No topic exceeds 8.

---

## 2. Hueber Sprachbausteine frequency table (15 mocks × ~20 gaps)

Each mock has Teil 1 (10 grammar MCQ) + Teil 2 (10 word-bank, mostly lexical but several grammar-driven). I coded ~300 gaps across mocks 01–15, classifying each by primary phenomenon. Counts are approximate; many gaps test 2 things (e.g., relative pronoun + case = both buckets).

| Phenomenon | Gaps | Mocks | Sample evidence |
|---|---:|---:|---|
| Prepositions + case (incl. Wechselprep.) | ~58 | 15/15 | Every mock tests `an/auf/in/zu/bei/mit/nach/seit/vor/durch/für/um` + dat/acc choice. Genitiv (`wegen, trotz, statt, während`) 1–2×/mock. |
| Articles + case endings (def./indef./poss.) | ~38 | 15/15 | dem/den/der/des; M5 g30, M2 g23 (`des Jahres`), M9 g25 (`statt des Mofas`). |
| Conjunctions + word order | ~34 | 15/15 | `denn` vs `weil` vs `da` (M3 g21); `damit` vs `um…zu` (M1 g22, M6 g30); `sondern/aber/oder/sonst`. |
| Verb forms — Perfekt/Präteritum/Plusqu. | ~28 | 15/15 | haben/sein (M1 g28); `geworden/worden` (M11 g23); modal Prät. (M6 g25 `musste/müsste`); doppelter Inf. (M2 g27). |
| Konjunktiv II (würde/hätte/wäre/könnte) | ~22 | 13/15 | M1 g24, M5 g29, M9 g28 `gäbe`, M11 g23, M14 g30. |
| Pronouns — personal/reflexive/indef./demonstr. | ~24 | 14/15 | `mich/mir/sich/uns` (M1.30, M2.22, M9.23); `man → einen`; `niemanden` rare. |
| Relative pronouns | ~14 | 11/15 | Dat. Pl. `denen` (M1 g29); Gen. `des` (M9 g25); M15 g29. |
| Adjective endings (declension) | ~12 | 9/15 | `mehrere/meisten/vielen` (M7 g26); `dieses/jenem` (M6 g23). Typically 1 dedicated gap/mock. |
| Comparative/superlative + `als/wie` | ~10 | 9/15 | `lange/länger/lang` (M2 g26); `als/wie` (M11 g26, M7 g21); `am liebsten` (M12 g26); `höchstens` (M11 g25). |
| Negation — `nicht/kein/nichts/niemand/weder…noch` | ~9 | 8/15 | `kein/kaum/nichts` (M10.25, M9.30, M3.28); `weder…noch` (M13 g24, M4 g28). |
| Infinitiv + zu (um…zu, ohne zu, statt zu) | ~9 | 8/15 | `aufpassen/aufzupassen` (M1 g27, M2 g33); `mitbringen/mitzubringen` (M10 g30); `ohne zu/statt zu` (M13 g30). |
| Verben + feste Präpositionen | ~8 | 6/15 | `freuen auf` (M7 g29); `interessieren für` (M3 g0); `sich erinnern an` (M2 g21). |
| Imperativ | ~5 | 5/15 | `Komm/Kommst du/Kommt` (M11 g29); `Wünsch dir` (M12 g30); `Vergiss/Vergessen Sie/Vergesst` (M10 g28). |
| Passiv (Vorgangs- + Zustand-) | ~6 | 5/15 | `wurden/haben/sind` (M2 g24); `worden/wurden/geworden` (M11 g23); `operiert werden musste` (M8 g24). |
| Pronominaladverbien `dafür/darauf/daran/dazu` | ~5 | 5/15 | M3 g26 `Daran/Darüber/Danach`; M14 g28; M7 g29. |
| Indirekte Rede — Konj. I | ~3 | 3/15 | M5 g26 `seien`; M3 g29 `sei`; M15 g26 `wisse`. Recognition only. |
| Trennbare Verben split | ~4 | 4/15 | `passen auf/aufpassen/aufzupassen` (M1.27, M10.30). |
| Plusquamperfekt | ~2 | 2/15 | M1 g24, M5 g24. Less frequent than expected. |
| `ob` / indirect question | ~3 | 3/15 | M2 g39, M4 g29, M11 g38. |
| Demonstrative `dieser/jener` | ~2 | 2/15 | M6 g23 `keinem/diesem/jenem`. |

Cumulative cloze gaps that test grammar (Teil 1 = 150 across 15 mocks; Teil 2 contains another ~50–60 grammar items mixed with lexical). Hueber's distribution matches the heylama list closely.

**Beyond the heylama 10:** Pronominaladverbien (`darauf/daran/dafür`) — Hueber treats as a distinct distractor cluster; Imperative (du/ihr/Sie forms) — present every other mock; `als/wie` after Komparativ — Hueber tests as its own pattern.

---

## 3. Gap list — missing or under-covered in `B1_grammar.json`

| Gap | Hueber freq | Current coverage | Severity |
|---|---|---|---|
| **Imperative — du/ihr/Sie + irregular stems** | 5/15 mocks (always 3-way distractor: `Komm/Kommst/Kommt`) | NOT covered as a topic. Touched briefly inside other entries. | High — easy points lost on a recurring item. |
| **Pronominaladverbien (`darauf/daran/wofür/woran`)** | 5/15 mocks; also feeds `freuen auf → darauf` | Partially in topic 16 (Verben + fest. Präp.) — 1 sentence about `wo(r)+Prep` pattern. No paradigm table, no dedicated exercises. | High. |
| **`als / wie` after Komparativ; `so…wie / nicht so…wie`** | 9/15 mocks | Inside topic 14 but only 2 of 6 exercises target the trap directly. | Medium — needs more drill items, not new topic. |
| **Negation system — `nicht` vs `kein` vs `nichts/niemand` placement** | 8/15 mocks | NOT a standalone topic. Appears piecewise inside pronouns and various explanations. | High — heylama lists this as a top-10 phenomenon and Hueber confirms it. |
| **`ob` and indirect questions** | 3/15 mocks; also blends into Konj. I in topic 13 | One brief mention inside Indirekte Rede, no `ob` vs `dass` vs `wenn` distractor drill. | Medium. |
| **Imperfekt der Modalverben in cloze (`musste/müsste/muss`)** | 5/15 mocks (M6 gap 25, M9 gap 26, M3 gap 30, M12 gap 23, M14 gap 24) | Topic 9 covers Perfekt + Doppelter Infinitiv but spends very little space on the present-vs-Präteritum-vs-Konj. II distractor cluster that Hueber loves. | Medium-high — current explanation focuses on doppelter Infinitiv (rare in cloze) at the expense of the high-frequency drill. |
| **Pronominal genitive constructions (`statt des Mofas`, `wegen des Wetters`, `während meines Aufenthalts`)** | ~5–6 grammar gaps across mocks | Inside topic 7 — well explained but only 2 exercises actually drill Genitiv after preposition. | Medium. |
| **Particle/Modaladverb inventory (`zwar…aber`, `sowohl…als auch`, `weder…noch`, `entweder…oder`, `nicht nur…sondern auch`)** | 6+ gaps (M2 gap 30, M3 gap 22, M4 gap 27 `Entweder/Weder/Sowohl`, M6 gap 28–29, M9 gap 35, M13 gap 24) | NOT a topic. Hueber treats this as a distinct grammar cluster in distractors. | High — would be its own entry. |
| **Pronouns `man → einem/einen` and `jemand/niemand` declination** | 3 gaps | Inside topic 15 but compressed into one sentence. | Low-medium. |
| **`ohne zu` / `(an)statt zu` / `ohne dass` / `anstatt dass`** | 2 gaps (M13 gap 30) | Inside topic 11 + topic 20 but split. | Low. |

---

## 4. Over-coverage — likely B2 leak or low-value at B1

| Topic | Why questionable for B1 |
|---|---|
| **17. Nominalisierung und n-Deklination** | Hueber n-Deklination shows up exactly **0 times** in my sweep of 15 mocks. The Goethe/telc B1 research file flags it as "rare but appears" — empirical Hueber data says it does not appear at all in cloze. Nominalisierung itself is a B2 productive skill, not a B1 testable phenomenon. **Recommend demoting** to a 2-paragraph appendix or moving entirely to B2. |
| **18. Partizip I und II als Adjektiv** | I found zero Hueber cloze gaps targeting attributive Partizip I (`das lachende Kind`). Partizip II as adjective shows up only inside larger Passiv distractors. The "Partizipialkonstruktion" example in the explanation (`Der im Garten spielende Hund…`) is squarely B2/C1. **Recommend trimming** to 1 paragraph + retire the productive examples; rebuild topic around Partizip II's role inside Perfekt/Passiv (which Hueber does test). |
| **13. Indirekte Rede — Konjunktiv I** | Only 3/15 Hueber mocks contain a Konj. I gap, and they target *recognition* (`sei/habe/wisse`) not production. The current explanation pushes toward production (full paradigm of `wachsen → wachse`). **Recommend trimming to recognition-only**, keep 2 exercises max. |
| **20. Je…desto — depth** | Only 2 marginal Hueber hits across 15 mocks. Topic also carries `als ob`, `anstatt dass`, `ohne dass` — which is too much for one bucket. **Recommend splitting**: keep `je…desto` short, fold `als ob` into Konjunktiv II, fold `anstatt zu / ohne zu` into Infinitiv mit zu. |
| **10. Futur I** | 1 gap across 15 mocks (M1 gap 28 `werde/habe/bin` for `geärgert`, where Futur I is actually wrong). Futur I in B1 cloze barely exists — the Vermutung use is more a reading skill. **Recommend trimming** to ½ length. |

Net: roughly 4 topics are bigger than they need to be. That space could fund the 4–5 new topics below.

---

## 5. Depth recommendations — topics needing more thorough treatment

| Topic | Current | Recommended |
|---|---|---|
| **Konnektoren (#4)** | 6 exercises; covers weil/da/denn/obwohl/trotzdem/damit | Hueber tests `denn/sondern/aber/oder` 4× per mock as Hauptsatz coordinators. **Bump to 12 exercises**, separate sub-blocks: (a) subord. Verb-final, (b) coord. position-0, (c) adverbial inversion. Adds ~300 chars of explanation. |
| **Wechselpräpositionen + feste Präp. (#7)** | 8 ex; `[REWRITE]` flagged | This is the single highest-frequency Hueber bucket (~58 gaps). **Bump to 14–16 exercises** split: 2-way prep dat/acc trap, fixed dative preps (mit/zu/bei/von/aus/nach/seit), fixed accusative (durch/für/gegen/ohne/um), Genitiv preps. Rewrite explanation into 3 short paragraphs instead of one wall. |
| **Pronouns (#15)** | 7 ex covering 4 pronoun types | Split into TWO topics: (a) personal + reflexive (Akk/Dat), (b) demonstrative + indefinite + `man → einem/einen`. Add a third small topic for **Pronominaladverbien** (`darauf/daran/wofür/woran`). |
| **Konjunktiv II (#1)** | 6 ex; `[REWRITE]` flagged | Hueber gives ~22 gaps. Bump to 10 ex. Add (a) `wäre/hätte/könnte` recognition in cloze, (b) polite request `Könnten Sie / Hätten Sie / Würden Sie`, (c) irrealer Bedingungssatz, (d) `als ob + Konj. II`. |
| **Passiv (#2)** | 6 ex; `[REWRITE]` flagged | Hueber tests `wurde/wird/worden` 5–6 times. Bump to 10 ex. Add Modalverb + Passiv (`muss gemacht werden`, M8 gap 24 type) and Passiv im Perfekt with `worden`. |
| **Adjektivdeklination (#12)** | 7 ex covering all three patterns | Hueber gaps usually present 3 declined-form options (`mehrere/meisten/vielen`). Bump to 10 ex with Hueber-style 3-way endings drills. |
| **Modalverben Vergangenheit (#9)** | 6 ex; `[PEDAGOGY-REWRITE]` flagged | De-emphasise doppelter Infinitiv (rare). Add 4 ex on Präteritum modals in cloze (`konnte/könnte/kann`, `musste/müsste/muss`) — that's where Hueber actually trips candidates. |

---

## 6. Priority actions for impl-lead — top 10 to add or upgrade

Numbered by ROI (Hueber-frequency × gap-severity × ease-of-authoring).

1. **NEW topic: Negation — `nicht` vs `kein` vs `nichts/niemand/nie/kaum`** with placement rules. ~700 chars explanation, 8 exercises drawn from Hueber-style 3-way distractor sets (M3 gap 28, M9 gap 30, M10 gap 25, M11 gap 30).
2. **NEW topic: Zweiteilige Konnektoren — `zwar…aber, sowohl…als auch, weder…noch, entweder…oder, nicht nur…sondern auch, je…desto`**. ~700 chars, 8 exercises. Hueber tests this in 6+ gaps; currently invisible.
3. **NEW topic: Imperativ — du/ihr/Sie + irregular stems (`gib, nimm, iss, sieh, lies`) and trennbare Verben (`Steh auf!`)**. ~500 chars, 6 ex. Always a 3-form Hueber gap (`Komm/Kommst/Kommt`, `Vergiss/Vergessen/Vergesst`).
4. **NEW topic: Pronominaladverbien (`darauf, daran, dafür, davon, dazu, worüber, woran, wofür`)** — both their formation rule and their use after fest. Präp.-Verben. ~600 chars, 8 ex. Pulls work out of topic 16.
5. **UPGRADE topic 7 (Präpositionen)** — split into (a) Wechselpräpositionen, (b) fixed-case preps, (c) Genitivpräpositionen. Triple the exercise count to 16. Highest-frequency Hueber bucket; deserves the deepest drill module.
6. **UPGRADE topic 4 (Konnektoren)** — bump to 12 ex with explicit sub-blocks for subord./coord./adverbial. Add `denn` vs `weil` vs `da`, `sondern` vs `aber`, `trotzdem` vs `obwohl` — the exact Hueber distractor traps.
7. **UPGRADE topic 9 (Modalverben Vergangenheit)** — rebalance away from doppelter Infinitiv toward Präteritum-vs-Konj.-II (`musste/müsste/muss`, `konnte/könnte/kann`). 4 new exercises minimum.
8. **UPGRADE topic 1 (Konjunktiv II)** — bump from 6 → 10 ex; add `als ob + Konj. II` (currently buried in topic 20), polite-request set, irrealer Bedingungssatz with `wäre`. Resolve the `[PEDAGOGY-REWRITE]` flag.
9. **UPGRADE topic 2 (Passiv)** — add Modalverb-Passiv (`muss gemacht werden`) and Perfekt-Passiv with `worden` (specifically the `worden` vs `geworden` trap). Resolve flag.
10. **DEMOTE topic 17 (Nominalisierung + n-Deklination)** — split: drop Nominalisierung entirely (B2), keep n-Deklination as a 1-paragraph note inside topic 12 (Adjektivdeklination) or topic 15 (Pronouns). Frees ~1000 chars and 6 ex slots that funded #1 above.

After actions 1–10: topic count 21 → ~22 (3 new, 1 demoted, 1 split). Exercise count ~130 → ~180. All three `[PEDAGOGY-REWRITE]` flags resolved. Coverage tracks Hueber's distractor distribution.

---

## Methodology

Sampled all 15 mocks' Sprachbausteine sections via OCR dumps. OCR garbled option markers (`[A]` often prints as `|A|`); option content was recoverable from context. Frequency = gap-level; `Hits / 15 mocks` = mocks where the phenomenon was primary in at least one gap. Multi-phenomenon gaps were double-counted (totals exceed 300 cumulative). The Hueber book (2002-era) predates the current telc spec but matches the heylama "11 grammar patterns" list on ~9 of 10 buckets.
