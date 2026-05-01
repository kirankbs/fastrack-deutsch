# B1 Content Upgrade Plan — Anchored on Hueber 15 Modelltests

> Date: 2026-05-01 · Author: orchestrator · Status: ready for `/deep-work` dispatch
>
> **Reference standard:** Hueber Verlag, *Zertifikat Deutsch — 15 Übungsprüfungen* (2010, 250 pp). Treated as gold-standard for telc B1 register, distractor design, topic distribution, and prompt diversity.

---

## 0. Executive summary

Goal: lift our B1 content (10 mocks, 2,630 vocab entries, 21 grammar topics) to the rigour of the Hueber book, **closely following its format** while paraphrasing all material (no verbatim copy — copyright safe).

Four parallel workstreams:

- **WS-A — Mocks.** Rewrite mocks 01–10 to fix register monoculture / templated stems / topic clustering. Add mocks 11–15 modelled on Hueber 11–15.
- **WS-B — Vocab.** 10 batches: gap-fill core verbs + discourse vocab + topic rebalance + B2-leak prune. Net delta ≈ +50…+100 entries (target ~2,700).
- **WS-C — Grammar.** 4 new topics (Negation, Zweiteilige Konnektoren, Imperativ, Pronominaladverbien). 5 topic upgrades. 1 B2 demotion. Resolve all 3 `[PEDAGOGY-REWRITE]` flags.
- **WS-D — Cross-cutting.** Catalog/registry sync, audio prompts (SSML) for any new mocks, content-roadmap update, language-checker pass.

Total: ~25–30 GitHub issues, ~6–8 PR waves, gated end-to-end by pedagogy-director + exam-tester.

---

## 1. Source artifacts

All audits and reference dumps live in `.planning/`:

| File | Purpose |
|---|---|
| `.planning/research/B1-pdf-reference/mock-01.txt` … `mock-15.txt` | OCR'd Hueber mocks — ~24 KB each, used as authoring reference (paraphrase only) |
| `.planning/research/B1-pdf-reference/transkriptionen-loesungen.txt` | Hueber listening scripts + answer keys (130 KB) |
| `.planning/research/B1-Hueber-15-mocks-inventory-2026-05-01.md` | Per-mock matrix (15×14) + cross-mock patterns (distractor types, stylistic markers, topic dist.) |
| `.planning/research/B1-exam-format.md` | Pre-existing telc B1 spec — confirmed accurate |
| `.planning/reports/B1-existing-mock-audit-2026-05-01.md` | Audit of our 10 mocks — structure perfect, register monoculture |
| `.planning/reports/B1-vocab-audit-vs-Hueber-2026-05-01.md` | Vocab gap analysis — 50% miss rate, 25 B2 leak |
| `.planning/reports/B1-grammar-audit-vs-Hueber-2026-05-01.md` | Grammar gap analysis — 4 missing topics, 3 PEDAGOGY-REWRITE flags |
| `.planning/reports/B1-pedagogy-audit-2026-04-27.md` | Prior pedagogy review (still valid, complements above) |

**Copyright guard:** No verbatim Hueber phrases. All paraphrase/inspired-by. Topics, distractor types, and prompt-diversity patterns are general telc-format properties, not copyrightable expression.

---

## 2. WS-A — Mocks (10 rewrites + 5 new)

### A1. Cross-cutting fixes for mocks 01–10 (one PR per mock)

Each existing mock keeps its ID and overall theme but gets surgically rewritten on these axes (drawn from existing-mock audit + Hueber inventory):

1. **Sprachbausteine register split.** Per Hueber norm: SB1 (cloze) and SB2 (word-bank) must alternate or differ. Ten SB pairs currently all `Liebe X / du`. Target distribution across 10 mocks:
   - 4 mocks: SB1 `du`-form private + SB2 `Sie`-form formal (inquiry/complaint) — Hueber default
   - 3 mocks: SB1 `Sie`-form formal + SB2 `du`-form private — inverse
   - 3 mocks: both formal (work emails / institutional inquiry) — Hueber rare but present (e.g. M07/M14)
