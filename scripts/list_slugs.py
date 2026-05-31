#!/usr/bin/env python3
"""Print the live catalogue as JSON: {"count": N, "tools": [{slug, name, vendor, category}]}.
Used by the weekly-tool-discovery workflow to dedupe candidates against what
already exists. Reads credentials from ../.env.
"""
import json
from pathlib import Path
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ROOT = Path(__file__).resolve().parent.parent
ENV = {l.split('=', 1)[0].strip(): l.split('=', 1)[1].strip()
       for l in (ROOT / '.env').read_text().splitlines()
       if '=' in l and not l.startswith('#')}
BASE, SITE = ENV['BASEURL'], ENV['SITE']

r = requests.post(f'{BASE}/auth/login',
                  data={'grant_type': 'password', 'username': ENV['EMAIL'], 'password': ENV['PW']},
                  headers={'Content-Type': 'application/x-www-form-urlencoded'}, verify=False)
JH = {'Authorization': f'Bearer {r.json()["access_token"]}', 'Content-Type': 'application/json'}

cts = requests.get(f'{BASE}/{SITE}/contenttypes/', headers=JH, verify=False).json()
tool_ct = next(c for c in cts if c.get('display_identifier') == 'tool')

items, page = [], 1
while True:
    rj = requests.get(f'{BASE}/{SITE}/elements/?type_id={tool_ct["id"]}&size=200&page={page}',
                      headers=JH, verify=False).json()
    items += rj.get('items', [])
    if not rj.get('has_next'):
        break
    page += 1

tools = [{'slug': el['data'].get('slug'), 'name': el['data'].get('name'),
          'vendor': el['data'].get('vendor'), 'category': el['data'].get('category')}
         for el in items]
print(json.dumps({'count': len(tools), 'tools': tools}, ensure_ascii=False))
