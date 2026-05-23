#!/usr/bin/env python3
"""Seed editorial article: 'Wie KI die Google-Suche verändert hat'.
Creates Post + Article element + generates cover via Nano Banana.
Idempotent: skips if slug already exists.
"""
import requests, urllib3
from pathlib import Path

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ROOT = Path(__file__).resolve().parent.parent
ENV = {l.split('=',1)[0].strip(): l.split('=',1)[1].strip()
       for l in (ROOT/'.env').read_text().splitlines() if '=' in l and not l.startswith('#')}
BASE, SITE = ENV['BASEURL'], ENV['SITE']

ARTICLE = {
    'slug': 'ki-google-suche',
    'title': 'Wie KI die Google-Suche verändert hat',
    'category': 'Praxis',
    'author': 'Redaktion',
    'date': '2026-05-08',
    'readTime': 13,
    'toc': [
        'Von zehn blauen Links zur generativen Antwort',
        'Die Chronologie: SGE, AI Overviews, AI Mode',
        'Wie AI Overviews technisch funktionieren',
        'AI Mode: Die zweite Stufe',
        'Die I/O-2026-Welle: Multimodal, Agenten, Generative UI',
        'Auswirkungen auf SEO und Marketing',
        'Auswirkungen auf Publisher und das offene Web',
        'Was als Nächstes kommt',
        'Fazit',
    ],
    'lead': (
        'In nur drei Jahren hat Google die Suchergebnisseite — das digitale Wohnzimmer einer halben '
        'Milliarde Menschen — komplett umgebaut. AI Overviews, AI Mode, Search Agents und die neue '
        'multimodale Suchleiste markieren den größten Schnitt seit 1998. Eine nüchterne Bestandsaufnahme '
        'der Veränderung und ihrer Folgen für Nutzer:innen, Publisher und Marketing-Teams.'
    ),
    'content': """## Von zehn blauen Links zur generativen Antwort

Über zwei Jahrzehnte war die Google-Suchergebnisseite konzeptionell stabil: zehn Treffer, ein paar Anzeigen oben, Featured Snippets für ausgewählte Fragen, daneben People Also Ask. Wer eine Frage hatte, klickte zu einem Quell-Dokument und las dort die Antwort.

Diese Architektur kippt seit 2023 — und sie kippt schneller, als die meisten Beobachter:innen erwartet hatten. Im Mai 2024 wurde die experimentelle „Search Generative Experience" (SGE) in **AI Overviews** umbenannt und für alle US-Nutzer:innen freigeschaltet. Ein gutes Jahr später, im Februar 2026, erschienen AI Overviews bereits in **59,7 % aller Suchanfragen** — eine Verdopplung in unter zwölf Monaten. Im Mai 2026 verkündete Google auf der I/O die „größte Änderung der Suchleiste in über 25 Jahren": eine komplett neue, multimodale Eingabe für Text, Bild, Video, Dateien und Browser-Tabs in einem.

Was sich dabei verschiebt, ist nicht nur die Oberfläche — es ist das **Verhältnis zwischen Suchanfrage und Antwort**. Die Suche schickt Nutzer:innen nicht mehr zu Quellen; sie liefert die Antwort selbst. Dieser Artikel zeichnet nach, wie es dazu kam, was das technisch bedeutet und welche Konsequenzen sich daraus für SEO, Marketing, Publisher und die Architektur des offenen Webs ergeben.

## Die Chronologie: SGE, AI Overviews, AI Mode

Die Veränderung ist nicht über Nacht passiert. Eine kompakte Timeline:

- **Mai 2023:** Google stellt SGE als Labs-Experiment in den USA vor — generierte Antworten oben auf der SERP, ergänzt durch traditionelle Trefferliste.
- **Mai 2024:** SGE wird in **AI Overviews** umbenannt und für alle US-Nutzer:innen ohne Labs-Opt-In freigeschaltet.
- **Oktober 2024:** AI Overviews rollen in über 100 Länder und mehrere Sprachen aus. Studien zeigen damals nur ~4,5 % AI-Overview-Quote.
- **März 2025:** **AI Mode** startet in den Labs — eine separate, vollständig konversationelle Such-Erfahrung mit Follow-up-Fragen und Multi-Schritt-Reasoning.
- **Mai 2025:** Google I/O 2025 — Gemini 2.5 wird zum Standard-Modell für Overviews und AI Mode.
- **Juli 2025:** AI Mode verlässt die Labs und ist für alle US-Nutzer:innen verfügbar.
- **Oktober 2025:** AI Mode rollt in 40+ neue Länder und 35+ neue Sprachen aus — insgesamt 200+ Länder.
- **Januar 2026:** Gemini 3 wird globaler Default für AI Overviews.
- **Februar 2026:** AI Overviews erscheinen in 59,7 % der Anfragen, mit durchschnittlich 15,2 Quellen-Links pro Overview — mehr als doppelt so viel wie im November 2024 (6,8 Links).
- **Mai 2026 (I/O 2026):** Komplett neu gestaltete Suchleiste, **Search Agents**, **Generative UI** und **Universal Cart** als nächste Stufe.

Die Geschwindigkeit ist bemerkenswert. Was in den 2000ern ein Jahrzehnt brauchte (Featured Snippets, Knowledge Panel, People Also Ask), wurde hier in einem Bruchteil der Zeit ausgerollt — und ist tiefer in die Kern-Such-Erfahrung integriert als alles davor.

## Wie AI Overviews technisch funktionieren

Hinter einem AI Overview steht keine einfache Schablone, sondern eine mehrstufige Pipeline:

1. **Query-Interpretation:** Gemini analysiert die Frage und entscheidet, ob sie für ein AI Overview geeignet ist (faktisch, mehrteilig, vergleichend) oder ob die klassische Treffer-Liste besser dient (Brand-Suche, transaktional, frische News).
2. **Retrieval:** Das System ruft eine größere Menge potenziell relevanter Quell-Dokumente ab — typisch 10 bis 30 Seiten aus dem Google-Index, ergänzt um Knowledge-Graph-Fakten, Shopping-Daten und ggf. YouTube-Inhalte.
3. **Reasoning + Synthese:** Gemini extrahiert die für die Frage relevanten Aussagen, gewichtet sie nach Konsistenz und Quell-Vertrauenswürdigkeit, und formuliert eine zusammenhängende Antwort.
4. **Citation-Linking:** Jeder generierte Satz oder Abschnitt wird mit einer Quell-Citation versehen — sichtbar als kleines Icon oder im erweiterten „Source Panel".
5. **Refinement-Loop:** Folgefragen oder Klicks auf Citations können das Overview erweitern oder verfeinern, ohne die Suche zu verlassen.

Wichtig ist die **Multi-Source-Synthese**: Anders als ein klassisches Featured Snippet, das genau eine Quelle paraphrasierte, kombiniert ein AI Overview Information aus 5 bis 15+ Quellen. Im Februar 2026 lag der Durchschnitt bei 15,2 zitierten Quellen pro Overview — Tendenz weiter steigend.

Das **Zitations-Modell** ist dabei ein bewusster Kompromiss: Google will den Eindruck unterstützen, dass die Antwort durch echte Web-Quellen gedeckt ist, nicht durch reines Modell-Wissen halluziniert. Studien zeigen aber, dass nur ein kleiner einstelliger Prozentsatz der Nutzer:innen tatsächlich auf eine Citation klickt — die Antwort allein reicht den meisten.

## AI Mode: Die zweite Stufe

Während AI Overviews die klassische SERP erweitern, ist **AI Mode** eine bewusst andere Such-Erfahrung. Statt einer einmaligen Antwort eröffnet sich ein **konversationeller Modus**: Folgefragen, „erkläre das genauer", Vergleichstabellen, parallele Sub-Recherchen — alles in einem fortlaufenden Dialog.

Drei Eigenschaften unterscheiden AI Mode von einem klassischen Chatbot wie Gemini, ChatGPT oder Claude:

- **Live-Web-Retrieval bei jeder Antwort.** AI Mode greift nicht auf einen Trainings-Snapshot zurück, sondern indexiert pro Anfrage frische Web-Quellen. Für aktuelle Themen ist das ein klarer Vorteil gegenüber Standalone-Chatbots.
- **Multi-Schritt-Reasoning mit „Query Fan-Out".** Bei komplexen Fragen zerlegt das System die Anfrage automatisch in Teil-Fragen, recherchiert sie parallel und fasst die Ergebnisse zusammen — das war zuvor das exklusive Territorium von Deep-Research-Tools.
- **Multimodalität als Default.** Bilder, PDFs, Screenshots, gerade auf Mobile sogar Echtzeit-Kamera-Eingaben sind regulärer Input — nicht ein Extra-Feature.

In der Reichweite ist AI Mode noch deutlich kleiner als AI Overviews (im Mai 2026 schätzungsweise 200–300 Mio. monatliche Nutzer:innen gegenüber 1+ Mrd. für die Hauptsuche), wächst aber stark — vor allem auf Mobile.

## Die I/O-2026-Welle: Multimodal, Agenten, Generative UI

Auf der Google I/O 2026 wurde die nächste Welle vorgestellt — und sie geht deutlich weiter als ein neues Modell:

**Reimagined Search Bar** mit nativer Multimodalität: Text, Bilder, Dateien, Videos und sogar offene Chrome-Tabs werden als gleichwertige Inputs behandelt. Wer ein Foto eines defekten Bauteils mit einer PDF des Reparatur-Handbuchs kombinieren will, prompt es in einem Schritt. Google nennt es die „größte Änderung der Suchleiste in über 25 Jahren" — das ist nicht nur Marketing, sondern beschreibt einen echten konzeptionellen Schnitt: die Suche wird vom **Text-Indexer** zum **Multimodal-Reasoning-Hub**.

**Search Agents** sind Hintergrund-Agents, die ein Thema 24/7 für Nutzer:innen beobachten — neue Studien zu einem Forschungsgebiet, Preisbewegungen für ein Produkt, Updates zu einer Gesetzesänderung. Statt selbst alle paar Tage zu suchen, bekommen Nutzer:innen synthetisierte Updates. Roll-out im Sommer 2026 für Google AI Pro/Ultra.

**Generative UI in Search** ist konzeptionell die ambitionierteste Änderung: Statt einer statischen SERP rendert Google für komplexe Anfragen eine **maßgeschneiderte Oberfläche** — interaktive Tabellen, Simulations-Widgets, kleine projektspezifische Mini-Apps. Wer „Hochzeitsplanung in München für 80 Gäste" sucht, bekommt nicht 10 Links, sondern eine kompakte Mini-App mit Budget-Rechner, Location-Vergleich und Timeline-Generator.

**Universal Cart** vereint Shopping über Suche, Gemini, YouTube und Gmail in einen einzigen Einkaufswagen — mit Background-Preis-Tracking, Stock-Alerts und einem neuen Bezahl-Protokoll (UCP). Für E-Commerce-Anbieter bedeutet das eine neue Distributions-Schicht zwischen Customer und Shop.

Das gemeinsame Muster: Google verlagert nicht nur die Antwort, sondern auch **Folge-Aktionen** auf seine Plattform. Wer auf einer SERP bleibt, statt zu einem Shop zu klicken, generiert weniger Daten für den Shop, weniger Werbe-Inventar für Publisher, weniger Klicks für SEO — und mehr Engagement und Werbe-Reichweite für Google selbst.

## Auswirkungen auf SEO und Marketing

Die Auswirkungen auf das SEO-Handwerk sind massiv und vielschichtig:

- **Click-Through-Rates auf Position 1 sinken spürbar.** Mehrere Studien aus 2025/26 zeigen Rückgänge zwischen 20 und 40 % auf Top-Positionen, sobald ein AI Overview erscheint — die Antwort wird oben gelesen, der Klick zur Quell-Seite entfällt.
- **„Zero-Click-Searches" werden zur Norm.** Bereits 2023 lag der Anteil bei ~57 %; in einer Welt mit AI Overviews auf 60 % der Anfragen verschärft sich dieser Trend deutlich.
- **Citations werden zur neuen Währung.** Wer in einem Overview als Quelle zitiert wird, bekommt Marken-Sichtbarkeit auch ohne Klick. SEO-Teams optimieren entsprechend für **„AIO-Inclusion"** — kurz formuliert: Strukturierte Antworten, klare H2-Hierarchien, prägnante Definitionen, schema.org-Markups.
- **Long-Tail-Queries verlieren an Bedeutung.** Komplexe, mehrstufige Fragen werden vom Overview oder AI Mode direkt beantwortet — die alte Strategie, viele Long-Tail-Seiten mit lockerem Tooltip-Content zu schreiben, verliert ihren ROI.
- **Brand-Search, transaktionale Queries und News-Queries bleiben relativ stabil** — hier zeigt Google weiter primär klassische Trefferlisten und Shopping-Karten.

Die neue SEO-Disziplin trägt schon einen Namen: **Generative Engine Optimization** (GEO) oder **AI Overview Optimization** (AIOO). Die Konsens-Empfehlungen haben sich 2026 verfestigt: Klare Struktur, semantisches HTML, deutliche Themen-Schwerpunkte pro Seite, autoritative Quellen-Backings, Entitäten-Optimierung im Knowledge-Graph, schnelle Page-Performance.

Im Marketing-Mix verschieben sich die Hebel: **Brand-Awareness** wird wichtiger, weil Markennennung in einem Overview oder AI Mode die einzige bleibende Sichtbarkeit ohne Klick ist. **Performance-Channels** außerhalb der Google-Suche (TikTok, LinkedIn, Reddit, Newsletter) gewinnen relativ an Gewicht.

## Auswirkungen auf Publisher und das offene Web

Für Publisher — Nachrichten-Seiten, Magazine, Fach-Blogs, Foren — ist die Situation existenziell. Die Klicks, die viele Verlage als Haupt-Refinanzierungsquelle nutzen, brechen weg, während die Inhalte selbst weiter genutzt werden. Mehrere große US-Verlage (NYT, WSJ, Daily Mail) haben 2025/26 öffentlich über Klick-Rückgänge zwischen 25 und 50 % berichtet — bei gleichbleibender oder steigender Web-Sichtbarkeit ihrer Inhalte.

Die rechtliche Reaktion folgt: In der EU laufen mehrere Klagen wegen unzureichender Vergütung im Rahmen des Leistungsschutzrechts. In den USA gibt es ähnliche Bemühungen über Copyright-Klagen und Anti-Trust-Verfahren. Google bietet seit 2025 punktuelle Lizenz-Deals an (Reddit, AP, einige große Verlage), das Ökosystem als Ganzes bleibt aber im Wartestand.

Die strukturelle Frage dahinter ist offen: Wenn die Refinanzierung des offenen Webs zu einem signifikanten Teil aus Klicks bestand und diese Klicks durch generative Antworten ersetzt werden, was bezahlt dann zukünftig die Recherche und das Schreiben? Die Diskussion oszilliert zwischen vier Modellen:

- **Lizenz-Deals** zwischen großen Plattformen und ausgewählten Publishern (aktuell der dominante Trend).
- **Paywalls und Abos** als Ergänzung oder Ersatz zu Werbe-Refinanzierung.
- **Branchen-übergreifende Tantieme-Modelle** ähnlich der Musik-Industrie (in der EU diskutiert, in den USA blockiert).
- **Eine grundlegende Reduktion der Web-Inhalte-Produktion** — der pessimistische Pfad, bei dem Quell-Inhalte schlicht weniger werden.

Welcher Pfad sich durchsetzt, ist 2026 noch nicht entschieden. Klar ist aber: Die Annahme „solange Suche Traffic schickt, finanziert sich das Web selbst" trägt nicht mehr.

## Was als Nächstes kommt

Drei Entwicklungslinien zeichnen sich für die nächsten 12–24 Monate ab:

**Erstens: Agenten in der Suche.** Search Agents (I/O 2026 angekündigt) sind nur der Anfang. Die nächste Stufe sind Agenten, die nicht nur recherchieren, sondern handeln — Buchungen, Käufe, Anfragen, Reservierungen über das **Universal Commerce Protocol**. Wer bei OpenAI Operator oder Anthropic Computer Use beobachtet hat, wo das hingeht, sieht die Stoßrichtung.

**Zweitens: Die Hardware-Seite.** Mit Android-XR-Brillen, die seit Herbst 2026 ausgerollt werden, bekommt die Suche eine ambiente Komponente — Antworten erscheinen kontextuell zur visuellen Umgebung, ohne dass nach ihnen gefragt wird. Was lange als Sci-Fi-Vision galt, wird real verfügbar.

**Drittens: Wettbewerb durch reine LLM-Anbieter.** ChatGPT-Search, Perplexity, Claude-Search und You.com haben in den letzten zwei Jahren beachtliche Reichweite aufgebaut. Insbesondere ChatGPT mit über 700 Mio. wöchentlich aktiven Nutzern hat das Potenzial, die Such-Hoheit von Google ernsthaft zu fragmentieren. Google reagiert mit aggressiveren Releases und tieferer Integration in das eigene Ökosystem — der Wettbewerb wird härter, nicht weicher.

## Fazit

Die Google-Suche, wie wir sie 2022 kannten, existiert 2026 nicht mehr. An ihre Stelle ist ein hybrides System getreten, das traditionelle Treffer-Listen, generative Antworten, konversationelle AI-Mode-Erfahrungen, multimodale Inputs und autonome Agenten in einer Oberfläche kombiniert.

Für Nutzer:innen bringt das spürbare Komfort-Gewinne — weniger Klicks zu Lese-Antworten, bessere Synthese aus vielen Quellen, multimodale Eingaben. Für Publisher und Marketer ist die Lage komplexer: Die Spielregeln, die zwei Jahrzehnte stabil waren, sind im Fluss, und nicht alle bisherigen Strategien überleben den Übergang.

Was bleibt, ist die zentrale Rolle der Suche als Default-Tor zum digitalen Wissen. Nur die Architektur dieses Tors hat sich verschoben — von einem Index, der zu Antworten führte, zu einer generativen Schicht, die Antworten selbst produziert. Wer in dieser Welt sichtbar bleiben will, muss verstehen, wie diese Schicht funktioniert, was sie zitiert und was sie ausblendet."""
}

