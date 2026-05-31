#!/usr/bin/env python3
"""Generic, JSON-driven tool seeder for the weekly auto-discovery pipeline.

Reads scripts/pending_tools.json — a JSON array of tool records in the
established schema — and for each NEW slug:
  1. creates the tool element (all base fields)
  2. creates the German overview Post and links it (post_id)
  3. fetches + uploads the logo (Google favicon, graceful on 404)
  4. appends a { slug, url[, stealth] } entry to capture_tool_screenshots.mjs
  5. appends a cover cue to generate_tool_images.py TOOL_CUES

Idempotent: slugs that already exist in the CMS are skipped entirely, and
capture/cover entries are only added if not already present.

After a successful run, pending_tools.json is moved to
scripts/pending_archive/pending_<timestamp>.json so the same batch is never
re-processed. Exit code 0 = done (even if 0 tools), 1 = hard error.

Tool record schema (per element of the JSON array):
  slug, name, vendor, category, tagline, price, api(bool), dsgvo, origin,
  rating(float), reviews(int), pros[], cons[], usecases[], launched, lastUpdated,
  website, domain, features(md), pricing(md), overview(md)
  optional: stealth(bool), screenshot_url(str), cover_cue(str)
"""
import json
import sys
import shutil
from datetime import datetime, timezone
from pathlib import Path

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

ROOT = Path(__file__).resolve().parent.parent
LOGOS_DIR = ROOT / 'logos'
LOGOS_DIR.mkdir(exist_ok=True)
PENDING = ROOT / 'scripts' / 'pending_tools.json'
ARCHIVE_DIR = ROOT / 'scripts' / 'pending_archive'
ARCHIVE_DIR.mkdir(exist_ok=True)
CAPTURE = ROOT / 'scripts' / 'capture_tool_screenshots.mjs'
COVER = ROOT / 'scripts' / 'generate_tool_images.py'
SENTINEL = 'WEEKLY-DISCOVERY-INSERT'

VALID_CATEGORIES = {
    'sprachmodelle', 'bildgenerierung', 'video-audio', 'coding', 'agenten',
    'produktivitaet', 'daten-analyse', 'marketing', 'forschung',
}
REQUIRED = ['slug', 'name', 'vendor', 'category', 'tagline', 'price', 'api',
            'dsgvo', 'origin', 'rating', 'reviews', 'pros', 'cons', 'usecases',
            'launched', 'lastUpdated', 'website', 'domain', 'features',
            'pricing', 'overview']


def load_env():
    return {l.split('=', 1)[0].strip(): l.split('=', 1)[1].strip()
            for l in (ROOT / '.env').read_text().splitlines()
            if '=' in l and not l.startswith('#')}


def fetch_logo(domain: str, size: int = 128) -> bytes:
    url = f'https://www.google.com/s2/favicons?domain={domain}&sz={size}'
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    return r.content


def append_capture(slug: str, url: str, stealth: bool):
    text = CAPTURE.read_text()
    if f"slug: '{slug}'" in text:
        return  # already present
    lines = text.splitlines()
    idx = next((i for i, l in enumerate(lines) if SENTINEL in l), None)
    if idx is None:
        print(f'  ! capture sentinel missing — skipped {slug}')
        return
    entry = '  { slug: %s, url: %s%s },' % (
        json.dumps(slug), json.dumps(url),
        ', stealth: true' if stealth else '')
    lines.insert(idx, entry)
    CAPTURE.write_text('\n'.join(lines) + '\n')


def append_cover(slug: str, cue: str):
    text = COVER.read_text()
    if f"'{slug}':" in text:
        return  # already present
    lines = text.splitlines()
    idx = next((i for i, l in enumerate(lines) if SENTINEL in l), None)
    if idx is None:
        print(f'  ! cover sentinel missing — skipped {slug}')
        return
    # repr() produces a valid, safely-escaped Python string literal
    entry = '    %r: %r,' % (slug, cue)
    lines.insert(idx, entry)
    COVER.write_text('\n'.join(lines) + '\n')


