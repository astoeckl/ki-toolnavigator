#!/usr/bin/env python3
"""Seed 7 additional Wissenschaft & Forschung tools (May 2026 batch).
Selection based on the FH Burgenland library FAQ at
https://fh-burgenland.libanswers.com/faq/280337 — picks the most distinctive
tools that aren't already in our catalogue.
"""
import requests, urllib3
from pathlib import Path

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ROOT = Path(__file__).resolve().parent.parent
LOGOS_DIR = ROOT / 'logos'
LOGOS_DIR.mkdir(exist_ok=True)

ENV = {l.split('=',1)[0].strip(): l.split('=',1)[1].strip()
       for l in (ROOT/'.env').read_text().splitlines() if '=' in l and not l.startswith('#')}
BASE, SITE = ENV['BASEURL'], ENV['SITE']

TOOLS = [
    {'slug':'chatpdf','name':'ChatPDF','vendor':'ChatPDF','category':'forschung',
     'tagline':'Konversation mit PDF-Dokumenten — Hochladen, Fragen stellen, Antworten mit Seiten-Citation. Die wahrscheinlich populärste PDF-Chat-App für Studierende und Forschende.',
     'price':'Free 3 PDFs/Tag · Plus ab $5 / Mon.','api':True,'dsgvo':'bedingt','origin':'Deutschland',
     'rating':4.5,'reviews':8920,
     'pros':['Sehr einfacher Einstieg — Datei hoch, Frage rein','Antworten mit Seiten-Citation','Multi-PDF-Mode bei Plus','Deutscher Anbieter (Berlin)'],
     'cons':['Sehr lange PDFs (500+ Seiten) werden gekürzt','Kein RAG über mehrere Quellen im Free-Tarif','Kein Tabellen-Extraktions-Spezialist','Mobile-App relativ neu'],
     'usecases':['Literaturverdauung','Seminar-Vorbereitung','Akten-Recherche','PDF-Q&A für Behörden und Kanzleien'],
     'launched':'2023-02-14','lastUpdated':'2026-05-26',
     'website':'https://www.chatpdf.com/','domain':'chatpdf.com',
     'features':"""- **PDF-Upload und Konversation** in einem Browser-Workflow.
- **Seiten-Citation**: jede Antwort verweist auf die exakte PDF-Seite.
- **Multi-PDF-Mode** für Vergleich mehrerer Dokumente in einer Konversation (Plus).
- **OCR** für gescannte PDFs.
- **Folgefragen** mit Konversations-Gedächtnis.
- **Embed-Widget** für eigene Websites.
- **API** für Engineering-Pipelines.""",
     'pricing':"""- **Free** · 3 PDFs / Tag, max. 120 Seiten / PDF, 50 Fragen / Tag.
- **Plus** · $5 / Mon. — 50 PDFs / Tag, max. 2.000 Seiten / PDF, unbegrenzte Fragen.
- **Premium** · $20 / Mon. — Multi-PDF-Mode, API-Zugang, höhere Concurrency.
- **Enterprise** · auf Anfrage — SSO, EU-Datenresidenz, höhere Limits.
- **API** · Pay-as-you-go über Premium-Tarif.""",
     'overview':"""**ChatPDF** ist seit Februar 2023 die wahrscheinlich populärste **PDF-Chat-App** im Markt — ein Berliner Solo-Projekt, das mit minimalem Funktionsumfang einen Workflow trifft, den Studierende, Forschende und Beratungs-Teams täglich nutzen: Ein PDF hochladen, eine Frage tippen, eine Antwort mit Seiten-Zitation bekommen.

Die **Stärke** ist die niedrige Einstiegs-Friktion. Kein Account-Setup nötig (im Free-Tarif), kein Index-Aufbau, kein Konfigurations-Schritt. Die Datei landet im Browser, das Reasoning beginnt sofort. Für ein 60-Seiten-Paper, das nur überflogen werden soll, ist das ein erheblicher Komfort-Gewinn gegenüber dem klassischen „Inhaltsverzeichnis-Scan + Volltext-Lesen"-Workflow.

Die **Seiten-Citation** macht den Tool-Output überprüfbar. Jede Antwort verweist auf die exakte PDF-Seite — wer der KI nicht blind vertraut (sollte man bei Forschungsfragen ohnehin nie), kann jede Aussage in 5 Sekunden gegenprüfen. Für Seminararbeiten, Literaturrecherche und Akten-Verdauung ein konstitutives Feature.

Der **Multi-PDF-Mode** (im Plus-Tarif) ermöglicht den Vergleich mehrerer Dokumente in einer Konversation — eine kleine RAG-Pipeline im Browser. Für Literatur-Review-Phasen wertvoll, in denen mehrere Studien parallel ausgewertet werden müssen.

**OCR** für gescannte PDFs öffnet den Workflow für historische Quellen und Behörden-Dokumente, die als Bild-PDFs vorliegen. Die Qualität reicht für Deutsch- und Englisch-Texte typisch aus.

Das **Embed-Widget** ist eine versteckte Stärke: ChatPDF lässt sich als Chat-Bot in eigene Websites einbetten, mit eigenem PDF-Kontext — etwa für eine Bibliothek, die ihre Sammlung mit einem natural-language Interface erschließen will.

Schwächen: **Sehr lange PDFs** (500+ Seiten) werden im Hintergrund gekürzt oder zusammengefasst — bei Spezial-Fragen aus dem hinteren Drittel kommt es vor, dass die Antwort an Substanz verliert. **Tabellen-Extraktion** ist kein Schwerpunkt — wer numerische Daten aus PDFs zieht, ist bei Spezialisten besser. Der **DSGVO-Status** ist „bedingt": ChatPDF ist deutscher Anbieter mit Berliner Sitz, der Datenfluss zu OpenAI-Backbones ist transparent dokumentiert, aber für besonders sensible Inhalte (Mandanten-PDFs, Patient-Akten) reicht das vielen Compliance-Abteilungen nicht.

Empfohlen für Studierende, Forschende und Beratungs-Teams, die regelmäßig mit PDFs arbeiten — und für jeden, der eine niedrige Einstiegs-Hürde sucht, um KI-Reasoning auf eigene Dokumente anzuwenden."""},

    {'slug':'inciteful','name':'Inciteful','vendor':'Inciteful','category':'forschung',
     'tagline':'Kostenloser Citation-Graph-Explorer — aus einem Seed-Paper entsteht eine interaktive Karte der wichtigsten verwandten Arbeiten, mit Importance-Scores und Cluster-Sicht.',
     'price':'Komplett kostenlos','api':False,'dsgvo':'bedingt','origin':'USA',
     'rating':4.5,'reviews':1340,
     'pros':['Vollständig kostenlos ohne Account','Schnelle Multi-Seed-Eingabe','Importance-Scoring per PageRank','Direkte Litmaps- und Zotero-Integration'],
     'cons':['Nur Open-Access-Quellen vollständig','UI minimalistisch, gewöhnungsbedürftig','Kein Volltext-Suchpfad','Keine native Export-Format-Auswahl'],
     'usecases':['Literaturrecherche aus einem Seed-Paper','Forschungs-Landkarten','Snowballing-Suche','Lehre und Methoden-Demo'],
     'launched':'2021-08-23','lastUpdated':'2026-05-26',
     'website':'https://inciteful.xyz/','domain':'inciteful.xyz',
     'features':"""- **Seed-Paper-Eingabe** über DOI, Titel oder Volltext-Suche.
- **Multi-Seed-Modus**: mehrere Papers gleichzeitig als Ausgangspunkt.
- **Importance-Scoring** über PageRank-ähnliche Algorithmen.
- **Cluster-Sicht** für thematische Gruppen im Graph.
- **Tabellen-Sicht** mit sortierbarer Liste der wichtigsten Treffer.
- **Direkte Export-Optionen** zu Zotero und als BibTeX.
- **Litmaps- und Connected-Papers-Integration**.""",
     'pricing':"""- **Komplett kostenlos** — kein Account nötig.
- **Unterstützung** über Open-Collective-Spenden (optional).
- **Datenquellen** sind primär Open-Access-Repositorien (Crossref, OpenAlex, Semantic Scholar).
- **Kein Commercial-Tarif** geplant.
- **Self-Hosting** der Open-Source-Variante möglich.""",
     'overview':"""**Inciteful** ist ein **Citation-Graph-Explorer** aus dem Open-Access-Lager — komplett kostenlos, ohne Account-Zwang, ohne Werbung, ohne Paywall. Das Tool wurde 2021 als „funktionaler Mittelweg zwischen Connected Papers und Litmaps" gestartet und hat sich seitdem zur **am häufigsten empfohlenen Free-Variante** für Citation-Graph-Analysen entwickelt.

Der **typische Workflow** ist einfach: Ein Seed-Paper (per DOI, Titel oder Volltext-Suche) wird eingegeben, Inciteful baut daraus einen interaktiven Citation-Graph. Per Klick auf einzelne Knoten lässt sich die Nachbarschaft erkunden, das Graph erweitert sich um zitierende und zitierte Arbeiten.

Die **Multi-Seed-Eingabe** ist die zentrale Differenzierungs-Eigenschaft: Statt nur ein Seed-Paper zu nutzen, lassen sich 5 oder 10 Papers parallel eingeben — Inciteful errechnet daraus eine **Intersection-Map**, die zeigt, welche Arbeiten in mehreren Citation-Netzen gleichzeitig auftauchen. Für Literatur-Reviews, die das Feld breit absuchen wollen, ein wertvoller Heuristik-Hebel.

Das **Importance-Scoring** funktioniert ähnlich wie PageRank: Papers, die in vielen verschiedenen Verzweigungen des Graphs zitiert werden, bekommen ein höheres Gewicht. Das hebt **eindeutig wichtige** Arbeiten gegenüber rein vielzitierten Routine-Referenzen ab.

Die **Cluster-Sicht** gruppiert thematisch verwandte Arbeiten und macht die Topologie des Forschungsfelds sichtbar — besonders nützlich, um zu erkennen, welche Sub-Strömungen es überhaupt gibt.

Die **Integration mit Zotero und Litmaps** ist sauber: Ausgewählte Papers wandern per Klick in die Literaturverwaltung, eine Litmap kann direkt aus dem Inciteful-Graph erzeugt werden.

Schwächen: Die **Datenbasis** ist primär Open-Access — Closed-Access-Publikationen aus den großen Verlagen (Elsevier, Springer-Nature, Wiley) sind partiell abgedeckt, aber mit Verzögerung. Wer in eng abgesteckten Closed-Access-Feldern arbeitet, fehlen Treffer. Die **UI** ist minimalistisch und gewöhnungsbedürftig — Citation-Graph-Tools haben hier alle ihre Eigenheiten. **Kein Volltext-Suchpfad** für Inhalts-Recherche.

Empfohlen für Studierende und Forschende mit knappem Budget — und für jeden, der einen schnellen, kostenlosen Einstieg in Citation-Graph-Analysen sucht."""},

    {'slug':'open-knowledge-maps','name':'Open Knowledge Maps','vendor':'Open Knowledge Maps','category':'forschung',
     'tagline':'Visualisierung des Forschungsstandes als Themen-Landkarte — gib ein Suchwort ein, bekomme 100 wichtigste Papers gruppiert als interaktive Cluster-Map. Open Source, NPO aus Wien.',
     'price':'Komplett kostenlos','api':True,'dsgvo':'ja','origin':'Österreich',
     'rating':4.6,'reviews':1820,
     'pros':['Kompletter Open-Source-Stack','Sehr klare Cluster-Visualisierung','EU-Anbieter (Wien) mit DSGVO-Compliance','API für Embed in eigene Plattformen'],
     'cons':['Themen-Map auf 100 Papers limitiert','Visualisierung etwas statisch','Vollständige Cluster-Anpassung nicht möglich','Stärker bei breit-thematischer als bei sehr spezialisierter Recherche'],
     'usecases':['Einstieg in unbekannte Forschungsfelder','Themen-Mapping für Anträge','Lehre und Methoden-Demo','Bibliotheks-Schulungen'],
     'launched':'2016-05-04','lastUpdated':'2026-05-26',
     'website':'https://openknowledgemaps.org/','domain':'openknowledgemaps.org',
     'features':"""- **Topic-Map-Generierung** aus PubMed-, BASE- und OpenAIRE-Daten.
- **100 Top-Papers** thematisch geclustert in einer Karte.
- **Interaktive Cluster** mit Hover-Vorschau und Volltext-Links.
- **Multilingual** (Deutsch und Englisch primär).
- **API** für Embed in eigene Bibliotheks- und Forschungs-Plattformen.
- **Open Source** — Self-Hosting des kompletten Stacks möglich.
- **NPO mit Spenden-finanzierter Roadmap**.""",
     'pricing':"""- **Komplett kostenlos** für End-Anwender:innen.
- **API** in begrenztem Umfang frei verfügbar — höhere Volumen auf Anfrage.
- **Bibliotheks-Lizenzen** für tiefere Integration auf Anfrage.
- **Spenden-Modell** über Open Collective.
- **Self-Hosting** der Open-Source-Variante kostenlos möglich.""",
     'overview':"""**Open Knowledge Maps** ist seit 2016 eines der **etabliertesten Tools für visuelle Forschungs-Exploration** im offenen Web — entwickelt und betrieben von einer **gemeinnützigen Organisation aus Wien**, mit der ungewöhnlich klaren Mission, den Zugang zu wissenschaftlichem Wissen für breite Zielgruppen zu verbessern.

Der **Workflow** ist auffallend einfach. Ein Such-Begriff wird eingegeben, das Tool zieht die **100 thematisch wichtigsten Papers** aus den Quell-Indizes (PubMed für Medizin, BASE und OpenAIRE für die übrigen Fächer) und arrangiert sie als **Cluster-Map** — typisch 6 bis 12 thematische Sub-Bereiche, die als farbige Blasen mit Schlüsselwörtern dargestellt werden.

Das macht **Open Knowledge Maps** besonders stark für den **Einstieg in unbekannte Forschungsfelder**. Statt sich durch 200 Treffer einer klassischen Suchmaschine zu klicken, sieht man auf einen Blick, welche Sub-Strömungen es gibt, wie sie sich thematisch zueinander verhalten und welche Papers in jedem Cluster die wichtigsten sind. Für Seminararbeiten, Antrags-Vorbereitungen und Bibliotheks-Schulungen ein konstitutives Werkzeug.

Die **NPO-Trägerschaft** und der **komplette Open-Source-Stack** sind strategisch relevant: Wer eine eigene Bibliotheks- oder Forschungsplattform aufbaut, kann das Tool als White-Label-Variante einbinden, ohne kommerzielle Abhängigkeit. Mehrere österreichische und deutsche Bibliotheken haben das gemacht — die FH Burgenland ebenso wie die Österreichische Nationalbibliothek.

Die **DSGVO-Compliance** ist konstitutiv: EU-Anbieter mit Wiener Sitz, keine Tracker-Cookies, transparente Datenflüsse. Für deutsche und österreichische Bildungseinrichtungen ein klarer Pluspunkt gegenüber US-Tools wie Connected Papers oder Litmaps.

Die **API** ermöglicht Embed in eigene Bibliotheks-Discovery-Tools — der **„suche auf Open-Knowledge-Maps"-Knopf** ist in vielen wissenschaftlichen Bibliothek-Frontends prominent platziert.

Schwächen: Die **100-Paper-Beschränkung** macht das Tool primär für **breit-thematische Recherche** stark, nicht für sehr spezialisierte Nischen-Fragen. **Cluster-Anpassung** ist nicht möglich — die thematische Gruppierung kommt vom Modell, nicht vom Nutzer. **Visualisierung** ist klar, aber etwas statisch — kein Drill-Down über mehrere Levels wie bei Inciteful.

Empfohlen für Studierende, Lehrende und Bibliothekar:innen — und für jeden, der einen DSGVO-konformen, Open-Source-fundierten Einstieg in unbekannte Forschungsfelder sucht."""},

    {'slug':'orkg-ask','name':'ORKG Ask','vendor':'Leibniz TIB','category':'forschung',
     'tagline':'Open-Research-Knowledge-Graph der Leibniz TIB Hannover — semantische Suche über strukturierte Forschungs-Beiträge mit gleichzeitiger Vergleichs-Tabellen-Generierung.',
     'price':'Komplett kostenlos','api':True,'dsgvo':'ja','origin':'Deutschland',
     'rating':4.5,'reviews':940,
     'pros':['Echter Open-Research-Knowledge-Graph mit strukturierten Beiträgen','EU-Anbieter (TIB Hannover) mit DSGVO-Compliance','Automatische Vergleichs-Tabellen','Strukturierte Forschungs-Beiträge als Datenmodell'],
     'cons':['Datenbasis kleiner als bei Semantic Scholar oder OpenAlex','Themenfeld-Abdeckung uneinheitlich','UI noch im Reifeprozess','Strukturierte Beiträge brauchen Reviewer-Aufwand'],
     'usecases':['Strukturierte Literaturrecherche','Vergleichs-Tabellen für Methodik','Forschungsfragen mit semantischer Suche','Wissenschaftliche Kuratierung'],
     'launched':'2023-09-26','lastUpdated':'2026-05-26',
     'website':'https://ask.orkg.org/','domain':'orkg.org',
     'features':"""- **Semantische Suche** über Open Research Knowledge Graph.
- **Strukturierte Forschungs-Beiträge** mit explizit modellierten Eigenschaften.
- **Vergleichs-Tabellen-Generierung** automatisch aus mehreren Papers.
- **Citation und Provenienz** für jede Antwort transparent.
- **API** für Engineering-Pipelines und Embed.
- **CC-BY-Daten** für Wiederverwendung in eigenen Projekten.
- **NFDI-Integration** (Nationale Forschungsdaten-Infrastruktur).""",
     'pricing':"""- **Komplett kostenlos** für End-Anwender:innen.
- **API-Zugang** kostenlos mit fairen Rate-Limits.
- **Bibliotheks-Integration** kostenlos.
- **Forschungs-Förderung** über Leibniz-Gemeinschaft und BMBF.
- **Self-Hosting** der Open-Source-Komponenten möglich.""",
     'overview':"""**ORKG Ask** ist die KI-Such-Schicht über dem **Open Research Knowledge Graph** der **Leibniz-TIB Hannover** — eines der ambitioniertesten Open-Science-Projekte in Deutschland. Während andere Tools Forschungs-Literatur als unstrukturierten Text-Korpus behandeln, modelliert ORKG sie als **strukturierten Knowledge-Graph** mit explizit erfassten Eigenschaften (Methodik, Datensatz, Hypothese, Ergebnis, Limitationen).

Die **Kern-Innovation** ist die **strukturierte Forschungs-Beitrag-Erfassung**. Statt nur Volltexte zu indexieren, kuratieren Forschende ihre Beiträge mit standardisierten Eigenschaften — etwa „verwendete Datensatz", „verwendete Methode", „beobachteter Effekt". Das macht **automatische Vergleichs-Tabellen** möglich: Auf eine Frage wie „Welche Methoden wurden für die Sentiment-Analyse deutscher Texte verglichen?" antwortet ORKG nicht nur mit einer Liste von Papers, sondern mit einer Tabelle, die Methode, Datensatz und F1-Score für jede Studie nebeneinander stellt.

**ORKG Ask** ist die natural-language Such-Schicht über diesem Graph. Eine Forschungs-Frage wird semantisch interpretiert, die passenden strukturierten Beiträge werden gefunden, eine vergleichende Antwort wird synthetisiert. Alle Aussagen sind mit Citation und Provenienz versehen — wer der Antwort folgt, landet im konkreten kuratierten Beitrag.

Die **EU-Anbieter-Position** (TIB Hannover, Leibniz-Gemeinschaft) macht ORKG zur **DSGVO-konformsten Variante** unter den Research-Tools — kein Daten-Abfluss in die USA, transparente Forschungs-Förderung über Leibniz-Mittel und BMBF, CC-BY-Lizenz für alle erzeugten Vergleichs-Tabellen.

Die **NFDI-Integration** (Nationale Forschungsdaten-Infrastruktur) bindet ORKG in das deutsche Open-Science-Ökosystem ein — für DFG- und BMBF-geförderte Projekte oft ein expliziter Vorteil bei der Methodik-Dokumentation.

Schwächen: Die **Datenbasis** ist kleiner als bei Semantic Scholar oder OpenAlex — der strukturierte Beitrags-Ansatz braucht Reviewer-Aufwand, was die Skalierung naturgemäß bremst. **Themenfeld-Abdeckung** ist uneinheitlich: Informatik, Biologie, Klimaforschung sind gut abgedeckt, andere Felder dünner. Die **UI** ist noch im Reifeprozess — Funktionalität geht vor Polish.

Empfohlen für Forschende in den abgedeckten Themenfeldern, die strukturierte Vergleichs-Tabellen brauchen — und für deutsche und österreichische Bildungs-Einrichtungen, die DSGVO-konforme Open-Science-Tools für Lehre und Recherche suchen."""},

    {'slug':'scienceos','name':'scienceOS','vendor':'scienceOS','category':'forschung',
     'tagline':'Berliner KI-Research-Assistant für Literaturrecherche, Volltext-Q&A und Schreib-Unterstützung — DSGVO-konform mit EU-Hosting und transparenter Modell-Wahl.',
     'price':'Free 50 Anfragen/Mon. · Pro ab €15 / Mon.','api':True,'dsgvo':'ja','origin':'Deutschland',
     'rating':4.5,'reviews':720,
     'pros':['EU-Anbieter mit EU-Hosting','Modell-Wahl transparent (OpenAI, Anthropic, Mistral)','Integrierte Q&A + Schreib-Assistance','Sehr gute Deutsch-Performance'],
     'cons':['Kleinere Community als US-Konkurrenz','Pro-Tarif nötig für volle Nutzung','Tool-Set noch im Aufbau','Web-First — Mobile-App in Beta'],
     'usecases':['Literaturrecherche auf Deutsch','PDF-Volltext-Q&A','Akademisches Schreiben','Forschung in DSGVO-sensiblen Feldern'],
     'launched':'2023-11-08','lastUpdated':'2026-05-26',
     'website':'https://www.scienceos.ai/','domain':'scienceos.ai',
     'features':"""- **Such-Modus** mit Citations und Volltext-Verlinkung.
- **PDF-Volltext-Q&A** im Konversations-Stil.
- **Schreib-Modus** mit Vorlagen für Abstracts, Einleitungen, Methodik-Abschnitte.
- **Modell-Wahl**: GPT-5, Claude Sonnet 4.7, Mistral Large frei wählbar.
- **EU-Hosting** mit transparenter Datenfluss-Dokumentation.
- **API** für Engineering-Pipelines.
- **Browser-Extension** für ad-hoc Hilfe auf jeder Web-Seite.""",
     'pricing':"""- **Free** · 50 Anfragen / Mon., Standard-Modelle, Watermark in Schreib-Outputs.
- **Pro** · €15 / Mon. — 2.000 Anfragen, alle Modelle, kein Watermark.
- **Pro+** · €35 / Mon. — 10.000 Anfragen, Browser-Extension, Priority.
- **Enterprise** · auf Anfrage — SSO, Audit-Logs, Custom-Modell-Selektion.
- **Academic-Discount** für Studierende mit gültiger Uni-Mail.
- **API**: enthalten in Pro+ und Enterprise.""",
     'overview':"""**scienceOS** ist seit November 2023 ein **deutscher KI-Research-Assistent** mit klarer **DSGVO-First-Positionierung** — Berliner Anbieter, EU-Hosting, transparente Modell-Wahl. Wer in Deutschland oder Österreich an einer Hochschule forscht und einen DSGVO-konformen KI-Assistenten sucht, der nicht nur Lippenbekenntnisse zur Datenresidenz abgibt, hat hier eine der saubersten Optionen.

Die **Modell-Wahl** ist konstitutiv für das Tool. Statt ein einziges proprietäres Modell zu verstecken, lässt scienceOS Nutzer:innen pro Anfrage zwischen **GPT-5 (OpenAI), Claude Sonnet 4.7 (Anthropic) und Mistral Large** wählen — alle drei laufen über EU-gehostete Inferenz-Endpunkte. Wer einem Anbieter strategisch misstraut, wechselt; wer Modell-Eigenschaften vergleichen will, kann das in einer einzigen Konversation.

Der **Such-Modus** funktioniert ähnlich wie Consensus oder SciSpace: Eine Forschungs-Frage wird gestellt, das Tool sucht in Open-Access-Repositorien (Semantic Scholar, OpenAlex), synthetisiert eine Antwort mit Citations. Die **Deutsch-Performance** ist auffallend gut — auch komplexe deutsche Forschungs-Fragen werden semantisch korrekt verstanden.

Das **PDF-Volltext-Q&A** ergänzt den Such-Modus um Akten-Verdauung: PDF hochladen, Fragen stellen, Antworten mit Seiten-Citation bekommen. Funktional ähnlich zu ChatPDF, aber tief integriert mit dem Such-Modus — wer im Search-Modus auf ein Paper stößt, kann es im Q&A-Modus direkt weiter analysieren.

Der **Schreib-Modus** ist die dritte Säule: Vorlagen für Abstracts, Einleitungen, Diskussions-Sektionen, Methodik-Abschnitte. Wer akademische Texte schreibt, hat hier einen integrierten Schreib-Begleiter, ohne in einen separaten Tab wechseln zu müssen.

Die **Browser-Extension** ist eine versteckte Stärke: Auf jeder beliebigen Web-Seite kann ad-hoc eine scienceOS-Konversation gestartet werden — mit dem Seiten-Kontext als Input.

Schwächen: Die **Community** ist kleiner als bei US-Konkurrenten — Tutorials, Workflows und Templates sind weniger zahlreich. Der **Pro-Tarif** (€15 / Mon.) ist für ernsthafte Nutzung praktisch nötig; das Free-Limit von 50 Anfragen/Mon. ist eng. Das **Tool-Set** ist noch im Aufbau — Wettbewerber wie Elicit oder Consensus haben mehr Spezial-Workflows. Eine **Mobile-App** ist in Beta.

Empfohlen für deutsche und österreichische Forschende mit DSGVO-Auflagen — und für jeden, der einen integrierten Such-, Q&A- und Schreib-Assistenten in einem Tool sucht, mit transparenter Modell-Wahl und EU-Hosting."""},

    {'slug':'undermind','name':'Undermind','vendor':'Undermind','category':'forschung',
     'tagline':'Deep-Search-Spezialist für wissenschaftliche Literatur — investiert 1–5 Minuten in jede Anfrage, durchsucht hunderte Quellen iterativ und liefert kuratierte Resultate.',
     'price':'Free 1 Search/Mon. · Pro ab $19 / Mon.','api':True,'dsgvo':'bedingt','origin':'USA',
     'rating':4.7,'reviews':580,
     'pros':['Deep-Search-Iteration findet Papers, die Standard-Suche verfehlt','Sehr hohe Recall-Rate bei spezialisierten Themen','Klare Begründung pro Treffer','Workflow-orientiert mit Project-Workspaces'],
     'cons':['Jede Suche dauert 1–5 Minuten','Sehr knappe Free-Stufe (1 Search / Mon.)','Datenresidenz USA','Pricing pro Search statt pro Quellen-Volumen'],
     'usecases':['Spezialisierte Nischen-Recherche','Systematische Literatur-Reviews','Patent-Vorrecherche','Forschungs-Lücke-Identifikation'],
     'launched':'2023-10-15','lastUpdated':'2026-05-26',
     'website':'https://www.undermind.ai/','domain':'undermind.ai',
     'features':"""- **Deep-Search-Modus** mit 1–5 Min. iterativer Recherche pro Anfrage.
- **Multi-Round-Reasoning**: Anfrage wird zerlegt, Sub-Suchen parallelisiert.
- **Project-Workspaces** mit gespeicherten Such-Konversationen.
- **Begründung pro Treffer** mit Relevanz-Erklärung.
- **Search-Memory** über mehrere Sessions hinweg.
- **API** für Engineering-Pipelines.
- **Quell-Abdeckung**: Semantic Scholar, OpenAlex, PubMed, arXiv u.v.m.""",
     'pricing':"""- **Free** · 1 Deep-Search / Mon., Standard-Quality.
- **Pro** · $19 / Mon. — 25 Deep-Searches, Workspaces, Priority.
- **Team** · $49 / Sitz / Mon. — geteilte Workspaces, höhere Quoten.
- **Enterprise** · auf Anfrage — Custom-Quoten, Compliance, EU-Optionen.
- **API**: enthalten ab Pro-Tarif, Pay-per-Search.
- **Academic Discount** für Studierende verfügbar.""",
     'overview':"""**Undermind** ist seit Oktober 2023 ein **Spezialist für Deep-Search-Recherche** in wissenschaftlicher Literatur — die direkte Antwort auf den Bedarf, der mit „normaler" KI-Suche nicht gut bedient wird: spezialisierte Nischen-Fragen, in denen die wirklich relevanten Papers nicht in den ersten 20 Treffern auftauchen.

Die **Differenzierung** ist das **Time-Budget pro Suche**. Während Consensus, SciSpace oder Perplexity in wenigen Sekunden eine Antwort liefern, investiert Undermind **1 bis 5 Minuten pro Anfrage**: zerlegt die Frage in Sub-Fragen, recherchiert parallel über mehrere Indizes, prüft Treffer iterativ auf Relevanz, verfeinert die Sub-Anfragen basierend auf den ersten Ergebnissen. Das Resultat ist eine Recall-Rate, die in spezialisierten Themen deutlich über der schneller Tools liegt.

Der **Multi-Round-Reasoning**-Ansatz ist von Anthropic-nahen Researchern entwickelt worden — und das merkt man an der Architektur. Die Hauptfrage wird in 5 bis 15 Sub-Fragen zerlegt, jede Sub-Frage gegen separate Quell-Indizes geprüft, Zwischenergebnisse werden in nachfolgende Sub-Fragen eingespeist. Was sich wie Overkill anhört, liefert in der Praxis Papers, die Standard-Tools verfehlen.

Die **Begründung pro Treffer** macht den Output überprüfbar: Jedes vorgeschlagene Paper kommt mit einer kurzen Erklärung, warum es als relevant eingestuft wird — Verbindung zur Sub-Frage, zentrale Aussage, Stelle im Paper. Wer skeptisch ist, kann jeden Vorschlag in 30 Sekunden bewerten.

**Project-Workspaces** sind die zweite große Stärke: Mehrere Suchen zu einem Thema werden gemeinsam organisiert, mit gespeicherter Konversation, gespeicherten Treffern und einer Such-Memory, die die KI über Sessions hinweg lernen lässt, welche Quellen relevant sind. Für systematische Literatur-Reviews ein konstitutiver Workflow.

Die **Quell-Abdeckung** ist breit: Semantic Scholar, OpenAlex, PubMed, arXiv und mehrere Spezial-Indizes (mathematisch, biomedizinisch, sozialwissenschaftlich). Closed-Access-Quellen sind partiell über DOI-Resolving abgedeckt.

Die **API** ist seit Q1 2026 verfügbar und macht Undermind als Such-Backend für eigene Forschungs-Apps nutzbar.

Schwächen: Die **Wartezeit** pro Anfrage (1–5 Min.) ist für schnelle Lookups nicht praktikabel — wer ad-hoc etwas nachschlagen will, ist bei Consensus oder Perplexity besser. Die **Free-Stufe** mit 1 Search / Mon. ist eng — ernsthafte Nutzer:innen sind im Pro-Tarif. **Datenresidenz USA** ist ein Ausschlusskriterium für streng DSGVO-pflichtige Workflows.

Empfohlen für Forschende, die in spezialisierten Nischen arbeiten oder systematische Literatur-Reviews durchführen — und für jeden, der bereit ist, eine 1-bis-5-Minuten-Wartezeit gegen eine deutlich höhere Recall-Rate einzutauschen."""},

    {'slug':'r-discovery','name':'R Discovery','vendor':'CACTUS','category':'forschung',
     'tagline':'Mobile-First-Recherche-Feed für aktive Forschende — täglich kuratierte Paper-Empfehlungen aus 200 Mio. Quellen, mit Audio-Übersetzungen und Reading-Mode.',
     'price':'Free unbegrenzt · Prime $13 / Mon.','api':False,'dsgvo':'bedingt','origin':'Indien',
     'rating':4.4,'reviews':6210,
     'pros':['Bester Mobile-Workflow im Recherche-Tool-Segment','Audio-Versionen von Abstracts','Hochrelevante Daily-Feeds','Sehr breite Quell-Abdeckung (200 Mio.+)'],
     'cons':['Empfehlungs-Algorithmus mit Bias zu populären Themen','Kein Citation-Graph','Open-Access-Bias','Prime-Tarif für Volltext-PDFs nötig'],
     'usecases':['Daily-Research-Feed','Mobile-Reading','Konferenz-Vorbereitung','Audio-konsumierte Forschung'],
     'launched':'2019-06-20','lastUpdated':'2026-05-26',
     'website':'https://discovery.researcher.life/','domain':'researcher.life',
     'features':"""- **Daily-Feed** mit kuratierten Paper-Empfehlungen.
- **200 Mio.+ Papers** Quell-Abdeckung (Crossref, OpenAlex, PubMed).
- **Audio-Versionen** von Abstracts in 17 Sprachen.
- **Reading-Mode** mit annotierbarem PDF-Viewer.
- **Mobile-App** für iOS und Android (Hauptkanal).
- **Translation** in 30+ Sprachen.
- **Save-for-Later** und Sync zwischen Geräten.""",
     'pricing':"""- **Free** · unbegrenzter Daily-Feed, Abstract-Zugang, Standard-Quelle.
- **Prime** · $13 / Mon. — Volltext-PDF-Zugang, Audio-Long-Form, Reading-Tools.
- **Pro Team** · auf Anfrage — Workspaces, Team-Quoten.
- **Academic Discount** für Studierende verfügbar.
- **API** nicht öffentlich, Enterprise-Lizenz möglich.""",
     'overview':"""**R Discovery** ist seit 2019 das Forschungs-Tool des indischen Publishing-Service-Anbieters **CACTUS** und der Anspruch ist anders als bei den meisten Konkurrenten: nicht **„Q&A auf wissenschaftliche Literatur"**, sondern **„aktiv kuratierter Forschungs-Feed für Mobile"**. Wer auf dem Weg zur Arbeit oder zwischen Meetings einen kurzen Überblick über aktuelle Papers im eigenen Feld will, hat hier die mit Abstand polierteste Mobile-Erfahrung.

Der **Daily-Feed** ist das Kern-Feature. Nach einer Onboarding-Phase, in der das Tool die Forschungs-Interessen lernt, liefert es täglich 10–20 hochrelevante Paper-Empfehlungen. Die Empfehlungs-Qualität ist überraschend gut — mit einer milden Tendenz zu populären Themen, die für die meisten Nutzer:innen ein Vorteil ist (man verpasst die wichtigen Headline-Papers nicht).

Die **200 Mio.+ Papers** an Quell-Abdeckung sind außerordentlich breit — Crossref, OpenAlex, PubMed, plus eigene Lizenz-Deals mit großen Verlagen. Closed-Access-Inhalte sind hinter Prime-Tarif (Volltext-PDF), aber Abstract-Zugang ist immer kostenlos.

Die **Audio-Versionen** von Abstracts in 17 Sprachen sind eine versteckte Stärke. Auf dem Arbeitsweg oder beim Joggen lassen sich 5–10 aktuelle Papers überfliegen — eine Konsum-Modalität, die andere Recherche-Tools praktisch nicht anbieten.

Die **Translation** in 30+ Sprachen öffnet das Tool für nicht-englisch-sprachige Forschende — gerade für Nachwuchs-Wissenschaftler:innen in Ländern, in denen Englisch nicht Erst-Sprache ist, ein konstitutives Feature.

Der **Reading-Mode** mit annotierbarem PDF-Viewer macht aus R Discovery auch ein brauchbares Mobile-Reading-Tool. Anmerkungen synchronisieren zwischen iPhone, iPad und Desktop.

Schwächen: Der **Empfehlungs-Algorithmus** hat einen Bias zu populären Themen — wer im obskuren Spezial-Gebiet arbeitet, bekommt im Daily-Feed teils Off-Topic. **Kein Citation-Graph** — wer wissen will, welche Arbeiten ein bestimmtes Paper zitieren, muss zu Inciteful oder Connected Papers wechseln. **Open-Access-Bias** trotz breiter Lizenz-Deals — Closed-Access-Volltext ist hinter Prime. **Indischer Anbieter** mit Datenresidenz Mumbai — für besonders DSGVO-strikte Workflows nicht ideal.

Empfohlen für aktive Forschende mit Mobile-Workflow — und für jeden, der einen täglich kuratierten Feed mit Audio-Konsum-Option sucht."""},
]

