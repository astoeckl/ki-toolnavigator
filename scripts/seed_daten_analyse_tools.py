#!/usr/bin/env python3
"""Seed 7 daten-analyse tools end-to-end (data + features + pricing + overview Post + logo + website).
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
    {'slug':'powerbi-copilot','name':'Power BI Copilot','vendor':'Microsoft','category':'daten-analyse',
     'tagline':'AI-Funktion in Microsoft Fabric / Power BI — Berichte, DAX und Erklärungen aus dem Datenmodell heraus.',
     'price':'Inklusive in Power BI Premium / Fabric F64+','api':False,'dsgvo':'bedingt','origin':'USA',
     'rating':4.2,'reviews':2410,
     'pros':['Tief im Microsoft-Stack (Fabric, OneLake)','Reports aus Prompt erzeugbar','DAX-/M-Erklärungen im Editor','Tenant-Daten verlassen Microsoft 365 nicht'],
     'cons':['Erst ab F64-Capacity (sehr teuer)','Qualität abhängig vom semantischen Modell','EU-Datenresidenz nur mit Multi-Geo-Aufpreis'],
     'usecases':['Self-Service-BI','Report-Prototypen','DAX-Lernen','Executive-Q&A'],
     'launched':'2023-05-23','lastUpdated':'2026-04-22',
     'website':'https://www.microsoft.com/en-us/power-platform/products/power-bi','domain':'microsoft.com',
     'features':"""- **Prompt → Bericht**: komplette Power-BI-Seiten aus einem Satz erstellen lassen.
- **DAX-Generation**: Maße und Spalten in natürlicher Sprache beschreiben.
- **Visual-Erklärungen**: jede Visualisierung zusammenfassen lassen.
- **Q&A** über das semantische Modell, mit Vorschlägen für Folgefragen.
- **Quick-Measure-Vorschläge** beim Modellieren.
- Verfügbar in Fabric **Notebooks**, **Data Factory** und **Real-Time Intelligence**.""",
     'pricing':"""- **Voraussetzung**: Power BI Premium per Capacity oder Microsoft Fabric ab **F64**.
- **Fabric F64** · ab ca. **€9.000 / Mon.** (Pay-as-you-go) — alle Copilot-Funktionen inklusive.
- Reservierte Kapazität (1-Year-Reserve) etwa 40 % günstiger.
- Power BI Pro (€10/User) und PPU (€20/User) **enthalten kein Copilot**.
- Microsoft 365 Copilot ist getrennt davon zu lizenzieren.""",
     'overview':"""**Power BI Copilot** ist Microsofts AI-Layer über dem populärsten Self-Service-BI-Tool der Welt — und nur sinnvoll für Organisationen, die ohnehin auf Power BI / Microsoft Fabric setzen. Die Stärke liegt in der nahtlosen Einbettung: Copilot kennt das semantische Modell, die Beziehungen, Maße und Hierarchien — und kann darauf basierend ganze Berichtsseiten oder DAX-Maße erzeugen.

Die wichtigsten Anwendungsfälle: **Prompt → Bericht** (eine Self-Service-Power-User skizziert eine Frage, Copilot baut die Visuals dazu), **DAX-Generation** (Maße in natürlicher Sprache beschreiben statt von Hand zu schreiben) und **Visual-Erklärungen** (jede Grafik zusammenfassen lassen — wertvoll für Executive-Dashboards). Auch **Microsoft Fabric Notebooks** und Data Factory haben Copilot-Integrationen.

Die Hürde ist die Lizenzierung: Erst ab **Fabric F64** (rund €9.000/Monat) ist Copilot eingeschlossen. Power-BI-Pro/PPU-Kunden bleiben außen vor. Damit richtet sich die Funktion klar an Konzerne und Mittelstand mit Fabric-Investment, nicht an Einzel-Analysten.

