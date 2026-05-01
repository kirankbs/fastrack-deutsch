# B1 Vocabulary Audit vs Hueber Modelltests

**Date:** 2026-05-01
**Source:** `apps/mobile/src/data/vocabulary/B1_vocabulary.json` (2,630 entries) cross-referenced against 15 Hueber B1 telc Modelltest mocks (`/.planning/research/B1-pdf-reference/mock-01.txt` through `mock-15.txt`, ~355 KB OCR, ~50,300 raw tokens).
**Method:** read-only frequency analysis. Lemmas extracted by regex tokenisation, lowercased, German stopword-filtered, length ≥4. Approximate stem-collapsing (drop common suffixes) used to dedupe inflections. OCR is imperfect — treat counts as ranked signal, not gospel.

---

## 1. Current state

- **Total entries:** 2,630
- **Distinct topics:** 18

### Topic distribution (sorted desc)

| Count | Topic |
|------:|-------|
| 307 | Politik und Gesellschaft |
| 283 | Gesundheit und Ernährung |
| 222 | Charaktereigenschaften |
| 207 | Wirtschaft |
| 202 | Beruf und Arbeit |
| 154 | Medien und Technik |
| 150 | Veranstaltungen |
| 144 | Wohnen |
| 143 | Bildung und Ausbildung |
| 141 | Klima und Umwelt |
| 138 | Wissenschaft und Technik |
| 133 | Sonstiges |
| 120 | Landschaft und Tourismus |
| 117 | Beziehungen und Familie |
| 97 | Kunst und Kultur |
| 26 | Biografien und Geschichte |
| 25 | Sport |
| 21 | Kommunikation und Sprache |

### Coverage check

About 1,311 of 2,630 entries (50%) do not appear (as ≥5-char stem) in any of the 15 Hueber mocks. That's expected — 15 mocks ≈ 50k tokens cannot exercise a 2.6k word list — but the **topic-level miss rate** is the relevant signal. Topics with 55%+ miss rate suggest list and Hueber don't share register:

| Miss rate | Topic | Likely cause |
|----------:|-------|--------------|
| 62% | Politik und Gesellschaft | List is heavy on legal/abstract terms (Aufenthaltserlaubnis, Gerichtsverhandlung, Solidarität); Hueber stays at integration/everyday register |
| 60% | Wohnen | Bureaucratic compounds (Wohnberechtigungsschein, Nebenkostenabrechnung); Hueber tests Wohnung/Miete/Nachbar level |
| 59% | Kunst und Kultur | List leans toward genre vocab (Lyrik, Komponistin, Bildhauer); Hueber prefers Theater/Film/Konzert/Buch |
| 58% | Wirtschaft | Macro/policy terms (Marktwirtschaft, Kapitalismus, Aufschwung); Hueber stays consumer-side (Preis, kaufen, Rechnung) |
| 57% | Klima und Umwelt | Specialised compounds (Trinkwasserversorgung, Ingenieurwissenschaft); Hueber sticks to Müll/Umwelt/Energie |

Topics with healthy match rates: Veranstaltungen (34% miss), Beziehungen und Familie (34%), Sonstiges (11%), Kommunikation und Sprache (5%).

### OCR garbage to ignore

Surface forms that ranked high but are noise: `page` (210 — page-number artifact), `prüfungsteil`, `hilfsmittel`, `tonband`, `markie`, `teih`, `zonmoou`, `clowndoktoren` (text-specific to one mock), proper nouns (`berlin`, `köln`, `münchen`, `düsseldorf`, `frankreich`, `julian`, `craig`, `mika`, `sean`, `thomas`, `guardian`). These were excluded from gap recommendations below.

---

## 2. Gap list — high-frequency Hueber lemmas missing from B1_vocabulary.json

Top ~150 missing lemmas (frequency from 15 mocks, after stopword + duplicate-stem filtering, OCR/proper-noun noise removed). Grouped by likely topic.

### Functional / discourse (highest priority — these recur across every mock)

Frequencies in parentheses.

