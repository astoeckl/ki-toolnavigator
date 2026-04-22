#!/usr/bin/env python3
"""Upload tool screenshots from ./screenshots/<slug>.jpg to Cognitor Media,
extend the tool content type with a `screenshot_id` field, and patch each
tool element to reference its screenshot.

Idempotent: skips tools that already have a screenshot_id set.
"""
import requests, urllib3, sys
from pathlib import Path

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ROOT = Path(__file__).resolve().parent.parent
SHOTS = ROOT / 'screenshots'

ENV = {l.split('=',1)[0].strip(): l.split('=',1)[1].strip()
       for l in (ROOT/'.env').read_text().splitlines() if '=' in l and not l.startswith('#')}
BASE, SITE = ENV['BASEURL'], ENV['SITE']

r = requests.post(f'{BASE}/auth/login',
    data={'grant_type':'password','username':ENV['EMAIL'],'password':ENV['PW']},
    headers={'Content-Type':'application/x-www-form-urlencoded'}, verify=False)
H = {'Authorization': f'Bearer {r.json()["access_token"]}'}
print('✓ Logged in')

# --- 1. Ensure schema has screenshot_id (idempotent) ---
cts = requests.get(f'{BASE}/{SITE}/contenttypes/', headers={**H, 'Content-Type':'application/json'}, verify=False).json()
tool_ct = next(c for c in cts if c.get('display_identifier') == 'tool')
schema = tool_ct.get('schema', {})
props = schema.get('properties', {})
if 'screenshot_id' not in props:
    props['screenshot_id'] = {
        'type': 'integer',
        'title': 'Screenshot der Tool-Website',
        'format': 'media_id',
        'description': 'Echter Screenshot der Tool-Website (für die Bildergalerie auf der Detailseite).',
    }
    schema['properties'] = props
    r = requests.patch(f'{BASE}/{SITE}/contenttypes/{tool_ct["id"]}',
        json={'schema': schema}, headers={**H, 'Content-Type':'application/json'}, verify=False)
    if not r.ok:
        sys.exit(f'❌ schema patch failed: {r.status_code} {r.text[:300]}')
    print('  ✓ added screenshot_id field')
else:
    print('  · schema already has screenshot_id')

# --- 2. Fetch tool elements ---
items, page = [], 1
while True:
    r = requests.get(f'{BASE}/{SITE}/elements/?type_id={tool_ct["id"]}&size=200&page={page}',
        headers={**H, 'Content-Type':'application/json'}, verify=False).json()
    items += r.get('items', [])
    if not r.get('has_next'): break
    page += 1
print(f'  · {len(items)} tools to process')

# --- 3. For each tool: upload screenshot if missing, then patch element ---
for el in items:
    d = el['data']
    slug = d.get('slug')
    file = SHOTS / f'{slug}.jpg'
    if not file.exists():
        print(f'  ⚠️  {slug}: no screenshot file at {file}')
        continue
    if d.get('screenshot_id'):
        print(f'  · {slug}: already has screenshot_id, skipping')
        continue

    # Upload to Cognitor
    with open(file, 'rb') as fh:
        files = {'file': (f'{slug}-screenshot.jpg', fh, 'image/jpeg')}
        data = {
            'name': f'{d.get("name", slug)} – Website-Screenshot',
            'alt_text': f'Screenshot der {d.get("name", slug)}-Website',
            'description': f'Live-Screenshot der offiziellen Webseite von {d.get("name", slug)}.',
        }
        r = requests.post(f'{BASE}/{SITE}/media/',
            files=files, data=data, headers=H, verify=False, timeout=120)
    if not r.ok:
        print(f'  ✗ {slug}: upload failed: {r.status_code} {r.text[:200]}')
        continue
    media = r.json()
    mid = media.get('id')
    print(f'  ✓ {slug}: uploaded media #{mid} ({file.stat().st_size:,} bytes)')

    # Patch element
    new_data = {**d, 'screenshot_id': mid}
    r = requests.patch(f'{BASE}/{SITE}/elements/{el["id"]}',
        json={'data': new_data}, headers={**H, 'Content-Type':'application/json'}, verify=False)
    if not r.ok:
        print(f'    ✗ element patch failed: {r.status_code} {r.text[:200]}')

print('\n✓ Done.')
