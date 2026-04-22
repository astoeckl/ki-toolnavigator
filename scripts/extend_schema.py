#!/usr/bin/env python3
"""Extend tool + article content types with editorial body fields, then
generate per-element text via Cognitor's AI.

Idempotent: re-running only generates text for elements that don't have it yet.
"""
import requests, urllib3, json, sys, time
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

# ---------- auth ----------
r = requests.post(f'{BASE}/auth/login',
    data={'grant_type':'password','username':ENV['EMAIL'],'password':ENV['PW']},
    headers={'Content-Type':'application/x-www-form-urlencoded'}, verify=False)
r.raise_for_status()
TOKEN = r.json()['access_token']
H = {'Authorization': f'Bearer {TOKEN}', 'Content-Type': 'application/json'}
print('✓ Logged in')

# ---------- step 1: extend content types ----------
def patch_schema(type_key, new_schema):
    cts = requests.get(f'{BASE}/{SITE}/contenttypes/', headers=H, verify=False).json()
    ct = next((c for c in cts if c.get('display_identifier') == type_key or c['identifier'] == type_key), None)
    if not ct:
        sys.exit(f'❌ content type {type_key} not found')
    r = requests.patch(f'{BASE}/{SITE}/contenttypes/{ct["id"]}',
        json={'schema': new_schema}, headers=H, verify=False)
    if not r.ok:
        sys.exit(f'❌ patch failed for {type_key}: {r.status_code} {r.text[:300]}')
    print(f'  ✓ patched schema "{type_key}"')

