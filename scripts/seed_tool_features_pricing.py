#!/usr/bin/env python3
"""Extend the `tool` content type with markdown `features` and `pricing` fields,
then seed per-tool content.
"""
import requests, urllib3, sys
from pathlib import Path

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ROOT = Path(__file__).resolve().parent.parent
ENV = {l.split('=',1)[0].strip(): l.split('=',1)[1].strip()
       for l in (ROOT/'.env').read_text().splitlines() if '=' in l and not l.startswith('#')}
BASE, SITE = ENV['BASEURL'], ENV['SITE']

r = requests.post(f'{BASE}/auth/login',
    data={'grant_type':'password','username':ENV['EMAIL'],'password':ENV['PW']},
    headers={'Content-Type':'application/x-www-form-urlencoded'}, verify=False)
H = {'Authorization': f'Bearer {r.json()["access_token"]}', 'Content-Type': 'application/json'}
print('✓ Logged in')

# ---- 1. Extend schema ----
cts = requests.get(f'{BASE}/{SITE}/contenttypes/', headers=H, verify=False).json()
tool_ct = next(c for c in cts if c.get('display_identifier') == 'tool')
schema = tool_ct.get('schema', {})
props = schema.get('properties', {})
patched = False
if 'features' not in props:
    props['features'] = {'type': 'string', 'title': 'Funktionen (Markdown)', 'description': 'Kern-Funktionen des Tools, redaktionell gepflegt.'}
    patched = True
if 'pricing' not in props:
    props['pricing'] = {'type': 'string', 'title': 'Preise (Markdown)', 'description': 'Preis-/Tarifübersicht.'}
    patched = True
if patched:
    schema['properties'] = props
    r = requests.patch(f'{BASE}/{SITE}/contenttypes/{tool_ct["id"]}',
        json={'schema': schema}, headers=H, verify=False)
    if not r.ok:
        sys.exit(f'❌ schema patch failed: {r.status_code} {r.text[:300]}')
    print('  ✓ added features + pricing to tool schema')
else:
    print('  · schema already has features + pricing')

