#!/usr/bin/env python3
"""Seed 7 additional marketing-category tools end-to-end:
  - tool elements (slug, name, vendor, tagline, price, api, dsgvo, …)
  - inline `features` and `pricing` markdown
  - inline `website` URL
  - overview Posts + post_id reference
  - logo (Google favicon V2) → upload to Cognitor Media → logo_id

Idempotent on every step.
Asset pipelines that still need to run AFTER this script:
  scripts/capture_tool_screenshots.mjs   — adds website screenshots locally
  scripts/upload_screenshots.py          — uploads + sets screenshot_id
  scripts/generate_tool_images.py        — Nano Banana cover illustrations
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
    {'slug':'copy-ai','name':'Copy.ai','vendor':'Copy.ai','category':'marketing',
     'tagline':'Workflow-Plattform für Marketing- und Sales-Texte mit AI-Agenten und Templates.',
     'price':'Free 2.000 Wörter · Pro ab $49 / Mon.','api':True,'dsgvo':'bedingt','origin':'USA',
     'rating':4.0,'reviews':1620,
     'pros':['90+ vorgefertigte Workflows','Brand Voice mit Beispieltexten lernbar','GTM-Templates für Outbound','Multi-Player-Workspaces'],
     'cons':['UI ist überladen','Templates teils generisch','Premium-Modelle erst ab Pro','Engl. besser als DE'],
     'usecases':['Outbound-Sequenzen','Werbeanzeigen','Newsletter','Produkttexte'],
     'launched':'2020-10-01','lastUpdated':'2026-04-12',
     'website':'https://www.copy.ai/','domain':'copy.ai',
     'features':"""- **Workflows**: visuelle Pipelines, die mehrere AI-Steps zu einem Output verketten.
- **Brand Voice** lernt euren Ton aus 5–10 Referenztexten.
- **Sales Workflows** (Outbound, LinkedIn, ICP-Recherche) mit CRM-Anbindung.
- **Knowledge Base** für Produkt-/Markendokumente, durchsucht je Workflow.
- **Marketplace**: über 90 fertige Templates und Community-Workflows.
- **API & Webhooks** für Integration in n8n, Zapier, Make.""",
     'pricing':"""- **Free** — 2.000 Wörter / Monat, 1 Seat.
- **Starter** · $49 / Mon. — 5.000 Workflow-Credits, GPT-4-Klasse-Modelle.
- **Advanced** · $249 / Mon. — 75.000 Credits, 5 Seats, API-Zugriff.
- **Enterprise** · auf Anfrage — SSO, SOC 2, Custom-Workflows, dediziertes Onboarding.""",
     'overview':"""**Copy.ai** ist eine der ältesten AI-Copywriting-Plattformen am Markt — und hat sich vom reinen Text-Generator zur Workflow-Plattform für Marketing- und Sales-Teams gewandelt. Statt einzelner Prompts orchestriert man heute *Workflows*, die mehrere AI-Schritte mit eigenen Datenquellen verbinden.

Die Stärke liegt im Workflow-Editor: Über 90 vorgefertigte Pipelines reichen von Outbound-E-Mail-Sequenzen über Wettbewerbsanalysen bis zu Blog-Briefings. Jeder Schritt kann verschiedene Modelle nutzen, eigene Knowledge-Base-Quellen referenzieren und auf Variablen aus vorherigen Schritten zugreifen. Brand Voice lernt aus Referenzen — ein deutlicher Vorteil gegenüber generischen Prompt-UIs.

Die Schwächen folgen aus dem breiten Funktionsumfang: Die Oberfläche wirkt für Einsteiger überladen, Templates liefern oft mittelmäßige Erstentwürfe, und das Beste bekommt man erst ab dem Advanced-Tarif. Deutsche Texte sind brauchbar, englische Outputs aber spürbar besser.