CONTENT_CUE = (
    'A clean editorial vignette of the classic Google search bar reinterpreted: '
    'a thin horizontal line-art rectangle for the search box, but instead of a single '
    'cursor inside it shows three small overlapping abstract glyphs — a tiny page, a tiny '
    'speech bubble, and a tiny camera-aperture — all drawn with hairline strokes. '
    'A single magenta sparkle hovers at the top-right of the box. Generous white space below.'
)

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

# ---- Login ----
r = requests.post(f'{BASE}/auth/login',
    data={'grant_type':'password','username':ENV['EMAIL'],'password':ENV['PW']},
    headers={'Content-Type':'application/x-www-form-urlencoded'}, verify=False)
H = {'Authorization': f'Bearer {r.json()["access_token"]}', 'Content-Type':'application/json'}
print('✓ Logged in')

# ---- Resolve content type ----
cts = requests.get(f'{BASE}/{SITE}/contenttypes/', headers=H, verify=False).json()
article_ct = next(c for c in cts if c.get('display_identifier') == 'article')
ART_CT_ID = article_ct['id']

# ---- Idempotency: skip if slug exists ----
items, page = [], 1
while True:
    rj = requests.get(f'{BASE}/{SITE}/elements/?type_id={ART_CT_ID}&size=200&page={page}', headers=H, verify=False).json()
    items += rj.get('items', [])
    if not rj.get('has_next'): break
    page += 1
