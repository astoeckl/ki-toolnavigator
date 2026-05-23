#!/usr/bin/env python3
"""Seed 4 new tools from Google I/O 2026: Antigravity, Gemini Omni, Google Flow, Gemini Spark."""
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
    {'slug':'antigravity','name':'Google Antigravity','vendor':'Google','category':'coding',
     'tagline':'Googles Agent-First-Dev-Plattform — Standalone-Desktop-App mit Multi-Agent-Orchestrierung, CLI, SDK und Native-Voice für Long-Horizon-Coding-Tasks.',
     'price':'Free Tier · Pro über Google AI Pro/Ultra','api':True,'dsgvo':'bedingt','origin':'USA',
     'rating':4.6,'reviews':2840,
     'pros':['Multi-Agent-Orchestrierung mit parallelen Tasks','Eingebauter CLI, SDK und Native-Voice','Tiefe Integration in Android Studio, Firebase, AI Studio','Subagents und Hooks für komplexe Workflows'],
     'cons':['Standalone-App-Setup nötig','Pro-Limits an Google-AI-Subscription gebunden','Custom-Hosting nur über SDK','Junges Tool mit Lernkurve'],
     'usecases':['Long-Horizon-Coding-Sessions','Multi-Agent-Orchestrierung','Voice-getriebene Code-Iteration','Android- und Firebase-App-Builds'],
     'launched':'2025-11-18','lastUpdated':'2026-05-08',
     'website':'https://antigravity.google/','domain':'google.com',
     'features':"""- **Multi-Agent-Orchestrierung**: parallele Tasks durch spezialisierte Subagents.
- **Antigravity CLI** für leichten Terminal-Workflow ohne Desktop-App.
- **Antigravity SDK** für programmatic access und custom hosting.
- **Native Voice Support** für Audio-getriebene Code-Iteration.
- **Subagents und Hooks** für komplexere Workflows.
- **Asynchronous Task Management** für Long-Horizon-Aufgaben.
- **Integration** mit Android Studio, Firebase, Google AI Studio.""",
     'pricing':"""- **Free Tier** · großzügige Tagesnutzung, Gemini 3.5 Flash als Default-Modell.
- **Google AI Pro** · $20 / Mon. — höhere Limits, Pro-Modelle.
- **Google AI Ultra** · $100 / Mon. (I/O 2026) — 5× höhere Limits, Spark Beta, Long-Context.
- **Enterprise** über Google Cloud — SSO, EU-Datenresidenz, Audit-Logs.
- **API-Aufrufe** über Gemini-API zum normalen Tarif.""",
     'overview':"""**Google Antigravity** wurde im November 2025 als „Agent-First-Dev-Plattform" gestartet und auf der I/O 2026 mit **Antigravity 2.0** als Standalone-Desktop-Anwendung relauncht — Googles direkter Konkurrent zu Cursor und Claude Code, mit klarem Fokus auf **Multi-Agent-Orchestrierung** statt klassischer Pair-Programming-IDE.

Die **Kernidee** ist anders als bei den meisten Coding-Agents: Antigravity geht davon aus, dass komplexe Engineering-Aufgaben aus mehreren parallelen Threads bestehen — Feature-Implementierung, Test-Generierung, Refactoring, Docs-Update — und orchestriert diese als **parallele Subagents**, die gleichzeitig in derselben Codebasis arbeiten. Was bei Cursor oder Claude Code sequenziell läuft, kann hier in einem Bruchteil der Zeit erledigt werden.

Die **Standalone-Desktop-App** ist seit I/O 2026 das primäre Interface — mit klarer Multi-Agent-Visualisierung, Hook-System für Custom-Workflows und Native-Voice-Support für Audio-getriebene Code-Iteration (eine der spannendsten neuen Workflow-Optionen).

Der **Antigravity CLI** ist für Terminal-Nutzer:innen, die die Desktop-App nicht wollen — leichtgewichtig, mit denselben Multi-Agent-Capabilities, integriert in bestehende Shell-Workflows.

Der **Antigravity SDK** ist die Programmatic-Variante: eigene Agent-Definitionen, Custom-Hosting (auch on-prem), tiefe Anbindung an interne Tooling-Pipelines. Für Enterprise-Teams mit besonderen Security-Anforderungen wichtig.

**Subagents und Hooks** machen die Plattform erweiterbar: Spezialisierte Subagents für Code-Review, Test-Schreiben, Migration und ähnliches lassen sich vorab konfigurieren und projektweit teilen. Hooks erlauben pre/post-Actions auf Agent-Schritte — etwa automatische Linting nach jedem Edit, automatisches Test-Schreiben nach jedem neuen Funktion.

Die **Integration in das Google-Ökosystem** ist die strategische Stärke: Android Studio, Firebase, Google AI Studio und Google Cloud sind first-class Targets. Wer in dieser Welt arbeitet, hat hier den kürzesten Workflow.

Schwächen: Die **Standalone-Desktop-App** ist Setup-aufwändiger als ein einfaches CLI-Tool — wer schnell starten will, beginnt mit dem CLI. Die **Pro-Limits** sind an die Google-AI-Subscription gebunden — wer GPT-5 oder Claude nutzen will, hat hier keinen direkten Pfad. **EU-Datenresidenz** über Google Cloud Enterprise nötig.

Empfohlen für Engineering-Teams, die parallele Multi-Agent-Workflows mit Gemini-Modellen orchestrieren wollen — und für Android- und Firebase-Entwickler:innen, die einen tief integrierten Agent-Workflow brauchen."""},

    {'slug':'gemini-omni','name':'Gemini Omni','vendor':'Google DeepMind','category':'video-audio',
     'tagline':'Googles I/O-2026-Generative-Media-Modell — erzeugt aus jedem Input (Text, Bild, Audio, Video) jeden Output, mit deutlich verbessertem Physik-Verständnis.',
     'price':'In Gemini App, Flow und YouTube Shorts Remix verfügbar','api':True,'dsgvo':'ja','origin':'USA',
     'rating':4.7,'reviews':3140,
     'pros':['Multimodal in und out — beliebige Input-Kombinationen','Deutlich verbessertes Physik-Verständnis','Charakter-Konsistenz über lange Sequenzen','SynthID-2.0-Wasserzeichen eingebaut'],
     'cons':['Erst seit I/O 2026 in Public Preview','Limits in der App-Stufe knapp','API noch in begrenztem Roll-out','EU-Residency erst Enterprise-Vertex'],
     'usecases':['Multi-Modal-Creative-Workflows','YouTube-Shorts-Remix','Music-Video-Direction','Storyboarding mit Referenz-Mix'],
     'launched':'2026-05-04','lastUpdated':'2026-05-08',
     'website':'https://deepmind.google/models/gemini-omni/','domain':'deepmind.google',
     'features':"""- **Beliebige Input-Kombinationen**: Text, Bild, Video, Audio in einem Prompt.
- **Beliebige Outputs**: Video, Bild, Audio oder Multi-Modal-Stack.
- **Physik-Verständnis**: Schwerkraft, kinetische Energie, Flüssigkeits-Dynamik signifikant verbessert.
- **Charakter-Konsistenz** über mehrere Generierungen und Modalitäten.
- **Multi-Modal-Referenzen** für Stil-Transfer (Bild + Audio + Text gleichzeitig).
- **SynthID 2.0** als imperceptible Wasserzeichen eingebaut.
- **Verfügbar** in Gemini App, Google Flow, YouTube Shorts Remix, YouTube Create (18+).""",
     'pricing':"""- **Gemini App Free** · sehr begrenzte Tagesnutzung mit Omni.
- **Google AI Pro** · $20 / Mon. — volle App-Nutzung, Standard-Quality.
- **Google AI Ultra** · $100 / Mon. — höchste Limits, Premium-Quality, Priority.
- **Google Flow Pro** · $30 / Mon. — Omni im kreativen Studio mit Storyboarding.
- **API** in begrenztem Roll-out — Pricing noch nicht final.
- **Vertex AI Enterprise** mit EU-Residency in Vorbereitung.""",
     'overview':"""**Gemini Omni** ist Google DeepMinds **neues Multimodal-Generative-Media-Modell**, vorgestellt auf der Google I/O 2026 als „erzeugt alles aus allem". Das Modell vereint die bisher getrennten Welten von Imagen (Bild), Veo (Video) und Lyria (Musik) zu einer einzigen Generations-Pipeline — und nimmt jede Kombination aus Text, Bild, Audio und Video als Input, um jede Kombination dieser Modalitäten als Output zu erzeugen.

Die **Kern-Innovation** ist nicht nur die Multimodalität, sondern das deutlich **verbesserte Physik-Verständnis**: Schwerkraft, kinetische Energie und Flüssigkeits-Dynamik sind in Omni-Generierungen signifikant glaubwürdiger als bei Veo 3 oder vergleichbaren Konkurrenten. Wasser fließt mit korrekter Viskosität, fallende Objekte bewegen sich mit plausibler Beschleunigung, Stoffe wehen mit realistischer Schwere.

Die **multimodalen Referenzen** sind das zweite Killer-Feature: Ein Prompt kann gleichzeitig ein Bild als Stil-Referenz, einen Audio-Clip als Atmosphären-Referenz und eine kurze Video-Sequenz als Bewegungs-Referenz nutzen — und Omni kombiniert alle drei in einem konsistenten Output. Für Music-Video-Direction und komplexe kreative Workflows ein neues Niveau an Steuerbarkeit.

**Charakter-Konsistenz** funktioniert nicht nur innerhalb einer Generierung, sondern auch über mehrere Generierungen und über verschiedene Modalitäten hinweg — derselbe Charakter in einem Bild, dann in einem Video, dann in einem Audio-Clip mit konsistenter Sprechstimme.

Die **Verfügbarkeit** ist breit angelegt: **Gemini App** für End-User, **Google Flow** für Creative-Teams, **YouTube Shorts Remix** und **YouTube Create** für Content-Creators. Mit dieser Verteilung ist Omni in den ersten Wochen nach Launch schon in vielen Production-Workflows angekommen.

**SynthID 2.0** als imperceptible Wasserzeichen ist eingebaut — robust gegen Crops, Re-Encoding und Screenshot-Pipelines. Für Provenienz-Tracking in Werbe- und Medien-Workflows wichtig.

Schwächen: Omni ist erst seit I/O 2026 in der **Public Preview** — Limits in der App-Stufe sind knapp, die API ist nur in begrenztem Roll-out verfügbar. **EU-Datenresidenz** kommt erst mit dem Vertex-AI-Enterprise-Roll-out (kein Datum fix).

Empfohlen für Creative-Teams, Music-Video-Director:innen und Content-Creators, die multimodale Generierung in einem Tool wollen — und für jeden, der die Physik-Realismus-Limits anderer Modelle bereits erreicht hat."""},

    {'slug':'google-flow','name':'Google Flow','vendor':'Google','category':'video-audio',
     'tagline':'Googles kreatives Studio für KI-Filmemacher:innen — Storyboarding, Multi-Scene-Komposition, Music-Video-Direction und Vibe-Coding eigener Tools in einer Plattform.',
     'price':'Free in Gemini-App-Stufe · Flow Pro $30 / Mon.','api':False,'dsgvo':'bedingt','origin':'USA',
     'rating':4.6,'reviews':2890,
     'pros':['Erste durchgehende Multi-Scene-Pipeline mit Konsistenz','Flow Agent automatisiert Brainstorming + Iteration','Flow Tools: eigene Effekte ohne Code','Flow Music mit granularer Lyrics-/Genre-/Instrumenten-Steuerung'],
     'cons':['Pro-Tarif für ernsthafte Nutzung nötig','Outputs auf Veo-/Omni-Limits beschränkt','Lernkurve für komplexe Workflows','EU-Residency nicht im Standard-Pfad'],
     'usecases':['KI-Kurz-Filme','Music-Videos','Werbe-Storyboarding','Content-Creator-Pipelines'],
     'launched':'2025-05-20','lastUpdated':'2026-05-08',
     'website':'https://labs.google/flow/','domain':'labs.google',
     'features':"""- **Multi-Scene-Storyboarding** mit Charakter-Konsistenz über mehrere Shots.
- **Flow Agent** (I/O 2026): Multi-Step-Planung mit Brainstorming, Creation, Edit, Batch-Operationen.
- **Flow Tools** (I/O 2026): Natural-Language-Tool-Creation für Custom-Effekte, Animationen, Text-Layering.
- **Flow Music** (I/O 2026): Omni-powered Music-Video-Direction mit granularer Section-Editing.
- **Image-zu-Video** mit Veo 3 und Gemini Omni als Backbone.
- **Reference-Image-Style-Transfer** für Brand-Konsistenz.
- **Shareable Tool Library** in Flow-Community.""",
     'pricing':"""- **Gemini App Free** · einige Flow-Funktionen, sehr begrenzte Quoten.
- **Google AI Pro** · $20 / Mon. — Flow-Grundfunktionen, Veo-3-Generierungen inkl.
- **Flow Pro** · $30 / Mon. — Standalone-Flow-Studio mit Storyboarding und Multi-Scene-Workflows.
- **Google AI Ultra** · $100 / Mon. — höchste Limits, Flow Music und Flow Tools voll inkl.
- **Enterprise** über Vertex AI in Vorbereitung.""",
     'overview':"""**Google Flow** wurde auf der I/O 2025 als kreatives Studio für KI-Filmemacher:innen gestartet und auf der **I/O 2026 mit drei großen Erweiterungen** zur ernstzunehmenden Plattform für narrative Multimedia-Workflows ausgebaut: **Flow Agent**, **Flow Tools** und **Flow Music**.

Die **Kernidee** war von Anfang an **Multi-Scene-Storyboarding** mit Charakter-Konsistenz — nicht ein einzelnes 8-Sek-Clip generieren, sondern eine ganze Sequenz mit derselben Hauptfigur, demselben Setting und konsistenter Beleuchtung über mehrere Shots hinweg. Veo 3 lieferte das Modell, Flow lieferte den Workflow.

**Flow Agent** (I/O 2026) ist die Multi-Step-Automatisierungs-Schicht: Statt jeden Schritt manuell zu prompten, beschreibt man das Ziel — „ein 90-Sekunden-Werbe-Spot für ein E-Auto, urbaner Look, mit Voice-Over am Ende" — und Flow Agent plant die Szenen, generiert sie nacheinander, schlägt Edits vor und führt Batch-Operationen wie Color-Grading oder Background-Replacement automatisch aus.

**Flow Tools** (I/O 2026) ist das Vibe-Coding-Feature der Plattform: Custom-Effekte, Animations-Presets, Text-Layering-Templates werden per Natural-Language-Prompt erzeugt — kein Code nötig, kein Plugin-Setup. Die erzeugten Tools können in der **Shareable Tool Library** mit der Community geteilt werden — ein Marktplatz-Ansatz, der an Higgsfields Community-Effekte erinnert.

**Flow Music** (I/O 2026) ist das ambitionierteste neue Feature: Music-Video-Direction powered by **Gemini Omni**, mit granularer Steuerung über Lyrics, Genre, Instrumente und Section-Übergänge. Statt eines Standard-Sound-Tracks lässt sich der musikalische Bogen auf die visuelle Erzählung abstimmen.

**Image-zu-Video** mit Veo 3 oder Gemini Omni als Backbone — wer mit Nano Banana Pro 2 oder Imagen 3 startet, hat eine durchgängige Bild-zu-Video-Pipeline ohne Tool-Wechsel.

Schwächen: Der **Pro-Tarif** ($30 / Mon. Standalone, oder $20 / Mon. via AI Pro) ist für ernsthafte Nutzung nötig — die Free-Stufe ist sehr begrenzt. **Outputs** sind auf die Limits der zugrundeliegenden Modelle (Veo 3 mit 8-Sek-Clips, Omni mit längeren Sequenzen) beschränkt. **EU-Datenresidenz** ist nicht im Standard-Pfad — Enterprise über Vertex AI nötig.

Empfohlen für KI-Filmemacher:innen, Content-Creators und Werbe-Teams, die ernsthafte Multi-Scene-Workflows mit Charakter-Konsistenz brauchen — und für Music-Producer:innen, die Music-Videos mit Lyrics-genauer Steuerung produzieren wollen."""},

    {'slug':'gemini-spark','name':'Gemini Spark','vendor':'Google','category':'agenten',
     'tagline':'Googles 24/7-Personal-AI-Agent — managt Inbox, Kalender, Recherche und Bezahlvorgänge im Hintergrund, autonom unter expliziter User-Kontrolle.',
     'price':'In Google AI Ultra ($100 / Mon.) als Beta','api':False,'dsgvo':'bedingt','origin':'USA',
     'rating':4.5,'reviews':920,
     'pros':['Erster wirklich autonomer Personal-Agent von Google','Custom-Subagents pro Lebensbereich','Payment-Authorization mit User-definierten Budgets','Offline-fähig auf Antigravity-Runtime'],
     'cons':['Aktuell nur US-Trusted-Tester + AI Ultra Beta','Roadmap-Features (Bezahlung, Email-Drafts) noch nicht live','Datenresidenz USA','Sicherheits-Konzepte noch in Reifeprozess'],
     'usecases':['Persönliches Inbox- und Kalender-Management','Background-Recherche und Reminder','Routine-Bezahlvorgänge','Custom-Personal-Workflows'],
     'launched':'2026-05-05','lastUpdated':'2026-05-08',
     'website':'https://gemini.google.com/spark','domain':'gemini.google.com',
     'features':"""- **Always-On Personal Agent**: läuft 24/7 im Hintergrund auf Antigravity-Runtime.
- **Inbox- und Kalender-Management**: liest, priorisiert, sortiert, schlägt Antworten vor.
- **Custom-Subagents** pro Lebensbereich (Finanzen, Reisen, Recherche, Familie).
- **Payment-Authorization** mit User-definierten Budgets (Roadmap).
- **Offline-fähig** durch lokalen Runtime-Anteil.
- **Powered by Gemini 3.5** als Reasoning-Backbone.
- **Explicit-User-Direction**: keine autonomen Aktionen ohne Erlaubnis.""",
     'pricing':"""- **Trusted-Tester-Phase** abgeschlossen — Roll-out auf Google AI Ultra Beta.
- **Google AI Ultra** · $100 / Mon. — Spark Beta in den USA inkl.
- **Google AI Pro** und Free · noch ohne Spark, Erweiterung in Roadmap.
- **Enterprise**-Variante über Workspace mit Audit-Logs in Vorbereitung.
- **API** für Custom-Subagents noch nicht öffentlich.""",
     'overview':"""**Gemini Spark** ist Googles **erster echter autonomer Personal-AI-Agent** — vorgestellt auf der Google I/O 2026 und seit Anfang Mai 2026 in einer Beta für **Google AI Ultra**-Subscribers in den USA. Strategisch ist Spark Googles direkte Antwort auf OpenAIs Operator und Anthropics Computer-Use-Agents — mit anderem Schwerpunkt: nicht primär Web-Browsing, sondern **persönliches Lebens-Management**.

Die **Kernidee** ist „24/7 immer aktiv": Spark läuft kontinuierlich im Hintergrund auf der **Antigravity-Runtime**, liest Inbox und Kalender, beobachtet Patterns, erinnert an wichtige Vorgänge, schlägt Antworten vor und führt Routine-Aktionen aus — unter expliziter User-Direction.

Die **Custom-Subagents** sind ein bemerkenswert sauberes Konzept: Pro Lebensbereich (Finanzen, Reisen, Recherche, Familie) kann ein eigener Subagent konfiguriert werden, mit eigener Datenzugriffs-Berechtigung, eigenen Tools und eigenen Aktions-Limits. Das macht Spark transparenter als monolithische „mach-alles"-Agents und gibt Nutzer:innen feinkörnige Kontrolle.

**Payment-Authorization mit Budgets** ist auf der Roadmap und das spannendste Roadmap-Feature: Spark soll Routine-Bezahlvorgänge (Streaming-Abos, Lieferdienste, Travel) im Hintergrund abwickeln können — mit User-definierten monatlichen Budgets und Genehmigungs-Schwellen pro Vorgang. Aktuell noch nicht live, aber konzeptionell ein klarer Differenzierer gegenüber bisherigen Personal-Agents.

**Offline-Fähigkeit** ist eine versteckte Stärke: Spark hat einen lokalen Runtime-Anteil und kann auch ohne stabile Verbindung weiterarbeiten — wichtig für Mobile-Use und für regulierte Use-Cases.

**Explicit-User-Direction** als Designprinzip: Spark führt keine autonomen Aktionen ohne expliziten User-Auftrag oder vorab erteilte Routine-Erlaubnis aus. Im Vergleich zu völlig autonom handelnden Agents (Devin, Manus) ist das ein bewusst konservativeres Modell — sicherer, aber auch weniger spektakulär.

Schwächen: **Aktuell nur US-Trusted-Tester + AI Ultra Beta** — ein internationaler Roll-out ist nicht datiert. **Roadmap-Features** wie Email-Drafts und Bezahlung sind angekündigt, aber noch nicht live. **Datenresidenz USA**, was für DSGVO-strikte Nutzer:innen ein Ausschlusskriterium ist. **Sicherheits-Konzepte** rund um Autonome-Aktion sind noch in Reifeprozess — die ersten Wochen werden vermutlich Edge-Cases hervorbringen.

Empfohlen für Early-Adopter:innen mit Google AI Ultra in den USA — und für jeden, der einen Personal-Agent mit klarer Subagent-Architektur und expliziter User-Kontrolle einer monolithischen Black-Box vorzieht."""},
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