Empfohlen für Marketing- und Sales-Teams, die wiederkehrende Content-Pipelines automatisieren wollen — nicht für gelegentliche Einzeltext-Erstellung."""},

    {'slug':'writesonic','name':'Writesonic','vendor':'Writesonic','category':'marketing',
     'tagline':'All-in-one-Plattform für AI-Content, SEO-Artikel und Chatbots — mit eigenem Suchindex Chatsonic.',
     'price':'Free Trial · Standard ab $20 / Mon.','api':True,'dsgvo':'bedingt','origin':'Indien/USA',
     'rating':4.1,'reviews':1340,
     'pros':['Sehr breite Vorlagen-Bibliothek','Chatsonic mit Web-Recherche','SEO-Modus mit SERP-Daten','Botsonic für eigene Knowledge-Bots'],
     'cons':['Qualität schwankt zwischen Funktionen','Bewertungs-Modul oberflächlich','Komplexer Pricing-Mix'],
     'usecases':['Lange SEO-Artikel','FAQ-Chatbots','Anzeigentexte','Newsletter'],
     'launched':'2020-12-01','lastUpdated':'2026-04-08',
     'website':'https://writesonic.com/','domain':'writesonic.com',
     'features':"""- **AI Article Writer 6**: SEO-optimierte Long-Form-Artikel inkl. Web-Recherche und SERP-Datenabgleich.
- **Chatsonic**: ChatGPT-Klon mit Echtzeit-Suche, Bildern, Voice-Input.
- **Botsonic**: No-Code-Chatbot-Builder auf eigenen Datenquellen.
- **Audiosonic** für Voice-over und Narration.
- **WordPress-Plugin** und **Shopify-Integration**.
- **API** für Bulk-Content-Generierung.""",
     'pricing':"""- **Free Trial** — 10.000 Wörter, alle Premium-Funktionen.
- **Individual** · $20 / Mon. — 100.000 hochwertige Wörter, 1 Seat.
- **Team** · $99 / Mon. — 1 Mio. Wörter, 5 Seats, Brand-Voice.
- **Agency** · $249 / Mon. — 4 Mio. Wörter, White-Label-Optionen.
- **Enterprise** · auf Anfrage — Custom-Limits, SSO, dedizierter Support.""",
     'overview':"""**Writesonic** ist eine der breitesten AI-Marketing-Plattformen — von Long-Form-SEO-Artikeln über Chatbots bis zur Stimmgenerierung in einer Oberfläche. Das macht den Anbieter zur attraktiven Allrounder-Wahl, schafft aber auch das typische Problem: Vieles ist *gut*, weniges ist *exzellent*.

Der **AI Article Writer 6** ist die Vorzeigefunktion: Er holt sich SERP-Daten zum Keyword, baut daraus eine Outline, schreibt den Artikel und liefert Meta-Description plus interne Verlinkungs-Vorschläge. Die Qualität ist für Mid-Funnel-SEO solide, lektoratswürdig bleibt der Output trotzdem. **Botsonic** ist eine eigene Stärke — ein verständlicher No-Code-Builder für Wissens-Chatbots, der ohne tiefes RAG-Setup nutzbar ist.

Schwächen: Die Bewertung von Texten (Performance-Score) ist oberflächlich, das Pricing-Modell ist mit Tarifen, Add-ons und Wort-Limits unübersichtlich, und manche Funktionen wirken eher angeklebt als integriert.

