#!/usr/bin/env python3
"""Seed a new editorial article: 'Lokale vs. Cloud-Modelle — Anwendungen, Vor- und Nachteile'.
Creates Post + Article element + generates cover via Nano Banana.
Idempotent: skips if slug already exists.
"""
import requests, urllib3, time
from pathlib import Path

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ROOT = Path(__file__).resolve().parent.parent
ENV = {l.split('=',1)[0].strip(): l.split('=',1)[1].strip()
       for l in (ROOT/'.env').read_text().splitlines() if '=' in l and not l.startswith('#')}
BASE, SITE = ENV['BASEURL'], ENV['SITE']

ARTICLE = {
    'slug': 'lokale-vs-cloud-modelle',
    'title': 'Lokale vs. Cloud-Modelle: Anwendungen, Vor- und Nachteile',
    'category': 'Praxis',
    'author': 'Redaktion',
    'date': '2026-05-01',
    'readTime': 12,
    'toc': [
        'Was unterscheidet lokale und Cloud-Modelle?',
        'Cloud-Modelle in der Praxis',
        'Lokale Modelle in der Praxis',
        'Vor- und Nachteile im Direktvergleich',
        'Hybride Setups',
        'Entscheidungshilfe: Wann was?',
        'Fazit',
    ],
    'lead': (
        'Cloud-LLMs liefern die Spitzenqualität ohne Hardware-Aufwand — lokale Modelle '
        'die Datenhoheit ohne laufende API-Kosten. Was passt wann? Ein nüchterner Vergleich '
        'der beiden Welten und ihrer praktischen Anwendungsfälle in 2026.'
    ),
    'content': """## Was unterscheidet lokale und Cloud-Modelle?

Bei **Cloud-Modellen** läuft die Inferenz auf den Servern eines externen Anbieters: Der Prompt wird über eine API verschickt, das Modell rechnet auf dessen GPU-Cluster, die Antwort kommt zurück. ChatGPT, Claude, Gemini, Mistral Large — alle SOTA-Modelle der bekannten Anbieter funktionieren so.

Bei **lokalen Modellen** läuft das gesamte Modell auf eigener Hardware: Auf dem Laptop, einem dedizierten GPU-Server, in der eigenen Cloud-Region oder am Edge-Gerät. Die Modelle sind in der Regel Open-Weight oder Open-Source — Llama 3.3, Mistral Small 3, Qwen 2.5, DeepSeek-V3, Phi-4 — und werden über Frameworks wie Ollama, LM Studio, vLLM oder Text Generation Inference betrieben.

Die **technische Trennlinie** liegt also bei der Frage, wer die Inferenz-Infrastruktur betreibt. Daraus folgen praktisch alle anderen Unterschiede: Latenz, Datenschutz, Kostenmodell, Modellqualität, Wartungsaufwand.

Eine wichtige Zwischenstufe ist die **„Private Cloud"-Variante**: Cloud-Modelle, die in einer dedizierten Region (Vertex AI EU, Azure OpenAI EU, Bedrock Frankfurt) laufen — technisch Cloud, datenschutzrechtlich näher am lokalen Setup. In diesem Artikel zählen wir solche Setups zur Cloud, weisen aber auf die Sonderrolle hin.

## Cloud-Modelle in der Praxis

Die typischen Anwendungsfälle, in denen Cloud-Modelle ihre Stärken voll ausspielen:

- **Konsumenten-Produkte mit hohem Qualitätsanspruch.** Wenn ein Chatbot für Endkunden gebaut wird oder ein Schreibassistent, der mit der Qualität von ChatGPT konkurrieren muss, führt 2026 kein Weg an GPT-5, Claude Sonnet 4.7 oder Gemini 3 Pro vorbei. Open-Weight-Modelle haben in vielen Benchmarks aufgeholt, im konversationellen Feinschliff und bei komplexen Reasoning-Aufgaben liegen die SOTA-Cloud-Modelle aber weiter vorn.
- **Multimodale Workflows.** Bildverstehen, Bildgenerierung, Audio-In/Out, Video-Verstehen — die durchgängig multimodalen Modelle (GPT-5, Gemini 3, Claude Sonnet 4.7) gibt es als lokale Alternativen nur in deutlich kleineren Versionen oder gar nicht. Wer regelmäßig PDFs mit Tabellen verarbeitet oder Bildanalyse mit Reasoning kombiniert, ist mit Cloud meist besser bedient.
- **Schwankende Last.** Eine Marketing-App, die typisch 100 Anfragen am Tag bedient und einmal pro Woche eine Kampagne mit 10.000 Anfragen fährt, ist in der Cloud trivial skalierbar. Lokale Hardware muss für die Spitzenlast dimensioniert werden — und steht den Rest der Zeit ungenutzt.
- **Schnelle Innovation.** Wer immer auf dem neuesten Modell laufen will, ohne alle drei Monate ein Reinstall-Wochenende einzulegen, lebt in der Cloud-Welt komfortabler. Anbieter rollen Modell-Updates ohne Mitwirken aus, A/B-Tests mit verschiedenen Modellen sind eine Konfig-Änderung.
- **Agentische Workflows mit großem Tool-Universum.** Frameworks wie OpenAI Agents SDK, Anthropic Claude Code oder Google ADK bauen tiefe Integrationen mit ihren jeweiligen Cloud-Modellen — Function Calling, Tool-Routing und Long-Horizon-Reasoning sind dort ausgereifter als bei den meisten Open-Weight-Setups.

## Lokale Modelle in der Praxis

Auf der anderen Seite die typischen Felder, in denen lokale Modelle 2026 die rationale Wahl sind:

- **Hochsensible Daten ohne Cloud-Optionen.** Patientendaten in Krankenhäusern, juristische Akten in Anwaltskanzleien, Quellcode in Sicherheits-kritischen Branchen, Forschungsdaten in der pharmazeutischen Industrie — überall dort, wo Daten das Haus oder zumindest die eigene Cloud-Region nicht verlassen dürfen, sind lokale Modelle oft die einzige praktikable Option. Selbst „EU-only"-Cloud-Tarife reichen manchen Compliance-Abteilungen nicht aus.
- **Kostenkontrolle bei sehr hoher Anfrage-Menge.** Wenn eine Anwendung Millionen Anfragen pro Monat bedient und pro Anfrage nur ein günstiges Klassifikationsergebnis braucht, kann ein eigenbetriebenes Llama-3.3-8B auf einer einzigen H100 oft drastisch günstiger sein als API-Calls — vor allem bei stabiler, vorhersagbarer Last.
- **Offline- oder Edge-Anwendungen.** Maschinensteuerungen in der Industrie, On-Device-Assistenten in Mobilgeräten, Anwendungen für Außendienst ohne stabile Verbindung — überall, wo Konnektivität nicht garantiert ist oder Latenz unter 100 Millisekunden gefordert wird, sind lokale Modelle alternativlos. Apple Intelligence on-device, Mistral 3B in mobiler App, Phi-4 in eingebetteten Systemen sind reale Beispiele.
- **Forschung und Customizing.** Wer ein Modell durch Fine-Tuning, LoRA-Training oder Retrieval-Anpassung tatsächlich verändern will, braucht Open-Weight-Zugriff. Cloud-APIs erlauben oft nur oberflächliche Anpassungen über System-Prompts und Custom GPTs.
- **Vendor-Lock-in vermeiden.** Strategisch wichtige Workflows, die auf einer Cloud-API laufen, geraten in Abhängigkeit vom Anbieter — Preis, Verfügbarkeit, Modell-Eigenschaften ändern sich ohne Vorwarnung. Wer lokal hostet, hat diese Risiken nicht.

## Vor- und Nachteile im Direktvergleich

Die wichtigsten Dimensionen nebeneinander:

**Modellqualität.** Cloud führt 2026 weiterhin bei den absoluten Top-Modellen für Reasoning, Multimodalität und sehr lange Kontexte (1 Mio.+ Tokens). Open-Weight-Modelle sind in vielen Standard-Aufgaben (Klassifikation, Extraction, einfache Generierung) gleichauf — bei komplexen Aufgaben liegen 6–18 Monate hinter Frontier-Modellen.

**Datenschutz.** Lokal gewinnt klar: Die Daten verlassen die eigene Infrastruktur nicht. Cloud-Anbieter bieten zwar No-Training-Garantien und EU-Hosting, aber die Daten gehen physisch zum Anbieter — ein Restrisiko, das viele Compliance-Abteilungen nicht akzeptieren.

**Kosten.** Hängt stark vom Volumen ab. Bei niedrigem Volumen (< 1.000 Anfragen/Tag) ist Cloud fast immer billiger — kein Hardware-Invest, kein Ops-Personal. Ab mittlerem Volumen (10.000+ Anfragen/Tag) und stabiler Last kippt die Rechnung oft zugunsten lokaler Setups. Bei hoher Spitzenlast und niedrigem Mittelwert bleibt Cloud meist günstiger.

**Latenz.** Lokal kann unter 50 Millisekunden liefern (kleine Modelle, schnelle Hardware, kein Netzwerk-Hop). Cloud liegt typisch bei 200–800 Millisekunden für die ersten Tokens, plus Generierungszeit. Für Echtzeit-Anwendungen (Sprachsteuerung, interaktive Werkzeuge) ein relevantes Argument.

**Wartungsaufwand.** Cloud praktisch null — Anbieter kümmert sich um Updates, Skalierung, Hardware. Lokal hat Wartungsaufwand: Modell-Updates, GPU-Treiber, Inferenz-Server, Monitoring. Realistisch braucht ein produktiver lokaler Stack 0,2–0,5 FTE Ops-Anteil.

**Innovation.** Cloud-Anbieter rollen neue Modelle und Features schnell aus. Bei lokalen Setups muss jedes Modell-Upgrade getestet, integriert und deployed werden — typisch 2–8 Wochen Zykluszeit.

**Skalierung.** Cloud skaliert horizontal mit einer Zeile Konfiguration. Lokale Setups skalieren mit mehr Hardware und mehr Ops-Aufwand. Für sehr volatile Lastprofile ist Cloud klar überlegen.

**Vendor-Risiko.** Cloud bedeutet Lock-in, Pricing-Risiko, Modell-Deprecation-Risiko. Lokal bedeutet Hardware-Investitions-Risiko, Skill-Risiko (Personal mit Inferenz-Stack-Erfahrung).

**Compliance.** Cloud kann mit AVV, EU-Hosting und SOC-2 vieles abdecken — aber nicht alles (etwa Bundesgesundheitsbehörden mit besonders strikten Anforderungen). Lokal löst Compliance fast immer, kostet aber mehr im Aufbau.

## Hybride Setups

In der Realität entscheiden sich viele Teams nicht für entweder/oder, sondern für eine **gestaffelte Architektur**:

- **Sensible Daten im Eingang lokal vorverarbeiten.** Personenbezogene Daten werden lokal anonymisiert oder zu Embeddings transformiert, bevor sie an ein Cloud-Modell gehen. Das eigentliche Reasoning läuft mit anonymisierten Tokens in der Cloud.
- **Routing nach Anfrage-Typ.** Einfache Klassifikation, Extraction und Routing-Entscheidungen laufen lokal auf einem schlanken Modell (Llama 3.3 8B). Komplexe Reasoning-, Generierungs- und multimodale Aufgaben gehen an die Cloud (GPT-5, Claude Sonnet 4.7, Gemini 3).
- **Caching und Retrieval lokal.** Vector-DBs, RAG-Indizes und Konversations-Caches liegen lokal — die eigentliche Generierung greift via Cloud auf diese lokalen Datenquellen zu.
- **Fallback-Logik.** Lokales Modell als Fallback, wenn Cloud-API ausfällt oder Rate-Limits greift. Wichtig für Anwendungen mit hohen Verfügbarkeitsanforderungen.

Die hybride Variante kombiniert die jeweils besten Eigenschaften, erhöht aber die Architektur-Komplexität spürbar. Sie lohnt sich vor allem ab einer gewissen Größe — kleine Teams sind mit der Wahl einer der beiden klaren Welten meist besser bedient.

## Entscheidungshilfe: Wann was?

Eine kleine Entscheidungs-Heuristik, die in vielen Beratungsgesprächen reicht:

- **Volumen niedrig + Daten unkritisch → Cloud.** API-Aufruf, keine Hardware, sofort produktiv. Klassischer Startup-Stack.
- **Volumen hoch + stabile Last + Daten unkritisch → Hybrid oder Cloud-Reserved.** Ab einigen 10.000 Anfragen/Tag lohnt sich der Vergleich der Total Cost of Ownership; manchmal reicht aber auch ein Reserved-Capacity-Vertrag mit dem Cloud-Anbieter.
- **Volumen niedrig + Daten sensibel → Cloud-EU oder lokal.** Vertex AI EU, Azure OpenAI EU oder Bedrock Frankfurt sind oft ausreichend; bei besonders strikter Compliance kommen lokale Modelle ins Spiel.
- **Volumen hoch + Daten sensibel → Lokal.** Hier rechnet sich die Investition in Ops und Hardware fast immer; der Marktstandard sind ein bis zwei H100/B200-Karten plus vLLM-Stack.
- **Latenz < 100 ms erforderlich → Lokal oder Edge.** Cloud-Latenz reicht für Echtzeit-Sprachverarbeitung selten aus.
- **Frontier-Reasoning erforderlich → Cloud.** Open-Weight ist 2026 immer noch nicht auf Frontier-Niveau bei den anspruchsvollsten Reasoning-Aufgaben.
- **Compliance vorwiegend für DSGVO → EU-Cloud reicht meist.** AVV, EU-Hosting und No-Training-Garantie decken die meisten DSGVO-Anforderungen ab.
- **Compliance gemäß BSI Cloud Computing C5 / Schwerstgrad → Lokal.** Hier wird Cloud auch in EU-Region eng.

## Fazit

Die Wahl zwischen lokalen und Cloud-Modellen ist 2026 keine ideologische, sondern eine pragmatische Architektur-Entscheidung — abhängig von Volumen, Daten-Sensibilität, Qualitätsanspruch und Team-Kapazität.

Cloud bleibt der schnellste Weg zu hoher Modellqualität ohne Hardware-Investition; lokale Modelle bleiben unverzichtbar, wenn Daten das Haus nicht verlassen dürfen oder die Inferenz-Kosten bei stabiler hoher Last die API-Rechnung übersteigen. Für alle dazwischen lohnt sich ein hybrider Ansatz mit lokalem Routing und Cloud-Eskalation.

Was sich klar abzeichnet: Die Open-Weight-Modelle sind zwischen 2024 und 2026 deutlich näher an die SOTA-Cloud-Modelle herangerückt — Llama 3.3 70B oder DeepSeek-V3 erreichen heute Qualitätsniveaus, die vor 18 Monaten nur GPT-4 erreichte. Das verschiebt die Architektur-Entscheidung tendenziell weiter in Richtung lokaler Setups, wann immer Datenschutz oder Volumen es nahelegen. Die Frontier bleibt aber für absehbare Zeit in der Cloud."""
}

CONTENT_CUE = (
    'Two contrasting abstract shapes facing each other across a thin horizontal line: '
    'on the left a small grounded ink-line server-box with a magenta dot inside; '
    'on the right a soft cloud outline with three dotted connection lines drifting '
    'into open space. A faint magenta arrow loops between them — the architectural choice.'
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
    # ---- 1. Create the Post (content + lead) ----
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

    # ---- 2. Create the article element ----
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

# ---- 3. Generate cover via Nano Banana ----
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
        # Patch the article element with media_id
        new_data = {**existing_data, 'media_id': mid}
        rp2 = requests.patch(f'{BASE}/{SITE}/elements/{el_id}',
            json={'data': new_data}, headers=H, verify=False)
        print(f'  ✓ element patch: {rp2.status_code}')

print('\n✓ Done.')
