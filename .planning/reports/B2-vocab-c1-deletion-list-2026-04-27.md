# B2 Vocab C1 Deletion Proposal — Issue #115

> Author: implementation-lead | Date: 2026-04-27
> Source audit: `.planning/reports/B2-pedagogy-audit-2026-04-27.md` Part C, P1-4
> Status: AWAITING USER SIGN-OFF — do NOT delete without explicit approval
> File: `apps/mobile/src/data/vocabulary/B2_vocabulary.json`

---

## Purpose

The pedagogy audit (P1-4) identified ~150-200 entries above the B2 boundary: research-methodology jargon, evidence-based medicine, software-architecture terminology, management-consulting register, and education-research vocabulary. These are not tested in telc B2 or Goethe B2; their presence miscalibrates the level and distracts learners.

This document lists each candidate with a recommendation. Three possible dispositions:

- **DELETE** — entry is above B2, has no productive use at B2, and its absence won't create a gap
- **DEMOTE-TO-C1** — entry is valid for C1 prep; re-tag `level: "C1"` and move to C1 vocab file rather than deleting
- **KEEP-WITH-TAG** — entry is borderline; adding a note or keeping with a caveat tag is sufficient

**No entries will be removed until the user approves this list.** Reply with your disposition per entry or per category, then open a follow-up PR.

---

## Category 1: Research Methodology

These are standard academic research method terms (Forschungsmethodik). Profile Deutsch places them at C1 under "Wissenschaftliche Kommunikation". A telc B2 candidate has no productive need for them; they appear in this vocab because the content generator conflated "Bildung" (education system) with "Bildungsforschung" (educational research).

| ID | German | English | topic | Recommendation | Rationale |
|----|--------|---------|-------|----------------|-----------|
| 526 | die Forschungsförderung | research funding | Bildung | KEEP-WITH-TAG | Appears in news coverage of science policy — borderline B2 receptive |
| 741 | die Stichprobe | sample | Bildung | DEMOTE-TO-C1 | Research-methodology jargon; not in B2 Wortliste proxies |
| 742 | die Befragung | survey | Bildung | KEEP-WITH-TAG | Appears in Gesellschaft contexts (polling, consumer research) — B2 receptive OK |
| 744 | die Auswertung | analysis | Bildung | KEEP-WITH-TAG | General-register usage (Auswertung eines Tests, einer Umfrage) — acceptable at B2 |
| 745 | die Datenerhebung | data collection | Bildung | DELETE | Methodology jargon; no B2 productive value |
| 746 | die Datenanalyse | data analysis | Bildung | DELETE | Same as above |
| 747 | die Dateninterpretation | data interpretation | Bildung | DELETE | Same as above |
| 750 | die Limitation | limitation | Bildung | DELETE | English academic loanword; Profile Deutsch: C1 Wissenschaftsdiskurs |
| 751 | die Forschungslücke | research gap | Bildung | DELETE | C1 academic register |
| 752 | die Forschungsfrage | research question | Bildung | DELETE | C1 academic register |
| 753 | das Forschungsinteresse | research interest | Bildung | DELETE | C1 academic register |
| 754 | die Anschlussforschung | follow-up research | Bildung | DELETE | Highly specialised; no B2 exam relevance |

Note: id 748 `das Ergebnis` (result), id 749 `die Schlussfolgerung` (conclusion) are general-register B2 — do NOT delete. id 740 `die Fallstudie` (case study) is borderline; appears in Lesen B2 texts — **KEEP-WITH-TAG**.

---

## Category 2: Evidence-Based Medicine (EBM)

These entries are from clinical-medicine methodology. The audit identified them around id 3449-3457. A telc B2 candidate studying for a Gesundheit topic exam needs Prävention, Therapieansatz, psychische Gesundheit — not Doppelblindstudie or Metaanalyse. The latter two are C1 Medizinwissenschaft register.

| ID | German | English | topic | Recommendation | Rationale |
|----|--------|---------|-------|----------------|-----------|
| 3449 | die Therapieleitlinie | treatment guideline | Gesundheit | DEMOTE-TO-C1 | Specialised clinical; occasionally appears in health-journalism B2 texts receptively — C1 is safer |
| 3452 | die Placebo-Kontrolle | placebo control | Gesundheit | DELETE | Clinical trial jargon; not B2 |
| 3453 | die Doppelblindstudie | double-blind study | Gesundheit | DELETE | EBM methodology; Profile Deutsch C1+ |
| 3454 | die Metaanalyse | meta-analysis | Gesundheit | DELETE | Academic-research jargon; C1+ |
| 3455 | die Evidenzstufe | evidence level | Gesundheit | DELETE | Technical medical-research register; not B2 |
| 3456 | die Leitliniengruppe | guideline working group | Gesundheit | DELETE | Institutional health-policy jargon; C1+ |
| 3457 | die Versorgungsforschung | health services research | Gesundheit | DELETE | Academic discipline name; C1+ |

