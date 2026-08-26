#!/usr/bin/env python3
"""Seed editorial article: 'KI-Wasserzeichen: Wie Texte ihre Herkunft verraten'.
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
    'slug': 'ki-wasserzeichen',
    'title': 'KI-Wasserzeichen: Wie Texte ihre Herkunft verraten',
    'category': 'Technik',
    'author': 'Redaktion',
    'date': '2026-08-26',
    'readTime': 13,
    'toc': [
        'Das Provenienz-Problem',
        'Wie Text-Wasserzeichen funktionieren',
        'Anthropics Wasserzeichen für Claude',
        'Was Wasserzeichen nicht leisten',
        'Bilder, Audio und Video: C2PA und SynthID',
        'Der regulatorische Rahmen: EU AI Act',
        'Was das für die Praxis bedeutet',
        'Fazit',
    ],
    'lead': (
        'Seit August 2026 versehen erste Anbieter die Texte ihrer Sprachmodelle mit unsichtbaren '
        'Wasserzeichen. Anthropic hat den Anfang gemacht. Wie die Technik funktioniert, was sie '
        'zuverlässig leistet — und warum sie das Problem der KI-Erkennung trotzdem nicht löst.'
    ),
    'content': """## Das Provenienz-Problem

Die Frage klingt simpel und ist doch technisch überraschend hart: **Stammt dieser Text von einer Maschine?** Lehrende stellen sie sich bei Hausarbeiten, Redaktionen bei eingereichten Beiträgen, Personalabteilungen bei Anschreiben, Plattformen bei Bewertungen und Kommentaren.

Die verbreitete Antwort waren bislang sogenannte **KI-Detektoren** — Dienste wie GPTZero oder Turnitins KI-Erkennung, die einen Text statistisch auf „maschinelle" Merkmale prüfen: gleichmäßige Satzlängen, geringe Überraschung in der Wortwahl, wenig stilistische Ausreißer. Das Problem: Diese Werkzeuge **raten von außen**. Sie kennen weder das Modell noch den Entstehungsprozess und liefern deshalb systematisch Fehlurteile. Besonders betroffen sind Menschen, die in einer Fremdsprache schreiben, oder Autor:innen mit bewusst klarem, schnörkellosem Stil — ihre Texte sehen statistisch „zu glatt" aus. Es hat reale Fälle gegeben, in denen Studierende auf Basis solcher Werte zu Unrecht des Betrugs bezichtigt wurden.

Wasserzeichen drehen den Ansatz um. Statt einen fertigen Text von außen zu beurteilen, hinterlässt **der Erzeuger selbst** beim Schreiben ein Signal — eine Art unsichtbare Signatur, die später mit dem passenden Schlüssel nachweisbar ist. Das ist konzeptionell etwas völlig anderes: kein Ratespiel über Stil, sondern ein statistischer Nachweis mit bekannter Herkunft.

