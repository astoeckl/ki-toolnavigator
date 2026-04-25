#!/usr/bin/env python3
"""Seed 7 forschung-category tools end-to-end (data + features + pricing + overview Post + logo + website).
Idempotent. Then run capture_tool_screenshots.mjs, upload_screenshots.py, generate_tool_images.py.
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
    {'slug':'scispace','name':'SciSpace','vendor':'SciSpace (Typeset)','category':'forschung',
     'tagline':'KI-Reading-Assistant für Forschungspapers — Chat-mit-PDF, automatische Zusammenfassungen und Literaturreviews aus über 280 Mio. Papers.',
     'price':'Free · Premium ab $20 / Mon.','api':False,'dsgvo':'bedingt','origin':'Indien',
     'rating':4.5,'reviews':2310,
     'pros':['280+ Mio. Papers durchsuchbar','Chat-mit-PDF mit Stellenverweisen','Literaturreview-Tabellen automatisch','Paraphrase + Detector + Translator inkludiert'],
     'cons':['Premium-Limit auf 5 PDFs/Tag im Free','Kein deutscher Copilot-Modus','Datenresidenz USA/Indien','Manche Papers nur Open-Access durchsuchbar'],
     'usecases':['Literaturrecherche','Paper-Zusammenfassungen','Methodenvergleich','Reviewer-Vorbereitung'],
     'launched':'2020-09-15','lastUpdated':'2026-04-22',
     'website':'https://typeset.io/','domain':'typeset.io',
     'features':"""- **Search-Engine** über 280 Mio. wissenschaftliche Papers (Open + Closed).
- **Chat-mit-PDF**: Fragen zum Volltext mit Stellenverweisen.
- **Literature-Review-Table**: tabellarische Synthese mehrerer Papers (Methode, Datenset, Ergebnis).
- **AI Detector** und **Paraphraser** für Manuskript-Vorbereitung.
- **Citation Generator** für APA, MLA, Chicago, Harvard, Vancouver.
- **Translator** für 75+ Sprachen, mit Fachterminologie-Erkennung.
- **Browser-Extension** (Chrome) für In-Context-Lookups auf jeder Webseite.""",
     'pricing':"""- **Free** · 5 PDF-Uploads pro Tag, Basis-Suche, 7-Tage-Verlauf.
- **Premium** · $20 / Mon. ($12 jährlich) — unbegrenzte PDFs, Literature-Review-Table, Priority Support.
- **Teams** · $40 / Sitz / Mon. — geteilte Workspaces, gemeinsame Bibliothek.
- **Institutional** · auf Anfrage — Site-Lizenz, SSO, Custom-Embeddings für interne Korpora.
- **Education-Discount** für Studierende und Lehrende auf Antrag.""",
     'overview':"""**SciSpace** (vormals Typeset) ist eine der mächtigsten KI-Suchmaschinen für wissenschaftliche Literatur — und in den letzten zwei Jahren ein zentrales Werkzeug für PhD-Studierende und Forschende geworden. Das Werteversprechen ist breit: Suche, Lesen, Synthese und Schreibhilfe in einem Tool.

Die **Suche** durchforstet über 280 Mio. Papers (Open Access plus große Verlage) und liefert Resultate nicht nur nach Relevanz, sondern mit einer von der KI generierten Drei-Satz-Antwort plus Quellenliste — ähnlich Perplexity, aber wissenschaftlich kuratiert. Das **Chat-mit-PDF**-Feature ist der Kern: Hochgeladene Papers werden volltext-indexiert, jede Antwort der KI verweist auf die genaue Stelle im Dokument.

Die **Literature-Review-Table** ist das herausragende Differenzierungsmerkmal: Mehrere Papers werden zeitgleich analysiert und in einer Tabelle synthetisiert — Spalten wie Methode, Stichprobe, Ergebnis, Limitations werden automatisch befüllt. Für systematische Reviews ein massiver Zeitgewinn.

Schwächen: Im Free-Tarif sind nur 5 PDF-Uploads pro Tag möglich, was für ernsthafte Recherche knapp ist. Die KI-Antworten sind solide, aber nicht immer auf dem Niveau von GPT-5 oder Claude — bei komplexen methodischen Fragen lohnt das Nachhaken.

