#!/usr/bin/env python3
"""Seed 7 coding-category tools end-to-end (data + features + pricing + overview Post + logo + website).
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
    {'slug':'claude-code','name':'Claude Code','vendor':'Anthropic','category':'coding',
     'tagline':'Anthropic-eigener Terminal-CLI für Claude — agentisches Pair-Programming direkt in der Shell und in jeder IDE.',
     'price':'Im Claude-Pro/Max-Tarif enthalten · API ab $3 / 1 M Token','api':True,'dsgvo':'bedingt','origin':'USA',
     'rating':4.7,'reviews':2840,
     'pros':['Tiefe Codebase-Awareness via Sub-Agents','Hooks für Lifecycle-Events','MCP-Server-Marketplace','Funktioniert nativ in jeder IDE und im Terminal'],
     'cons':['Verbraucht viele Tokens schnell','Permission-Prompts können nerven','Anthropic-Lock-in (kein Modell-Routing)'],
     'usecases':['Refactoring-Sprints','Bug-Fixes','Code-Reviews','Migrations'],
     'launched':'2024-08-01','lastUpdated':'2026-04-23',
     'website':'https://www.anthropic.com/claude-code','domain':'anthropic.com',
     'features':"""- **Agentic Loop** mit eigenem Toolset (Bash, Edit, Read, Write, Grep, Glob).
- **Sub-Agents** für spezialisierte Aufgaben (general-purpose, code-reviewer, …).
- **Hooks** auf Lifecycle-Events (PreToolUse, PostToolUse, Stop, UserPromptSubmit).
- **MCP-Server** zum Anbinden externer Tools (GitHub, Slack, Datenbanken, Browser).
- **Slash-Commands** als wiederverwendbare Workflow-Snippets.
- **Plan Mode** für read-only-Recherche vor destruktiven Änderungen.
- **Background Tasks** für lange laufende Builds und Tests.""",
     'pricing':"""- **Free** über die API (Pay-per-use).
- **Claude Pro** · $20 / Mon. — Claude Code mit fairer Nutzung enthalten.
- **Claude Max** · $100/$200 / Mon. — deutlich höhere Limits, Priority Access.
- **Team** · $30 / Sitzplatz / Mon. (min. 5) — gemeinsamer Workspace.
- **API direct**: Sonnet $3 in / $15 out · Opus höher; Token-Verbrauch real.
- Enterprise via Bedrock und Vertex (EU-Region).""",
     'overview':"""**Claude Code** ist Anthropics eigene CLI für agentisches Pair-Programming — und seit dem Sommer 2024 die Standardwahl für viele Teams, die Sonnet 4.5 / 4.6 / 4.7 für anspruchsvolle Coding-Aufgaben einsetzen. Statt im Editor zu sitzen, läuft Claude Code in jedem Terminal, hat vollen Tool-Zugriff und arbeitet sich autonom durch mehrstufige Aufgaben.

Die Stärken liegen in den **Sub-Agents** (delegierte Worker für Recherche, Code-Reviews, Tests), den **Hooks** (Skripte, die bei Lifecycle-Events feuern, etwa Linter nach jedem Edit) und dem **MCP-Server-Marketplace**: tausende Drittanbieter-Tools — GitHub, Linear, Datenbanken, Browser, eigene APIs — werden über das Model-Context-Protocol angedockt und sind sofort vom Agent nutzbar.

**Plan Mode** ist eine wertvolle Eskalationsbremse: vor destruktiven Änderungen (Migrationen, große Refactorings) erstellt Claude einen Read-only-Plan zur Freigabe. **Slash-Commands** verpacken eigene Workflows zu wiederverwendbaren Aktionen — etwa `/security-review` oder `/babysit-prs`.

Schwächen: Token-Verbrauch ist real und kann bei großen Codebases schnell teuer werden. Das **Permission-System** zeigt jeden Bash-Call zur Bestätigung — produktiv ab Tag 3 nach gut konfigurierten Allowlists.