- **Core verbs missing as headwords:** hören (161), gehören (68), erzählen (50), passen/passt (47), berichten (47), sehen (32), sagen (26), finden (24), bieten (18), helfen (16), nehmen (13), bringen (14), meinen (11), erhalten (9), scheinen (9)
- **Core nouns missing:** Information (116), Thema (65), Brief (59), Überschrift (59), Ausdruck (35), Wort/Wörter (33), Moment (18), Abend (16), Lücke (13), Alter (13), Kosten (13), Programm (12), Monat (12), Nähe (12), Adresse (12), Platz (11)
- **Adjectives/adverbs:** gern (62), selbst (49), schnell (33), lange (31), weitere (22), klein (22), wichtig (17), besser (16), groß (16), sofort (13), leider (13), direkt (12), endlich (12), weit (12), eigene (11), am liebsten (11)
- **Numerals as headwords:** drei (43), fünf (76), sechs (11), zehn (30) — and decade/hundreds compounds

### Daily life / themes (frequency in parentheses)

- **Sonstiges/general:** Mensch (51), Leute (30), Stunde (22), Hobby (20), Wochenende (14), Sekunde (16), Sommer (10), Million (9), Prozent (17), täglich (19), allein (31), früher (10), später (14)
- **Beziehungen und Familie:** kennenlernen (25), Junge/Jungen (15), Mädchen (18), Streit (9), Lust haben (8), Männer (10), Flirt (11), Heimat (8)
- **Bildung:** Studium (21), Wörterbuch (44), Bleistift (19), Notiz (17), Zettel (15), Studenten (12), Sprachreise (9), Mitschüler (8)
- **Veranstaltungen:** Mitglieder (12), Party (9), verbringen (14)
- **Wohnen:** Garten (31), Straße (13), umziehen (7)
- **Wirtschaft:** Preis (12), Service (13), tauschen (9)
- **Klima:** Umweltschutz (9)
- **Beruf:** Erfahrung (46), Büro (9)
- **Kunst und Kultur:** Musik (26), Film (11), Band (10), Theater (8)
- **Tourismus:** Bahn (11), Motorrad (10)
- **Gesundheit:** essen (verb, 49), Schlaf/schlafen (12), Augen (8)
- **Medien:** Zeitungsartikel (12), Zeitschrift (8), Betreff (8)
- **Kommunikation und Sprache:** Sprache (18), Englisch (8), Kontaktaufnahme (16, Sprechen Teil 1 stock phrase)
- **Politik und Gesellschaft:** Jugendliche (19), Jugend (9), Verhalten (8), Organisation (8)
- **Other discourse markers:** Schluss/zum Schluss (20), Achtung (15), inzwischen (7), rund (13), Reihenfolge (45)
- **Sonstiges (proper nouns/animals):** Hund (26), Sprache (18), Wort (33)

That's ~140 high-frequency gaps. Filling Batch 1+2 (below) alone covers the top 60.

---

## 3. Above-level candidates — possible B2/C1 register leak

These current entries are flagged either by suffix patterns (-ität, -ismus, -isierung) or by being unusually long compounds/abstract. Many ARE legitimate B1 (telc B1 word list does include some of these), but each warrants pedagogy review:

### Probably above-level — strong leak signal

| Entry | Topic | Reason |
|-------|-------|--------|
| die Steueridentifikationsnummer | Politik und Gesellschaft | 27-char compound, B2/C1 register |
| die Sozialversicherungsnummer | Politik und Gesellschaft | bureaucratic, B2 |
| die Lebensabschnittspartnerin | Beziehungen und Familie | journalistic/abstract, B2+ |
| die Glutenunverträglichkeit | Gesundheit und Ernährung | medical specialised, B2 |
| der Wohnberechtigungsschein | Wohnen | German bureaucracy, B2 |
| die Trinkwasserversorgung | Klima und Umwelt | environmental policy, B2 |
| die Ingenieurwissenschaft | Wissenschaft und Technik | academic, B2/C1 |
| die Datenschutzerklärung | Medien und Technik | legal, B2 |
| die Aufenthaltserlaubnis | Politik und Gesellschaft | legal, edge B1/B2 — keep but verify |
| das Literaturverzeichnis | Bildung und Ausbildung | academic writing, B2 |
| die Wirtschaftsstruktur | Wirtschaft | macroeconomics, B2 |
| die Arbeitsmarktpolitik | Wohnen (mistagged) | policy, B2; also wrong topic |
| die Nebenkostenabrechnung | Wohnen | bureaucratic, B2 |
| die Kundenzufriedenheit | Wirtschaft | business jargon, B2 |
| der Dienstleistungssektor | Wirtschaft | macroeconomics, B2 |
| die Vorsorgeuntersuchung | Gesundheit | medical, B2 |
| die Gerichtsverhandlung | Politik | legal, B2 |
| der Rassismus | Politik | abstract -ismus, B2 |
| der Terrorismus | Politik | abstract -ismus, B2 |
| der Kapitalismus | Wirtschaft | abstract -ismus, B2/C1 |
| die Globalisierung | Wirtschaft | abstract -isierung, B2 |
| die Digitalisierung | Wissenschaft und Technik | abstract -isierung, B2 |
| die Solidarität | Politik | abstract, B2 |
| die Kriminalität | Politik | abstract, edge B1/B2 |
| die Hilfsorganisation | Politik | abstract compound, edge B1/B2 |
| die Lebensqualität | Charaktereigenschaften | abstract — also miscategorised |

