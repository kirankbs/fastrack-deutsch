#!/usr/bin/env python3
"""
Builder script for C1 mock_01.json.
Theme: Wissenschaftliche Erkenntnis und Verantwortung
  (Reproduzierbarkeitskrise, Open Science, Wissenschaftsethik, KI in der Forschung)

Sections (per gate doc C1-exam-format.md):
  Lesen:          3 parts  -> 6 + 6 + 12 (11 R/F/N + 1 Makro) = 24 items, 48 pts
  Sprachbausteine: 1 part  -> 22 MCQ-4opt cloze items, 22 pts
  Hören:          3 parts  -> 8 + 10 + 10 = 28 items, 48 pts
  Schreiben:      1 task   -> choose 1 of 2, 4 Leitpunkte, 350+ words, 48 pts
  Sprechen:       3 parts  -> Teil 1A (Präsentation) + Teil 1B (Zusammenfassung) + Teil 2 (Diskussion)
"""

import json, os

# ─────────────────────────────────────────────────────────────────────────────
# READING
# ─────────────────────────────────────────────────────────────────────────────

reading_teil1_text = """Wissenschaft im Vertrauenscrash

Die Grundlage wissenschaftlichen Arbeitens ist der Gedanke, dass Ergebnisse nachvollziehbar und reproduzierbar sind. [1] Wer ein Experiment unter denselben Bedingungen wiederholt, müsste – so die Erwartung – zu denselben Schlüssen gelangen. Dieses Prinzip galt lange als selbstverständlich. [2] Doch seit gut einem Jahrzehnt häufen sich Befunde, die genau diese Selbstverständlichkeit in Frage stellen.

Ausgangspunkt der Debatte war eine groß angelegte Studie aus dem Jahr 2015, bei der Wissenschaftlerinnen und Wissenschaftler versuchten, hundert Experimente aus führenden Psychologiezeitschriften zu replizieren. [3] Nur rund 36 Prozent der ursprünglichen Befunde konnten dabei statistisch bestätigt werden – ein Ergebnis, das in der Fachwelt wie ein Schock wirkte und die sogenannte Reproduzierbarkeitskrise auslöste.

Was steckt hinter diesem Phänomen? Einfache Antworten greifen zu kurz. Zum einen spielen strukturelle Anreize im Wissenschaftssystem eine Rolle: [4] Wer publiziert, wird befördert; wer scheitert, bleibt unsichtbar. Negative Ergebnisse finden kaum Platz in renommierten Fachzeitschriften. Zum anderen verführt die Fülle moderner Analysesoftware zu einem Phänomen, das Methodologen als „p-Hacking" bezeichnen: Das gezielte Testen zahlreicher Variablen so lange, bis sich eine statistisch signifikante – jedoch zufällige – Korrelation ergibt.

Hinzu kommt ein dritter Faktor, der selten offen benannt wird. [5] Die akademische Gemeinschaft ist nicht immun gegen den Wunsch, bestehende Überzeugungen zu bestätigen. Dieser Bestätigungsfehler tritt auch bei gut ausgebildeten Forschenden auf und kann unbewusst die Auswahl von Stichproben, die Formulierung von Hypothesen oder die Interpretation mehrdeutiger Daten beeinflussen.

Open Science gilt vielen als vielversprechendste Antwort auf die Krise. [6] Dazu gehören Vorregistrierung von Studien – bei der Forscher ihre Hypothesen und Methoden vor Beginn der Datenerhebung öffentlich festhalten –, offene Datensätze sowie transparente Peer-Review-Verfahren. Kritiker warnen allerdings, dass allein mehr Transparenz strukturelle Fehlanreize nicht beseitigt, solange Beförderung und Drittmittelerfolg die Richtschnur akademischer Karrieren bleiben."""

reading_teil1_sentences = [
    {"id": "C1_m01_R1_sent_a", "type": "notice", "content": "a) Dieses Ideal prägten die Naturwissenschaften seit dem 17. Jahrhundert, als die experimentelle Methode zum Eckstein des modernen Wissensgebäudes wurde."},
    {"id": "C1_m01_R1_sent_b", "type": "notice", "content": "b) Allerdings stößt selbst dieses Modell an Grenzen, wenn die zugrundeliegenden Rohdaten nicht zugänglich sind oder Stichprobengrößen zu klein ausfallen."},
    {"id": "C1_m01_R1_sent_c", "type": "notice", "content": "c) Das Ergebnis erschütterte nicht nur die Psychologie, sondern befeuerte eine Debatte, die seither auf Medizin, Ökologie und Wirtschaftswissenschaften übergegriffen hat."},
    {"id": "C1_m01_R1_sent_d", "type": "notice", "content": "d) Unter solchen Bedingungen lohnt es sich für viele Forschende schlicht nicht, Zeit in das aufwendige Nachprüfen fremder Studien zu investieren."},
    {"id": "C1_m01_R1_sent_e", "type": "notice", "content": "e) Das bedeutet freilich nicht, dass jede wissenschaftliche Erkenntnis grundsätzlich unzuverlässig ist – vielmehr mahnt es zu größerer Bescheidenheit beim Interpretieren einzelner Studien."},
    {"id": "C1_m01_R1_sent_f", "type": "notice", "content": "f) Solche Vorwürfe treffen nicht nur auf Ablehnung, sondern sind mittlerweile empirisch belegt: Analysen von Tausenden Studien zeigen gehäufte p-Werte knapp unterhalb der Signifikanzschwelle von 0,05 – ein statistisches Fingerabdruck von Datenselektion."},
    {"id": "C1_m01_R1_sent_g", "type": "notice", "content": "g) Die Kommission empfahl daraufhin, alle Studien mit menschlichen Probanden vor Beginn in einem öffentlich zugänglichen Register einzutragen."},
    {"id": "C1_m01_R1_sent_h", "type": "notice", "content": "h) Dennoch bleibt umstritten, ob solche Maßnahmen ausreichen oder ob ein grundlegenderer Wandel der Bewertungskultur nötig wäre."},
]

reading_teil1_questions = [
    {
        "id": "C1_m01_R1_q1",
        "type": "matching",
        "questionText": "Lücke 1 im Text: '…sind nachvollziehbar und reproduzierbar. [1] Wer ein Experiment…'",
        "matchingSources": [{"id": s["id"], "label": s["id"].split("_")[-1]} for s in reading_teil1_sentences],
        "correctAnswer": "a",
        "explanation": "Lücke 1 folgt auf die grundlegende Aussage über Nachvollziehbarkeit und Reproduzierbarkeit. Satz a) führt historisch aus, dass dieses Ideal seit dem 17. Jahrhundert gilt – der Diskurs-Marker 'Dieses Ideal' verbindet rückverweisend auf den Vorsatz. Satz e) käme thematisch nahe, verwendet aber 'Das bedeutet freilich nicht' – eine konzessive Wendung, die eine bereits genannte Kritik voraussetzt, die an Lücke 1 noch nicht eingeführt wurde."
    },
    {
        "id": "C1_m01_R1_q2",
        "type": "matching",
        "questionText": "Lücke 2 im Text: '…galt lange als selbstverständlich. [2] Doch seit gut einem Jahrzehnt…'",
        "matchingSources": [{"id": s["id"], "label": s["id"].split("_")[-1]} for s in reading_teil1_sentences],
        "correctAnswer": "e",
        "explanation": "Lücke 2 steht direkt vor dem konzessiven 'Doch', das die Selbstverständlichkeit in Frage stellt. Satz e) ('Das bedeutet freilich nicht, dass…') schlägt eine konzessive Brücke – er räumt Bedenken ein, ohne die Grundlage zu verwerfen, was perfekt mit der nachfolgenden Warnung 'Doch seit gut einem Jahrzehnt…' korrespondiert."
    },
    {
        "id": "C1_m01_R1_q3",
        "type": "matching",
        "questionText": "Lücke 3 im Text: '…hundert Experimente…zu replizieren. [3] Nur rund 36 Prozent…'",
        "matchingSources": [{"id": s["id"], "label": s["id"].split("_")[-1]} for s in reading_teil1_sentences],
        "correctAnswer": "c",
        "explanation": "Lücke 3 folgt auf die Beschreibung der Replikationsstudie. Satz c) wertet das Ergebnis aus und benennt seine Ausstrahlungswirkung auf andere Disziplinen – das Wort 'Das Ergebnis' verweist anaphorisch auf die Studie im Vorsatz."
    },
    {
        "id": "C1_m01_R1_q4",
        "type": "matching",
        "questionText": "Lücke 4 im Text: '…spielen strukturelle Anreize…eine Rolle: [4] Wer publiziert, wird befördert…'",
        "matchingSources": [{"id": s["id"], "label": s["id"].split("_")[-1]} for s in reading_teil1_sentences],
        "correctAnswer": "d",
        "explanation": "Lücke 4 steht mitten in der Erläuterung struktureller Anreize. Satz d) schließt direkt an: 'Unter solchen Bedingungen lohnt es sich…nicht, Zeit…zu investieren' – 'solchen Bedingungen' verweist anaphorisch auf die im Vorsatz beschriebene Publish-or-Perish-Logik."
    },
    {
        "id": "C1_m01_R1_q5",
        "type": "matching",
        "questionText": "Lücke 5 im Text: '…selten offen benannt wird. [5] Die akademische Gemeinschaft ist nicht immun…'",
        "matchingSources": [{"id": s["id"], "label": s["id"].split("_")[-1]} for s in reading_teil1_sentences],
        "correctAnswer": "f",
        "explanation": "Lücke 5 folgt auf die Einführung des Bestätigungsfehlers. Satz f) liefert empirische Belege für das p-Hacking-Phänomen ('statistisches Fingerabdruck von Datenselektion') und schließt damit die Reihe der Erklärungsfaktoren ab. Satz g) käme thematisch in Frage, setzt aber eine vorangehende Empfehlung voraus, die im Kontext nicht erscheint."
    },
    {
        "id": "C1_m01_R1_q6",
        "type": "matching",
        "questionText": "Lücke 6 im Text: '…Open Science gilt vielen als vielversprechendste Antwort…[6] Dazu gehören Vorregistrierung…'",
        "matchingSources": [{"id": s["id"], "label": s["id"].split("_")[-1]} for s in reading_teil1_sentences],
        "correctAnswer": "b",
        "explanation": "Lücke 6 steht am Ende des Textes, nachdem Open Science eingeführt wurde. Satz b) ('stößt selbst dieses Modell an Grenzen, wenn die zugrundeliegenden Rohdaten nicht zugänglich sind…') ergänzt die im Folgesatz genannten Maßnahmen mit einer kritischen Einschränkung – 'selbst dieses Modell' verweist katakaphorisch auf das Open-Science-Konzept."
    }
]

# LV Teil 2 — Selektives Verstehen: 5 paragraphs + 6 questions
# Topic: KI in der Forschung — 5 kurze Absätze aus verschiedenen Perspektiven

reading_teil2_paragraphs = [
    {
        "id": "C1_m01_R2_para_a",
        "type": "article",
        "content": "a) Immer mehr Forschungsgruppen weltweit setzen KI-gestützte Werkzeuge ein, um Literaturrecherchen zu beschleunigen, Datensätze auszuwerten und erste Textfassungen von Manuskripten zu strukturieren. Befürworter betonen, dass künstliche Intelligenz dabei helfe, den wachsenden Publikationsberg zu bewältigen: Ein Algorithmus kann in Stunden Tausende Papers nach relevanten Befunden durchforsten, was menschlichen Forschenden Wochen kosten würde. Allerdings warnen Methodologen, dass KI-Systeme bestehende Verzerrungen in der Forschungsliteratur unkritisch reproduzieren – wer also voreingenommene Daten eingibt, erhält voreingenommene Zusammenfassungen."
    },
    {
        "id": "C1_m01_R2_para_b",
        "type": "article",
        "content": "b) Die Frage, ob KI-generierte Texte in wissenschaftlichen Arbeiten deklariert werden müssen, wird in Fachkreisen kontrovers diskutiert. Während einige Verlage bereits eine vollständige Offenlegung verlangen – und KI ausdrücklich nicht als Mitautor anerkennen –, lehnen andere eine Regulierung als praxisfern ab. Kritiker weisen darauf hin, dass die Grenze zwischen legitimer Nutzung eines Rechtschreibprogramms und dem Erstellen ganzer Argumentationsketten durch ein Sprachmodell fließend ist und bislang keine allgemein akzeptierte Definition existiert, was genau offenlegungspflichtig sein soll."
    },
    {
        "id": "C1_m01_R2_para_c",
        "type": "article",
        "content": "c) Besonders in den Lebenswissenschaften hat der Einsatz von KI zur Proteinfaltungsvorhersage bereits messbare Fortschritte erzielt. AlphaFold, das von DeepMind entwickelte System, ermöglichte Strukturvorhersagen, für die Forscher zuvor Jahrzehnte experimenteller Arbeit benötigt hätten. Dieser Durchbruch verändert die Grundbedingungen biomedizinischer Forschung fundamental: Was früher ein mühsamer Prozess war, der ganze Laborgenerationen beanspruchte, kann nun in Wochen simuliert werden. Einige Wissenschaftlerinnen sehen darin den Beginn einer neuen Ära – andere mahnen, dass Simulationsergebnisse nach wie vor experimentell validiert werden müssen."
    },
    {
        "id": "C1_m01_R2_para_d",
        "type": "article",
        "content": "d) Weniger beachtet, aber nicht weniger folgenreich ist die Frage der Datenhoheit. Wenn Forschungseinrichtungen proprietäre KI-Systeme großer Technologiekonzerne nutzen, geben sie unter Umständen Kontrolle über sensible Forschungsdaten ab. Mehrere europäische Universitäten haben daher begonnen, eigene, quelloffene Sprachmodelle zu betreiben, die auf ihren eigenen Servern laufen. Dieser Ansatz ist kostspielig und technisch anspruchsvoll, bietet aber den Vorteil, dass Forschungsdaten die institutionelle Kontrolle nicht verlassen."
    },
    {
        "id": "C1_m01_R2_para_e",
        "type": "article",
        "content": "e) Die Debatte um KI in der Wissenschaft berührt schließlich eine grundlegendere Frage: Was ist eigentlich Autorenschaft? Wenn ein Algorithmus den strukturellen Rahmen eines Artikels vorgibt, Belege auswählt und Schlussfolgerungen formuliert, wer trägt dann die wissenschaftliche Verantwortung für die Richtigkeit der Aussagen? Bislang gilt in der Wissenschaftsethik die Regel, dass Autorenschaft intellektuelle Eigenverantwortung voraussetzt – eine Norm, die durch den massenhaften Einsatz generativer KI unter Druck gerät."
    }
]