existing = next((el for el in items if el['data'].get('slug') == ARTICLE['slug']), None)

if existing:
    print(f'· article {ARTICLE["slug"]} already exists (id={existing["id"]}), reusing')
    el_id = existing['id']
    existing_data = existing['data']
else:
    post_payload = {
        'title': ARTICLE['title'],
        'slug': f'{ARTICLE["slug"]}-content',
        'content': ARTICLE['content'],
        'short_description': ARTICLE['lead'],
        'status': 'published',
    }
    rp = requests.post(f'{BASE}/{SITE}/posts/', json=post_payload, headers=H, verify=False)
    rp.raise_for_status()
    post_id = rp.json()['id']
    print(f'✓ post #{post_id} ({len(ARTICLE["content"])} chars content, {len(ARTICLE["lead"])} chars lead)')

    payload = {'type_id': ART_CT_ID, 'published': True, 'data': {
        'slug': ARTICLE['slug'],
        'title': ARTICLE['title'],
        'category': ARTICLE['category'],
        'author': ARTICLE['author'],
        'date': ARTICLE['date'],
        'readTime': ARTICLE['readTime'],
        'toc': ARTICLE['toc'],
        'post_id': post_id,
    }}
    re_ = requests.post(f'{BASE}/{SITE}/elements/', json=payload, headers=H, verify=False)
    if not re_.ok:
        raise SystemExit(f'✗ element create failed: {re_.status_code} {re_.text[:300]}')
    el = re_.json()
    el_id = el['id']
    existing_data = el['data']
    print(f'✓ article element #{el_id}')
    if not el.get('published'):
        requests.patch(f'{BASE}/{SITE}/elements/{el_id}',
            json={'published': True}, headers=H, verify=False)

