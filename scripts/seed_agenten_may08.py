#!/usr/bin/env python3
"""Seed 7 additional Agenten & Automation tools end-to-end (May 2026 batch)."""
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
    {'slug':'openai-agents-sdk','name':'OpenAI Agents SDK','vendor':'OpenAI','category':'agenten',
     'tagline':'OpenAIs offizieller Open-Source-Agent-Framework — Tool-Use, Hand-offs, Tracing, Guardrails. Python und TypeScript, läuft mit GPT-5 und beliebigem Provider.',
     'price':'Open Source · Modell-Aufrufe via OpenAI-API','api':True,'dsgvo':'bedingt','origin':'USA',
     'rating':4.7,'reviews':5210,
     'pros':['Offizielles SDK von OpenAI mit nahtloser GPT-5-Integration','Multi-Agent-Hand-offs eingebaut','Eingebauter Tracer für Debugging','Funktioniert auch mit anderen LLM-Providern'],
     'cons':['Junges Projekt mit häufigen Breaking Changes','Dokumentation noch unvollständig','Tracer nur in OpenAI-Dashboard sichtbar','Memory-Layer noch dünn'],
     'usecases':['Customer-Support-Agenten','Recherche-Workflows','Daten-Pipeline-Agenten','Multi-Step-Reasoning'],
     'launched':'2025-03-11','lastUpdated':'2026-05-08',
     'website':'https://github.com/openai/openai-agents-python','domain':'openai.com',
     'features':"""- **Agents-Klasse** als zentrale Abstraktion mit Instructions, Tools und Hand-offs.
- **Hand-offs** ermöglichen Multi-Agent-Workflows ohne externe Orchestrierung.
- **Tools** als typed Python-Funktionen, automatisch als JSON-Schema bereitgestellt.
- **Guardrails** für Input-/Output-Validierung mit Pydantic-Modellen.
- **Tracing** in das OpenAI-Dashboard mit kompletter Step-Visualisierung.
- **Streaming** mit Token-Level-Events und Tool-Call-Updates.
- **Provider-agnostisch**: arbeitet mit Claude, Gemini, lokalen LiteLLM-Backends.""",
     'pricing':"""- **Open Source** · MIT-Lizenz, Nutzung kostenlos.
- **Modell-Aufrufe** über die OpenAI-API zum normalen Tarif (GPT-5 ab $1,25 / 1M In-Tokens).
- **Tracing** im OpenAI-Dashboard kostenlos enthalten.
- **Self-Hosting** möglich, Provider frei wählbar.
- **Enterprise** über OpenAI Business / Enterprise mit SSO und Audit-Logs.""",
     'overview':"""**OpenAI Agents SDK** ist das offizielle Agent-Framework von OpenAI — vorgestellt im März 2025, seitdem in mehreren großen Releases zur produktionsreifen Multi-Agent-Bibliothek gereift. Wer Agents mit GPT-5 baut, sollte sich dieses SDK als Default ansehen, bevor er zu generischeren Frameworks wie LangChain oder CrewAI greift.

Die **Kernabstraktion** ist überraschend schlank: Eine `Agent`-Klasse hält Instructions, Tools und mögliche Hand-offs an andere Agents. Tools sind getypte Python-Funktionen — der Decorator schreibt automatisch das passende JSON-Schema, sodass das LLM die Funktion korrekt aufrufen kann. Das ist deutlich weniger Boilerplate als bei den meisten Konkurrenten.

**Hand-offs** sind das spannendste Feature: Ein Agent kann strukturiert an einen anderen Agent übergeben — etwa vom „Triage-Agent" zum „Refund-Agent" oder „Technical-Support-Agent". Multi-Agent-Workflows entstehen ohne separate Orchestrierungs-Schicht, der Code bleibt linear lesbar.

**Guardrails** prüfen Eingaben und Ausgaben gegen Pydantic-Modelle — ein eigener Agent als Filter, der etwa unsichere Anfragen blockt oder Outputs auf Schema-Konformität prüft. Für regulierte Workflows ein wichtiger Baustein.

Das **Tracing** ist die zweite große Stärke: Jeder Step (Agent-Aufruf, Tool-Use, Hand-off) wird automatisch in das OpenAI-Dashboard geschickt, mit kompletter Visualisierung des Reasoning-Pfads. Für Debugging und Performance-Analysen unschätzbar wertvoll — im Vergleich zu CrewAI oder LangChain ein klarer Komfort-Vorteil.

**Provider-Agnostik**: Trotz des Namens läuft das SDK mit Claude (Anthropic), Gemini (Google), DeepSeek, lokalen Modellen via LiteLLM. Das macht das SDK zu einer der ehrlicheren Migrations-Wege für Teams, die Modell-Providers wechseln wollen.

Schwächen: Das SDK ist **noch jung** — Breaking Changes in den letzten 12 Monaten waren häufig, die offizielle Dokumentation hinkt teils hinter. Der **Memory-Layer** ist dünner als bei LangGraph oder Letta — wer langes Gedächtnis braucht, baut selbst.

Empfohlen für Teams, die mit OpenAI-Modellen arbeiten und ein durchdachtes, leichtes Agent-Framework brauchen — und für jeden, der bereit ist, mit einer aktiv entwickelten Library zu leben."""},

    {'slug':'autogen','name':'Microsoft AutoGen','vendor':'Microsoft Research','category':'agenten',
     'tagline':'Forschungs-First-Framework für Multi-Agent-Systeme aus Microsoft Research — mit AutoGen Studio als visueller IDE für komplexe Agenten-Konversationen.',
     'price':'Open Source (MIT) · LLM-Kosten je nach Provider','api':True,'dsgvo':'bedingt','origin':'USA',
     'rating':4.4,'reviews':3870,
     'pros':['Sehr starke Multi-Agent-Konversationen','Visual Builder über AutoGen Studio','Magentic-One als ready-made General-Purpose-Agent','Aktive Forschung von Microsoft Research'],
     'cons':['API-Konzepte ändern sich oft (v0.4 war großer Cut)','Lernkurve steiler als bei OpenAI Agents SDK','Tracing weniger ausgereift','Production-Patterns selten dokumentiert'],
     'usecases':['Forschung mit komplexen Multi-Agent-Setups','Code-generierende Workflows','Datenanalyse-Pipelines','Konversations-Agenten mit mehreren Personas'],
     'launched':'2023-09-25','lastUpdated':'2026-05-08',
     'website':'https://microsoft.github.io/autogen/','domain':'microsoft.com',
     'features':"""- **AssistantAgent** und **UserProxyAgent** als Kern-Bausteine.
- **GroupChat** für strukturierte Multi-Agent-Konversationen.
- **AutoGen Studio**: visuelle IDE zum Bauen, Testen und Deployen.
- **Magentic-One**: Ready-Made General-Purpose-Multi-Agent-System.
- **Code-Execution** in sandboxed Docker-Containern.
- **Provider-agnostisch** (OpenAI, Azure, Anthropic, lokal).
- **Distributed Runtime** für skalierende Production-Workloads (v0.4+).""",
     'pricing':"""- **Open Source** · MIT-Lizenz, kostenlose Nutzung.
- **AutoGen Studio** kostenlos, läuft lokal oder als Container.
- **Magentic-One** kostenlos, eigenes Hosting nötig.
- **LLM-Kosten** je nach Provider (Azure OpenAI, OpenAI, Claude, lokal).
- **Enterprise**-Support nicht direkt verfügbar — Azure-Integration über Azure Cognitive Services.""",
     'overview':"""**AutoGen** ist Microsoft Researchs experimentelles Framework für Multi-Agent-Systeme — gestartet im September 2023, seitdem zu einer der einflussreichsten Open-Source-Agent-Libraries gereift. Anders als die meisten Konkurrenten kommt AutoGen aus der **Forschungsabteilung**: Konzepte ändern sich häufig, dafür sind die Patterns für komplexe Multi-Agent-Konversationen besonders ausgereift.

Die **Kernidee** ist ungewöhnlich: Statt eines linearen Agent-Loops modelliert AutoGen Agents als **Konversationspartner**, die miteinander reden — ein `AssistantAgent` denkt nach und schreibt, ein `UserProxyAgent` führt Tool-Calls aus, ein `GroupChat` orchestriert mehrere Agents in einer Runde. Das macht komplexe Setups (Researcher + Critic + Coder + Reviewer) intuitiver beschreibbar als in den meisten Konkurrenten.

**AutoGen Studio** ist die visuelle IDE: Agents per Drag-and-Drop konfigurieren, Konversationen testen, Workflows als JSON exportieren. Für Teams, die lieber visuell modellieren als in Python codieren, ein erfrischender Einstieg — und für Workshops und Demos ideal.

**Magentic-One** ist seit Ende 2024 der Star: Ein ready-made General-Purpose-Multi-Agent-System mit einem Orchestrator und vier spezialisierten Agents (Web-Surfer, File-Surfer, Coder, Computer-Terminal). Out-of-the-Box auf Web-Browsing- und Tool-Use-Benchmarks führend — als Forschungsbasis für eigene General-Purpose-Agents wertvoll.

Die **Distributed Runtime** (seit v0.4) macht AutoGen production-tauglich: Agents können auf verschiedenen Maschinen laufen, asynchron kommunizieren, Mid-Conversation-Failover funktioniert. Wer skaliert, profitiert von dieser Architektur.

Schwächen: Die **API-Stabilität** ist die größte Hürde — der v0.4-Cut Anfang 2025 hat viel Code gebrochen, und kleinere Breaking Changes gibt es weiter regelmäßig. Die **Lernkurve** ist steiler als bei OpenAI Agents SDK oder CrewAI — die Multi-Agent-Konversations-Patterns brauchen Eingewöhnung.

Empfohlen für Forschungsteams und Engineers, die komplexe Multi-Agent-Patterns explorieren — und für jeden, der mit AutoGen Studio einen visuellen Einstieg in Multi-Agent-Architekturen sucht. Für stabile Production-Agenten mit OpenAI-Modellen ist das Agents SDK aktuell oft die bessere Wahl."""},

    {'slug':'agentforce','name':'Salesforce Agentforce','vendor':'Salesforce','category':'agenten',
     'tagline':'Salesforces Enterprise-Agent-Plattform — Pre-Built Agents für Sales, Service, Marketing, tief mit Data Cloud, Flow und Einstein verzahnt.',
     'price':'Ab $2 / Konversation · Enterprise-Lizenzierung','api':True,'dsgvo':'ja','origin':'USA',
     'rating':4.3,'reviews':2940,
     'pros':['Tiefste CRM-Integration im Markt','Pre-Built Agents für Standard-Use-Cases','Atlas Reasoning Engine als spezielles Agent-Modell','EU-Datenresidenz bei Hyperforce-EU'],
     'cons':['Pricing pro Konversation kann teuer werden','Stark an Salesforce-Datenmodell gebunden','Maßgeschneiderte Agents brauchen Salesforce-Knowhow','Lock-in-Risiko'],
     'usecases':['Service-Agents','Sales-Development-Reps','Marketing-Personalisierung','Field-Service-Triage'],
     'launched':'2024-09-12','lastUpdated':'2026-05-08',
     'website':'https://www.salesforce.com/agentforce/','domain':'salesforce.com',
     'features':"""- **Agent Builder** im Lightning-Stil für Konfiguration ohne Code.
- **Atlas Reasoning Engine**: Salesforce-eigenes Agent-Modell, optimiert für CRM-Daten.
- **Pre-Built Agents** für Sales, Service, Marketing, Commerce.
- **Data Cloud-Integration**: Einheitliche Sicht auf Kundendaten als Agent-Kontext.
- **Flow-Integration**: bestehende Salesforce-Flows als Tools nutzbar.
- **Einstein Trust Layer** für Compliance, Audit und Data Masking.
- **Hyperforce-EU** für DSGVO-konforme Datenresidenz.""",
     'pricing':"""- **Agentforce Service** · ab $2 / Konversation, Volumen-Rabatte ab 10.000 / Mon.
- **Agentforce Sales** · ab $2 / Konversation.
- **Agentforce Marketing** · auf Anfrage.
- **Custom Agents** · enthalten in Agentforce-Lizenz, je nach Edition.
- **Enterprise Edition** · ab $165 / Sitz / Mon. (Sales/Service Cloud).
- **Setup** über Salesforce-Partner oder eigene Salesforce-Admins.""",
     'overview':"""**Salesforce Agentforce** ist Salesforces Antwort auf die Agent-Welle 2024/25 — vorgestellt auf der Dreamforce 2024, seitdem zur **enterprise-tauglichsten Agent-Plattform für CRM-zentrische Workflows** gereift. Wer Salesforce als Datendrehscheibe nutzt, hat hier den kürzesten Weg zu produktiven Agents.

Die **strategische Stärke** ist die **CRM-Integration**: Agents haben out-of-the-Box Zugriff auf Accounts, Contacts, Opportunities, Cases — als typed Datenobjekte mit Beziehungs-Wissen. Was bei generischen Frameworks (LangChain, CrewAI) ein eigener RAG-Stack wäre, ist hier konstitutiv. Service-Agents kennen die Kundenhistorie, Sales-Agents kennen den Pipeline-Status, ohne dass Engineering-Teams Pipelines bauen.

**Pre-Built Agents** für Sales, Service, Marketing und Commerce sind die häufigste Einstiegs-Variante — Konfiguration über den **Agent Builder**, der wie der bekannte Salesforce-Flow-Builder aussieht. Eine Service-Lead-Triage, ein Sales-Development-Rep für Inbound-Leads, ein Marketing-Personalisierungs-Agent: alle in Stunden konfigurierbar, nicht in Monaten gebaut.

Die **Atlas Reasoning Engine** ist Salesforces eigenes Agent-Modell — fine-tuned auf CRM-Workflows und Salesforce-Datenstrukturen. Für Standard-Aufgaben oft besser als ein generisches GPT-5 oder Claude, weil das Modell die Salesforce-Domäne kennt.

Der **Einstein Trust Layer** löst die Compliance-Frage in regulierten Branchen — Data Masking, Audit Trails, Output-Filtering, alles eingebaut. **Hyperforce-EU** macht Agentforce für deutsche Banken, Krankenhäuser und Behörden DSGVO-konform deploybar.

**Flow-Integration** ist der versteckte Hebel: Bestehende Salesforce-Flows (Workflows, Approval-Processes, Apex-Funktionen) sind als Tools für Agents nutzbar. Wer 10 Jahre Salesforce-Flow-Investitionen hat, kann sie als Agent-Tools wiederverwenden.

Schwächen: Das **Pricing pro Konversation** ($2 ist die Standard-Rate) wird bei hohem Volumen schnell teuer — Volumen-Rabatte sind verhandelbar, aber Modelle wie GPT-5 + LangChain sind oft günstiger. **Lock-in** ist real: Custom Agents nutzen Salesforce-spezifische APIs und sind nicht portabel.

Empfohlen für Salesforce-Kunden mit produktiven CRM-Workflows — und für Enterprise-Teams, die in einem regulierten Umfeld die etabliertesten Compliance-Tools brauchen. Für Greenfield-Projekte ohne Salesforce-Anbindung sind generische Agent-Frameworks meist günstiger und flexibler."""},

    {'slug':'copilot-studio','name':'Microsoft Copilot Studio','vendor':'Microsoft','category':'agenten',
     'tagline':'Visuelles Low-Code-Studio für eigene Microsoft-Copilots — Agents bauen, mit M365-Daten, Power-Platform-Connectoren und Azure-AI-Modellen verbinden.',
     'price':'Ab $200 / Mon. (Pay-as-you-go) · Per-Message-Pricing','api':True,'dsgvo':'ja','origin':'USA',
     'rating':4.4,'reviews':4180,
     'pros':['Tiefste Microsoft-365-Integration','Über 1.500 Power-Platform-Connectoren','Visual Topic Designer für Konversations-Logik','EU-Datenresidenz im Rahmen von M365 Enterprise'],
     'cons':['Pricing pro Message kann sich aufaddieren','Lock-in an Microsoft-Stack','Komplexere Custom-Logik braucht Power-Fx','Modell-Auswahl auf Azure-OpenAI begrenzt'],
     'usecases':['IT-Helpdesk-Bots','HR-Self-Service','Sales-Enablement','Internal-Knowledge-Agents'],
     'launched':'2023-10-31','lastUpdated':'2026-05-08',
     'website':'https://www.microsoft.com/en-us/microsoft-copilot/microsoft-copilot-studio','domain':'microsoft.com',
     'features':"""- **Visual Topic Designer**: Konversations-Logik per Drag-and-Drop.
- **1.500+ Connectoren** zu SharePoint, Dynamics, SAP, ServiceNow, Salesforce u.v.m.
- **Knowledge-Sources** über SharePoint, Websites, Dataverse, Files.
- **Azure-OpenAI-Backbone** mit GPT-4.1, GPT-5, o-series.
- **Microsoft 365 Copilot Extension** für eigene Copilots in Teams, Word, Outlook.
- **Authentifizierung** über Entra ID (Azure AD) mit Rollen-Vererbung.
- **Power-Fx-Skripting** für komplexe Logik.""",
     'pricing':"""- **Pay-as-you-go** · $200 / 25.000 Messages.
- **Tenant-Pack** · $200 / Mon. — 25.000 Messages, in M365-Tenant.
- **Generative-Messages** (mit GPT-5) · 4× normale Messages-Kosten.
- **Authentifizierte Messages** · 2× normale Kosten.
- **Microsoft 365 Copilot Studio Extension** · in M365 Copilot ($30/Sitz/Mon.) enthalten.
- **Enterprise** · auf Anfrage, EU-Datenresidenz mit M365 E3/E5.""",
     'overview':"""**Microsoft Copilot Studio** ist Microsofts Low-Code-Plattform für **eigene Copilots** — vorgestellt im Oktober 2023 als Nachfolger von Power Virtual Agents, seitdem zur strategischen Plattform für **enterprise-weite Agent-Builds in Microsoft-Ökosystemen** gewachsen.

Die **strategische Idee**: Statt SDKs für Engineers zu liefern (wie OpenAI Agents SDK oder AutoGen), gibt Copilot Studio **Power-Platform-Builder:innen** die Möglichkeit, Agents zu konfigurieren — visuell, mit Connectoren, mit M365-Daten. Wer in einem Microsoft-Shop arbeitet, hat hier den niedrigsten Einstieg.

Der **Visual Topic Designer** modelliert Konversations-Logik als Flussdiagramm: Begrüßung, Intent-Erkennung, Verzweigungen, Tool-Aufrufe, Antwort-Generierung. Was bei Code-First-Frameworks 200 Zeilen Python wären, sind hier ein paar Drag-and-Drop-Schritte — gut für IT-Helpdesk-Bots, HR-Self-Service, Sales-Enablement.

Die **1.500+ Power-Platform-Connectoren** sind der größte Hebel: SharePoint, Dynamics 365, SAP, ServiceNow, Salesforce, Jira, Workday — alle als out-of-the-Box-Tools für Agents nutzbar. Was bei generischen Agent-Frameworks ein eigener API-Wrapper wäre, ist hier konfigurativ.

**Knowledge-Sources** ergänzen den Bot um RAG: SharePoint-Sites, interne Websites, Dataverse-Tabellen, hochgeladene Dateien werden indexiert und in der Konversation referenziert — automatisch mit Citations. Für Internal-Knowledge-Agents ein direkter Weg ohne separaten Vector-DB-Setup.

Die **Microsoft 365 Copilot Extension** ist der versteckte Hebel: Custom Copilots können in Teams-Chats, Word, Outlook eingebettet werden — Endnutzer:innen sehen sie als zusätzliche „Copilots" neben dem Standard-M365-Copilot. Für Adoption ein massiver Komfort-Vorteil.

**Entra-ID-Integration** löst die Authentifizierungs- und Berechtigungsfrage: Agents kennen den Login-User, respektieren SharePoint-Berechtigungen, vererben Rollen aus Azure AD. Für Enterprise-Compliance unerlässlich.

Schwächen: Das **Per-Message-Pricing** wird bei hohem Volumen teuer — Generative Messages (mit GPT-5) kosten 4× normale Messages, addiert sich schnell. **Lock-in** an den Microsoft-Stack ist real und tief. **Modell-Auswahl** ist auf Azure-OpenAI begrenzt — Claude, Gemini, lokale Modelle sind nicht direkt verfügbar.

Empfohlen für Microsoft-Shops mit etablierten M365- und Power-Platform-Investitionen — und für Citizen Developers, die ohne Engineering-Team Agents in produktiven Workflows ausrollen wollen."""},

    {'slug':'browser-use','name':'Browser Use','vendor':'Browser Use','category':'agenten',
     'tagline':'Open-Source-Bibliothek für Browser-automatisierende Agents — LLMs steuern echte Chrome-Sessions, mit DOM-Awareness und Vision-Fallback.',
     'price':'Open Source · Cloud-Tier ab $30 / Mon.','api':True,'dsgvo':'bedingt','origin':'Schweiz',
     'rating':4.6,'reviews':2840,
     'pros':['Zuverlässigste Open-Source-Browser-Steuerung','DOM + Vision Hybrid-Ansatz','Provider-agnostisch (GPT, Claude, Gemini, lokal)','EU-Anbieter (Zürich)'],
     'cons':['Browser-Setup erfordert Engineering-Knowhow','Anti-Bot-Pages bleiben Stolperstein','Vision-Fallback erhöht Token-Kosten','Cloud-Tier noch jung'],
     'usecases':['Web-Scraping mit dynamischen Seiten','Form-Filling-Automation','Browser-basierte Test-Workflows','Personal-Browser-Agents'],
     'launched':'2024-11-04','lastUpdated':'2026-05-08',
     'website':'https://browser-use.com/','domain':'browser-use.com',
     'features':"""- **DOM-aware Browser-Steuerung** mit hochpräzisen Selektoren.
- **Vision-Fallback** für CAPTCHAs und komplexe Layouts.
- **Multi-Tab-Sessions** parallel.
- **Persistente Browser-Profile** für Login-Erhalt zwischen Runs.
- **Provider-agnostisch** über LiteLLM-Wrapper.
- **Cloud-Service** für gehostete Browser-Sessions ohne Setup.
- **Recording-Mode** zur Automation-Erfassung aus Demonstrationen.""",
     'pricing':"""- **Open Source** · MIT-Lizenz, Selbst-Hosting kostenlos.
- **Cloud Starter** · $30 / Mon. — 1.000 Browser-Sessions, EU-Hosting.
- **Cloud Pro** · $99 / Mon. — 5.000 Sessions, längere Laufzeiten.
- **Cloud Scale** · ab $499 / Mon. — Volumen-basiert.
- **LLM-Kosten** zusätzlich (typisch $0,02–$0,15 / Session bei GPT-5).
- **Enterprise** · auf Anfrage, EU-Datenresidenz garantiert.""",
     'overview':"""**Browser Use** ist die wahrscheinlich populärste Open-Source-Bibliothek für Browser-automatisierende Agents — gestartet im November 2024 von einem Schweizer Team, in nur sechs Monaten zur **Standard-Wahl für LLM-gesteuerte Browser-Agents** geworden. Die GitHub-Stars haben sich Anfang 2025 explosionsartig vermehrt.

Der **technische Differenzierer** ist der **Hybrid-Ansatz**: Statt nur DOM-basiert (wie Playwright-Wrapper) oder nur vision-basiert (wie OpenAI Operator), kombiniert Browser Use beides. **DOM-Steuerung** wird priorisiert (präzise, schnell, billig), **Vision-Fallback** greift bei CAPTCHAs, Canvas-Elementen oder komplexen visuellen Layouts. In der Praxis liegt die Erfolgsrate bei alltäglichen Web-Tasks deutlich über reinen vision-basierten Tools.

Die **DOM-Awareness** macht den Workflow effizient: Der Agent sieht die Seite als strukturierten DOM-Baum mit clickable Elementen, getypten Inputs, sichtbaren Texten — nicht als Pixel-Mosaik. Ein Klick auf „Add to Cart" wird zu einem präzisen Selektor, nicht zu einem Pixel-Klick. Das spart 70–90% der Vision-Tokens und ist deutlich schneller.

**Persistente Browser-Profile** lösen das Login-Problem: Cookies, LocalStorage, Sessions bleiben zwischen Runs erhalten. Wer einen Personal-Browser-Agent baut, der wiederholt auf dieselbe Plattform geht, hat hier einen pragmatischen Pfad.

**Multi-Tab-Sessions** und **Recording-Mode** runden das Feature-Set ab — der Recording-Mode ist besonders interessant für Citizen Developers, die ein Workflow-Pattern einmal manuell durchklicken und dann als wiederverwendbare Automation speichern.

Der **Cloud-Service** (seit März 2025) hostet Browser-Sessions ohne lokales Playwright-Setup — pragmatisch für Cloud-Worker und Teams ohne DevOps-Kapazität. EU-Hosting in Zürich ist DSGVO-attraktiv.

**Provider-Agnostik** über LiteLLM-Wrapper: GPT-5, Claude Sonnet 4.7, Gemini 3, DeepSeek-V3, lokale Modelle — alle nutzbar. Wer Modell-Kosten optimieren will, kann zwischen schnellen kleinen Modellen (Routine-Klicks) und smarten großen Modellen (Reasoning-Schritte) routen.

Schwächen: Das **Browser-Setup** erfordert Engineering-Knowhow (Playwright, Chromium-Container) — Citizen Developers sind im Cloud-Tier besser aufgehoben. **Anti-Bot-Pages** (Cloudflare, Akamai) bleiben weiter ein Stolperstein, wie bei allen Browser-Agents.

Empfohlen für Engineering-Teams, die produktive Browser-Automation bauen — und für Personal-Use-Cases, in denen ein lokaler Agent regelmäßig dieselben Web-Workflows ausführt."""},

    {'slug':'langgraph','name':'LangGraph','vendor':'LangChain','category':'agenten',
     'tagline':'Graph-basierte Orchestrierung für LangChain-Agents — Cycles, State, Human-in-the-Loop und Persistence in einer Library, mit LangSmith für Tracing.',
     'price':'Open Source · LangSmith ab $39 / Sitz / Mon.','api':True,'dsgvo':'bedingt','origin':'USA',
     'rating':4.6,'reviews':5630,
     'pros':['Sehr starke Stateful-Workflow-Modellierung','Eingebauter Checkpoint-Mechanismus','Human-in-the-Loop nativ unterstützt','LangSmith-Tracing erstklassig'],
     'cons':['Konzept-Overhead höher als bei OpenAI Agents SDK','Volle Power braucht LangSmith (Bezahlservice)','LangChain-Ökosystem-Knowhow erforderlich','Versions-Migrationen bisher schmerzhaft'],
     'usecases':['Stateful Multi-Step-Workflows','Recherche-Pipelines mit Backtracking','Human-Approval-Workflows','Lange agentische Konversationen'],
     'launched':'2024-01-09','lastUpdated':'2026-05-08',
     'website':'https://www.langchain.com/langgraph','domain':'langchain.com',
     'features':"""- **Graph-Modell** mit Nodes und konditionalen Edges für komplexe Workflows.
- **State-Management** über typed Pydantic-Schemas, persistierbar.
- **Checkpoint-System** für Pause/Resume mid-execution.
- **Human-in-the-Loop** mit Interrupts vor kritischen Aktionen.
- **Streaming** von State-Updates und LLM-Tokens parallel.
- **LangSmith-Integration** für Debugging und Performance-Analyse.
- **Provider-agnostisch** (OpenAI, Anthropic, Google, lokal).""",
     'pricing':"""- **Open Source** · MIT-Lizenz, kostenlose Nutzung.
- **LangSmith Free** · 5.000 Traces / Mon., 1 User.
- **LangSmith Plus** · $39 / Sitz / Mon. — 100.000 Traces, Team-Workspaces.
- **LangSmith Enterprise** · auf Anfrage — SSO, EU-Hosting, Audit-Logs.
- **LLM-Kosten** je nach Provider zusätzlich.
- **LangGraph Cloud** (Beta) · gehostete Deployments, Pay-as-you-go.""",
     'overview':"""**LangGraph** ist seit Januar 2024 der **Weiterentwicklungs-Pfad von LangChain für Stateful Agents** — und hat sich in 18 Monaten zu einer der respektiertesten Agent-Orchestrations-Libraries entwickelt. Wer LangChain bereits nutzt und an die Grenzen einfacher Agent-Loops stößt, findet hier die natürliche Fortsetzung.

Die **Kernabstraktion** ist ein **Graph**: Nodes (Funktionen, die State transformieren), Edges (konditionale Übergänge zwischen Nodes), und ein typed State-Objekt (typisch ein Pydantic-Modell), das durch das Graph fließt. Das Modell ist mathematisch sauberer als die meisten Konkurrenten — und erlaubt **Cycles** (Backtracking, Iteration, Self-Reflection), was reine DAG-basierte Frameworks nicht können.

Das **Checkpoint-System** ist die zweite große Stärke: An beliebiger Stelle im Graph kann ein Workflow gepausiert, persistiert und Tage später fortgesetzt werden — der State landet in PostgreSQL oder Redis. Für Long-Running-Workflows (Approval-Prozesse, asynchrone Recherche, Human-Review-Loops) ein konstitutives Feature, das viele Frameworks erst nachträglich nachbauen müssen.

**Human-in-the-Loop** ist nativ unterstützt: Der Graph kann vor kritischen Aktionen (Datenbank-Schreibvorgang, externe API-Aufruf) automatisch pausieren, auf eine menschliche Freigabe warten, danach fortsetzen. Für regulierte Workflows (Healthcare, Finance, Legal) ein wichtiger Differenzierer.

**LangSmith-Integration** ist erstklassig: Jeder Step im Graph wird automatisch getrackt, mit kompletter Visualisierung des Reasoning-Pfads, der State-Übergänge und der LLM-Calls. Für Debugging und Performance-Optimierung deutlich besser als die meisten Konkurrenten — auch wenn LangSmith ab Team-Use kostet.

**Streaming** kann zwei Ebenen parallel ausgeben: LLM-Tokens (für UX) und State-Updates (für Debugging). Für interaktive Anwendungen ein versteckter Hebel.

Schwächen: Der **Konzept-Overhead** ist höher als bei OpenAI Agents SDK — wer einen einfachen Tool-Use-Agent baut, hat hier mehr Bootstrap. Das **LangChain-Ökosystem** ist groß und teils inkohärent — Knowhow zu Chains, Prompts, Memory, Tools ist Voraussetzung. **Versions-Migrationen** waren bisher mehrfach schmerzhaft (v0.1 → v0.2 → v0.3).

Empfohlen für Teams, die komplexe Stateful-Workflows mit Backtracking, Persistierung oder Human-Approval bauen — und für jeden, der LangSmith-Level-Tracing als zentrales Debug-Tool nutzen will."""},

    {'slug':'gumloop','name':'Gumloop','vendor':'Gumloop','category':'agenten',
     'tagline':'No-Code-Agent-Builder mit Drag-and-Drop-Canvas — Datenanreicherung, Recherche, Marketing-Automation in produktiven Workflows ohne Coding.',
     'price':'Free 1.000 Credits/Mon. · Pro ab $97 / Mon.','api':True,'dsgvo':'bedingt','origin':'USA',
     'rating':4.5,'reviews':1620,
     'pros':['Sehr schneller Einstieg ohne Coding','Stark für Datenanreicherung und Lead-Recherche','Vorlagen-Marktplatz mit hunderten Workflows','Multi-LLM-Routing eingebaut'],
     'cons':['Pricing pro Step kann teuer werden','Komplexere Logik braucht Workarounds','Datenresidenz USA','Weniger flexibel als Code-First-Frameworks'],
     'usecases':['Lead-Anreicherung','Content-Repurposing','Web-Scraping mit AI-Postprocessing','Marketing-Automation'],
     'launched':'2024-02-21','lastUpdated':'2026-05-08',
     'website':'https://www.gumloop.com/','domain':'gumloop.com',
     'features':"""- **Drag-and-Drop-Canvas** für Workflow-Modellierung.
- **150+ Pre-Built Nodes** für Web-Scraping, AI-Calls, CRM-Integration.
- **Multi-LLM-Routing**: GPT-5, Claude Sonnet 4.7, Gemini 3 in einem Workflow.
- **Schedule und Trigger** (Webhook, Cron, Form-Submit, Email).
- **Browser-Automation** über eingebauten Headless-Browser.
- **Vorlagen-Marktplatz** mit hunderten produktionsreifer Workflows.
- **API** für Workflow-Triggering aus eigenen Anwendungen.""",
     'pricing':"""- **Free** · 1.000 Credits / Mon., Standard-Queue, Watermark.
- **Pro** · $97 / Mon. — 30.000 Credits, kein Watermark, Priority.
- **Enterprise** · auf Anfrage — SSO, höhere Concurrency, EU-Optionen.
- **Credits** entsprechen Workflow-Steps (1 Credit ≈ 1 Step).
- **LLM-Aufrufe** kosten 1–10 Credits je nach Modell (GPT-5 teurer, Sonnet günstiger).
- **API** in allen Tarifen enthalten.""",
     'overview':"""**Gumloop** ist seit Februar 2024 einer der **am schnellsten wachsenden No-Code-Agent-Builder** im Markt — und hat sich besonders bei **Sales-, Marketing- und RevOps-Teams** etabliert, die produktive Datenanreicherungs- und Recherche-Workflows ohne Engineering-Support bauen wollen.

Die **Stärke** ist ein **klarer Drag-and-Drop-Canvas**: Nodes verbinden, Inputs konfigurieren, Output formatieren. Die **150+ Pre-Built Nodes** decken die häufigen Bausteine ab — Web-Scraping, AI-Generierung, Daten-Anreicherung über Apollo/LinkedIn/Crunchbase, CRM-Schreiben (Salesforce, HubSpot), Email-Versand (SendGrid, Mailgun), Slack-Notifications. Was bei generischen Frameworks ein eigener Connector-Build wäre, ist hier ein Klick.

**Multi-LLM-Routing** ist ungewöhnlich tief: In einem Workflow können verschiedene Steps verschiedene Modelle nutzen — ein günstiges Sonnet für Klassifikation, ein teures GPT-5 für komplexe Reasoning-Schritte, ein lokales Modell für PII-sensible Daten. Wer Kosten optimiert, hat hier einen direkten Hebel ohne separate Tool-Auswahl.

**Web-Scraping mit AI-Postprocessing** ist der häufigste Anwendungsfall: Eine Liste von Firmen-Websites scrapen, mit GPT-5 die wichtigsten Informationen extrahieren, in HubSpot anreichern, einen personalisierten Outreach-Entwurf generieren — alles in einem Workflow, der täglich gegen 10.000 Leads läuft.

Der **Vorlagen-Marktplatz** ist eine versteckte Stärke: Hunderte produktionsreife Workflows von anderen Nutzer:innen, kostenlos einsehbar und klonbar. Wer einen ähnlichen Use-Case sucht, findet meist ein 80%-passendes Template als Startpunkt.

**Schedule und Trigger** machen Workflows wirklich autonom: Webhook-, Cron-, Form-Submit- und Email-Trigger laufen ohne manuelle Aktivierung. Für Marketing-Automation und Lead-Routing-Workflows ein konstitutives Feature.

Die **API** spiegelt die UI-Workflows — pragmatisch für Teams, die Workflows in Gumloop bauen und aus eigenen Apps triggern.

Schwächen: Das **Credit-Pricing** wird bei hohem Volumen teuer — 30.000 Credits bei Pro reichen für 1.000–3.000 komplexere Workflows pro Monat, danach wird Enterprise nötig. **Komplexere Logik** (verschachtelte Loops, dynamische Branching) braucht teils Workarounds — Code-First-Frameworks (LangGraph, Agents SDK) sind hier flexibler. **Datenresidenz USA** schließt DSGVO-strikte Workflows aus.

Empfohlen für Sales-, Marketing- und RevOps-Teams, die schnell produktive Datenanreicherungs- oder Recherche-Workflows brauchen — und für Citizen Developers, die ohne Engineering-Team echte Automation ausrollen wollen."""},
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