reading_teil2_questions = [
    {
        "id": "C1_m01_R2_q1",
        "type": "mcq",
        "questionText": "In welchem Absatz wird darauf hingewiesen, dass KI bestehende Forschungsverzerrungen übernehmen kann?",
        "options": ["a", "b", "c", "d", "e"],
        "correctAnswer": "a",
        "explanation": "Absatz a) enthält explizit: 'wer also voreingenommene Daten eingibt, erhält voreingenommene Zusammenfassungen'. Diese Aussage über die unkritische Reproduktion von Verzerrungen durch KI findet sich nur in Absatz a)."
    },
    {
        "id": "C1_m01_R2_q2",
        "type": "mcq",
        "questionText": "Welcher Absatz behandelt die Schwierigkeit, eine einheitliche Definition für offenlegungspflichtige KI-Nutzung zu finden?",
        "options": ["a", "b", "c", "d", "e"],
        "correctAnswer": "b",
        "explanation": "Absatz b) thematisiert die Kontroverse um Deklarationspflichten und stellt fest: 'bislang keine allgemein akzeptierte Definition existiert, was genau offenlegungspflichtig sein soll'. Diese Definitionsproblematik wird ausschließlich in Absatz b) behandelt."
    },
    {
        "id": "C1_m01_R2_q3",
        "type": "mcq",
        "questionText": "In welchem Absatz wird betont, dass KI-gestützte Ergebnisse weiterhin experimentell überprüft werden müssen?",
        "options": ["a", "b", "c", "d", "e"],
        "correctAnswer": "c",
        "explanation": "Absatz c) schließt mit: 'andere mahnen, dass Simulationsergebnisse nach wie vor experimentell validiert werden müssen'. Der Hinweis auf die Notwendigkeit experimenteller Validierung erscheint nur in Absatz c)."
    },
    {
        "id": "C1_m01_R2_q4",
        "type": "mcq",
        "questionText": "Welcher Absatz beschreibt Maßnahmen, die den Verlust institutioneller Datenkontrolle verhindern sollen?",
        "options": ["a", "b", "c", "d", "e"],
        "correctAnswer": "d",
        "explanation": "Absatz d) beschreibt, dass europäische Universitäten quelloffene, selbst betriebene Sprachmodelle entwickeln, um die Kontrolle über Forschungsdaten zu behalten. Das Thema Datenhoheit und institutionelle Kontrollmaßnahmen ist ausschließlich Gegenstand von Absatz d)."
    },
    {
        "id": "C1_m01_R2_q5",
        "type": "mcq",
        "questionText": "Welcher Absatz wirft die Frage auf, wer bei KI-mitgeneriertem Inhalt die wissenschaftliche Verantwortung trägt?",
        "options": ["a", "b", "c", "d", "e"],
        "correctAnswer": "e",
        "explanation": "Absatz e) fragt explizit: 'wer trägt dann die wissenschaftliche Verantwortung für die Richtigkeit der Aussagen?' Die Frage nach Autorenschaft und wissenschaftlicher Eigenverantwortung ist der Kern von Absatz e)."
    },
    {
        "id": "C1_m01_R2_q6",
        "type": "mcq",
        "questionText": "In welchem Absatz wird erläutert, dass KI die Geschwindigkeit bestimmter biologischer Forschungsprozesse radikal verändert hat?",
        "options": ["a", "b", "c", "d", "e"],
        "correctAnswer": "c",
        "explanation": "Absatz c) beschreibt, dass AlphaFold Strukturvorhersagen ermöglicht, 'für die Forscher zuvor Jahrzehnte experimenteller Arbeit benötigt hätten', und nennt dies den 'Beginn einer neuen Ära'. Die Radikalbeschleunigung biologischer Forschung durch KI ist Thema von Absatz c)."
    }
]

# LV Teil 3 — Detailverstehen + Globalverstehen: long article ~950 words
# Topic: Open Science — Wie offene Wissenschaft die Forschungslandschaft verändert

reading_teil3_article = {
    "id": "C1_m01_R3_article",
    "type": "article",
    "content": """Open Science: Zwischen Aufbruch und Überforderung

Der Begriff Open Science klingt schlicht: Wissenschaft soll offen sein, für alle zugänglich, transparent und nachvollziehbar. Hinter dieser Formel verbirgt sich jedoch ein tiefgreifender Wandel in der Art und Weise, wie Forschung produziert, bewertet und verbreitet wird. Seit gut einem Jahrzehnt gewinnt die Open-Science-Bewegung an Dynamik – getragen von einer Generation von Forschenden, die sich gegen die geschlossenen Strukturen des akademischen Verlagswesens stemmen, und befeuert durch digitale Infrastrukturen, die eine weltweite Teilen von Daten, Methoden und Ergebnissen erstmals praktikabel machen.

Der Kern des Problems liegt in einem historisch gewachsenen Paradox: Öffentlich finanzierte Forschung landet in Zeitschriften privater Verlage, die ihren Inhalt hinter teuren Abonnementzäunen sperren. Universitätsbibliotheken in Deutschland zahlen jährlich Hunderte Millionen Euro, damit ihre Wissenschaftler und Studierenden auf Artikel zugreifen können, die sie selbst geschrieben oder deren Begutachtung sie unentgeltlich übernommen haben. Dieses Geschäftsmodell, das in den 1970er Jahren mit dem Aufkommen spezialisierter Fachverlage entstand, gilt Kritikern als anachronistisch – und als strukturelle Bremse für wissenschaftlichen Fortschritt in ressourcenschwachen Ländern.

Open Access – der freie Zugang zu wissenschaftlichen Publikationen – ist der bekannteste Pfeiler von Open Science. Doch die Bewegung reicht weiter: Open Data verlangt, dass die erhobenen Rohdaten einer Studie öffentlich zugänglich gemacht werden, damit andere Forschende sie nachprüfen oder für eigene Analysen nutzen können. Open Methods fordert transparente Dokumentation von Labormethoden und Analyseskripten. Open Peer Review öffnet den bislang anonymen Begutachtungsprozess für externe Beobachter oder publiziert Gutachten zusammen mit dem Artikel. Zusammen genommen sollen diese Prinzipien jene Lücken schließen, die die Reproduzierbarkeitskrise aufgedeckt hat: zu wenige Daten, zu wenig Methodentransparenz, zu viel Selektionsdruck.

Die Fortschritte sind real, aber unevenverteil. In der Biomedizin und den Naturwissenschaften haben Preprint-Server wie bioRxiv und medRxiv die Verbreitung vorläufiger Ergebnisse revolutioniert: Forschende stellen Manuskripte vor der Begutachtung online, erhalten schnell Rückmeldungen aus der Community und können Fehler beheben, bevor ein Artikel offiziell erscheint. In der COVID-19-Pandemie erwies sich dieses System als unverzichtbar: In wenigen Wochen kurierten Wissenschaftler weltweit auf Preprint-Servern die für die Impfstoffentwicklung relevanten Erkenntnisse. Gleichzeitig zeigte die Pandemie die Schattenseiten: Vorläufige Ergebnisse ohne Peer Review wurden von Medien aufgegriffen und als gesichertes Wissen dargestellt – mit teils folgenreichen Missverständnissen.

In den Geistes- und Sozialwissenschaften ist die Lage komplizierter. Forschungsdaten bestehen häufig aus vertraulichen Interviews, sensiblen Archivmaterialien oder personenbezogenen Umfrageantworten – alles Material, das aus datenschutzrechtlichen oder ethischen Gründen nicht ohne Weiteres geteilt werden kann. Hier stoßen die Prinzipien von Open Data an rechtliche und methodologische Grenzen, die noch kein Konsens überbrückt hat. Viele Geistes- und Sozialwissenschaftler empfinden die aus den MINT-Fächern importierten Open-Science-Normen als kulturfremd und halten die Qualität eines Interpretationsprozesses für nicht sinnvoll in ein offenes Datenformat übersetzbar.

Hinzu kommt eine ökonomische Dimension, die Reformbemühungen verkompliziert. Open-Access-Verlage finanzieren sich häufig über Artikel-Bearbeitungsgebühren (Article Processing Charges, APCs), die Autorinnen und Autoren – oder deren Institutionen – zahlen müssen, wenn ihre Arbeit frei zugänglich erscheinen soll. Für Forschende aus Hochlohnländern mit gut ausgestatteten Bibliotheken ist das handhabbar. Für Wissenschaftlerinnen und Wissenschaftler aus dem Globalen Süden, die weder über institutionelle Abonnementbudgets noch über APC-Fördertöpfe verfügen, droht Open Access paradoxerweise eine neue Exklusionslogik zu erzeugen: Lesen können nun alle – publizieren nicht.

Europäische Forschungsförderer wie die Deutsche Forschungsgemeinschaft und die EU-Kommission haben mit Plan S eine Initiative auf den Weg gebracht, die für geförderte Forschung verbindlichen Open-Access-Zugang bis 2025 vorschreibt. Die Initiative hat Bewegung in den Markt gebracht: Mehrere Großverlage verhandeln sogenannte Transformationsverträge, die Abonnementgebühren und APCs in einem Gesamtpaket bündeln. Ob diese Verträge wirklich zur Öffnung des Systems führen oder lediglich die Erlösmodelle der Verlage sichern, ist unter Bibliothekaren und Wissenschaftlern heftig umstritten.

Am Ende läuft die Open-Science-Debatte auf eine tiefere Frage hinaus: Wem gehört Wissen? Wenn es mit öffentlichen Mitteln erzeugt wird, scheint die Antwort naheliegend – der Gesellschaft. Doch die Umsetzung dieser Antwort verlangt, überkommene Infrastrukturen, Anreizstrukturen und Bewertungslogiken des Wissenschaftssystems von Grund auf zu transformieren. Das ist kein technisches, sondern ein politisches und kulturelles Problem. Und bis es gelöst ist, bleibt Open Science das, was ihr Name verspricht und noch nicht ganz einlöst: ein Ideal im Werden.""",
    "source": "Forschung & Lehre, Ausgabe 3/2026"
}

