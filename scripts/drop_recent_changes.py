#!/usr/bin/env python3
"""Delete the recent-change content type and all its elements."""
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
ct = next((c for c in cts if c.get('display_identifier') == 'recent-change'), None)
if not ct:
    print('  · recent-change type not found (already gone?)'); sys.exit(0)

# delete all elements of this type
items, page = [], 1
while True:
    r = requests.get(f'{BASE}/{SITE}/elements/?type_id={ct["id"]}&size=200&page={page}', headers=H, verify=False).json()
    items += r.get('items', [])
    if not r.get('has_next'): break
    page += 1
print(f'  · deleting {len(items)} recent-change elements ...')
for el in items:
    r = requests.delete(f'{BASE}/{SITE}/elements/{el["id"]}', headers=H, verify=False)
    if not r.ok:
        print(f'  ⚠️  failed for element {el["id"]}: {r.status_code}')

# delete the content type
r = requests.delete(f'{BASE}/{SITE}/contenttypes/{ct["id"]}', headers=H, verify=False)
if not r.ok:
    sys.exit(f'❌ failed to delete content type: {r.status_code} {r.text[:200]}')
print(f'✓ Deleted content type "recent-change" (id={ct["id"]})')