Empfohlen für Studierende und Forschende, die regelmäßig Literaturrecherchen machen — und ein integriertes Werkzeug statt fünf einzelner Tools (Suche, PDF-Reader, Citation-Manager, Übersetzer, Paraphraser) wollen."""},

    {'slug':'scite','name':'Scite','vendor':'Scite.ai','category':'forschung',
     'tagline':'Smart Citations zeigen, ob ein Paper bestätigt, widersprochen oder nur erwähnt wird — Klassifikation per KI über 1,3 Mrd. Zitationen.',
     'price':'Ab $20 / Mon. · Free-Trial','api':True,'dsgvo':'bedingt','origin':'USA',
     'rating':4.6,'reviews':1850,
     'pros':['Klassifizierte Zitationen (supports/contrasts/mentions)','Citation-Statements im Volltext sichtbar','Browser-Extension auf 30+ Plattformen','Reference-Check für eigene Manuskripte'],
     'cons':['Premium-Pflicht für Volltext-Excerpts','Klassifikation primär in englischer Literatur','Keine deutsche Oberfläche','Smart-Citations weniger gut bei jungen Papers'],
     'usecases':['Evidenz-Prüfung','Peer-Review','Reference-Check','Forschungsfeld-Mapping'],
     'launched':'2018-03-01','lastUpdated':'2026-04-18',
     'website':'https://scite.ai/','domain':'scite.ai',
     'features':"""- **Smart Citations**: KI klassifiziert jede Zitation als supports, contrasts oder mentions.
- **Citation-Statements**: das exakte Zitat-Excerpt aus dem zitierenden Paper, in Sekunden.
- **Reference Check**: lädt das eigene Manuskript hoch und sieht, welche Referenzen widersprochen sind.
- **Custom Dashboards** für Forschungsfelder, Autoren, Institutionen.
- **Assistant** (LLM-Chat) mit Fokus auf Evidenz statt Halluzination.
- **Browser-Extension** für PubMed, Google Scholar, Wikipedia, Web of Science u. v. m.
- **API** für institutionelle Integration in Bibliothekssysteme.""",
     'pricing':"""- **Free Trial** · 7 Tage Vollzugriff.
- **Personal** · $20 / Mon. ($12 jährlich) — Smart Citations, Assistant, Browser-Extension.
- **Institutional** · ab $1.200 / Jahr — Site-Lizenz, SSO, Bibliotheks-Discovery-Layer.
- **Reference Check** · in Personal enthalten, 25 Manuskripte pro Monat.
- **API-Zugang** · auf Anfrage, Pay-per-call oder Flatrate.
- 30-Tage-Geld-zurück-Garantie.""",
     'overview':"""**Scite** beantwortet eine Frage, die Google Scholar nicht stellt: Wie wurde dieses Paper zitiert — bestätigend, widersprechend oder nur am Rande erwähnt? Die Antwort darauf entscheidet oft, ob ein Forschungsergebnis robust ist oder längst überholt.

Der Kern ist die **Smart-Citation-Datenbank** mit über 1,3 Mrd. klassifizierten Zitationen. Ein eigens trainiertes KI-Modell liest die zitierende Stelle und entscheidet, ob das Original-Paper als Beleg, als Gegenbeweis oder neutral verwendet wird. Im Tool sieht man pro Paper drei Zähler — und kann jede einzelne Zitation als Excerpt im Originalkontext öffnen.

Die **Reference-Check**-Funktion ist für Autorinnen Gold wert: Manuskript hochladen, und Scite prüft jede Referenz auf widersprechende Folgepublikationen. Eine Vorab-Reviewer-Prüfung, die manche Embarrassment vor der Submission verhindert.

Die **Browser-Extension** ist der Alltagshelfer: Beim Lesen von PubMed, Google Scholar oder Wikipedia werden Smart-Citation-Badges direkt eingeblendet. Wer regelmäßig Literatur sichtet, will sie nicht mehr missen.

Schwächen: Die Klassifikation funktioniert in englischer Literatur deutlich besser als in deutscher oder spanischer. Junge Papers (< 2 Jahre) haben naturgemäß wenige Smart Citations — ein Henne-Ei-Problem. Und der Premium-Preis von $20/Monat ist für Studierende ohne institutionellen Zugang spürbar.

