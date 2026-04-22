#!/usr/bin/env python3
"""Add a curated set of additional AI tools to the Cognitor CMS.

Each new tool entry:
  1. Creates a Post with the editorial overview (markdown).
  2. Creates a tool element referencing that post via post_id,
     including features + pricing markdown inline.

Idempotent: skips any slug that already exists in the CMS.
"""
import requests, urllib3, sys, time
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

# ---- Resolve content type id
cts = requests.get(f'{BASE}/{SITE}/contenttypes/', headers=H, verify=False).json()
tool_ct = next(c for c in cts if c.get('display_identifier') == 'tool')

# ---- Load existing slugs for idempotency
existing = []
page = 1
while True:
    r = requests.get(f'{BASE}/{SITE}/elements/?type_id={tool_ct["id"]}&size=200&page={page}',
        headers=H, verify=False).json()
    existing += r.get('items', [])
    if not r.get('has_next'): break
    page += 1
existing_slugs = {el['data'].get('slug') for el in existing}
print(f'  · {len(existing_slugs)} tools already in CMS')

# =====================================================================
# NEW TOOLS
# =====================================================================
# Each entry: all tool data + overview (markdown) for the Post.
# =====================================================================
TOOLS = [
# ---- Sprachmodelle & Chat ----
{
    'slug':'ms-copilot', 'name':'Microsoft Copilot', 'vendor':'Microsoft', 'category':'sprachmodelle',
    'tagline':'KI-Assistent tief in Microsoft 365 verzahnt — für Outlook, Word, Excel und Teams.',
    'price':'Ab €21,90 / Nutzer / Monat', 'api':True, 'dsgvo':'bedingt', 'origin':'USA',
    'rating':4.2, 'reviews':1420,
    'pros':['Direkt in Outlook/Word/Excel','Meeting-Zusammenfassungen in Teams','Enterprise-Rollout mit Entra ID','Nutzt GPT-5 als Modell-Kern'],
    'cons':['Nur mit M365-Lizenz nutzbar','Qualität je Aufgabe schwankend','Regionale Verfügbarkeit uneinheitlich'],
    'usecases':['E-Mail-Triage','Meeting-Notizen','Excel-Analyse','Slide-Erstellung'],
    'launched':'2023-11-01',
    'overview':"""**Microsoft Copilot** ist die KI-Assistenz-Schicht, die Microsoft konsequent in das gesamte M365-Ökosystem eingezogen hat. Statt eines separaten Chat-Tools wird die KI dort eingebettet, wo die Arbeit tatsächlich stattfindet: in Outlook-E-Mails, Word-Dokumenten, Excel-Tabellen, PowerPoint-Folien und Teams-Meetings.

Der Kern ist ein GPT-5-basierter Agent, der über die Graph-API auf E-Mails, Kalender und SharePoint zugreift. Besonders wertvoll sind die nahtlose Meeting-Transkription mit Aufgaben-Extraktion sowie die Tabellen-Analyse in Excel mit natürlicher Sprache.

Der Pferdefuß: Ohne M365-Lizenz gibt es keinen Zugang. Die Integration ist strategisch gedacht, nicht offen. Für Organisationen, die ohnehin mit Microsoft-Stack arbeiten, ist Copilot die pragmatischste Adoption-Option — weil sie das bestehende Berechtigungsmodell respektiert. Für alle anderen ist der Einstieg teuer und die Bindung eng.""",
    'features':"""- **Copilot in Word/Excel/PowerPoint/Outlook/Teams** — native Integration pro App.
- **Microsoft 365 Graph** — Zugriff auf E-Mails, Kalender, Dateien, Chats.
- **Meeting-Transkription** mit Aufgaben-Extraktion in Teams.
- **Copilot Studio** — eigene Agents auf Microsoft-Infrastruktur bauen.
- **Enterprise Data Protection** — Daten werden nicht für Training verwendet.
- **Agent Store** mit vorgefertigten Rollen-Copilots.
- **Azure OpenAI Integration** mit EU-Datenresidenz (gegen Aufpreis).""",
    'pricing':"""- **Copilot Pro** · €21,90 / Nutzer / Monat — für Einzelpersonen mit M365 Personal/Family.
- **Copilot for Microsoft 365** · $30 / Nutzer / Monat — Enterprise-Lizenz, benötigt M365 E3/E5/Business.
- **Copilot Chat** · Free — eingeschränkte Web-Version mit GPT-5.
- **Copilot Studio** · ab $200 / Monat — für eigene Agent-Entwicklung.""",
},
{
    'slug':'grok', 'name':'Grok', 'vendor':'xAI', 'category':'sprachmodelle',
    'tagline':'Provokanter KI-Assistent mit Echtzeit-X-Zugang — für Recherche mit Biss.',
    'price':'Freemium — SuperGrok $30/Mon.', 'api':True, 'dsgvo':'nein', 'origin':'USA',
    'rating':4.0, 'reviews':890,
    'pros':['Echtzeit-Zugriff auf X/Twitter-Feed','Offenere Meinungsäußerung','Competitive in Reasoning-Benchmarks','Günstige API-Preise'],
    'cons':['Auf X verankert — Bias in Recherche','Kein DSGVO-Setup','Fokus eher westlich/englisch'],
    'usecases':['Trend-Monitoring','Quick-Recherche','Entertainment-/Alltags-Chat'],
    'launched':'2023-11-04',
    'overview':"""**Grok** ist das KI-Frontend von Elon Musks Firma xAI, tief mit der X-Plattform (ehemals Twitter) verzahnt. Dadurch hat Grok als einziges der großen Sprachmodelle nativen Echtzeit-Zugriff auf den aktuellen Social-Feed — für Trend-Tracking und Breaking-News-Recherche ein echter Vorteil.

Technisch liegt Grok-4 in Standard-Benchmarks auf Augenhöhe mit GPT-5 und Claude. Die Besonderheit ist eher kultureller Natur: Grok ist bewusst weniger zensierend getunt als die Konkurrenz, was manche als Freiheit schätzen und andere als Risiko bewerten.

Für professionelle, DSGVO-kritische Anwendungen ist Grok keine Option — das Unternehmen verarbeitet in den USA und bietet keine Standard-Auftragsverarbeitung. Für Social-Analytics, kreative Entwürfe oder als Zweitmeinung neben einem Haupttool ist es hingegen eine schnelle, preiswerte Ergänzung.""",
    'features':"""- **Live-Zugriff auf X/Twitter-Feed** — einmalig unter den großen Chatbots.
- **Grok 4** Modell mit starker Reasoning-Fähigkeit.
- **Think-Modus** für mehrstufige Analysen.
- **Image-Generation** via Flux integriert.
- **API** mit Pay-per-Use-Preisen, auch für Enterprise.
- **DeepSearch** für längere Rechercheketten.
- **Eingeschränkte Zensur-Filter** im Vergleich zu Konkurrenz.""",
    'pricing':"""- **Free** — begrenzte Anfragen mit Grok 4 Fast.
- **SuperGrok** · $30 / Monat — höhere Limits, Grok 4 Heavy, Think-Modus.
- **SuperGrok Heavy** · $300 / Monat — Agent-Mode, höchste Priorität.
- **X Premium+** · $40 / Monat — Grok-Zugang inklusive.
- **API** — Grok 4 ab $3 / 1 M Input-Token, $15 / 1 M Output.""",
},
{
    'slug':'deepseek', 'name':'DeepSeek', 'vendor':'DeepSeek', 'category':'sprachmodelle',
    'tagline':'Open-Weights-Modell aus China — extrem günstig und auf Reasoning-Benchmarks stark.',
    'price':'Freemium — API ab $0.27 / 1M Token', 'api':True, 'dsgvo':'nein', 'origin':'CN',
    'rating':4.3, 'reviews':620,
    'pros':['Open Weights — frei selbst hostbar','Extrem günstige API-Preise','Starke Reasoning-Leistung (V3, R1)','Breite Community-Rezeption'],
    'cons':['Datenverarbeitung in China','Rechtliche Bedenken bei sensiblen Inhalten','Ohne EU-Compliance-Setup'],
    'usecases':['Self-Hosting','Code-Generierung','Günstige Massen-Inferenz','Forschung'],
    'launched':'2023-07-17',
    'overview':"""**DeepSeek** hat die Branche Ende 2024 mit einem Paukenschlag überrascht: Ein chinesisches Open-Weights-Modell, das GPT-4-Niveau erreicht — zu einem Bruchteil der API-Kosten der US-Konkurrenz. Das anschließend veröffentlichte R1-Reasoning-Modell setzte noch eins drauf und löste in den USA Diskussionen über Infrastruktur-Investitionen aus.

Für Entwicklerinnen und Forschende ist DeepSeek deshalb interessant: Die Modelle (V3, R1, Coder) können frei heruntergeladen und auf eigener Hardware betrieben werden. Die API ist mit $0,27 pro Million Input-Token unvergleichlich günstig und erlaubt Massen-Anwendungen, die sonst unwirtschaftlich wären.

Der strategische Haken liegt im Anbieter-Ursprung. Wer die gemanagte API nutzt, übermittelt Daten nach China — für europäische Organisationen mit DSGVO-Bindung praktisch ausgeschlossen. Self-Hosting umgeht das, verlangt aber GPU-Infrastruktur. Für Forschung, Prototyping und nicht-sensible Anwendungen bleibt DeepSeek dennoch eine der interessantesten Entwicklungen des letzten Jahres.""",
    'features':"""- **Open Weights** — Modelle unter MIT-/Apache-Lizenz frei nutzbar.
- **DeepSeek V3.1 & R1** — Reasoning-fokussiert, starke Benchmark-Ergebnisse.
- **DeepSeek-Coder** für Programmieraufgaben.
- **Extrem günstige API** — ein Zehntel der GPT-5-Preise.
- **Web-Chat** gratis mit allen Modellen.
- **Distillation-Varianten** (1.5B–70B) für lokalen Betrieb.
- **Growing Community** auf Hugging Face mit Forks und Feintuning.""",
    'pricing':"""- **DeepSeek Chat** · Free — unbegrenzter Web-Zugang.
- **API** — DeepSeek V3.1 ab $0.27 / 1 M Input-Token, $1.10 / 1 M Output.
- **R1 API** — $0.55 / 1 M Input, $2.19 / 1 M Output.
- **Self-Hosting** — kostenlos (GPU-Kosten exklusiv).
- **Enterprise** — via Resellern oder Cloud-Anbietern mit EU-Residenz.""",
},
# ---- Bildgenerierung ----
{
    'slug':'flux', 'name':'FLUX', 'vendor':'Black Forest Labs', 'category':'bildgenerierung',
    'tagline':'Europäisches Bildmodell aus Freiburg — State-of-the-Art bei Typografie und Prompt-Treue.',
    'price':'Freemium — API ab $0.003 / Bild', 'api':True, 'dsgvo':'ja', 'origin':'EU (DE)',
    'rating':4.6, 'reviews':480,
    'pros':['Deutscher Anbieter','Herausragende Textwiedergabe im Bild','Open-Source-Varianten verfügbar','FLUX.1 Kontext für präzise Bearbeitung'],
    'cons':['Frontend weniger ausgereift als Midjourney','API-Abrechnung Credit-basiert','Kleineres Community-Ökosystem'],
    'usecases':['Editorial-Illustration','Typografie-lastige Visuals','Produkt-Mockups','Präzise Bildbearbeitung'],
    'launched':'2024-08-01',
    'overview':"""**FLUX** kommt aus Freiburg im Breisgau. Das Team hinter Black Forest Labs besteht aus den ursprünglichen Stable-Diffusion-Autoren, die Stability AI verlassen haben. Das erste Release (FLUX.1) setzte 2024 neue Maßstäbe bei Prompt-Treue und — besonders auffällig — bei der Wiedergabe von Text im Bild, einem lange ungelösten Problem.

Das Portfolio umfasst Pro-/Dev-/Schnell-Varianten sowie FLUX.1 Kontext für punktgenaue Nachbearbeitung bestehender Bilder (präzises Inpainting, Style-Transfer, Charakter-Konsistenz). Die Modelle werden als Weights freigegeben (Dev/Schnell) oder über die API gehostet (Pro) — ein pragmatischer Mix aus Open und Managed.

Für deutsche Unternehmen mit DSGVO-Auflagen ist FLUX derzeit die mit Abstand beste Adresse für Bildgenerierung. Die API-Preise sind aggressiv, die Qualität auf Augenhöhe mit Midjourney, das Stilspektrum ist breit. Das Web-Frontend ist weniger poliert als bei der US-Konkurrenz — wer mit APIs oder Drittanbieter-Frontends arbeitet, bekommt das nicht zu spüren.""",
    'features':"""- **FLUX.1 Pro/Dev/Schnell** — drei Varianten je nach Tempo/Qualität.
- **FLUX.1 Kontext** für präzise Bild-Editing-Workflows.
- **Herausragende Typografie-Wiedergabe** — Text im Bild sauber lesbar.
- **Open Weights** (Dev + Schnell) unter Non-Commercial-Lizenz.
- **API via bfl.ai** mit EU-Datenresidenz.
- **Hugging Face & Replicate** als Drittanbieter-Routen.
- **FLUX Krea** — kuratierte Ästhetik-Variante.""",
    'pricing':"""- **Playground (bfl.ai)** · Free — begrenzte Demo-Generationen.
- **API FLUX.1 Schnell** — ab $0.003 / Bild.
- **API FLUX.1 Dev** — ab $0.025 / Bild.
- **API FLUX.1 Pro** — ab $0.055 / Bild.
- **FLUX.1 Kontext Pro** — ab $0.04 / Edit.
- **Self-Hosting** — kostenlos für Dev/Schnell (Non-Commercial).""",
},
{
    'slug':'ideogram', 'name':'Ideogram', 'vendor':'Ideogram', 'category':'bildgenerierung',
    'tagline':'Spezialist für Bilder mit perfekter Typografie — Plakate, Logos, Social-Creative.',
    'price':'Freemium — Plus $10/Mon.', 'api':True, 'dsgvo':'bedingt', 'origin':'USA',
    'rating':4.4, 'reviews':530,
    'pros':['Beste Typografie im Bild am Markt','Stil-Referenzen via Pinsel','Gute Gestaltungskonvention (Poster, Logos)','Kostenloser Tarif großzügig'],
    'cons':['Weniger Fotorealismus als FLUX/Midjourney','Keine EU-Datenresidenz','API noch in Beta'],
    'usecases':['Social-Media-Creative','Logo-Ideation','Plakat-Prototypen','Event-Grafiken'],
    'launched':'2023-08-01',
    'overview':"""**Ideogram** hat sich früh auf ein einziges Problem konzentriert, das andere Bildmodelle lange ignoriert haben: lesbare, gestaltete Typografie im Bild. Logos, Plakate, Social-Creative mit exakten Texten — was bei Midjourney jahrelang nur über Photoshop-Nacharbeit ging, liefert Ideogram direkt.

Der Editor ist gestaltet wie ein leichtes Design-Tool: Magic-Fill, Style-Pinsel zur Übertragung einer Optik auf neue Bilder, Template-Bibliothek für typische Creative-Formate. Das macht Ideogram besonders für Marketing- und Agentur-Teams interessant, die schnell erste Entwürfe brauchen.

Bei Fotorealismus und ästhetischer Finesse rangiert Ideogram hinter Midjourney und FLUX. Als Typografie-Spezialwerkzeug in der Content-Pipeline ist es aber konkurrenzlos — und der Free-Tier ist so großzügig, dass Ausprobieren problemlos ist.""",
    'features':"""- **Magic Fill & Editor** für gezielte Bildbearbeitung.
- **Style Reference** — Look eines Bildes auf neue übertragen.
- **Ideogram 3.0** — State-of-the-Art bei Text-Rendering.
- **Templates** für Posts, Plakate, Logos, Event-Grafiken.
- **Canvas** für mehrere Iterationen nebeneinander.
- **API** für Pipeline-Integration (Beta).
- **Remix-Funktion** zum schnellen Variieren öffentlicher Bilder.""",
    'pricing':"""- **Free** — 10 Prompts / Tag mit begrenzten Features.
- **Basic** · $7 / Monat — 400 Prompts / Monat, privater Modus.
- **Plus** · $10 / Monat — 1 000 Prompts, bevorzugte Generierung.
- **Pro** · $20 / Monat — 4 000 Prompts, alle Premium-Features.
- **API** · Pay-as-you-go, ab $0.01 / Bild.""",
},
{
    'slug':'adobe-firefly', 'name':'Adobe Firefly', 'vendor':'Adobe', 'category':'bildgenerierung',
    'tagline':'Bildgenerierung aus dem Adobe-Kosmos — auf kommerziell lizenzierten Trainingsdaten.',
    'price':'Ab €5 / Monat oder mit Creative Cloud', 'api':True, 'dsgvo':'bedingt', 'origin':'USA',
    'rating':4.2, 'reviews':1760,
    'pros':['Commercial-safe Trainingsdaten','Tiefe Integration in Photoshop/Illustrator','Generative Fill, Remove, Expand','Enterprise-Lizenzbedingungen'],
    'cons':['Qualität unter Midjourney/FLUX','Credit-System kann einschränken','Teils nur in Creative Cloud nutzbar'],
    'usecases':['Konzeptarbeit in Photoshop','Bild-Retusche','Content-Vervielfältigung','Rechtssichere Agenturarbeit'],
    'launched':'2023-03-21',
    'overview':"""**Adobe Firefly** ist die Antwort eines traditionellen Kreativsoftware-Herstellers auf generative KI — mit einem starken Verkaufsargument: Das Modell wurde ausschließlich auf Adobe-Stock-Material und gemeinfreien Bildern trainiert. Adobe garantiert dadurch kommerzielle Nutzbarkeit und übernimmt bei Enterprise-Verträgen sogar die Rechtsverteidigung. Das macht Firefly für Agenturen und Corporates zur pragmatischsten Option.

Die eigentliche Stärke liegt in der Integration: Generative Fill und Expand in Photoshop, Retype und Vector-Recolor in Illustrator, Scene-Detection in Premiere. Wer ohnehin in der Creative Cloud arbeitet, bekommt die KI dort, wo sie gebraucht wird.

In der reinen Bildqualität liegt Firefly deutlich hinter Midjourney und FLUX — stilistische Finesse und Prompt-Treue sind moderater. Für visuelle Recherche oder künstlerische Freiheit greifen Profis deshalb oft zusätzlich zu spezialisierten Tools und routen Firefly ausschließlich dann ein, wenn Rechtssicherheit wichtig ist.""",
    'features':"""- **Generative Fill / Expand** in Photoshop — die Killer-Features.
- **Text-to-Image** im Firefly Web-Frontend.
- **Generative Recolor** und Vector-to-Image in Illustrator.
- **Commercial-Safe Training** auf lizenzierten Quellen.
- **Firefly Services API** für Enterprise-Integration.
- **Style & Structure Reference** aus eigenen Bildern.
- **Rights Clearance & IP Indemnification** in Enterprise-Tier.""",
    'pricing':"""- **Firefly Free** — 25 Generations pro Monat (begrenzt).
- **Firefly Standard** · €5 / Monat — 2 000 Generations, kommerzielle Nutzung.
- **Firefly Pro** · €30 / Monat — 7 000 Generations, Video-Features.
- **Creative Cloud All Apps** · €70 / Monat — Firefly inklusive.
- **Enterprise** — Custom-Pricing mit IP-Absicherung.""",
},
# ---- Video & Audio ----
{
    'slug':'suno', 'name':'Suno', 'vendor':'Suno AI', 'category':'video-audio',
    'tagline':'Songs, Instrumentals und Sprachspuren aus Text-Prompts — Musik-Generierung in Studio-Qualität.',
    'price':'Freemium — Pro $10/Mon.', 'api':False, 'dsgvo':'nein', 'origin':'USA',
    'rating':4.5, 'reviews':1840,
    'pros':['Verblüffende Musik-Qualität','Verschiedene Genres und Sprachen','Vocals mit Lyrics generierbar','V4-Modell mit neuer Klarheit'],
    'cons':['Kein offenes Modell','Rechtliche Grauzone bei Stil-Imitation','Keine API'],
    'usecases':['Jingles','Demo-Tracks','Soundtrack-Prototypen','Content-Musik'],
    'launched':'2023-12-01',
    'overview':"""**Suno** hat die Musik-KI aus dem Forschungslabor in den Mainstream gebracht. Wer „A melancholic indie folk song about leaving Berlin in autumn" eingibt, bekommt innerhalb von Sekunden zwei vollständige Tracks — inklusive Gesangsspur mit Lyrics, mehrstimmig, rhythmisch tight.

Das seit 2024 veröffentlichte V4-Modell hat die Klangqualität noch einmal deutlich gehoben: Stimmen klingen weniger artifiziell, Mixes sind sauberer. Für Jingles, Hintergrundmusik in Videos, Demo-Tracks oder als Ideations-Werkzeug für professionelle Komponisten ist Suno ein echtes Produktivitäts-Tool.

Die rechtliche Lage ist unklar. Gegen Suno und Konkurrent Udio laufen Klagen großer Labels wegen Trainings-Datennutzung. Für kommerziellen Einsatz sollte man den Custom-Tier mit Commercial-Use-Flag wählen und stilistische Imitation echter Künstler unterlassen. Für kreatives Spiel und Content mit moderatem Risiko ist Suno jedoch unschlagbar.""",
    'features':"""- **Text-to-Song** mit generierten Lyrics in 30+ Sprachen.
- **Custom Mode** — eigene Lyrics und strukturierte Songabschnitte vorgeben.
- **Persona** zum Wiederverwenden einer Stimme über Tracks.
- **V4-Modell** mit deutlich verbesserter Audio-Qualität.
- **Cover-Feature** zum Ummixen eigener Aufnahmen.
- **Stems Download** (Pro+) für DAW-Nachbearbeitung.
- **Community-Feed** für Entdeckung und Remix.""",
    'pricing':"""- **Basic** · Free — 50 Credits / Tag (10 Songs).
- **Pro** · $10 / Monat — 2 500 Credits, kommerzielle Nutzung.
- **Premier** · $30 / Monat — 10 000 Credits, Prioritätsrendering.
- **Enterprise** · auf Anfrage — Custom-Verträge mit IP-Schutz.""",
},
{
    'slug':'synthesia', 'name':'Synthesia', 'vendor':'Synthesia', 'category':'video-audio',
    'tagline':'KI-Avatar-Videos in 140+ Sprachen — Schulungen, Produkt-Demos, Onboarding ohne Kamera.',
    'price':'Ab $22 / Monat', 'api':True, 'dsgvo':'ja', 'origin':'UK',
    'rating':4.4, 'reviews':1030,
    'pros':['Realistische Avatare in vielen Sprachen','Enterprise-Ready (SSO, SOC 2)','UK/EU Datenverarbeitung','Eigene Personal Avatars trainierbar'],
    'cons':['Teuer bei hohem Volumen','Avatare wirken noch leicht künstlich','Eingeschränkte Mimik-Dynamik'],
    'usecases':['Corporate-Trainings','Produkt-Erklärvideos','Internes Onboarding','Multilingual-Lokalisierung'],
    'launched':'2017-01-01',
    'overview':"""**Synthesia** ist seit Jahren der Marktführer für KI-Avatar-Videos — und lange bevor es den Begriff „generative KI" im Mainstream gab. Das Londoner Unternehmen bedient primär den Enterprise-Markt: Konzerne drehen Produktschulungen, Compliance-Videos oder Onboarding-Inhalte, ohne Sprecher zu buchen oder Studios zu mieten.

Aus einem eingetippten Skript entsteht in Minuten ein Video mit einem der 250+ Stock-Avatare in 140+ Sprachen. Wer möchte, kann sich einen Personal Avatar trainieren lassen — aus wenigen Minuten eigener Aufnahmen entsteht ein KI-Zwilling, der beliebige Texte in beliebigen Sprachen spricht.

Für europäische Organisationen ein großer Vorteil: Synthesia ist UK-basiert, DSGVO-konform, mit Standard-AVV. Die Preise sind allerdings kein Taschengeld — ab $22/Monat im Starter-Tier, ab $89 im Creator-Tier, Enterprise-Verträge im fünfstelligen Bereich. Wer regelmäßig Lokalisierungs-Kosten hat, amortisiert das schnell.""",
    'features':"""- **250+ Stock-Avatare** in 140+ Sprachen und Akzenten.
- **Personal Avatar** — eigenen KI-Zwilling trainieren (Creator+).
- **Video-Editor** mit Szenen, Transitions, Branding.
- **ElevenLabs-Integration** für Premium-Stimmen (optional).
- **API & Webhooks** für automatisierte Video-Pipelines.
- **Translation** — vorhandene Videos automatisch umsprechen.
- **Enterprise-Grade** — SOC 2, DPA, SSO, UK/EU-Residenz.""",
    'pricing':"""- **Free** — 3 Minuten Video / Monat zum Ausprobieren.
- **Starter** · $22 / Monat — 120 Minuten, Stock-Avatare.
- **Creator** · $89 / Monat — 360 Minuten, Personal Avatar.
- **Enterprise** · auf Anfrage — unlimited, SSO, Custom-Support.
- **API** — Volume-Tarife, ab ~$0.50 pro Minute Video.""",
},
# ---- Coding ----
{
    'slug':'windsurf', 'name':'Windsurf', 'vendor':'Codeium', 'category':'coding',
    'tagline':'KI-native IDE mit Agent-Workflow — Cursor-Herausforderer mit Fokus auf Team-Setups.',
    'price':'Freemium — Pro $15/Mon.', 'api':False, 'dsgvo':'bedingt', 'origin':'USA',
    'rating':4.4, 'reviews':610,
    'pros':['Agent-Mode mit Cascade-Funktion','Schnelle Autocomplete','Team-Features inklusive','Enterprise-Deployment möglich'],
    'cons':['Jüngeres Produkt als Cursor','Einige Tool-Integrationen noch im Aufbau','Self-Hosted nur im Teams-Tier'],
    'usecases':['Tägliche Entwicklung','Multi-File-Refactoring','Code-Review'],
    'launched':'2024-11-01',
    'overview':"""**Windsurf** ist der zweite IDE-Launch des Codeium-Teams — nach dem Browser-Plugin bauen sie jetzt eine vollwertige VS-Code-Fork-IDE mit KI-Fokus. Das Produkt positioniert sich direkt gegen Cursor und setzt auf einen zentralen Agent-Mode namens Cascade, der über mehrere Dateien autonom Änderungen plant und ausführt.

Die Completion-Qualität ist auf Augenhöhe mit Cursor, die UX ähnelt der Konkurrenz stark (VS-Code-Basis, Chat-Panel, Diff-Review). Unterschiede: Die Teams-Pläne sind günstiger als bei Cursor und Windsurf bietet Self-Hosting im Enterprise-Tier an — für Organisationen mit striktem Code-Schutz ein wichtiges Argument.

Für Einzelentwicklerinnen ist die Wahl zwischen Cursor und Windsurf heute weitgehend Geschmackssache. Für Teams mit Budget- oder Compliance-Zwängen lohnt ein genauerer Vergleich — Windsurf hat in beiden Kategorien Vorteile.""",
    'features':"""- **Cascade Agent** — plant und führt Multi-File-Edits autonom aus.
- **Supercomplete** — kontextgetriebenes Autocomplete über Dateigrenzen.
- **Memory-System** lernt Projekt-Konventionen.
- **Inline Chat** direkt im Editor.
- **Model-Routing** zwischen Claude, GPT-5, Gemini.
- **Teams-Features** mit Shared-Context und Rollen.
- **Self-Hosted Enterprise** mit Air-Gap-Support.""",
    'pricing':"""- **Free** — 25 Agent-Aktionen / Monat, begrenzte Completion.
- **Pro** · $15 / Monat — 500 Agent-Aktionen, volle Completion.
- **Pro Ultimate** · $60 / Monat — unlimited Completion, 3 000 Agent-Aktionen.
- **Teams** · $30 / Nutzer / Monat — Team-Admin, zentrale Abrechnung.
- **Enterprise** · auf Anfrage — Self-Hosting, SSO, Audit-Logs.""",
},
# ---- Agenten & Automation ----
{
    'slug':'n8n', 'name':'n8n', 'vendor':'n8n GmbH', 'category':'agenten',
    'tagline':'Open-Source Workflow-Automation aus Berlin — visuelle Nodes mit LLM-Integration.',
    'price':'Freemium — Cloud ab €20/Mon.', 'api':True, 'dsgvo':'ja', 'origin':'EU (DE)',
    'rating':4.7, 'reviews':780,
    'pros':['Self-Hosting ohne Limits','Deutscher Anbieter, EU-Hosting','Über 400 Integrationen','AI Agent Nodes integriert'],
    'cons':['Learning-Curve steiler als bei Zapier','Sustainable-Use-Lizenz ist kein reines OSS','Cloud-Tarife bei hohem Volumen teuer'],
    'usecases':['CRM-Sync','Content-Pipelines','RAG-Pipelines','IT-Automation'],
    'launched':'2019-06-25',
    'overview':"""**n8n** ist das europäische Pendant zu Zapier und Make — aber mit einem wesentlichen Unterschied: Fair-Code-Lizenz, komplett Self-Host-fähig, mit vollem Feature-Zugriff ohne künstliche Limits. Das Berliner Unternehmen hat sich zur Go-to-Plattform für alle entwickelt, die Datenschutz und Kontrolle ernst nehmen.

Mit dem neuen AI-Agent-Node ist n8n nicht mehr nur Workflow-Engine, sondern vollwertige Agenten-Plattform. Nodes für OpenAI, Anthropic, lokale Modelle via Ollama, Vector-Databases (Qdrant, Pinecone) machen es zum Standardwerkzeug für produktive RAG-Pipelines und Multi-Step-Agent-Systeme.

Über 400 fertige Integrationen decken CRM, E-Commerce, Dev-Tools, Messenger ab. Die Lernkurve ist steiler als bei No-Code-Konkurrenz — wer Schritt-für-Schritt visuell denkt, gewinnt aber enorme Flexibilität. Die deutsche Herkunft und der Self-Host-Weg machen n8n zur unkompliziertesten Option für EU-Organisationen.""",
    'features':"""- **Visual Workflow Editor** mit 400+ Nodes.
- **AI Agent Node** — LangChain-basierte Agenten visuell bauen.
- **Self-Hosting** in Docker, Kubernetes oder auf Bare Metal.
- **Code Nodes** in JavaScript/Python für individuelle Logik.
- **Trigger-Vielfalt** — Webhook, Cron, Events, Polling.
- **Version Control** und Team-Kollaboration.
- **Sub-Workflows** für modulare Pipeline-Architektur.""",
    'pricing':"""- **Self-Hosted Community** · Free — komplett, lokal oder in eigener Cloud.
- **Cloud Starter** · €20 / Monat — 5 aktive Workflows, 2 500 Executions.
- **Cloud Pro** · €50 / Monat — 15 aktive Workflows, 10 000 Executions.
- **Enterprise** · auf Anfrage — SSO, Audit-Logs, 24/7-Support.
- **Sustainable Use License** — Production-Nutzung erlaubt, Reselling nicht.""",
},
{
    'slug':'make', 'name':'Make', 'vendor':'Celonis', 'category':'agenten',
    'tagline':'No-Code-Automation-Plattform mit visuellem Scenario-Builder und starker KI-Integration.',
    'price':'Freemium — Core $9/Mon.', 'api':True, 'dsgvo':'ja', 'origin':'EU (CZ)',
    'rating':4.5, 'reviews':1240,
    'pros':['Visueller Flow-Builder','EU-Hosting in Prag','2 000+ Apps','AI-Module (OpenAI, Claude) integriert'],
    'cons':['Operations-basierte Abrechnung schwer abzuschätzen','Komplexe Scenarios brauchen Übung','Support nur per Ticket'],
    'usecases':['Marketing-Automation','Data-Routing','Social-Media-Pipelines','Meeting-Nachbereitung'],
    'launched':'2012-01-01',
    'overview':"""**Make** (früher Integromat) kommt aus Prag und ist seit der Celonis-Übernahme 2020 ein wichtiger europäischer Anbieter für No-Code-Automation. Der visuelle Scenario-Builder ist expressiver als Zapiers Schritt-für-Schritt-Ansatz und erlaubt parallele Zweige, Iterations- und Aggregations-Module — fühlt sich eher wie Programmieren auf einem Whiteboard an.

Mit 2 000+ Integrationen und einem starken KI-Modul-Repertoire (OpenAI, Claude, Azure OpenAI, Perplexity) lassen sich auch anspruchsvolle KI-gestützte Prozesse abbilden: E-Mails klassifizieren und automatisch antworten, Social-Posts mit Bildgenerierung erstellen, Kunden-Feedback durch Sentiment-Analyse filtern.

Die EU-Datenresidenz in Prag und ein Standard-AVV machen Make für deutsche Unternehmen unkritisch. Die Abrechnung nach „Operations" (Aktionen pro Monat) ist beim Skalieren nicht immer vorhersehbar — Scenario-Design lohnt sich also.""",
    'features':"""- **Visual Scenario Builder** — Parallelzweige, Aggregatoren, Iteratoren.
- **2 000+ App-Integrationen** inklusive aller großen SaaS-Tools.
- **AI Modules** für OpenAI, Claude, Perplexity, Stability, ElevenLabs.
- **HTTP/Webhook/Custom-App-Builder** für eigene APIs.
- **Scheduler** mit komplexen Zeit- und Event-Triggern.
- **Error-Handling-Routes** für robuste Produktions-Workflows.
- **Make Template Library** mit vorgefertigten Szenarien.""",
    'pricing':"""- **Free** — 1 000 Operations / Monat, 2 aktive Scenarios.
- **Core** · $9 / Monat — 10 000 Operations, unlimited Scenarios.
- **Pro** · $16 / Monat — 10 000 Operations, Scheduling im Minuten-Takt.
- **Teams** · $29 / Monat — Team-Rollen, SSO.
- **Enterprise** · auf Anfrage — EU-Residenz, dedizierter Support.""",
},
# ---- Produktivität & Wissen ----
{
    'slug':'notebooklm', 'name':'NotebookLM', 'vendor':'Google', 'category':'produktivitaet',
    'tagline':'Wissens-Assistent über eigene Dokumente — mit erstaunlich guten Audio-Overviews.',
    'price':'Free (Plus ab €21,99/Mon.)', 'api':False, 'dsgvo':'bedingt', 'origin':'USA',
    'rating':4.6, 'reviews':1920,
    'pros':['Antworten mit Quellen-Anker','Audio Overview — KI-Podcast über Dokumente','Mindmap- und FAQ-Generierung','Großzügiger Free-Tier'],
    'cons':['Kein eigenständiges Schreib-Tool','Datenfluss zu Google','Keine Team-Kollaboration'],
    'usecases':['Literatur-Review','Team-Wiki-Zusammenfassung','Studien-Vorbereitung','Audio-Briefings'],
    'launched':'2023-07-12',
    'overview':"""**NotebookLM** ist Googles wohl unterschätztestes KI-Produkt — und seit dem Audio-Overview-Feature von Mitte 2024 eines der meistgeteilten. Das Prinzip ist einfach: Dokumente, PDFs, Webseiten, YouTube-Videos in ein „Notebook" laden, und Gemini 2.5 Pro beantwortet Fragen ausschließlich aus diesen Quellen — mit präzisen Quellenangaben pro Antwort.

Das virale Feature ist Audio Overview: Zwei KI-Hosts diskutieren in 10–20 Minuten die hochgeladenen Dokumente als Podcast. Klingt verblüffend natürlich, eignet sich perfekt für Commute-Vorbereitung vor Meetings oder als Briefing-Format.

Für Studierende, Wissenschaftler und Wissensarbeitende ist NotebookLM ein Produktivitäts-Game-Changer: Literatur-Review, Zusammenfassung von Team-Wikis, Vorbereitung auf Fachgespräche. Die Antworten sind grounded und fehleranfällig nur dort, wo auch die Quellen fehlerhaft sind. Was fehlt: Team-Kollaboration und API-Zugriff — Google baut NotebookLM bewusst als Verbraucher-Produkt.""",
    'features':"""- **Source-Grounded Answers** — Antworten nur aus hochgeladenen Quellen.
- **Audio Overview** — KI-Podcast über das Notebook (DE verfügbar).
- **Video Overview** (Beta) — bewegte Erklärvideos aus Quellen.
- **Mindmap-Generator** für visuelle Struktur.
- **FAQ- und Briefing-Dokumente** automatisch erstellen.
- **Multimodale Quellen** — PDFs, Docs, URLs, YouTube.
- **Unterstützt 35+ Sprachen** inklusive Deutsch.""",
    'pricing':"""- **NotebookLM Free** — 100 Sources pro Notebook, Audio Overviews begrenzt.
- **NotebookLM Plus** (Teil von Google AI Pro) · €21,99 / Monat — 5× Limits, Custom-Audio-Stile, Team-Freigaben.
- **NotebookLM Enterprise** via Google Cloud — Enterprise-Kontrollen.
- **Kostenloser Zugang für Bildungseinrichtungen** über Google Workspace for Education.""",
},
# ---- Daten & Analyse ----
{
    'slug':'julius', 'name':'Julius AI', 'vendor':'Julius AI Inc.', 'category':'daten-analyse',
    'tagline':'Conversational Data Analyst — CSVs, Excel, Datenbanken in natürlicher Sprache auswerten.',
    'price':'Freemium — Essential $20/Mon.', 'api':True, 'dsgvo':'bedingt', 'origin':'USA',
    'rating':4.5, 'reviews':420,
    'pros':['Schnelle Exploratory-Analyse','Auto-generierte Visualisierungen','Python-Notebook-Ausgabe','Connectors zu SQL, Snowflake, BigQuery'],
    'cons':['Kein EU-Hosting als Standard','Bei komplexer Statistik noch oberflächlich','Daten-Upload-Limits im Free-Tier'],
    'usecases':['Ad-hoc-Analysen','Marketing-Reporting','Scientific-Pre-Analyse','Dashboards prototypen'],
    'launched':'2022-12-01',
    'overview':"""**Julius AI** positioniert sich als konversationeller Datenanalyst für Nicht-Entwickler. Eine CSV-Datei, ein Excel-Export oder eine SQL-Verbindung werden hochgeladen — die Auswertung erfolgt dann über natürliche Sprache. „Zeig mir die Verteilung der Auftragswerte nach Region, als gestapeltes Balkendiagramm." Innerhalb von Sekunden erscheint die Analyse, inklusive des dahinterliegenden Python-Codes.

Das macht Julius für Marketing-, Sales- und Ops-Teams interessant, die selten tiefer in Datenquellen einsteigen, aber regelmäßig Auswertungen brauchen. Die generierten Charts sind sauber, der zugängliche Code-Output ermöglicht Datenwissenschaftlern eine Übernahme in produktive Notebooks.

Für tiefgehende Statistik und Modellierung ist das Tool nicht ausgelegt — dort brauchen Profis weiterhin eigene Notebooks oder BI-Spezialtools. Als Ergänzung in einer analytischen Toolchain, oder als niedrigschwelliger Einstieg für Fachabteilungen, ist Julius aber eine überraschend gute Lösung.""",
    'features':"""- **Chat-basierte Datenanalyse** mit Auto-Chart-Generierung.
- **Connectors** — CSV/Excel-Upload, Google Sheets, Snowflake, BigQuery, PostgreSQL.
- **Python-Notebook-Export** für reproduzierbare Analysen.
- **Forecast-Funktionen** für Zeitreihen.
- **PDF-/Image-Ingestion** — Charts aus PDFs extrahieren.
- **Workspace** mit Dashboards und geteilten Analysen.
- **API** für Pipeline-Integration.""",
    'pricing':"""- **Free** — 15 Messages / Tag, 2 MB File-Limit.
- **Essential** · $20 / Monat — unbegrenzte Nachrichten, 25 MB Files.
- **Plus** · $50 / Monat — 100 MB Files, erweitertes Reasoning.
- **Professional** · $150 / Monat — Priority, 500 MB Files.
- **Enterprise** — auf Anfrage mit SSO und DPA.""",
},
# ---- Marketing & Content ----
{
    'slug':'neuroflash', 'name':'Neuroflash', 'vendor':'Neuroflash GmbH', 'category':'marketing',
    'tagline':'Deutsches Content-Tool mit SEO-Fokus — Blogposts, Ads und Newsletter auf Knopfdruck.',
    'price':'Freemium — Basic €29/Mon.', 'api':False, 'dsgvo':'ja', 'origin':'EU (DE)',
    'rating':4.3, 'reviews':520,
    'pros':['Hamburger Anbieter, DSGVO-konform','Starke deutsche Sprachqualität','SEO-Analyse integriert','Brand-Voice-Training'],
    'cons':['Kleinere Funktionsbreite als Jasper','Qualitätssprung zu GPT-5 mitunter spürbar','Keine öffentliche API'],
    'usecases':['Blog-Content','Social-Media-Kampagnen','Newsletter','E-Commerce-Produktbeschreibungen'],
    'launched':'2021-03-01',
    'overview':"""**Neuroflash** aus Hamburg ist einer der seltenen deutschen Content-KI-Anbieter, die sich gegen die US-Konkurrenz mit Jasper und Copy.ai behaupten. Der Fokus liegt auf deutschsprachigem Marketing-Content: Blogposts, Werbetexte, Produktbeschreibungen, Newsletter — mit einer fein abgestimmten SEO-Integration.

Unternehmen können eine eigene Brand Voice trainieren — Neuroflash analysiert Beispieltexte und erzeugt danach konsistent im gewünschten Tonfall. Der integrierte „Performance Score" kombiniert Emotion- und Sentiment-Analyse, um Texte vor Veröffentlichung zu prüfen.

Für deutsche Marketing-Teams, die DSGVO-konforme KI brauchen und nicht auf die API-Nutzung von OpenAI direkt wechseln wollen, ist Neuroflash die nahelegende Adresse. Die reine Schreibqualität liegt unter dem, was Claude oder GPT-5 in deutscher Sprache leisten — die Branchen-Features (Keyword-Recherche, Content-Planer, Template-Bibliothek) kompensieren das für den Marketing-Einsatz.""",
    'features':"""- **Content Flash** für kurze Formate (Ads, Posts, Subject-Lines).
- **Blog Post Flash** mit strukturierter Artikel-Erstellung.
- **Performance Score** — Emotion- und Resonanz-Analyse pro Text.
- **SEO Analytics** mit Keyword-Recherche.
- **Brand Voice** aus Beispieltexten trainierbar.
- **90+ Text-Templates** für gängige Marketing-Formate.
- **DeepL-Translation** direkt integriert.""",
    'pricing':"""- **Free** — 2 000 Wörter / Monat, Basis-Templates.
- **Basic** · €29 / Monat — 30 000 Wörter, SEO-Features.
- **Power** · €59 / Monat — 100 000 Wörter, Brand Voice, Team-Features.
- **Premium** · €149 / Monat — unbegrenzte Wörter, 5 Users.
- **Business** · auf Anfrage — SSO, Audit-Logs, EU-DPA.""",
},
# ---- Wissenschaft & Forschung ----
{
    'slug':'elicit', 'name':'Elicit', 'vendor':'Elicit Research', 'category':'forschung',
    'tagline':'Literatur-Recherche in wissenschaftlichen Papers — automatisiertes Screening und Extraktion.',
    'price':'Freemium — Plus $12/Mon.', 'api':True, 'dsgvo':'bedingt', 'origin':'USA',
    'rating':4.5, 'reviews':380,
    'pros':['125 Mio. Papers durchsuchbar','Automatische Tabellen aus Papers','Ein-Klick-Summary pro Paper','Systematic-Review-Workflow'],
    'cons':['Stark englischsprachige Literatur','API im Aufbau','Kein EU-Hosting als Standard'],
    'usecases':['Systematic Reviews','Thesis-Recherche','Marktrecherche basierend auf Studien','Lit-Mapping'],
    'launched':'2021-10-01',
    'overview':"""**Elicit** ist eines der wenigen KI-Forschungs-Tools, das für die Wissenschafts-Community gebaut ist — und nicht umgekehrt. Der Kern ist eine Suche über 125 Millionen wissenschaftliche Papers, die nicht auf Keyword-Match basiert, sondern auf Bedeutungsähnlichkeit zu einer natürlichsprachigen Forschungsfrage.

Besonders wertvoll ist die strukturierte Extraktion: Elicit erstellt aus Dutzenden Papers eine Tabelle mit Studien-Design, Sample-Size, Outcome-Messungen und Haupt-Findings — eine Arbeit, die manuell Tage dauern würde. Für Systematic Reviews und Meta-Analysen ist das eine fundamentale Zeitersparnis.

Die Einschränkungen sind disziplinspezifisch: Die Paper-Basis ist englischsprachig und stark STEM-orientiert. Für Geistes- und Sozialwissenschaften ist die Abdeckung geringer. Auch deutsche Paper sind unterrepräsentiert. Für Forschende mit internationalem Scope — also die Mehrheit — ist Elicit derzeit das stärkste dedizierte Recherche-Tool.""",
    'features':"""- **Semantic Search** über 125 Mio. Papers aus Semantic Scholar.
- **Paper Summaries** pro Treffer mit Key Findings.
- **Extract Data** — strukturierte Tabellen aus mehreren Papers.
- **Systematic Review Workflow** mit Inclusion/Exclusion-Tracking.
- **Chat with PDFs** — direkte Frage-Antwort auf eigene Papers.
- **API & BibTeX-Export** für Reference-Manager.
- **Replication-Score** — automatische Einschätzung der Evidenz-Stärke.""",
    'pricing':"""- **Basic** · Free — 5 000 Credits zum Ausprobieren.
- **Plus** · $12 / Monat — 12 000 Credits / Monat.
- **Pro** · $49 / Monat — 30 000 Credits, erweiterte Features.
- **Enterprise** — auf Anfrage mit API-Zugang und Custom-Workflows.""",
},
]