2. **Schreiben prompt diversification.** All 10 are currently semi-informal letters. Rewrite distribution to mirror Hueber:
   - 6 mocks: private letter / penpal reply (canonical Hueber default — 10 of 15 in PDF)
   - 2 mocks: semi-formal inquiry (Sprachschule, Reisebüro, Kursanmeldung)
   - 1 mock: formal complaint (Beschwerde — defective product / hotel / service)
   - 1 mock: arrangement-change letter (terminverschiebung, absagen)
3. **Listening Teil 3 question stems.** Replace the templated `Worauf einigen sich…` / `Was empfiehlt…` / `Was ist das größte Problem…` triplet that recurs in 10/10 mocks. Target: each mock has its own stem set drawn from Hueber's actual stem repertoire (`Wieso glaubt X dass…`, `Was schlägt X vor…`, `Was hat X letzte Woche gemacht…`, etc.).
4. **Sprechen Teil 3 archetype variation.** Currently 5/10 are party/festival. Reset to mirror Hueber dist:
   - 4 party / Geburtstag / Klassenfest
   - 3 trip / Ausflug / Reise organisieren
   - 1 gift planning (group present)
   - 1 community event (Quartiersfest / Vereinsfeier)
   - 1 study-abroad or Stadtbummel planning
5. **Reading Teil 3 ad-cluster theme uniqueness.** Currently Reparatur / Second-Hand / Mitfahrgelegenheit appear in ≥4 of 10. Each mock should own one cluster:
   - M01: travel + accommodation
   - M02: jobs + Praktika
   - M03: courses + Bildung
   - M04: vehicles + transport
   - M05: housing rentals
   - M06: events + Kultur
   - M07: services (Reparatur / Reinigung / Pflege)
   - M08: secondhand + Tausch
   - M09: pets + Haustier-Service
   - M10: weddings + Feiern
6. **Distractor sophistication.** From Hueber inventory §Distractor design — 9 trap types (numerical near-miss, subject-swap, generalisation, causal reversal, time-frame, false-inference, lexical false-friends, voice/mood swap, preposition micro-traps). Each rewritten mock must demonstrate ≥6 of the 9 types across its 5 reading T2 MCQs and 5 listening T3 MCQs.
7. **Idiom budget.** Hueber lands ~1–2 idioms per mock. Currently we have ≤1 in some mocks, idiom-clusters in others. Set hard target: 1–2 per mock, no more.
8. **Era audit.** Hueber is 2002 — we modernise (no DM prices, no Walkman). Modern themes ALLOWED at parity (Klima, Streaming, Migration) — Hueber lacks these but they're standard B1 register today.

### A2. New mocks 11–15

Five new mocks modelled on Hueber 11–15 (paraphrased):

| Our # | Working title | Lead theme | Distinctive feature |
|---|---|---|---|
| M11 | Arbeit und Karriere | jobs, Bewerbung, Praktikum | reading T2 = profile of a quereinsteiger; SB1 formal Bewerbungsschreiben |
| M12 | Gesundheit und Lebensstil | sport, Ernährung, Schlaf | listening T2 = radio interview with a Ernährungsberaterin; speaking T3 = group fitness plan |
| M13 | Reisen und Mobilität | travel, public transport, env. | reading T3 = travel ads cluster; writing prompt = travel-agency complaint |
| M14 | Familie und Generationen | family relations, ageing | listening T3 = grandparent ↔ teen dialogue; speaking T2 = family-time chart |
| M15 | Medien und digitales Leben | social media, Smartphone | SB1 = formal inquiry to streaming service; speaking T3 = plan a Lese-/Filmclub |

Each follows full canonical 5/5/10 + 10/10 + 5/10/5 + 1 + 3 structure. Each gets per-PR audio prompts (`.planning/audio-prompts/B1_mock_NN_*.ssml`). Each gets a `B1_mock_NN.json` in `apps/mobile/assets/content/B1/`.