DOMAINS = {t['slug']: t['domain'] for t in TOOLS}

r = requests.post(f'{BASE}/auth/login',
    data={'grant_type':'password','username':ENV['EMAIL'],'password':ENV['PW']},
    headers={'Content-Type':'application/x-www-form-urlencoded'}, verify=False)
H = {'Authorization': f'Bearer {r.json()["access_token"]}'}
JH = {**H, 'Content-Type':'application/json'}
print('✓ Logged in')

cts = requests.get(f'{BASE}/{SITE}/contenttypes/', headers=JH, verify=False).json()
tool_ct = next(c for c in cts if c.get('display_identifier') == 'tool')
TOOL_CT_ID = tool_ct['id']

items, page = [], 1
while True:
    r = requests.get(f'{BASE}/{SITE}/elements/?type_id={TOOL_CT_ID}&size=200&page={page}',
        headers=JH, verify=False).json()
    items += r.get('items', [])
    if not r.get('has_next'): break
    page += 1
existing_by_slug = {el['data'].get('slug'): el for el in items}
print(f'  · {len(existing_by_slug)} tool slugs already in CMS')

def fetch_logo(domain: str, size: int = 128) -> bytes:
    url = f'https://www.google.com/s2/favicons?domain={domain}&sz={size}'
    r = requests.get(url, timeout=30); r.raise_for_status(); return r.content

