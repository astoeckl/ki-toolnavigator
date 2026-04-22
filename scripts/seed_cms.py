#!/usr/bin/env python3
"""Seed Cognitor CMS with KI-Toolnavigator content types + initial data."""
import os, sys, json, requests, urllib3
from pathlib import Path

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

ROOT = Path(__file__).resolve().parent.parent
ENV = {}
for line in (ROOT / '.env').read_text().splitlines():
    if '=' in line and not line.strip().startswith('#'):
        k, v = line.split('=', 1)
        ENV[k.strip()] = v.strip()

BASE = ENV['BASEURL']
SITE = ENV['SITE']

def login():
    r = requests.post(f'{BASE}/auth/login',
        data={'grant_type':'password','username':ENV['EMAIL'],'password':ENV['PW']},
        headers={'Content-Type':'application/x-www-form-urlencoded'}, verify=False)
    r.raise_for_status()
    return r.json()['access_token']

TOKEN = login()
H = {'Authorization': f'Bearer {TOKEN}', 'Content-Type': 'application/json'}
print(f'✓ Logged in')

# ---------- Content type schemas ----------
SCHEMAS = {
    'category': {
        'name': 'Kategorie',
        'identifier': 'category',
        'description': 'Tool-Kategorie im KI-Toolnavigator',
        'schema': {
            'type': 'object',
            'properties': {
                'slug':  {'type': 'string', 'title': 'Slug'},
                'name':  {'type': 'string', 'title': 'Name'},
                'count': {'type': 'integer', 'title': 'Anzahl Tools'},
                'desc':  {'type': 'string', 'title': 'Beschreibung'},
                'order': {'type': 'integer', 'title': 'Sortierung'},
            },
            'required': ['slug', 'name'],
        },
    },
    'tool': {
        'name': 'KI-Tool',
        'identifier': 'tool',
        'description': 'KI-Tool-Eintrag mit Steckbrief',
        'schema': {
            'type': 'object',
            'properties': {
                'slug':        {'type': 'string', 'title': 'Slug'},
                'name':        {'type': 'string', 'title': 'Name'},
                'vendor':      {'type': 'string', 'title': 'Anbieter'},
                'category':    {'type': 'string', 'title': 'Kategorie-Slug'},
                'tagline':     {'type': 'string', 'title': 'Tagline'},
                'price':       {'type': 'string', 'title': 'Preis'},
                'api':         {'type': 'boolean', 'title': 'API verfügbar'},
                'dsgvo':       {'type': 'string', 'title': 'DSGVO-Status', 'enum': ['ja','bedingt','nein']},
                'origin':      {'type': 'string', 'title': 'Herkunft'},
                'rating':      {'type': 'number', 'title': 'Bewertung'},
                'reviews':     {'type': 'integer', 'title': 'Anzahl Bewertungen'},
                'pros':        {'type': 'array', 'title': 'Pro-Argumente', 'items': {'type': 'string'}},
                'cons':        {'type': 'array', 'title': 'Contra-Argumente', 'items': {'type': 'string'}},
                'usecases':    {'type': 'array', 'title': 'Anwendungsfälle', 'items': {'type': 'string'}},
                'launched':    {'type': 'string', 'title': 'Launch-Datum'},
                'lastUpdated': {'type': 'string', 'title': 'Zuletzt aktualisiert'},
            },
            'required': ['slug','name','vendor','category'],
        },
    },
    'article': {
        'name': 'Artikel',
        'identifier': 'article',
        'description': 'Redaktioneller Artikel im Wiki-Stil',
        'schema': {
            'type': 'object',
            'properties': {
                'slug':     {'type': 'string', 'title': 'Slug'},
                'title':    {'type': 'string', 'title': 'Titel'},
                'category': {'type': 'string', 'title': 'Rubrik'},
                'author':   {'type': 'string', 'title': 'Autor'},
                'date':     {'type': 'string', 'title': 'Datum'},
                'readTime': {'type': 'integer', 'title': 'Lesezeit (Min.)'},
                'toc':      {'type': 'array', 'title': 'Inhaltsverzeichnis', 'items': {'type': 'string'}},
            },
            'required': ['slug','title'],
        },
    },
    'recent-change': {
        'name': 'Letzte Änderung',
        'identifier': 'recent-change',
        'description': 'Eintrag im "Letzte Änderungen"-Feed',
        'schema': {
            'type': 'object',
            'properties': {
                'time':   {'type': 'string', 'title': 'Zeitangabe'},
                'user':   {'type': 'string', 'title': 'Benutzer'},
                'action': {'type': 'string', 'title': 'Aktion'},
                'target': {'type': 'string', 'title': 'Betroffenes Objekt'},
                'detail': {'type': 'string', 'title': 'Detail'},
                'order':  {'type': 'integer', 'title': 'Reihenfolge'},
            },
            'required': ['time','user','action','target'],
        },
    },
}