Empfohlen für Engineering-Teams, die Claude bereits als Modell der Wahl nutzen und Coding aus dem Terminal als ihren Hauptworkflow sehen — eine sehr ausgereifte Alternative oder Ergänzung zu Cursor und Windsurf."""},

    {'slug':'codex-cli','name':'Codex','vendor':'OpenAI','category':'coding',
     'tagline':'OpenAIs autonomer Coding-Agent als CLI und Cloud-Worker — schreibt Code, führt Tests aus, eröffnet PRs.',
     'price':'Cloud im ChatGPT-Plus/Pro · CLI Free · API ab $2 / 1 M Token','api':True,'dsgvo':'bedingt','origin':'USA',
     'rating':4.4,'reviews':1980,
     'pros':['Cloud-Worker für asynchrone Tasks','GitHub-Integration: Issue → PR','CLI mit eigener Sandbox','GPT-5-Codex stark in Tool-Use'],
     'cons':['Cloud-Worker im günstigen Tarif limitiert','Datenresidenz USA','Pricing pro Aufgabe schwer planbar','UI mehrgleisig (CLI vs. Cloud vs. Plugin)'],
     'usecases':['Bug-Fixes','Tests-Generierung','Refactoring','Code-Reviews'],
     'launched':'2025-05-16','lastUpdated':'2026-04-21',
     'website':'https://chatgpt.com/codex','domain':'openai.com',
     'features':"""- **Codex Cloud**: parallele Tasks im Hintergrund, jede in eigener Sandbox.
- **Codex CLI**: Terminal-Agent mit Sandboxing und Tool-Use.
- **GitHub-Integration**: Issue zuweisen → Branch + PR.
- **VS-Code-Plugin** mit Inline-Edit und Chat.
- **GPT-5-Codex** als spezialisiertes Coding-Modell (Long-Context + Tool-Use).
- **Custom Setup-Skripte** pro Repo für reproduzierbare Sandbox-Umgebungen.""",
     'pricing':"""- **CLI** · Free auf eigener API-Nutzung.
- **ChatGPT Plus** · $20 / Mon. — Codex Cloud mit moderatem Limit.
- **ChatGPT Pro** · $200 / Mon. — sehr hohe Cloud-Limits, längere Tasks.
- **Team** · $30 / Sitz / Mon. — geteilter Workspace, Audit-Trails.
- **Enterprise** · auf Anfrage — SSO, SCIM, EU-Datenresidenz, BAA.
- API direct: GPT-5 ab $1.25 in / $10 out pro 1 M Token.""",
     'overview':"""**Codex** war ursprünglich der Name eines OpenAI-Coding-Modells aus 2021 — und ist heute eine ganze Produktfamilie aus CLI, Cloud-Worker und IDE-Plugin, alle gemeinsam unter dem Dach des **GPT-5-Codex**-Modells. OpenAIs Antwort auf Devin und Claude Code für agentisches Pair-Programming und autonome Aufgaben-Bearbeitung.

**Codex Cloud** ist die spannendste Komponente: Im ChatGPT-Web-Interface gestartete Tasks laufen parallel in dedizierten Sandboxes, jede mit Zugriff auf das verbundene Repo und einer eigenen Setup-Routine. Tasks dauern Minuten oder Stunden, der User bekommt am Ende einen Pull Request inklusive Tests, der Plan und die Zwischenschritte sind nachvollziehbar.

Die **CLI** läuft im Terminal mit eigenem Sandboxing — direktes Pendant zu Claude Code, mit dem Vorteil von OpenAIs Toolkette. Das **VS-Code-Plugin** liefert Inline-Edits und einen Chat, der das offene Repo als Kontext kennt.

Schwächen: Im Plus-Tarif sind Cloud-Worker stark limitiert (typisch 5–10 parallele Tasks pro Tag), die Datenresidenz liegt in den USA, und die Vielfalt der Eintrittspunkte (CLI, Cloud, Plugin) macht die Auswahl nicht einfacher. Wer bei OpenAI bleibt, bekommt aber einen sehr ausgereiften Stack.

Empfohlen für Engineering-Teams, die ChatGPT bereits als Standard nutzen und einen Mix aus interaktiver IDE-Arbeit und asynchronen Background-Tasks anstreben."""},

    {'slug':'bolt','name':'Bolt.new','vendor':'StackBlitz','category':'coding',
     'tagline':'AI-Pair-Programmer für Full-Stack-Web-Apps im Browser — von Prompt zur deploybaren Vite/Next-App in Minuten.',
     'price':'Free · Pro ab $20 / Mon.','api':False,'dsgvo':'bedingt','origin':'USA',
     'rating':4.4,'reviews':1620,
     'pros':['Komplett im Browser (WebContainer)','Direkt deploybar nach Netlify','Multi-Framework (Astro, Next.js, Vite, Svelte)','Mobile-App-Modus mit Capacitor'],
     'cons':['Token-Limits eskalieren bei großen Apps','Komplexere Backend-Logik wackelig','Wenig Kontrolle über Architektur','Kein lokales Hosting'],
     'usecases':['MVP-Prototypen','Landing-Pages','Internal Tools','Produktdemos'],
     'launched':'2024-10-01','lastUpdated':'2026-04-19',
     'website':'https://bolt.new/','domain':'bolt.new',
     'features':"""- **WebContainer**: Node.js + Vite + npm direkt im Browser.
