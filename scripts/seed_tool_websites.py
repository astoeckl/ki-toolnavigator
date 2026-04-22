#!/usr/bin/env python3
"""Add `website` field to the tool schema and patch every tool with its real URL.
Idempotent: skips tools that already have a website set.
"""
import requests, urllib3, sys
from pathlib import Path

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ROOT = Path(__file__).resolve().parent.parent
ENV = {l.split('=',1)[0].strip(): l.split('=',1)[1].strip()
       for l in (ROOT/'.env').read_text().splitlines() if '=' in l and not l.startswith('#')}
BASE, SITE = ENV['BASEURL'], ENV['SITE']

# Canonical homepage / product page per tool
WEBSITES = {
    'chatgpt':          'https://chatgpt.com',
    'claude':           'https://claude.ai',
    'gemini':           'https://gemini.google.com',
    'mistral':          'https://chat.mistral.ai',
    'midjourney':       'https://www.midjourney.com',
    'stable-diffusion': 'https://stability.ai/stable-image',
    'elevenlabs':       'https://elevenlabs.io',
    'runway':           'https://runwayml.com',
    'cursor':           'https://cursor.com',
    'copilot':          'https://github.com/features/copilot',
    'notion-ai':        'https://www.notion.so/product/ai',
    'perplexity':       'https://www.perplexity.ai',
    'deepl-write':      'https://www.deepl.com/write',
    'aleph-alpha':      'https://aleph-alpha.com',
    # newer entries
    'ms-copilot':       'https://www.microsoft.com/en-us/microsoft-copilot',
    'grok':             'https://grok.com',
    'deepseek':         'https://www.deepseek.com',
    'flux':             'https://bfl.ai',
    'ideogram':         'https://ideogram.ai',
    'adobe-firefly':    'https://firefly.adobe.com',
    'suno':             'https://suno.com',
    'synthesia':        'https://www.synthesia.io',
    'windsurf':         'https://windsurf.com',
    'n8n':              'https://n8n.io',
    'make':             'https://www.make.com',
    'notebooklm':       'https://notebooklm.google.com',
    'julius':           'https://julius.ai',
    'neuroflash':       'https://neuroflash.com/de/',
    'elicit':           'https://elicit.com',
}

r = requests.post(f'{BASE}/auth/login',
    data={'grant_type':'password','username':ENV['EMAIL'],'password':ENV['PW']},
    headers={'Content-Type':'application/x-www-form-urlencoded'}, verify=False)
H = {'Authorization': f'Bearer {r.json()["access_token"]}', 'Content-Type':'application/json'}
print('✓ Logged in')

# 1. Patch schema (idempotent)
cts = requests.get(f'{BASE}/{SITE}/contenttypes/', headers=H, verify=False).json()
tool_ct = next(c for c in cts if c.get('display_identifier') == 'tool')
schema = tool_ct.get('schema', {})
props = schema.get('properties', {})
if 'website' not in props:
    props['website'] = {'type': 'string', 'title': 'Website-URL', 'description': 'Offizielle Tool-Website (Hersteller-Homepage oder Produktseite).'}
    schema['properties'] = props
    r = requests.patch(f'{BASE}/{SITE}/contenttypes/{tool_ct["id"]}',
        json={'schema': schema}, headers=H, verify=False)
    if not r.ok:
        sys.exit(f'❌ schema patch failed: {r.status_code} {r.text[:300]}')
    print('  ✓ added website field to tool schema')
else:
    print('  · schema already has website')

# 2. Fetch + patch all tool elements
items, page = [], 1
while True:
    r = requests.get(f'{BASE}/{SITE}/elements/?type_id={tool_ct["id"]}&size=200&page={page}',
        headers=H, verify=False).json()
    items += r.get('items', [])
    if not r.get('has_next'): break
    page += 1
print(f'  · {len(items)} tools to process')

patched = skipped = errored = unmapped = 0
for el in items:
    d = el['data']
    slug = d.get('slug')
    target = WEBSITES.get(slug)
    if not target:
        print(f'  ⚠️  {slug}: no URL mapping')
        unmapped += 1
        continue
    if d.get('website') == target:
        print(f'  · {slug}: already set')
        skipped += 1
        continue
    new_data = {**d, 'website': target}
    r = requests.patch(f'{BASE}/{SITE}/elements/{el["id"]}',
        json={'data': new_data}, headers=H, verify=False)
    if r.ok:
        patched += 1
        print(f'  ✓ {slug}: {target}')
    else:
        errored += 1
        print(f'  ✗ {slug}: {r.status_code} {r.text[:200]}')

print(f'\n✓ Done — patched {patched}, skipped {skipped}, errored {errored}, unmapped {unmapped}')