### A3. Quality gates per mock PR

Mandatory chain before merge (subagent self-dispatch allowed):

1. `language-checker` — Goethe B1 Wortliste compliance, German accuracy, English UI text consistency.
2. `pedagogy-director` — 6-dimension review; gated rewrite authority; tags `[PEDAGOGY-REWRITE]` if needed.
3. `exam-tester` — Layer A 10-check structural (5/10/5 listening, 10+10 SB, 5/5/10 reading, 130–170 word writing, audio refs valid) **then** Layer B Jest run.
4. `audio-designer` — only for new mocks 11–15: SSML scripts + voice assignment.

PRs are sized per-mock (one mock = one PR). Cap parallel waves at 3 concurrent impl-lead dispatches per CLAUDE.md rate-limit rule.

---

## 3. WS-B — Vocab (10 batches, ≈+50…+100 net)

Drive from `.planning/reports/B1-vocab-audit-vs-Hueber-2026-05-01.md` §5 verbatim. Each batch = one PR. Order:

| # | Batch | Action | Net Δ |
|---|---|---|---|
| B1 | Test-meta + discourse vocab | ADD ~30 | +30 |
| B2 | Core verbs as headwords | ADD ~25 | +25 |
| B3 | Beziehungen und Familie | ADD ~30 | +30 |
| B4 | Politik trim + rebalance | DEL 13 / ADD 13 | 0 |
| B5 | Wirtschaft trim + consumer pivot | DEL 9 / ADD 13 | +4 |
| B6 | Wohnen trim + housing pivot | DEL 5 / ADD 6 | +1 |
| B7 | Medien und Technik (everyday-tech) | ADD ~25 | +25 |
| B8 | Charaktereigenschaften adjective layer | DEL 8–10 nouns / ADD ~12 adj | +4 |
| B9 | Veranstaltungen / leisure | ADD ~20 | +20 |
| B10 | Numerals + adverbs of time/quantity | ADD ~20 | +20 |

Hard rules:

- All deletes must be cross-checked against B1 mock JSON usage. If a mock currently uses a B2-leak word, the deletion is blocked until the mock is rewritten. (Sequencing: WS-A waves precede or interleave with WS-B 4–6.)
- Above-level deletes go to `.planning/B1-vocab-graveyard-2026-05-01.md` (not promoted to B2 list yet — separate decision).
- Each new entry needs: `german`, `english`, `exampleSentence`, `topic`, `article` (for nouns), `plural` (for nouns), and SR fields initialised at zero.
- Pedagogy-director gate before merge.

---

## 4. WS-C — Grammar (21 → ~22 topics, 130 → ~180 exercises)

Drive from `.planning/reports/B1-grammar-audit-vs-Hueber-2026-05-01.md` §6 verbatim.

### C1. New topics (4 PRs)

| # | New topic | Length | Exercises | Hueber freq |
|---|---|---|---|---|
| G1 | Negation — `nicht` vs `kein` vs `nichts/niemand/nie/kaum` | ~700 chars | 8 | 8/15 mocks |
| G2 | Zweiteilige Konnektoren | ~700 chars | 8 | 6/15 mocks |
| G3 | Imperativ (du/ihr/Sie + trennbare + irregular) | ~500 chars | 6 | 5/15 mocks |
| G4 | Pronominaladverbien (`darauf/davon/woran/wofür`) | ~600 chars | 8 | 5/15 mocks |

### C2. Topic upgrades (5 PRs)