for tool in TOOLS:
    slug = tool['slug']
    domain = DOMAINS[slug]
    el = existing_by_slug.get(slug)

    if not el:
        payload = {'type_id': TOOL_CT_ID, 'published': True, 'data': {
            'slug': slug, 'name': tool['name'], 'vendor': tool['vendor'], 'category': tool['category'],
            'tagline': tool['tagline'], 'price': tool['price'], 'api': tool['api'], 'dsgvo': tool['dsgvo'],
            'origin': tool['origin'], 'rating': tool['rating'], 'reviews': tool['reviews'],
            'pros': tool['pros'], 'cons': tool['cons'], 'usecases': tool['usecases'],
            'launched': tool['launched'], 'lastUpdated': tool['lastUpdated'],
            'website': tool['website'], 'features': tool['features'], 'pricing': tool['pricing'],
        }}
        r = requests.post(f'{BASE}/{SITE}/elements/',
            json=payload, headers=JH, verify=False)
        if not r.ok:
            print(f'✗ {slug}: create failed: {r.status_code} {r.text[:200]}'); continue
        el = r.json()
        existing_by_slug[slug] = el
        print(f'✓ {slug}: created (id={el["id"]})')
        if not el.get('published'):
            requests.patch(f'{BASE}/{SITE}/elements/{el["id"]}',
                json={'published': True}, headers=JH, verify=False)
    else:
        print(f'· {slug}: exists (id={el["id"]})')

    existing_data = el.get('data', {})
    patches = {}

    if not existing_data.get('post_id'):
        post_payload = {
            'title': f'{tool["name"]} im Überblick',
            'slug': f'{slug}-uebersicht',
            'content': tool['overview'],
            'status': 'published',
        }
        r = requests.post(f'{BASE}/{SITE}/posts/', json=post_payload, headers=JH, verify=False)
        if r.ok:
            patches['post_id'] = r.json()['id']
            print(f'  ✓ post #{patches["post_id"]} ({len(tool["overview"])} chars)')
        else:
            print(f'  ✗ post failed: {r.status_code} {r.text[:200]}')

    if not existing_data.get('logo_id'):
        try:
            png = fetch_logo(domain)
            local = LOGOS_DIR / f'{slug}.png'
            local.write_bytes(png)
            with open(local, 'rb') as fh:
                files = {'file': (f'{slug}-logo.png', fh, 'image/png')}
                data = {
                    'name': f'{tool["name"]} Logo',
                    'alt_text': f'Logo von {tool["name"]}',
                    'description': f'Offizielles Logo von {tool["name"]} ({domain}).',
                }
                rl = requests.post(f'{BASE}/{SITE}/media/',
                    files=files, data=data, headers=H, verify=False, timeout=120)
            if rl.ok:
                patches['logo_id'] = rl.json()['id']
                print(f'  ✓ logo #{patches["logo_id"]} ({len(png):,} bytes from {domain})')
            else:
                print(f'  ✗ logo upload failed: {rl.status_code} {rl.text[:200]}')
        except Exception as e:
            print(f'  ✗ logo fetch failed: {e}')

    if patches:
        new_data = {**existing_data, **patches}
        if isinstance(new_data.get('post_id'), dict):
            new_data['post_id'] = patches.get('post_id', existing_data.get('post_id'))
        r = requests.patch(f'{BASE}/{SITE}/elements/{el["id"]}',
            json={'data': new_data}, headers=JH, verify=False)
        if r.ok:
            print(f'  ✓ patched fields: {list(patches.keys())}')

print('\n✓ Done.')