Empfohlen für Forschende, die Evidenzbewertung systematisch betreiben — und für jeden, der vor dem Zitieren prüfen will, ob ein Paper in der Community noch als gültig gilt."""},

    {'slug':'researchrabbit','name':'ResearchRabbit','vendor':'ResearchRabbit','category':'forschung',
     'tagline':'Spotify-für-Papers: visuelle Discovery-Engine mit Citation-Networks und automatischen Empfehlungen — 100 % kostenlos.',
     'price':'Komplett kostenlos','api':False,'dsgvo':'bedingt','origin':'USA',
     'rating':4.7,'reviews':3120,
     'pros':['Vollständig kostenlos','Visuelle Citation-Networks','Automatische Empfehlungen pro Sammlung','Zotero-Integration'],
     'cons':['Kein Volltext-Suche','Englischsprachige Literatur dominiert','Kein KI-Chat (anders als SciSpace)','Datenresidenz USA'],
     'usecases':['Literatur-Exploration','Citation-Tracking','Reading-List-Aufbau','Forschungsfeld-Karten'],
     'launched':'2021-08-01','lastUpdated':'2026-04-20',
     'website':'https://www.researchrabbitapp.com/','domain':'researchrabbitapp.com',
     'features':"""- **Collections**: Papers in Sammlungen organisieren, ResearchRabbit empfiehlt automatisch ähnliche.
- **Citation-Network-Graphen**: visuelles Mapping von Vor- und Nachfolge-Papers.
- **Author-Tracking**: neue Publikationen wichtiger Autoren automatisch erkennen.
- **Earlier Work / Later Work / Similar Work** in einem Klick aus jedem Paper.
- **Zotero-Sync** bidirektional.
- **E-Mail-Updates** über neue Empfehlungen pro Sammlung.
- **Kollaborative Sammlungen** zum Teilen mit Co-Autoren.""",
     'pricing':"""- **Komplett kostenlos** für alle Funktionen.
- **Keine Sitz-Lizenzen**, keine Limits.
- Finanzierung über Förderungen und institutionelle Partnerschaften.
- **Premium-Modell** ist nicht angekündigt — Roadmap setzt auf Spenden und institutionelle Verträge.
- **Zotero-Integration** ohne Aufpreis.""",
     'overview':"""**ResearchRabbit** wird oft als „Spotify für Forschungspapers" bezeichnet — und der Vergleich passt. Statt einer klassischen Suchmaske startet das Tool mit einem oder mehreren Seed-Papers, baut daraus ein Citation-Netzwerk und schlägt automatisch verwandte Arbeiten vor, sortiert nach „Similar Work", „Earlier Work" und „Later Work".

Die **Visualisierung** ist der wahre Star: Jedes Paper wird als Knoten dargestellt, Verbindungen zeigen Zitationen, Cluster färben sich nach Themen. Wer ein neues Forschungsfeld erschließt, sieht in Minuten, welche Arbeiten zentral sind und wo die Cluster liegen — eine Übersicht, die mit einer linearen Trefferliste in Google Scholar Stunden bräuchte.

**Author-Tracking** ist subtil aber mächtig: Wichtige Autoren in einer Sammlung lassen sich abonnieren, ResearchRabbit benachrichtigt bei neuen Publikationen. Die **Zotero-Integration** schließt den Workflow: Sammlungen wandern direkt in den eigenen Reference-Manager.

Schwächen: Es gibt kein Volltext-Suche, kein Chat-mit-PDF und keine KI-generierten Zusammenfassungen. ResearchRabbit ist puristisch eine Discovery-Engine — kein All-in-One-Reading-Assistant wie SciSpace. Wer Synthese braucht, nutzt es als Ergänzung, nicht als Ersatz.