# =====================================================================
# Seed: create one post per tool, then create tool element
# =====================================================================
today = time.strftime('%Y-%m-%d')
for t in TOOLS:
    if t['slug'] in existing_slugs:
        print(f'  · {t["slug"]} already exists, skipping')
        continue
    # 1. Create post
    post_payload = {
        'title': f'{t["name"]} — Übersicht',
        'content': t['overview'],
        'short_description': t['tagline'],
        'keywords': [t['vendor'], t['category']],
        'published': True,
        'locale': 'de',
    }
    r = requests.post(f'{BASE}/{SITE}/posts/',
        json=post_payload, headers=H, verify=False, timeout=60)
    if not r.ok:
        print(f'  ✗ {t["slug"]}: post create failed {r.status_code} {r.text[:200]}')
        continue
    post_id = r.json().get('id')

    # 2. Create tool element
    data = {
        'slug':         t['slug'],
        'name':         t['name'],
        'vendor':       t['vendor'],
        'category':     t['category'],
        'tagline':      t['tagline'],
        'price':        t['price'],
        'api':          t['api'],
        'dsgvo':        t['dsgvo'],
        'origin':       t['origin'],
        'rating':       t['rating'],
        'reviews':      t['reviews'],
        'pros':         t['pros'],
        'cons':         t['cons'],
        'usecases':     t['usecases'],
        'launched':     t['launched'],
        'lastUpdated':  today,
        'post_id':      post_id,
        'features':     t['features'],
        'pricing':      t['pricing'],
    }
    r = requests.post(f'{BASE}/{SITE}/elements/',
        json={'type_id': tool_ct['id'], 'data': data, 'published': True},
        headers=H, verify=False, timeout=60)
    if not r.ok:
        print(f'  ✗ {t["slug"]}: element create failed {r.status_code} {r.text[:200]}')
        continue
    print(f'  ✓ {t["slug"]:15}  post #{post_id:<4}  element #{r.json().get("id")}')

print(f'\n✓ Added {len(TOOLS)} tool entries (idempotent).')