- **Multi-Framework-Support**: Next.js, Astro, Svelte, SolidJS, Vite-Vanilla.
- **Database-Integrationen**: Supabase, Convex, Cloudflare D1.
- **Bolt Mobile** mit Capacitor für iOS/Android.
- **One-Click-Deploy** nach Netlify oder Vercel.
- **GitHub-Sync** für vollständigen Code-Export.""",
     'pricing':"""- **Free** · 1 M Token / Monat zum Probieren.
- **Pro** · $20 / Mon. — 10 M Token, private Projekte, Custom-Domain.
- **Pro 50** · $50 / Mon. — 26 M Token, höhere Geschwindigkeit.
- **Pro 100** · $100 / Mon. — 55 M Token, Mobile-App-Modus.
- **Teams** · $30 / Sitz / Mon. — gemeinsame Workspaces, Admin-Tools.""",
     'overview':"""**Bolt.new** ist das Aushängeschild von StackBlitz — und gleichzeitig die radikalste Verkörperung des "AI baut deine App"-Versprechens. Komplett im Browser über die WebContainer-Technologie läuft Node.js, npm, Vite und das Build-System nativ — ohne Container-Roundtrip.

Der Workflow ist verblüffend einfach: Prompt eingeben (z. B. "Aufgabenliste mit Drag&Drop, dunklem Modus und Supabase-Backend"), 30–60 Sekunden warten, der App-Code entsteht live im Editor, läuft im rechten Preview-Panel und wartet auf Verfeinerungs-Prompts. Mit einem Klick deployt Bolt nach Netlify oder Vercel — fertige URL inklusive.

Die **Multi-Framework-Unterstützung** macht Bolt vielseitiger als spezialisierte Konkurrenz: ob Next.js, Astro, Svelte oder Vanilla-Vite, der Agent passt seinen Output an. **Bolt Mobile** mit Capacitor ist 2026 dazugekommen und erlaubt iOS-/Android-Apps aus demselben Web-Stack.

Schwächen: Token-Limits eskalieren schnell, sobald eine App über mehrere Komponenten und Daten-Layer wächst. Komplexe Backend-Logik (Race Conditions, Transactions) bleibt schwierig. Wer mehr Kontrolle über Architektur und Code-Qualität braucht, ist mit Cursor/Claude Code besser dran.

Empfohlen für MVP-Prototypen, Landing-Pages, Internal Tools und Produktdemos — alles, was schnell sichtbar werden muss, ohne Enterprise-Anspruch an Code-Qualität."""},

    {'slug':'v0','name':'v0','vendor':'Vercel','category':'coding',
     'tagline':'Vercels AI-UI-Generator — von Prompt oder Screenshot zu produktionsreifem React-/shadcn-Code mit einem Klick.',
     'price':'Free · Premium ab $20 / Mon.','api':True,'dsgvo':'bedingt','origin':'USA',
     'rating':4.5,'reviews':1430,
     'pros':['Sehr saubere shadcn/ui-Outputs','Iteratives Refining im Chat','Direkt nach Vercel deploybar','Screenshot-zu-Code-Funktion'],
     'cons':['Stark React/Next.js-zentriert','Backend-Logik nur rudimentär','Premium-Modelle erst ab Premium','Wenig Architektur-Freiheit'],
     'usecases':['UI-Komponenten','Marketing-Pages','Admin-Dashboards','Design-System-Erweiterungen'],
     'launched':'2023-10-12','lastUpdated':'2026-04-22',
     'website':'https://v0.dev/','domain':'vercel.com',
     'features':"""- **Prompt → React-Komponente** mit shadcn/ui und Tailwind.
- **Screenshot Upload**: Mockup hochladen, Code zurückbekommen.
- **v0 Chat** für iterative Verfeinerung.
- **Open in Codespace** für tiefes Refactoring.
- **Vercel-Deploy** in einem Klick.
- **Templates Marketplace** mit kuratierten Starter-Setups.""",
     'pricing':"""- **Free** · 200 Credits / Monat, 5 Projekte, öffentlich.
