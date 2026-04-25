#!/usr/bin/env python3
"""Generate brand-styled cover images per tool via Cognitor's media/generate
(Nano Banana / Fal.ai with thinking_level=high), store them in Cognitor Media,
and reference them from the tool element via `media_id`.

Idempotent: skips tools that already have media_id set.
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

# ---- Brand style preamble — shared with article covers ----
STYLE_PREAMBLE = (
    "Editorial magazine illustration in a muted, hand-drawn style. "
    "Off-white paper background (#FAF8F5), deep ink black linework (#17140F), "
    "a single magenta accent color (#A01E78). "
    "1-pixel hairline strokes, no drop shadows, no gradients, no photorealism, "
    "no 3D rendering. Flat composition with generous negative space, "
    "reminiscent of a 1970s serif-typography editorial or a German tech magazine. "
    "Subject should be rendered as simple, abstract symbols or small vignettes, "
    "not as realistic imagery. No text, no letters, no logos in the image. "
    "Aspect ratio 16:9, composition centered with breathing room around the subject."
)

# Per-tool subject — abstract symbol that captures the tool's essence,
# never the tool's actual logo (no text, no real branding).
TOOL_CUES = {
    'chatgpt':          'A simple speech bubble with a single magenta dot inside it, surrounded by small concentric line ripples — symbolizing widespread, conversational AI.',
    'claude':           'A long horizontal scroll or unfolded book with thin parallel lines representing text, a magenta margin marker on the left edge — emphasizing depth and long context.',
    'gemini':           'Two abstract overlapping shapes (a triangle and a circle) with a magenta dot at their intersection — a quiet metaphor for multimodality.',
    'mistral':          'A minimal stylized wind shape (three flowing curved lines) with a magenta dot in the middle, gently bending right — fast, European, free-flowing.',
    'midjourney':       'An abstract painters palette as thin outlines, with one magenta dot of paint in the center — artistic, premium, hand-crafted.',
    'stable-diffusion': 'A small grid of dots gradually organizing into clean line shapes from left to right, single magenta dot at the rightmost — open, configurable diffusion.',
    'elevenlabs':       'A simple wave form with peaks of varying heights, the tallest peak tipped with a magenta dot — a voice waveform, minimal and editorial.',
    'runway':           'A small abstract film strip frame with motion blur lines emerging, a magenta star in one frame — moving image, generative video.',
    'cursor':           'A line-drawn editor caret (vertical bar with serifs) inside a faint code-bracket frame, the caret tinted magenta — IDE, fast typing.',
    'copilot':          'Two paper airplanes flying in close formation, one slightly ahead and rendered in magenta — pair-programming.',
    'notion-ai':        'A simple sheet of paper with thin horizontal lines, an upward-pointing magenta arrow rising from it — knowledge lifted out.',
    'perplexity':       'A magnifying glass over a stack of thin horizontal lines (citations), the lens itself outlined in magenta — research with sources.',
    'deepl-write':      'A fountain pen nib drawing a single horizontal line, a magenta dot at the tip of the nib — careful editing, German precision.',
    'aleph-alpha':      'A small fortified building (abstract castle shape with crenellations) drawn in line art, magenta flag on top — sovereign, on-premise AI.',
    # ---- new tools ----
    'ms-copilot':       'Four abstract documents arranged in a 2x2 grid, linked by thin lines, one document tinted magenta — an assistant weaving an office suite together.',
    'grok':             'A stylized lightning bolt cutting through a cluster of small chat-bubbles, the bolt rendered magenta — fast, irreverent real-time AI.',
    'deepseek':         'Two whales (an Orca-like silhouette) swimming in echelon formation, the leading one in magenta, the rest in thin line-art — open, collective, efficient.',
    'flux':             'A compass with three concentric rings and an arrow pointing to a magenta point on the horizon — European orientation, precision.',
    'ideogram':         'A serif capital letter shape drawn with precise contours inside an abstract frame, a magenta dot as counter — typography-first imagery.',
    'adobe-firefly':    'A firefly silhouette with a glowing magenta abdomen, surrounded by faint line-traces of wings — luminous, crafted, controlled.',
    'suno':             'A music staff with a single magenta note, simplified to three horizontal lines and one dot — condensed composition.',
    'synthesia':        'An abstract human silhouette inside a thin rectangular frame (like a video monitor), a magenta dot marking the mouth — synthetic presenter.',
    'windsurf':         'A stylized wave with a thin sail surfing its crest, the sail rendered magenta — velocity on top of code flow.',
    'n8n':              'A connected network of small circular nodes linked by curved lines, one central node magenta — modular workflow.',
    'make':             'Two interlocking gears with thin teeth, a magenta dot in the center of the smaller one — mechanical, integrating, automation.',
    'notebooklm':       'A spiral-bound notebook with a stylized sound-wave emerging from the page, the wave rendered magenta — notes becoming audio.',
    'julius':           'A scatter plot of line-art dots with one larger magenta dot highlighted, and a thin trend line — data analysis at a glance.',
    'neuroflash':       'A lightning bolt emerging from an abstract ink pen, the bolts tip magenta — instant copy, thought-in-motion.',
    'elicit':           'A magnifying glass over an open book with multiple thin bookmarks, one bookmark magenta — structured literature review.',
    # ---- April 2026 batch ----
    'llama':            'A stylized llama silhouette with a tightly wound coil of string forming the body, a magenta dot as the eye — open, friendly, weaving.',
    'cohere':           'A stylized graph with three concentric arcs meeting at a single magenta point — a quiet emblem of retrieval and ranking.',
    'recraft':          'A stylized vector pen tool with three control-point handles, one tinted magenta, drawing a smooth curve — the essence of vector design.',
    'pika':             'A small abstract film clip frame with a tiny magenta star bursting at one corner — playful, kinetic motion.',
    'heygen':           'A simple human silhouette inside a thin rectangular frame, with a small magenta speech-glow at the mouth — a synthetic presenter, calm and clean.',
    'descript':         'An abstract waveform morphing into typed text characters, the active cursor tinted magenta — text becoming sound.',
    'replit':           'A small browser window outline with a thin curved arrow exiting to the right, a magenta dot at the arrow tip — code becoming live deploy.',
    'zapier':           'Two small clouds connected by a thin lightning bolt, the bolt tinted magenta — connection across silos.',
    'otter':            'A small abstract microphone with three short text-line segments rising from it, the topmost line tinted magenta — speech turned into structured note.',
    'hex':              'A stylized hexagonal grid with three cells highlighted in line-art, one cell tinted magenta — modular analytics blocks.',
    'jasper':           'A stylized speech-bubble with a thin frame around it (the brand boundary), one corner tinted magenta — voice with structure.',
    'consensus':        'A stylized scale balance with three small dots on each pan, one central dot tinted magenta — measuring consensus.',
    # ---- Marketing batch April 2026 ----
    'copy-ai':          'A small abstract document fanning out into three arrows pointing right, the longest arrow tinted magenta — workflow-driven copy.',
    'writesonic':       'A stylized fountain pen nib with three small radiating sparks, one spark tinted magenta — energetic, multi-format writing.',
    'surfer-seo':       'A minimal cresting wave with a tiny surfboard at the peak, the board rendered magenta — riding the search ranking curve.',
    'frase':            'A stylized question-mark formed by an open book curve, a magenta dot as the question dot — research and answers.',
    'anyword':          'A simple bar-chart of three rising bars with a magenta dot crowning the tallest bar — performance-driven copy.',
    'typeface':         'A serif capital letter A inside a thin frame, with a small magenta brand mark in the corner — typography as enterprise identity.',
    'canva-magic':      'A wand outline with three sparkle marks emanating from its tip, the central sparkle tinted magenta — design conjured into being.',
    # ---- Agenten batch April 2026 ----
    'manus':            'A small line-drawn human hand reaching toward a single magenta dot at the end of a curved trajectory of small dots — autonomous reach.',
    'devin':            'A stylized bracket pair containing three vertical lines (representing code), one tinted magenta — autonomous code assembly.',
    'lindy':            'A small abstract bird silhouette with thin radiating connection lines, one line tinted magenta — agile, connected, helpful.',
    'crewai':           'Three small triangular figures arranged in a coordinated formation, one tinted magenta — a crew of specialized agents.',
    'langchain':        'A line of three interlocking ring-shapes, each ring drawn with thin contours, the middle ring tinted magenta — chained components.',
    'relevance-ai':     'A stylized abstract figure with three branching arms each holding a tiny tool symbol, the central arm tinted magenta — a digital workforce of skills.',
    'activepieces':     'Four interlocking puzzle-piece outlines arranged in a row, one piece tinted magenta — modular, open, composable.',
    # ---- Daten & Analyse batch April 2026 ----
    'powerbi-copilot':  'A clustered bar chart of three rising bars with a small magenta speech-bubble emerging from the tallest — analytics in conversation.',
    'thoughtspot':      'A magnifying glass over a small pie-chart fragment, the lens outlined in magenta — search-driven analytics.',
    'databricks-genie': 'A simple lamp outline with three rising thin lines that morph into bar shapes, one line tinted magenta — insight summoned from data.',
    'rows':             'A small grid of five horizontal lines with a magenta dot at the right end of one row — spreadsheet meets AI.',
    'akkio':            'A line chart trending upward with a magenta dot crowning the highest point and a faint forecast curve dotted ahead — predictive analytics.',
    'vanna-ai':         'An open speech-bubble pointing into a small abstract database cylinder, a magenta dot inside the bubble — natural-language SQL.',
    'dataiku':          'Three connected nodes (data, model, app) drawn with thin lines, the central node tinted magenta — end-to-end data flow.',
    # ---- Coding batch April 2026 ----
    'claude-code':      'A terminal-window outline with a thin blinking cursor inside and a small magenta chevron prompt — agentic command-line coding.',
    'codex-cli':        'A pair of overlapping curly braces { } with a tiny magenta cloud floating between them — code in the cloud and the shell.',
    'bolt':             'A lightning bolt outline split into two halves, the right half tinted magenta and resolving into a tiny browser-window glyph — instant full-stack apps.',
    'v0':               'A bold lowercase letter v with a small numeral 0 nested inside, the 0 tinted magenta — design becomes code.',
    'tabnine':          'Three stacked horizontal lines suggesting code, with a small magenta tab-key glyph hovering at the right edge — autocomplete on tap.',
    'continue':         'A sideways arrow built from short dashes that loops back into itself, the arrowhead tinted magenta — open extensible coding loop.',
    'aider':            'A small thin git-branch icon meeting a typed-prompt arrow, with a magenta dot at the merge node — pair-programming through commits.',
    # ---- Wissenschaft & Forschung batch April 2026 ----
    'scispace':         'An open book outline with a small magenta speech-bubble emerging from the spine — chat with research papers.',
    'scite':            'Three short tally lines, the first green-check, the second magenta-cross, the third grey-dash — supports, contrasts, mentions.',
    'researchrabbit':   'A small node-graph of three paper-rectangles connected by thin lines, the central paper tinted magenta — citation network discovery.',
    'connected-papers': 'A constellation of six small dots arranged in a loose orbit, two dots tinted magenta and connected by a curved line — co-citation map.',
    'semantic-scholar': 'A simple open book with a small thin search-magnifier hovering over the right page, the lens outlined in magenta — open academic search.',
    'litmaps':          'A horizontal timeline of five thin tick marks, two marks growing into small magenta sparkline branches — living citation map over time.',
    'scholarcy':        'A small flashcard rectangle with three thin horizontal lines and a magenta corner-fold — structured paper summary.',
}

# ---- Step 1: ensure tool schema has media_id (idempotent) ----
cts = requests.get(f'{BASE}/{SITE}/contenttypes/', headers=H, verify=False).json()
tool_ct = next(c for c in cts if c.get('display_identifier') == 'tool')
current_schema = tool_ct.get('schema', {})
props = current_schema.get('properties', {})
if 'media_id' not in props:
    props['media_id'] = {
        'type': 'integer',
        'title': 'Cover-Bild',
        'format': 'media_id',
        'description': 'Referenz auf das Media-Asset, das als Tool-Cover dient.',
    }
    new_schema = {**current_schema, 'properties': props}
    r = requests.patch(f'{BASE}/{SITE}/contenttypes/{tool_ct["id"]}',
        json={'schema': new_schema}, headers=H, verify=False)
    if not r.ok:
        sys.exit(f'❌ schema patch failed: {r.status_code} {r.text[:300]}')
    print('  ✓ added media_id field to tool schema')
else:
    print('  · tool schema already has media_id')

# ---- Step 2: fetch tool elements ----
items, page = [], 1
while True:
    r = requests.get(f'{BASE}/{SITE}/elements/?type_id={tool_ct["id"]}&size=200&page={page}', headers=H, verify=False).json()
    items += r.get('items', [])
    if not r.get('has_next'): break
    page += 1
print(f'  · {len(items)} tools to process')

def build_prompt(slug: str, name: str, vendor: str, category: str) -> str:
    cue = TOOL_CUES.get(slug, f'A small abstract emblem for an AI tool, with a single magenta dot.')
    return (
        f"{STYLE_PREAMBLE}\n\n"
        f"Subject: {cue}\n"
        f"Context: Cover illustration for the entry on the AI tool '{name}' "
        f"(vendor: {vendor}, category: {category}) in a German editorial AI-tool encyclopedia. "
        f"The illustration must be intellectually serious and editorial — never cute, "
        f"never corporate, never resembling the real product logo."
    )

# ---- Step 3: generate + patch per tool ----
summary = []
for el in items:
    d = el['data']
    slug, name = d.get('slug'), d.get('name')
    if d.get('media_id'):
        # Already has media — could be int, dict, or resolved string
        kind = type(d['media_id']).__name__
        print(f'  · {slug}: already has media_id ({kind}), skipping')
        summary.append((slug, 'skipped', None))
        continue

    prompt = build_prompt(slug, name, d.get('vendor', ''), d.get('category', ''))
    payload = {
        'prompt': prompt,
        'name': f'tool-{slug}',
        'aspect_ratio': '16:9',
        'sync_mode': True,
        'num_images': 1,
        'output_format': 'jpeg',
        'thinking_level': 'high',
    }
    print(f'\n  → {slug}: generating cover ...')
    r = requests.post(f'{BASE}/{SITE}/media/generate', json=payload, headers=H, verify=False, timeout=240)
    if not r.ok:
        print(f'    ✗ {r.status_code} {r.text[:200]}')
        summary.append((slug, f'error-{r.status_code}', None))
        continue
    media = r.json()
    mid, murl = media.get('id'), media.get('url')
    print(f'    ✓ media #{mid} ({(murl or "")[:60]}…)')
    new_data = {**d, 'media_id': mid}
    r = requests.patch(f'{BASE}/{SITE}/elements/{el["id"]}',
        json={'data': new_data}, headers=H, verify=False)
    if not r.ok:
        print(f'    ✗ element patch failed: {r.status_code} {r.text[:200]}')
        summary.append((slug, 'patch-error', mid))
    else:
        summary.append((slug, 'generated', mid))
    time.sleep(0.5)

# ---- Summary ----
print('\n' + '='*60)
print('SUMMARY')
print('='*60)
for slug, status, mid in summary:
    badge = '✓' if status.startswith(('generated','skipped')) else '✗'
    print(f'  {badge} {slug:20} {status:18} {mid or ""}')
print('\n✓ Tool covers complete.')
