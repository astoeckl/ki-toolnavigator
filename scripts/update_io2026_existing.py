#!/usr/bin/env python3
"""Update existing Gemini, Stitch, Veo entries with Google I/O 2026 announcements."""
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
print('✓ Logged in')

UPDATES = [
    # ---------------- Gemini (I/O 2026: 3.5 Flash, Neural Expressive, Daily Brief) ----------------
    {
        'eid': 19891,
        'pid': 567,
        'data_patch': {
            'tagline': 'Googles Multimodal-LLM-Familie — mit Gemini 3.5 Flash als neuem Frontier-Modell (I/O 2026): 4× schneller bei Frontier-Reasoning, in App, AI Studio und Vertex.',
            'price': 'Gemini App Free · Google AI Pro $20/Mon. · Ultra $100/Mon.',
            'lastUpdated': '2026-05-08',
            'features': """- **Gemini 3.5 Flash** (I/O 2026): Frontier-Reasoning bei 4× Output-Speed, weniger als die Hälfte der Frontier-Kosten.
- **Gemini 3.5 Pro** in internem Test, Roll-out Juni 2026.
- **Native Multimodalität**: Text, Bild, Audio, Video als Input und Output.
- **Long Context** mit 2 Mio. Token bei Pro (1 Mio. bei Flash).
- **Tool-Use** und **Function Calling** mit strukturierten Schemas.
- **Neural Expressive Redesign** der Gemini App: fluide Animation, interaktive Embeds, neue Live-Erfahrung.
- **Daily Brief**: nächtliche Analyse von Inbox + Kalender als Tages-Briefing (US-Roll-out).
- **Verfügbar** in Gemini App, AI Studio, Vertex AI, Antigravity und ab sofort als Default in Google Search AI Mode.""",
            'pricing': """- **Gemini App Free** · Standard-Modell, Tageslimits, ohne Bild- und Video-Generierung in Premium-Qualität.
- **Google AI Pro** · $20 / Mon. — Gemini 3.5 Flash und Pro, höhere Limits, Daily Brief, Deep Research.
- **Google AI Ultra** · $100 / Mon. (I/O 2026) — 5× höhere Limits, 20 TB Cloud-Storage, Gemini Spark Beta, YouTube Premium Lite inkl.
- **API standard** (Gemini 3.5 Flash) · ab $0,30 / 1M In-Tokens, $1,20 / 1M Out-Tokens.
- **API premium** (Gemini 3.5 Pro) · höherer Tarif, ab Juni 2026.
- **Workspace Business+** · Gemini 3.5 in Gmail, Docs, Slides, Sheets inkl.""",
        },
        'post_append': """

---

**Update Mai 2026 — Google I/O 2026:** Google hat **Gemini 3.5 Flash** als neuen Frontier-Default vorgestellt — auf Coding- und Agentic-Benchmarks schlägt das Modell den bisherigen Gemini 3.1 Pro (Terminal-Bench 76,2 %, GDPval-AA 1.656 Elo), liefert dabei aber den 4× höheren Output-Speed der Flash-Serie und kostet „weniger als die Hälfte anderer Frontier-Modelle" auf Long-Horizon-Tasks. **Gemini 3.5 Pro** wird intern getestet und im Juni 2026 ausgerollt.

Die **Gemini App** wurde komplett mit dem neuen Design-System **„Neural Expressive"** überarbeitet — fluide Animationen, interaktive Embeds (zoomable Bilder, Timelines), neuer Gemini-Live-Modus mit verbesserter Stör-Geräusch-Robustheit. Neu in der App: **Daily Brief** — eine nächtliche Analyse von Gmail und Kalender, die morgens als prioritisierter Tagesplan bereitsteht (US-Roll-out, Google AI Subscriber, 18+).

Strategisch wichtig: Mit dem neuen **Google AI Ultra**-Plan ($100/Mon.) kommen 5× höhere Limits, 20 TB Cloud-Storage, **Gemini Spark Beta** (24/7-Personal-Agent) und YouTube Premium Lite ohne Aufpreis — eine deutliche Aufwertung der Top-Stufe."""
    },

    # ---------------- Google Stitch (I/O 2026: real-time collab, codebase imports) ----------------
    {
        'eid': 20023,
        'pid': 677,
        'data_patch': {
            'tagline': 'Googles UI-Designer mit Gemini 3.5 — seit I/O 2026 mit Real-Time-Collaboration via Text/Voice und Import bestehender Figma-Dateien oder Codebases als Startpunkt.',
            'price': 'Free in Public Preview · Custom-Bundling über Google AI Pro/Ultra',
            'lastUpdated': '2026-05-08',
            'features': """- **Text- und Voice-zu-UI** mit Gemini 3.5 Flash als Reasoning-Backbone.
- **Real-Time-Collaboration** (I/O 2026): mehrere Personen prompten parallel im selben Workspace.
- **Codebase- und Figma-Import** (I/O 2026): bestehende Projekte als Stil-Referenz.
- **Image-zu-UI** mit Foto, Skizze oder Screenshot.
- **Figma-Export** mit Layer-Struktur und Auto-Layout.
- **HTML/CSS-Code-Export** für Tailwind und Standard-CSS.
- **Mehrere Style-Modes**: Modern, Classic, Vibrant, Minimal.
- **Iteratives Editing** Screen-für-Screen.""",
        },
        'post_append': """

---

**Update Mai 2026 — Google I/O 2026:** Stitch wurde mit zwei wesentlichen Funktionen erweitert. **Real-Time-Collaboration** via Text oder Voice — mehrere Personen können parallel im selben Workspace prompten, Live-Cursor sehen, gegenseitig Edits beobachten. Für Workshop- und Design-Sprint-Workflows ein massiver Komfort-Gewinn gegenüber dem bisherigen Single-Player-Modus.

Zweitens: **Import bestehender Figma-Dateien und Codebases** als Stil-Referenz. Statt bei Null zu starten, lädt Stitch ein vorhandenes Design-System ein und generiert neue Screens im selben visuellen System. Für Teams mit etablierter Brand-Identity ein konstitutiver Vorteil.

Das Tool ist weiter in der Public Preview, läuft jetzt aber auf **Gemini 3.5 Flash** als Reasoning-Backbone — die Layout-Präzision hat damit spürbar zugelegt."""
    },

    # ---------------- Veo (I/O 2026: Gemini Omni complement) ----------------
    {
        'eid': 20066,
        'pid': 720,
        'data_patch': {
            'lastUpdated': '2026-05-08',
        },
        'post_append': """

---

**Update Mai 2026 — Google I/O 2026:** Auf der I/O 2026 hat Google **Gemini Omni** als neue, übergreifende Generative-Media-Modell-Familie vorgestellt — ein Modell, das Video, Bild, Audio und Text in einem Pass aus beliebigen Inputs generiert. Veo 3 bleibt das eigenständige Video-Spezial-Modell mit Cinematic-Reasoning und 8-Sek-Clips; Gemini Omni ergänzt es für längere, Multi-Modal kombinierte Workflows in der Gemini App, in Google Flow und in der YouTube Shorts Remix-Funktion. Veo-Nutzer:innen behalten ihren bestehenden Workflow; wer multimodale Inputs mischen will, greift zusätzlich zu Omni."""
    },
]

for upd in UPDATES:
    r = requests.get(f'{BASE}/{SITE}/elements/{upd["eid"]}', headers=H, verify=False)
    el = r.json()
    new_data = {**el['data'], **upd['data_patch']}
    rp = requests.patch(f'{BASE}/{SITE}/elements/{upd["eid"]}', json={'data': new_data}, headers=H, verify=False)
    print(f'element {upd["eid"]} ({new_data["slug"]}): patch {rp.status_code}')

    r = requests.get(f'{BASE}/{SITE}/posts/{upd["pid"]}', headers=H, verify=False)
    post = r.json()
    new_content = post['content'] + upd['post_append']
    rpp = requests.patch(f'{BASE}/{SITE}/posts/{upd["pid"]}', json={'content': new_content}, headers=H, verify=False)
    print(f'  post {upd["pid"]}: patch {rpp.status_code} · {len(new_content)} chars total')

print('\n✓ Done.')