| # | Topic | Action | New ex count |
|---|---|---|---|
| G5 | T7 Präpositionen | Split into Wechselpräp / fixed-case / Genitivpräp; expand examples | 16 (was ~6) |
| G6 | T4 Konnektoren | Add denn/weil/da, sondern/aber, trotzdem/obwohl distractor pairs | 12 |
| G7 | T9 Modalverben Vergangenheit | Rebalance Präteritum-vs-Konj.II | +4 ex |
| G8 | T1 Konjunktiv II | Resolve PEDAGOGY-REWRITE; add als ob, polite request, wäre-Bedingungssatz | 10 (was 6) |
| G9 | T2 Passiv | Resolve PEDAGOGY-REWRITE; add Modalverb-Passiv + worden vs geworden | +3 ex |

### C3. Demotion (1 PR)

- **G10:** T17 Nominalisierung + n-Deklination → drop Nominalisierung entirely (B2 territory), keep n-Dekl. as a single paragraph inside T12 (Adjektivdeklination). Reclaim ~1000 chars and 6 exercise slots — those slots funded G1 above.

### C4. Quality gates

- Pedagogy-director must approve each new topic / upgrade before merge.
- exam-tester runs Layer B Jest tests after each grammar JSON change (catches schema regressions).
- All `[PEDAGOGY-REWRITE]` flags must be cleared by end of WS-C.

---

## 5. WS-D — Cross-cutting

### D1. Catalog and registry

- `packages/content/src/catalog.ts` titles array for B1 must reflect the 5 new mocks 11–15. Per CLAUDE.md merge-hygiene rule: every B1-touching mock PR rewrites the **entire B1 titles array** to its convergent end-state.
- Mock count guard in tests must move from 10 → 15.

### D2. Audio assets

- Mocks 11–15 need SSML scripts in `.planning/audio-prompts/B1_mock_{11..15}_*.ssml` (5 files per mock × 5 mocks = 25 SSML files).
- Mocks 01–10 audio is reusable IF the rewrite preserves listening transcripts verbatim. Plan: minimise listening-script changes during rewrites unless register fixes require it. Where a script must change, regenerate audio.

### D3. Content roadmap

- Update `.planning/content-roadmap.md` to reflect: 15 B1 mocks, vocab Δ +75, grammar 22 topics, all PEDAGOGY-REWRITE flags clear.

### D4. Language-checker sweep

After all WS-A + WS-B + WS-C waves merge, run a final `language-checker` pass across all B1 JSON to catch any introduced register drift or English-side inconsistency.

---

## 6. Sequencing and dependencies

```
Wave 1 (parallel, 3 PRs)
├── WS-A.M01 rewrite
├── WS-A.M02 rewrite
└── WS-C.G1  Negation (new topic)

Wave 2 (parallel, 3 PRs)
├── WS-A.M03 rewrite
├── WS-A.M04 rewrite
└── WS-C.G2  Zweiteilige Konnektoren

Wave 3 (parallel, 3 PRs)
├── WS-A.M05 rewrite
├── WS-A.M06 rewrite
└── WS-C.G3  Imperativ

Wave 4 (parallel, 3 PRs)
├── WS-A.M07 rewrite
├── WS-A.M08 rewrite
└── WS-C.G4  Pronominaladverbien

Wave 5 (parallel, 3 PRs)
├── WS-A.M09 rewrite
├── WS-A.M10 rewrite
└── WS-C.G5  Präpositionen split (highest-freq upgrade)

Wave 6 (parallel, 3 PRs)
├── WS-A.M11 NEW
├── WS-A.M12 NEW
└── WS-C.G6  Konnektoren upgrade

Wave 7 (parallel, 3 PRs)
├── WS-A.M13 NEW
├── WS-A.M14 NEW
└── WS-C.G7+G8+G9+G10 (single PR — grammar finalisation)

Wave 8 (parallel, 3 PRs)
├── WS-A.M15 NEW
├── WS-B.B1+B2  (test-meta + core verbs combined)
└── WS-D.audio  SSML for M11–15

Wave 9 (parallel, 3 PRs)
├── WS-B.B3+B4
├── WS-B.B5+B6
└── WS-B.B7+B8

Wave 10 (parallel, 2 PRs)
├── WS-B.B9+B10
└── WS-D.catalog + content-roadmap + language-checker sweep
```