Empfohlen für jeden, der ein neues Forschungsfeld erschließt oder bestehende Sammlungen systematisch erweitern will. Bemerkenswert: vollständig kostenlos und ohne Werbung — eine seltene Kombination im KI-Tool-Markt."""},

    {'slug':'connected-papers','name':'Connected Papers','vendor':'Connected Papers','category':'forschung',
     'tagline':'Visuelle Paper-Graphen aus Co-Citation-Analyse — sieht den lokalen Kontext eines Papers in Sekunden.',
     'price':'Free (5 Graphen/Mon.) · Pro ab $6 / Mon.','api':True,'dsgvo':'bedingt','origin':'Israel',
     'rating':4.6,'reviews':2740,
     'pros':['Sehr klare Visualisierung','Co-Citation statt direkte Zitation','Prior + Derivative Work in eigenen Tabs','Open-Access-Filter'],
     'cons':['5 Graphen/Mon. im Free knapp','Kein KI-Chat oder Volltext-Reading','Datenbasis Semantic Scholar (Lücken)','Keine deutsche Oberfläche'],
     'usecases':['Paper-Exploration','Verwandte Werke finden','Forschungslandschaft kartieren','Lit-Review-Anstoß'],
     'launched':'2020-07-21','lastUpdated':'2026-04-15',
     'website':'https://www.connectedpapers.com/','domain':'connectedpapers.com',
     'features':"""- **Graph-View**: Co-Citation-basierte Visualisierung verwandter Papers.
- **Prior Work**: häufig zitierte Vorgänger in eigenem Tab.
- **Derivative Work**: aktuelle Papers, die das Seed-Paper nutzen.
- **Open-Access-Filter** zeigt nur frei lesbare Treffer.
- **Knoten-Größe = Citation-Count**, Farbintensität = Erscheinungsjahr.
- **Bibliographie-Export** in BibTeX, RIS und Zotero-Format.
- **API** für institutionelle Integrationen.""",
     'pricing':"""- **Free** · 5 Graphen pro Monat, alle Kernfeatures.
- **Academic** · $6 / Mon. ($60 jährlich) — unbegrenzte Graphen, 25 % Studierenden-Discount.
- **Business** · $20 / Mon. — kommerzielle Nutzung, Priority Support.
- **API** · ab $99 / Mon. für institutionelle Lizenzen.
- **Bulk-Lizenzen** für Bibliotheken auf Anfrage.""",
     'overview':"""**Connected Papers** ist das visuelle Werkzeug, das man sich wünscht, wenn man ein einzelnes wichtiges Paper hat und schnell verstehen will, in welchem Forschungskontext es steht. Aus dem Seed-Paper wird ein Graph generiert, der nicht direkte Zitationen zeigt, sondern **Co-Citation-Muster**: Welche Papers werden gemeinsam mit dem Seed-Paper zitiert?

Das Ergebnis ist eine Karte des „lokalen Forschungsfelds" — typischerweise 30–50 Papers, gruppiert nach inhaltlicher Nähe. Knoten-Größe steht für Zitationszahl, Farbintensität für Erscheinungsjahr, Verbindungen für Co-Citation-Stärke. In wenigen Sekunden ist klar, welche Arbeiten zentral sind und welche Untercluster existieren.

**Prior Work** und **Derivative Work** sind eigene Tabs: häufig zitierte Vorgänger des Seed-Papers und neuere Arbeiten, die es selbst zitieren. Beide ergänzen den Co-Citation-Graphen um die direkte Vor- und Folge-Linie.

Connected Papers ist bewusst minimalistisch — kein Chat, kein PDF-Reader, keine Synthese. Es macht eine Sache, und die exzellent: ein Paper im Forschungskontext sichtbar machen.

Schwächen: 5 Graphen pro Monat im Free-Tarif sind wenig, der Pro-Tarif mit $6/Mon. aber fair. Die Datenbasis kommt von Semantic Scholar und hat in randständigen Disziplinen Lücken.