# ---- 2. Per-tool content ----
FEATURES = {
'chatgpt': """- **GPT-5 & GPT-5 mini** — die aktuellen Modelle des Anbieters mit deutlich verbesserter Reasoning-Qualität.
- **Multimodale Eingabe**: Text, Bild, Dokumente, Sprache — alles im selben Chat.
- **Custom GPTs & GPT-Store** — eigene Assistenten bauen, teilen oder aus dem Marktplatz installieren.
- **DALL·E 3** für direkte Bildgenerierung im Chat, inkl. Variations-Workflow.
- **Advanced Data Analysis** — Python-Code-Ausführung, CSV-/Excel-Auswertung, Charts.
- **Memory** erinnert sich über Sessions hinweg an Präferenzen (opt-in).
- **OpenAI-API** mit Function Calling, Assistants, Responses, Structured Outputs.""",

'claude': """- **Kontextfenster 200 000 Tokens** (ca. 500 Buchseiten) — führend bei langen Dokumenten.
- **Artifacts** rendern Code, HTML, SVG, Diagramme in einem Seitenpanel — live editierbar.
- **Projects** bündeln Dateien, Anweisungen und Chats zu einem persistenten Arbeitsraum.
- **Computer Use (API)** — Claude kann den Desktop/Browser steuern (Beta).
- **Code-Qualität auf dem Niveau spezialisierter IDEs** (starker SWE-Bench-Score).
- **Constitutional AI**: nuancierte Sicherheitsprinzipien statt plumper Filter.
- **API in EU-Region** (Bedrock & Google Vertex), Enterprise-Plan mit DPA.""",

'gemini': """- **Bis zu 2 Mio. Token Kontext** (Gemini 2.5 Pro) — unübertroffen bei sehr langen Inputs.
- **Tiefe Integration** in Gmail, Docs, Sheets, Meet, Drive, Calendar.
- **Multimodal nativ** — Text, Bild, Audio, Video, Code im selben Call.
- **Deep Research**: Agent, der über Minuten eigenständig Quellen zusammenträgt.
- **Gems** — persönliche, wiederverwendbare Assistenten (Pendant zu Custom GPTs).
- **Veo 3** (Video) und **Imagen 4** (Bild) direkt im selben Interface.
- **Vertex AI** für Enterprise-Einsatz mit Datenresidenz in der EU.""",

'mistral': """- **Le Chat Pro** mit Zugriff auf Mistral Large und Codestral.
- **Web-Suche und Code-Interpreter** für aktuelle Recherchen & Analysen.
- **Open-Weights-Modelle** (Mixtral, Mistral 7B, Codestral) — selbst hostbar.
- **EU-Datenresidenz** — Server in Frankreich, DPA Standard.
- **Sehr hohe Inferenz-Geschwindigkeit** dank optimierter Serving-Stack.
- **Mistral API** mit Function Calling, JSON-Mode, Embeddings.
- **Canvas** für strukturiertes Arbeiten an längeren Texten.""",

'midjourney': """- **V7** mit deutlich verbesserter Kohärenz und Typografie.
- **Style References (`--sref`)** — einheitlicher visueller Look über Bilder hinweg.
- **Character Reference (`--cref`)** — Charakter-Konsistenz zwischen Szenen.
- **Image-to-Image** und **Upscaling** bis zu hohen Auflösungen.
- **Niji** — dediziertes Modell für Anime- und Illustrationsstile.
- **Moodboards & Collections** zum Sammeln und Wiederverwenden.
- **Video-Modus (V1)** — Animation eines Standbilds.""",

'stable-diffusion': """- **Stable Diffusion 3.5 & Stable Image Ultra** — neueste Basismodelle.
- **Komplett Open Weights** — lokal, on-premise oder Cloud nach Wahl.
- **LoRA-Feintuning** für eigene Stile/Charaktere mit wenigen Beispielbildern.
- **ControlNet** — präzise Komposition via Posen, Tiefenkarten, Skeletten.
- **Stability API** als managed Option (Credit-Modell).
- **Riesiges Ökosystem** (ComfyUI, Automatic1111, Civitai, Hugging Face).
- **Stable Video Diffusion** für kurze Clip-Generierung.""",

'elevenlabs': """- **Instant Voice Clone** aus 30–60 Sek. Audiomaterial.
- **Professional Voice Clone** für Studio-Qualität (Opt-in mit Verifizierung).
- **32+ Sprachen**, die die Originalstimme beibehalten (Multilingual v2).
- **Emotions- und Stil-Steuerung** via Stability/Similarity-Regler.
- **Dubbing Studio** — Video-Lokalisierung mit Lip-Sync-Alignment.
- **Voice Library** mit kuratierten Stimmen inkl. kommerzieller Nutzung.
- **API** mit extrem niedriger Latenz für Echtzeit-Anwendungen.""",

'runway': """- **Gen-4** — Text-zu-Video und Bild-zu-Video mit verbesserter Kohärenz.
- **Motion Brush** — definiere per Pinsel, welche Bildteile sich bewegen.
- **Camera Control** — Kamerabewegungen (Pan, Zoom, Truck) steuern.
- **Lip-Sync** für vertonte Charakter-Videos.
- **Act-One** überträgt Mimik/Performance vom Video auf Avatare.
- **Inpainting & Green-Screen** direkt im Browser-Editor.
- **Workflows** als Node-Editor für wiederholbare Pipelines.""",

'cursor': """- **Tab-Autocomplete** mit Multi-Line-Edit-Prediction (das Killer-Feature).
- **Composer / Agent** — plant und schreibt Multi-File-Änderungen ganzer Features.
- **Codebase-weite Suche & Kontext** via embeddings.
- **Background Agent** — Tasks laufen in paralleler Umgebung, Pull-Request am Ende.
- **Model-Routing** zwischen Claude, GPT-5, Gemini automatisch oder manuell.
- **MDC Rules** — Projekt-spezifische Regeln für konsistenten Stil.
- **Volle VS-Code-Kompatibilität** (Extensions, Settings, Keybindings).""",

'copilot': """- **GitHub Copilot Chat** in IDE, GitHub.com, CLI und Mobile.
- **Copilot Agent / Workspace** — selbstständiges Bearbeiten ganzer Issues.
- **Code Review** direkt im Pull-Request mit Vorschlägen.
- **Copilot Spaces** für Team-spezifisches Wissen & Regeln.
- **Multi-Modell-Auswahl** (GPT-5, Claude, Gemini) je nach Aufgabe.
- **Enterprise Data Controls** — Indexierung privater Repos mit Governance.
- **Nahtlos in alle großen IDEs** (VS Code, JetBrains, Neovim, Xcode, Visual Studio).""",

'notion-ai': """- **Q&A über den gesamten Workspace** mit Quellenverweisen auf Originalseiten.
- **Summarize & Translate** in jeder Seite oder Datenbank-Zeile.
- **Meeting-Notizen** aus Audioaufnahmen (Notion AI Meeting Notes).
- **Autofill** für Datenbank-Properties (z. B. Zusammenfassung, Priorität).
- **AI Connectors** zu Slack, Google Drive, GitHub — als integrierte Wissensquellen.
- **Writing-Assistenten** (Ton, Länge, Grammatik, Übersetzung) im Editor.
- **Enterprise Search** kombiniert Notion + verbundene Quellen.""",

'perplexity': """- **Jede Antwort mit nummerierten Quellen** — direktes Prüfen via Klick.
- **Pro Search**: mehrstufige Rechercheketten mit Follow-up-Fragen.
- **Deep Research** — tiefergehende Berichte über Minuten.
- **Spaces** bündeln Recherchen zu einem Thema; teambereich-fähig.
- **Labs** — strukturierte Outputs (Tabellen, Code, kleine Apps).
- **Datei- und PDF-Upload** für Analysen auf eigenen Dokumenten.
- **Comet Browser** (Beta) — integriert Perplexity als Browser-Companion.""",

'deepl-write': """- **Stilanpassung**: formell, freundschaftlich, sachlich, überzeugend.
- **Ton-Abstimmung** mit einem Klick — Wortwahl und Satzbau bleiben intakt.
- **Umformulierungs-Vorschläge** pro Satz, nicht nur pro Absatz.
- **Grammatik-, Komma-, Rechtschreib-Korrekturen** mit Erklärung.
- **Deutsch & Englisch** in beiden Varianten (US/UK, DE/AT/CH).
- **DeepL Pro Write** für Browser, Desktop, Word-Add-in.
- **DSGVO-konform**: EU-Server, keine Datenverwendung für Training.""",

'aleph-alpha': """- **Pharia-1-LLM** auf EU-Hardware trainiert und betrieben.
- **Self-Hosting** in eigener Infrastruktur oder souveräner Cloud.
- **Explainability** — Attributions zeigen Trainingsquellen pro Antwort.
- **Multimodale Funktionen** (Text, Bild) für Industrie-Use-Cases.
- **Pharia Assistant** als Basis für eigene Enterprise-Agenten.
- **Pharia Studio** für Prompt-Entwicklung und Feintuning.
- **BSI-C5-Audit**, DSGVO-konform, BDBOS-Referenzprojekte.""",
}