Empfohlen für Solo-Marketer und kleine Agenturen, die viele unterschiedliche Content-Formate aus einer Hand generieren wollen, ohne mehrere Tools zu abonnieren."""},

    {'slug':'surfer-seo','name':'Surfer','vendor':'Surfer','category':'marketing',
     'tagline':'SEO-Content-Optimierung mit AI: vom Keyword-Cluster über die Outline zum vollständigen, ranking-fähigen Artikel.',
     'price':'Essential ab $99 / Mon.','api':True,'dsgvo':'ja','origin':'EU (PL)',
     'rating':4.6,'reviews':2210,
     'pros':['Sehr starke On-Page-Empfehlungen (NLP-basiert)','Surfer AI schreibt komplette Artikel','Audit-Modus für bestehende Inhalte','EU-Anbieter aus Polen, DSGVO-konform'],
     'cons':['Höherer Einstiegspreis','Surfer AI verbraucht eigene Credits','Kein Free-Tier','Backend-API nur in höheren Tarifen'],
     'usecases':['Content-Briefings','SEO-Audits','Long-Form-Artikel','Topical-Maps'],
     'launched':'2017-01-01','lastUpdated':'2026-04-15',
     'website':'https://surferseo.com/','domain':'surferseo.com',
     'features':"""- **Content Editor** mit Echtzeit-Score basierend auf NLP-Analyse der Top-SERP-Konkurrenz.
- **Surfer AI**: Komplettartikel inkl. Outline, Internal Links und Schema in 20 Min.
- **Audit-Modul**: Vorschläge für vorhandene URLs (Keyword-Lücken, Meta, NLP).
- **Topical Map / Cluster**: ganze Themengruppen mit verlinkten Briefings planen.
- **Auto-Optimize** für WordPress, Webflow und Google Docs.
- **API** + Zapier-Integration für Bulk-Workflows.""",
     'pricing':"""- **Essential** · $99 / Mon. — 30 Artikel/Mon., Surfer-AI-Add-on optional.
- **Advanced** · $219 / Mon. — 100 Artikel, Audits, Topical Map.
- **Max** · $419 / Mon. — 360 Artikel, API, White-Label.
- **Enterprise** · auf Anfrage — Custom-Limits, SSO, SLA.
- **Surfer AI Add-on** — pro generiertem Komplettartikel ~ $19.""",
     'overview':"""**Surfer** ist seit Jahren der Goldstandard für **On-Page-SEO-Optimierung mit AI**. Das polnische Unternehmen kombiniert NLP-Analyse der Top-Suchergebnisse mit einem Editor, der live anzeigt, welche Keywords, Strukturen und Wörter ein Artikel braucht, um in einer bestimmten Suchposition realistisch ranken zu können.

Die jüngste Innovation **Surfer AI** schreibt ganze Artikel: Keyword rein, Tonalität wählen, 20 Minuten warten — heraus kommt ein 1.500–3.000-Wort-Artikel mit Outline, internen Links, Schema-Markup und passender Meta-Description. Die Ergebnisse sind erstaunlich brauchbar, bedürfen aber redaktioneller Politur. Im Vergleich zu generischen AI-Schreibern liegt der Vorteil in der NLP-Term-Coverage.

Das Audit-Modul ist die unterschätzte Stärke: Bestehende URLs werden gegen die SERP-Konkurrenz analysiert und konkrete Verbesserungsvorschläge geliefert. Das spart in Inhouse-SEO-Teams Stunden pro Woche.

Schwäche bleibt der Preis: Mit $99 Einstieg und Surfer-AI-Aufpreis pro Artikel ist das Tool für Solo-Blogger zu teuer. Empfohlen für Inhouse-SEO-Teams und Agenturen, die regelmäßig Content für Top-Rankings produzieren."""},

    {'slug':'frase','name':'Frase','vendor':'Frase','category':'marketing',
     'tagline':'AI-gestützte Content-Briefings, SERP-Analyse und Long-Form-Generierung für SEO-Teams.',
     'price':'Solo ab $15 / Mon. · Basic $45 / Mon.','api':True,'dsgvo':'bedingt','origin':'USA',
     'rating':4.4,'reviews':1180,
     'pros':['Sehr gutes Brief-Generator-Tool','SERP-Analyse mit Sub-Topics','Question-Mining aus PAA','API + Wordpress-Plugin'],
     'cons':['UI nicht so poliert wie Surfer','SEO-Outline manchmal flach','AI-Writer im Solo-Tarif limitiert'],
     'usecases':['Content-Briefings','Outlines','Q&A-Recherche','SEO-Updates'],
     'launched':'2017-04-01','lastUpdated':'2026-03-30',
     'website':'https://www.frase.io/','domain':'frase.io',
     'features':"""- **Content Briefs** in unter 5 Min. — komplette Outline, Topics, Statistiken aus den Top-20.