- **Premium** · $20 / Mon. — 5.000 Credits, private Projekte, Premium-Modelle.
- **Team** · $30 / Sitz / Mon. — gemeinsame Workspaces, Admin.
- **Enterprise** · auf Anfrage — SSO, SAML, dedizierte Limits, EU-Region.
- Credit-Verbrauch hängt von Modell-Wahl und Komplexität ab.""",
     'overview':"""**v0** ist Vercels Antwort auf die Frage, wie React- und Next.js-Apps schneller gebaut werden können — und gleichzeitig die wahrscheinlich beste UI-zu-Code-Engine am Markt. Statt komplette Apps zu generieren wie Bolt fokussiert v0 auf **Komponenten und Pages**: Ein Prompt oder ein Screenshot wird zu sauberem shadcn/ui-Code mit Tailwind-Klassen, der direkt ins eigene Projekt kopiert werden kann.

Die Stärke liegt in der **Code-Qualität**: Die Outputs nutzen die etablierten Patterns von shadcn/ui (Radix-basierte Primitives, Tailwind-Klassen, sauberes TypeScript) — kein generierter Spaghetti-Code, sondern Komponenten, die sich wie hand-geschrieben lesen. **Iteratives Refining** funktioniert im Chat, und mit "Open in Codespace" lässt sich die Komponente in einem vollwertigen VS-Code-Devspace weiter bearbeiten.

**Screenshot-zu-Code** ist 2026 reif geworden: Ein Figma-Export oder ein Konkurrenz-Screenshot wird zu spielfertigem Code, oft 80 % brauchbar. Mit dem **Vercel-Deploy-Knopf** ist eine Komponente in zwei Klicks live.

Schwächen: v0 ist klar React/Next.js-fokussiert. Wer Vue, Svelte oder Backend-heavy-Logik braucht, ist mit Bolt oder Cursor besser bedient. Backend-Endpoints sind möglich, aber rudimentär.

Empfohlen für React-Teams, die Design-Systeme effizient erweitern, Marketing-Pages bauen oder Admin-Dashboards prototypen — und für jeden, der bereits Vercel als Deployment-Plattform nutzt."""},

    {'slug':'tabnine','name':'Tabnine','vendor':'Tabnine','category':'coding',
     'tagline':'Enterprise-AI-Coding-Assistent mit Self-Hosting-Option — datenschutzkonform und mit lokal-trainierten Custom-Modellen.',
     'price':'Free · Dev ab $9 / Mon. · Enterprise ab $39 / Sitz / Mon.','api':True,'dsgvo':'ja','origin':'EU/USA (Israel)',
     'rating':4.0,'reviews':1480,
     'pros':['Self-Hosting verfügbar','Custom-Modelle auf eigener Codebase','Sehr breite IDE-Unterstützung','Datenresidenz-Garantien (EU, On-Prem)'],
     'cons':['Vorschläge weniger smart als bei Cursor/Copilot','Enterprise-Setup aufwändig','Custom-Training-Aufwand erheblich'],
     'usecases':['Banken','Behörden','Defense','Regulierte Branchen'],
     'launched':'2018-11-01','lastUpdated':'2026-04-15',
     'website':'https://www.tabnine.com/','domain':'tabnine.com',
     'features':"""- **Self-Hosted-Deployment** in eigener Cloud oder On-Prem.
- **Custom-Models** auf der eigenen Codebase trainierbar.
- **Code-Completion**, Chat und Test-Generierung.
- **15+ IDE-Plugins**: VS Code, JetBrains, Eclipse, Visual Studio, Neovim, Vim.
- **SOC 2 Type II**, ISO 27001, BAA-fähig.
- **AWS Bedrock** und **Azure OpenAI** als optionale LLM-Backends.""",
     'pricing':"""- **Free** · Basic Completions, kleine Modelle.
- **Dev** · $9 / Sitz / Mon. — Pro-Modelle, Chat, Tests.
- **Enterprise** · $39 / Sitz / Mon. — SSO, Self-Hosted, Custom-Models.
- **Defense** · auf Anfrage — Air-Gapped-Deployment, FIPS-140-3.
- Custom-Model-Training: einmalige Setup-Gebühr + laufende Inferenz.""",
     'overview':"""**Tabnine** war 2018 einer der ersten AI-Coding-Assistenten — und ist 2026 die wahrscheinlich datenschutzfreundlichste Wahl im Enterprise-Markt. Während GitHub Copilot, Cursor und Windsurf grundsätzlich Cloud-basiert arbeiten, kann Tabnine **vollständig selbst gehostet** werden — in der eigenen Cloud, on-premises, sogar air-gapped.