def main():
    if not PENDING.exists():
        print('No pending_tools.json — nothing to seed.')
        return 0
    try:
        tools = json.loads(PENDING.read_text())
    except json.JSONDecodeError as e:
        print(f'✗ pending_tools.json is not valid JSON: {e}')
        return 1
    if not isinstance(tools, list) or not tools:
        print('pending_tools.json is empty — nothing to seed.')
        return 0

    # validate up front
    for t in tools:
        missing = [k for k in REQUIRED if k not in t]
        if missing:
            print(f'✗ tool {t.get("slug","?")} missing fields: {missing}')
            return 1
        if t['category'] not in VALID_CATEGORIES:
            print(f'✗ tool {t["slug"]} has invalid category: {t["category"]}')
            return 1

    env = load_env()
    BASE, SITE = env['BASEURL'], env['SITE']
    r = requests.post(f'{BASE}/auth/login',
                      data={'grant_type': 'password', 'username': env['EMAIL'],
                            'password': env['PW']},
                      headers={'Content-Type': 'application/x-www-form-urlencoded'},
                      verify=False)
    H = {'Authorization': f'Bearer {r.json()["access_token"]}'}
    JH = {**H, 'Content-Type': 'application/json'}
    print('✓ Logged in')

    cts = requests.get(f'{BASE}/{SITE}/contenttypes/', headers=JH, verify=False).json()
    tool_ct = next(c for c in cts if c.get('display_identifier') == 'tool')
    TOOL_CT_ID = tool_ct['id']

    items, page = [], 1
    while True:
        rj = requests.get(f'{BASE}/{SITE}/elements/?type_id={TOOL_CT_ID}&size=200&page={page}',
                          headers=JH, verify=False).json()
        items += rj.get('items', [])
        if not rj.get('has_next'):
            break
        page += 1
    existing = {el['data'].get('slug') for el in items}
    print(f'  · {len(existing)} tool slugs already in CMS')

    added = []
    for tool in tools:
        slug = tool['slug']
        if slug in existing:
            print(f'· {slug}: already in CMS, skipping')
            continue

        payload = {'type_id': TOOL_CT_ID, 'published': True, 'data': {
            k: tool[k] for k in REQUIRED
        }}
        r = requests.post(f'{BASE}/{SITE}/elements/', json=payload, headers=JH, verify=False)
        if not r.ok:
            print(f'✗ {slug}: create failed: {r.status_code} {r.text[:200]}')
            continue
        el = r.json()
        print(f'✓ {slug}: created (id={el["id"]})')
        if not el.get('published'):
            requests.patch(f'{BASE}/{SITE}/elements/{el["id"]}',
                           json={'published': True}, headers=JH, verify=False)

        patches = {}
        # overview Post
        post_payload = {
            'title': f'{tool["name"]} im Überblick',
            'slug': f'{slug}-uebersicht',
            'content': tool['overview'],
            'status': 'published',
        }
        rp = requests.post(f'{BASE}/{SITE}/posts/', json=post_payload, headers=JH, verify=False)
        if rp.ok:
            patches['post_id'] = rp.json()['id']
            print(f'  ✓ post #{patches["post_id"]} ({len(tool["overview"])} chars)')
        else:
            print(f'  ✗ post failed: {rp.status_code} {rp.text[:200]}')

        # logo
        try:
            png = fetch_logo(tool['domain'])
            local = LOGOS_DIR / f'{slug}.png'
            local.write_bytes(png)
            with open(local, 'rb') as fh:
                files = {'file': (f'{slug}-logo.png', fh, 'image/png')}
                data = {'name': f'{tool["name"]} Logo',
                        'alt_text': f'Logo von {tool["name"]}',
                        'description': f'Offizielles Logo von {tool["name"]} ({tool["domain"]}).'}
                rl = requests.post(f'{BASE}/{SITE}/media/', files=files, data=data,
                                   headers=H, verify=False, timeout=120)
            if rl.ok:
                patches['logo_id'] = rl.json()['id']
                print(f'  ✓ logo #{patches["logo_id"]} ({len(png):,} bytes)')
            else:
                print(f'  ✗ logo upload failed: {rl.status_code}')
        except Exception as e:
            print(f'  ✗ logo fetch failed: {e}')

        if patches:
            new_data = {**el['data'], **patches}
            r = requests.patch(f'{BASE}/{SITE}/elements/{el["id"]}',
                               json={'data': new_data}, headers=JH, verify=False)
            if r.ok:
                print(f'  ✓ patched: {list(patches.keys())}')

        # capture + cover pipeline registration
        shot_url = tool.get('screenshot_url') or tool['website']
        append_capture(slug, shot_url, bool(tool.get('stealth')))
        cue = tool.get('cover_cue') or (
            f'A small abstract emblem for {tool["name"]}, hairline strokes on '
            f'off-white, with a single magenta accent dot.')
        append_cover(slug, cue)
        added.append(slug)

    # archive the batch
    ts = datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')
    archived = ARCHIVE_DIR / f'pending_{ts}.json'
    shutil.move(str(PENDING), str(archived))
    print(f'\n✓ Done. Added {len(added)} tools: {added}')
    print(f'  archived batch → {archived.relative_to(ROOT)}')
    # emit machine-readable summary for the orchestrator
    print('ADDED_SLUGS=' + ','.join(added))
    return 0


if __name__ == '__main__':
    sys.exit(main())