reading_teil3_questions = [
    {
        "id": "C1_m01_R3_q1",
        "type": "true_false",
        "questionText": "Öffentlich finanzierte Forschung wird häufig in Zeitschriften veröffentlicht, für die Universitäten hohe Summen zahlen müssen.",
        "options": ["richtig", "falsch", "nicht im Text"],
        "correctAnswer": "richtig",
        "explanation": "Der Text beschreibt explizit: 'Universitätsbibliotheken in Deutschland zahlen jährlich Hunderte Millionen Euro' für den Zugang zu Artikeln aus öffentlich finanzierter Forschung. Die Aussage ist korrekt."
    },
    {
        "id": "C1_m01_R3_q2",
        "type": "true_false",
        "questionText": "Open Peer Review bedeutet, dass Gutachter anonym bleiben, aber ihre Bewertungen veröffentlicht werden.",
        "options": ["richtig", "falsch", "nicht im Text"],
        "correctAnswer": "falsch",
        "explanation": "Der Text definiert Open Peer Review als Öffnung 'des bislang anonymen Begutachtungsprozesses für externe Beobachter oder publiziert Gutachten zusammen mit dem Artikel'. Anonymität der Gutachter ist nicht die Kernaussage – vielmehr wird gerade die Anonymität aufgebrochen. Die Aussage ist daher falsch."
    },
    {
        "id": "C1_m01_R3_q3",
        "type": "true_false",
        "questionText": "Preprint-Server wie bioRxiv erlauben es, Forschungsergebnisse vor dem Peer-Review-Prozess zu veröffentlichen.",
        "options": ["richtig", "falsch", "nicht im Text"],
        "correctAnswer": "richtig",
        "explanation": "Der Text sagt: 'Forschende stellen Manuskripte vor der Begutachtung online'. Die Aussage entspricht genau dem im Text Beschriebenen."
    },
    {
        "id": "C1_m01_R3_q4",
        "type": "true_false",
        "questionText": "Während der COVID-19-Pandemie wurden Preprints ausschließlich von Fachleuten rezipiert, ohne in der Öffentlichkeit Missverständnisse zu erzeugen.",
        "options": ["richtig", "falsch", "nicht im Text"],
        "correctAnswer": "falsch",
        "explanation": "Der Text stellt explizit fest: 'Vorläufige Ergebnisse ohne Peer Review wurden von Medien aufgegriffen und als gesichertes Wissen dargestellt – mit teils folgenreichen Missverständnissen.' Die Aussage ist eindeutig falsch."
    },
    {
        "id": "C1_m01_R3_q5",
        "type": "true_false",
        "questionText": "In den Geistes- und Sozialwissenschaften werden Open-Data-Normen manchmal als unpassend empfunden.",
        "options": ["richtig", "falsch", "nicht im Text"],
        "correctAnswer": "richtig",
        "explanation": "Der Text beschreibt: 'Viele Geistes- und Sozialwissenschaftler empfinden die aus den MINT-Fächern importierten Open-Science-Normen als kulturfremd.' Die Aussage ist korrekt."
    },
    {
        "id": "C1_m01_R3_q6",
        "type": "true_false",
        "questionText": "Forschende aus einkommensschwachen Ländern können dank Open Access nun kostenfrei sowohl lesen als auch publizieren.",
        "options": ["richtig", "falsch", "nicht im Text"],
        "correctAnswer": "falsch",
        "explanation": "Der Text beschreibt das Gegenteil: 'Für Wissenschaftlerinnen und Wissenschaftler aus dem Globalen Süden…droht Open Access paradoxerweise eine neue Exklusionslogik zu erzeugen: Lesen können nun alle – publizieren nicht.' Die Aussage ist falsch."
    },
    {
        "id": "C1_m01_R3_q7",
        "type": "true_false",
        "questionText": "Plan S schreibt für EU-geförderte Forschung verbindlichen Open-Access-Zugang bis 2025 vor.",
        "options": ["richtig", "falsch", "nicht im Text"],
        "correctAnswer": "richtig",
        "explanation": "Der Text nennt Plan S explizit als Initiative, 'die für geförderte Forschung verbindlichen Open-Access-Zugang bis 2025 vorschreibt'. Die Aussage ist korrekt."
    },
    {
        "id": "C1_m01_R3_q8",
        "type": "true_false",
        "questionText": "Transformationsverträge zwischen Verlagen und Forschungseinrichtungen werden allgemein als Schritt zur echten Öffnung des Wissenschaftssystems begrüßt.",
        "options": ["richtig", "falsch", "nicht im Text"],
        "correctAnswer": "falsch",
        "explanation": "Der Text sagt: 'Ob diese Verträge wirklich zur Öffnung des Systems führen oder lediglich die Erlösmodelle der Verlage sichern, ist unter Bibliothekaren und Wissenschaftlern heftig umstritten.' Allgemeine Begrüßung wird nicht berichtet – vielmehr Kontroverse."
    },
    {
        "id": "C1_m01_R3_q9",
        "type": "true_false",
        "questionText": "Die Open-Science-Bewegung entstand als Reaktion auf die Einführung personalisierter Suchmaschinen im Internet.",
        "options": ["richtig", "falsch", "nicht im Text"],
        "correctAnswer": "nicht im Text",
        "explanation": "Im Text wird kein Bezug zu Suchmaschinen als Entstehungsgrund der Open-Science-Bewegung hergestellt. Die Aussage ist nicht im Text vorhanden."
    },
    {
        "id": "C1_m01_R3_q10",
        "type": "true_false",
        "questionText": "Das aktuelle Geschäftsmodell wissenschaftlicher Verlage entstand in den 1970er Jahren.",
        "options": ["richtig", "falsch", "nicht im Text"],
        "correctAnswer": "richtig",
        "explanation": "Der Text beschreibt: 'Dieses Geschäftsmodell, das in den 1970er Jahren mit dem Aufkommen spezialisierter Fachverlage entstand'. Die Aussage ist korrekt."
    },
    {
        "id": "C1_m01_R3_q11",
        "type": "true_false",
        "questionText": "Open Science scheitert nach Ansicht des Textes vor allem an technologischen Hindernissen.",
        "options": ["richtig", "falsch", "nicht im Text"],
        "correctAnswer": "falsch",
        "explanation": "Der Text nennt am Ende explizit: 'Das ist kein technisches, sondern ein politisches und kulturelles Problem.' Die Behauptung technologischer Hindernisse als Hauptursache ist falsch."
    },
    {
        "id": "C1_m01_R3_q12",
        "type": "mcq",
        "questionText": "Welcher Titel fasst den Artikel am treffendsten zusammen?",
        "options": [
            "a) Open Science: ein vollständig realisiertes Reformmodell für die Wissenschaft",
            "b) Open Science: ein vielversprechendes, aber noch ungelöstes Transformationsprojekt",
            "c) Open Science: warum Transparenz die Reproduzierbarkeitskrise allein nicht lösen kann"
        ],
        "correctAnswer": "b",
        "explanation": "Der Artikel schildert sowohl echte Fortschritte (bioRxiv, Plan S) als auch strukturelle Hindernisse (APCs, disziplinäre Widerstände, politische Komplexität). Der Schluss – 'ein Ideal im Werden' – bestätigt Option b). Option a) ist falsch (der Text beschreibt gerade, was noch nicht gelöst ist). Option c) greift ein Teilargument heraus, trifft aber nicht den Gesamtduktus."
    }
]

# ─────────────────────────────────────────────────────────────────────────────
# SPRACHBAUSTEINE — 22 MCQ-4opt cloze items
# Topic: Wissenschaftsethik und Forschungsverantwortung (~330 words)
# ─────────────────────────────────────────────────────────────────────────────

sprachbausteine_text = """Die Frage, (1) ____ wissenschaftliche Erkenntnisse als gesichert gelten können, lässt sich nicht mit einem einfachen Kriterium beantworten. In der Forschungspraxis gilt gemeinhin das Prinzip der Reproduzierbarkeit: Ein Befund wird erst dann (2) ____ anerkannt, wenn er unter vergleichbaren Bedingungen von unabhängigen Gruppen repliziert werden konnte. Dieses Ideal ist jedoch schwieriger zu (3) ____ als es auf den ersten Blick scheint.

Ein zentrales Problem liegt im sogenannten Publikationsbias, (4) ____ dem negative oder nicht signifikante Ergebnisse kaum Chancen haben, in renommierten Fachzeitschriften zu erscheinen. Wer keine spektakulären Befunde vorweisen kann, riskiert, im akademischen Wettbewerb (5) ____ zu werden. Das verleitet manche Forschende dazu, Daten so lange zu analysieren, bis sich eine scheinbar bedeutsame Korrelation ergibt – ein Vorgehen, das Methodologen als „p-Hacking" (6) ____.

Hinzu kommt, dass Studien häufig mit zu kleinen Stichproben durchgeführt werden, (7) ____ statistische Aussagekraft einzuschränken. Solche Arbeiten können den Peer-Review-Prozess durchlaufen, ohne dass die Gutachter die mangelhafte Power der Studie (8) ____. Erst wenn mehrere Replikationsversuche scheitern, (9) ____ Zweifel an der Solidität des Ausgangsbefunds.

Die Open-Science-Bewegung (10) ____ auf diese Schwächen, indem sie Vorregistrierung, offene Daten und transparente Methoden (11) ____. Kritiker räumen ein, dass mehr Transparenz notwendig, aber nicht (12) ____ sei: Solange Karrieren primär an der Zahl der Veröffentlichungen (13) ____ werden, bleiben die strukturellen Fehlanreize bestehen. Eine tiefergehende Reform (14) ____ daher einen Wandel in den Bewertungskriterien akademischer Leistung (15) ____.

Wissenschaftsethik bedeutet in diesem Kontext nicht nur, Daten nicht zu fälschen. Sie (16) ____ auch, Unsicherheiten offen zu kommunizieren, Limitationen einer Studie transparent zu machen und nicht mehr (17) ____ als tatsächlich belegt ist. Wer als Forschende oder Forscher (18) ____ mit diesem Anspruch nicht auseinandersetzt, schadet letztlich nicht nur der eigenen Glaubwürdigkeit, sondern dem Vertrauen der Öffentlichkeit in die Wissenschaft (19) ____. Eine Kultur der epistemischen Bescheidenheit ist daher keine akademische Tugend unter vielen – sie ist (20) ____ des wissenschaftlichen Projekts selbst. Nur wer bereit ist, die eigenen Befunde (21) ____ zu hinterfragen, kann zur Akkumulation verlässlichen Wissens (22) ____."""