# ---- Generate cover ----
if existing_data.get('media_id') and not isinstance(existing_data.get('media_id'), dict):
    print(f'· cover already set: media_id={existing_data["media_id"]}')
else:
    prompt = (
        f"{STYLE_PREAMBLE}\n\n"
        f"Subject: {CONTENT_CUE}\n"
        f"Context: Cover illustration for an article titled '{ARTICLE['title']}' "
        f"in a German wiki-style AI-tools encyclopedia. The illustration should feel "
        f"intellectually serious and editorial — not cute, not corporate, not technical-looking."
    )
    media_payload = {
        'prompt': prompt,
        'name': f'cover-{ARTICLE["slug"]}',
        'aspect_ratio': '16:9',
        'sync_mode': True,
        'num_images': 1,
        'output_format': 'jpeg',
        'thinking_level': 'high',
    }
    print(f'\n→ generating cover ...')
    rg = requests.post(f'{BASE}/{SITE}/media/generate', json=media_payload, headers=H, verify=False, timeout=240)
    if rg.status_code == 402:
        print(f'  ✗ insufficient AI credits: {rg.json().get("detail",{}).get("message","")}')
    elif not rg.ok:
        print(f'  ✗ {rg.status_code} {rg.text[:300]}')
    else:
        media = rg.json()
        mid = media.get('id')
        print(f'  ✓ media #{mid}')
        new_data = {**existing_data, 'media_id': mid}
        rp2 = requests.patch(f'{BASE}/{SITE}/elements/{el_id}',
            json={'data': new_data}, headers=H, verify=False)
        print(f'  ✓ element patch: {rp2.status_code}')

print('\n✓ Done.')