- **SERP-Analyse** mit Subtopic-Clustering und PAA-Fragen.
- **AI Writer** für Outlines, Intros, FAQs und Vollartikel.
- **Optimize**: Score-basiertes Editing wie bei Surfer.
- **Question-Insights**: Echte User-Fragen aus Reddit, Quora, PAA aggregiert.
- **API + WordPress-Plugin**.""",
     'pricing':"""- **Free Trial** — 5 Tage, 30 Briefs.
- **Solo** · $15 / Mon. — 4 Article Credits, 1 Seat.
- **Basic** · $45 / Mon. — 30 Article Credits, AI-Writer enthalten.
- **Team** · $115 / Mon. — Unlimited Articles, 3 Seats, Pro-Add-ons.
- **Add-on Pro** · ab $35 / Mon. — Unlimited AI Writer, Plagiarism, mehr Wettbewerber.""",
     'overview':"""**Frase** ist das pragmatischere Geschwister von Surfer — fokussiert auf den Workflow zwischen Briefing und Schreiben, nicht auf den glänzenden Score-Editor. Wer SEO-Briefings für Agenturen oder Inhouse-Teams in Serie erstellt, findet in Frase oft den schnelleren Weg.

Das **Brief-Tool** ist der Star: Keyword eingeben, fünf Minuten warten, fertiger 2-Pager mit Outline, Sub-Topics, Statistiken und Frage-Sammlung aus People-Also-Ask. Diese Briefs lassen sich direkt an Freelancer schicken oder in Frase als Schreibumgebung weiterverarbeiten. **Question-Insights** aggregiert echte Fragen aus Reddit, Quora und Foren — eine Funktion, die andere Tools so nicht haben.

Der **AI Writer** ist solide, erreicht aber nicht die Outline-Präzision von Surfer AI. Das Optimize-Modul mit Score-basiertem Feedback existiert, ist aber spürbar weniger ausgereift. Insgesamt fehlt der UI etwas Politur — Funktionalität geht vor Design.

Empfohlen für Content-Agenturen und Inhouse-Redaktionen, die schnelle, gute Briefings brauchen und die eigentliche Schreibarbeit oft an Freelancer auslagern. Preislich der zugänglichste SEO-AI-Allrounder."""},

    {'slug':'anyword','name':'Anyword','vendor':'Anyword','category':'marketing',
     'tagline':'Performance-getriebenes AI-Copywriting mit eigenem Predictive-Score, der Conversion-Wahrscheinlichkeit schätzt.',
     'price':'Starter ab $39 / Mon.','api':True,'dsgvo':'bedingt','origin':'USA',
     'rating':4.3,'reviews':940,
     'pros':['Predictive Performance Score','Brand-Voice mit Tone-Lock','Channel-spezifische Optimierung','Direkte Ad-Plattform-Integration'],
     'cons':['Höherer Einstiegspreis','Score-Methodik nicht 100 % transparent','Beste Ergebnisse erst nach Brand-Training'],
     'usecases':['Performance-Ads','Landing-Page-Copy','E-Mail-Subject-Lines','A/B-Test-Varianten'],
     'launched':'2013-01-01','lastUpdated':'2026-04-10',
     'website':'https://anyword.com/','domain':'anyword.com',
     'features':"""- **Predictive Performance Score** trainiert auf Anyword-Performance-Daten von Mio. Anzeigen.
- **Brand Voice** + **Custom Audience Profiles** für mehrere Personas.
- **Channel-Optimierung**: Google Ads, Meta, LinkedIn, TikTok mit eigenen Best-Practices.
- **Continuous Optimization**: bestehender Copy wird laufend gegen aktuelle Daten gemessen.
- **Anyword Web Optimizer** für Landing-Pages.
- **Integrationen**: HubSpot, Marketo, Zapier, Drift.""",
     'pricing':"""- **Free Trial** — 7 Tage, 1.000 Wörter.