sprachbausteine_questions = [
    {
        "blankNumber": 1,
        "type": "mcq",
        "options": ["ob", "wann", "als", "weil"],
        "correctAnswer": "ob",
        "explanation": "'ob' leitet einen indirekten Fragesatz ein, der die Frage paraphrasiert, wann etwas als gesichert gilt. 'wann' wäre grammatisch möglich, aber semantisch ungenau – es fragt nach einem Zeitpunkt, nicht nach einer Bedingung. 'als' und 'weil' passen syntaktisch nicht in einen dass-losen Fragesatz."
    },
    {
        "blankNumber": 2,
        "type": "mcq",
        "options": ["breit", "kaum", "selten", "vorläufig"],
        "correctAnswer": "breit",
        "explanation": "'breit anerkannt' ist das gebräuchliche Kollokationsmuster im wissenschaftlichen Register (breite Anerkennung, breit rezipiert). 'kaum' und 'selten' wären semantisch falsch (der Kontext beschreibt eine positive Bedingung). 'vorläufig anerkannt' wäre grammatisch möglich, widerspricht aber dem Kontext – Reproduzierbarkeit führt zu dauerhafter, nicht vorläufiger Anerkennung."
    },
    {
        "blankNumber": 3,
        "type": "mcq",
        "options": ["verwirklichen", "widerlegen", "entwickeln", "verstehen"],
        "correctAnswer": "verwirklichen",
        "explanation": "'verwirklichen' passt zur Aussage, dass das Reproduzierbarkeitsideal schwer in die Praxis umzusetzen ist. 'widerlegen' wäre semantisch falsch (das Ideal wird nicht widerlegt, sondern die Umsetzung ist schwierig). 'entwickeln' und 'verstehen' passen nicht zum Kontext der praktischen Realisierung."
    },
    {
        "blankNumber": 4,
        "type": "mcq",
        "options": ["dem zufolge", "wonach", "wobei", "anhand dessen"],
        "correctAnswer": "wonach",
        "explanation": "'wonach' ist das korrekte Relativpronomen für einen Relativsatz, der sich auf den Publikationsbias bezieht und ihn charakterisiert ('wonach negative Ergebnisse kaum Chancen haben'). 'dem zufolge' wäre ein Evidenzmarker, nicht ein Relativpronomen. 'wobei' leitet einen Begleitsatz ein, nicht eine Relativcharakterisierung. 'anhand dessen' ist eine Präpositionalphrase, kein Relativpronomen."
    },
    {
        "blankNumber": 5,
        "type": "mcq",
        "options": ["übergangen", "überholt", "überarbeitet", "übernommen"],
        "correctAnswer": "übergangen",
        "explanation": "'übergangen werden' bedeutet im akademischen Kontext, nicht berücksichtigt/ignoriert zu werden – passend für das akademische Wettbewerbsszenario. 'überholt werden' bezieht sich auf technisches Veralten. 'überarbeitet' und 'übernommen' passen semantisch nicht."
    },
    {
        "blankNumber": 6,
        "type": "mcq",
        "options": ["bezeichnen", "kritisieren", "benennen", "ablehnen"],
        "correctAnswer": "bezeichnen",
        "explanation": "'als X bezeichnen' ist die korrekte Kollokation für Terminologieeinführung im Fachregister. 'kritisieren' wäre inhaltlich vertretbar, aber nicht als Terminus-Einführung geeignet. 'benennen' wäre ohne 'als' korrekt; mit 'als' ist 'bezeichnen' idiomatischer. 'ablehnen' passt semantisch nicht."
    },
    {
        "blankNumber": 7,
        "type": "mcq",
        "options": ["um deren", "ohne deren", "wodurch deren", "was deren"],
        "correctAnswer": "um deren",
        "explanation": "'um … einzuschränken' ist die korrekte Konstruktion ('zu kleinen Stichproben, um deren statistische Aussagekraft einzuschränken'). 'ohne deren' würde eine Infinitivkonstruktion ohne Bezug benötigen. 'wodurch deren' leitet keinen Infinitivsatz ein. 'was deren' ist grammatisch nicht wohlgeformt."
    },
    {
        "blankNumber": 8,
        "type": "mcq",
        "options": ["erkennen", "bemerken", "durchschauen", "aufdecken"],
        "correctAnswer": "erkennen",
        "explanation": "'erkennen' ist im wissenschaftlichen Register die neutrale, idiomatisch passende Wahl für 'als Gutachter einen Mangel wahrnehmen'. 'bemerken' wäre umgangssprachlicher. 'durchschauen' impliziert Täuschungsabsicht, die im Kontext nicht erwähnt wird. 'aufdecken' setzt gezielte Untersuchung voraus."
    },
    {
        "blankNumber": 9,
        "type": "mcq",
        "options": ["entstehen", "wachsen", "erheben sich", "mehren sich"],
        "correctAnswer": "mehren sich",
        "explanation": "'Zweifel mehren sich' ist eine gebräuchliche Kollokation im journalistisch-akademischen Register. 'entstehen' wäre zu abrupt – Zweifel entstehen nicht schlagartig, sondern akkumulieren. 'wachsen' ist möglich, aber weniger präzise als 'mehren'. 'erheben sich' klingt forciert-literarisch."
    },
    {
        "blankNumber": 10,
        "type": "mcq",
        "options": ["reagiert", "antwortet", "zielt", "richtet sich"],
        "correctAnswer": "reagiert",
        "explanation": "'reagiert auf' ist die korrekte Präpositionalrektion. 'antwortet auf' wäre grammatisch vertretbar, aber weniger idiomatisch für institutionelle Bewegungen. 'zielt auf' erfordert ein Objekt ohne 'auf diese Schwächen'. 'richtet sich gegen' würde eine Gegnerschaft implizieren."
    },
    {
        "blankNumber": 11,
        "type": "mcq",
        "options": ["einfordert", "verspricht", "ermöglicht", "beschreibt"],
        "correctAnswer": "einfordert",
        "explanation": "'einfordern' bedeutet aktiv verlangen/fordern – korrekt für eine Bewegung, die Transparenz als Norm verlangt. 'verspricht' wäre semantisch falsch (eine Bewegung gibt keine Versprechen im üblichen Sinne). 'ermöglicht' ist zu passiv. 'beschreibt' beschreibt nur, statt einen Forderungscharakter auszudrücken."
    },
    {
        "blankNumber": 12,
        "type": "mcq",
        "options": ["hinreichend", "ausreichend", "notwendig", "sinnvoll"],
        "correctAnswer": "hinreichend",
        "explanation": "Im logischen Kontext ('notwendig, aber nicht hinreichend') ist 'hinreichend' der korrekte philosophisch-logische Terminus. 'ausreichend' wäre umgangssprachliches Synonym, aber im akademischen Register ist 'hinreichend' die korrekte Wahl. 'notwendig' und 'sinnvoll' widersprechen dem Kontext."
    },
    {
        "blankNumber": 13,
        "type": "mcq",
        "options": ["gemessen", "bewertet", "beurteilt", "eingeschätzt"],
        "correctAnswer": "gemessen",
        "explanation": "'an der Zahl gemessen werden' ist die korrekte Kollokation im Bewertungskontext ('Karrieren, die an Publikationszahlen gemessen werden'). 'bewertet' und 'beurteilt' sind semantisch nahe, aber 'messen' ist im Kontext von Leistungsmetriken idiomatischer. 'eingeschätzt' ist zu subjektiv."
    },
    {
        "blankNumber": 14,
        "type": "mcq",
        "options": ["erfordert", "ermöglicht", "bedingt", "impliziert"],
        "correctAnswer": "erfordert",
        "explanation": "'erfordert' (im Sinne von 'macht notwendig') ist die korrekte Wahl für strukturelle Notwendigkeiten in akademischem Register. 'bedingt' wäre semantisch möglich, klingt aber antiquierter. 'ermöglicht' wäre semantisch falsch. 'impliziert' ist zu schwach für eine notwendige Bedingung."
    },
    {
        "blankNumber": 15,
        "type": "mcq",
        "options": ["voraus", "vorüber", "voran", "vorbei"],
        "correctAnswer": "voraus",
        "explanation": "'erfordert … voraus' ergänzt das Trennverb 'voraussetzen': 'Eine Reform setzt einen Wandel voraus'. Dies ist die idiomatische Verbalkonstruktion. 'vorüber', 'voran', 'vorbei' ergeben keinen semantischen Sinn mit 'setzen' im Reformkontext."
    },
    {
        "blankNumber": 16,
        "type": "mcq",
        "options": ["bedeutet", "verlangt", "umfasst", "beinhaltet"],
        "correctAnswer": "umfasst",
        "explanation": "'umfasst auch' signalisiert, dass Wissenschaftsethik mehr als Datenfälschungsvermeidung einschließt. 'bedeutet' wäre semantisch möglich, aber 'umfasst' ist passender für eine Erweiterung einer Definition. 'verlangt' wäre im Kontext zu stark normativ. 'beinhaltet' ist Synonym zu 'umfasst', aber 'umfasst' ist im akademischen Register stilistisch bevorzugt."
    },
    {
        "blankNumber": 17,
        "type": "mcq",
        "options": ["zu behaupten", "zu fordern", "zu versprechen", "zu erwarten"],
        "correctAnswer": "zu behaupten",
        "explanation": "'nicht mehr zu behaupten als tatsächlich belegt ist' ist die korrekte Konstruktion für das Prinzip epistemischer Bescheidenheit. 'zu fordern' wäre zu aktivistisch. 'zu versprechen' passt nicht ins Wissensanspruchs-Register. 'zu erwarten' ändert die Bedeutung grundlegend."
    },
    {
        "blankNumber": 18,
        "type": "mcq",
        "options": ["sich ernsthaft", "sich kaum", "sich scheinbar", "sich angeblich"],
        "correctAnswer": "sich ernsthaft",
        "explanation": "'sich ernsthaft auseinandersetzen' bedeutet sich aufrichtig und gründlich mit einem Thema befassen – korrekte Kollokation im Kontext wissenschaftlicher Verantwortungsethik. 'sich kaum auseinandersetzen' würde eine negative Implikation erzeugen, die den Satz falsch macht. 'scheinbar' und 'angeblich' sind Evidenzmarker, keine Adverbien der Intensität."
    },
    {
        "blankNumber": 19,
        "type": "mcq",
        "options": ["insgesamt", "gegenüber", "überhaupt", "letztendlich"],
        "correctAnswer": "gegenüber",
        "explanation": "'das Vertrauen der Öffentlichkeit in die Wissenschaft gegenüber' ergänzt die Kollokation 'schaden + Dat.': 'schadet … der Öffentlichkeit gegenüber' – hier ist 'gegenüber' Nachstellung für das Dativobjekt. C1-Falle: 'insgesamt' und 'überhaupt' modifizieren den Satz adverbial, ändern aber nicht die Valenz von 'schaden'."
    },
    {
        "blankNumber": 20,
        "type": "mcq",
        "options": ["Grundbedingung", "Begleiterscheinung", "Nebenwirkung", "Voraussetzung"],
        "correctAnswer": "Voraussetzung",
        "explanation": "'Voraussetzung des wissenschaftlichen Projekts' bedeutet, dass ohne epistemische Bescheidenheit Wissenschaft als Erkenntnisunternehmen nicht funktioniert. 'Grundbedingung' wäre semantisch ähnlich, aber 'Voraussetzung' ist im Kontext von logischen Bedingungen präziser. 'Begleiterscheinung' und 'Nebenwirkung' implizieren Zufälligkeit, nicht Notwendigkeit."
    },
    {
        "blankNumber": 21,
        "type": "mcq",
        "options": ["kritisch", "deutlich", "ausdrücklich", "gründlich"],
        "correctAnswer": "kritisch",
        "explanation": "'kritisch hinterfragen' ist die feste Kollokation im wissenschaftlich-epistemischen Register. 'deutlich hinterfragen' klingt umgangssprachlich. 'ausdrücklich' passt nicht als Adverb zu 'hinterfragen'. 'gründlich hinterfragen' wäre möglich, aber 'kritisch' ist die Standardkollokation."
    },
    {
        "blankNumber": 22,
        "type": "mcq",
        "options": ["beitragen", "verhelfen", "leisten", "dienen"],
        "correctAnswer": "beitragen",
        "explanation": "'zur Akkumulation verlässlichen Wissens beitragen' ist die idiomatische Kollokation. 'verhelfen' benötigt ein Dativobjekt + Infinitiv ('jemandem dazu verhelfen'). 'leisten' würde einen direkten Akkusativ brauchen. 'dienen' ('dient der Akkumulation') wäre grammatisch möglich, aber schwächer im Reformduktus."
    }
]

# ─────────────────────────────────────────────────────────────────────────────
# LISTENING
# ─────────────────────────────────────────────────────────────────────────────

# HV Teil 1 — 8 speakers, 10 summary statements, 8 correct + 2 distractors
# Speaker summaries (a-j, 8 correct answers + 2 distractors)
# Topic: Reproduzierbarkeitskrise und Forschungsqualität — Kurzaussagen

hv1_summaries = [
    {"id": "C1_m01_HV1_sum_a", "label": "a", "content": "a) Die Sprecherin hält offene Forschungsdaten für ein wirksames Mittel, um Manipulation vorzubeugen."},
    {"id": "C1_m01_HV1_sum_b", "label": "b", "content": "b) Der Sprecher findet, dass Wissenschaftler mit negativen Ergebnissen benachteiligt werden."},
    {"id": "C1_m01_HV1_sum_c", "label": "c", "content": "c) Die Sprecherin ist skeptisch, ob Vorregistrierung allein das Verhalten von Forschenden wirklich verändert."},
    {"id": "C1_m01_HV1_sum_d", "label": "d", "content": "d) Der Sprecher glaubt, dass Peer Review ein grundsätzlich zuverlässiges System ist, das nur besser finanziert werden müsste."},
    {"id": "C1_m01_HV1_sum_e", "label": "e", "content": "e) Die Sprecherin fordert, dass Forschungsergebnisse nur dann publiziert werden sollten, wenn sie dreifach repliziert wurden."},
    {"id": "C1_m01_HV1_sum_f", "label": "f", "content": "f) Der Sprecher sieht in der Reproduzierbarkeitskrise hauptsächlich ein Problem einzelner unehrlicher Forscher, nicht des Systems."},
    {"id": "C1_m01_HV1_sum_g", "label": "g", "content": "g) Die Sprecherin plädiert dafür, dass Karrierefortschritt stärker an Replikationsstudien gebunden werden sollte."},
    {"id": "C1_m01_HV1_sum_h", "label": "h", "content": "h) Der Sprecher sieht in KI-gestützten Analysen ein Risiko, das vorhandene Verzerrungen in der Literatur verstärken kann."},
    {"id": "C1_m01_HV1_sum_i", "label": "i", "content": "i) Die Sprecherin betont, dass Medien eine Mitverantwortung tragen, wenn Preprints als gesicherte Erkenntnisse dargestellt werden."},
    {"id": "C1_m01_HV1_sum_j", "label": "j", "content": "j) Der Sprecher findet, dass Open Science in kleinen Forschungseinrichtungen kaum umsetzbar ist."},
]