Empfohlen für Microsoft-365-Häuser, die bereits in Fabric oder Power BI Premium investiert sind und Self-Service-Analytics auf eine breitere Nutzergruppe öffnen wollen."""},

    {'slug':'thoughtspot','name':'ThoughtSpot Spotter','vendor':'ThoughtSpot','category':'daten-analyse',
     'tagline':'Such-getriebene BI-Plattform mit AI-Agent Spotter — komplexe Folgefragen in natürlicher Sprache, Antworten mit Quellen.',
     'price':'Pro $1.250 / Mon. · Enterprise auf Anfrage','api':True,'dsgvo':'bedingt','origin':'USA',
     'rating':4.4,'reviews':880,
     'pros':['Hochskalierbarer Search-First-Ansatz','Spotter führt Multi-Step-Analysen autonom aus','Embedded Analytics tief integrierbar','Strong Live-Query-Engine'],
     'cons':['Teurer Einstiegspreis','Setup des Worksheets aufwändig','Enterprise-Funktionen erst ab teurerer Stufe'],
     'usecases':['Self-Service-Analytics','Embedded BI','Datenexploration','Anomalie-Erkennung'],
     'launched':'2014-05-01','lastUpdated':'2026-04-19',
     'website':'https://www.thoughtspot.com/','domain':'thoughtspot.com',
     'features':"""- **Spotter Agent**: führt Multi-Step-Analysen aus, mit Plan und Quellen-Trace.
- **Search Bar Insights**: Frage tippen, Antwort + passende Visualisierung.
- **SpotIQ**: automatische Anomalie- und Korrelationserkennung.
- **Live Query Engine** auf Snowflake, BigQuery, Databricks, Redshift.
- **Embedded Analytics SDK** für Drittanwendungen.
- **Liveboards** statt klassischer Dashboards.""",
     'pricing':"""- **Free Trial** · 14 Tage, 5 Nutzer, alle Features.
- **Team** · ab $1.250 / Mon. — 5 Editor-Nutzer, 25 Viewer, 3 Connections.
- **Pro** · auf Anfrage — größere Teams, Live-Query, mehr Connections.
- **Enterprise** · auf Anfrage — SSO, RBAC, Customer-Managed Keys, dediziertes Onboarding.
- **Spotter Agent** ist im Pro/Enterprise-Tarif enthalten.""",
     'overview':"""**ThoughtSpot** war einer der Pioniere der search-driven Analytics: Statt Dashboards mit fixen KPIs zu pflegen, tippt der Anwender seine Frage in die Suche und bekommt unmittelbar eine passende Visualisierung. Mit **Spotter** ist 2024 ein Agentic-AI-Layer dazugekommen, der Multi-Step-Analysen eigenständig durchführt — inklusive Plan, Source-Tracing und natürlichsprachiger Erklärung.

Die Plattform glänzt mit einer **Live-Query-Engine**, die direkt auf Snowflake, BigQuery, Databricks und Redshift läuft — ohne Datenkopie und ohne Cube. Das skaliert zuverlässig auf Milliarden Zeilen. **SpotIQ** entdeckt Anomalien und Korrelationen automatisch und schlägt sie als Insights vor. **Liveboards** ersetzen klassische Dashboards mit suchbaren, drill-down-fähigen Ansichten.

Die Schwächen sind ähnlich wie bei den meisten Enterprise-BI-Tools: hoher Einstiegspreis, aufwändige Einrichtung der "Worksheets" (semantische Modellierungs-Layer), und Funktionen wie SSO oder Customer-Managed Keys sind erst auf höheren Tarifen verfügbar.

Empfohlen für mittelständische und große Unternehmen mit modernem Cloud-Data-Warehouse, die Self-Service-BI für viele Anwender öffnen wollen — und für Software-Anbieter, die Embedded-Analytics in ihre eigenen Apps einbauen."""},

    {'slug':'databricks-genie','name':'Databricks AI/BI Genie','vendor':'Databricks','category':'daten-analyse',
     'tagline':'Conversational-Analytics-Layer auf Databricks Lakehouse — Text-to-SQL mit Unity-Catalog-Awareness.',
     'price':'Inklusive in Databricks Premium-Workspaces','api':True,'dsgvo':'ja','origin':'USA',
     'rating':4.3,'reviews':620,
     'pros':['Direkt auf Lakehouse-Daten ohne Replikation','Unity Catalog versteht Berechtigungen, Lineage','Custom-Instruktionen je Genie-Space','Kostengünstig im Vergleich zu BI-Tools'],
     'cons':['Setup eines guten Genie-Space braucht Zeit','Nur als Conversation-Modul, kein Dashboard-Builder','Visualisierungs-Optionen begrenzt'],
     'usecases':['Self-Service-SQL','Internal Data Q&A','Embedded Analytics in Apps','Data-Steward-Reviews'],
     'launched':'2024-06-12','lastUpdated':'2026-04-21',
     'website':'https://www.databricks.com/product/ai-bi','domain':'databricks.com',
     'features':"""- **Genie Spaces**: kuratierte Domain-spezifische Q&A-Bereiche.