### Likely keep but flag for review

| Entry | Note |
|-------|------|
| die Universität, die Theorie, die Spezialität, der Tourismus, die Nationalität, die Pressekonferenz, die Videokonferenz, die Konferenz, die Konsequenz, der Optimismus, der Pessimismus, die Kreativität | These are common enough to stay — they're in standard telc B1 word lists. |

About **20–25 entries** are realistic candidates for downward delete or move-to-B2.

---

## 4. Topic rebalancing recommendations

### Over-represented relative to Hueber

- **Politik und Gesellschaft (307, top topic):** 62% miss rate. Cluster has too many legal/bureaucratic/abstract terms. Hueber pulls Politik content but at register: Demonstration, Toleranz, Heimat, Integration (general) — not Aufenthaltserlaubnis, Gerichtsverhandlung, Freispruch. Consider trimming 30–40 abstract/legal entries.
- **Wirtschaft (207):** 58% miss. Macro vocab (Marktwirtschaft, Aufschwung, Kapitalismus) outweighs everyday consumer vocab. Trim 20–25 macro terms.
- **Wissenschaft und Technik (138):** 51% miss. Academic terminology (Schwerkraft, Ingenieurwissenschaft, Soziologie, Galaxie, Satellit). Trim ~15 entries; replace with everyday tech (Internet, Email, Passwort, App, herunterladen, hochladen — currently absent).
- **Charaktereigenschaften (222):** 51% miss. Some abstract nouns (Gelassenheit, Traurigkeit, Lebensstandard) — Hueber tests adjectives, not abstract emotion nouns. Cluster is mostly fine; trim ~10.

### Under-represented relative to Hueber

- **Sonstiges/discourse + meta-vocab:** missing core function words (Brief, Überschrift, Lücke, Notiz, Tabelle, Reihenfolge, Wort, Information). These appear in *every* mock and are needed for test instructions/Sprachbausteine.
- **Kommunikation und Sprache (21):** wildly under-built. Hueber Sprechen Teil 1 ("Kontaktaufnahme") uses recurring set of phrases — list has only 21 entries here.
- **Beziehungen und Familie (117):** core relationship verbs/nouns missing (kennenlernen, Streit, Lust haben, allein, Mädchen, Junge). Add 30–40.
- **Veranstaltungen (150):** missing Party, Wochenende, verbringen, Mitglieder, Hobby. Cluster likely has corporate-event bias instead of leisure/social.
- **Sport (25), Biografien und Geschichte (26):** both very thin but defensible — telc B1 doesn't lean heavily on these. Hold.

---

## 5. Priority actions for impl-lead

Top 10 vocab batches to add or replace, in priority order. Each batch is a coherent ~25–40 word set the impl-lead can build in one session.

1. **Test-meta and discourse vocabulary (≈30 entries)** — Brief, Überschrift, Lücke, Notiz, Tabelle, Reihenfolge, Information, Thema, Ausdruck, Wort, Wörterbuch, Beispiel, Aufgabe, Antwort, Frage, Markierung, Erklärung, Hinweis, Begründung, Zusammenfassung, etc. **Highest priority** — appear in every Hueber mock.

2. **Core verbs missing as headwords (≈25 entries)** — hören, sehen, sagen, erzählen, berichten, finden, meinen, scheinen, erhalten, helfen, nehmen, bringen, bieten, passen, gehören, verbringen, ziehen, tauschen, reparieren. Plus past participles where common (gehört, gelesen, gelernt, gefallen).