hv1_questions = [
    {
        "id": "C1_m01_HV1_q1",
        "type": "matching",
        "questionText": "Sprecher 1: Frau Dr. Kettner, Wissenschaftsforscherin",
        "matchingSources": hv1_summaries,
        "correctAnswer": "a",
        "explanation": "Frau Dr. Kettner sagt: 'Wenn Daten frei zugänglich sind und jederzeit nachgeprüft werden können, wird es für einzelne viel schwieriger, Ergebnisse zu manipulieren. Offenheit ist ein struktureller Schutz.' Das entspricht Zusammenfassung a). Distraktor g) klingt ähnlich, bezieht sich aber auf Karriereregeln, nicht auf Offenheit als Manipulationsschutz."
    },
    {
        "id": "C1_m01_HV1_q2",
        "type": "matching",
        "questionText": "Sprecher 2: Herr Prof. Steinmann, Methodik-Experte",
        "matchingSources": hv1_summaries,
        "correctAnswer": "b",
        "explanation": "Prof. Steinmann betont: 'Ein Artikel über eine fehlgeschlagene Replikation hat kaum Aussichten auf Publikation in einem renommierten Journal. Das System bestraft Forscher, die zeigen, dass etwas nicht stimmt.' Das trifft genau Zusammenfassung b) über die Benachteiligung bei negativen Ergebnissen."
    },
    {
        "id": "C1_m01_HV1_q3",
        "type": "matching",
        "questionText": "Sprecher 3: Frau Prof. Wahl, Wissenschaftsphilosophin",
        "matchingSources": hv1_summaries,
        "correctAnswer": "c",
        "explanation": "Frau Prof. Wahl sagt: 'Vorregistrierung ist ein guter Anfang, aber man darf sich nicht in falscher Sicherheit wiegen. Solange die Bewertungslogik dieselbe bleibt, werden Forscher Wege finden, das System zu umgehen.' Das entspricht c) – Skepsis gegenüber Vorregistrierung als alleiniger Lösung."
    },
    {
        "id": "C1_m01_HV1_q4",
        "type": "matching",
        "questionText": "Sprecher 4: Herr Dr. Berger, Fachzeitschriften-Herausgeber",
        "matchingSources": hv1_summaries,
        "correctAnswer": "d",
        "explanation": "Dr. Berger argumentiert: 'Peer Review ist im Kern das Beste, was wir haben. Das Problem ist nicht das Verfahren, sondern dass Gutachter ehrenamtlich arbeiten und irgendwann erschöpft sind. Investitionen ins System würden viel bewirken.' Das entspricht d) – Verteidigung des Peer Review als zuverlässiges, aber unterfinanziertes System."
    },
    {
        "id": "C1_m01_HV1_q5",
        "type": "matching",
        "questionText": "Sprecher 5: Frau Dr. Reuter, Forschungsberaterin",
        "matchingSources": hv1_summaries,
        "correctAnswer": "g",
        "explanation": "Dr. Reuter sagt: 'Wir müssen aufhören, Karrieren fast ausschließlich an Erstveröffentlichungen zu messen. Wer Replikationsstudien durchführt, leistet wissenschaftlich wertvolle Arbeit und sollte dafür auch belohnt werden.' Das entspricht g) – Karrierefortschritt an Replikationsstudien knüpfen."
    },
    {
        "id": "C1_m01_HV1_q6",
        "type": "matching",
        "questionText": "Sprecher 6: Herr Dr. Schwarz, KI-Forscher",
        "matchingSources": hv1_summaries,
        "correctAnswer": "h",
        "explanation": "Dr. Schwarz warnt: 'KI-Systeme lernen aus der vorhandenen Literatur. Wenn diese Literatur selektiv ist und positive Ergebnisse überrepräsentiert, dann reproduziert die KI genau diese Verzerrung in ihren Analysen und Empfehlungen.' Das entspricht h) – KI verstärkt bestehende Verzerrungen."
    },
    {
        "id": "C1_m01_HV1_q7",
        "type": "matching",
        "questionText": "Sprecher 7: Frau Lanz, Wissenschaftsjournalistin",
        "matchingSources": hv1_summaries,
        "correctAnswer": "i",
        "explanation": "Frau Lanz betont: 'Als Journalistin sage ich: Wir haben Fehler gemacht. Wir haben Preprints zitiert als wären es peer-reviewte Artikel. Das ist irreführend, und wir als Medien müssen da klarer kommunizieren.' Das entspricht i) – Medien tragen Mitverantwortung beim Umgang mit Preprints."
    },
    {
        "id": "C1_m01_HV1_q8",
        "type": "matching",
        "questionText": "Sprecher 8: Herr Prof. Nkemdirim, Entwicklungsländer-Forscher",
        "matchingSources": hv1_summaries,
        "correctAnswer": "j",
        "explanation": "Prof. Nkemdirim sagt: 'Open Science klingt schön in einem gut ausgestatteten europäischen Labor. Aber in meiner Universität in Lagos fehlen die technischen Ressourcen, um eigene Server zu betreiben oder APCs zu zahlen. Für uns ist das nicht umsetzbar.' Das entspricht j) – Open Science kaum realisierbar für kleine/ressourcenschwache Einrichtungen."
    }
]

# HV Teil 2 — 10 MCQ-3opt items — Radiointerview
# Topic: Hochschule und hybride Lehre — Interview mit Wissenschaftsforscherin

hv2_questions = [
    {
        "id": "C1_m01_HV2_q1",
        "type": "mcq",
        "questionText": "Was ist laut Prof. Dr. Hagedorn die ursprüngliche Funktion der Universität, die durch Digitalisierung am stärksten unter Druck gerät?",
        "options": [
            "a) Die Verwaltung von Prüfungsleistungen und Creditpoints",
            "b) Die Funktion als Ort des lebendigen intellektuellen Austauschs",
            "c) Die Organisation internationaler Forschungsverbünde"
        ],
        "correctAnswer": "b",
        "explanation": "Prof. Dr. Hagedorn betont: 'Was eine Universität von einem Fernstudienportal unterscheidet, ist der lebendige intellektuelle Austausch – Diskussionen im Seminar, zufällige Gespräche im Flur, das Ringen um Argumente in Echtzeit. Genau das gerät durch reine Onlinelehre unter Druck.' Option a) und c) werden im Interview zwar erwähnt, aber nicht als die unter Druck geratene Kernfunktion identifiziert."
    },
    {
        "id": "C1_m01_HV2_q2",
        "type": "mcq",
        "questionText": "Was sagt Prof. Dr. Hagedorn über die Lernergebnisse reiner Online-Lehre im Vergleich zu Präsenzlehre?",
        "options": [
            "a) Online-Lernergebnisse sind grundsätzlich schlechter als in der Präsenz.",
            "b) Die Lernergebnisse sind vergleichbar, wenn bestimmte didaktische Bedingungen erfüllt sind.",
            "c) Online-Kurse führen erwiesenermaßen zu höherem Lernerfolg, weil Studierende ihr Tempo selbst bestimmen."
        ],
        "correctAnswer": "b",
        "explanation": "Hagedorn differenziert: 'Die Metaanalysen zeigen: Wenn Online-Lehre gut konzipiert ist, mit klaren Lernzielen, aktivem Feedback und sozialer Einbindung, sind die Lernergebnisse durchaus vergleichbar mit Präsenzformaten.' Sie lehnt pauschale Urteile in beide Richtungen ab. Option a) übertreibt, Option c) dreht die Kausallogik um."
    },
    {
        "id": "C1_m01_HV2_q3",
        "type": "mcq",
        "questionText": "Welches Hauptproblem sieht Prof. Dr. Hagedorn bei der derzeitigen Umsetzung hybrider Lehre?",
        "options": [
            "a) Dozierende werden nicht ausreichend für digitale Werkzeuge geschult.",
            "b) Hybride Modelle werden oft als Kompromisslösung statt als eigenständiges Format entwickelt.",
            "c) Studierende bevorzugen reine Präsenzlehre und akzeptieren hybride Formate nicht."
        ],
        "correctAnswer": "b",
        "explanation": "Hagedorn sagt: 'Das Grundproblem ist, dass hybride Lehre meist als Notlösung entstand – man schaltet einfach eine Kamera dazu und hofft, dass das reicht. Hybrides Unterrichten ist aber eine eigene didaktische Disziplin.' Option a) wird am Rande erwähnt, ist aber nicht das Hauptproblem laut Hagedorn. Option c) ist falsch – Studierende werden als durchaus offen für Hybridformate beschrieben."
    },
    {
        "id": "C1_m01_HV2_q4",
        "type": "mcq",
        "questionText": "Was empfiehlt Prof. Dr. Hagedorn bezüglich der Präsenzpflicht?",
        "options": [
            "a) Präsenzpflicht sollte vollständig abgeschafft werden, da sie kontraproduktiv ist.",
            "b) Präsenzpflicht ist sinnvoll, aber nur für interaktive Lehrformate, nicht für Vorlesungen.",
            "c) Präsenzpflicht sollte für alle Lehrformate beibehalten werden, um soziale Kohäsion zu sichern."
        ],
        "correctAnswer": "b",
        "explanation": "Hagedorn erklärt: 'Eine Vorlesung, die ich auch als Aufzeichnung oder Podcast konsumieren könnte, hat keine starke Begründung für Präsenzpflicht. Aber ein Seminar, das von Diskussion lebt, oder ein Praktikum – da ist Anwesenheit nicht optional.' Sie differenziert nach Format, empfiehlt weder vollständige Abschaffung noch flächendeckende Pflicht."
    },
    {
        "id": "C1_m01_HV2_q5",
        "type": "mcq",
        "questionText": "Was sagt Hagedorn über den Zusammenhang zwischen hybrider Lehre und sozioökonomischer Benachteiligung?",
        "options": [
            "a) Hybride Lehre schafft mehr Gerechtigkeit, weil Studierende aus einkommensschwachen Familien Pendelkosten sparen.",
            "b) Hybride Lehre kann bestehende Ungleichheiten verstärken, wenn nicht alle Studierenden gleichen Zugang zu technischer Ausstattung haben.",
            "c) Die Frage der Zugangsgerechtigkeit spielt bei hybrider Lehre keine wesentliche Rolle."
        ],
        "correctAnswer": "b",
        "explanation": "Hagedorn sagt: 'Wir dürfen nicht vergessen, dass nicht alle Studierenden zu Hause gute Internetverbindungen, ruhige Arbeitsplätze oder aktuelle Laptops haben. Hybride Lehre kann bestehende Ungleichheiten verschärfen, wenn wir das ignorieren.' Option a) greift einen möglichen Vorteil auf, ist aber nicht Hagedorns Hauptaussage. Option c) widerspricht dem Interview direkt."
    },
    {
        "id": "C1_m01_HV2_q6",
        "type": "mcq",
        "questionText": "Was sagt Hagedorn über die Bewertung von Lehrqualität an deutschen Hochschulen?",
        "options": [
            "a) Lehrqualität wird an deutschen Hochschulen bereits systematisch und konsequent bewertet.",
            "b) Studentische Lehrevaluationen allein sind kein ausreichendes Instrument zur Qualitätssicherung.",
            "c) Forschungsleistung sollte vollständig von Lehrleistung getrennt bewertet werden."
        ],
        "correctAnswer": "b",
        "explanation": "Hagedorn kritisiert: 'Studentische Evaluationen messen oft eher Zufriedenheit als Lernerfolg. Ob Studierende tatsächlich kompetenter wurden, lässt sich damit kaum erfassen. Wir brauchen differenziertere Instrumente.' Sie lehnt Evaluationen nicht ab, hält sie aber für unzureichend. Optionen a) und c) decken sich nicht mit Hagedorns Aussagen."
    },
    {
        "id": "C1_m01_HV2_q7",
        "type": "mcq",
        "questionText": "Welche Rolle schreibt Hagedorn dem Peer Learning in gut gestalteter hybrider Lehre zu?",
        "options": [
            "a) Peer Learning ist in hybriden Formaten kaum realisierbar und sollte auf Präsenzphasen beschränkt bleiben.",
            "b) Peer Learning ist ein zentrales Element, das hybride Formate besonders effektiv machen kann.",
            "c) Peer Learning wird im Interview als überbewertet eingestuft."
        ],
        "correctAnswer": "b",
        "explanation": "Hagedorn erklärt: 'Peer Learning – also das voneinander Lernen in kleinen Gruppen – funktioniert in Hybridformaten erstaunlich gut, wenn man es bewusst einsetzt. Digitale Kollaborationstools können Gruppenarbeit sogar intensiver gestalten als im Präsenzraum.' Option a) widerspricht dieser Aussage. Option c) ist das Gegenteil von dem, was Hagedorn sagt."
    },
    {
        "id": "C1_m01_HV2_q8",
        "type": "mcq",
        "questionText": "Wie bewertet Hagedorn die Rolle von KI-Assistenten im Lernprozess?",
        "options": [
            "a) KI-Assistenten sollten aus Hochschulkontexten grundsätzlich verbannt werden.",
            "b) KI kann sinnvoll eingesetzt werden, birgt aber die Gefahr, eigenständiges Denken zu untergraben.",
            "c) KI-Assistenten sind uneingeschränkt positiv für den Lernprozess."
        ],
        "correctAnswer": "b",
        "explanation": "Hagedorn differenziert: 'Ich sehe KI als Werkzeug, das Studierenden helfen kann – etwa beim Strukturieren oder bei Recherchen. Aber wenn KI immer stärker das Denken übernimmt, das Studierenden eigentlich selbst leisten sollten, verlieren wir einen wesentlichen Teil des Lernprozesses.' Sie plädiert für differenzierten Einsatz, nicht für Verbot oder uneingeschränkten Einsatz."
    },
    {
        "id": "C1_m01_HV2_q9",
        "type": "mcq",
        "questionText": "Was sagt Hagedorn über internationale Erfahrungen mit Online- und Hybridlehre?",
        "options": [
            "a) Deutsche Hochschulen sind im internationalen Vergleich Vorreiter bei digitaler Lehre.",
            "b) Im internationalen Vergleich haben deutsche Hochschulen erheblichen Nachholbedarf.",
            "c) Internationale Erfahrungen sind wegen struktureller Unterschiede kaum auf Deutschland übertragbar."
        ],
        "correctAnswer": "b",
        "explanation": "Hagedorn stellt fest: 'Wenn ich mir anschaue, was Hochschulen in Kanada, den Niederlanden oder Australien in den letzten zehn Jahren an digitalen Lehrkonzepten entwickelt haben, dann müssen wir in Deutschland ehrlich sagen: Wir haben deutlich Nachholbedarf.' Option a) widerspricht dieser Einschätzung. Option c) wird nicht als Hagedorns Position beschrieben."
    },
    {
        "id": "C1_m01_HV2_q10",
        "type": "mcq",
        "questionText": "Was ist Hagedorns abschließende Forderung?",
        "options": [
            "a) Alle Lehrveranstaltungen sollten mittelfristig vollständig ins Digitale verlagert werden.",
            "b) Hochschulen sollten hybride Lehre als eigenständige Kompetenz systematisch aufbauen und fördern.",
            "c) Entscheidungen über Lehrformat sollten ausschließlich Studierenden überlassen werden."
        ],
        "correctAnswer": "b",
        "explanation": "Hagedorn schließt: 'Was ich mir wünsche, ist, dass hybride Lehre nicht mehr als Notlösung, sondern als echte Kompetenz verstanden wird – eine Kompetenz, in die Hochschulen investieren, Dozierende ausbilden und Studierende von Anfang an einbinden.' Option a) widerspricht ihrer differenzierten Haltung. Option c) wird nicht als Forderung formuliert."
    }
]