Total: 10 waves × ~2 hours each, with rate-limit budget margins.

---

## 7. Quality gate matrix

| Workstream | language-checker | pedagogy-director | exam-tester | audio-designer | spec-tracker |
|---|---|---|---|---|---|
| WS-A.01–10 rewrite | ✓ | ✓ (gated rewrite) | ✓ Layer A+B | optional (only if listening script changes) | ✓ |
| WS-A.11–15 new | ✓ | ✓ (gated rewrite) | ✓ Layer A+B | ✓ (mandatory) | ✓ |
| WS-B vocab | ✓ | ✓ | tests must pass | — | optional |
| WS-C grammar | ✓ | ✓ | tests must pass | — | optional |
| WS-D | ✓ (sweep) | optional | ✓ | ✓ | ✓ |

`compliance-guardian` runs on every PR via existing project hook — not listed per-row.

---

## 8. /deep-work dispatch contract

Hand-off to `/deep-work` skill with this plan as the master prompt. Deep-work to:

1. Open one tracking GitHub issue per workstream (4 issues — `B1-upgrade/mocks`, `B1-upgrade/vocab`, `B1-upgrade/grammar`, `B1-upgrade/cross-cutting`).
2. Open child issues per PR (~25–30 children).
3. For each PR: dispatch product-owner first (write AC), then implementation-lead with branch name, then quality gates, then merge.
4. Stagger waves max 3 concurrent impl-leads (CLAUDE.md rate-limit rule).
5. Per-mock convergent catalog rewrite (CLAUDE.md merge-hygiene rule).
6. Never write to `.planning/ACTIVITY-LOG.md` from feature branches.
7. Each merged PR drops a date-stamped handoff into `.planning/handoffs/`.
8. After Wave 10 merges, deep-work runs final `compliance-guardian` + `language-checker` sweep, posts a single completion summary referencing all 4 audit reports.

Stop conditions:

- Hard stop: any PR fails Layer A exam-tester check 3× — escalate, ask the user.
- Soft pause: rate-limit exhaustion mid-wave — wait, retry next wave.
- User interrupt at any time — the orchestrator can resume from the last completed wave by re-reading this plan + the handoff log.

---

## 9. Open questions for user

These are items the orchestrator should confirm BEFORE dispatching deep-work, but each has a default the orchestrator will use if no answer:

1. **Audio regeneration policy for mocks 01–10 rewrite.** Default: minimise script changes; only regenerate where register fix forces a change. Alternative: full re-author all audio for consistency across mocks.
2. **Above-level deletes in vocab — promote to B2 list?** Default: park in `.planning/B1-vocab-graveyard.md` for separate decision; do NOT auto-promote.
3. **Mock-content modernisation level.** Default: modern themes allowed (Klima, Streaming, Migration) at parity with traditional themes; era-2002 vocabulary actively avoided.
4. **Branch-name convention.** Default: `b1-upgrade/<workstream>-<short-id>` (e.g. `b1-upgrade/mock-03-rewrite`, `b1-upgrade/vocab-batch-01`).

If the user has no overrides, deep-work proceeds with the defaults above.

---

## 10. Success criteria (Definition of Done)

- 15 B1 mock JSONs in `apps/mobile/assets/content/B1/`, all passing exam-tester Layer A + B.
- B1_vocabulary.json: ~2,700 entries, 0 entries flagged as B2-leak by language-checker, all 18 topics within ±15% of target distribution.
- B1_grammar.json: 22 topics, 0 `[PEDAGOGY-REWRITE]` flags, ~180 exercises total.
- 4 new mocks have full SSML audio in `.planning/audio-prompts/`.
- `packages/content/src/catalog.ts` lists 15 B1 mocks.
- `.planning/content-roadmap.md` updated.
- All 10 waves merged to `main` via PR (no direct pushes).
- One Activity-log entry posted from `main` summarising the upgrade (orchestrator only — never from feature branches).