- **Starter** · $39 / Mon. — Brand Voice, Score, 3 Channels.
- **Data-Driven** · $79 / Mon. — alle Channels, A/B-Test-Generator.
- **Business** · $349 / Mon. — Custom Audiences, Web Optimizer, 3 Seats.
- **Enterprise** · auf Anfrage — SSO, dediziertes Onboarding, eigene Modelle.""",
     'overview':"""**Anyword** spielt in einer eigenen Liga: Statt nur "guten" Marketing-Text zu generieren, sagt das Tool für jede Variante eine **Performance-Wahrscheinlichkeit** voraus — basierend auf einem proprietären Modell, das auf Millionen tatsächlich geschalteter Anzeigen trainiert wurde. Das ist der wichtigste Unterschied zu Copy.ai, Writesonic oder Jasper.

Wer regelmäßig **Performance-Marketing** betreibt — Google Ads, Meta, LinkedIn, TikTok — bekommt mit Anyword ein Werkzeug, das nicht "schöne Texte" liefert, sondern Texte mit einer konkreten Vorhersage, ob sie funktionieren. Brand Voice und Custom-Audience-Profile schärfen das Output für eigene Personas. Der **Web Optimizer** geht einen Schritt weiter und A/B-testet kontinuierlich Live-Landing-Pages.

Die Schwäche: Das Score-Modell ist eine Black Box — niemand kann wirklich nachvollziehen, warum eine Variante 87 % bekommt und eine andere 62 %. Erfahrungen variieren je nach Branche, und für tiefe Brand-Wirkung sind 2–3 Wochen Eingewöhnung nötig.

Empfohlen für Performance-Marketing-Teams in B2C-Skaleups, die wirklich Conversion-Daten haben, an denen sie das Tool messen können. Für reine Inhalts-Erstellung ohne Performance-Anspruch zu teuer."""},

    {'slug':'jasper-brand','name':'Typeface','vendor':'Typeface','category':'marketing',
     'tagline':'Enterprise-Plattform für markenkonsistente Generative-AI-Inhalte — Text, Bild und Templates aus dem eigenen Brand-DNA-Modell.',
     'price':'Auf Anfrage (Enterprise)','api':True,'dsgvo':'bedingt','origin':'USA',
     'rating':4.4,'reviews':210,
     'pros':['Brand-DNA-Modell aus Style-Guide trainiert','Vereint Text + Bild in einem Workflow','Tiefe Integrationen (Adobe, Figma, Microsoft 365)','Enterprise-Kontrollen (SOC 2, SSO, RBAC)'],
     'cons':['Nur für Enterprise relevant','Kein öffentliches Pricing','Onboarding mehrwöchig','Setup-Kosten erheblich'],
     'usecases':['Brand-Konsistenz im Konzern','Multi-Channel-Kampagnen','Approval-Workflows','Asset-Management'],
     'launched':'2022-09-01','lastUpdated':'2026-04-05',
     'website':'https://www.typeface.ai/','domain':'typeface.ai',
     'features':"""- **Brand DNA Engine** trainiert auf Style-Guide, Tonalität, Bildwelt und gesperrten Wörtern.
- **Affinities** speichern Persona-, Produkt- und Kanal-Profile.
- **Multimodal Workflows**: Text, Bild und Template in einem Lauf.
- **Approval & Governance** mit RBAC, Audit-Logs, Versionierung.
- **Integrationen**: Microsoft 365, Adobe Express, Figma, Sitecore, Salesforce.
- **AI Studio** für Custom-Workflows pro Team.""",
     'pricing':"""- Kein öffentliches Pricing. Enterprise-Vertrag mit jährlicher Lizenz.