TOOL_SCHEMA = {
    'type': 'object',
    'properties': {
        'slug':        {'type': 'string', 'title': 'Slug'},
        'name':        {'type': 'string', 'title': 'Name'},
        'vendor':      {'type': 'string', 'title': 'Anbieter'},
        'category':    {'type': 'string', 'title': 'Kategorie-Slug'},
        'tagline':     {'type': 'string', 'title': 'Tagline'},
        'overview':    {'type': 'string', 'title': 'Übersichtstext (Markdown)', 'description': 'Editorialer Übersichtstext für die Tool-Detailseite.'},
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
}

ARTICLE_SCHEMA = {
    'type': 'object',
    'properties': {
        'slug':     {'type': 'string', 'title': 'Slug'},
        'title':    {'type': 'string', 'title': 'Titel'},
        'category': {'type': 'string', 'title': 'Rubrik'},
        'author':   {'type': 'string', 'title': 'Autor'},
        'date':     {'type': 'string', 'title': 'Datum'},
        'readTime': {'type': 'integer', 'title': 'Lesezeit (Min.)'},
        'toc':      {'type': 'array', 'title': 'Inhaltsverzeichnis', 'items': {'type': 'string'}},
        'lead':     {'type': 'string', 'title': 'Lead/Vorspann'},
        'body':     {'type': 'string', 'title': 'Artikel-Body (Markdown)', 'description': 'Vollständiger Artikeltext in Markdown.'},
    },
    'required': ['slug','title'],
}

print('\n=== Step 1: extend schemas ===')
patch_schema('tool', TOOL_SCHEMA)
patch_schema('article', ARTICLE_SCHEMA)

# ---------- step 2: load elements, generate missing text ----------
def list_elements(type_key):
    cts = requests.get(f'{BASE}/{SITE}/contenttypes/', headers=H, verify=False).json()
    ct = next(c for c in cts if c.get('display_identifier') == type_key or c['identifier'] == type_key)
    page, all_items = 1, []
    while True:
        r = requests.get(f'{BASE}/{SITE}/elements/?type_id={ct["id"]}&size=200&page={page}',
            headers=H, verify=False).json()
        items = r.get('items', [])
        all_items.extend(items)
        if not r.get('has_next'): break
        page += 1
    return all_items

def generate(prompt):
    """Use Cognitor's AI text generator."""
    r = requests.post(f'{BASE}/{SITE}/seo/generatetext',
        json={'prompt': prompt}, headers=H, verify=False, timeout=120)
    if not r.ok:
        print(f'  ⚠️  AI gen failed ({r.status_code}); falling back to manual text')
        return None
    data = r.json()
    return data.get('generated_text') or data.get('text') or data.get('content')

def patch_element(eid, new_data_partial, existing):
    """Merge new fields into existing data (PATCH replaces data wholesale)."""
    merged = {**existing, **new_data_partial}
    r = requests.patch(f'{BASE}/{SITE}/elements/{eid}',
        json={'data': merged}, headers=H, verify=False)
    if not r.ok:
        print(f'  ✗ patch element {eid}: {r.status_code} {r.text[:200]}')
        return False
    return True

# ---------- tools ----------
print('\n=== Step 2a: tool overviews ===')
tools = list_elements('tool')
print(f'  · {len(tools)} tools to process')
for el in tools:
    d = el['data']
    if d.get('overview'):
        print(f'  · {d.get("name")}: already has overview, skipping')
        continue
    prompt = (
        f"Schreibe einen sachlichen, redaktionellen Übersichtstext (auf Deutsch, ca. 180-220 Wörter, "
        f"in 3-4 Absätzen, in Markdown ohne Überschriften) über das KI-Tool \"{d['name']}\" "
        f"vom Anbieter {d['vendor']} aus der Kategorie {d['category']}. "
        f"Tagline: \"{d.get('tagline','')}\". "
        f"Stärken: {', '.join(d.get('pros', []))}. "
        f"Schwächen: {', '.join(d.get('cons', []))}. "
        f"Typische Anwendungsfälle: {', '.join(d.get('usecases', []))}. "
        f"Preis: {d.get('price','')}. DSGVO-Status: {d.get('dsgvo','')}. "
        f"Schreibe nüchtern und einordnend wie ein Wiki-Artikel — keine Werbesprache. "
        f"Erwähne die wichtigsten Stärken und Schwächen, ordne das Tool im Markt ein und nenne, "
        f"für welche Zielgruppe es sich besonders eignet. "
        f"Beginne direkt mit dem Fließtext, ohne Einleitung wie 'Hier ist der Text'."
    )
    print(f'  · {d.get("name")}: generating ...', end='', flush=True)
    text = generate(prompt)
    if not text:
        # Fallback template — at least different per tool
        text = (
            f"**{d['name']}** ({d['vendor']}) ist ein Werkzeug der Kategorie *{d.get('category')}*. "
            f"{d.get('tagline','')}\n\n"
            f"Zu den hervorgehobenen Stärken zählen {', '.join(d.get('pros', [])[:3]).lower()}. "
            f"Bekannte Schwächen: {', '.join(d.get('cons', [])[:2]).lower()}.\n\n"
            f"Typische Einsatzfelder sind {', '.join(d.get('usecases', [])[:3]).lower()}. "
            f"Preisbasis: {d.get('price','')}. DSGVO-Status: {d.get('dsgvo','')}."
        )
    if patch_element(el['id'], {'overview': text.strip()}, d):
        print(f' ✓ ({len(text)} chars)')
    time.sleep(0.5)

# ---------- articles ----------
print('\n=== Step 2b: article bodies ===')
articles = list_elements('article')
print(f'  · {len(articles)} articles to process')
for el in articles:
    d = el['data']
    if d.get('body'):
        print(f'  · {d.get("title")}: already has body, skipping')
        continue
    toc_str = '; '.join(d.get('toc', []))
    prompt = (
        f"Schreibe einen redaktionellen, gut recherchierten Wiki-Artikel auf Deutsch zum Titel "
        f"\"{d['title']}\" für die Rubrik {d.get('category','')}. "
        f"Gliedere ihn in folgende Abschnitte (jeweils als ## H2 in Markdown, "
        f"in genau dieser Reihenfolge): {toc_str}. "
        f"Pro Abschnitt 2-4 Absätze, insgesamt etwa {d.get('readTime', 8) * 100} Wörter. "
        f"Sachlicher Ton, einordnende Sprache, keine Werbung. "
        f"Wenn passend, baue ein Markdown-Zitat (> ...) ein. "
        f"Beginne direkt mit dem ersten H2, ohne Vorrede."
    )
    print(f'  · {d.get("title")[:60]}: generating ...', end='', flush=True)
    body = generate(prompt)
    lead = None
    if body:
        # Also generate a one-paragraph lead
        lead_prompt = (
            f"Schreibe einen einzelnen Vorspann-Absatz (1-2 Sätze, ca. 35-50 Wörter, deutsch, "
            f"sachlich-einordnend, ohne Anführungszeichen) für den Wiki-Artikel \"{d['title']}\"."
        )
        lead = generate(lead_prompt)
    if not body:
        body = '\n\n'.join([f'## {section}\n\n*Inhalt für diesen Abschnitt folgt in Kürze.*' for section in d.get('toc', [])])
    update = {'body': body.strip()}
    if lead: update['lead'] = lead.strip()
    if patch_element(el['id'], update, d):
        print(f' ✓ ({len(body)} chars)')
    time.sleep(0.5)

print('\n✓ Schema extended and content generated.')
print('Next: rebuild Next.js types and update components to render the new fields.')