- **Text-to-SQL** mit Unity-Catalog-Beschreibungen, Synonymen und Beispielen.
- **Plan-Erklärung** vor jeder Ausführung, mit "Trust"-Feedback-Loop.
- **Visualisierungen** automatisch oder konfigurierbar.
- **Embeddable** via SDK in eigene Apps.
- **Kostenkontrolle** pro Workspace via DBU-Limits.""",
     'pricing':"""- **Inklusive** in Databricks Premium- und Enterprise-Workspaces.
- DBU-basierte Abrechnung: Genie-Queries verbrauchen Compute-DBUs.
- Ungefähr **$0.40 – $1.20 pro Query**, abhängig von Cluster-Größe und SKU.
- Custom Genie Models (Beta) ab Enterprise-Workspace.
- Für reine Auswertungs-Use-Cases günstiger als klassische BI-Plattformen.""",
     'overview':"""**Databricks AI/BI Genie** ist Databricks' Antwort auf die Frage, wie Anwender ohne SQL-Kenntnisse den Lakehouse anzapfen können — ohne dass die Daten ein zweites Mal in eine BI-Plattform kopiert werden. Das spart Pipeline-Komplexität und nutzt Unity Catalog als Single Source of Truth für Berechtigungen, Lineage und Beschreibungen.

Das Konzept dreht sich um **Genie Spaces**: ein Data Engineer kuratiert pro Domain (Sales, Finance, Operations) einen Bereich mit erlaubten Tabellen, Custom-Instruktionen, Beispielfragen und Synonymen. Anwender stellen Fragen in natürlicher Sprache, Genie generiert SQL, zeigt den Plan, führt aus und visualisiert. Der **Trust-Loop** lernt aus User-Feedback (Daumen hoch/runter), welche Antworten korrekt waren.

**Embedding** in eigene Apps via SDK macht Genie auch für SaaS-Anbieter spannend, die ihren Kunden eine Conversational-Datenanalyse anbieten wollen. Visualisierungen sind funktional, aber spartanisch — wer Pixel-perfect Dashboards braucht, kombiniert Genie mit Power BI oder Tableau.

Empfohlen für Organisationen mit Databricks Lakehouse, die Self-Service-Analytics für SQL-fremde Stakeholder öffnen wollen — günstiger als ein separater BI-Stack und mit Unity-Catalog-Garantien für Governance."""},

    {'slug':'rows','name':'Rows','vendor':'Rows','category':'daten-analyse',
     'tagline':'AI-Spreadsheet aus Lissabon — kombiniert Excel-Vertrautheit mit AI-Funktionen, Live-Datenquellen und Sharing.',
     'price':'Free · Pro ab $59 / Mon.','api':True,'dsgvo':'ja','origin':'EU (PT)',
     'rating':4.5,'reviews':1140,
     'pros':['Vertraute Spreadsheet-UI mit AI-Power','Live-Connectors zu 50+ Datenquellen','EU-Anbieter, DSGVO-konform','AI-Analyst-Funktion fasst zusammen'],
     'cons':['Keine vollwertige Excel-Ersatz für komplexe Modelle','Pro-Plan erst lohnenswert','Kollaborations-Features noch im Aufbau'],
     'usecases':['SaaS-KPI-Dashboards','Marketing-Reporting','Sales-Pipelines','Forschungs-Datenextraktion'],
     'launched':'2017-04-01','lastUpdated':'2026-04-15',
     'website':'https://rows.com/','domain':'rows.com',
     'features':"""- **=AI()-Funktion**: jeder Cell-Wert kann AI-Output sein (Klassifikation, Übersetzung, Zusammenfassung).