Die **Custom-Models** sind der zweite große USP: Banken, Behörden und Regulierte Branchen können Tabnine-Modelle auf der eigenen Codebase fein-trainieren und damit Vorschläge bekommen, die zu den internen Patterns, Frameworks und Konventionen passen — ohne dass Code je das eigene Netzwerk verlässt.

**IDE-Reichweite** ist breiter als bei jedem Konkurrenten: 15+ Plugins inklusive Eclipse, Visual Studio (nicht Code) und sogar Vim. Compliance-Stack ist enterprise-klasse: SOC 2 Type II, ISO 27001, BAA-fähig für HIPAA, FIPS-140-3 in der Defense-Variante.

Schwäche: Die reine **Vorschlagsqualität** liegt unter Cursor und Copilot — Tabnine arbeitet konservativer, manchmal hinkt es bei brandneuen Frameworks hinterher. Wer kein striktes Self-Hosting braucht, fährt mit Copilot oder Cursor angenehmer.

Empfohlen für Banken, Behörden, Verteidigung und alle Branchen, in denen Codebases unter keinen Umständen das eigene Netz verlassen dürfen — und für Konzerne, die ein zentral verwaltetes, compliance-zertifiziertes AI-Coding-Werkzeug für tausende Entwickler brauchen."""},

    {'slug':'continue','name':'Continue','vendor':'Continue Dev','category':'coding',
     'tagline':'Open-Source-AI-Coding-Plattform für VS Code und JetBrains — selbst hostbar, jeder LLM verwendbar.',
     'price':'Open Source · Hub Free · Enterprise auf Anfrage','api':True,'dsgvo':'ja','origin':'USA',
     'rating':4.6,'reviews':920,
     'pros':['Open Source (Apache 2.0)','LLM-agnostisch','Custom-Workflows via .continuerc','Aktive Community + Hub'],
     'cons':['Konfiguration aufwändiger als bei Cursor','Wenig Polish im Vergleich zu Premium-Tools','Eigene LLM-Kosten via Provider'],
     'usecases':['DSGVO-strenge Teams','Self-Hosted-Setups','Multi-Provider-Routing','Custom-IDE-Workflows'],
     'launched':'2023-05-01','lastUpdated':'2026-04-23',
     'website':'https://www.continue.dev/','domain':'continue.dev',
     'features':"""- **Multi-Provider**: OpenAI, Anthropic, Mistral, lokale Ollama, AWS Bedrock.
- **Plug-In für VS Code und JetBrains** — beide gepflegt.
- **Continue Hub**: Marketplace für Custom-Models und Assistants.
- **Slash-Commands** wie `/edit`, `/test`, `/comment`.
- **Custom Context Providers** (Codebase, Open Files, Git Diff, Terminal).
- **Self-Hosted Hub** für Enterprise-Deployments.""",
     'pricing':"""- **Open Source** (Apache 2.0) — vollständig kostenlos.
- **Continue Hub Free** — Community-Assistants, persönliche Konfiguration.
- **Hub Pro** · in Beta — geteilte Workspaces, Premium-Models.
- **Enterprise** · auf Anfrage — Self-Hosted Hub, SSO, Audit-Logs.
- LLM-Kosten richten sich nach gewähltem Provider.""",
     'overview':"""**Continue** ist die Open-Source-Antwort auf Cursor und Windsurf: ein VS-Code- und JetBrains-Plugin, das jeden LLM-Provider unterstützt — OpenAI, Anthropic, Mistral, lokale Ollama-Modelle, AWS Bedrock — und sich tief konfigurieren lässt. Wer Cursor zu proprietär findet oder strikte DSGVO-Anforderungen hat, findet hier eine echte Alternative.

Das Mental-Modell ist deklarativ: In `.continuerc.json` wird festgelegt, welche Modelle für welche Aufgabe genutzt werden, welche Context-Provider verfügbar sind (Codebase-Embedding, offene Dateien, Git-Diff, Terminal-Output) und welche Slash-Commands zur Verfügung stehen (`/edit`, `/test`, `/comment`, eigene Workflows). Das gibt mehr Flexibilität als jede SaaS-Lösung — kostet aber Konfigurationszeit.

