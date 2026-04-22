#!/usr/bin/env python3
"""Convert inline article body/lead fields into proper Posts referenced by post_id.

For each article element with a `body` field:
  1. Create a Post (title = article.title, content = body, short_description = lead)
  2. Update the element: remove body/lead, set post_id
After processing all elements, PATCH the article schema to reflect the new shape.

Idempotent: skips articles that already have post_id set.
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

# ---- Get article content type
cts = requests.get(f'{BASE}/{SITE}/contenttypes/', headers=H, verify=False).json()
article_ct = next(c for c in cts if c.get('display_identifier') == 'article')
print(f'  article content type id={article_ct["id"]}')

# ---- Fetch all article elements
items, page = [], 1
while True:
    r = requests.get(f'{BASE}/{SITE}/elements/?type_id={article_ct["id"]}&size=200&page={page}', headers=H, verify=False).json()
    items += r.get('items', [])
    if not r.get('has_next'): break
    page += 1
print(f'  {len(items)} articles to migrate')

# ---- Step 1: create post per article, update element
for el in items:
    d = el['data']
    if d.get('post_id'):
        print(f'  · {d.get("slug")}: already has post_id={d["post_id"]}, skipping')
        continue
    if not d.get('body'):
        print(f'  ⚠️  {d.get("slug")}: no body, skipping')
        continue
    # Create the post
    post_payload = {
        'title': d['title'],
        'content': d['body'],
        'short_description': d.get('lead') or '',
        'keywords': [d.get('category') or 'Allgemein'],
        'published': True,
        'locale': 'de',
    }
    r = requests.post(f'{BASE}/{SITE}/posts/', json=post_payload, headers=H, verify=False)
    if not r.ok:
        print(f'  ✗ {d.get("slug")}: post create failed: {r.status_code} {r.text[:200]}')
        continue
    post = r.json()
    pid = post['id']
    # Update element: drop body/lead, add post_id
    new_data = {k: v for k, v in d.items() if k not in ('body', 'lead')}
    new_data['post_id'] = pid
    r = requests.patch(f'{BASE}/{SITE}/elements/{el["id"]}', json={'data': new_data}, headers=H, verify=False)
    if not r.ok:
        print(f'  ✗ {d.get("slug")}: element patch failed: {r.status_code} {r.text[:200]}')
        continue
    print(f'  ✓ {d.get("slug")}: post_id={pid}, body moved to post ({len(d["body"])} chars)')

# ---- Step 2: update content type schema
NEW_SCHEMA = {
    'type': 'object',
    'properties': {
        'slug':     {'type': 'string', 'title': 'Slug'},
        'title':    {'type': 'string', 'title': 'Titel'},
        'category': {'type': 'string', 'title': 'Rubrik'},
        'author':   {'type': 'string', 'title': 'Autor'},
        'date':     {'type': 'string', 'title': 'Datum'},
        'readTime': {'type': 'integer', 'title': 'Lesezeit (Min.)'},
        'toc':      {'type': 'array', 'title': 'Inhaltsverzeichnis', 'items': {'type': 'string'}},
        'post_id':  {'type': 'integer', 'title': 'Post-Referenz', 'format': 'post_id',
                     'description': 'Referenz auf den Post mit dem eigentlichen Artikeltext.'},
    },
    'required': ['slug','title'],
}
r = requests.patch(f'{BASE}/{SITE}/contenttypes/{article_ct["id"]}', json={'schema': NEW_SCHEMA}, headers=H, verify=False)
if not r.ok:
    sys.exit(f'❌ schema patch failed: {r.status_code} {r.text[:300]}')
print('\n✓ Article schema updated: body/lead removed, post_id added (format: post_id)')
print('Migration complete.')