- **AI Analyst**: fasst Tabellen zusammen, schlägt Charts und Insights vor.
- **Live-Connectors**: HubSpot, Salesforce, Stripe, Google Analytics, Notion, Postgres.
- **Magic Format**: Tabellen aus Text-Snippets erkennen + parsen.
- **Sharing als Live-Page**, Embed in Notion/Confluence.
- **API** zum Lesen/Schreiben.""",
     'pricing':"""- **Free** — 5 Spreadsheets, 1 GB, 50 AI-Credits / Mon.
- **Plus** · $19,99 / Mon. — 50 Spreadsheets, 250 AI-Credits.
- **Pro** · $59 / Mon. — unlimited Spreadsheets, 1.500 AI-Credits.
- **Business** · $179 / Mon. — Premium-Modelle, 5.000 AI-Credits, Brand-Kit.
- **Enterprise** · auf Anfrage — SSO, SAML, Audit-Logs, EU-Region.""",
     'overview':"""**Rows** ist die spannendste Spreadsheet-Innovation der letzten Jahre — und kommt ausgerechnet aus Lissabon, nicht aus dem Silicon Valley. Die Plattform sieht aus wie Google Sheets, fühlt sich vertraut an, hat aber zwei Killer-Features: **=AI()** als nativer Cell-Funktion und **50+ Live-Connectors** zu Daten aus HubSpot, Stripe, Postgres, GA4 und Co.

Das ändert Workflows: Eine Sales-KPI-Tabelle zieht Live-Daten aus Salesforce, AI-Funktionen klassifizieren jede Opportunity nach Branche und Stage, und der **AI Analyst** liefert eine Zusammenfassung plus Chart-Vorschläge. Magic Format extrahiert Tabellen aus Text — etwa eine ChatGPT-Antwort, die als sauberer Spreadsheet-Block ankommt.

Als **EU-Anbieter** ist Rows DSGVO-fest, mit Frankfurter Hosting im Enterprise-Tarif. Sharing als Live-Page ersetzt PDF-Reports — Stakeholder bekommen aktuelle Zahlen ohne wöchentliche Mail.

Schwäche: Für komplexe Finanzmodelle mit hunderten verschachtelten Formeln bleibt Excel die erste Wahl. Rows brilliert bei Kollaboration, Live-Daten und AI-gestützter Auswertung — nicht im Tax-Modeling.

Empfohlen für Marketing-, Sales- und Operations-Teams in SaaS-Unternehmen, die Live-Reporting ohne BI-Tool brauchen, sowie für jeden, der Sheets und AI-Funktionen kombinieren will, ohne mehrere Tools zu wechseln."""},

    {'slug':'akkio','name':'Akkio','vendor':'Akkio','category':'daten-analyse',
     'tagline':'No-Code-AI für tabulare Vorhersagen — Modelle in 10 Minuten, ohne Data-Science-Team.',
     'price':'Basic ab $49 / Mon. · Professional ab $199 / Mon.','api':True,'dsgvo':'bedingt','origin':'USA',
     'rating':4.3,'reviews':390,
     'pros':['Sehr schneller Time-to-Value (10-Min-Modelle)','Generative-AI-Layer für Berichte','Direkte HubSpot/Salesforce/GA-Integration','Erklärbare Predictions mit Feature-Importance'],
     'cons':['Begrenzte Modell-Tuning-Optionen','Pricing eskaliert mit Datenmenge','Wenig granulare DSGVO-Kontrollen'],
     'usecases':['Lead-Scoring','Churn-Prognose','Demand-Forecasting','Klassifikation für Support-Tickets'],
     'launched':'2019-09-01','lastUpdated':'2026-04-12',
     'website':'https://www.akkio.com/','domain':'akkio.com',
     'features':"""- **AutoML** für Klassifikation, Regression, Forecasting.
- **Chat Explore**: natürliche Sprache → SQL → Chart.
- **Generative Reports** mit narrativer Auswertung.
- **Direct Connectors**: HubSpot, Salesforce, BigQuery, Snowflake, GA4.
- **Erklärbarkeit**: Feature-Importance + Decision Path pro Prediction.
- **Embedding** der Predictions via API in eigene Workflows.""",
     'pricing':"""- **Free Trial** · 14 Tage, 100k Predictions.
