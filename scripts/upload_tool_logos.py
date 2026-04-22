#!/usr/bin/env python3
"""Download each tool's logo from Google's favicon/touch-icon service, upload to
Cognitor Media, and patch the tool element with logo_id.
Also extends the tool schema with a logo_id field on first run.

Idempotent: skips tools that already have a logo_id set.
"""
import requests, urllib3, sys, hashlib, io
from pathlib import Path

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ROOT = Path(__file__).resolve().parent.parent
LOGOS_DIR = ROOT / 'logos'
LOGOS_DIR.mkdir(exist_ok=True)

ENV = {l.split('=',1)[0].strip(): l.split('=',1)[1].strip()
       for l in (ROOT/'.env').read_text().splitlines() if '=' in l and not l.startswith('#')}
BASE, SITE = ENV['BASEURL'], ENV['SITE']

# Mapping: tool slug → domain to fetch logo from (one domain = best-known brand site).
DOMAINS = {
    'chatgpt':          'openai.com',
    'claude':           'anthropic.com',
    'gemini':           'gemini.google.com',
    'mistral':          'mistral.ai',
    'midjourney':       'midjourney.com',
    'stable-diffusion': 'stability.ai',
    'elevenlabs':       'elevenlabs.io',
    'runway':           'runwayml.com',
    'cursor':           'cursor.com',
    'copilot':          'github.com',
    'notion-ai':        'notion.so',
    'perplexity':       'perplexity.ai',
    'deepl-write':      'deepl.com',
    'aleph-alpha':      'aleph-alpha.com',
    # ---- new additions ----
    'ms-copilot':       'microsoft.com',
    'grok':             'x.ai',
    'deepseek':         'deepseek.com',
    'flux':             'bfl.ai',
    'ideogram':         'ideogram.ai',
    'adobe-firefly':    'adobe.com',
    'suno':             'suno.com',
    'synthesia':        'synthesia.io',
    'windsurf':         'windsurf.com',
    'n8n':              'n8n.io',
    'make':             'make.com',
    'notebooklm':       'notebooklm.google.com',
    'julius':           'julius.ai',
    'neuroflash':       'neuroflash.com',
    'elicit':           'elicit.com',
}

def fetch_logo(domain: str, size: int = 256) -> bytes:
    """Fetch via Google's favicon V2 service — returns largest available icon."""
    url = f'https://www.google.com/s2/favicons?domain={domain}&sz={size}'
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    return r.content

# ---- Login ----
r = requests.post(f'{BASE}/auth/login',
    data={'grant_type':'password','username':ENV['EMAIL'],'password':ENV['PW']},
    headers={'Content-Type':'application/x-www-form-urlencoded'}, verify=False)
H = {'Authorization': f'Bearer {r.json()["access_token"]}'}
print('✓ Logged in')

# ---- Ensure schema ----
cts = requests.get(f'{BASE}/{SITE}/contenttypes/',
    headers={**H,'Content-Type':'application/json'}, verify=False).json()
tool_ct = next(c for c in cts if c.get('display_identifier') == 'tool')
schema = tool_ct.get('schema', {})
props = schema.get('properties', {})
if 'logo_id' not in props:
    props['logo_id'] = {
        'type': 'integer',
        'title': 'Logo',
        'format': 'media_id',
        'description': 'Offizielles Logo des Tools (Apple Touch Icon der Hersteller-Website).',
    }
    schema['properties'] = props
    r = requests.patch(f'{BASE}/{SITE}/contenttypes/{tool_ct["id"]}',
        json={'schema': schema}, headers={**H,'Content-Type':'application/json'}, verify=False)
    if not r.ok:
        sys.exit(f'❌ schema patch failed: {r.status_code} {r.text[:300]}')
    print('  ✓ added logo_id field to tool schema')
else:
    print('  · schema already has logo_id')

# ---- Fetch tool elements ----
items, page = [], 1
while True:
    r = requests.get(f'{BASE}/{SITE}/elements/?type_id={tool_ct["id"]}&size=200&page={page}',
        headers={**H,'Content-Type':'application/json'}, verify=False).json()
    items += r.get('items', [])
    if not r.get('has_next'): break
    page += 1
print(f'  · {len(items)} tools to process')

# ---- Per-tool: download + upload + patch ----
for el in items:
    d = el['data']
    slug = d.get('slug')
    if d.get('logo_id'):
        print(f'  · {slug}: already has logo_id, skipping')
        continue
    domain = DOMAINS.get(slug)
    if not domain:
        print(f'  ⚠️  {slug}: no domain mapping')
        continue
    try:
        png = fetch_logo(domain)
    except Exception as e:
        print(f'  ✗ {slug}: fetch failed ({e})')
        continue
    local = LOGOS_DIR / f'{slug}.png'
    local.write_bytes(png)
    size = len(png)
    # Upload
    with open(local, 'rb') as fh:
        files = {'file': (f'{slug}-logo.png', fh, 'image/png')}
        data = {
            'name': f'{d.get("name", slug)} – Logo',
            'alt_text': f'Logo von {d.get("name", slug)}',
            'description': f'Offizielles Logo von {d.get("name", slug)} ({domain}).',
        }
        r = requests.post(f'{BASE}/{SITE}/media/',
            files=files, data=data, headers=H, verify=False, timeout=120)
    if not r.ok:
        print(f'  ✗ {slug}: upload failed: {r.status_code} {r.text[:200]}')
        continue
    mid = r.json().get('id')
    print(f'  ✓ {slug}: logo #{mid} ({size:,} bytes from {domain})')
    # Patch element
    new_data = {**d, 'logo_id': mid}
    r = requests.patch(f'{BASE}/{SITE}/elements/{el["id"]}',
        json={'data': new_data}, headers={**H,'Content-Type':'application/json'}, verify=False)
    if not r.ok:
        print(f'    ✗ element patch failed: {r.status_code} {r.text[:200]}')

print('\n✓ Done.')