# HV Teil 3 — Vortrag mit Folien — Forschungsmethoden und Reproduzierbarkeit
# 5 slides with 2 gaps each = 10 gap-fill items, continuous audio

hv3_slides = [
    {
        "slideNumber": 1,
        "title": "Was ist Reproduzierbarkeit?",
        "content": "Definition: Fähigkeit, unter gleichen Bedingungen zu identischen Ergebnissen zu gelangen\n- Analytische Reproduzierbarkeit: gleiche Daten, gleiche Methode → gleiche Ergebnisse\n- Empirische Reproduzierbarkeit: Neuerhebung der Daten → vergleichbare Befunde\nGap 1: ______ (Anteil reproduzierbarer Studien laut 2015-Großstudie)\nGap 2: ______ (Betroffene Disziplin mit dem meisten Aufsehen)"
    },
    {
        "slideNumber": 2,
        "title": "Ursachen der Krise",
        "content": "Strukturelle Fehlanreize:\n- Publish-or-Perish: Karriere hängt von Publikationszahl ab\n- Negativergebnisse: kaum publizierbar\n- Gap 3: ______ (Bezeichnung für gezieltes Datenmining bis zur Signifikanz)\nMenschliche Faktoren:\n- Bestätigungsfehler (confirmation bias)\n- Gap 4: ______ (Bezeichnung für unbewusste Selektion günstiger Daten)"
    },
    {
        "slideNumber": 3,
        "title": "Open Science als Antwort",
        "content": "Vier Kernprinzipien:\n1. Open Access — freier Zugang zu Publikationen\n2. Open Data — Gap 5: ______ (was offen sein soll)\n3. Open Methods — Dokumentation von Labormethoden und Skripten\n4. Gap 6: ______ (viertes Kernprinzip)"
    },
    {
        "slideNumber": 4,
        "title": "Vorregistrierung — Ablauf",
        "content": "Schritte der Studie:\n1. Forschungsfrage formulieren\n2. Hypothesen festlegen\n3. Gap 7: ______ (was vor der Datenerhebung öffentlich eingetragen wird)\n4. Daten erheben und auswerten\n5. Abweichungen vom Plan: Gap 8: ______ (wie Abweichungen im Artikel zu behandeln sind)"
    },
    {
        "slideNumber": 5,
        "title": "Herausforderungen und Ausblick",
        "content": "Verbleibende Probleme:\n- APC-Modell trifft Forschende aus dem Gap 9: ______ besonders hart\n- Open Data in Geistes-/Sozialwissenschaften: Gap 10: ______ (Haupthindernis)\nAusblick: Reform der Bewertungslogik als entscheidende Stellschraube"
    }
]

hv3_questions = [
    {
        "id": "C1_m01_HV3_q1",
        "type": "true_false",
        "questionText": "Folie 1 / Lücke 1: Anteil reproduzierbarer Studien laut der 2015-Großstudie",
        "options": ["36 Prozent", "60 Prozent", "unter 20 Prozent", "etwa die Hälfte"],
        "correctAnswer": "36 Prozent",
        "explanation": "Der Vortragende sagt: 'Die Studie der Open Science Collaboration aus dem Jahr 2015 zeigte, dass lediglich 36 Prozent der 100 untersuchten Studien replizierbar waren.' Der Wert 36 Prozent ist klar im Vortrag genannt und muss in die Folie eingetragen werden."
    },
    {
        "id": "C1_m01_HV3_q2",
        "type": "true_false",
        "questionText": "Folie 1 / Lücke 2: Betroffene Disziplin mit dem meisten Aufsehen",
        "options": ["Psychologie", "Medizin", "Wirtschaftswissenschaften", "Soziologie"],
        "correctAnswer": "Psychologie",
        "explanation": "Der Vortragende erklärt: 'Obwohl die Krise alle empirischen Wissenschaften betrifft, war es die Psychologie, die das meiste öffentliche Aufsehen erregte, weil die ursprüngliche 2015-Studie ausschließlich psychologische Experimente reprizierte.' Die Antwort ist Psychologie."
    },
    {
        "id": "C1_m01_HV3_q3",
        "type": "true_false",
        "questionText": "Folie 2 / Lücke 3: Fachbegriff für gezieltes Datenmining bis zur Signifikanz",
        "options": ["p-Hacking", "Data Mining", "Cherrypicking", "HARKing"],
        "correctAnswer": "p-Hacking",
        "explanation": "Der Vortragende nennt: 'Dieses Verhalten, Daten so lange auszuprobieren, bis p unter 0,05 fällt, wird in der Methodenliteratur als p-Hacking bezeichnet.' Der Fachbegriff p-Hacking ist explizit im Vortrag genannt."
    },
    {
        "id": "C1_m01_HV3_q4",
        "type": "true_false",
        "questionText": "Folie 2 / Lücke 4: Bezeichnung für unbewusste Selektion günstiger Daten",
        "options": ["HARKing", "Selektionsbias", "Nullhypothese", "Konfundierung"],
        "correctAnswer": "HARKing",
        "explanation": "Der Vortragende erläutert: 'Ein verwandtes Phänomen ist das sogenannte HARKing – Hypothesizing After Results Known. Man formuliert die Hypothese erst, nachdem man die Ergebnisse kennt, als hätte man sie vorher aufgestellt.' HARKing ist die im Vortrag genannte Bezeichnung für diese Praxis."
    },
    {
        "id": "C1_m01_HV3_q5",
        "type": "true_false",
        "questionText": "Folie 3 / Lücke 5: Was bei Open Data offen sein soll",
        "options": ["Rohdaten der Studie", "Literaturliste", "Peer-Review-Berichte", "Forschungsanträge"],
        "correctAnswer": "Rohdaten der Studie",
        "explanation": "Der Vortragende sagt: 'Open Data bedeutet, dass die erhobenen Rohdaten einer Studie öffentlich zugänglich gemacht werden, damit Dritte sie nachprüfen oder für eigene Analysen verwenden können.' Rohdaten der Studie ist die korrekte Antwort."
    },
    {
        "id": "C1_m01_HV3_q6",
        "type": "true_false",
        "questionText": "Folie 3 / Lücke 6: Viertes Kernprinzip von Open Science",
        "options": ["Open Peer Review", "Open Source", "Open Budget", "Open Curriculum"],
        "correctAnswer": "Open Peer Review",
        "explanation": "Der Vortragende zählt auf: 'Und schließlich das vierte Prinzip: Open Peer Review – die Öffnung des Begutachtungsprozesses, sei es durch die Publikation der Gutachten oder durch das Nennen der Gutachternamen.' Open Peer Review ist das vierte genannte Prinzip."
    },
    {
        "id": "C1_m01_HV3_q7",
        "type": "true_false",
        "questionText": "Folie 4 / Lücke 7: Was vor der Datenerhebung öffentlich eingetragen wird",
        "options": ["Hypothesen und Analysemethoden", "Literaturliste", "Förderantragsbudget", "Ethikvotum"],
        "correctAnswer": "Hypothesen und Analysemethoden",
        "explanation": "Der Vortragende erklärt: 'Im Schritt der Vorregistrierung tragen Forschende ihre Hypothesen und geplanten Analysemethoden in ein öffentliches Register ein, bevor sie die erste Datenerhebung beginnen.' Hypothesen und Analysemethoden ist die korrekte Antwort."
    },
    {
        "id": "C1_m01_HV3_q8",
        "type": "true_false",
        "questionText": "Folie 4 / Lücke 8: Wie Abweichungen vom Studienplan im Artikel zu behandeln sind",
        "options": ["transparent zu berichten", "zu verschweigen", "in einem Anhang zu verstecken", "nach Rücksprache mit Verlag zu entscheiden"],
        "correctAnswer": "transparent zu berichten",
        "explanation": "Der Vortragende sagt: 'Wenn Forschende im Verlauf der Studie von ihrem ursprünglichen Plan abweichen – was durchaus legitim ist –, sind diese Abweichungen im Artikel transparent zu berichten. Nur so kann die Leserschaft die Aussagekraft der Ergebnisse richtig einschätzen.' Transparent berichten ist die korrekte Antwort."
    },
    {
        "id": "C1_m01_HV3_q9",
        "type": "true_false",
        "questionText": "Folie 5 / Lücke 9: Wen das APC-Modell besonders hart trifft",
        "options": ["Globalen Süden", "kleinen Privatuniversitäten", "Fachhochschulen", "Doktoranden ohne Stipendium"],
        "correctAnswer": "Globalen Süden",
        "explanation": "Der Vortragende stellt fest: 'Das APC-Modell trifft Forschende aus dem Globalen Süden besonders hart: Sie können zwar nun lesen, aber oft nicht publizieren, weil ihre Institutionen weder über Abonnementbudgets noch über APC-Fördertöpfe verfügen.' Globalen Süden ist die korrekte Antwort."
    },
    {
        "id": "C1_m01_HV3_q10",
        "type": "true_false",
        "questionText": "Folie 5 / Lücke 10: Haupthindernis für Open Data in Geistes-/Sozialwissenschaften",
        "options": ["Datenschutz und Vertraulichkeit", "fehlende Digitalisierung", "mangelndes Interesse", "zu kleine Fachgemeinschaft"],
        "correctAnswer": "Datenschutz und Vertraulichkeit",
        "explanation": "Der Vortragende erklärt: 'In den Geistes- und Sozialwissenschaften stößt Open Data auf besondere Hindernisse: Interviews, Archivmaterialien und Umfrageantworten sind oft aus datenschutzrechtlichen oder ethischen Gründen vertraulich und können nicht einfach geteilt werden.' Datenschutz und Vertraulichkeit ist die korrekte Antwort."
    }
]

# ─────────────────────────────────────────────────────────────────────────────
# WRITING
# ─────────────────────────────────────────────────────────────────────────────

