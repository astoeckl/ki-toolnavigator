#!/usr/bin/env python3
"""Update GPT Image and Nano Banana to their v2 / Pro 2 versions (April 2026)."""
import requests, urllib3, json
from pathlib import Path

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ROOT = Path(__file__).resolve().parent.parent

ENV = {l.split('=',1)[0].strip(): l.split('=',1)[1].strip()
       for l in (ROOT/'.env').read_text().splitlines() if '=' in l and not l.startswith('#')}
BASE, SITE = ENV['BASEURL'], ENV['SITE']

r = requests.post(f'{BASE}/auth/login',
    data={'grant_type':'password','username':ENV['EMAIL'],'password':ENV['PW']},
    headers={'Content-Type':'application/x-www-form-urlencoded'}, verify=False)
H = {'Authorization': f'Bearer {r.json()["access_token"]}'}
JH = {**H, 'Content-Type':'application/json'}
print('✓ Logged in')

UPDATES = [
    # ---------------- GPT Image 2 ----------------
    {
        'element_id': 20015,
        'post_id': 669,
        'data_patch': {
            'name': 'GPT Image 2',
            'tagline': 'OpenAIs zweite Bildmodell-Generation — deutlich präziser bei Layout und Typografie, mit Reasoning-Schritt vor jedem Bild und 4K-Native-Output.',
            'price': 'In ChatGPT-Plus enthalten · API ab $0,03 / Bild',
            'rating': 4.8,
            'reviews': 7240,
            'pros': [
                'Reasoning-Schritt vor jeder Generierung (denkt Komposition durch)',
                'Native 4K-Auflösung ohne Upscaler',
                'Texttreue jetzt mit Layout-Verständnis (Spalten, Tabellen)',
                'Multi-Image-Composition wie Nano Banana',
            ],
            'cons': [
                'Reasoning-Modus erhöht Latenz auf 8–15 Sek.',
                'Pro-Bild-Kosten weiter über Open-Source-Modellen',
                'Inhaltsfilter strenger als FLUX/SDXL',
                'Datenresidenz USA bleibt (EU optional Enterprise)',
            ],
            'launched': '2026-03-18',
            'lastUpdated': '2026-04-30',
            'features': """- **Reasoning-Image**: Modell plant Komposition, Layout und Lichtsetzung vor der Pixel-Generierung.
- **Native 4K-Output** (3840×2160) ohne nachgeschalteten Upscaler.
- **Layout-aware Typografie**: Spalten, Tabellen, mehrsprachige Schilder werden korrekt aufgebaut.
- **Multi-Image-Composition**: bis zu 8 Referenzbilder pro Prompt (vgl. Nano Banana).
- **Conversational Editing** mit Iterationen über mehrere Turns.
- **Style-Reference**: visuelle Stilvorgabe als Bild-Upload.
- **C2PA-Wasserzeichen** und sichtbares Provenance-Tag in Sora Images.""",
            'pricing': """- **ChatGPT Free** · einzelne Bilder pro Tag mit GPT Image 2 (Standard-Quality).
- **ChatGPT Plus** · $20 / Mon. — großzügiges Kontingent inkl. Reasoning-Modus.
- **ChatGPT Pro** · $200 / Mon. — Priority Access, höchste Limits.
- **API low** · ca. $0,03 / Bild (1024 px).
- **API high (4K + reasoning)** · $0,12–$0,28 / Bild.
- **Enterprise** · auf Anfrage — SSO, EU-Datenresidenz, BAA.""",
        },
        'post_patch': {
            'title': 'GPT Image 2 im Überblick',
            'content': """**GPT Image 2** ist OpenAIs zweite Bildmodell-Generation, im März 2026 vorgestellt und seit April allgemein verfügbar. Wer GPT Image 1 bereits gut fand, bekommt mit v2 drei deutliche Sprünge: einen vorgeschalteten **Reasoning-Schritt**, **native 4K-Auflösung** und **Multi-Image-Composition**.

Der **Reasoning-Schritt** ist die konzeptionell spannendste Neuerung. Vor der Pixel-Generierung „überlegt" das Modell Komposition, Lichtführung, Perspektive und Typografie und erzeugt eine interne Layout-Skizze. Das Resultat: Schilder mit Tabellen, Plakate mit Spalten, Cover-Designs mit präziser Hierarchie funktionieren auf einem Niveau, das frühere Modelle nicht erreicht haben. Die Latenz steigt im Reasoning-Modus auf 8–15 Sekunden — ein bewusster Trade-off.

**Native 4K-Output** (3840×2160) ohne Upscaler-Pipeline ist der zweite Hebel: Print- und Display-Workflows kommen ohne Nachbearbeitung aus, Detailtiefe in Texturen und Schatten ist deutlich höher. Die API kennt drei Quality-Stufen (low/medium/high), die Pricing-Achse ist linear.

**Multi-Image-Composition** schließt die Lücke zu Nano Banana: bis zu 8 Referenzbilder pro Prompt werden konsistent verschmolzen — Person aus Bild 1, Outfit aus Bild 2, Hintergrund aus Bild 3. **Style-Reference** (visuelle Stilvorgabe als Upload) ist eine zusätzliche Achse für Brand-Konsistenz.

**Conversational Editing** funktioniert wie bei v1, ist aber spürbar genauer: „Mach das Hemd dunkler, ohne den Faltenwurf zu ändern" wird konsequenter respektiert. Edits über 5+ Turns bleiben stabil.

Schwächen: Der Reasoning-Modus ist langsamer — wer schnelle Iterationen braucht, schaltet ihn ab und arbeitet mit der Standard-Pipeline. Inhaltsfilter sind weiter strenger als bei FLUX oder SDXL, was für Werbung selten ein Problem ist, für künstlerische Arbeit aber. EU-Datenresidenz bleibt Enterprise-Feature.

Empfohlen für alle, die GPT Image 1 schon im Workflow hatten — Upgrade lohnt sich für Print, Layout-lastige Arbeit und Multi-Reference-Komposition. Für reine schnelle Mood-Bilder bleibt der Standard-Modus die richtige Wahl."""
        },
    },
    # ---------------- Nano Banana Pro 2 ----------------
    {
        'element_id': 20016,
        'post_id': 670,
        'data_patch': {
            'name': 'Nano Banana Pro 2',
            'tagline': 'Googles Gemini 3 Pro Image — die zweite Generation des „Nano Banana"-Modells: Reasoning-Image, 4K-Native, Texttreue auf GPT-Image-2-Niveau.',
            'price': 'In Gemini-App enthalten · API ab $0,034 / Bild',
            'rating': 4.9,
            'reviews': 8910,
            'pros': [
                'Texttreue jetzt auf GPT-Image-2-Niveau (Schilder, Logos)',
                'Charakter-Konsistenz weiter unschlagbar (bis zu 14 Refs)',
                'Native 4K-Output bei vergleichbarer Geschwindigkeit',
                'Reasoning-Modus „Think with Image"',
            ],
            'cons': [
                'Reasoning-Modus erhöht Latenz auf 5–10 Sek.',
                'Inhaltsfilter im Free-Tarif streng',
                'EU-Datenresidenz erst Enterprise (Vertex AI)',
                'Style-Diversität immer noch geringer als FLUX',
            ],
            'launched': '2026-03-25',
            'lastUpdated': '2026-04-30',
            'features': """- **Think with Image**: optionaler Reasoning-Schritt vor der Generierung (Komposition, Layout, Licht).
- **Native 4K-Output** (3840×2160) ohne Upscaler.
- **Charakter-Konsistenz** mit bis zu 14 Referenzbildern pro Prompt.
- **Layout-aware Texttreue**: Plakate, Tabellen, mehrsprachige Schilder.
- **Multi-Image-Editing** mit präziseren Masken und Selektionen.
- **Conversational Editing** in Gemini, AI Studio und Vertex.
- **Native Workspace-Integration** (Slides, Docs, Sheets).
- **SynthID 2.0**-Wasserzeichen, robuster gegen Crops und Re-Encoding.""",
            'pricing': """- **Gemini App** · Free mit Tageslimit, in Gemini Advanced ($20/Mon.) deutlich höher.
- **Google AI Studio** · Free zum Experimentieren, Standard-Quality.
- **API standard** · $0,034 / Bild (1024 px).
- **API 4K + Reasoning** · $0,11–$0,24 / Bild.
- **Workspace Enterprise** · Bilder im Slides- und Docs-Editor inkludiert.
- **Vertex AI** · Enterprise-Pricing mit EU-Region und SLA.""",
        },
        'post_patch': {
            'title': 'Nano Banana Pro 2 im Überblick',
            'content': """**Nano Banana Pro 2** ist Googles zweite Generation des im August 2025 anonym auf LMArena gestarteten Bildmodells — offiziell **Gemini 3 Pro Image**, im Code „Nano Banana 2" oder eben „Nano Banana Pro 2". Seit der Veröffentlichung Ende März 2026 hat das Modell die Spitze mehrerer Benchmark-Leaderboards zurückerobert.

Die größte Neuerung ist **Think with Image** — Googles Variante des Reasoning-Image-Ansatzes. Vor der Generierung plant das Modell Komposition, Layout, Lichtsetzung und Typografie in einer internen Skizze. Das Resultat ist eine **Texttreue auf GPT-Image-2-Niveau**: Schilder, Plakate, mehrsprachige Beschriftungen werden zuverlässig korrekt gerendert — die größte Schwäche der ersten Nano-Banana-Generation ist damit Geschichte.

Die historischen Stärken bleiben erhalten und werden ausgebaut: **Charakter-Konsistenz** funktioniert jetzt mit bis zu 14 Referenzbildern (vorher 8) — derselbe Mensch, dieselbe Brand-Welt, dieselbe Produktlinie über dutzende Bilder hinweg. **Multi-Image-Editing** ist präziser geworden, Masken und Selektionen werden treuer respektiert.

**Native 4K-Output** (3840×2160) ist neu und bleibt überraschend schnell: Standard-Generierung in 3–5 Sekunden, Reasoning-Modus in 5–10 Sekunden. Damit ist Nano Banana Pro 2 weiter das schnellste der neuen 4K-Reasoning-Modelle.

**Workspace-Integration** wurde ebenfalls upgegradet: Bildgenerierung in Slides und Docs läuft jetzt out-of-the-box mit dem Pro-Modell, kein Add-on mehr nötig. **SynthID 2.0** ist robuster gegen Crops, JPEG-Re-Encoding und Screenshot-Pipelines.

Schwächen: Inhaltsfilter sind im Free-Tarif weiter spürbar konservativ. EU-Datenresidenz bleibt Enterprise-Feature über Vertex AI mit europäischer Region. Style-Diversität ist gegenüber FLUX immer noch geringer — wer experimentell-künstlerisch arbeitet, hat bei den Open-Source-Modellen mehr Spielraum.

Empfohlen für alle, die Charakter-Konsistenz, Multi-Image-Workflows oder hohe Geschwindigkeit brauchen — und für Workspace-Nutzer:innen, die jetzt erstmals auch Schilder und Plakate zuverlässig im Bild bekommen. Der direkte Konkurrent zu GPT Image 2: Nano Banana Pro 2 gewinnt bei Speed und Charakter-Konsistenz, GPT Image 2 bei strenger Layout-Präzision."""
        },
    },
]

for upd in UPDATES:
    eid = upd['element_id']
    pid = upd['post_id']

    # Fetch current element
    r = requests.get(f'{BASE}/{SITE}/elements/{eid}', headers=JH, verify=False)
    r.raise_for_status()
    el = r.json()
    new_data = {**el['data'], **upd['data_patch']}

    # Patch element
    rp = requests.patch(f'{BASE}/{SITE}/elements/{eid}',
        json={'data': new_data}, headers=JH, verify=False)
    print(f'· element {eid} ({new_data["slug"]}) → {upd["data_patch"]["name"]}: {rp.status_code}')

    # Patch post
    rpp = requests.patch(f'{BASE}/{SITE}/posts/{pid}',
        json=upd['post_patch'], headers=JH, verify=False)
    print(f'  post {pid}: {rpp.status_code} · {len(upd["post_patch"]["content"])} chars')

print('\n✓ Done.')
