# Handoff — #232 — B1 vocab combined batches B1-B10

## What was built

Applied all 10 B1 vocab upgrade priority actions from the Hueber audit in a single PR. Net result: 2630 → 2739 entries (+109).

## Net delta per batch

| Batch | Topic | Adds | Deletes | Net |
|-------|-------|------|---------|-----|
| B1 | Kommunikation und Sprache | 22 | 0 | +22 |
| B2 | Verben Grundwortschatz | 21 | 0 | +21 |
| B3 | Beziehungen und Familie | 21 | 0 | +21 |
| B4 | Politik und Gesellschaft | 10 | 13 | -3 |
| B5 | Wirtschaft / Konsum | 8 | 7 | +1 |
| B6 | Wohnen | 8 | 4 | +4 |
| B7 | Medien und Technik | 18 | 0 | +18 |
| B8 | Charaktereigenschaften (adj layer) | 4 | 8 | -4 |
| B9 | Veranstaltungen / Freizeit | 10 | 0 | +10 |
| B10 | Adverbien und Zahlen | 19 | 0 | +19 |
| **Total** | | **141** | **32** | **+109** |

56 add candidates were already present and silently skipped. 32 deleted entries archived to `.planning/B1-vocab-graveyard-2026-05-03.md`.

## Files changed

- `apps/mobile/src/data/vocabulary/B1_vocabulary.json` — 2630 → 2739 entries; 32 B2-leak/bureaucratic-register deletes, 141 adds across 10 topic clusters
- `apps/web/src/__tests__/vocab/loadVocabulary.test.ts` — updated hardcoded count assertion from 2630 to 2739
- `.planning/B1-vocab-graveyard-2026-05-03.md` — new; all 32 removed entries with german + english fields, organised by batch

## Tests

- Unit: 1 test updated (count assertion), 41 web test files all passing
- E2E: CI green (E2E Tests pass)
- Typecheck: clean

## Quality gates

- compliance: n/a
- language: n/a
- spec-tracker: n/a
