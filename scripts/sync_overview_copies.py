#!/usr/bin/env python3
"""Sync data.overview with the canonical Post content.

The generic seeder stores the overview twice: as a Post (what the site renders)
and as a duplicate `overview` field on the element (shipped in the public API
payload). Post-only edits leave the copy stale and self-contradictory.
This resyncs any drifted element. Idempotent.
"""
import requests, urllib3
from pathlib import Path
urllib3.disable_warnings()
ROOT = Path(__file__).resolve().parent.parent
ENV = {l.split('=',1)[0].strip(): l.split('=',1)[1].strip()
       for l in (ROOT/'.env').read_text().splitlines() if '=' in l and not l.startswith('#')}
BASE, SITE = ENV['BASEURL'], ENV['SITE']
r = requests.post(f'{BASE}/auth/login',
    data={'grant_type':'password','username':ENV['EMAIL'],'password':ENV['PW']},
    headers={'Content-Type':'application/x-www-form-urlencoded'}, verify=False)
H = {'Authorization': f'Bearer {r.json()["access_token"]}', 'Content-Type':'application/json'}

cts = requests.get(f'{BASE}/{SITE}/contenttypes/', headers=H, verify=False).json()
ct = next(c for c in cts if c.get('display_identifier') == 'tool')
items, page = [], 1
while True:
    rj = requests.get(f'{BASE}/{SITE}/elements/?type_id={ct["id"]}&size=200&page={page}',
                      headers=H, verify=False).json()
    items += rj.get('items', [])
    if not rj.get('has_next'):
        break
    page += 1

fixed = 0
for el in items:
    d = el['data']
    ov, pid = d.get('overview'), d.get('post_id')
    if not ov or not isinstance(pid, int):
        continue
    pc = requests.get(f'{BASE}/{SITE}/posts/{pid}', headers=H, verify=False).json().get('content', '')
    if not pc or ov.strip() == pc.strip():
        continue
    new_data = {**d, 'overview': pc}
    rp = requests.patch(f'{BASE}/{SITE}/elements/{el["id"]}',
                        json={'data': new_data}, headers=H, verify=False)
    print(f'  synced {d.get("slug"):16} el={el["id"]} post={pid}  {len(ov)}c -> {len(pc)}c  [{rp.status_code}]')
    fixed += 1
print(f'Done. {fixed} element(s) resynced, {len(items)} checked.')