- Typische Einstiegspakete: 25–100 Seats.
- Setup-Onboarding (2–6 Wochen) bepreist gesondert.
- Kostenmodell oft hybrid: Plattform-Lizenz + nutzungsbasierte Generierungs-Credits.
- Pilot-Phase mit 1–2 Use-Cases empfohlen.""",
     'overview':"""**Typeface** ist die Antwort auf das größte Problem von Generative-AI im Enterprise-Marketing: **Markenkonsistenz**. Während die meisten Tools generische Texte liefern, trainiert Typeface ein Brand-DNA-Modell aus dem eigenen Style-Guide, der Tonalität, der Bildwelt und expliziten Wort-Sperren — und nutzt dieses Modell für jede einzelne Generierung.

Das Tool versteht sich als **Workflow-Plattform**, nicht als Editor. Marketing-Operations-Teams definieren Affinities (Persona, Produkt, Kanal), legen Templates an und übergeben sie ihren Stakeholdern. Output kann Text, Bild oder kombinierte Assets sein — alles aus einem Lauf, mit Approval-Workflow und Audit-Trail.

Die **Integrationen** sind der wahre USP: Microsoft 365, Adobe Express, Figma, Sitecore, Salesforce, HubSpot. Inhalte entstehen dort, wo Teams ohnehin arbeiten, statt in einem isolierten Tool. SOC-2-Compliance, SSO und granulare Rollenrechte sind Standard.

Die Schattenseite: Pricing ist intransparent, das Onboarding dauert Wochen, und die Plattform lohnt sich erst ab 25–50 aktiven Nutzern. Für Mittelstands-Marketing zu schwer, für Konzern-Marketing oft *die* richtige Wahl."""},

    {'slug':'canva-magic','name':'Canva Magic Studio','vendor':'Canva','category':'marketing',
     'tagline':'AI-Suite innerhalb von Canva: Magic Write, Magic Design, Magic Edit und Magic Switch im Designer-Workflow.',
     'price':'Free · Pro ab €11,99 / Mon.','api':False,'dsgvo':'ja','origin':'Australien',
     'rating':4.7,'reviews':5320,
     'pros':['AI dort, wo Marken-Assets ohnehin entstehen','Sehr breite Vorlagen-Bibliothek','Magic Edit für Bild-Inpainting','Brand Kit + Brand Voice für Marken'],
     'cons':['Stärke vor allem im Design, weniger im Long-Form','Magic-Funktionen erst ab Pro','Wenig Output-Format-Granularität','Keine echte API'],
     'usecases':['Social-Media-Visuals','Präsentationen','Anzeigen-Sets','Marketing-One-Pager'],
     'launched':'2023-10-01','lastUpdated':'2026-04-18',
     'website':'https://www.canva.com/magic/','domain':'canva.com',
     'features':"""- **Magic Write**: AI-Texte direkt im Layout (Slogans, Captions, Body).
- **Magic Design**: Layout-Vorschläge aus Prompt + Brand Kit.
- **Magic Edit / Eraser**: AI-Inpainting in Fotos.
- **Magic Switch**: Layout in andere Format-Sets übersetzen (Story → Post → Banner).
- **Magic Media**: Bilder, Videos und Grafiken aus Text generieren.
- **Brand Kit + Brand Voice** für konsistente Outputs.""",
     'pricing':"""- **Free** — Magic-Funktionen mit Tageslimits.
- **Canva Pro** · €11,99 / Mon. — alle Magic-Funktionen, 1 TB Cloud-Speicher.
- **Canva Teams** · €10 / Mon. / Seat (min. 3) — Brand Kit, Approval-Flows.
- **Canva Enterprise** · auf Anfrage — SSO, Brand Templates, Asset-Library, dedizierter CSM.
- **Education** und **NPO** kostenlos für berechtigte Organisationen.""",
     'overview':"""**Canva Magic Studio** macht Generative-AI dort verfügbar, wo bei vielen Marketing-Teams ohnehin die Marken-Assets entstehen — direkt im Canva-Editor. Diese Nähe zum Workflow ist der entscheidende Vorteil: Statt zwischen Texter, Bildgenerator und Layout-Tool zu wechseln, läuft alles in einer Oberfläche.