writing_task = {
    "taskNumber": 1,
    "type": "essay",
    "instructions": "Wählen Sie eine der beiden Aufgaben (A oder B) und schreiben Sie einen Text von mindestens 350 Wörtern. Sie haben 70 Minuten Zeit. Beachten Sie die vier Leitpunkte.",
    "instructionsTranslation": "Choose one of the two tasks (A or B) and write a text of at least 350 words. You have 70 minutes. Pay attention to the four guiding points.",
    "prompt": """Aufgabe A — Erörterung: Soll künstliche Intelligenz im schulischen Unterricht verboten werden?

Zwei Stimmen zur Debatte:

Stimme 1 (Elternverband): „Der Einsatz von KI-Tools wie Chatbots im Unterricht sollte schulweit verboten werden. Schülerinnen und Schüler, die sich auf KI verlassen, verlernen das eigenständige Denken. Wer komplexe Aufgaben an eine Maschine delegiert, verzichtet auf die kognitiven Anstrengungen, die echtes Lernen ausmachen."

Stimme 2 (Bildungstechnologin): „Ein Verbot wäre kontraproduktiv. KI gehört zur Lebensrealität der nächsten Generation. Schulen sollten stattdessen lehren, wie man KI kritisch und kompetent einsetzt – als Werkzeug, nicht als Ersatz für das eigene Denken."

Leitpunkte:
1. Führen Sie in das Thema ein und erläutern Sie die gesellschaftliche Bedeutung der Frage.
2. Diskutieren Sie Argumente, die für ein Verbot von KI im Unterricht sprechen.
3. Diskutieren Sie Argumente, die gegen ein Verbot und für einen geregelten Einsatz sprechen.
4. Begründen Sie abschließend Ihren eigenen Standpunkt.

---

Aufgabe B — Stellungnahme: Offene Wissenschaft – ein Ideal mit Grenzen?

Ausgangsbehauptung (Wissenschaftsrat): „Open Science ist die wichtigste Reform des Wissenschaftssystems in den letzten Jahrzehnten. Transparenz, offene Daten und freier Zugang zu Publikationen sind unverzichtbar für eine glaubwürdige Forschungsgemeinschaft."

Leitpunkte:
1. Führen Sie in das Thema ein und erläutern Sie die Kernidee von Open Science.
2. Diskutieren Sie Argumente, die die Behauptung des Wissenschaftsrats stützen.
3. Diskutieren Sie Grenzen und Schwachstellen des Open-Science-Modells.
4. Nehmen Sie abschließend Stellung: Teilen Sie die Position des Wissenschaftsrats – oder nicht?

Mindestlänge: 350 Wörter. Empfehlung: 350–400 Wörter.""",
    "promptTranslation": "Task A — Argumentative essay: Should artificial intelligence be banned in school lessons? | Task B — Opinion statement: Open Science — an ideal with limits?",
    "requiredPoints": [
        "Thema einführen und gesellschaftliche Bedeutung erläutern",
        "Argumente für eine Position diskutieren",
        "Argumente für die Gegenposition diskutieren",
        "Eigenen Standpunkt begründen"
    ],
    "wordCountMin": 350,
    "wordCountMax": 450,
    "sampleAnswer": """Aufgabe A — Musterlösung (Erörterung)

Der Einzug von KI-Assistenten in die Klassenräume stellt das Bildungssystem vor eine Grundsatzfrage, die weit über pädagogische Technikskepsis hinausgeht: Welche kognitiven Leistungen soll die nächste Generation noch selbst erbringen – und welche darf sie delegieren?

Für ein Verbot sprechen gewichtige Argumente. Wer Aufsätze, Rechenaufgaben oder Analysen routinemäßig von einem Sprachmodell erledigen lässt, entzieht sich jener produktiven Anstrengung, aus der nach aktuellem Forschungsstand nachhaltige Lerneffekte entstehen. Die sogenannte desirable difficulty – die wünschenswerte kognitive Erschwernis – gilt als unverzichtbar für die Gedächtniskonsolidierung. Hinzu kommt die Frage der Leistungsgerechtigkeit: Wenn Schülerinnen und Schüler je nach Elternhaus unterschiedlichen Zugang zu KI-Tools haben, vergrößert ein unkontrollierter Einsatz bestehende Bildungsungleichheiten, anstatt sie abzubauen.

Gleichwohl ist ein generelles Verbot keine überzeugende Antwort. Erstens wäre es kaum durchsetzbar: Wer zu Hause schreibt, kann seine KI-Nutzung nicht wirksam kontrollieren lassen. Zweitens ignoriert ein Verbot die Berufswirklichkeit der Lernenden: In nahezu jedem wissensintensiven Berufsfeld gehört der kompetente Einsatz von KI-Werkzeugen bereits heute zur Grundausstattung. Drittens verwechselt die Verbotsforderung das Werkzeug mit dem Lernziel. Eine Taschenrechner-Analogie zeigt, wie kurzsichtig das ist: Der Mathematikunterricht verbot den Taschenrechner zunächst, erkannte dann aber, dass das Ziel nicht handschriftliches Rechnen, sondern mathematisches Denken ist.

In Anbetracht dieser Abwägung überzeuge ich mich von folgendem Standpunkt: Ein pauschales Verbot ist weder sinnvoll noch realitätsnah. Was die Schule leisten sollte, ist die explizite Vermittlung von KI-Kompetenz – kritische Bewertung von KI-Ausgaben, Erkennen von Halluzinationen, Verständnis von Grenzen und Risiken. Gleichzeitig muss es Lernformate geben, in denen eigenständiges Denken uneingeschränkt gefordert wird, unabhängig von KI. Das eine schließt das andere nicht aus. Nicht das Verbot, sondern die pädagogisch reflektierte Integration ist der zukunftsfähige Weg.

[ca. 370 Wörter — demonstriert alle 4 Leitpunkte, ≥3 FVG, Konjunktiv II, Passiv-Ersatzformen, Genitiv-Präpositionen, Konnektoren-Vielfalt]""",
    "scoringCriteria": [
        {
            "criterion": "Aufgabengerechtheit",
            "maxPoints": 12,
            "description": "Alle 4 Leitpunkte vollständig und mit C1-angemessener Tiefe behandelt (≥3–4 Sätze pro Punkt mit Begründung + Beispiel). Kein Leitpunkt ausgelassen oder nur oberflächlich angerissen."
        },
        {
            "criterion": "Repertoire",
            "maxPoints": 12,
            "description": "Breiter C1-Wortschatz: abstrakte argumentative Lexik (Leistungsgerechtigkeit, Gedächtniskonsolidierung, desirable difficulty), ≥3 Funktionsverbgefüge, Hedging-Ausdrücke, Register-Marker. Keine B1/B2-Einheitsprosa."
        },
        {
            "criterion": "Korrektheit",
            "maxPoints": 12,
            "description": "Morphologische und syntaktische Korrektheit. C1-Erwartung: Fehler dürfen vorkommen, dürfen aber weder Verständnis beeinträchtigen noch Register brechen. Konjunktiv II, Genitiv-Präpositionen und Passiv-Ersatzformen korrekt eingesetzt."
        },
        {
            "criterion": "Kommunikative Gestaltung",
            "maxPoints": 12,
            "description": "Klare Textstruktur (Einleitung 10–15% / Hauptteil 70–75% / Schluss 10–15%), kohärente Absatzführung, vielfältige Konnektoren (gleichwohl, hinzu kommt, in Anbetracht, gleichwohl, erstens/zweitens/drittens), Register durchgängig formal-akademisch."
        }
    ]
}

# ─────────────────────────────────────────────────────────────────────────────
# SPEAKING
# ─────────────────────────────────────────────────────────────────────────────

speaking_parts = [
    {
        "partNumber": 1,
        "instructions": "Teil 1A — Präsentation: Wählen Sie eines der beiden Themen und halten Sie eine Präsentation von ca. 3 Minuten. Nutzen Sie die Stichpunkte als Anregung. Sie haben 20 Minuten Vorbereitungszeit.",
        "instructionsTranslation": "Part 1A — Presentation: Choose one of the two topics and give a presentation of approximately 3 minutes. Use the bullet points as prompts. You have 20 minutes preparation time.",
        "type": "presentation",
        "prompt": """Thema A: Lebenslanges Lernen — Notwendigkeit oder Last?

Mögliche Aspekte (Sie müssen nicht alle ansprechen):
• Warum ist lebenslanges Lernen in der heutigen Gesellschaft gefordert?
• Welche gesellschaftlichen Gruppen profitieren — welche werden benachteiligt?
• Ist lebenslanges Lernen Selbstverwirklichung oder struktureller Zwang?
• Wie sollte die Gesellschaft / der Staat lebenslanges Lernen unterstützen?

---

Thema B: Wissenschaft und Öffentlichkeit — Wem vertrauen wir noch?

Mögliche Aspekte (Sie müssen nicht alle ansprechen):
• Warum ist das Vertrauen in Wissenschaft und Experten in Teilen der Gesellschaft gesunken?
• Welche Verantwortung tragen Medien bei der Vermittlung wissenschaftlicher Erkenntnisse?
• Wie sollten Wissenschaftlerinnen und Wissenschaftler mit Unsicherheit und widersprüchlichen Studien umgehen?
• Welche Maßnahmen könnten das öffentliche Vertrauen in die Wissenschaft stärken?""",
        "sampleResponse": """[Thema B — Musterpräsentation]

Meine Damen und Herren, die Frage, wem wir in der Wissenschaft noch vertrauen, ist eine der drängendsten unserer Zeit. Die COVID-19-Pandemie hat auf dramatische Weise gezeigt, wie schnell öffentliches Vertrauen in wissenschaftliche Institutionen unter Druck geraten kann – und wie folgenreich es ist, wenn dieses Vertrauen schwindet.

Zunächst möchte ich erörtern, warum das Vertrauen in Teilen der Bevölkerung nachgelassen hat. Ein zentraler Faktor ist die Beschleunigung des Informationsflusses. In sozialen Medien verbreiten sich Preprints – also noch nicht peer-reviewte Vorstudien – mit derselben Geschwindigkeit wie gesicherte Erkenntnisse. Wenn Medien diese Nuancen nicht vermitteln, entsteht der Eindruck, Wissenschaft widerspreche sich ständig selbst. Das schafft Raum für Desinformation.

Eine besondere Verantwortung tragen dabei die Medien. Wer eine Schlagzeile schreibt, die eine Einzelstudie als „Durchbruch" bezeichnet, ohne auf deren Vorläufigkeit hinzuweisen, schadet dem wissenschaftlichen Vertrauen nachhaltig. Medienkompetenz und wissenschaftliche Bildung müssen daher als gesellschaftliche Aufgabe verstanden werden.

Was Wissenschaftlerinnen und Wissenschaftler selbst tun können, ist ebenso entscheidend: Sie müssen lernen, Unsicherheit als Teil des wissenschaftlichen Prozesses transparent zu kommunizieren, statt Ergebnisse mit einer Gewissheit vorzutragen, die sie nicht haben. Epistemische Bescheidenheit ist keine Schwäche, sondern ein Zeichen von Integrität.

Mein Fazit: Vertrauen in die Wissenschaft ist kein natürliches Gut, das sich selbst erhält – es muss aktiv gepflegt werden, durch transparente Kommunikation, verantwortungsbewusste Medienberichterstattung und eine Wissenschaftskultur, die Unsicherheit als normal begreift.""",
        "evaluationTips": [
            "Strukturieren Sie Ihren Vortrag mit einer klaren Einleitung, einem Hauptteil mit mindestens zwei Argumentationssträngen und einem Fazit.",
            "Nutzen Sie Signalwörter: 'Zunächst möchte ich…', 'Ein weiterer Aspekt…', 'Mein Fazit…'",
            "Vermeiden Sie reine Auflistung – jeder Punkt muss argumentativ entwickelt werden.",
            "C1-Erwartung: abstrakte Argumentation, nicht nur Beschreibung. Stellen Sie Ursache-Wirkungs-Zusammenhänge dar.",
            "Verwenden Sie Konjunktiv II für höfliche Distanzierung: 'Ich würde behaupten, dass…', 'Es ließe sich argumentieren…'",
            "Blickkontakt und natürliche Sprechweise sind Teil der Bewertung (Aussprache und Intonation)."
        ],
        "keyPhrases": [
            "Ich möchte zunächst auf … eingehen",
            "Ein zentraler Aspekt ist …",
            "Es ließe sich argumentieren, dass …",
            "Dem ist entgegenzuhalten, dass …",
            "Meinem Dafürhalten nach …",
            "Zusammenfassend lässt sich sagen …",
            "In Anbetracht dieser Überlegungen …",
            "Dies hat weitreichende Konsequenzen für …"
        ]
    },
    {
        "partNumber": 2,
        "instructions": "Teil 1B — Zusammenfassung und Anschlussfrage: Der/die Prüfungspartner/in fasst die Präsentation kurz zusammen und stellt eine Anschlussfrage. Der/die Präsentierende antwortet.",
        "instructionsTranslation": "Part 1B — Summary and follow-up question: The exam partner briefly summarises the presentation and asks one follow-up question. The presenter responds.",
        "type": "discussion",
        "prompt": """Aufgabe für den/die Prüfungspartner/in:
1. Fassen Sie die Hauptthesen der Präsentation in 2–3 Sätzen zusammen.
2. Stellen Sie eine Anschlussfrage, die einen neuen Aspekt des Themas öffnet oder eine der Thesen kritisch hinterfragt.

Beispiele für Anschlussfragen (je nach Präsentationsthema):
- „Du hast argumentiert, dass Medien Mitverantwortung tragen. Aber wäre es nicht die Aufgabe der Wissenschaft selbst, einfacher zu kommunizieren?"
- „Siehst du das lebenslange Lernen eher als Chance oder als Zwang – und ändert sich das mit dem Lebensalter?"
- „Wie würdest du mit jemandem diskutieren, der sagt: ‚Ich vertraue Wissenschaftlern grundsätzlich nicht mehr – zu viele Widersprüche'?"

Aufgabe für den/die Präsentierende/n:
Reagieren Sie direkt auf die Zusammenfassung: korrigieren Sie ggf. Missverständnisse und beantworten Sie die Anschlussfrage mit einer begründeten Argumentation.""",
        "sampleResponse": """[Musterreaktion auf Anschlussfrage zur Wissenschaftskommunikation]

Diese Frage trifft einen wunden Punkt. Ja, Wissenschaftlerinnen und Wissenschaftler tragen durchaus eine Kommunikationsverantwortung. Allerdings würde ich einer einseitigen Schuldzuweisung widersprechen: Die Aufgabe, komplexe Erkenntnisse für eine breite Öffentlichkeit zu übersetzen, kann nicht allein den Forschenden überlassen bleiben, die primär für ihre Fachcommunity publizieren. Das ist, als würde man von Chirurginnen verlangen, auch Sanitäter auszubilden. Sinnvoller wäre eine klare Arbeitsteilung: Wissenschaft produziert rigorose Erkenntnisse und kommuniziert diese transparent mit ihren Limitationen – Wissenschaftsjournalismus übersetzt und kontextualisiert. Beide müssen ihre Kompetenz darin als Beruf begreifen, nicht als Nebenaufgabe.""",
        "evaluationTips": [
            "Hören Sie der Zusammenfassung des Partners aktiv zu und bestätigen Sie korrekte Punkte oder korrigieren Sie Missverständnisse.",
            "Die Anschlussfrage muss direkt und argumentativ beantwortet werden – nicht ausweichen.",
            "C1-Erwartung: Reagieren Sie differenziert, räumen Sie Teilargumente ein, bevor Sie widersprechen.",
            "Verwenden Sie turn-taking-Marker: 'Diese Frage trifft…', 'Ich möchte ergänzen, dass…', 'Das stimmt, aber…'"
        ],
        "keyPhrases": [
            "Ich stimme zu, dass … allerdings …",
            "Das ist ein wichtiger Punkt, den ich ergänzen möchte: …",
            "Ich würde einer einseitigen Schuldzuweisung widersprechen …",
            "Das trifft einen wesentlichen Aspekt …",
            "In diesem Zusammenhang ist zu bedenken, dass …"
        ]
    },
    {
        "partNumber": 3,
        "instructions": "Teil 2 — Diskussion: Diskutieren Sie gemeinsam mit Ihrem/Ihrer Prüfungspartner/in die folgende These. Beide müssen aktiv argumentieren und auf die Argumente des Partners eingehen. Ca. 5–6 Minuten.",
        "instructionsTranslation": "Part 2 — Discussion: Discuss the following thesis together with your exam partner. Both must actively argue and respond to the partner's arguments. Approximately 5–6 minutes.",
        "type": "discussion",
        "prompt": """Diskussionsthese:

„Sind Lehrer durch künstliche Intelligenz ersetzbar?"

Hintergrund: Auf Ihre Diskussionskarten steht eine kurze Einschätzung als Ausgangspunkt:

Karte A: „KI kann Wissen effizienter und individualisierter vermitteln als jeder menschliche Lehrer. Bildungssysteme, die das nicht nutzen, verschwenden Ressourcen."

Karte B: „Bildung ist nicht nur Wissensvermittlung, sondern Persönlichkeitsentwicklung. Was Lehrpersonen leisten – Empathie, Vorbild sein, soziale Kompetenz – kann kein Algorithmus ersetzen."

Diskutieren Sie:
- Was versteht man unter 'Ersetzbarkeit'?
- In welchen Bereichen könnte KI Lehrpersonen sinnvoll unterstützen oder ersetzen?
- Was sind die Grenzen dieser Ersetzbarkeit?
- Welche gesellschaftlichen Konsequenzen hätte eine weitgehende KI-gestützte Bildung?""",
        "sampleResponse": """[Musterargumentation — Karte B-Position]

Ich möchte zunächst den Begriff 'Ersetzbarkeit' hinterfragen. Wenn wir darunter verstehen, dass KI dieselben Lernoutcomes erzielt wie ein Lehrer, dann ist das für bestimmte Bereiche – Vokabeln lernen, Mathematikübungen – vielleicht realistisch. Aber Bildung im umfassenden Sinne erschöpft sich nicht in Lernoutcomes.

Was eine Lehrperson leistet, hat eine relationale Dimension: Sie erkennt, wenn ein Kind an diesem Tag nicht aufnahmefähig ist, nicht wegen mangelnder Intelligenz, sondern wegen eines Konflikts zu Hause. Sie reagiert mit Empathie, nicht mit einem optimierten Lernpfad. Das ist Erziehung, nicht Unterricht im technischen Sinne.

Trotzdem möchte ich deiner Position eines zugestehen: Es gibt eindeutig Bereiche, in denen KI Lehrkräfte entlasten oder ergänzen kann – administrative Aufgaben, Übungsaufgaben differenzieren, Rückmeldungen auf Hausaufgaben geben. Das wäre kein Ersatz, sondern eine Entlastung, die Lehrenden mehr Zeit für das lässt, was Maschinen nicht können: den Menschen zu sehen.

Letztlich würde ich sagen: 'Ersetzbar' ist das falsche Wort. Die Frage sollte lauten: Wie gestalten wir die Zusammenarbeit zwischen KI und Lehrpersonen so, dass beide das leisten, was sie am besten können?""",
        "evaluationTips": [
            "C1-Diskussion verlangt dialektisches Vorgehen: These → Antithese → Synthese (nicht Monolog).",
            "Gehen Sie explizit auf die Argumente des Partners ein: 'Das überzeugt mich nicht ganz, weil…', 'Ich möchte deiner Aussage teilweise widersprechen…'",
            "Vermeiden Sie Wiederholung Ihrer eigenen Position – entwickeln Sie sie weiter oder räumen Sie Teilargumente ein.",
            "Nutzen Sie Konzessivmarker: 'Gleichwohl…', 'Dennoch…', 'Allerdings…', 'Immerhin…'",
            "Achten Sie auf Turn-Taking: Lassen Sie den Partner ausreden, bestätigen Sie Gehörtes aktiv ('Ich höre, dass du sagst…')."
        ],
        "keyPhrases": [
            "Ich möchte zunächst den Begriff … hinterfragen",
            "Das überzeugt mich nicht vollständig, weil …",
            "Ich möchte einem Aspekt deiner Argumentation widersprechen: …",
            "Gleichwohl ist zu berücksichtigen, dass …",
            "Darin stimme ich dir zu, allerdings …",
            "Letztlich würde ich argumentieren, dass …",
            "Das bringt mich zu einem weiteren Punkt …",
            "Ich denke, wir sind uns einig, dass … – aber strittig bleibt …"
        ]
    }
]