Empfohlen als Teil eines Toolstacks: Connected Papers für die visuelle Exploration, ResearchRabbit für die Sammlungspflege, SciSpace oder Scite für die inhaltliche Tiefe."""},

    {'slug':'semantic-scholar','name':'Semantic Scholar','vendor':'Allen Institute for AI','category':'forschung',
     'tagline':'KI-getriebene Open-Access-Suchmaschine für 220 Mio. wissenschaftliche Papers — vom Allen Institute for AI, vollständig kostenlos.',
     'price':'Komplett kostenlos','api':True,'dsgvo':'bedingt','origin':'USA',
     'rating':4.5,'reviews':4280,
     'pros':['220+ Mio. Papers, alle Felder','TLDR-Zusammenfassungen pro Paper','Open Research Corpus für Forscher','Kostenlose API mit großzügigen Limits'],
     'cons':['UI weniger ausgeklügelt als SciSpace','Kein Chat mit eigenen PDFs','TLDRs nicht für alle Papers verfügbar','Datenresidenz USA'],
     'usecases':['Allgemeine Literatursuche','Citation-Recherche','API-Integration','Open-Data-Forschung'],
     'launched':'2015-11-01','lastUpdated':'2026-04-23',
     'website':'https://www.semanticscholar.org/','domain':'semanticscholar.org',
     'features':"""- **Suche** über 220+ Mio. Papers aus allen Disziplinen.
- **TLDR**: KI-generierte Ein-Satz-Zusammenfassung pro Paper.
- **Influential Citations**: gewichtete Liste der wichtigsten Folge-Papers.
- **Author Pages** mit Publikationsverlauf und H-Index-Analytics.
- **Recommendations** auf Basis gelesener Papers (mit Account).
- **Open API** mit ~5000 Requests/sec für institutionelle Nutzung.
- **Semantic Reader** Beta mit interaktiven Zitations-Hover-Cards.""",
     'pricing':"""- **Komplett kostenlos** für alle Endnutzer.
- **Keine Premium-Stufe**, keine Sitz-Lizenzen.
- Finanzierung durch das **Allen Institute for AI** (Paul Allen Foundation).
- **API** kostenlos mit fairer Nutzung — Sonderkonditionen für hohe Volumina auf Anfrage.
- **Open Research Corpus** zum Download für akademische Forschung.""",
     'overview':"""**Semantic Scholar** ist die Open-Access-Suchmaschine, die das Allen Institute for AI 2015 gestartet hat — und seitdem zur unverzichtbaren Infrastruktur für Forschende und Tool-Entwickler geworden ist. Mit über 220 Mio. indexierten Papers aus allen Disziplinen ist sie eine der größten frei zugänglichen Wissenschaftsdatenbanken.

Die **TLDR-Zusammenfassungen** sind das KI-Markenzeichen: Eine selbst trainierte Modellfamilie generiert pro Paper einen Ein-Satz-Abstract, der oft präziser ist als der vom Autor verfasste. Bei rund 80 % der Papers ist eine TLDR verfügbar — nützlich beim Schnellscreening von Trefferlisten.

**Influential Citations** ist eine versteckte Stärke: Statt aller Zitationen wird eine gewichtete Liste der wichtigsten Folge-Arbeiten angezeigt — basierend darauf, wie zentral das Paper im Citation-Kontext war. Spart oft Stunden manueller Recherche.

Die **Open API** ist der eigentliche Hebel für die Tool-Landschaft: Connected Papers, ResearchRabbit, Elicit und viele weitere Tools nutzen Semantic Scholar als Datenquelle. Die Lizenzbedingungen sind Forscher-freundlich, der Open Research Corpus steht zum Bulk-Download bereit.

Schwächen: Die Web-UI ist funktional, aber weniger ausgeklügelt als kommerzielle Alternativen. Es gibt kein Chat-mit-PDF-Feature und keine Workflow-Tools für Literaturreviews — Semantic Scholar ist primär Suchmaschine und Datenquelle, kein All-in-One-Workspace.

