#!/usr/bin/env python3
"""Set every article's `author` to the unified editorial byline.

All content on the site is produced by one editorial team, so the individual
names that were seeded early on ("M. Hartmann", "Dr. S. Klein", …) misattribute
it. Google's Article markup also flags a Person author without an author page,
whereas "Redaktion" is mapped to the site Organization in lib/seo.ts.

Idempotent — articles already set to AUTHOR are skipped.
Dry run:  python3 scripts/unify_article_bylines.py
Apply:    python3 scripts/unify_article_bylines.py --apply
"""
import sys
import requests, urllib3
from pathlib import Path

urllib3.disable_warnings()
ROOT = Path(__file__).resolve().parent.parent
ENV = {l.split('=', 1)[0].strip(): l.split('=', 1)[1].strip()
       for l in (ROOT / '.env').read_text().splitlines() if '=' in l and not l.startswith('#')}
BASE, SITE = ENV['BASEURL'], ENV['SITE']

AUTHOR = 'Redaktion'
APPLY = '--apply' in sys.argv

r = requests.post(f'{BASE}/auth/login',
                  data={'grant_type': 'password', 'username': ENV['EMAIL'], 'password': ENV['PW']},
                  headers={'Content-Type': 'application/x-www-form-urlencoded'}, verify=False)
r.raise_for_status()
JH = {'Authorization': f'Bearer {r.json()["access_token"]}', 'Content-Type': 'application/json'}
print('✓ Logged in')

els = requests.get(f'{BASE}/public/{SITE}/elements/',
                   params={'type': f'{SITE}_article', 'limit': 500}, verify=False).json()

changed = skipped = failed = 0
for el in sorted(els, key=lambda e: e['data'].get('slug', '')):
    slug = el['data'].get('slug', '?')
    current = el['data'].get('author')
    if current == AUTHOR:
        print(f'  =  {slug:26} already "{AUTHOR}"')
        skipped += 1
        continue
    print(f'  →  {slug:26} "{current}" → "{AUTHOR}"')
    if not APPLY:
        changed += 1
        continue
    # Re-read through the auth API so the patch carries the full, current data blob.
    full = requests.get(f'{BASE}/{SITE}/elements/{el["id"]}', headers=JH, verify=False).json()
    data = full['data']
    data['author'] = AUTHOR
    resp = requests.patch(f'{BASE}/{SITE}/elements/{el["id"]}', json={'data': data},
                          headers=JH, verify=False)
    if resp.ok:
        changed += 1
    else:
        failed += 1
        print(f'     ✗ patch failed: {resp.status_code} {resp.text[:160]}')

verb = 'patched' if APPLY else 'would change'
print(f'\n{verb}: {changed} · unchanged: {skipped} · failed: {failed}')
if not APPLY:
    print('Dry run — re-run with --apply to write.')