# ─────────────────────────────────────────────────────────────────────────────
# ASSEMBLE MOCK
# ─────────────────────────────────────────────────────────────────────────────

mock = {
    "id": "C1_mock_01",
    "level": "C1",
    "title": "C1 Übungstest 1: Wissenschaftliche Erkenntnis und Verantwortung",
    "version": 1,
    "sections": {
        "reading": {
            "totalTimeMinutes": 90,
            "parts": [
                {
                    "partNumber": 1,
                    "instructions": "Lesen Sie den folgenden Text. Sechs Sätze wurden herausgenommen. Wählen Sie aus den acht angebotenen Sätzen (a–h) den jeweils passenden. Zwei Sätze passen nicht. Schreiben Sie den Buchstaben des richtigen Satzes in die entsprechende Lücke.",
                    "instructionsTranslation": "Read the following text. Six sentences have been removed. Choose the appropriate sentence from the eight offered (a–h) for each gap. Two sentences do not fit. Write the letter of the correct sentence in the corresponding gap.",
                    "texts": [
                        {
                            "id": "C1_m01_R1_main",
                            "type": "article",
                            "content": reading_teil1_text,
                            "source": "Spektrum der Wissenschaft, Dezember 2025"
                        }
                    ] + reading_teil1_sentences,
                    "questions": reading_teil1_questions
                },
                {
                    "partNumber": 2,
                    "instructions": "Lesen Sie die fünf Absätze (a–e) zum Thema KI in der Wissenschaft. Lesen Sie dann die sechs Fragen. Welcher Absatz enthält die Antwort auf jede Frage? Schreiben Sie den Buchstaben des richtigen Absatzes. Ein Absatz kann für mehrere Fragen passen. Wenn kein Absatz passt, schreiben Sie 'x'.",
                    "instructionsTranslation": "Read the five paragraphs (a–e) on the topic of AI in research. Then read the six questions. Which paragraph contains the answer to each question? Write the letter of the correct paragraph. One paragraph may match multiple questions. If no paragraph fits, write 'x'.",
                    "texts": reading_teil2_paragraphs,
                    "questions": reading_teil2_questions
                },
                {
                    "partNumber": 3,
                    "instructions": "Lesen Sie den folgenden Artikel. Entscheiden Sie bei jeder Aussage, ob sie richtig (R), falsch (F) oder nicht im Text (N) ist. Außerdem: Welcher Titel passt am besten zum Text? Wählen Sie a, b oder c.",
                    "instructionsTranslation": "Read the following article. For each statement decide whether it is correct (R), incorrect (F) or not in the text (N). In addition: Which title best fits the text? Choose a, b, or c.",
                    "texts": [reading_teil3_article],
                    "questions": reading_teil3_questions
                }
            ]
        },
        "sprachbausteine": {
            "totalTimeMinutes": 25,
            "parts": [
                {
                    "partNumber": 1,
                    "instructions": "Lesen Sie den folgenden Text. Wählen Sie bei jeder Lücke (1–22) die richtige Antwort (a, b, c oder d). Es gibt jeweils nur eine richtige Antwort.",
                    "instructionsTranslation": "Read the following text. For each gap (1–22) choose the correct answer (a, b, c or d). There is only one correct answer each time.",
                    "text": sprachbausteine_text,
                    "questions": sprachbausteine_questions
                }
            ]
        },
        "listening": {
            "totalTimeMinutes": 40,
            "parts": [
                {
                    "partNumber": 1,
                    "instructions": "Sie hören acht kurze Stellungnahmen verschiedener Personen zum Thema Reproduzierbarkeitskrise in der Wissenschaft. Lesen Sie zuerst die zehn Zusammenfassungen (a–j). Hören Sie dann die acht Aussagen. Welche Zusammenfassung passt zu welchem Sprecher? Zwei Zusammenfassungen passen nicht. Sie hören die Texte nur einmal.",
                    "instructionsTranslation": "You will hear eight short statements from different people on the topic of the replication crisis in science. First read the ten summaries (a–j). Then listen to the eight statements. Which summary matches which speaker? Two summaries do not fit. You will hear the texts only once.",
                    "audioFile": "assets/audio/C1/mock01/listening_part1.mp3",
                    "playCount": 1,
                    "questions": [
                        {
                            **q,
                            "matchingSources": hv1_summaries
                        }
                        for q in hv1_questions
                    ]
                },
                {
                    "partNumber": 2,
                    "instructions": "Sie hören ein Interview mit Prof. Dr. Hagedorn zum Thema hybride Lehre an Hochschulen. Lesen Sie zuerst die zehn Aufgaben. Hören Sie dann das Interview. Was ist richtig? Kreuzen Sie an: a, b oder c. Sie hören das Interview nur einmal.",
                    "instructionsTranslation": "You will hear an interview with Prof. Dr. Hagedorn on the topic of hybrid teaching in higher education. First read the ten tasks. Then listen to the interview. What is correct? Choose a, b, or c. You will hear the interview only once.",
                    "audioFile": "assets/audio/C1/mock01/listening_part2.mp3",
                    "playCount": 1,
                    "questions": hv2_questions
                },
                {
                    "partNumber": 3,
                    "instructions": "Sie hören einen akademischen Vortrag zum Thema Forschungsmethoden und Reproduzierbarkeit. Im Testheft finden Sie fünf Folien mit je zwei Lücken. Füllen Sie die Lücken während des Vortrags aus. Sie hören den Vortrag nur einmal.",
                    "instructionsTranslation": "You will hear an academic lecture on the topic of research methods and reproducibility. In the test booklet you will find five slides each with two gaps. Fill in the gaps during the lecture. You will hear the lecture only once.",
                    "audioFile": "assets/audio/C1/mock01/listening_part3.mp3",
                    "playCount": 1,
                    "slides": hv3_slides,
                    "questions": hv3_questions
                }
            ]
        },
        "writing": {
            "totalTimeMinutes": 70,
            "tasks": [writing_task]
        },
        "speaking": {
            "totalTimeMinutes": 16,
            "prepTimeMinutes": 20,
            "parts": speaking_parts
        }
    }
}

# Write output
output_path = os.path.join(
    os.path.dirname(__file__),
    "apps/mobile/assets/content/C1/mock_01.json"
)
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(mock, f, ensure_ascii=False, indent=2)

print(f"Written to: {output_path}")
print(f"File size: {os.path.getsize(output_path):,} bytes")

# Count items
lesen_items = 6 + 6 + 12  # Teil 1 (6) + Teil 2 (6) + Teil 3 (11 R/F/N + 1 Makro)
sb_items = len(sprachbausteine_questions)
hoeren_items = len(hv1_questions) + len(hv2_questions) + len(hv3_questions)
schreiben_items = 1
sprechen_items = len(speaking_parts)

print(f"\nItem counts:")
print(f"  Lesen: {lesen_items} (target: 24)")
print(f"  Sprachbausteine: {sb_items} (target: 22)")
print(f"  Hören: {hoeren_items} (target: 28)")
print(f"  Schreiben: {schreiben_items} (target: 1)")
print(f"  Sprechen: {sprechen_items} (target: 3)")