Empfohlen als Standardstart-Tool für jede Literaturrecherche und als API-Backbone für eigene Forschungs-Tools — kostenlos, gemeinnützig, ohne Datenverkauf an Werbenetzwerke."""},

    {'slug':'litmaps','name':'Litmaps','vendor':'Litmaps','category':'forschung',
     'tagline':'Live-Citation-Maps mit automatischen Updates — die eigene Reading-List wird zur überwachten Forschungslandkarte.',
     'price':'Free (1 Map) · Pro ab $10 / Mon.','api':False,'dsgvo':'bedingt','origin':'Neuseeland',
     'rating':4.6,'reviews':1490,
     'pros':['Live-Updates: neue Papers werden in Map eingespielt','Klare Wachstumsvisualisierung über Zeit','Discovery-Modus mit „Nahe Nachbarn"','Mendeley + Zotero-Sync'],
     'cons':['Free-Tarif auf 1 aktive Map limitiert','Lernkurve größer als Connected Papers','Kein Chat oder Volltext-Reading','Wenig deutsche Literatur indexiert'],
     'usecases':['Live-Monitoring von Themenfeldern','Systematische Reviews','Reading-List-Pflege','Gap-Analyse'],
     'launched':'2018-09-01','lastUpdated':'2026-04-17',
     'website':'https://www.litmaps.com/','domain':'litmaps.com',
     'features':"""- **Live-Maps**: Citation-Graphen, die sich automatisch mit neuen Papers aktualisieren.
- **Seed Papers**: Map aus 1–N Startartikeln aufbauen.
- **Discovery-Modus**: KI schlägt nahe Nachbarn vor, Aufnahme per Klick.
- **Citation-Updates per E-Mail** wöchentlich oder monatlich.
- **Forschungslücken-Analyse** durch Cluster-Visualisierung.
- **Sync** mit Zotero, Mendeley, EndNote.
- **Team-Workspaces** für gemeinsame systematische Reviews.""",
     'pricing':"""- **Free** · 1 aktive Map, max. 25 Seed-Papers.
- **Pro** · $10 / Mon. ($96 jährlich) — unbegrenzte Maps, alle Discovery-Tools.
- **Pro Annual + Reviews** · $190 / Jahr — inkl. Systematic-Review-Tools.
- **Teams** · $25 / Sitz / Mon. — geteilte Workspaces.
- **Institutional** · auf Anfrage — Site-Lizenz, SSO, Custom-Onboarding.
- 25 % Discount für Studierende mit verifiziertem Status.""",
     'overview':"""**Litmaps** unterscheidet sich von Connected Papers und ResearchRabbit durch einen einzigen, aber zentralen Aspekt: die Citation-Maps sind **lebendig**. Neue Papers, die in das Forschungsfeld einer bestehenden Map passen, werden automatisch erkannt und vorgeschlagen — wer eine Map als Reading-List pflegt, bekommt regelmäßige Updates per E-Mail.

Der **Workflow** beginnt mit Seed Papers (1 bis ~25 Startartikeln). Litmaps generiert daraus eine visuelle Map, in der Knoten Papers darstellen und Verbindungen Zitationen abbilden. Anders als Connected Papers ist die Visualisierung als Zeitachse organisiert — man sieht das Wachstum eines Forschungsfelds über die Jahre.

Der **Discovery-Modus** schlägt „nahe Nachbarn" vor: Papers, die im Citation-Netzwerk nah am bestehenden Cluster liegen, aber noch nicht in der Map sind. Per Klick aufnehmen und die Map wächst kontrolliert.

**Live-Updates** sind das Killer-Feature für Doktoranden und Systematic-Review-Teams: Wer ein Forschungsfeld über Jahre verfolgt, will neue zentrale Publikationen nicht händisch suchen müssen. Die wöchentlichen E-Mails fassen neue Treffer pro Map zusammen — manchmal 0, manchmal 5, immer kuratiert.

Schwächen: Der Free-Tarif ist mit 1 aktiver Map und 25 Seed-Papers spürbar enger als bei Connected Papers. Die Lernkurve ist größer — wer nur schnell ein Forschungsfeld erkunden will, ist mit Connected Papers in 30 Sekunden weiter.

