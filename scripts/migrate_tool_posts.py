#!/usr/bin/env python3
"""Convert inline tool `overview` field into proper Posts referenced by post_id.

For each tool element with an `overview` field:
  1. Create a Post (title = "<Tool name> — Übersicht", content = overview, short_description = tagline)
  2. Update the element: remove overview, set post_id
After processing all elements, PATCH the tool schema to reflect the new shape.

Idempotent: skips tools that already have post_id set.
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

# ---- Get tool content type
cts = requests.get(f'{BASE}/{SITE}/contenttypes/', headers=H, verify=False).json()
tool_ct = next(c for c in cts if c.get('display_identifier') == 'tool')
print(f'  tool content type id={tool_ct["id"]}')

# ---- Fetch all tool elements
items, page = [], 1
while True:
    r = requests.get(f'{BASE}/{SITE}/elements/?type_id={tool_ct["id"]}&size=200&page={page}', headers=H, verify=False).json()
    items += r.get('items', [])
    if not r.get('has_next'): break
    page += 1
print(f'  {len(items)} tools to migrate')

# ---- Step 1: create post per tool, update element
for el in items:
    d = el['data']
    if d.get('post_id'):
        print(f'  · {d.get("slug")}: already has post_id={d["post_id"]}, skipping')
        continue
    if not d.get('overview'):
        print(f'  ⚠️  {d.get("slug")}: no overview, skipping')
        continue
    post_payload = {
        'title': f'{d["name"]} — Übersicht',
        'content': d['overview'],
        'short_description': d.get('tagline') or '',
        'keywords': [d.get('vendor', ''), d.get('category', '')],
        'published': True,
        'locale': 'de',
    }
    r = requests.post(f'{BASE}/{SITE}/posts/', json=post_payload, headers=H, verify=False)
    if not r.ok:
        print(f'  ✗ {d.get("slug")}: post create failed: {r.status_code} {r.text[:200]}')
        continue
    post = r.json()
    pid = post['id']
    new_data = {k: v for k, v in d.items() if k != 'overview'}
    new_data['post_id'] = pid
    r = requests.patch(f'{BASE}/{SITE}/elements/{el["id"]}', json={'data': new_data}, headers=H, verify=False)
    if not r.ok:
        print(f'  ✗ {d.get("slug")}: element patch failed: {r.status_code} {r.text[:200]}')
        continue
    print(f'  ✓ {d.get("slug")}: post_id={pid}, overview moved to post ({len(d["overview"])} chars)')

# ---- Step 2: update content type schema
NEW_SCHEMA = {
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
        'post_id':     {'type': 'integer', 'title': 'Übersichts-Post', 'format': 'post_id',
                        'description': 'Referenz auf den Post mit dem editorialen Übersichtstext.'},
    },
    'required': ['slug','name','vendor','category'],
}
r = requests.patch(f'{BASE}/{SITE}/contenttypes/{tool_ct["id"]}', json={'schema': NEW_SCHEMA}, headers=H, verify=False)
if not r.ok:
    sys.exit(f'❌ schema patch failed: {r.status_code} {r.text[:300]}')
print('\n✓ Tool schema updated: overview removed, post_id added (format: post_id)')
print('Migration complete.')
