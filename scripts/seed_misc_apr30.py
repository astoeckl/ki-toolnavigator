#!/usr/bin/env python3
"""Seed 4 mixed tools (Lovable, Google Stitch, Miro AI, Microsoft Designer) end-to-end."""
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
    {'slug':'lovable','name':'Lovable','vendor':'Lovable','category':'coding',
     'tagline':'AI-Full-Stack-App-Builder im Browser — vom Prompt zur deploybaren React/Tailwind/Supabase-App in Minuten, mit GitHub-Sync.',
     'price':'Free (5 Credits/Tag) · Pro ab $25 / Mon.','api':False,'dsgvo':'bedingt','origin':'Schweden',
     'rating':4.6,'reviews':3210,
     'pros':['Native Supabase- und Stripe-Integration','GitHub-Sync mit echtem Repo','Multiplayer für Team-Workspaces','EU-Anbieter (Stockholm)'],
     'cons':['Komplexere Apps brauchen viele Iterationen','Backend-Anpassungen wackelig','Pricing pro Credit nicht ganz transparent','Mobile-App nur als Web-Wrapper'],
     'usecases':['MVP-Prototypen','Internal Tools','SaaS-Landingpages','Side-Projects'],
     'launched':'2024-04-15','lastUpdated':'2026-04-30',
     'website':'https://lovable.dev/','domain':'lovable.dev',
     'features':"""- **Full-Stack-Generation**: Frontend, Backend, DB-Schema in einem Prompt.
- **Supabase-Integration**: Auth, DB, Storage, Edge-Functions out-of-the-box.
- **Stripe-Integration** für Payments und Subscriptions.
- **GitHub-Sync**: jede Iteration commitet, eigenes Repo bleibt dein Code.
- **Multiplayer-Workspace** für Team-Bearbeitung.
- **Custom Domains** und Vercel/Netlify-Deploy mit einem Klick.
- **Visual-Edit-Mode**: per Klick Komponenten editieren ohne Prompt.""",
     'pricing':"""- **Free** · 5 Credits / Tag, Lovable-Subdomain, Lovable-Branding.
- **Pro** · $25 / Mon. ($240 jährlich) — 100 Credits / Mon., Custom Domain.
- **Teams** · $30 / Sitz / Mon. — Workspaces, geteilte Projekte.
- **Scale** · $100 / Mon. — 500 Credits, Priority-Generierung, Premium-Support.
- **Enterprise** · auf Anfrage — SSO, Audit-Logs, EU-Datenresidenz.
- **Credits** sind Generierungs-Tokens; ein typischer Edit kostet 1 Credit.""",
     'overview':"""**Lovable** ist seit 2024 die europäische Antwort auf v0 und Bolt — und hat sich in nur 18 Monaten zu einem der am schnellsten wachsenden AI-App-Builder entwickelt. Der schwedische Anbieter aus Stockholm differenziert sich über drei Dinge: **Full-Stack-Tiefe**, **echte GitHub-Integration** und **EU-Datenresidenz**.

**Full-Stack-Generation** heißt: Ein Prompt erzeugt nicht nur Frontend-Komponenten, sondern auch passende Backend-Routen, ein Supabase-Schema, Authentifizierung, Stripe-Anbindung. Wer eine SaaS-MVP baut, kommt von „Idee" zu „funktionierender App mit Login, Datenbank und Bezahlung" oft in unter zwei Stunden.

Die **GitHub-Integration** ist tiefer als bei vielen Konkurrenten: Statt nur einen ZIP-Export anzubieten, pusht Lovable jeden Edit als echten Commit in dein eigenes Repo. Wer sein Projekt aus Lovable „auswachsen" lassen will, hat nahtlosen Übergang zu lokalen IDEs, Pull-Requests, CI/CD.

Der **Visual-Edit-Mode** ist der zweite Killer-Feature: Statt jede Änderung per Prompt zu beschreiben, lässt sich auf Komponenten klicken, Text inline editieren, Farben tauschen — direkt in der Live-Preview. Für Designer-orientierte Workflows deutlich schneller als reines Prompting.

**Multiplayer-Workspaces** machen Lovable team-tauglich: Mehrere Personen sehen die Live-Preview, können parallel prompten, sehen sich gegenseitig im Cursor.

Schwächen: Komplexere Backend-Logik (etwa eigene Webhooks, Background-Jobs, externe APIs) braucht viele Iterationen, bis die KI die richtige Architektur trifft. Das **Credit-Pricing** ist nicht ganz transparent — ein simpler Edit kostet 1 Credit, ein größerer Refactor 5–10. Wer mit knappem Free-Tarif startet, ist schnell beim Pro-Plan.

Empfohlen für Founder, Product Manager und Designer, die schnell zu einer funktionierenden App kommen wollen — und für EU-Teams, die DSGVO-Datenresidenz und einen europäischen Anbieter brauchen."""},

    {'slug':'google-stitch','name':'Google Stitch','vendor':'Google','category':'coding',
     'tagline':'Googles UI-Designer mit Gemini — vom Text-Brief zu fertigen Screens, exportierbar als Figma oder Code.',
     'price':'Free (in Public Preview)','api':False,'dsgvo':'bedingt','origin':'USA',
     'rating':4.4,'reviews':1180,
     'pros':['Sehr starke Design-Konsistenz über mehrere Screens','Direkter Figma-Export','HTML/CSS-Code-Output','Powered by Gemini 3 Pro'],
     'cons':['Noch in Public Preview, Limits ändern sich','Code-Output noch unter v0-Niveau','Kein Backend, nur Frontend-Screens','Datenresidenz USA'],
     'usecases':['UI-Konzepte','Mockups für Stakeholder','Design-Sprints','Wireframe-Generierung'],
     'launched':'2025-05-20','lastUpdated':'2026-04-30',
     'website':'https://stitch.withgoogle.com/','domain':'withgoogle.com',
     'features':"""- **Text-zu-UI**: ein Brief erzeugt mehrere konsistente Screens auf einmal.
- **Image-zu-UI**: Foto, Skizze oder Screenshot als Input.
- **Figma-Export** mit erhaltener Layer-Struktur.
- **HTML/CSS-Code-Export** für Frontend-Implementierung.
- **Mehrere Style-Modes**: Modern, Classic, Vibrant, Minimal.
- **Iteratives Editing**: Screen-für-Screen verfeinern.
- **Powered by Gemini 3 Pro** für Design-Reasoning.""",
     'pricing':"""- **Public Preview** · komplett kostenlos, mit fairem Tageslimit.
- **Limits**: typisch 50 UI-Generierungen / Tag.
- **Bezahlmodell** noch nicht angekündigt — Roadmap deutet auf Workspace-Bundle.
- Watermark/Attribution im aktuellen Preview-Output nicht erforderlich.
- **Enterprise**-Pricing wird voraussichtlich über Google Cloud / Vertex laufen.""",
     'overview':"""**Google Stitch** wurde im Mai 2025 auf der Google I/O angekündigt und ist seit Sommer 2025 in einer Public Preview verfügbar. Das Tool füllt eine spezifische Lücke zwischen v0 (Code-zentriert) und Midjourney/Nano Banana (Bild-zentriert): **strukturiertes UI-Design**, das sich als Figma-Datei oder als HTML/CSS exportieren lässt.

Der **Workflow** ist erfrischend einfach. Ein Brief — „Eine SaaS-Landingpage für ein KI-Notiz-Tool, modern, dunkel, mit Hero, Features, Pricing, FAQ" — erzeugt einen ganzen Screen-Set, das stilistisch und typografisch konsistent ist. Anders als bei reinen Bildmodellen sind Buttons echte Buttons, Inputfelder echte Inputfelder, Spacings folgen einem Grid. Das macht den Output für Designer:innen direkt brauchbar.

Die **Mehrere-Screens-auf-einmal**-Generierung ist die größte Stärke: Während v0 oder Midjourney ein einzelnes Screen produzieren, liefert Stitch typischerweise 3–8 zusammenhängende Screens (Landing, Dashboard, Settings, Pricing) — alle im selben visuellen System. Für Stakeholder-Mockups ein massiver Zeitgewinn.

Der **Figma-Export** erhält die Layer-Struktur — Buttons, Karten, Container sind als Figma-Frames angelegt, Auto-Layout ist gesetzt, Komponenten sind verschachtelt. Designer können direkt im Figma weiterarbeiten, ohne alles neu aufzubauen.

Der **HTML/CSS-Output** ist solide, aber noch unter dem Niveau von v0 oder Lovable: Tailwind-Klassen werden teils ungewöhnlich kombiniert, Komponentenbenennung ist generisch. Für schnelle Frontend-Prototypen reicht es, für Production-Code muss nachgearbeitet werden.

Schwächen: Stitch ist **kein Backend-Tool** — es generiert nur Frontend-Screens, keine Datenbanken, keine APIs. Das **Code-Output**-Niveau hinkt v0 noch hinterher. Und die Public-Preview-Limits können sich kurzfristig ändern (waren schon mehrfach reduziert worden).

Empfohlen für Designer:innen und Produktmanager:innen, die schnelle UI-Konzepte brauchen — und für Teams, die im Google-Workspace-Ökosystem arbeiten und Stitch in den nächsten Monaten in den vollen Workspace-Kontext eingebettet sehen werden."""},

    {'slug':'miro-ai','name':'Miro AI','vendor':'Miro','category':'produktivitaet',
     'tagline':'KI-Layer im Miro-Whiteboard — generiert Mind-Maps, fasst Sticky-Cluster zusammen, baut User-Stories und Flowcharts aus Briefings.',
     'price':'In Miro Business+ enthalten · ab $16 / Sitz / Mon.','api':True,'dsgvo':'ja','origin':'USA',
     'rating':4.5,'reviews':5840,
     'pros':['Tief in den Miro-Workflow integriert','Cluster-Summary von Sticky-Notes','Mind-Map und Flowchart aus Prompt','EU-Hosting im Enterprise-Tarif'],
     'cons':['Nur in Bezahltarifen verfügbar','Outputs etwas generisch ohne Style-Vorlagen','Kein eigenes Modell-Routing','Teilweise Englisch-bias bei deutschen Briefings'],
     'usecases':['Workshop-Vorbereitung','Sticky-Note-Synthese','Flowchart-Generierung','User-Story-Mapping'],
     'launched':'2023-09-12','lastUpdated':'2026-04-30',
     'website':'https://miro.com/ai/','domain':'miro.com',
     'features':"""- **Cluster-Summary**: KI fasst Sticky-Note-Cluster zu Themen zusammen.
- **Mind-Map-Generator**: aus Stichwort entsteht eine vollständige Mind-Map.
- **Flowchart-Builder**: Prozess-Beschreibung wird zu Flussdiagramm.
- **User-Story-Generator** mit Akzeptanzkriterien.
- **AI-Image-Generator** für Mood-Boards direkt im Board.
- **Smart-Tagging** und **Auto-Grouping** von Stickies.
- **Talktrack**: aufgenommene Audio-Sessions werden zu strukturierten Notizen.""",
     'pricing':"""- **Free** · ohne Miro AI.
- **Starter** · $8 / Sitz / Mon. — limitierte AI-Aktionen.
- **Business** · $16 / Sitz / Mon. — volle Miro-AI-Funktionalität.
- **Enterprise** · auf Anfrage — SSO, EU-Datenresidenz, SLA, Audit-Logs.
- **AI-Credits** sind in Business+ unbegrenzt für Standard-Aktionen.
- **Trial** über 14 Tage für Business.""",
     'overview':"""**Miro AI** wurde im September 2023 als integraler KI-Layer in das Miro-Whiteboard eingebaut — und hat sich seitdem von einer Spielerei zum festen Bestandteil moderner Workshop- und Produkt-Workflows entwickelt. Der zentrale Vorteil ist die **tiefe Integration**: Statt ein separates KI-Tool zu öffnen, läuft Miro AI direkt im Board, nutzt vorhandene Stickies, Karten und Verbindungen als Kontext.

Die **Cluster-Summary** ist der häufigste Anwendungsfall: Nach einem Brainstorming mit 80 Stickies synthetisiert die KI thematische Cluster mit Titeln und Kernpunkten — was sonst ein nervöses Moderationskunststück nach dem Workshop war, ist jetzt eine Ein-Klick-Aktion. Ähnlich nützlich: **Smart-Tagging** und **Auto-Grouping**, die Stickies semantisch sortieren statt nur räumlich.

Der **Mind-Map-Generator** und der **Flowchart-Builder** sind die zweite Säule: Aus „Onboarding-Prozess für neue SaaS-User" entsteht ein vollständiges Flussdiagramm mit Entscheidungspunkten, Aktoren und Datenflüssen. Für Workshop-Vorbereitung und schnelle Konzeptarbeit ein massiver Zeitgewinn.

Der **User-Story-Generator** trifft den Product-Management-Workflow: Aus „Suchfunktion mit Filtern für E-Commerce-Produktliste" entstehen User-Stories im klassischen Format inklusive Akzeptanzkriterien — direkt als Stickies im Board.

**Talktrack** ist eine versteckte Stärke: Aufgenommene Audio-Sessions (Workshop-Aufnahmen, Diskussionen) werden in strukturierte Notizen verwandelt, die als Stickies im Board landen. Wer asynchron mit globalen Teams arbeitet, hat hier ein wertvolles Werkzeug.

Schwächen: Miro AI ist nur in den Bezahltarifen verfügbar — Free-User sehen die Funktionen, können sie aber nicht nutzen. Outputs sind solide, aber tendenziell generisch — wer Brand-Konsistenz braucht, muss manuell nachbearbeiten.

Empfohlen für Teams, die Miro bereits als zentrales Workshop-Tool nutzen — und für Workshop-Moderator:innen, die ihre Synthese-Arbeit beschleunigen wollen, ohne ein zweites Tool im Tab-Stapel."""},

    {'slug':'microsoft-designer','name':'Microsoft Designer','vendor':'Microsoft','category':'bildgenerierung',
     'tagline':'Microsofts Antwort auf Canva — KI-getrieben, mit GPT-Image-Backbone, tief in Microsoft 365 integriert und in der Free-Stufe großzügig.',
     'price':'Free · in M365 Personal/Family enthalten','api':False,'dsgvo':'ja','origin':'USA',
     'rating':4.5,'reviews':4720,
     'pros':['Sehr großzügiger Free-Tarif','GPT-Image-Backbone für Bildgenerierung','Native Integration in Word, PowerPoint, Outlook','EU-Datenresidenz im M365 Enterprise'],
     'cons':['Templates weniger zahlreich als Canva','Kein eigenes Brand-Kit auf Free','Kollaboration nur über M365-Konto','Dating-Funktionen weniger ausgereift'],
     'usecases':['Social-Media-Posts','Einladungen + Karten','Slide-Decks','Marketing-Visuals'],
     'launched':'2023-10-12','lastUpdated':'2026-04-30',
     'website':'https://designer.microsoft.com/','domain':'designer.microsoft.com',
     'features':"""- **Image Creator** (powered by GPT Image) für Foto-realistische Bildgenerierung.
- **Designs** mit Text-zu-Layout-Generierung für Social, Print, Web.
- **Sticker Creator** für eigene Sticker-Sets.
- **Frame Creator**: Personenbilder in Style-Frames einbetten.
- **Restyle Image**: bestehendes Bild im neuen Stil.
- **Invitations** mit personalisierbaren Einladungs-Designs.
- **Native PowerPoint-, Word-, Outlook-Integration** mit Designer-Vorschlägen.""",
     'pricing':"""- **Free** · großzügiges Tageslimit für Bildgenerierung und Designs.
- **Microsoft 365 Personal** · €7 / Mon. — Designer Premium ohne Limit.
- **Microsoft 365 Family** · €10 / Mon. (6 Personen) — Designer Premium für alle.
- **Microsoft 365 Business Standard** · €11,70 / Sitz / Mon. — Designer + alle Office-Apps.
- **Microsoft 365 E3/E5** · Designer als Bestandteil, EU-Datenresidenz.
- **Copilot Pro** · $20 / Mon. — höhere Designer-Limits zusätzlich.""",
     'overview':"""**Microsoft Designer** ist seit Oktober 2023 Microsofts direkte Antwort auf Canva — und hat sich von einem zaghaften Anfänger-Tool zu einer der **großzügigsten kostenlosen Design-Apps** der Branche entwickelt. Im Hintergrund läuft GPT Image (zuvor DALL·E 3) für die Bildgenerierung, was Designer in vielen Generierungs-Disziplinen näher an die SOTA-Modelle bringt als die meisten Mitbewerber.

Der **Image Creator** ist der häufigste Einstieg: Ein Prompt, ein Bild — kostenlos, ohne Account-Friktion (mit Microsoft-Account), in vergleichsweise hoher Qualität. Wer keinen ChatGPT-Plus-Account hat, bekommt hier den günstigsten regulären Zugang zu GPT-Image-generierten Bildern.

**Designs** ist der Canva-Konkurrent: Vorlagen für Social-Media-Posts, Einladungen, Karten, Slide-Decks. Die Auswahl ist kleiner als bei Canva (geschätzt 1/5), die Qualität aber ähnlich. Was Microsoft besser kann: **Text-zu-Layout-Generierung** — ein Prompt, ein fertiges Layout mit AI-generiertem Bild und passender Typografie.

**Restyle Image** und **Frame Creator** sind die spannendsten Editing-Features: Bestehende Bilder in einen anderen Stil transformieren oder Personenbilder in Style-Frames einbetten — beides funktioniert überraschend gut.

Die **native Office-Integration** ist der entscheidende strategische Vorteil: Designer-Vorschläge erscheinen direkt in PowerPoint (Folien-Layouts), Word (Cover-Designs), Outlook (E-Mail-Banner). Wer Microsoft 365 sowieso nutzt, hat Designer ohne separates Abo direkt im Arbeitsfluss.

**EU-Datenresidenz** im Enterprise-Tarif (M365 E3/E5) macht Designer für DSGVO-sensible Workflows in deutschen Behörden, Krankenhäusern und Banken zugänglich — ein klarer Vorteil gegenüber Canva und Adobe Firefly.

Schwächen: Der **Vorlagenkatalog** ist kleiner als bei Canva, das **Brand-Kit** für eigene Logos/Farben gibt's nur in Pro-Tarifen. Kollaboration funktioniert nur über das Microsoft-Konto — keine offenen Sharing-Links wie bei Canva.

Empfohlen für Microsoft-365-Nutzer:innen aller Art und für jeden, der einen sehr großzügigen kostenlosen KI-Bildgenerator mit integrierter Design-App sucht. Für Teams in regulierten Branchen mit M365 E3/E5-Lizenzen oft die einzige DSGVO-konforme Designer-Wahl."""},
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