3. **Beziehungen und Familie expansion (≈30 entries)** — kennenlernen, Kontaktaufnahme, Streit (sich streiten), Lust haben (auf), Verabredung, sich verabreden, allein, Junge/Mädchen, Männer/Frauen as collective, Trennung, Heirat (already present?), Flirt, Party, Hobby. Many of these already appear in the language-of-introduction speaking task.

4. **Politik und Gesellschaft trim + rebalance (≈30 in/30 out)** — DELETE: Steueridentifikationsnummer, Sozialversicherungsnummer, Wohnberechtigungsschein, Gerichtsverhandlung, Freispruch, Angeklagte, Diebstahl, Marktwirtschaft, Kapitalismus, Terrorismus, Rassismus, Solidarität, Lebensabschnittspartnerin. ADD: Mensch, Heimat, Verhalten, Jugend, Jugendliche, Organisation, Toleranz (already?), Demonstration (already?), Integration, Million, Prozent, Gesellschaft, Umweltschutz.

5. **Wirtschaft trim + everyday-consumer pivot (≈25 in/20 out)** — DELETE: Dienstleistungssektor, Wirtschaftsstruktur, Kundenzufriedenheit, Aufschwung, Marktwirtschaft, Kapitalismus, Globalisierung, Marktstand, Bauernmarkt. ADD: Preis, Service, Kosten, reparieren, tauschen, Adresse, Rechnung, Konto, sparen, überweisen, Quittung, Beschwerde, einkaufen.

6. **Wohnen trim + everyday-housing pivot (≈25 in/20 out)** — DELETE: Wohnberechtigungsschein, Nebenkostenabrechnung, Wohnungsbaugesellschaft, Arbeitsmarktpolitik (mistagged), Trinkwasserversorgung. ADD: Garten, Straße, Nähe, umziehen, Vermieter, Vermieterin, Reparatur, Renovierung, Nachbar (already?), eigene (Wohnung), Platz.

7. **Medien und Technik everyday-tech (≈25 entries)** — Internet (probably present), Email, Betreff, Anhang, Passwort, App, herunterladen, hochladen, Smartphone, Handy, surfen, posten, Profil, Account, Nachricht senden, Zeitungsartikel, Zeitschrift, Programm. Many of these are surprisingly absent.

8. **Charaktereigenschaften adjective layer (≈20 entries)** — replace abstract nouns with frequent adjectives that Hueber actually tests. ADD: ehrlich (?), lustig, ernst, ruhig, nervös, frech, faul, fleißig, freundlich, zuverlässig, hilfsbereit, ordentlich. DELETE 8–10 abstract emotion nouns (Gelassenheit, Traurigkeit, Erschöpfung).

9. **Veranstaltungen / leisure (≈20 entries)** — Wochenende, Party, Hobby, Hobbys, verbringen, Mitglieder, Verein, Sportverein, Theater, Konzert, Musikfestival, Ausstellung, Lesung, Treffen. Current cluster is corporate-event-heavy.

10. **Numerals + adverbs of time/quantity (≈20 entries)** — drei, fünf, sechs, sieben, acht, neun, zehn, hundert, tausend, Million, Prozent, einmal, zweimal, dreimal, täglich, allein, früher, später, sofort, endlich, inzwischen, leider, jedoch, deshalb, trotzdem, außerdem, einerseits, andererseits. These are *Sprachbausteine ammunition* and several appear ZERO times in our list.

---

## Summary numbers

- 2,630 entries → recommend net **~+50 to +100** after trim/add cycle (target ~2,700).
- ~25 entries flagged as B2 leak → move to B2 list or delete.
- ~150 high-frequency Hueber lemmas to add (Batches 1–2 alone cover the top 60).
- 4 topics (Politik, Wirtschaft, Wohnen, Wissenschaft und Technik) need register pivot from policy/academic to everyday/consumer.
- 3 topics (Kommunikation und Sprache, Beziehungen, Veranstaltungen) need volume.

Caveats: OCR is noisy (page-number tokens, proper nouns, fragmented compounds). Lemma extraction was bag-of-words — no morphology, no NER. Treat ranks as ordinal signal. Final add/delete calls should run through pedagogy-director before impl-lead executes batches.