---

## Category 3: Software Architecture Jargon

Entries around id 4004-4008. These were generated as part of a Technologie / IT cluster but represent professional software-engineering terminology, not general digital-literacy vocabulary. A B2 candidate needs Digitalisierung, Algorithmus, Datenschutz — not Softwarearchitektur or Refactoring.

| ID | German | English | topic | Recommendation | Rationale |
|----|--------|---------|-------|----------------|-----------|
| 4004 | die Softwarearchitektur | software architecture | Technologie | DELETE | IT professional jargon; not in B2 scope |
| 4005 | die Systemarchitektur | system architecture | Technologie | DELETE | Same |
| 4006 | der Softwarearchitekt | software architect | Technologie | KEEP-WITH-TAG | Job title — can appear in B2 Beruf / CV contexts receptively; borderline |
| 4007 | die technische Schuld | technical debt | Technologie | DELETE | Software-engineering jargon; not B2 |
| 4008 | das Refactoring | refactoring | Technologie | DELETE | Software-engineering term; even many native speakers outside IT don't know it |

---

## Category 4: Management Consulting

Entries flagged by the audit as above-B2 management-consulting register.

| ID | German | English | topic | Recommendation | Rationale |
|----|--------|---------|-------|----------------|-----------|
| 3590 | die Lieferantendiversifizierung | supplier diversification | Wirtschaft | DELETE | C1+ supply-chain management register |
| 4012 | die Unternehmensresilienz | corporate resilience | Wirtschaft | DELETE | Management-consulting register; the human-development sense of Resilienz (id 1007) is B2 — this compound is C1+ |
| 4014 | die Risikokultur | risk culture | Wirtschaft | DEMOTE-TO-C1 | Appears in financial-sector journalism; C1 receptive is reasonable |

---

## Category 5: Education Research

Entries around id 3425-3429 and 3587-3588. These are Bildungswissenschaft / Hochschulverwaltung register, not general Bildung vocabulary.

| ID | German | English | topic | Recommendation | Rationale |
|----|--------|---------|-------|----------------|-----------|
| 713 | der Bildungswissenschaftler | educational scientist | Bildung | DEMOTE-TO-C1 | Profession name; appears in academic-context texts at C1 |
| 3425 | die Kompetenzmessung | competence measurement | Bildung | DELETE | Education-research jargon; not B2 |
| 3426 | die Lernstandsdiagnose | learning assessment | Bildung | DELETE | Pädagogisches Fachvokabular; C1 Bildungswissenschaft |
| 3427 | die bildungswissenschaftliche Studie | educational research study | Bildung | DELETE | Discipline-specific; not B2 |
| 3428 | die formative Evaluation | formative evaluation | Bildung | DELETE | Didactics jargon; Profile Deutsch C1 |
| 3429 | die summative Evaluation | summative evaluation | Bildung | DELETE | Same |
| 3587 | die Promotionskommission | doctoral committee | Bildung | DELETE | Hochschulverwaltung; not B2 productive |
| 3588 | das Promotionsrecht | right to award doctorates | Bildung | DELETE | Hochschulrecht; C1+ |

---

## Summary

| Category | DELETE | DEMOTE-TO-C1 | KEEP-WITH-TAG |
|----------|--------|--------------|---------------|
| Research methodology | 8 | 1 | 3 |
| Evidence-based medicine | 6 | 1 | 0 |
| Software architecture | 4 | 0 | 1 |
| Management consulting | 2 | 1 | 0 |
| Education research | 6 | 1 | 0 |
| **Total** | **26** | **4** | **4** |

Note: This count is based on the auditor's sampled zones. The full file may contain additional above-B2 entries in other zones not yet sampled. A second-pass grep across the full file against a C1 term list would surface the remainder. The audit estimated 150-200 total contamination entries; this proposal covers the confirmed sample of ~34 entries. The user may choose to commission a broader sweep as a follow-up.

---

## Action Required from User

For each category above, please confirm:
1. Accept the DELETE / DEMOTE-TO-C1 / KEEP-WITH-TAG recommendations, or override per entry
2. For DEMOTE-TO-C1 entries: confirm whether to move them to `C1_vocabulary.json` (requires the same entry format with `level: "C1"`) or simply remove from B2
3. Authorize a follow-up PR to implement the accepted dispositions