- **Basic** · $49 / Mon. — 100k Predictions/Mon., 3 Connectors.
- **Professional** · $199 / Mon. — 500k Predictions, alle Connectors, Generative Reports.
- **Business** · $999 / Mon. — 5M Predictions, Multi-User, Priority-Support.
- **Enterprise** · auf Anfrage — Custom-Limits, dediziertes Modell-Hosting.""",
     'overview':"""**Akkio** macht das, was viele AutoML-Plattformen versprechen, ungewöhnlich gut: ein nicht-technischer Anwender lädt eine CSV oder verbindet HubSpot/Salesforce, wählt eine Zielspalte, klickt — und hat zehn Minuten später ein produktiv einsetzbares Modell mit nachvollziehbarer Genauigkeit. Das deckt Standard-Use-Cases wie Lead-Scoring, Churn-Prognose und Demand-Forecasting in Marketing- und Sales-Teams ab.

Die jüngste Erweiterung **Chat Explore** und **Generative Reports** kombiniert das mit konversationaler Datenanalyse: Frage in natürlicher Sprache → SQL → Chart → narrativer Report. Damit verschiebt Akkio sich aus der reinen "AutoML-Nische" in Richtung "Self-Service-Analytics für Operations-Teams".

Stark ist die **Erklärbarkeit**: Feature-Importance und Decision-Path pro Prediction sind Standard. Das macht es einfacher, Modelle bei Kunden, Marketing-Managern oder Compliance-Funktionen zu verteidigen.

Schwächen: Wer richtige Data Science braucht (eigene Algorithmen, fortgeschrittenes Tuning, A/B-Test-Setup), bleibt mit Snowflake-Cortex, Databricks oder Custom-Notebooks besser bedient. Das Pricing pro Million Predictions kann bei Live-Scoring schnell teuer werden.

Empfohlen für KMU-Marketing- und Sales-Teams, die schnelle Predictive-Analytics-Use-Cases umsetzen wollen, ohne ein Data-Science-Team aufzubauen."""},

    {'slug':'vanna-ai','name':'Vanna AI','vendor':'Vanna AI','category':'daten-analyse',
     'tagline':'Open-Source-Text-to-SQL-Agent mit RAG über das Datenbank-Schema — selbst hostbar, jeder LLM nutzbar.',
     'price':'Open Source · Cloud auf Anfrage','api':True,'dsgvo':'ja','origin':'USA',
     'rating':4.5,'reviews':520,
     'pros':['Komplett Open Source (MIT)','RAG-Trainings-Workflow für SQL-Beispiele','Plug-and-Play mit jedem LLM und jeder DB','Self-Hosting trivial möglich'],
     'cons':['Setup erfordert Python-Kenntnisse','Visualisierungen rudimentär','Multi-User-Funktionen rudimentär ohne Cloud'],
     'usecases':['Internal Data Q&A','SQL-Lernen','Embedded SQL-Agent','Datenbank-Self-Service'],
     'launched':'2023-06-01','lastUpdated':'2026-04-08',
     'website':'https://vanna.ai/','domain':'vanna.ai',
     'features':"""- **RAG-Training** auf Schema, Beispielen und Dokumentation.
- **LLM-agnostisch** (OpenAI, Anthropic, Mistral, lokal via Ollama).
- **Vector Store agnostisch** (ChromaDB, Pinecone, pgvector, Weaviate).
- **DB-agnostisch** (Postgres, MySQL, Snowflake, BigQuery, DuckDB).
- **Streamlit Web UI** out-of-the-box, Slack-Bot Beispiel.
- **`vanna train()`** für inkrementelle Verbesserung mit Feedback.""",
     'pricing':"""- **Open Source** (MIT) — komplett kostenlos.