> **Video zum Thema:** Eine kompakte, visuelle Erklärung des Verfahrens gibt das Video [„Understanding Text Watermarking – How AI Text Carries an Invisible Signature"](https://youtu.be/0jAtFkN6DFs) von Andreas Stöckl — empfehlenswert, wenn man den Mechanismus einmal Schritt für Schritt sehen möchte.

## Wie Text-Wasserzeichen funktionieren

Bei Bildern ist ein Wasserzeichen anschaulich: Man verändert einzelne Pixel so geringfügig, dass das Auge nichts merkt, ein Detektor das Muster aber findet. Bei Text ist das ungleich schwieriger. Ein Text hat keine „unwichtigen Pixel" — jedes Zeichen ist bedeutungstragend. Unsichtbare Sonderzeichen oder manipulierte Leerzeichen, wie sie früher diskutiert wurden, überleben kein Copy-Paste in ein einfaches Textfeld.

Der heute maßgebliche Ansatz heißt **SynthID-Text** und wurde von Google DeepMind entwickelt; die Methode wurde 2024 in *Nature* veröffentlicht. Der Trick setzt an einer Eigenschaft an, die alle Sprachmodelle teilen: **Zufall bei der Wortwahl**.

Ein Sprachmodell berechnet für jedes nächste Wort eine Wahrscheinlichkeitsverteilung. Häufig gibt es nicht *eine* richtige Fortsetzung, sondern viele gleichwertige: „Das Ergebnis war **bemerkenswert** / **erstaunlich** / **beachtlich** / **überraschend**". Welches Wort tatsächlich erscheint, entscheidet normalerweise ein Zufallsgenerator.

Genau hier greift das Wasserzeichen ein. Statt echtem Zufall nutzt das Modell eine **kryptografisch abgeleitete Pseudozufallsfolge**: Ein geheimer Schlüssel wird mit dem unmittelbar vorangehenden Textkontext kombiniert und bestimmt, welche der gleichwertigen Alternativen bevorzugt wird. Anthropic verwendet dafür ein hübsches Bild: Es ist, als würde man beim Brettspiel statt zu würfeln die Nachkommastellen der Kreiszahl Pi verwenden — die Quelle der Zufälligkeit ändert sich, das Spiel bleibt dasselbe.

Für Leser:innen ist das Ergebnis **nicht unterscheidbar**. Es werden keine versteckten Zeichen eingefügt, keine zusätzlichen Tokens angehängt, nichts markiert. Der Text liest sich exakt wie zuvor.

Sichtbar wird die Signatur erst **statistisch, über viele Wörter hinweg**. Ein Detektor, der denselben Schlüssel besitzt, kann für jede einzelne Wortentscheidung prüfen: Passt die getroffene Wahl zu dem, was der Schlüssel vorhergesagt hätte? Bei einem einzelnen Wort ist das Zufall. Bei tausend Wörtern ergibt sich eine Häufung, die sich messen lässt. Das Resultat ist deshalb nie ein Ja oder Nein, sondern eine **Wahrscheinlichkeit**.

Daraus folgt unmittelbar die wichtigste technische Eigenschaft — und zugleich die zentrale Schwäche: **Das Verfahren braucht Spielraum bei der Wortwahl.** Wo das Modell frei formulieren kann, ist das Signal stark. Wo es kaum Alternativen gibt, ist es schwach oder fehlt ganz.

## Anthropics Wasserzeichen für Claude

Anthropic hat im August 2026 [angekündigt](https://www.anthropic.com/news/claude-text-watermark), die Claude-Modelle mit einem solchen Text-Wasserzeichen nach dem SynthID-Text-Verfahren zu versehen. Der erklärte Anlass ist die Erfüllung der Transparenzpflichten des **EU AI Act**.

Die konkreten Eckpunkte der Ankündigung:

- **Unsichtbar für Leser:innen** — keine versteckten Zeichen, keine zusätzlichen Tokens, keine erkennbaren Markierungen.
- **Kein Qualitätsverlust**: Nach Anthropics Angaben gibt es keinen Einfluss auf Inhalt, Kreativität oder Lesbarkeit; die Geschwindigkeitseinbußen sind vernachlässigbar, zusätzliche Kosten entstehen nicht.
- **Roll-out**: Künftige Claude-Modelle bekommen das Wasserzeichen direkt zum Start; für Modelle, die vor dem 2. August 2026 erschienen sind, ist eine Nachrüstung geplant. Die Maßnahme gilt global, nicht nur in der EU.
- **Detektions-API**: Ein Dienst zur Prüfung von Texten wurde angekündigt, Details standen zum Zeitpunkt der Ankündigung noch aus.
- **Bilder** werden nicht per Wasserzeichen, sondern über **C2PA Content Credentials** gekennzeichnet.

Bemerkenswert ist der Kontext: Anthropic ist einer von rund **190 Unterzeichnern** des EU-Verhaltenskodex für KI (Code of Practice). Die Kennzeichnung ist damit weniger ein Alleingang als der erste sichtbare Schritt einer Branchenbewegung, die durch Regulierung ausgelöst wurde.

## Was Wasserzeichen nicht leisten

Hier ist Nüchternheit angebracht — und Anthropic selbst benennt die Grenzen ungewöhnlich offen. Ein Text-Wasserzeichen ist ein **Herkunftsnachweis für den positiven Fall**, kein Lügendetektor.

**Es kann nicht zwischen Mensch und Maschine im Allgemeinen unterscheiden.** Es kann nur sagen: „Dieser Text trägt mit hoher Wahrscheinlichkeit die Signatur *dieses* Anbieters." Ein Text ohne Wasserzeichen kann von einem Menschen stammen — oder von einem anderen Modell, von einem älteren Claude ohne Nachrüstung, aus einem selbst gehosteten Open-Weight-Modell oder aus einer paraphrasierten Fassung.

**Kurze Texte sind unzuverlässig.** Weil das Signal statistisch entsteht, braucht es Textlänge. Bei einer E-Mail von drei Sätzen oder einem Social-Media-Post lässt sich kaum etwas Belastbares sagen.

**Faktenlastige und formal gebundene Texte tragen kaum Signal.** Wo die Wortwahl durch die Sache vorgegeben ist — historische Daten, Fachbegriffe, Zahlen — oder wo Syntax streng ist wie bei **Programmcode**, fehlt der nötige Spielraum. Ausgerechnet bei Quellcode, einem der häufigsten KI-Anwendungsfälle, ist die Methode also schwach.

**Bearbeitung verdünnt das Signal.** Wer einen KI-Entwurf gründlich überarbeitet, umformuliert und mit eigenen Passagen mischt, reduziert den Anteil der vom Modell gewählten Wörter — und damit das Wasserzeichen. Anthropic formuliert das explizit: Bei stark redigiertem Text bleibt wenig übrig, das messbar wäre.

Daraus folgt der vielleicht wichtigste Punkt für die Praxis: **Die Abwesenheit eines Wasserzeichens beweist gar nichts.** Ein Nachweis ist ein Indiz für KI-Herkunft; das Fehlen ist kein Beleg für menschliche Autorschaft. Wer diese Asymmetrie ignoriert und Wasserzeichen-Prüfungen als Betrugsdetektor einsetzt, wiederholt genau den Fehler, den die alten KI-Detektoren begangen haben.

Hinzu kommt: Ein motivierter Angreifer **kann** das Signal entfernen. Konsequentes Paraphrasieren, maschinelle Rückübersetzung über eine zweite Sprache oder das Mischen mehrerer Quellen zerstören die statistische Struktur weitgehend. Wasserzeichen erschweren die unbemerkte Massenproduktion — sie verhindern gezielte Täuschung nicht.

## Bilder, Audio und Video: C2PA und SynthID

Bei anderen Medien ist die Lage etwas komfortabler, weil dort mehr „unwichtige" Information zum Verstecken zur Verfügung steht.

**SynthID** von Google DeepMind markiert entsprechend Bilder, Audio und Video aus den hauseigenen Generatoren mit robusten, für Menschen nicht wahrnehmbaren Mustern. Diese überstehen typische Bearbeitungen wie Komprimierung, Zuschnitt oder Screenshots deutlich besser als jedes Text-Wasserzeichen — perfekt sind sie aber ebenfalls nicht.

Der zweite, komplementäre Ansatz sind **C2PA Content Credentials**: kryptografisch signierte Metadaten, die an einer Datei dokumentieren, womit sie erzeugt und wie sie bearbeitet wurde — eine Art Herkunfts-Etikett. Auf diesen Weg setzt Anthropic bei Bildern. Der Vorteil ist Nachvollziehbarkeit über ganze Bearbeitungsketten; der Nachteil liegt auf der Hand: Metadaten lassen sich entfernen. Ein Screenshot genügt.

In der Kombination ergibt sich das realistische Bild: **Wasserzeichen im Inhalt** (überlebt Metadaten-Verlust) plus **signierte Metadaten** (dokumentieren den Kontext) sind zusammen deutlich stärker als jede Methode allein — und trotzdem kein lückenloser Schutz.

## Der regulatorische Rahmen: EU AI Act

Dass die Kennzeichnung gerade jetzt kommt, ist kein Zufall. Der **EU AI Act** verpflichtet Anbieter generativer KI in seinen Transparenzregeln dazu, maschinell erzeugte Inhalte in **maschinenlesbarer Form** als künstlich erzeugt zu kennzeichnen. Die einschlägigen Pflichten greifen ab dem **2. August 2026** — exakt das Datum, das auch in Anthropics Nachrüstungsplan auftaucht.

Ergänzend gilt: Wer Deepfakes oder KI-generierte Inhalte veröffentlicht, muss dies offenlegen. Die Verantwortung verteilt sich damit auf zwei Ebenen — **Anbieter** müssen technisch kennzeichnen, **Anwender** müssen transparent machen.

Für europäische Unternehmen ist das der eigentlich relevante Teil: Die Kennzeichnungspflicht endet nicht beim Modellanbieter. Wer KI-Inhalte in Produkten, Kampagnen oder Publikationen einsetzt, sollte die eigenen Offenlegungspflichten kennen — ein Wasserzeichen des Anbieters nimmt sie einem nicht ab.

## Was das für die Praxis bedeutet

**Für Bildung und Prüfungswesen** ist die nüchterne Botschaft: Wasserzeichen lösen das Prüfungsproblem nicht. Sie funktionieren nicht zuverlässig bei kurzen Texten, nicht bei überarbeiteten Entwürfen und nicht bei Modellen, die nicht mitmachen. Wer Leistungsnachweise absichern will, kommt um veränderte Prüfungsformate — mündliche Verteidigung, Prozessdokumentation, betreute Zwischenschritte — nicht herum. Eine Wasserzeichen-Prüfung darf allenfalls ein Anhaltspunkt sein, nie ein Urteil.

**Für Redaktionen und Verlage** ist der Nutzen konkreter: Bei längeren, eingereichten Texten kann eine Prüfung ein sinnvolles Signal liefern, ob ein Beitrag im Wesentlichen maschinell erzeugt wurde. In Kombination mit klaren Richtlinien zur KI-Nutzung — und mit der Offenheit, dass KI-Unterstützung erlaubt, aber deklarationspflichtig ist — entsteht daraus eine praktikable Redaktionsroutine.

**Für Unternehmen** ist vor allem die Dokumentation relevant. Wer KI im Content-Prozess einsetzt, sollte intern festhalten, welche Inhalte maschinell erzeugt wurden — nicht, weil ein Wasserzeichen sie überführen könnte, sondern weil die Offenlegungspflichten des AI Act dies ohnehin verlangen und eine saubere Dokumentation im Zweifel entlastet.

**Für Entwickler:innen** bleibt eine strukturelle Lücke bestehen: **Open-Weight-Modelle**, die lokal betrieben werden — etwa über Ollama —, lassen sich nicht zur Kennzeichnung zwingen. Wer ein Modell selbst hostet, kontrolliert den Sampling-Prozess und damit das Wasserzeichen. Genau die Nutzergruppe, die am ehesten Grund hätte, Spuren zu vermeiden, ist von der Regelung praktisch nicht erfasst. Das ist keine Nachlässigkeit der Anbieter, sondern eine Eigenschaft offener Modelle.

## Fazit

Text-Wasserzeichen sind ein **echter technischer Fortschritt** — und ein bemerkenswert eleganter dazu: Sie kosten nichts, verändern die Textqualität nicht und sind für Leser:innen unsichtbar. Gegenüber den unzuverlässigen KI-Detektoren der letzten Jahre sind sie ein methodischer Sprung, weil das Signal vom Erzeuger stammt und nicht aus einer Stilvermutung.

Zugleich lösen sie das Problem nicht, das viele ihnen zuschreiben. Sie beantworten die Frage „Stammt das von Claude?" mit einer Wahrscheinlichkeit — nicht die Frage „Hat ein Mensch das geschrieben?". Sie versagen bei kurzen Texten, bei Code, bei stark überarbeiteten Entwürfen und bei jedem Modell, das nicht mitmacht. Und ihre Aussagekraft ist einseitig: Ein Fund ist ein Indiz, ein Nicht-Fund ist nichts.

Realistisch betrachtet sind Wasserzeichen daher **ein Baustein von mehreren**: zusammen mit signierten Herkunftsdaten wie C2PA, mit Offenlegungspflichten für Anwender und mit organisatorischen Antworten dort, wo Technik prinzipiell an Grenzen stößt. Wer sie als das versteht, gewinnt ein nützliches Werkzeug. Wer sie für eine Wahrheitsmaschine hält, wird enttäuscht — und richtet im Zweifel Schaden an.

---

**Quellen und Weiterführendes:** Anthropics Ankündigung [„Watermarking Claude's text output"](https://www.anthropic.com/news/claude-text-watermark) · das Video [„Understanding Text Watermarking – How AI Text Carries an Invisible Signature"](https://youtu.be/0jAtFkN6DFs) von Andreas Stöckl · SynthID-Text wurde 2024 in *Nature* veröffentlicht (Google DeepMind)."""
}

CONTENT_CUE = (
    'A hand-drawn page of horizontal text lines where a few individual characters carry tiny '
    'hairline tick-marks above them, and those ticks together trace a faint repeating rhythm '
    'across the page; one single tick is tinted magenta. Generous white space around the page.'
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

cts = requests.get(f'{BASE}/{SITE}/contenttypes/', headers=H, verify=False).json()
article_ct = next(c for c in cts if c.get('display_identifier') == 'article')
ART_CT_ID = article_ct['id']

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
        requests.patch(f'{BASE}/{SITE}/elements/{el_id}', json={'published': True}, headers=H, verify=False)

# ---- Cover ----
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
    print('\n→ generating cover ...')
    rg = requests.post(f'{BASE}/{SITE}/media/generate', json=media_payload, headers=H, verify=False, timeout=240)
    if rg.status_code == 402:
        print(f'  ✗ insufficient AI credits: {rg.json().get("detail",{}).get("message","")}')
    elif not rg.ok:
        print(f'  ✗ {rg.status_code} {rg.text[:300]}')
    else:
        mid = rg.json().get('id')
        print(f'  ✓ media #{mid}')
        new_data = {**existing_data, 'media_id': mid}
        rp2 = requests.patch(f'{BASE}/{SITE}/elements/{el_id}', json={'data': new_data}, headers=H, verify=False)
        print(f'  ✓ element patch: {rp2.status_code}')

print('\n✓ Done.')