PRICING = {
'chatgpt': """- **Free** — Zugriff auf GPT-5 mit reduzierten Limits.
- **Plus** · $20 / Monat — volle GPT-5-Nutzung, bevorzugte Verfügbarkeit, Image-Gen, Data Analysis.
- **Pro** · $200 / Monat — unbegrenzt GPT-5, o3-pro, längere Antworten.
- **Team** · ab $25 / Nutzer / Monat — gemeinsamer Workspace, erweiterte Admin-Kontrollen.
- **Enterprise** · Preis auf Anfrage — SSO, DPA, EU-Datenresidenz, erweiterte Compliance.
- **API** — Pay-as-you-go, aktuell GPT-5 ab $1,25 / 1 M Input-Token, $10 / 1 M Output.""",

'claude': """- **Free** — begrenzte Nutzung von Claude 3.7 Sonnet.
- **Pro** · $20 / Monat — Claude 4.x, Projects, Artifacts, 5× mehr Nutzung als Free.
- **Max** · $100 / Monat — deutlich höhere Nutzungs-Limits, Priority-Access.
- **Team** · $30 / Nutzer / Monat (min. 5) — Admin-Panel, zentrale Rechnung.
- **Enterprise** · Preis auf Anfrage — SSO, Audit-Logs, DPA, Customer-Managed Keys.
- **API** — Claude 4 Sonnet $3/$15 pro 1 M Token (Input/Output), Opus höher.""",

'gemini': """- **Free** — Gemini 2.0 Flash, begrenzter Zugang zu Pro.
- **Google AI Pro** · €21,99 / Monat — Gemini 2.5 Pro, Deep Research, 2 TB Speicher.
- **Google AI Ultra** · €274,99 / Monat — höchste Limits, neueste Modelle, Flow & Whisk.
- **Workspace Business Starter** · €6 / Nutzer — Gemini in Gmail, Docs etc.
- **Vertex AI** — Pay-as-you-go mit Gemini 2.5 Pro ab $1,25 / 1 M Input-Token.""",

'mistral': """- **Free** — kostenlose Nutzung von Le Chat mit Standard-Modellen.
- **Pro** · €14,99 / Monat — Mistral Large 2, Web-Suche, Code-Interpreter, Bildgenerierung.
- **Team** · €24,99 / Nutzer / Monat — kollaborative Spaces, Admin-Tools.
- **Enterprise** · auf Anfrage — On-Prem- oder Private-Cloud-Deployment.
- **API (La Plateforme)** — Mistral Large 2 ab €2 / 1 M Input, €6 / 1 M Output.
- **Open-Source** — Mixtral/Mistral 7B/Codestral kostenlos unter Apache 2.0 nutzbar.""",

'midjourney': """- **Basic** · $10 / Monat — ~200 Bilder, Mitgliederbereich.
- **Standard** · $30 / Monat — 15 Stunden Fast-GPU + unlimited Relax-Modus.
- **Pro** · $60 / Monat — 30 Stunden Fast-GPU, Stealth-Modus (private Generationen).
- **Mega** · $120 / Monat — 60 Stunden Fast-GPU, für intensive Produktion.
- Jahresabos mit ~20 % Rabatt. Keine öffentliche API.""",

'stable-diffusion': """- **Open-Source** — Modelle kostenlos unter Stability-Community-License auf Hugging Face.
- **Stability API** — Credits ab $10 für ~350 Bilder (SD 3.5 Large).
- **DreamStudio Web** · Pay-per-use, ähnliche Credit-Preise.
- **Stability for Enterprise** · Preis auf Anfrage — kommerzielle Lizenzen, Support, Self-Hosting.
- **Lokaler Betrieb** — kostenlos, benötigt NVIDIA-GPU ab 6 GB VRAM (für SD 3.5: 12 GB+).""",

'elevenlabs': """- **Free** — 10 000 Zeichen / Monat, 3 Custom Voices.
- **Starter** · $5 / Monat — 30 000 Zeichen, 10 Voices, kommerzielle Nutzung.
- **Creator** · $22 / Monat — 100 000 Zeichen, Professional Voice Clone.
- **Pro** · $99 / Monat — 500 000 Zeichen, höchste Audio-Qualität.
- **Scale** · $330 / Monat — 2 M Zeichen, 5 Seats, Usage-Analytics.
- **Business / Enterprise** · auf Anfrage — höheres Volumen, Zero-Retention, HIPAA/SOC 2.""",

'runway': """- **Free** · 125 Credits einmalig zum Ausprobieren.
- **Standard** · $15 / Monat — 625 Credits / Monat, Gen-3-Video bis 10 Sek.
- **Pro** · $35 / Monat — 2 250 Credits, unlimited Relax-Modus, 4K-Upscale.
- **Unlimited** · $95 / Monat — unlimited Gen-3 Alpha Turbo, für Profis.
- **Enterprise** · auf Anfrage — Custom-Models, SSO, dedizierte Kapazität.""",

'cursor': """- **Hobby** · Free — 2 Wochen Pro-Trial, dann begrenzter Slow-Modus.
- **Pro** · $20 / Monat — 500 Fast-Requests pro Monat, unlimited Slow.
- **Pro+** · $60 / Monat — deutlich mehr Fast-Requests für Power-User.
- **Business** · $40 / Nutzer / Monat — Team-Admin, Privacy-Mode zentral erzwingbar.
- **Enterprise** · auf Anfrage — SSO, erweiterte Security-Controls.""",

'copilot': """- **Free** — 2 000 Code-Completions + 50 Chat-Messages / Monat.
- **Pro** · $10 / Monat — unlimited Completions + Chat, Premium-Modelle nutzbar.
- **Pro+** · $39 / Monat — volle Premium-Modell-Nutzung, Spark, Coding Agent.
- **Business** · $19 / Nutzer — Team-Setup, Policy-Management.
- **Enterprise** · $39 / Nutzer — Codebase-Indexing, Knowledge-Bases, SSO, Audit-Logs.""",

'notion-ai': """- **Notion AI** ist inklusive in:
  - **Plus** · $12 / Nutzer / Monat (jährlich)
  - **Business** · $24 / Nutzer / Monat (jährlich)
  - **Enterprise** · auf Anfrage
- **Notion AI Add-on** (für Teams ohne Plus/Business): $10 / Nutzer / Monat.
- **Free Personal** enthält ein limitiertes AI-Kontingent zum Ausprobieren.
- **Enterprise-Funktionen**: Connectors zu Slack/Drive/GitHub/Jira inklusive.""",

'perplexity': """- **Free** — 5 Pro-Searches / Tag, Standard-Modelle.
- **Pro** · $20 / Monat — 600+ Pro-Searches / Tag, Wahl zwischen GPT-5, Claude 4, Gemini 2.5 Pro etc.
- **Enterprise Pro** · $40 / Nutzer / Monat — Team-Features, SSO, erhöhte Limits.
- **Max** · $200 / Monat — höchste Limits, früher Zugriff auf neue Features, Labs-Zugang.
- **API (Sonar)** — Pay-per-use, ab ca. $1 / 1 000 Requests für Sonar-Small.""",

'deepl-write': """- **Starter (Free)** — begrenzte Nutzung zum Ausprobieren.
- **Pro Starter** · €7,49 / Monat — unbegrenztes Schreiben, Ton-/Stil-Optionen.
- **Pro Advanced** · €22,49 / Monat — zusätzlich Glossare, erweitertes Stil-Matching.
- **Pro Ultimate** · €44,99 / Monat — Enterprise-Features, Support, Team-Dashboard.
- **DeepL API Pro** — mengenbasiert, EU-Server, DPA Standard.""",

'aleph-alpha': """- **Cloud API** — Enterprise-Pricing, keine Pay-as-you-go für Endkunden.
- **Self-Hosted** — Lizenz pro Modell und Hardware, typisch sechsstellige Einstiegskosten.
- **Pharia Studio / Assistant** — im Enterprise-Paket enthalten.
- **Public Sector Track** — Referenzprojekte mit Bundes- und Länderbehörden.
- Projekte starten typisch bei 10–50 k€ Onboarding plus laufende Lizenz-/Betriebs-Kosten.
- Kontakt für Pilot- und PoC-Angebote direkt über das Aleph-Alpha-Sales-Team.""",
}

# ---- 3. Fetch tool elements and patch each ----
items, page = [], 1
while True:
    r = requests.get(f'{BASE}/{SITE}/elements/?type_id={tool_ct["id"]}&size=200&page={page}',
        headers=H, verify=False).json()
    items += r.get('items', [])
    if not r.get('has_next'): break
    page += 1
print(f'  · {len(items)} tools to update')

for el in items:
    d = el['data']
    slug = d.get('slug')
    features = FEATURES.get(slug)
    pricing = PRICING.get(slug)
    if not features or not pricing:
        print(f'  ⚠️  {slug}: no content mapped')
        continue
    new_data = {**d, 'features': features, 'pricing': pricing}
    r = requests.patch(f'{BASE}/{SITE}/elements/{el["id"]}',
        json={'data': new_data}, headers=H, verify=False)
    if r.ok:
        print(f'  ✓ {slug}: features ({len(features)} chars) + pricing ({len(pricing)} chars)')
    else:
        print(f'  ✗ {slug}: {r.status_code} {r.text[:200]}')

print('\n✓ Done.')