Empfohlen für Doktorand:innen und Forschende, die ein Themenfeld langfristig verfolgen und systematische Literaturreviews planen — Litmaps ist hier das ausgereifteste Werkzeug am Markt."""},

    {'slug':'scholarcy','name':'Scholarcy','vendor':'Scholarcy','category':'forschung',
     'tagline':'KI-Zusammenfassungen für lange Papers — Flashcards mit Kernpunkten, Robustheit-Analyse und automatischen Glossaren.',
     'price':'Free Browser-Ext. · Premium ab $7 / Mon.','api':True,'dsgvo':'bedingt','origin':'UK',
     'rating':4.4,'reviews':1320,
     'pros':['Strukturierte Flashcards statt Fließtext-Summary','Robustheit-Score pro Paper','Automatische Glossare wissenschaftlicher Begriffe','Browser-Extension kostenlos'],
     'cons':['Premium-Pflicht für Bulk-Uploads','Lange Papers (>50 Seiten) brechen Karten ab','UI-Design altbacken','Keine eigene Suchfunktion'],
     'usecases':['Schnelles Paper-Screening','Vorlesungs-Vorbereitung','Reading-List-Triage','Kommentierte Bibliografien'],
     'launched':'2018-04-01','lastUpdated':'2026-04-12',
     'website':'https://www.scholarcy.com/','domain':'scholarcy.com',
     'features':"""- **Flashcards**: strukturierte Summary mit Sektionen (Hintergrund, Methode, Ergebnis, Limitations).
- **Robustness-Indicator**: Bewertet Studie nach Stichprobe, Methode und Ko-Konfundern.
- **Glossar**: extrahiert wissenschaftliche Fachbegriffe und definiert sie.
- **Reference-Liste** mit Verlinkung zu Open-Access-Quellen.
- **Browser-Extension** funktioniert auf jeder Webseite und PDF-URL.
- **Bulk-Upload** für Premium-Nutzer (bis 100 Papers gleichzeitig).
- **API** für Bibliotheks- und LMS-Integrationen.""",
     'pricing':"""- **Free Browser-Extension** · unbegrenzte Einzel-Summaries.
- **Browser Library** · $7 / Mon. — eigene Bibliothek, Export in Word/Excel.
- **Personal Library** · $9 / Mon. — alle Features, Bulk-Upload bis 100/Monat.
- **Academic License** · ab $1.500 / Jahr — institutionelle Site-Lizenz.
- **API** · individuell verhandelbar, auf Volumen-Basis.""",
     'overview':"""**Scholarcy** löst ein konkretes Problem: Wer 30 PDFs in der Reading-Liste hat, will nicht 30 Mal eine Stunde lesen, um zu entscheiden, welche 5 wirklich relevant sind. Die Antwort sind strukturierte **Flashcards** — kompakte Summaries mit klarer Sektionierung statt verlustigem Fließtext.

Eine Scholarcy-Karte zeigt typischerweise: zentrale Forschungsfrage, verwendete Methode, Stichprobe, wichtigste Ergebnisse, Limitations, Schlüsselbefunde der Diskussion. Das macht das Triage-Lesen deutlich schneller — typischerweise 2–3 Minuten pro Paper statt 30–60.

Das **Robustness-Indicator** ist ein nützliches Hilfsmittel: Scholarcy bewertet Studien nach Stichprobengröße, Methodenklarheit und Erwähnung von Ko-Konfundern und gibt einen Score. Kein Ersatz für eigene Methodenkritik, aber ein hilfreicher erster Filter.

Die **kostenlose Browser-Extension** ist die häufigste Eintrittstür: Auf einer beliebigen Paper-URL ein Klick, fertig ist die Zusammenfassung. Wer das Tool intensiver nutzt, braucht das Premium-Abo für die persistente Bibliothek und Bulk-Uploads.

Schwächen: Die UI wirkt etwas in die Jahre gekommen, lange Papers (>50 Seiten) erzeugen mitunter unvollständige Karten, und es gibt keine eigene Suchfunktion — Scholarcy ist Reading-Tool, keine Discovery-Engine.

Empfohlen als kostengünstiges Triage-Werkzeug für jeden, der regelmäßig viele Papers screenen muss — und für Lehrende, die Studierenden vorstrukturierte Lesematerialien bereitstellen wollen."""},
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
        # Create element with all base data; new elements default to published=False
        # so we explicitly publish below after creation.
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
        # Belt-and-braces publish flip — some Cognitor versions ignore `published` in POST.
        if not el.get('published'):
            requests.patch(f'{BASE}/{SITE}/elements/{el["id"]}',
                json={'published': True}, headers=JH, verify=False)
    else:
        print(f'· {slug}: exists (id={el["id"]})')

    existing_data = el.get('data', {})
    patches = {}

    # Overview Post
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

    # Logo
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
