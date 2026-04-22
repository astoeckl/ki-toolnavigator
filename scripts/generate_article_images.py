#!/usr/bin/env python3
"""Generate editorial cover images per article via Cognitor's media/generate
(Nano Banana), store them in the Cognitor Media library, and reference them
from the article element via a new `media_id` field.

Pipeline (per article):
  1. Build a prompt combining the brand-style preamble + per-article content cue.
  2. POST /{site}/media/generate with thinking_level=nano-banana.
  3. PATCH the article element: data.media_id = new_media.id
  4. PATCH the article content type schema (once): add media_id field.

Idempotent: skips articles that already have a `media_id` set.
Graceful on 402 (insufficient credits) — logs which articles still need regen.
"""
import requests, urllib3, sys, time
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

# ---- Brand style preamble: locked across all articles ----
STYLE_PREAMBLE = (
    "Editorial magazine illustration in a muted, hand-drawn style. "
    "Off-white paper background (#FAF8F5), deep ink black linework (#17140F), "
    "a single magenta accent color (#A01E78). "
    "1-pixel hairline strokes, no drop shadows, no gradients, no photorealism, "
    "no 3D rendering. Flat composition with generous negative space, "
    "reminiscent of a 1970s serif-typography editorial or a German tech magazine. "
    "Subject should be rendered as simple, abstract symbols or small vignettes, "
    "not as realistic imagery. No text, no letters, no logos in the image. "
    "Aspect ratio 16:9, composition slightly offset to the left."
)

# Content cues per article — what the image should depict
CONTENT_CUES = {
    'was-ist-ki': 'An abstract brain silhouette made from interlocking geometric shapes, with a single magenta node pulsing at the center.',
    'llm-vergleich': 'Four tall minimal columns of different heights on a horizon line, each a different shade of ink, the tallest one tipped with a magenta dot — like an editorial bar chart.',
    'dsgvo-ki': 'A stylized folder with a padlock, both rendered as thin line art, overlapping EU star pattern as faint background dots; one star replaced by a magenta asterisk.',
    'prompt-engineering': 'An abstract speech bubble opening into an ornate branching tree of thin lines, each branch ending in a small magenta dot — representing chain-of-thought.',
    'rag-erklaert': 'Two abstract shapes connected by a dashed line: on the left a stack of thin horizontal lines (documents), on the right a spiral (the retrieval process), joined by a magenta arrow.',
    'ki-bildgenerierung': 'A minimal composition showing noise dots on the left gradually organizing into a clean line-drawn landscape on the right, with a single magenta star in the sky.',
}

FALLBACK_CUE = 'An abstract compass needle pointing toward a small magenta dot, on an off-white background.'

def build_prompt(slug: str, title: str) -> str:
    cue = CONTENT_CUES.get(slug, FALLBACK_CUE)
    return (
        f"{STYLE_PREAMBLE}\n\n"
        f"Subject: {cue}\n"
        f"Context: Cover illustration for an article titled '{title}' in a German "
        f"wiki-style AI-tools encyclopedia. The illustration should feel intellectually "
        f"serious and editorial — not cute, not corporate, not technical-looking."
    )

# ---- Step 1: ensure the article schema has media_id (idempotent) ----
cts = requests.get(f'{BASE}/{SITE}/contenttypes/', headers=H, verify=False).json()
article_ct = next(c for c in cts if c.get('display_identifier') == 'article')
current_schema = article_ct.get('schema', {})
props = current_schema.get('properties', {})
if 'media_id' not in props:
    props['media_id'] = {
        'type': 'integer',
        'title': 'Aufmacherbild',
        'format': 'media_id',
        'description': 'Referenz auf das Media-Asset, das als Artikel-Aufmacher dient.',
    }
    new_schema = {**current_schema, 'properties': props}
    r = requests.patch(f'{BASE}/{SITE}/contenttypes/{article_ct["id"]}',
        json={'schema': new_schema}, headers=H, verify=False)
    if not r.ok:
        sys.exit(f'❌ schema patch failed: {r.status_code} {r.text[:300]}')
    print('  ✓ added media_id field to article schema')
else:
    print('  · article schema already has media_id')

# ---- Step 2: fetch article elements ----
items, page = [], 1
while True:
    r = requests.get(f'{BASE}/{SITE}/elements/?type_id={article_ct["id"]}&size=200&page={page}', headers=H, verify=False).json()
    items += r.get('items', [])
    if not r.get('has_next'): break
    page += 1
print(f'  · {len(items)} articles to process')

# ---- Step 3: generate + patch per article ----
no_credits = False
summary = []
for el in items:
    d = el['data']
    slug, title = d.get('slug'), d.get('title')
    if d.get('media_id') and not isinstance(d['media_id'], dict):
        print(f'  · {slug}: already has media_id={d["media_id"]}, skipping')
        summary.append((slug, 'skipped', d['media_id']))
        continue
    # For the resolved-object case (inlined Post-like), check if there's a media ref
    if isinstance(d.get('media_id'), dict) and d['media_id'].get('id'):
        print(f'  · {slug}: already has resolved media, skipping')
        summary.append((slug, 'skipped-resolved', None))
        continue

    prompt = build_prompt(slug, title)
    payload = {
        'prompt': prompt,
        'name': f'cover-{slug}',
        'aspect_ratio': '16:9',
        'sync_mode': True,
        'num_images': 1,
        'output_format': 'jpeg',
        'thinking_level': 'high',
    }
    print(f'\n  → {slug}: generating cover ...')
    r = requests.post(f'{BASE}/{SITE}/media/generate', json=payload, headers=H, verify=False, timeout=240)
    if r.status_code == 402:
        print(f'    ✗ insufficient AI credits — {r.json().get("detail",{}).get("message","")}')
        summary.append((slug, 'no-credits', None))
        no_credits = True
        continue
    if not r.ok:
        print(f'    ✗ {r.status_code} {r.text[:200]}')
        summary.append((slug, f'error-{r.status_code}', None))
        continue
    media = r.json()
    mid, murl = media.get('id'), media.get('url')
    print(f'    ✓ media #{mid} ({murl[:60]}…)')
    # Patch the element
    new_data = {**d, 'media_id': mid}
    r = requests.patch(f'{BASE}/{SITE}/elements/{el["id"]}',
        json={'data': new_data}, headers=H, verify=False)
    if not r.ok:
        print(f'    ✗ element patch failed: {r.status_code} {r.text[:200]}')
        summary.append((slug, f'patch-error', mid))
    else:
        summary.append((slug, 'generated', mid))
    time.sleep(1)

# ---- Summary ----
print('\n' + '='*60)
print('SUMMARY')
print('='*60)
for slug, status, mid in summary:
    badge = '✓' if status.startswith(('generated','skipped')) else '✗'
    print(f'  {badge} {slug:25} {status:20} {mid or ""}')

if no_credits:
    print('\n⚠️  Some articles could not be generated due to 0 AI credits.')
    print('   Top up at the Cognitor settings, then re-run this script.')
    print('   The script is idempotent — only missing covers will be regenerated.')
    sys.exit(2)
print('\n✓ All article covers generated.')