# ---------- Create content types ----------
existing = requests.get(f'{BASE}/{SITE}/contenttypes/', headers=H, verify=False).json()
existing_ids = {ct['identifier']: ct['id'] for ct in existing}
ct_ids = {}
for key, spec in SCHEMAS.items():
    if key in existing_ids:
        ct_ids[key] = existing_ids[key]
        print(f'  · content type "{key}" already exists (id={existing_ids[key]})')
    else:
        r = requests.post(f'{BASE}/{SITE}/contenttypes/', json=spec, headers=H, verify=False)
        if not r.ok:
            print(f'  ✗ failed to create {key}: {r.status_code} {r.text[:300]}')
            sys.exit(1)
        ct_ids[key] = r.json()['id']
        print(f'  ✓ created content type "{key}" (id={ct_ids[key]})')

# ---------- Seed data (mirrors design/ki-toolnavigator/project/data.js) ----------
DATA = {
    'category': [
        {'slug':'sprachmodelle',    'name':'Sprachmodelle & Chat',    'count':47, 'desc':'Allgemeine LLMs und Chat-Assistenten für Text, Recherche und Analyse.', 'order':1},
        {'slug':'bildgenerierung',  'name':'Bildgenerierung',         'count':34, 'desc':'Text-zu-Bild, Stilübertragung und generative Bildbearbeitung.', 'order':2},
        {'slug':'video-audio',      'name':'Video & Audio',           'count':28, 'desc':'Video-Synthese, Stimmklonung, Musik und Transkription.', 'order':3},
        {'slug':'coding',           'name':'Coding-Assistenten',      'count':22, 'desc':'KI-gestützte Entwicklungsumgebungen, Copiloten und Code-Review.', 'order':4},
        {'slug':'agenten',          'name':'Agenten & Automation',    'count':19, 'desc':'Autonome Agenten, Workflow-Automation und Orchestrierung.', 'order':5},
        {'slug':'produktivitaet',   'name':'Produktivität & Wissen',  'count':41, 'desc':'Notizen, Zusammenfassung, Wissensmanagement, Meetings.', 'order':6},
        {'slug':'daten-analyse',    'name':'Daten & Analyse',         'count':17, 'desc':'SQL-Assistenten, BI-Agenten, automatisierte Auswertung.', 'order':7},
        {'slug':'marketing',        'name':'Marketing & Content',     'count':33, 'desc':'Copywriting, SEO, Social-Media, Ad-Creative.', 'order':8},
        {'slug':'forschung',        'name':'Wissenschaft & Forschung','count':12, 'desc':'Literaturrecherche, wissenschaftliches Schreiben, Zitation.', 'order':9},
    ],
    'tool': [
        {'slug':'chatgpt','name':'ChatGPT','vendor':'OpenAI','category':'sprachmodelle',
         'tagline':'Der bekannteste KI-Assistent für Dialog, Recherche und Textarbeit.',
         'price':'Freemium — Plus $20/Mon.','api':True,'dsgvo':'bedingt','origin':'USA',
         'rating':4.6,'reviews':2841,
         'pros':['Größtes Ökosystem','Multimodal (Bild, Stimme, Dateien)','Custom GPTs & Store','Breite API-Verfügbarkeit'],
         'cons':['Datenverarbeitung außerhalb EU','Kontext-Limit in Plus-Tarif','Halluziniert bei Nischenfragen'],
         'usecases':['Recherche','Entwurf','Code-Review','Übersetzung','Brainstorming'],
         'launched':'2022-11-30','lastUpdated':'2026-03-12'},
        {'slug':'claude','name':'Claude','vendor':'Anthropic','category':'sprachmodelle',
         'tagline':'Sprachmodell mit Fokus auf lange Kontexte, Sorgfalt und nuancierte Texte.',
         'price':'Freemium — Pro $20/Mon.','api':True,'dsgvo':'bedingt','origin':'USA',
         'rating':4.7,'reviews':1420,
         'pros':['200k+ Kontextfenster','Sehr gute Schreibqualität','Artifacts für interaktive Ausgaben','Projects für Wissenssammlungen'],
         'cons':['Kleineres Ökosystem','Weniger Plugins','Keine native Bildgenerierung'],
         'usecases':['Langtext-Analyse','Redaktion','Recherche','Prototyping'],
         'launched':'2023-03-14','lastUpdated':'2026-04-02'},
        {'slug':'gemini','name':'Gemini','vendor':'Google','category':'sprachmodelle',
         'tagline':'Googles multimodales Modell, tief in Workspace und Suche integriert.',
         'price':'Freemium — Advanced €21,99/Mon.','api':True,'dsgvo':'bedingt','origin':'USA',
         'rating':4.3,'reviews':1987,
         'pros':['Integration in Gmail/Docs','Sehr großes Kontextfenster','Starke Recherche-Features','Multimodal'],
         'cons':['Qualität schwankt zwischen Modellen','Europäische Features teils eingeschränkt'],
         'usecases':['Google-Workspace-Nutzer','Recherche','Meeting-Zusammenfassung'],
         'launched':'2023-12-06','lastUpdated':'2026-03-28'},
        {'slug':'mistral','name':'Le Chat','vendor':'Mistral AI','category':'sprachmodelle',
         'tagline':'Europäisches LLM aus Paris — schnell, offen, DSGVO-freundlich.',
         'price':'Freemium — Pro €14,99/Mon.','api':True,'dsgvo':'ja','origin':'EU (FR)',
         'rating':4.4,'reviews':612,
         'pros':['EU-Datenverarbeitung','Open-Source-Modelle verfügbar','Sehr schnelle Inferenz','Faire Preise'],
         'cons':['Kleineres Ökosystem','Weniger Integrationen','Weniger multimodal'],
         'usecases':['EU-Compliance','Self-Hosting','Chat','Coding'],
         'launched':'2024-02-26','lastUpdated':'2026-04-08'},
        {'slug':'midjourney','name':'Midjourney','vendor':'Midjourney Inc.','category':'bildgenerierung',
         'tagline':'Der Industriestandard für ästhetische Bildgenerierung.',
         'price':'Ab $10/Mon.','api':False,'dsgvo':'nein','origin':'USA',
         'rating':4.5,'reviews':3210,
         'pros':['Ausgezeichnete Bildqualität','Starke Community','Style References (--sref)'],
         'cons':['Keine öffentliche API','Discord- und Web-only','Rechtliche Grauzone'],
         'usecases':['Konzeptkunst','Mood-Boards','Editorial','Ideation'],
         'launched':'2022-07-12','lastUpdated':'2026-03-15'},
        {'slug':'stable-diffusion','name':'Stable Diffusion','vendor':'Stability AI','category':'bildgenerierung',
         'tagline':'Offenes Bildmodell — lokal lauffähig, voll anpassbar.',
         'price':'Open Source / API ab $0.01','api':True,'dsgvo':'ja','origin':'UK/DE',
         'rating':4.2,'reviews':1540,
         'pros':['Open Source','Lokal nutzbar','Riesige Modell-Community','LoRA-Feintuning'],
         'cons':['Setup anspruchsvoll','Qualität hängt vom Modell ab'],
         'usecases':['Lokale Generierung','Feintuning','Batch-Produktion'],
         'launched':'2022-08-22','lastUpdated':'2026-02-19'},
        {'slug':'elevenlabs','name':'ElevenLabs','vendor':'ElevenLabs','category':'video-audio',
         'tagline':'Realistische Stimmsynthese und Voice-Cloning in 30+ Sprachen.',
         'price':'Freemium — Starter $5/Mon.','api':True,'dsgvo':'bedingt','origin':'USA/PL',
         'rating':4.7,'reviews':892,
         'pros':['Beste Stimmqualität am Markt','Sehr schnelle Generierung','Mehrsprachig'],
         'cons':['Missbrauchspotenzial','Teurer bei Volumen'],
         'usecases':['Podcasts','Hörbücher','Lokalisierung','Voice-Over'],
         'launched':'2022-11-01','lastUpdated':'2026-04-01'},
        {'slug':'runway','name':'Runway','vendor':'Runway ML','category':'video-audio',
         'tagline':'Text-zu-Video und Video-Bearbeitung mit KI — Gen-3 und neuer.',
         'price':'Freemium — Standard $15/Mon.','api':True,'dsgvo':'nein','origin':'USA',
         'rating':4.3,'reviews':745,
         'pros':['Führend bei Text-zu-Video','Intuitive Oberfläche','Viele Effekte'],
         'cons':['Credits schnell aufgebraucht','Längen begrenzt'],
         'usecases':['Musikvideos','Werbung','Prototyping'],
         'launched':'2018-11-01','lastUpdated':'2026-03-22'},
        {'slug':'cursor','name':'Cursor','vendor':'Anysphere','category':'coding',
         'tagline':'KI-native IDE auf VS-Code-Basis — Code schreiben im Dialog.',
         'price':'Freemium — Pro $20/Mon.','api':False,'dsgvo':'bedingt','origin':'USA',
         'rating':4.6,'reviews':1203,
         'pros':['Vollwertige IDE','Composer für Multi-File-Edits','Eigenes Modell-Routing','Tab-Vervollständigung stark'],
         'cons':['Pro-Limits spürbar','Komplexität für Einsteiger'],
         'usecases':['Tägliche Entwicklung','Refactoring','Prototyping'],
         'launched':'2023-03-01','lastUpdated':'2026-04-10'},
        {'slug':'copilot','name':'GitHub Copilot','vendor':'GitHub/Microsoft','category':'coding',
         'tagline':'Der Pionier der KI-Code-Vervollständigung — jetzt mit Agent-Modus.',
         'price':'Ab $10/Mon.','api':False,'dsgvo':'bedingt','origin':'USA',
         'rating':4.4,'reviews':2198,
         'pros':['Tiefe GitHub-Integration','Alle großen IDEs','Chat + Agent'],
         'cons':['Kontext kleiner als Cursor','Enterprise-Preise'],
         'usecases':['IDE-Autocomplete','PR-Reviews','Tests'],
         'launched':'2021-10-29','lastUpdated':'2026-03-30'},
        {'slug':'notion-ai','name':'Notion AI','vendor':'Notion Labs','category':'produktivitaet',
         'tagline':'KI-Features direkt im Notion-Workspace — Q&A über alle Seiten.',
         'price':'$10/Mon. Add-on','api':False,'dsgvo':'bedingt','origin':'USA',
         'rating':4.2,'reviews':980,
         'pros':['Nahtlos in Notion','Q&A über Workspace','Schreiben im Kontext'],
         'cons':['Nur für Notion-Nutzer','Eingeschränkt ohne Notion-Daten'],
         'usecases':['Team-Wiki','Zusammenfassung','Meeting-Notizen'],
         'launched':'2023-02-22','lastUpdated':'2026-02-28'},
        {'slug':'perplexity','name':'Perplexity','vendor':'Perplexity AI','category':'forschung',
         'tagline':'Antwort-Maschine mit Quellenangaben — KI für Recherche.',
         'price':'Freemium — Pro $20/Mon.','api':True,'dsgvo':'bedingt','origin':'USA',
         'rating':4.5,'reviews':1670,
         'pros':['Immer mit Quellen','Echtzeit-Websuche','Spaces für Themen'],
         'cons':['Qualität der Quellen variiert','Kein eigenes Modell'],
         'usecases':['Recherche','Fact-Checking','Literatur'],
         'launched':'2022-12-07','lastUpdated':'2026-04-05'},
        {'slug':'deepl-write','name':'DeepL Write','vendor':'DeepL','category':'marketing',
         'tagline':'Deutsches KI-Schreibwerkzeug aus Köln — perfekt für Business-Texte.',
         'price':'Freemium — Pro €8,99/Mon.','api':True,'dsgvo':'ja','origin':'EU (DE)',
         'rating':4.6,'reviews':540,
         'pros':['Beste deutsche Sprachqualität','DSGVO-konform','Unternehmensserver in EU'],
         'cons':['Nur Textverbesserung, kein Generator','Begrenzte Kreativität'],
         'usecases':['E-Mails','Berichte','Lektorat'],
         'launched':'2023-01-17','lastUpdated':'2026-03-08'},
        {'slug':'aleph-alpha','name':'Pharia AI','vendor':'Aleph Alpha','category':'sprachmodelle',
         'tagline':'Souveräne KI aus Heidelberg — Fokus auf Behörden und Industrie.',
         'price':'Enterprise — auf Anfrage','api':True,'dsgvo':'ja','origin':'EU (DE)',
         'rating':4.1,'reviews':89,
         'pros':['Deutscher Anbieter','Self-Hosting möglich','Erklärbare KI','Enterprise-Support'],
         'cons':['Keine Consumer-Version','Hohe Einstiegshürde'],
         'usecases':['Behörden','Versicherung','Industrie'],
         'launched':'2021-04-15','lastUpdated':'2026-01-20'},
    ],
    'article': [
        {'slug':'was-ist-ki','title':'Was ist Künstliche Intelligenz?','category':'Grundlagen','author':'Redaktion','date':'2026-04-02','readTime':8,'toc':['Definition','Geschichte','Teilgebiete','Heutige Anwendungen','Grenzen und Kritik']},
        {'slug':'llm-vergleich','title':'Große Sprachmodelle im Vergleich 2026','category':'Vergleich','author':'M. Hartmann','date':'2026-03-28','readTime':14,'toc':['Einführung','Methodik','Benchmark-Ergebnisse','Kosten pro Token','Empfehlungen']},
        {'slug':'dsgvo-ki','title':'DSGVO und KI: Was Unternehmen 2026 wissen müssen','category':'Recht','author':'Dr. S. Klein','date':'2026-03-15','readTime':11,'toc':['Rechtliche Grundlagen','EU AI Act','Auftragsverarbeitung','Checkliste']},
        {'slug':'prompt-engineering','title':'Prompt Engineering: Techniken und Muster','category':'Praxis','author':'J. Weber','date':'2026-03-10','readTime':16,'toc':['Grundprinzipien','Few-Shot','Chain-of-Thought','Rollen','Anti-Patterns']},
        {'slug':'rag-erklaert','title':'Retrieval-Augmented Generation erklärt','category':'Technik','author':'Dr. T. Müller','date':'2026-02-22','readTime':12,'toc':['Was ist RAG?','Architektur','Vektordatenbanken','Evaluierung']},
        {'slug':'ki-bildgenerierung','title':'KI-Bildgenerierung: Von Diffusion zu Video','category':'Technik','author':'L. Schmidt','date':'2026-02-10','readTime':9,'toc':['Diffusionsmodelle','Training','Steuerung','Video-Generation']},
    ],
    'recent-change': [
        {'time':'vor 12 Min.','user':'M. Hartmann','action':'ergänzte','target':'Claude','detail':'Artifacts-Sektion','order':1},
        {'time':'vor 47 Min.','user':'Redaktion','action':'aktualisierte','target':'ChatGPT','detail':'Preistabelle','order':2},
        {'time':'vor 2 Std.','user':'J. Weber','action':'erstellte','target':'Prompt Engineering','detail':'neuer Artikel','order':3},
        {'time':'vor 4 Std.','user':'L. Schmidt','action':'korrigierte','target':'Midjourney','detail':'Preisangabe','order':4},
        {'time':'vor 6 Std.','user':'Dr. S. Klein','action':'ergänzte','target':'DSGVO und KI','detail':'EU AI Act §15','order':5},
        {'time':'vor 1 Tag','user':'Redaktion','action':'erstellte','target':'Pharia AI','detail':'neuer Eintrag','order':6},
        {'time':'vor 1 Tag','user':'T. Müller','action':'verlinkte','target':'RAG','detail':'Querverweis zu Vektordatenbanken','order':7},
    ],
}

# ---------- Wipe existing elements then reseed (idempotent) ----------
print('\n=== Seeding elements ===')
for type_key, ct_id in ct_ids.items():
    # Fetch existing for this content type
    existing = requests.get(f'{BASE}/{SITE}/elements/?type_id={ct_id}&size=200', headers=H, verify=False).json()
    items = existing.get('items', existing) if isinstance(existing, dict) else existing
    for el in items:
        eid = el.get('id')
        if eid:
            requests.delete(f'{BASE}/{SITE}/elements/{eid}', headers=H, verify=False)
    print(f'  · cleared {len(items)} existing "{type_key}" elements')

    rows = DATA.get(type_key, [])
    for row in rows:
        payload = {'type_id': ct_id, 'data': row, 'published': True}
        r = requests.post(f'{BASE}/{SITE}/elements/', json=payload, headers=H, verify=False)
        if not r.ok:
            print(f'  ✗ failed for {row.get("slug") or row.get("target")}: {r.status_code} {r.text[:200]}')
        else:
            label = row.get('slug') or row.get('target') or row.get('name') or '?'
            print(f'  ✓ {type_key}: {label}')

print('\n✓ Seeding complete')
print(f'Content type IDs: {ct_ids}')
