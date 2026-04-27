"""
[PEDAGOGY-REWRITE] B2 vocab additions — issue #115
Adds: Argumentation cluster (P0-2), FVG expansions (P1-2), 2024-2026 current-affairs lexis (P1-3)
IDs start at 4017. No deletions. No renumbering.
Entries already present in the file are automatically skipped.
"""
import json
import sys

VOCAB_PATH = '/Users/kiran.kumar/kk/worspaces/personal/fastrack-deutsch/.worktrees/fix-b2-vocab-argumentation-fvg/apps/mobile/src/data/vocabulary/B2_vocabulary.json'


def entry(id_, german, english, example, topic, article=None, plural=None):
    e = {
        "id": id_,
        "level": "B2",
        "german": german,
        "english": english,
        "exampleSentence": example,
        "topic": topic,
        "audioFile": None,
        "easeFactor": 2.5,
        "intervalDays": 0,
        "repetitions": 0,
        "nextReviewDate": None,
        "lastReviewedAt": None,
    }
    if article is not None:
        e["article"] = article
        e["plural"] = plural
    return e


def build_candidates():
    """Build the full candidate list. Duplicates are filtered out by the caller."""
    c = []

    def add(german, english, example, topic, article=None, plural=None):
        c.append((german, english, example, topic, article, plural))

    # -------------------------------------------------------------------------
    # P0-2: Argumentation cluster — topic="Argumentation"
    # -------------------------------------------------------------------------

    # Nouns (10 mandatory)
    add("der Standpunkt", "standpoint / point of view",
        "Die Autorin vertritt den Standpunkt, dass wirtschaftliches Wachstum und Klimaschutz vereinbar sind.",
        "Argumentation", "der", "die Standpunkte")

    add("die Stellungnahme", "position statement / opinion piece",
        "In seiner schriftlichen Stellungnahme widersprach der Verband den Plänen der Bundesregierung.",
        "Argumentation", "die", "die Stellungnahmen")

    add("das Argument", "argument",
        "Ihr zentrales Argument stützt sich auf aktuelle Studiendaten zur Beschäftigungslage.",
        "Argumentation", "das", "die Argumente")

    add("das Gegenargument", "counter-argument",
        "Das stärkste Gegenargument lautet, dass kurzfristige Kosteneinsparungen langfristige Schäden verursachen.",
        "Argumentation", "das", "die Gegenargumente")

    add("die Begründung", "justification / reasoning",
        "Die Begründung für die Maßnahme bleibt vage und überzeugt nicht alle Beteiligten.",
        "Argumentation", "die", "die Begründungen")

    add("der Beleg", "evidence / proof",
        "Als Beleg für diese These führt die Studie mehrere Langzeiterhebungen an.",
        "Argumentation", "der", "die Belege")

    add("der Befürworter", "supporter / proponent",
        "Befürworter der Reform betonen, dass die Änderungen längst überfällig seien.",
        "Argumentation", "der", "die Befürworter")

    add("der Gegner", "opponent",
        "Die Gegner des Projekts warnen vor nicht absehbaren Folgen für die betroffene Region.",
        "Argumentation", "der", "die Gegner")

    add("der Skeptiker", "sceptic",
        "Skeptiker bezweifeln, ob die versprochenen Einsparungen tatsächlich realisierbar sind.",
        "Argumentation", "der", "die Skeptiker")

    add("der Kritiker", "critic",
        "Kritiker werfen dem Konzern vor, soziale Verantwortung hinter wirtschaftlichen Interessen zurückzustellen.",
        "Argumentation", "der", "die Kritiker")

    # Verbs (11 mandatory — unterstützen, einräumen, belegen, ablehnen already in file)
    add("argumentieren", "to argue",
        "Wer überzeugend argumentiert, verknüpft Beobachtungen stets mit nachvollziehbaren Schlussfolgerungen.",
        "Argumentation")

    add("behaupten", "to claim / assert",
        "Die Studie behauptet, einen direkten Zusammenhang zwischen Medienkonsum und politischer Polarisierung nachzuweisen.",
        "Argumentation")

    add("einwenden", "to raise an objection",
        "Kritische Stimmen wenden ein, dass die Datenbasis für solche weitreichenden Aussagen zu schmal ist.",
        "Argumentation")

    add("widersprechen", "to contradict / dissent",
        "Der Sachverständige widersprach der offiziellen Einschätzung und legte eigene Berechnungen vor.",
        "Argumentation")

    add("anzweifeln", "to call into question / doubt",
        "Mehrere Experten zweifeln die Methodik der Erhebung grundsätzlich an.",
        "Argumentation")

    add("in Frage stellen", "to question / challenge",
        "Der Bericht stellt die bisherigen Annahmen zur Wirksamkeit dieser Maßnahmen grundlegend in Frage.",
        "Argumentation")

    add("zustimmen", "to agree / assent",
        "Der Ausschuss stimmte dem Vorschlag nach langer Debatte mit knapper Mehrheit zu.",
        "Argumentation")

    add("widerlegen", "to refute",
        "Die neuere Forschung widerlegt die Annahme, dass Wirtschaftswachstum automatisch zu sozialer Teilhabe führt.",
        "Argumentation")

    # Hedging adverbials (7 mandatory — weitgehend, grundsätzlich already in file)
    add("tendenziell", "on the whole / tending towards",
        "Jüngere Beschäftigte beurteilen flexible Arbeitsmodelle tendenziell positiver als ältere Generationen.",
        "Argumentation")

    add("größtenteils", "for the most part / largely",
        "Die Einwände der Opposition wurden größtenteils ignoriert, was zu erheblicher Kritik führte.",
        "Argumentation")

    add("in der Regel", "as a rule / generally",
        "In der Regel sind gut strukturierte Argumente überzeugender als emotional geprägte Aussagen.",
        "Argumentation")

    add("im Großen und Ganzen", "by and large / on the whole",
        "Im Großen und Ganzen begrüßt die Mehrheit der Bevölkerung die Reformpläne, auch wenn Details umstritten bleiben.",
        "Argumentation")

    add("im Prinzip", "in principle",
        "Im Prinzip stimmt die Fraktion dem Vorhaben zu, fordert aber substanzielle Nachbesserungen.",
        "Argumentation")

    add("im Wesentlichen", "essentially / in essence",
        "Die beiden Positionen unterscheiden sich im Wesentlichen in der Frage der Finanzierungsverantwortung.",
        "Argumentation")

    add("vorwiegend", "predominantly / mainly",
        "Diese Sichtweise wird vorwiegend von denjenigen vertreten, die direkt von der Regelung betroffen sind.",
        "Argumentation")

    # Discourse markers (6 mandatory — demgegenüber already in file)
    add("einerseits", "on the one hand",
        "Einerseits bietet Digitalisierung enorme Chancen; andererseits entstehen neue Risiken für den Datenschutz.",
        "Argumentation")

    add("andererseits", "on the other hand",
        "Die Flexibilisierung des Arbeitsmarktes hat andererseits zur Erosion sozialer Sicherungssysteme beigetragen.",
        "Argumentation")

    add("im Gegensatz dazu", "in contrast to this / by contrast",
        "Im Gegensatz dazu sprechen sich Arbeitnehmerverbände für eine strengere Regulierung aus.",
        "Argumentation")

    add("abgesehen von", "apart from / leaving aside",
        "Abgesehen von einzelnen Ausnahmen ist die Rechtslage in allen Bundesländern vergleichbar.",
        "Argumentation")

    add("verglichen mit", "compared with",
        "Verglichen mit den Vorjahreswerten ist die Zustimmung zur Maßnahme deutlich gestiegen.",
        "Argumentation")

    # demzufolge already in file (id 3930) — skip; add substitute discourse marker
    add("hingegen", "whereas / by contrast / on the other hand",
        "Die eine Seite fordert mehr staatliche Regulierung; die andere Seite hingegen setzt auf Marktmechanismen.",
        "Argumentation")

    # Evaluative adjectives (5 mandatory — schlüssig, überzeugend, einseitig already in file)
    add("fragwürdig", "questionable / dubious",
        "Die methodische Grundlage dieser Schlussfolgerung erscheint aus wissenschaftlicher Sicht fragwürdig.",
        "Argumentation")

    add("plausibel", "plausible / credible",
        "Das klingt auf den ersten Blick plausibel, lässt sich aber empirisch kaum belegen.",
        "Argumentation")

    # Additional argumentation lexis (>=5 to reach >=40)
    # die Schlussfolgerung (id 749) and die These (id 739) already in file — skip; add others
    add("die Gegenposition", "opposing position / counter-stance",
        "Die Gegenposition wurde im Plenum ausführlich dargelegt, fand aber keine Mehrheit.",
        "Argumentation", "die", "die Gegenpositionen")

    add("die Auseinandersetzung", "debate / engagement with",
        "Eine sachliche Auseinandersetzung mit den Gegenargumenten stärkt die eigene Position erheblich.",
        "Argumentation", "die", "die Auseinandersetzungen")

    add("nachvollziehbar", "comprehensible / traceable",
        "Die Entscheidung mag nachvollziehbar sein, aber ihre gesellschaftlichen Folgen sind nicht ausreichend bedacht worden.",
        "Argumentation")

    add("überzeugend darlegen", "to set out convincingly / make a compelling case",
        "Die Expertin legte überzeugend dar, dass alternative Finanzierungsmodelle langfristig tragfähiger wären.",
        "Argumentation")

    add("die Einschränkung", "qualification / limitation / caveat",
        "Die Verfasser selbst formulieren mehrere Einschränkungen, die den Geltungsbereich der Studie begrenzen.",
        "Argumentation", "die", "die Einschränkungen")

    add("zugestehen", "to grant / concede",
        "Selbst entschiedene Gegner der Maßnahme gestehen zu, dass kurzfristig Einsparungen zu erzielen sind.",
        "Argumentation")

    add("in Abrede stellen", "to deny / dispute",
        "Die Unternehmensleitung stellt nicht in Abrede, dass Handlungsbedarf besteht.",
        "Argumentation")

    add("die Erörterung", "discussion / discursive essay",
        "Eine Erörterung stellt beide Seiten einer Frage vor und kommt zu einer begründeten Schlussfolgerung.",
        "Argumentation", "die", "die Erörterungen")

    add("die Polemik", "polemic / polemical rhetoric",
        "Der Artikel greift auf Polemik zurück, anstatt sachlich zu argumentieren.",
        "Argumentation", "die", "die Polemiken")

    add("rhetorisch", "rhetorical",
        "Die Frage war rhetorisch gemeint und sollte die Schwächen der Gegenposition verdeutlichen.",
        "Argumentation")

    # -------------------------------------------------------------------------
    # P1-2: FVG expansions — missing from mandatory list
    # Present: in Anspruch nehmen, Bezug nehmen auf, einen Beitrag leisten,
    #   unter Beweis stellen, ins Auge fassen, in Erwägung ziehen, zur Sprache bringen,
    #   in Erscheinung treten, Kritik üben an, in Kraft treten, zur Anwendung kommen,
    #   zur Diskussion stellen, zur Kenntnis nehmen, in Betracht kommen,
    #   Rücksicht nehmen auf, zum Ausdruck bringen, zur Verfügung stellen, in Kauf nehmen
    # Missing (15 from mandatory list):
    #   zu dem Schluss kommen, eine Maßnahme ergreifen, in Verbindung stehen mit,
    #   Abstand nehmen von, in Aussicht stellen, Druck ausüben auf, Einfluss nehmen auf,
    #   Wert legen auf, ins Leben rufen, Anwendung finden, in Auftrag geben,
    #   sich Mühe geben, einen Versuch unternehmen, die Verantwortung übernehmen,
    #   Stellung nehmen zu
    # Plus extra FVGs to meet >=27 net-new target
    # -------------------------------------------------------------------------

    add("zu dem Schluss kommen", "to come to the conclusion",
        "Nach eingehender Prüfung kommen die Gutachter zu dem Schluss, dass der Antrag abgelehnt werden muss.",
        "Argumentation")

    add("eine Maßnahme ergreifen", "to take a measure / take action",
        "Die Behörde ergreift konkrete Maßnahmen, um die Situation im öffentlichen Raum zu verbessern.",
        "Gesellschaft")

    add("in Verbindung stehen mit", "to be associated with / to be linked to",
        "Die Fälle stehen nachweislich in Verbindung mit dem Einsatz bestimmter Chemikalien.",
        "Gesellschaft")

    add("Abstand nehmen von", "to refrain from / to move away from",
        "Die Partei nahm nach der Niederlage von ihrem ursprünglichen Plan Abstand.",
        "Gesellschaft")

    add("in Aussicht stellen", "to hold out the prospect of / to promise",
        "Die Ministerin stellte zusätzliche Fördermittel für strukturschwache Regionen in Aussicht.",
        "Gesellschaft")

    add("Druck ausüben auf", "to exert pressure on",
        "Nichtregierungsorganisationen üben gezielt Druck auf Unternehmen aus, ihre Lieferketten transparenter zu gestalten.",
        "Gesellschaft")

    add("Einfluss nehmen auf", "to exert influence on / to influence",
        "Lobbygruppen versuchen, auf die Gesetzgebung Einfluss zu nehmen.",
        "Gesellschaft")

    add("Wert legen auf", "to attach importance to / to value",
        "Die Jury legt besonderen Wert auf die sprachliche Präzision und die argumentative Stringenz der Beiträge.",
        "Argumentation")

    add("ins Leben rufen", "to establish / to set up / to launch",
        "Die Initiative wurde 2019 ins Leben gerufen, um benachteiligte Jugendliche beim Berufseinstieg zu unterstützen.",
        "Gesellschaft")

    add("Anwendung finden", "to be applied / to find application",
        "Diese Methode findet inzwischen in zahlreichen europäischen Ländern Anwendung.",
        "Technologie")

    add("in Auftrag geben", "to commission",
        "Das Bundesministerium gab eine unabhängige Studie in Auftrag, die die bisherigen Ergebnisse überprüfen soll.",
        "Gesellschaft")

    add("sich Mühe geben", "to make an effort / to take pains",
        "Die Kommission gibt sich sichtlich Mühe, alle Interessengruppen in den Prozess einzubeziehen.",
        "Argumentation")

    add("einen Versuch unternehmen", "to make an attempt",
        "Es lohnt sich, einen Versuch zu unternehmen, die Konfliktparteien an einen Tisch zu bringen.",
        "Argumentation")

    add("die Verantwortung übernehmen", "to take responsibility",
        "Die Unternehmensführung muss die Verantwortung für die Fehler der vergangenen Jahre übernehmen.",
        "Wirtschaft")

    add("Stellung nehmen zu", "to comment on / to take a position on",
        "Der Minister nahm öffentlich zu den Vorwürfen Stellung und kündigte eine interne Überprüfung an.",
        "Argumentation")

    # Extra FVGs not in mandatory list — for good measure
    add("in Betracht ziehen", "to take into consideration",
        "Bei der Entscheidungsfindung sollten alle möglichen Konsequenzen sorgfältig in Betracht gezogen werden.",
        "Argumentation")

    add("eine Entscheidung treffen", "to make / reach a decision",
        "Angesichts der knappen Frist musste das Gremium eine Entscheidung treffen, ohne alle Folgen abschätzen zu können.",
        "Argumentation")

    add("Rechenschaft ablegen", "to give account / to account for",
        "Öffentliche Institutionen sind verpflichtet, regelmäßig Rechenschaft über den Einsatz von Steuermitteln abzulegen.",
        "Gesellschaft")

    add("in den Vordergrund rücken", "to bring to the fore / to foreground",
        "Die Debatte rückt zunehmend die sozialen Folgen der Automatisierung in den Vordergrund.",
        "Gesellschaft")

    add("eine Rolle spielen", "to play a role",
        "Neben wirtschaftlichen Faktoren spielt auch das soziale Umfeld eine entscheidende Rolle.",
        "Gesellschaft")

    add("zur Verfügung haben", "to have available / to have at one's disposal",
        "Den Kommunen stehen nur begrenzte finanzielle Mittel zur Verfügung, um die Infrastruktur zu erneuern.",
        "Gesellschaft")

    add("in Angriff nehmen", "to tackle / to address",
        "Die strukturellen Probleme des Gesundheitssystems müssen endlich ernsthaft in Angriff genommen werden.",
        "Gesellschaft")

    add("Konsequenzen ziehen", "to draw conclusions / take consequences",
        "Aus den Ergebnissen der Untersuchung müssen jetzt politische Konsequenzen gezogen werden.",
        "Gesellschaft")

    add("auf den Punkt bringen", "to get to the point / to sum up",
        "Es gelingt ihr, ein komplexes Thema präzise auf den Punkt zu bringen.",
        "Argumentation")

    # -------------------------------------------------------------------------
    # P1-3: 2024-2026 prüfungsrelevante Themen
    # Already present: Filterblase (id present), Echokammer-Phänomen, Verkehrswende,
    #   Klimaneutralität, Resilienz (id 1007), Achtsamkeit (id 151), Achtsamkeitspraxis,
    #   Generationengerechtigkeit (id 1354), Algorithmus (compounds only)
    # Missing: standalone Algorithmus, Künstliche Intelligenz, Echokammer (standalone),
    #   CO2-Bepreisung, hybrides Arbeiten, Homeoffice-Pauschale, Fachkräftemangel,
    #   Zuwanderung qualifizierter Arbeitskräfte, psychische Gesundheit, Burnout,
    #   Stigmatisierung psychischer Erkrankungen
    # -------------------------------------------------------------------------

    add("die Künstliche Intelligenz", "artificial intelligence (AI)",
        "Die Künstliche Intelligenz verändert nicht nur den Arbeitsmarkt, sondern auch Fragen der Haftung und Verantwortung.",
        "Technologie", "die", None)

    add("der Algorithmus", "algorithm",
        "Der Algorithmus entscheidet ohne menschliche Kontrolle, welche Inhalte den Nutzern angezeigt werden.",
        "Technologie", "der", "die Algorithmen")

    add("die Echokammer", "echo chamber",
        "Soziale Medien begünstigen die Entstehung von Echokammern, in denen politische Meinungen kaum hinterfragt werden.",
        "Technologie", "die", "die Echokammern")

    add("der Deepfake", "deepfake",
        "Deepfakes stellen demokratische Öffentlichkeiten vor neue Herausforderungen bei der Unterscheidung von Fakten und Manipulation.",
        "Technologie", "der", "die Deepfakes")

    add("die CO2-Bepreisung", "carbon pricing",
        "Eine effektive CO2-Bepreisung gilt als zentrales Steuerungsinstrument der Klimapolitik, stößt aber auf breite Widerstände.",
        "Umwelt", "die", None)

    add("hybrides Arbeiten", "hybrid working",
        "Hybrides Arbeiten, also die Kombination aus Homeoffice und Büropräsenz, hat sich in vielen Branchen dauerhaft etabliert.",
        "Beruf", None, None)

    add("die Homeoffice-Pauschale", "home-office tax allowance",
        "Die Homeoffice-Pauschale wurde angehoben, um Arbeitnehmende steuerlich zu entlasten, die regelmäßig von zu Hause arbeiten.",
        "Beruf", "die", None)

    add("der Fachkräftemangel", "skilled-worker shortage",
        "Der Fachkräftemangel in Pflege und IT zwingt Unternehmen und Politik zu neuen Strategien bei der Gewinnung von Arbeitskräften.",
        "Beruf", "der", None)

    add("die Zuwanderung qualifizierter Arbeitskräfte", "immigration of qualified workers",
        "Die Zuwanderung qualifizierter Arbeitskräfte wird als wesentlicher Baustein zur Bewältigung des Fachkräftemangels diskutiert.",
        "Gesellschaft", "die", None)

    add("die Arbeitsverdichtung", "work intensification",
        "Arbeitsverdichtung und ständige Erreichbarkeit gelten als Hauptursachen für steigende Burnout-Raten.",
        "Beruf", "die", None)

    add("die psychische Gesundheit", "mental health",
        "Die psychische Gesundheit am Arbeitsplatz zu fördern ist nicht nur eine ethische, sondern auch eine wirtschaftliche Notwendigkeit.",
        "Gesundheit", "die", None)

    add("der Burnout", "burnout",
        "Burnout wird inzwischen von der WHO als ernstzunehmendes Berufssyndrom anerkannt, das einer frühzeitigen Prävention bedarf.",
        "Gesundheit", "der", None)

    add("die Stigmatisierung psychischer Erkrankungen", "stigmatisation of mental illness",
        "Die Stigmatisierung psychischer Erkrankungen hält Betroffene oft davon ab, rechtzeitig Hilfe zu suchen.",
        "Gesundheit", "die", None)

    add("die Desinformation", "disinformation",
        "Staatlich gelenkte Desinformation untergräbt das Vertrauen der Bevölkerung in demokratische Institutionen.",
        "Gesellschaft", "die", "die Desinformationen")

    return c


