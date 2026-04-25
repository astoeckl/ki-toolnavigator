#!/usr/bin/env python3
"""Seed 7 additional agenten-category tools end-to-end (data + features +
pricing + overview Post + logo + website). Idempotent.

After this, run in order:
  scripts/capture_tool_screenshots.mjs   (extend slugs first)
  scripts/upload_screenshots.py
  scripts/generate_tool_images.py        (extend TOOL_CUES first)
"""
import requests, urllib3, sys
from pathlib import Path

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ROOT = Path(__file__).resolve().parent.parent
LOGOS_DIR = ROOT / 'logos'
LOGOS_DIR.mkdir(exist_ok=True)

ENV = {l.split('=',1)[0].strip(): l.split('=',1)[1].strip()
       for l in (ROOT/'.env').read_text().splitlines() if '=' in l and not l.startswith('#')}
BASE, SITE = ENV['BASEURL'], ENV['SITE']

TOOLS = [
    {'slug':'manus','name':'Manus','vendor':'Butterfly Effect','category':'agenten',
     'tagline':'Autonomer General-Purpose-Agent aus China — denkt, plant und führt komplexe Aufgaben eigenständig zu Ende.',
     'price':'Free 1.000 Credits / Tag · Plus ab $39 / Mon.','api':False,'dsgvo':'nein','origin':'China',
     'rating':4.3,'reviews':1140,
     'pros':['Sehr starke autonome Aufgabenausführung','Multi-Step-Planung mit Tool-Use','Asynchrone Ausführung im Hintergrund','Beeindruckende Web- und Code-Fähigkeiten'],
     'cons':['Datenresidenz China','Beim Launch lange Warteliste','Kein API-Zugang','Halluziniert bei mehrtägigen Aufgaben'],
     'usecases':['Marktrecherche','Reise- und Eventplanung','Datenanalyse','Software-Prototyping'],
     'launched':'2025-03-06','lastUpdated':'2026-04-22',
     'website':'https://manus.im/','domain':'manus.im',
     'features':"""- **Autonome Multi-Step-Tasks**: definiert eigenständig Teilziele und führt sie nacheinander aus.
- **Tool-Use** mit Browser, Shell, Python und Datei-System.
- **Asynchroner Modus**: Agent arbeitet weiter, auch wenn der Tab geschlossen ist.
- **Replay**-Ansicht zeigt jeden Reasoning- und Action-Step.
- **Memory** über Sessions hinweg, mit selektivem Vergessen.
- **Knowledge Base** für Dokumente, die der Agent referenzieren kann.""",
     'pricing':"""- **Free** — 1.000 Credits / Tag, max. 3 parallele Tasks.
- **Plus** · $39 / Mon. — 19.900 Credits, 5 parallele Tasks, Priority-Slot.
- **Pro** · $199 / Mon. — 200.000 Credits, 20 parallele Tasks, längere Tasks (24 h+).
- **Team** · auf Anfrage — gemeinsame Workspaces, Audit-Logs, SSO.""",
     'overview':"""**Manus** ist 2025 wie ein Komet eingeschlagen: ein chinesischer General-Purpose-Agent, der mehrstufige Aufgaben weitgehend autonom ausführt — von der Marktrecherche über die Reiseplanung bis zur Erstellung kompletter Software-Prototypen. Im Gegensatz zu Chat-Assistenten startet Manus echte Browser- und Shell-Sessions, plant Teilziele und arbeitet sie selbstständig ab.

Die **Replay-Ansicht** macht den Agent transparent: Jeder Reasoning-Schritt, jeder Tool-Call und jede Datei-Operation sind nachvollziehbar. Das war ein Game-Changer für die Akzeptanz autonomer Agenten — User können nachvollziehen, wie die Antwort zustande kam, und korrigierend eingreifen. Der **asynchrone Modus** erlaubt es, eine Aufgabe loszuschicken und Stunden später das Ergebnis abzurufen.

Schwächen sind ernst zu nehmen: Datenresidenz in China macht die Plattform für viele europäische Unternehmen ausgeschlossen. Bei Tasks über mehrere Tage halluziniert der Agent gelegentlich oder verliert den Faden. Eine API gibt es bislang nicht — Skalierung ist nur via UI möglich.

Empfohlen für Recherche-, Strategie- und Prototyping-Aufgaben, bei denen ein autonomer Agent stundenlang weiterarbeiten soll. Für regulierte Branchen aktuell nicht einsetzbar."""},

    {'slug':'devin','name':'Devin','vendor':'Cognition','category':'agenten',
     'tagline':'Autonomer KI-Software-Engineer von Cognition — schreibt, debuggt und shipt Code in eigener Sandbox-Umgebung.',
     'price':'Core ab $20 / Mon. · Team ab $500 / Mon.','api':True,'dsgvo':'bedingt','origin':'USA',
     'rating':4.1,'reviews':480,
     'pros':['Echte autonome Coding-Sessions in eigener Sandbox','Versteht große Codebases','Pull-Request am Ende, nicht nur Code-Snippet','Slack-/Linear-/GitHub-Integrationen'],
     'cons':['Hoher Preis','Lange Laufzeiten pro Task','Kann sich in Schleifen verlaufen','Keine vollständige Transparenz über Reasoning'],
     'usecases':['Bug-Fixes','Migrationen','PR-Reviews','Refactoring-Sprints'],
     'launched':'2024-03-12','lastUpdated':'2026-04-19',
     'website':'https://devin.ai/','domain':'devin.ai',
     'features':"""- **Sandbox-Umgebung**: dedizierte Container mit Browser, IDE und Shell.
- **Codebase-Indexing** via Embeddings für tiefe Kontext-Awareness.
- **Plan & Execute**-Modus mit explizitem Zwischenschritte-Plan.
- **GitHub-Integration**: Issue → autonomer Branch + Pull Request.
- **Slack-Bot**: @Devin im Channel → Task wird gestartet.
- **Knowledge Base** für Architektur-Docs und Coding-Standards.""",
     'pricing':"""- **Core** · $20 / Mon. — 250 ACU (Agent Compute Units), persönlicher Workspace.
- **Team** · $500 / Mon. — 500 ACU + 10 ACU/User-Pack, geteilter Workspace.
- **Enterprise** · auf Anfrage — On-Prem-Sandbox, SSO, dediziertes Onboarding.
- ACU-Pakete als Add-on: 100 ACU ≈ $50.
- ACU-Verbrauch hängt von Task-Länge und Modell-Wahl ab.""",
     'overview':"""**Devin** war im März 2024 der erste KI-Agent, der mit "autonomer Software-Engineer" beworben wurde — und löste damit eine eigene Welle in der Branche aus. Statt Code-Snippets zu liefern, läuft Devin in einer eigenen Sandbox-Umgebung mit Browser, IDE und Shell, und arbeitet ein Issue Schritt für Schritt zu einem Pull Request hin.

Die **Codebase-Awareness** ist das Stärkere im Vergleich zu Cursor oder Copilot: Devin indiziert große Repos und versteht so Architektur-Konventionen, ohne dass jede Datei in den Prompt geladen werden muss. Die **Slack- und GitHub-Integrationen** sind Schlüssel: Ein Engineering-Manager kann ein Linear-Ticket einfach dem Bot zuweisen und bekommt am Ende einen reviewbereiten PR.

Die Schwächen sind die typischen Probleme autonomer Agenten: Lange Tasks (45+ Min.) kosten viele ACUs, Devin kann sich in Schleifen verlaufen, und das Reasoning ist weniger transparent als bei Manus. Der Preis ist erheblich — eine Kosten-Nutzen-Rechnung lohnt sich nur, wenn echte Engineering-Stunden entlastet werden.

Empfohlen für Engineering-Teams ab 20+ Personen mit klar definierten, gut dokumentierten Bugs oder Migrationen — nicht als Ersatz, sondern als Verstärker einer existierenden Engineering-Pipeline."""},

    {'slug':'lindy','name':'Lindy','vendor':'Lindy AI','category':'agenten',
     'tagline':'No-Code-Plattform für AI-Mitarbeiter — Lindys übernehmen wiederkehrende Geschäfts-Workflows wie Sales, Support und Recruiting.',
     'price':'Free Trial · Pro ab $49,99 / Mon.','api':True,'dsgvo':'bedingt','origin':'USA',
     'rating':4.4,'reviews':560,
     'pros':['Sehr zugängliche No-Code-Oberfläche','Marketplace für vorgefertigte Lindys','Tiefe Integrationen (3.000+)','Triggerbar via Webhook, E-Mail, Slack'],
     'cons':['Komplexere Workflows brauchen Übung','Teilweise versteckte Limits','API-Zugang nur Premium','EU-Datenresidenz nicht garantiert'],
     'usecases':['Lead-Qualifizierung','Meeting-Recap','Customer-Support-Triage','Recruiting-Outreach'],
     'launched':'2023-04-01','lastUpdated':'2026-04-16',
     'website':'https://www.lindy.ai/','domain':'lindy.ai',
     'features':"""- **Lindy Phone**: AI-Agent telefoniert mit Kunden oder Leads.
- **Lindy Inbox**: liest, klassifiziert und beantwortet E-Mails autonom.
- **Lindy Meet**: nimmt an Calls teil, führt Notizen und folgt Action Items nach.
- **Marketplace** mit über 200 vorgefertigten Lindys.
- **Trigger**-Logik: E-Mail, Webhook, Schedule, Slack-Befehl, Calendar-Event.
- **Knowledge Bases** mit Auto-Refresh aus Notion, Drive, Confluence.""",
     'pricing':"""- **Free** — 400 Credits / Mon., 1 Lindy aktiv.
- **Pro** · $49,99 / Mon. — 5.000 Credits, unlimitierte Lindys, Premium-Modelle.
- **Business** · $299,99 / Mon. — 30.000 Credits, Multi-User, Priority-Support.
- **Enterprise** · auf Anfrage — SSO, SOC 2, dedizierter CSM, Custom-Lindys.
- Credits-Add-ons ab $20 / 5.000 Credits.""",
     'overview':"""**Lindy** ist die zugänglichste No-Code-Plattform für AI-Agenten am Markt. Während Tools wie LangChain und CrewAI sich an Entwickler richten, baut Lindy für Operations-Teams in Sales, Support und Recruiting — Menschen, die Workflows verstehen, aber keinen Python-Code schreiben.

Das **Trigger → Aktion**-Modell ist das Herzstück: Eine Lindy startet bei einem Event (E-Mail, Webhook, Calendar-Eintrag) und führt dann eine Kette aus AI-Schritten und Tool-Calls aus. Dazu gibt es 3.000+ Integrationen über native Konnektoren und ein Marketplace mit über 200 vorgefertigten Lindys von Wettbewerbsanalyse bis Recruiter-Outreach. **Lindy Phone** und **Lindy Meet** sind echte Differenzierungs-Features: Agenten, die telefonieren oder in Calls sitzen.

Schwächen: Komplexere Workflows mit Loops oder Bedingungen sind in der UI fummelig, manche API-Limits sind erst nach dem ersten Hit transparent, und EU-Datenresidenz ist nicht garantiert. Für regulierte Branchen ist das relevant.

Empfohlen für KMU-Operations-Teams, die wiederkehrende Workflows automatisieren wollen, ohne ein Engineering-Team zu binden. Eine ausgereifte Plattform mit echtem Produkt-Polish."""},

    {'slug':'crewai','name':'CrewAI','vendor':'CrewAI Inc.','category':'agenten',
     'tagline':'Open-Source-Framework für Multi-Agent-Orchestrierung — spezialisierte Rollen, die als Crew an einer Aufgabe arbeiten.',
     'price':'Open Source · Enterprise auf Anfrage','api':True,'dsgvo':'ja','origin':'USA',
     'rating':4.5,'reviews':840,
     'pros':['Klares Rollen-/Task-/Crew-Modell','Sehr aktive Community','Verbindbar mit jedem LLM-Provider','Self-Hosting trivial möglich'],
     'cons':['Steile Python-Lernkurve','Schwierig zu debuggen bei vielen Rollen','Enterprise-Pricing intransparent'],
     'usecases':['Research-Crews','Marketing-Pipelines','Code-Review-Crews','Datenanalyse-Teams'],
     'launched':'2023-12-01','lastUpdated':'2026-04-21',
     'website':'https://www.crewai.com/','domain':'crewai.com',
     'features':"""- **Rollen-Modell**: jede Agent-Rolle hat Goal, Backstory und Tools.
- **Tasks** definieren, was eine Crew lösen soll, mit Output-Schema.
- **Sequential & Hierarchical Process**-Modi für Koordination.
- **Tool-Bibliothek** mit 50+ vorgefertigten Capabilities.
- **CrewAI Studio**: visueller Workflow-Builder.
- **Enterprise-Cloud** mit Observability, Versionierung, Approvals.""",
     'pricing':"""- **Open Source** (MIT) — kostenlos, vollständig nutzbar.
- **CrewAI Studio Free** — 1 Crew, lokales Hosting.
- **Pro** · auf Anfrage — gehosteter Studio + Observability.
- **Enterprise** · auf Anfrage — SSO, SOC 2, Custom-Tools, dedizierter Support.
- Token-Kosten richten sich nach LLM-Provider (OpenAI, Anthropic, lokal).""",
     'overview':"""**CrewAI** hat sich neben LangChain als zweites großes Open-Source-Framework für Multi-Agent-Systeme etabliert — mit einem deutlich einfacheren Mental-Model. Statt Chains und Graphs definiert man **Rollen**: ein Researcher, ein Writer, ein Editor — jeder mit eigenem Goal, Backstory und Tool-Set. Eine **Crew** koordiniert sie auf eine **Task** hin.

Diese Klarheit ist der Hauptgrund, warum CrewAI in der Community so schnell wuchs. Wer Multi-Agent-Orchestrierung baut, beginnt oft mit einem 30-Zeilen-CrewAI-Skript — und versteht es Wochen später noch. Die **50+ Built-in-Tools** decken Web-Suche, File-IO, Code-Execution und APIs ab; eigene Tools sind in 10 Zeilen geschrieben.

CrewAI Studio ergänzt einen visuellen Workflow-Builder für nicht-Engineering-Teams. Die Enterprise-Cloud bietet Observability, Versionierung und Approval-Workflows für produktive Multi-Agent-Pipelines.

Schwächen: Mit vielen Rollen wird Debugging anspruchsvoll — Logs zeigen jede Reasoning-Iteration, aber Ursachen für Fehl-Coordination sind schwer zu finden. Enterprise-Pricing ist nicht öffentlich.

Empfohlen für Engineering-Teams, die Multi-Agent-Systeme selbst bauen wollen, und für alle, die LangChain zu komplex finden. Mit Self-Hosting ist es für DSGVO-sensitive Use-Cases die EU-freundlichste Option."""},

    {'slug':'langchain','name':'LangChain','vendor':'LangChain Inc.','category':'agenten',
     'tagline':'Die populärste Open-Source-Bibliothek für LLM-Anwendungen — von einfachen Chains bis zu komplexen Agent-Systemen.',
     'price':'Open Source · LangSmith ab $39 / Mon.','api':True,'dsgvo':'ja','origin':'USA',
     'rating':4.3,'reviews':3450,
     'pros':['Enormes Ökosystem (700+ Integrationen)','LangSmith für Tracing & Evals','LangGraph für Stateful Agents','Aktive Community + viele Beispiele'],
     'cons':['Viele Abstraktionen (Lernkurve)','API-Brüche zwischen Major-Versions','Bloated Dependencies','Debugging ohne LangSmith mühsam'],
     'usecases':['RAG-Pipelines','Custom-Agents','Chatbots','Datenextraktion'],
     'launched':'2022-10-01','lastUpdated':'2026-04-23',
     'website':'https://www.langchain.com/','domain':'langchain.com',
     'features':"""- **LangChain Core**: Chains, Prompts, Tools, Memory, Agents.
- **LangGraph**: stateful Agents als Graph mit Cycles und Persistence.
- **LangSmith**: Tracing, Eval-Suites und Production-Observability.
- **LangServe**: REST-API um jede Chain mit einer Zeile.
- **700+ Integrationen** zu LLMs, Vector-DBs, Tools.
- **Templates** für gängige Patterns (RAG, ReAct, SQL-Chains).""",
     'pricing':"""- **Open Source** (MIT) — alle Core-Bibliotheken kostenlos.
- **LangSmith Developer** · Free — 5.000 Traces / Mon., 1 Seat.
- **LangSmith Plus** · $39 / Mon. — 10.000 Traces, 5 Seats, Eval-Suite.
- **LangSmith Enterprise** · auf Anfrage — SSO, On-Prem, SLA.
- **LangGraph Cloud** · Beta — managed Graph-Hosting.""",
     'overview':"""**LangChain** ist seit 2022 *die* Open-Source-Referenz für LLM-Anwendungen — und dabei zugleich die meistgehasste Bibliothek im Bereich. Beides nicht zu Unrecht: Das Ökosystem ist mit 700+ Integrationen und Templates für nahezu jeden Use-Case unschlagbar, doch die vielen Abstraktionsschichten erfordern Wochen, bis das Mental-Model sitzt.

**LangChain Core** liefert die Bausteine: Chains, Prompts, Tools, Memory, Agents. **LangGraph** ergänzt ein deutlich saubereres Modell für Stateful Agents — gerichtete Graphen mit Cycles, Persistence und Human-in-the-Loop-Steps. **LangSmith** ist das kommerzielle Komplement: Tracing für jeden Run, Eval-Suites für regression-resistente Updates und Production-Observability.

Die Schwäche bleibt die Komplexität: Viele Wege führen ans gleiche Ziel, API-Brüche zwischen Versionen sind real, und ohne LangSmith ist Debugging im Produktivbetrieb mühsam. Wer einfache Use-Cases hat, ist mit CrewAI oder direkter SDK-Nutzung oft schneller.

Empfohlen für Engineering-Teams, die produktive LLM-Anwendungen mit komplexer Orchestrierung bauen — oder für jeden, der den größten Pool an Beispielen und Integrationen sucht. Beim Self-Hosting voll EU-fähig."""},

    {'slug':'relevance-ai','name':'Relevance AI','vendor':'Relevance AI','category':'agenten',
     'tagline':'No-Code-Plattform für AI-Workforce-Agents — Sales-, Marketing- und Operations-Workflows als trainierbare digitale Mitarbeiter.',
     'price':'Free 100 Credits · Pro ab $19 / Mon.','api':True,'dsgvo':'bedingt','origin':'Australien',
     'rating':4.4,'reviews':390,
     'pros':['Sehr klares Agent-Konzept','Tools-Marketplace mit über 100 Skills','Eigene LLM-Logik mit Multi-Step-Chains','Visueller Builder + Code-Editor'],
     'cons':['Kleinere Community','Pricing-Modell mit Credits unübersichtlich','EU-Datenresidenz kostenpflichtig','Wenig deutsche Doku'],
     'usecases':['Sales-Outreach','Lead-Anreicherung','Internal-Knowledge-Bots','Recruiting-Pipelines'],
     'launched':'2020-09-01','lastUpdated':'2026-04-14',
     'website':'https://relevanceai.com/','domain':'relevanceai.com',
     'features':"""- **Agents**: Rollen mit Tools, Knowledge und Trigger.
- **Tools-Marketplace**: 100+ vorgefertigte Skills (CRM, Email, Web).
- **AI Workforce-Konzept**: Agents als digitale Team-Mitglieder.
- **Multi-Step-Chains** mit verschachtelten Bedingungen.
- **Knowledge-Layer** mit Vector-DB-Anbindung (eigene oder Pinecone).
- **API** für Headless-Integration in eigene Anwendungen.""",
     'pricing':"""- **Free** — 100 Credits, 1 Agent, 1 Tool, Community-Support.
- **Pro** · $19 / Mon. — 10.000 Credits, unlimitierte Agents, alle Tools.
- **Team** · $199 / Mon. — 100.000 Credits, Multi-User, Premium-Modelle.
- **Business** · $599 / Mon. — Custom Limits, Slack-Integration, EU-Region.
- **Enterprise** · auf Anfrage — SSO, dedizierter Support, On-Prem-Option.""",
     'overview':"""**Relevance AI** vermarktet seine Plattform als "AI Workforce" — Agenten als digitale Mitarbeiter, die Sales-, Marketing- und Operations-Workflows in Eigenregie übernehmen. Das Mental-Model ist bewusst HR-nah: jede Rolle bekommt ein Job-Profil, Tools, Knowledge und ein Onboarding.

Der **Tools-Marketplace** ist das Herzstück: über 100 vorgefertigte Skills von HubSpot-Lookup über LinkedIn-Recherche bis zum Slack-Notify. Eigene Tools sind in TypeScript oder Python in wenigen Zeilen geschrieben. Die Multi-Step-Chains erlauben verschachtelte Logik mit Bedingungen und Schleifen — visueller Builder und Code-Editor wechseln sich nahtlos ab.

Schwächen: Die Community ist deutlich kleiner als bei LangChain oder CrewAI, das Credit-basierte Pricing-Modell ist im Voraus schwer zu kalkulieren, und EU-Datenresidenz wird erst ab dem Business-Tarif garantiert.

Empfohlen für KMU-Operations-Teams ohne Engineering-Backbone, die spezialisierte AI-Mitarbeiter für klar abgegrenzte Workflows brauchen. Wer Multi-Agent-Pipelines als Engineering-Team selbst baut, ist mit CrewAI besser bedient."""},

    {'slug':'activepieces','name':'Activepieces','vendor':'Activepieces','category':'agenten',
     'tagline':'Open-Source-Alternative zu Zapier mit eingebauten AI-Pieces — selbst-hostbar, fair-code-Lizenz, EU-freundlich.',
     'price':'Cloud Free · Cloud Plus ab $25 / Mon.','api':True,'dsgvo':'ja','origin':'EU (NL)',
     'rating':4.5,'reviews':720,
     'pros':['Komplett selbst hostbar (MIT-licensed Pieces)','280+ vorgefertigte Pieces','AI-Pieces für OpenAI/Anthropic/HF','Saubere visuelle UI'],
     'cons':['Jüngeres Ökosystem als n8n','Manche Pieces unvollständig','Performance bei sehr großen Flows wackelig'],
     'usecases':['Marketing-Automation','Lead-Sync','AI-Pipelines','Slack-Bots'],
     'launched':'2022-12-01','lastUpdated':'2026-04-20',
     'website':'https://www.activepieces.com/','domain':'activepieces.com',
     'features':"""- **280+ Pieces** als modulare Bausteine (CRM, Email, AI, DevOps).
- **AI-Pieces** für OpenAI, Anthropic, Hugging Face, Replicate.
- **Self-Hosting** in Docker oder Kubernetes (Apache 2.0).
- **Branchen** und **Loops** für komplexe Logik.
- **API**-Trigger und **Webhooks** für jede externe Integration.
- **Activepieces Cloud** für gemanagtes Hosting.""",
     'pricing':"""- **Self-Hosted** — kostenlos, alle Pieces verfügbar.
- **Cloud Free** — 1.000 Tasks / Mon., 1 Projekt, 2 Seats.
- **Cloud Plus** · $25 / Mon. — 10.000 Tasks, unlimitierte Projekte.
- **Cloud Business** · $99 / Mon. — 100.000 Tasks, Audit-Logs, Premium-Pieces.
- **Enterprise** · auf Anfrage — On-Prem-Lizenz, SSO, dediziertes Onboarding.""",
     'overview':"""**Activepieces** ist die offene, EU-basierte Antwort auf Zapier — und die jüngere Schwester von n8n. Mit Apache-2.0-Lizenz für die Pieces-Bibliothek ist die Plattform vollständig selbst hostbar, ohne die Lizenz-Einschränkungen, die bei n8n diskutiert werden.

Die **Pieces-Bibliothek** umfasst 280+ Konnektoren — von HubSpot über Notion bis zu OpenAI und Anthropic. Eigene Pieces sind in TypeScript geschrieben, mit klarem SDK und Hot-Reload. Die **AI-Pieces** sind besonders ausgereift: nicht nur einfache Chat-Calls, sondern Helper für RAG, Function-Calling und Multi-Step-Reasoning.

Die Bedienung ist sauber und schnell, der visuelle Editor weniger überladen als bei n8n. Loops, Branches und Conditional Steps sind erstklassig integriert. **Activepieces Cloud** bietet gemanagtes Hosting, falls Self-Hosting nicht passt.

Schwächen: Mit 720 Reviews und einem 2022-Launch ist das Ökosystem jünger als n8n oder Zapier; manche Pieces sind noch unvollständig (oft Community-Beiträge). Bei sehr großen Workflows (50+ Steps) wackelt die Performance gelegentlich.

Empfohlen für Teams, die n8n-ähnliche Automation suchen, aber eine echte Apache-2.0-Lizenz brauchen — ideal für Behörden, regulierte Branchen und Open-Source-Verfechter."""},
]

DOMAINS = {t['slug']: t['domain'] for t in TOOLS}

# ---- Login ----
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