**Continue Hub** ist 2025 als Community-Marketplace gestartet: Vorgefertigte Assistants (z. B. "Code-Reviewer für Python-Backends", "Terraform-Helfer") können installiert und mit eigenen Modellen kombiniert werden. **Self-Hosted Hub** für Enterprise-Deployments mit SSO und Audit-Logs ist in Beta.

Schwächen: Die UI fühlt sich roher an als bei Cursor, manche Features (Tab-Completion, Agent-Modus) hinken hinterher. Eigenes Provider-Setup bedeutet, dass auch Tokenkosten selbst überblickt werden müssen.

Empfohlen für Engineering-Teams mit strengen Datenschutzanforderungen, für alle, die Multi-Provider-Routing brauchen, und für jeden, der das beste OSS-Coding-Plugin sucht."""},

    {'slug':'aider','name':'Aider','vendor':'Aider','category':'coding',
     'tagline':'Open-Source-Pair-Programmer für das Terminal — mit Git-Integration, Multi-File-Edits und LLM-agnostisch.',
     'price':'Open Source · Pay-per-API','api':True,'dsgvo':'ja','origin':'USA',
     'rating':4.7,'reviews':1310,
     'pros':['Git-First-Workflow mit Auto-Commit','Multi-File-Edits in einem Lauf','LLM-agnostisch (Claude, GPT, Gemini, lokal)','Repository-Map für Codebase-Awareness'],
     'cons':['Kein GUI — reine CLI','Lernkurve für Slash-Commands','Token-Kosten bei großen Repos'],
     'usecases':['Refactorings','Bug-Fixes','Greenfield-Skripte','Doku-Updates'],
     'launched':'2023-05-01','lastUpdated':'2026-04-20',
     'website':'https://aider.chat/','domain':'aider.chat',
     'features':"""- **Git-Integration**: jede Edit-Session wird automatisch commitet.
- **Repository-Map** mit dynamischer Auswahl relevanter Dateien.
- **Multi-File-Edits** in einem Prompt.
- **LLM-agnostisch** (Claude, GPT, Gemini, DeepSeek, lokal via LiteLLM).
- **/voice**-Modus für Sprachsteuerung.
- **Web-Modus** für GitHub-Issue-Workflows.""",
     'pricing':"""- **Open Source** (Apache 2.0) — kostenlos.
- LLM-Kosten richten sich nach Provider.
- Typisch: $1 – $5 pro mittlerer Coding-Session mit Sonnet 4.6.
- DeepSeek- oder lokale-Modelle deutlich günstiger.
- Keine SaaS-Komponente, kein Subscription-Lock-in.""",
     'overview':"""**Aider** ist die wahrscheinlich populärste Open-Source-CLI für AI-Pair-Programming — und der direkteste Konkurrent zu Claude Code und Codex CLI. Was Aider auszeichnet, ist die **Git-First-Philosophie**: Jeder Edit, den der Agent macht, wird sofort commitet, mit aussagekräftiger Commit-Message. Das macht das Reverten von Fehlentscheidungen trivial — `git reset HEAD~1` und weiter geht's.

Die **Repository-Map** ist die zweite Stärke: Aider scannt das Repo, extrahiert Funktions- und Klassen-Signaturen mit Tree-Sitter und nutzt dieses Wissen für jeden Prompt — ohne den vollen Code in den Context laden zu müssen. Bei großen Repos spart das massiv Tokens und macht Multi-File-Edits zuverlässig.

**LLM-Agnostik** ist Standard: Claude Sonnet, GPT-5, Gemini, DeepSeek-V3, lokale Modelle via LiteLLM — alles funktioniert mit derselben Konfigurationsdatei. Der **/voice**-Modus erlaubt Hands-Free-Workflows (etwa beim Pair-Programming am Whiteboard), der **Web-Modus** integriert sich in GitHub-Issue-Workflows.

Schwächen: Aider ist reine CLI — kein Editor, kein GUI, kein Tab-Completion. Wer sein Coding-Tool im IDE-Kontext braucht, ist mit Cursor oder Continue besser dran. Die Slash-Commands haben Lernkurve.

Empfohlen für Terminal-affine Engineering-Teams, die maximale Kontrolle über Modell und Workflow wollen — und für jeden mit DSGVO-Anforderungen, die nur lokale oder europäische Modelle erlauben."""},
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
                    'name': f'{tool["name"]} Logo',  # avoid "/" in name
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