if __name__ == "__main__":
    with open(VOCAB_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    existing_german_lower = {e['german'].lower() for e in data}

    candidates = build_candidates()

    # Filter duplicates
    new_entries = []
    skipped = []
    next_id = data[-1]['id'] + 1

    for (german, english, example, topic, article, plural) in candidates:
        if german.lower() in existing_german_lower:
            skipped.append(german)
            continue
        new_entries.append(entry(next_id, german, english, example, topic, article, plural))
        existing_german_lower.add(german.lower())
        next_id += 1

    print(f"Skipped (already present): {len(skipped)}")
    if skipped:
        for s in skipped:
            print(f"  - {s}")
    print()

    arg_entries = [e for e in new_entries if e['topic'] == 'Argumentation']

    fvg_mandatory = {
        'zu dem Schluss kommen', 'eine Maßnahme ergreifen', 'in Verbindung stehen mit',
        'Abstand nehmen von', 'in Aussicht stellen', 'Druck ausüben auf', 'Einfluss nehmen auf',
        'Wert legen auf', 'ins Leben rufen', 'Anwendung finden', 'in Auftrag geben',
        'sich Mühe geben', 'einen Versuch unternehmen', 'die Verantwortung übernehmen',
        'Stellung nehmen zu',
    }
    fvg_extra = {
        'in Betracht ziehen', 'eine Entscheidung treffen', 'Rechenschaft ablegen',
        'in den Vordergrund rücken', 'eine Rolle spielen', 'zur Verfügung haben',
        'in Angriff nehmen', 'Konsequenzen ziehen', 'auf den Punkt bringen',
        'Wert legen auf',
    }
    all_fvg = fvg_mandatory | fvg_extra
    # Also count FVG entries that landed in Argumentation or other topics as part of FVG expansion
    fvg_entries = [e for e in new_entries if e['german'] in all_fvg]

    current_topics = {'Technologie', 'Beruf', 'Gesundheit', 'Gesellschaft', 'Umwelt'}
    current_entries = [e for e in new_entries
                       if e['topic'] in current_topics
                       and e['german'] not in {x['german'] for x in arg_entries}
                       and e['german'] not in all_fvg]

    print(f"Total new entries added: {len(new_entries)}")
    print(f"  Argumentation cluster (P0-2): {len(arg_entries)} entries")
    print(f"  FVG additions (P1-2): {len(fvg_entries)} net-new")
    print(f"  2024-2026 current-affairs (P1-3): {len(current_entries)} entries")
    print(f"  IDs: {new_entries[0]['id'] if new_entries else 'n/a'} – {new_entries[-1]['id'] if new_entries else 'n/a'}")

    if not new_entries:
        print("Nothing to add.")
        sys.exit(0)

    data.extend(new_entries)

    with open(VOCAB_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')

    print(f"\nFile written. Total entries now: {len(data)}")
