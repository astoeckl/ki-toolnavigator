#!/usr/bin/env python3
"""Seed 15 additional KI-Tool elements into the CMS.
Idempotent: skips slugs that already exist.

Run after this:
  scripts/upload_tool_logos.py        — fetches + uploads logos, sets logo_id
  scripts/capture_tool_screenshots.mjs — captures website screenshots
  scripts/upload_screenshots.py       — uploads screenshots, sets screenshot_id
  scripts/generate_tool_images.py     — Nano Banana cover illustrations, sets media_id
  scripts/seed_overviews_new.py       — overview Posts + post_id
  scripts/seed_features_pricing_new.py — features + pricing markdown
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
H = {'Authorization': f'Bearer {r.json()["access_token"]}', 'Content-Type':'application/json'}
print('✓ Logged in')

cts = requests.get(f'{BASE}/{SITE}/contenttypes/', headers=H, verify=False).json()
tool_ct = next(c for c in cts if c.get('display_identifier') == 'tool')

NEW_TOOLS = [
    {'slug':'ms-copilot','name':'Microsoft 365 Copilot','vendor':'Microsoft','category':'produktivitaet',
     'tagline':'KI-Assistent direkt in Word, Excel, Outlook, Teams und der gesamten Microsoft-365-Welt.',
     'price':'Ab €29,75 / Nutzer / Monat (Jahresvertrag)','api':False,'dsgvo':'bedingt','origin':'USA',
     'rating':4.2,'reviews':1820,
     'pros':['Tief in Microsoft 365 integriert','Daten verlassen den eigenen Tenant nicht','Enterprise-Compliance & Audit-Logs','Copilot Studio für eigene Agenten'],
     'cons':['Hoher Preis pro Sitz','Bestes Erlebnis nur mit Microsoft-Stack','Qualität schwankt je Office-App'],
     'usecases':['E-Mail-Drafting','Excel-Auswertung','Meeting-Zusammenfassung','Onboarding-FAQs'],
     'launched':'2023-11-01','lastUpdated':'2026-04-15'},
    {'slug':'grok','name':'Grok','vendor':'xAI','category':'sprachmodelle',
     'tagline':'Der unmittelbare X-integrierte Chatbot mit Echtzeit-Anbindung an die Plattform.',
     'price':'Freemium — Premium ab $40 / Mon. (X)','api':True,'dsgvo':'nein','origin':'USA',
     'rating':4.0,'reviews':610,
     'pros':['Live-Daten aus X (Twitter)','Schnelle Antworten','Kontextfenster wächst stark','Bild- und Reasoning-Modi'],
     'cons':['Datenschutz unklar','Stark an X-Konto gebunden','Wenig Enterprise-Funktionen'],
     'usecases':['Trend-Recherche','Witzige Texte','Live-Event-Analyse'],
     'launched':'2023-11-04','lastUpdated':'2026-04-09'},
    {'slug':'deepseek','name':'DeepSeek','vendor':'DeepSeek','category':'sprachmodelle',
     'tagline':'Quelloffenes chinesisches LLM mit beeindruckendem Reasoning bei niedrigen Token-Preisen.',
     'price':'API ab $0.14 / 1 M Token (V3)','api':True,'dsgvo':'nein','origin':'China',
     'rating':4.3,'reviews':1240,
     'pros':['Open-Weights-Modelle','Sehr günstige API','Starkes Reasoning (R1)','Aktive Community'],
     'cons':['Datenresidenz China problematisch','Inhaltliche Filterung nach chinesischen Vorgaben','Keine EU-Datenschutzgarantie'],
     'usecases':['Self-Hosting','Forschung','Code-Generierung','Kosten-sensitive APIs'],
     'launched':'2023-12-12','lastUpdated':'2026-03-29'},
    {'slug':'flux','name':'FLUX.1','vendor':'Black Forest Labs','category':'bildgenerierung',
     'tagline':'Europäisches Bildmodell aus Freiburg — fotorealistisch, controlnet-fähig, Open Weights.',
     'price':'Freemium · API ab $0.025 / Bild (Schnell)','api':True,'dsgvo':'ja','origin':'EU (DE)',
     'rating':4.5,'reviews':520,
     'pros':['Sehr gute Bildqualität','Verschiedene Lizenzstufen (Schnell/Dev/Pro)','EU-Anbieter','Stark bei Typografie und Händen'],
     'cons':['Keine native Plattform-UI','Teurere Pro-Variante','Community kleiner als bei SD'],
     'usecases':['Editorial','Marketing-Visuals','Realistische Porträts'],
     'launched':'2024-08-01','lastUpdated':'2026-04-12'},
    {'slug':'ideogram','name':'Ideogram','vendor':'Ideogram','category':'bildgenerierung',
     'tagline':'Bildgenerator mit Schwerpunkt auf lesbarer Typografie — Plakate, Logos, Memes.',
     'price':'Freemium — Plus ab $8 / Mon.','api':True,'dsgvo':'bedingt','origin':'USA',
     'rating':4.3,'reviews':380,
     'pros':['Beste Schrift-Generierung','Sehr saubere Layouts','Magic Prompt für Hilfe','Public Feed zur Inspiration'],
     'cons':['Weniger fotorealistisch','Style-Control teils begrenzt'],
     'usecases':['Plakate','Social-Media-Visuals','Logo-Konzepte','Karten & Cover'],
     'launched':'2023-08-23','lastUpdated':'2026-03-20'},
    {'slug':'adobe-firefly','name':'Adobe Firefly','vendor':'Adobe','category':'bildgenerierung',
     'tagline':'Kommerziell sicheres Bildmodell, integriert in Photoshop, Illustrator und Express.',
     'price':'Inklusive in Adobe Creative Cloud · Standalone ab $9,99','api':True,'dsgvo':'bedingt','origin':'USA',
     'rating':4.1,'reviews':2100,
     'pros':['Trainiert nur auf lizenzierten/eigenen Daten','In CC-Apps eingebaut','Generative Fill in Photoshop','Adobe-Compliance & Indemnification'],
     'cons':['Output stilistisch etwas konservativer','Nur mit CC-Konto sinnvoll'],
     'usecases':['Marketing-Assets','Stockfoto-Erweiterung','Designprozesse'],
     'launched':'2023-03-21','lastUpdated':'2026-04-08'},
    {'slug':'suno','name':'Suno','vendor':'Suno','category':'video-audio',
     'tagline':'Vollständige Songs (Vocals + Instrumente + Lyrics) per Prompt — beeindruckend gut.',
     'price':'Freemium — Pro ab $10 / Mon.','api':False,'dsgvo':'bedingt','origin':'USA',
     'rating':4.4,'reviews':1690,
     'pros':['Komplette Songs in Sekunden','Lyric-Steuerung','Custom-Style-Tags','Cover-Modus'],
     'cons':['Rechtsfragen rund um Trainingsdaten offen','Keine Mehrkanal-Stems im günstigsten Tarif','Keine API'],
     'usecases':['Jingles','Demo-Tracks','Soundtracks für Videos'],
     'launched':'2023-12-20','lastUpdated':'2026-04-02'},
    {'slug':'synthesia','name':'Synthesia','vendor':'Synthesia','category':'video-audio',
     'tagline':'Sprechende KI-Avatare für Schulungs- und Erklärvideos — komplett textbasiert produzieren.',
     'price':'Personal ab $29 / Mon. · Enterprise individuell','api':True,'dsgvo':'ja','origin':'EU (UK/DE)',
     'rating':4.5,'reviews':1230,
     'pros':['250+ Stock-Avatare in 140 Sprachen','Eigene Avatar-Klone möglich','SOC 2, GDPR, EU-Hosting','Templates & Branding'],
     'cons':['Keine emotionalen Gesichter','Begrenzte Bewegungs-Animationen','Höhere Tarife für Custom-Avatare'],
     'usecases':['Onboarding','E-Learning','Produkt-Walkthroughs','Compliance-Schulung'],
     'launched':'2017-06-01','lastUpdated':'2026-04-11'},
    {'slug':'windsurf','name':'Windsurf','vendor':'Codeium','category':'coding',
     'tagline':'Cascade-Agent-IDE auf VS-Code-Basis — Konkurrent von Cursor mit eigenem Modell-Stack.',
     'price':'Freemium — Pro ab $15 / Mon.','api':False,'dsgvo':'bedingt','origin':'USA',
     'rating':4.4,'reviews':780,
     'pros':['Cascade Agent Modus','Großzügiger Free-Tier','Gute Multi-Repo-Awareness','Eigene proprietäre Modelle (SWE-1)'],
     'cons':['Jüngere Marke','Pro-Limits ähnlich wie bei Cursor','Weniger Community-Plugins'],
     'usecases':['Agentic Coding','Refactorings','Pair-Programming-Ersatz'],
     'launched':'2024-11-01','lastUpdated':'2026-04-13'},
    {'slug':'n8n','name':'n8n','vendor':'n8n','category':'agenten',
     'tagline':'Open-Source-Workflow-Automation aus Berlin mit AI-Nodes für LangChain, OpenAI, Claude & Co.',
     'price':'Self-hosted kostenlos · Cloud ab €20 / Mon.','api':True,'dsgvo':'ja','origin':'EU (DE)',
     'rating':4.6,'reviews':1450,
     'pros':['Selbst hostbar (fair-code)','400+ Integrationen','Native AI-Agent-Nodes','Versionierbare JSON-Workflows'],
     'cons':['Steile Lernkurve am Anfang','Cloud-Tarife teurer als Self-Host','UI-Komplexität bei großen Flows'],
     'usecases':['LLM-Pipelines','RAG-Workflows','Datenintegration','Slack-/CRM-Bots'],
     'launched':'2019-10-01','lastUpdated':'2026-04-17'},
    {'slug':'make','name':'Make','vendor':'Make (Celonis)','category':'agenten',
     'tagline':'Visuelle Workflow-Automation mit AI-Modulen — der Nachfolger von Integromat.',
     'price':'Free 1.000 Ops · Pro ab $10,59 / Mon.','api':True,'dsgvo':'bedingt','origin':'EU (CZ)','rating':4.3,'reviews':2050,
     'pros':['Sehr visuelle Workflow-UI','1.500+ Apps','OpenAI/Anthropic/Mistral als Module','Skalierbar bis Enterprise'],
     'cons':['Operations-basiertes Pricing kann teuer werden','Komplexere Logik schwer zu debuggen'],
     'usecases':['Marketing-Automation','Lead-Routing','AI-Content-Pipelines'],
     'launched':'2016-02-01','lastUpdated':'2026-04-04'},
    {'slug':'notebooklm','name':'NotebookLM','vendor':'Google','category':'forschung',
     'tagline':'Quellen-gestützter Recherche-Assistent von Google — inkl. automatischer Audio-Übersichten.',
     'price':'Free · Plus ab $19,99 / Mon. (im AI-Pro-Abo)','api':False,'dsgvo':'bedingt','origin':'USA',
     'rating':4.6,'reviews':940,
     'pros':['Antworten ausschließlich aus eigenen Quellen','Audio-Overviews als Podcast','Unterstützt PDF, Docs, Slides, Web','Mind-Maps & Studienleitfäden'],
     'cons':['Keine Schnittstellen für Drittanwendungen','Quellen-Limit pro Notebook','Benötigt Google-Konto'],
     'usecases':['Literaturrecherche','Studienvorbereitung','Podcast-Skripte','Wissensorganisation'],
     'launched':'2023-07-12','lastUpdated':'2026-04-10'},
    {'slug':'julius','name':'Julius AI','vendor':'Julius','category':'daten-analyse',
     'tagline':'Datenanalyse, Statistik und Visualisierung im Chat — Excel, CSV, SQL.',
     'price':'Freemium — Standard ab $20 / Mon.','api':True,'dsgvo':'bedingt','origin':'USA',
     'rating':4.2,'reviews':430,
     'pros':['Direkte Excel-/CSV-Analyse','Automatische Charts','Code-Export (Python/R)','Statistische Tests im Dialog'],
     'cons':['Kein Self-Hosting','Sensible Daten landen in der Cloud','Pro-Modelle hinter teurerem Tarif'],
     'usecases':['Ad-hoc-Analyse','Berichts-Generierung','Schnelle Visualisierungen','BI für Nicht-Techniker'],
     'launched':'2023-06-15','lastUpdated':'2026-03-25'},
    {'slug':'neuroflash','name':'Neuroflash','vendor':'Neuroflash','category':'marketing',
     'tagline':'Hamburger AI-Copywriting-Plattform mit deutscher Sprache, SEO-Workflows und DSGVO-Hosting.',
     'price':'Free 2.000 Wörter · Pro ab €29 / Mon.','api':True,'dsgvo':'ja','origin':'EU (DE)',
     'rating':4.4,'reviews':390,
     'pros':['Auf deutsche Marketing-Texte zugeschnitten','EU-Server, ISO-zertifiziert','Performance-Score (KI-bewertet)','Markenbibliothek (Brand Hub)'],
     'cons':['Englische Outputs schwächer','Generische Long-Form-Texte','Konkurrenz aus den USA günstiger'],
     'usecases':['Newsletter','SEO-Texte','Werbeanzeigen','Produktbeschreibungen'],
     'launched':'2021-04-15','lastUpdated':'2026-03-30'},
    {'slug':'elicit','name':'Elicit','vendor':'Elicit','category':'forschung',
     'tagline':'KI-gestützter wissenschaftlicher Recherche-Assistent — Paper finden, extrahieren, vergleichen.',
     'price':'Freemium — Plus ab $12 / Mon.','api':True,'dsgvo':'bedingt','origin':'USA',
     'rating':4.5,'reviews':610,
     'pros':['200 M+ Paper indexiert','Spaltenweise Datenextraktion','Systematische Reviews per Workflow','Quellen-Treue dokumentiert'],
     'cons':['Schwerpunkt auf englischsprachiger Forschung','Pro-Modi für tiefe Analysen nötig','Keine SaaS-Bibliotheks-Integration'],
     'usecases':['Literaturreviews','Meta-Studien','Theorie-Vergleich','Studienkartierung'],
     'launched':'2020-09-01','lastUpdated':'2026-04-06'},
]

# Fetch existing
items, page = [], 1
while True:
    r = requests.get(f'{BASE}/{SITE}/elements/?type_id={tool_ct["id"]}&size=200&page={page}',
        headers=H, verify=False).json()
    items += r.get('items', [])
    if not r.get('has_next'): break
    page += 1
existing_slugs = {el['data'].get('slug') for el in items}
print(f'  · {len(existing_slugs)} existing tool slugs')

created = skipped = errored = 0
for tool in NEW_TOOLS:
    if tool['slug'] in existing_slugs:
        print(f'  · {tool["slug"]}: already exists, skipping')
        skipped += 1
        continue
    payload = {'type_id': tool_ct['id'], 'data': tool, 'published': True}
    r = requests.post(f'{BASE}/{SITE}/elements/', json=payload, headers=H, verify=False)
    if r.ok:
        created += 1
        print(f'  ✓ {tool["slug"]}: created (id={r.json().get("id")})')
    else:
        errored += 1
        print(f'  ✗ {tool["slug"]}: {r.status_code} {r.text[:200]}')

print(f'\n✓ Done — created {created}, skipped {skipped}, errored {errored}')