- **Vanna Cloud** · auf Anfrage — gemanagter RAG-Store, Multi-User, Audit.
- LLM- und DB-Kosten richten sich nach Provider.
- Self-Hosting empfohlen für DSGVO-relevante Daten.
- Community-Support via GitHub-Discussions und Discord.""",
     'overview':"""**Vanna AI** ist die ehrlichste Open-Source-Antwort auf das Text-to-SQL-Problem: keine Magie-LLM-Calls, sondern ein klar dokumentierter RAG-Workflow. Man trainiert Vanna auf das Datenbank-Schema, fügt Beispiel-Queries und Geschäftsdokumente hinzu, und ab dann kann jede natürliche Frage in passendes SQL übersetzt werden — auf der eigenen Datenbank, mit dem eigenen LLM, im eigenen Stack.

Die **Plug-and-Play-Philosophie** macht Vanna für Engineering-Teams attraktiv: ChatGPT oder Claude oder Mistral als LLM, Postgres oder Snowflake oder DuckDB als DB, ChromaDB oder pgvector als Embedding-Store. Alles tauschbar, alles dokumentiert. Das macht Vanna zur EU-freundlichen Wahl, wenn keine Daten an US-SaaS-Anbieter raus dürfen.

Der **`train()`-Workflow** ist die unterschätzte Stärke: Jede gute Antwort kann zurück in den Vector Store geschrieben werden, jede schlechte korrigiert. Über Wochen wird das Modell für die eigene Domäne immer treffsicherer.

Schwächen: Für eine UI muss man eine Streamlit-App oder den Slack-Bot selbst aufsetzen; eine polierte SaaS-Erfahrung wie bei Hex oder ThoughtSpot gibt es nicht. Visualisierungen sind rudimentär. Multi-User-Berechtigungen gibt es nur in der (kostenpflichtigen) Cloud-Version.

Empfohlen für Engineering-Teams, die einen produktiven SQL-Agenten in eigene Anwendungen oder Slack-Workflows einbauen wollen — und für jeden, der Datenresidenz-Anforderungen hat, die SaaS-Tools ausschließen."""},

    {'slug':'dataiku','name':'Dataiku','vendor':'Dataiku','category':'daten-analyse',
     'tagline':'Enterprise-Data-Science-Plattform mit AI Agent Studio — vom Data Prep über AutoML bis zu produktiven LLM-Apps.',
     'price':'Free Edition · Cloud ab €15.000 / Jahr','api':True,'dsgvo':'ja','origin':'EU (FR)',
     'rating':4.4,'reviews':1820,
     'pros':['Sehr breite Plattform (DataPrep, ML, MLOps, Apps)','Visual + Code Hybrid für Mixed-Skill-Teams','LLM Mesh + AI Agent Studio','EU-Anbieter, ISO-/SOC-zertifiziert'],
     'cons':['Steile Lernkurve','Lizenzkosten erheblich','Enterprise-Setup mehrwöchig','Self-Hosting-Setup komplex'],
     'usecases':['Konzern-Data-Science','MLOps','Embedded LLM-Apps','Daten-Governance'],
     'launched':'2013-02-01','lastUpdated':'2026-04-17',
     'website':'https://www.dataiku.com/','domain':'dataiku.com',
     'features':"""- **DSS Visual Flows** für ETL ohne Code.
- **AutoML** mit Erklärbarkeit, Drift-Monitoring, Versionierung.
- **AI Agent Studio**: orchestrierte LLM-Workflows mit Tools und Memory.
- **LLM Mesh**: zentrale Verwaltung mehrerer Provider mit Cost-Tracking.
- **MLOps-Ende-zu-Ende**: CI/CD, Model Registry, Monitoring.
- **Apps**: gebaute Modelle als Endnutzer-Anwendungen veröffentlichen.""",
     'pricing':"""- **Free Edition** · Self-Hosted, 3 User, alle Core-Features.
- **Cloud Edition** · ab €15.000 / Jahr (Starter), Pro-Tarif sechsstellig.
- **Online Edition** · gemanagt mit dedizierten Worker-Nodes.
- **Enterprise** · auf Anfrage — On-Prem-Lizenz, SSO, RBAC, Custom-Plugins.
- **AI Agent Studio Add-on** im LLM-Pricing der genutzten Provider.""",
     'overview':"""**Dataiku** ist seit Jahren die führende Enterprise-Plattform für Mixed-Skill-Data-Teams: visuelle Flows für Daten-Engineers, Notebooks für Data Scientists, Jobs für ML-Engineers — alles in einer Umgebung, mit zentralem Catalog, Lineage und Versionierung. Mit dem **AI Agent Studio** und **LLM Mesh** erweitert das französische Unternehmen jetzt konsequent in Richtung Generative-AI-Operations.