**Magic Design** generiert komplette Layout-Vorschläge aus einem Prompt und dem Brand Kit. **Magic Switch** übersetzt einen Post zwischen Story, Reel, Banner und Print in einem Klick. **Magic Edit** ist ein erstaunlich gutes Inpainting-Werkzeug für Fotos. Und **Magic Write** liefert die Texte gleich im Layout — keine Copy-Paste-Strecken zwischen Tools.

Schwächen: Long-Form-Texte sind nicht das Ziel — wer einen 2.000-Wort-Artikel braucht, ist mit Surfer oder Writesonic besser bedient. Magic-Funktionen haben Tagesquoten, die sich erst mit Pro merklich öffnen. Eine echte API gibt es nicht; Skalierung läuft über die UI.

Empfohlen für Marketing-Teams in KMU und Agenturen, die schnelle visuelle Marken-Assets brauchen — und für alle, die ohnehin bereits Canva-Kunden sind. Kaum eine andere Plattform integriert AI so nahtlos in den täglichen Designer-Workflow."""},
]

DOMAINS = {t['slug']: t['domain'] for t in TOOLS}

# ---- Login ----
r = requests.post(f'{BASE}/auth/login',
    data={'grant_type':'password','username':ENV['EMAIL'],'password':ENV['PW']},
    headers={'Content-Type':'application/x-www-form-urlencoded'}, verify=False)
H = {'Authorization': f'Bearer {r.json()["access_token"]}'}
JH = {**H, 'Content-Type':'application/json'}
print('✓ Logged in')

# ---- Find tool content type ----
cts = requests.get(f'{BASE}/{SITE}/contenttypes/', headers=JH, verify=False).json()
tool_ct = next(c for c in cts if c.get('display_identifier') == 'tool')
TOOL_CT_ID = tool_ct['id']

# ---- Fetch existing tool elements ----
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

LOGOS_DIR = ROOT / 'logos'
LOGOS_DIR.mkdir(exist_ok=True)

for tool in TOOLS:
    slug = tool['slug']
    overview = tool.pop('overview')
    domain = tool.pop('domain')

    # ---- Step 1: create or get tool element ----
    el = existing_by_slug.get(slug)
    if el:
        print(f'\n· {slug}: exists (id={el["id"]})')
        existing_data = el['data']
    else:
        # Create with base data (without media refs / overview-post yet)
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

    # ---- Step 2: ensure features + pricing + website ----
    for k in ('features', 'pricing', 'website'):
        if not existing_data.get(k) and tool.get(k):
            patches[k] = tool[k]

    # ---- Step 3: overview post ----
    if not (isinstance(existing_data.get('post_id'), int) or
            (isinstance(existing_data.get('post_id'), dict) and existing_data['post_id'].get('content'))):
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
        else:
            print(f'  ✗ post create failed: {r.status_code} {r.text[:200]}')

    # ---- Step 4: logo ----
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
            else:
                print(f'  ✗ logo upload failed: {rl.status_code}')
        except Exception as e:
            print(f'  ✗ logo fetch failed: {e}')

    # ---- Step 5: apply patches ----
    if patches:
        new_data = {**existing_data, **patches}
        # Strip resolved Post object if present (we patch only id)
        if isinstance(new_data.get('post_id'), dict):
            new_data['post_id'] = patches.get('post_id', existing_data.get('post_id'))
        r = requests.patch(f'{BASE}/{SITE}/elements/{el["id"]}',
            json={'data': new_data}, headers=JH, verify=False)
        if r.ok:
            print(f'  ✓ patched fields: {list(patches.keys())}')
        else:
            print(f'  ✗ patch failed: {r.status_code} {r.text[:200]}')

print('\n✓ Done. Next: capture_tool_screenshots.mjs → upload_screenshots.py → generate_tool_images.py')