Der **LLM Mesh** ist die unterschätzte Stärke: Statt direkt OpenAI- oder Anthropic-Calls zu schreiben, geht jede AI-Anfrage durch eine zentrale Mesh-Schicht, die Provider, Modell, Cost-Tracking und Compliance-Filter durchsetzt. Das **AI Agent Studio** baut darauf auf — Engineers definieren Tools, Memory und Orchestrierung; Compliance-Teams haben den Audit-Trail.

Auch klassische **MLOps-Funktionen** sind enterprise-ready: Model Registry, CI/CD für Modelle, Drift-Monitoring, Approval-Workflows. **Apps** veröffentlicht Modelle als Endnutzer-Tools mit Forms und Visualisierungen.

Schwächen: Lizenzkosten beginnen sechsstellig pro Jahr für ernsthaften Einsatz; das Enterprise-Setup dauert Wochen, und die Lernkurve ist steil. Für KMU oder kleine Daten-Teams ist Dataiku überdimensioniert.

Empfohlen für Konzerne und Mittelstand mit dedizierten Data-Science-Teams, die eine durchgängige Plattform für klassische ML, Generative AI und MLOps suchen. Als EU-Anbieter mit ISO-/SOC-Zertifizierungen ist Dataiku DSGVO-fest."""},
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

def fetch_logo(domain: str, size: int = 256) -> bytes:
    url = f'https://www.google.com/s2/favicons?domain={domain}&sz={size}'
    r = requests.get(url, timeout=30); r.raise_for_status(); return r.content

for tool in TOOLS:
    slug = tool['slug']
    overview = tool.pop('overview')
    domain = tool.pop('domain')

    el = existing_by_slug.get(slug)
    if el:
        print(f'\n· {slug}: exists (id={el["id"]})')
        existing_data = el['data']
    else:
        base = {k: v for k, v in tool.items()}
        r = requests.post(f'{BASE}/{SITE}/elements/',
            json={'type_id': TOOL_CT_ID, 'data': base, 'published': True},
            headers=JH, verify=False)
        if not r.ok:
            print(f'  ✗ {slug}: create failed: {r.status_code} {r.text[:200]}')
            continue
        el = r.json()
        existing_data = el['data']
        print(f'\n✓ {slug}: created (id={el["id"]})')

    patches = {}
    for k in ('features', 'pricing', 'website'):
        if not existing_data.get(k) and tool.get(k):
            patches[k] = tool[k]

    has_post = (isinstance(existing_data.get('post_id'), int) or
                (isinstance(existing_data.get('post_id'), dict) and existing_data['post_id'].get('content')))
    if not has_post:
        post_payload = {
            'title': f'{tool["name"]} — Übersicht',
            'content': overview,
            'short_description': tool.get('tagline', ''),
            'keywords': [tool.get('vendor',''), tool.get('category','')],
            'published': True, 'locale': 'de',
        }
        r = requests.post(f'{BASE}/{SITE}/posts/', json=post_payload, headers=JH, verify=False)
        if r.ok:
            patches['post_id'] = r.json()['id']
            print(f'  ✓ post #{patches["post_id"]} ({len(overview)} chars)')

    if not existing_data.get('logo_id'):
        try:
            png = fetch_logo(domain)
            local = LOGOS_DIR / f'{slug}.png'
            local.write_bytes(png)
            with open(local, 'rb') as fh:
                files = {'file': (f'{slug}-logo.png', fh, 'image/png')}
                data = {
                    'name': f'{tool["name"]} – Logo',
                    'alt_text': f'Logo von {tool["name"]}',
                    'description': f'Offizielles Logo von {tool["name"]} ({domain}).',
                }
                rl = requests.post(f'{BASE}/{SITE}/media/',
                    files=files, data=data, headers=H, verify=False, timeout=120)
            if rl.ok:
                patches['logo_id'] = rl.json()['id']
                print(f'  ✓ logo #{patches["logo_id"]} ({len(png):,} bytes from {domain})')
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
