#!/usr/bin/env python3
"""Seed 7 additional Video & Audio tools end-to-end (May 2026 batch)."""
import requests, urllib3
from pathlib import Path

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ROOT = Path(__file__).resolve().parent.parent
LOGOS_DIR = ROOT / 'logos'
LOGOS_DIR.mkdir(exist_ok=True)

ENV = {l.split('=',1)[0].strip(): l.split('=',1)[1].strip()
       for l in (ROOT/'.env').read_text().splitlines() if '=' in l and not l.startswith('#')}
BASE, SITE = ENV['BASEURL'], ENV['SITE']

TOOLS = [
    {'slug':'sora','name':'Sora 2','vendor':'OpenAI','category':'video-audio',
     'tagline':'OpenAIs zweite Generation des Text-zu-Video-Modells — bis zu 60 Sek., physikalisch konsistente Szenen, Native-Audio inklusive Dialog und Sound-Design.',
     'price':'In ChatGPT Plus enthalten · API ab $0,40 / Sek.','api':True,'dsgvo':'bedingt','origin':'USA',
     'rating':4.8,'reviews':9430,
     'pros':['Physikalisch konsistente Bewegung über 60 Sek.','Native Audio mit Dialog und Sound-Design','Charakter-Konsistenz über mehrere Shots','Storyboard-Modus mit getrennten Szenen'],
     'cons':['Generierungszeit 1–4 Min. pro Clip','API-Quoten knapp im Plus-Tarif','Inhaltsfilter strenger als Konkurrenten','EU-Datenresidenz nur Enterprise'],
     'usecases':['Werbe-Spots','Kurz-Filme','Storyboard-Animation','Social-Media-Reels'],
     'launched':'2025-12-09','lastUpdated':'2026-05-08',
     'website':'https://sora.com/','domain':'sora.com',
     'features':"""- **Text-zu-Video** bis 60 Sek. (vorher 20 Sek.).
- **Native Audio**: Dialog, Atmosphären-Sounds, Musik in einem Pass.
- **Image-zu-Video** mit Foto, Skizze oder gerendertem Frame als Input.
- **Storyboard-Modus**: mehrere Szenen mit Charakter-Konsistenz.
- **Remix-Workflow**: bestehendes Video umgestalten.
- **4K-Output** (3840×2160) ohne Upscaler.
- **C2PA-Wasserzeichen** und sichtbares Sora-Tag.""",
     'pricing':"""- **ChatGPT Plus** · $20 / Mon. — 50 Standard-Clips, max 5 Sek.
- **ChatGPT Pro** · $200 / Mon. — 500 Clips, bis 20 Sek., Priority.
- **Sora Studio** · $30 / Mon. — Standalone-Zugang ohne ChatGPT-Bundle.
- **API standard** · $0,40 / Sek. (720p, 5 Sek.).
- **API premium** · $1,80 / Sek. (4K, 60 Sek., Native-Audio).
- **Enterprise** · auf Anfrage — EU-Datenresidenz, Bulk-Pricing.""",
     'overview':"""**Sora 2** ist OpenAIs zweite Generation des Text-zu-Video-Modells — vorgestellt im Dezember 2025, seit Februar 2026 allgemein verfügbar. Wer Sora 1 als technische Demo wahrgenommen hat (mit knappen 20-Sek-Clips ohne Audio), bekommt mit v2 ein Tool, das tatsächlich produktionsreifen Output liefert.

Die wichtigste Neuerung ist **Native Audio**: Dialog, Atmosphären-Sounds, Musik werden in einem Pass mit dem Video generiert — nicht nachträglich aufgesetzt. Lippen-Synchronisation funktioniert in den meisten Fällen out-of-the-Box. Damit fällt einer der größten Workflow-Stolpersteine der Konkurrenten weg.

Die zweite Neuerung ist die **physikalisch konsistente Bewegung** über bis zu 60 Sekunden. Ein Wasserglas, das umfällt, gießt seinen Inhalt in plausibler Richtung aus; eine Person, die durch eine Tür geht, behält dieselbe Kleidung und denselben Haarstil; ein Auto bremst mit nachvollziehbarer Trägheit. Konkurrenten wie Veo 3 oder Kling sind in einzelnen Disziplinen ebenbürtig, aber Sora 2 liegt in der Gesamtkonsistenz aktuell vorn.

Der **Storyboard-Modus** ist die dritte große Neuerung: Mehrere Szenen mit demselben Charakter werden in einem Workflow generiert, ohne dass die Person zwischen Cuts wechselt. Für Werbe-Spots und Kurz-Filme ein konstitutiver Vorteil.

**Image-zu-Video** funktioniert mit Foto, Skizze oder gerendertem Standbild als Startpunkt — die häufigste Variante für Storyboarding-Workflows, die mit GPT Image 2 oder Nano Banana Pro 2 beginnen.

**4K-Output** (3840×2160) ist neu und ohne Upscaler-Pipeline — Print-, Display- und Streaming-Workflows kommen ohne Nachbearbeitung aus.

Schwächen: Die **Generierungszeit** liegt bei 1–4 Minuten pro Clip — wer iterativ arbeiten will, wartet spürbar. Die **API-Quoten** im Plus-Tarif (50 Standard-Clips/Mon.) sind knapp — Power-User landen schnell im Pro- oder Studio-Tarif. **Inhaltsfilter** sind strenger als bei Veo 3 oder Kling — bestimmte historische, politische oder dokumentarische Stilisierungen werden blockiert. **EU-Datenresidenz** bleibt Enterprise-Feature.

Empfohlen für Werbe- und Filmteams, die kurze produktionsreife Video-Sequenzen brauchen — und für jeden, der Native-Audio in einem Pass mit dem Bild generieren will, ohne separaten Voice-Over-Workflow."""},

    {'slug':'veo','name':'Veo 3','vendor':'Google DeepMind','category':'video-audio',
     'tagline':'Googles dritte Generation des Veo-Modells — Native-Audio, deutlich besseres Cinematic-Reasoning, in Vertex AI und Flow direkt verfügbar.',
     'price':'In Gemini Advanced enthalten · API ab $0,35 / Sek.','api':True,'dsgvo':'ja','origin':'USA',
     'rating':4.7,'reviews':6840,
     'pros':['Native-Audio mit Sound-FX und Musik','Sehr starkes Cinematic-Reasoning','EU-Datenresidenz über Vertex AI','Bestens in Google-Workspace und Flow integriert'],
     'cons':['Quoten in Free-Stufe sehr knapp','Maximale Clip-Länge 8 Sek. (Sora kann 60)','Inhaltsfilter im Free-Tarif streng','Dialog-Lippen-Synchronisation noch hinter Sora'],
     'usecases':['Werbe-Visuals','Cinematic-Mockups','Music-Videos','Marketing-Reels'],
     'launched':'2025-08-26','lastUpdated':'2026-05-08',
     'website':'https://deepmind.google/models/veo/','domain':'deepmind.google',
     'features':"""- **Text-zu-Video** mit 8-Sek-Clips, optional zusammenhängend bis 32 Sek.
- **Native Audio**: Atmosphären-Sounds, Musik, gelegentlich Dialog.
- **Image-zu-Video** mit Imagen-3- oder Nano-Banana-Pro-2-Outputs als Startpunkt.
- **Cinematic-Camera-Controls** (Dolly, Pan, Tilt, Zoom).
- **Reference-Image-Style-Transfer** für Brand-Konsistenz.
- **Verfügbar in Vertex AI, Gemini App und Google Flow**.
- **SynthID-Wasserzeichen** und sichtbares Veo-Tag.""",
     'pricing':"""- **Gemini App Free** · 3 Veo-Clips / Mon. (Standard-Quality).
- **Gemini Advanced** · $20 / Mon. — 50 Clips / Mon. mit Veo 3.
- **Google Flow Pro** · $30 / Mon. — kreatives Studio mit Storyboarding.
- **API standard** · $0,35 / Sek. (720p, 8 Sek.).
- **API premium** · $1,40 / Sek. (4K, 8 Sek., Native-Audio).
- **Vertex AI Enterprise** · auf Anfrage, EU-Region und SLA.""",
     'overview':"""**Veo 3** ist Google DeepMinds dritte Generation des Veo-Modells — vorgestellt auf der I/O 2025, seit Spätsommer 2025 in Gemini Advanced und Flow integriert. Damit ist Google direkter Konkurrent zu Sora 2 in einer Disziplin, die historisch eher OpenAI dominiert hat.

Das Modell hat in zwei Disziplinen besonders aufgeholt. Erstens **Cinematic-Reasoning**: Veo 3 versteht Kamera-Sprache deutlich besser — Dolly-Shots, Crane-Bewegungen, Zoom-Ins, Establishing-Shots werden so umgesetzt, wie ein Filmemacher es erwartet. Für Werbe- und Music-Video-Workflows ein konstitutiver Vorteil.

Zweitens **Native Audio**: Atmosphären-Sounds, Musik und gelegentlich Dialog werden mit dem Video in einem Pass generiert. Die Sound-Designs sind oft überraschend präzise — eine Straßenszene bekommt passende Verkehrsgeräusche, eine Wald-Szene bekommt Vogelgezwitscher mit korrektem Rauminhalt.

Die **Integration** in das Google-Ökosystem ist die strategische Stärke: **Vertex AI** für Engineering-Workflows mit EU-Datenresidenz, **Gemini App** für End-Anwender:innen, **Google Flow** als kreatives Studio mit Storyboarding und Multi-Scene-Management. Wer im Google-Workspace arbeitet, hat hier einen besonders kurzen Weg.

**Image-zu-Video** funktioniert nahtlos mit Imagen-3- oder Nano-Banana-Pro-2-Outputs — ein Standbild aus einem dieser Modelle wird in Veo 3 zu einem 8-Sek-Clip animiert, ohne Re-Encode.

Die **Cinematic-Camera-Controls** sind explizit: Statt nur „Kamera bewegt sich nach rechts" zu schreiben, lassen sich Dolly-In, Crane-Up, Tilt-Down als typed Parameter setzen. Für präzise Storyboard-Frames ein wichtiger Workflow-Vorteil.

**EU-Datenresidenz** über Vertex AI ist ein klarer Vorteil gegenüber Sora 2, das diese Option nur Enterprise bietet — für DSGVO-sensible Werbe- und Marketing-Workflows oft entscheidend.

Schwächen: Die **maximale Clip-Länge** liegt bei 8 Sekunden (Sora 2 schafft 60); zusammenhängende längere Sequenzen brauchen Storyboarding mit Multi-Clip-Stitching. Die **Quoten in der Free-Stufe** sind sehr knapp (3 Clips / Monat), Power-User landen schnell im Bezahltarif. **Dialog-Lippen-Synchronisation** ist noch nicht ganz auf Sora-2-Niveau.

Empfohlen für Werbe-, Marketing- und Music-Video-Teams, die im Google-Ökosystem arbeiten — und für DSGVO-sensible Workflows, in denen EU-Datenresidenz Pflicht ist."""},

    {'slug':'kling','name':'Kling AI','vendor':'Kuaishou','category':'video-audio',
     'tagline':'Kuaishous chinesisches Spitzenmodell — sehr realistische Personen-Bewegungen, präzise Image-zu-Video-Pipeline und konkurrenzlose Kosten pro Clip.',
     'price':'Free 6 Clips/Tag · Pro ab $10 / Mon.','api':True,'dsgvo':'nein','origin':'China',
     'rating':4.6,'reviews':7320,
     'pros':['Sehr realistische Personen-Bewegung','Image-zu-Video besonders präzise','Deutlich günstiger als Sora oder Veo','Lange Clip-Optionen (bis 2 Min.)'],
     'cons':['Datenresidenz China — kein DSGVO-Use-Case','UI teils chinesisch-zentriert','Inhaltsfilter undurchsichtig','Output-Qualität schwankt mit Auslastung'],
     'usecases':['Image-zu-Video-Animation','Werbe-Mockups für asiatische Märkte','Tanz- und Performance-Videos','Charakter-Animation'],
     'launched':'2024-06-06','lastUpdated':'2026-05-08',
     'website':'https://klingai.com/','domain':'klingai.com',
     'features':"""- **Text-zu-Video** mit 5-, 10- und Extended-Modi (bis 2 Min.).
- **Image-zu-Video** als Hauptstärke, sehr stabile Persistenz.
- **Charakter-Konsistenz** mit Reference-Image-System.
- **Lip-Sync-Modus** für vorgegebene Audio-Spuren.
- **Kling 2.0**-Modell mit Premium-Quality.
- **API mit identischen Modellen** wie Web-UI.
- **Bulk-Generation** für Production-Workflows.""",
     'pricing':"""- **Free** · 6 Clips / Tag, 5 Sek., Watermark.
- **Standard** · $10 / Mon. — 660 Credits, kein Watermark, alle Modi.
- **Pro** · $37 / Mon. — 3.000 Credits, Priority-Queue.
- **Premier** · $93 / Mon. — 8.000 Credits, höchste Concurrency.
- **API**: Pay-as-you-go ab $0,02 / Sek. (Kling 1.6) bis $0,12 / Sek. (Kling 2.0 Master).
- **Enterprise**: nur über chinesische Vertretung.""",
     'overview':"""**Kling AI** ist Kuaishous Antwort auf Sora und Veo — gestartet im Juni 2024 als technische Demo, seitdem zu einem der **populärsten Video-Generatoren weltweit** gewachsen. Mit Kling 2.0 (vorgestellt April 2025) liegt das Modell in mehreren Benchmark-Disziplinen mit Sora 2 und Veo 3 gleichauf — bei deutlich niedrigeren Pro-Sekunde-Kosten.

Die **Kernstärke** ist **realistische Personen-Bewegung**: Tanz-Choreographien, sportliche Aktionen, Mimik-Wechsel funktionieren bei Kling auffallend stabil. Der Background im Trainingsdatensatz von Kuaishou (chinesisches TikTok-Pendant) zeigt sich hier — das Modell ist auf kurze Performance-Videos optimiert.

Die **Image-zu-Video-Pipeline** ist die zweite Stärke und funktioniert besser als bei den US-Konkurrenten. Ein hochgeladenes Foto bleibt charakteristisch konsistent über die volle Clip-Dauer; Hintergründe verschieben sich in plausibler Perspektive; Lichtsituation bleibt erhalten. Für Storyboarding-Workflows mit GPT Image 2 oder Nano Banana Pro 2 als Vorstufe ein klarer Vorteil.

Die **Extended-Modi** (bis 2 Minuten) sind in dieser Form bei keinem anderen Modell verfügbar — Sora 2 schafft 60 Sek., Veo 3 nur 8 Sek. Wer narrative Sequenzen ohne Cuts braucht, hat hier eine einzigartige Option.

Der **Lip-Sync-Modus** nimmt eine vorgegebene Audio-Spur (Voice-Over, Song-Vocal) und passt die Lippenbewegungen an — für Music-Video- und Voice-Over-Workflows pragmatisch.

Die **API** spiegelt das Web-Studio und ist deutlich günstiger als Sora oder Veo: 5-Sek-Clips schon ab $0,10. Für Hochvolumen-Anwendungen (Marketing, Social-Media-Output) der wirtschaftlichste Pfad.

Schwächen: **Datenresidenz China** ist ein Ausschlusskriterium für DSGVO-sensible Use-Cases — keine EU-Region verfügbar. **Inhaltsfilter** sind undurchsichtig und auch politisch motiviert (chinesische Sensibilitäten). Die **UI** ist teils chinesisch-zentriert, auch wenn Englisch-Mode verfügbar ist. **Output-Qualität** schwankt mit Server-Auslastung — zu Stoßzeiten teils spürbar reduziert.

Empfohlen für Content-Creators und Performance-Video-Teams ohne strikte Datenschutz-Auflagen — und für Hochvolumen-Workflows, in denen die Pro-Sekunde-Kosten der ausschlaggebende Faktor sind."""},

    {'slug':'hailuo','name':'Hailuo AI','vendor':'MiniMax','category':'video-audio',
     'tagline':'MiniMax Hailuo 02 — chinesisches Video-Modell mit besonders realistischer Physik und scharfen Detail-Texturen, sehr starkem Image-zu-Video-Output.',
     'price':'Free 1.000 Credits/Mon. · Standard ab $10 / Mon.','api':True,'dsgvo':'nein','origin':'China',
     'rating':4.5,'reviews':5180,
     'pros':['Sehr realistische Physik-Simulation','Scharfe Detail-Texturen (Stoff, Haar, Wasser)','Image-zu-Video besonders präzise','Konkurrenzfähige Pro-Sekunde-Kosten'],
     'cons':['Datenresidenz China — kein DSGVO-Use-Case','Maximale Clip-Länge 10 Sek.','Native-Audio noch in Beta','UI primär für asiatischen Markt'],
     'usecases':['Produkt-Showcase-Videos','Realistische Werbe-Mockups','Image-zu-Video-Animation','Detail-orientierte Cinematic-Frames'],
     'launched':'2024-09-01','lastUpdated':'2026-05-08',
     'website':'https://hailuoai.video/','domain':'hailuoai.video',
     'features':"""- **Text-zu-Video** mit 6-, 10-Sek-Clips.
- **Image-zu-Video** als Hauptstärke, sehr präzise Persistenz.
- **Subject-Reference**: Charakter-Konsistenz mit Reference-Bildern.
- **Director-Mode**: Kamerabewegungen explizit steuerbar.
- **Hailuo 02-Modell** mit Premium-Quality (seit Q1 2026).
- **API mit denselben Modellen** wie Web-UI.
- **Native-Audio** (Beta): Atmosphären-Sounds optional.""",
     'pricing':"""- **Free** · 1.000 Credits / Mon., Standard-Quality, Watermark.
- **Standard** · $10 / Mon. — 5.500 Credits, kein Watermark.
- **Unlimited** · $95 / Mon. — unbegrenzte Generierung, Priority-Queue.
- **API**: Pay-as-you-go ab $0,025 / Sek. (Standard) bis $0,15 / Sek. (Premium).
- **Enterprise**: über chinesische Vertretung.""",
     'overview':"""**Hailuo AI** ist MiniMaxs Video-Modell — gestartet September 2024 als kostenloser Service, seitdem in mehreren Versionen gereift. Mit **Hailuo 02** (vorgestellt Q1 2026) liegt das Modell in mehreren Disziplinen mit Kling und Veo 3 auf Augenhöhe und ist besonders stark in **realistischer Physik-Simulation** und **Detail-Texturen**.

Die **Physik-Simulation** ist die unterscheidende Stärke: Wasser fließt mit plausibler Viskosität, Stoffe wehen mit realistischer Schwere, Haare bewegen sich mit Eigendynamik. Konkurrenzmodelle erreichen ähnliche Qualität in einzelnen Disziplinen, Hailuo 02 ist in der Gesamtphysik besonders konsistent.

Die **Detail-Texturen** sind die zweite Stärke: Hochauflösende Stoff-, Haar-, Wasser- und Reflexions-Darstellungen sind oft schärfer als bei den US-Konkurrenten. Für Produkt-Showcase-Videos (Mode, Schmuck, Kosmetik, Lebensmittel) ein direkter Workflow-Vorteil.

Die **Image-zu-Video-Pipeline** funktioniert auf Kling-Niveau sehr stabil — Charakter, Outfit und Setting bleiben über die volle Clip-Dauer konsistent. Für Storyboarding-Workflows ein verlässlicher Pfad.

Der **Director-Mode** (seit Hailuo 02) erlaubt explizite Kamera-Steuerung als typed Parameter — Dolly, Pan, Crane, Zoom. Für narrative Workflows wertvoll.

Der **Subject-Reference** erlaubt Charakter-Konsistenz über mehrere Generierungen mit einem Referenz-Bild — gut für Personen-Brand-Inhalte und Serien-Inhalte.

**Native-Audio** ist als Beta in den Pro-Tarifen verfügbar — Atmosphären-Sounds funktionieren bereits brauchbar, Dialog ist noch experimentell.

Die **API** ist deutlich günstiger als Sora oder Veo — 6-Sek-Clips ab $0,15. Für Hochvolumen-Anwendungen wettbewerbsfähig.

Schwächen: **Datenresidenz China** ist ein Ausschlusskriterium für DSGVO-sensible Anwendungen. **Maximale Clip-Länge** liegt bei 10 Sek. — Sora 2 schafft 60, Kling kann 2 Min. Wer längere Sequenzen braucht, ist hier eingeschränkt. Die **UI** ist primär für den asiatischen Markt designt; die Englisch-Variante funktioniert, fühlt sich aber sekundär an.

Empfohlen für Produkt-Showcase-Workflows mit hohen Detail-Anforderungen — und für Image-zu-Video-Pipelines, in denen Physik-Konsistenz und Texturen wichtiger sind als maximale Clip-Länge."""},

    {'slug':'dream-machine','name':'Luma Dream Machine','vendor':'Luma Labs','category':'video-audio',
     'tagline':'Lumas Video-Modell — pragmatisch schnell, hervorragend integriert mit Luma Photon für die durchgängige Bild-zu-Video-Pipeline in einem Tool.',
     'price':'Free 30 Credits/Mon. · Standard ab $10 / Mon.','api':True,'dsgvo':'bedingt','origin':'USA',
     'rating':4.6,'reviews':6520,
     'pros':['Sehr schnelle Generierung (15–40 Sek pro Clip)','Direkter Photon-Bild-zu-Video-Übergang','Loop-Modus für nahtlose Endlos-Clips','Sehr aktive Community auf Discord'],
     'cons':['Maximale Clip-Länge 10 Sek.','Native-Audio noch nicht verfügbar','Datenresidenz USA','Kosten pro 4K-Clip relativ hoch'],
     'usecases':['Social-Media-Reels','Produkt-Visualisierung','Bild-zu-Video-Workflows','Loop-Videos für Hintergründe'],
     'launched':'2024-06-12','lastUpdated':'2026-05-08',
     'website':'https://lumalabs.ai/dream-machine','domain':'lumalabs.ai',
     'features':"""- **Text-zu-Video** mit 5-, 10-Sek-Clips.
- **Image-zu-Video** mit Photon-Output ohne Re-Encode.
- **Keyframe-Modus**: Anfangs- und Endbild als Steuerung.
- **Loop-Modus** für nahtlose Endlos-Clips.
- **Camera-Motion-Presets** (Dolly, Pan, Tilt, Orbit).
- **Multi-Tool-Integration**: Photon + Dream Machine in einem Workspace.
- **API mit identischen Modellen** wie Web-UI.""",
     'pricing':"""- **Free** · 30 Credits / Mon., 5-Sek-Clips, Watermark.
- **Standard** · $10 / Mon. — 1.000 Credits, alle Features, kein Watermark.
- **Plus** · $30 / Mon. — 4.000 Credits, höhere Concurrency.
- **Unlimited** · $95 / Mon. — unbegrenzte Generierung, Priority-Queue.
- **API**: Pay-as-you-go ab $0,03 / Sek. (Standard) bis $0,18 / Sek. (4K Premium).
- **Enterprise** · auf Anfrage — Volumen-Pricing, Custom-Modelle.""",
     'overview':"""**Luma Dream Machine** ist Lumas Video-Modell — gestartet Juni 2024, seitdem zu einem der **populärsten Video-Generatoren** für Social-Media- und Produkt-Workflows gewachsen. Wer mit Luma Photon Bilder generiert, hat hier den direktesten Pfad zur Animation in einem Tool und unter einem Pricing.

Die **Geschwindigkeit** ist die zentrale Stärke: 5-Sek-Clips in 15 Sek., 10-Sek-Clips in 40 Sek. Das ist deutlich schneller als Sora 2 (1–4 Min.) oder Veo 3 (40–90 Sek.). Für iterative Workflows — wo viele Variationen verglichen werden — ein massiver Produktivitäts-Vorteil.

Der **Photon-Bild-zu-Video-Übergang** ist der zweite große Hebel: Generiertes Photon-Bild in der Web-UI auswählen, einen Klick — und Dream Machine animiert es ohne Re-Encode oder Qualitätsverlust. Für Storyboarding und Mockup-Workflows ein durchgängiger Pfad, den Konkurrenten nur mit mehreren Tools abbilden.

Der **Keyframe-Modus** ist ein versteckter Hebel: Statt nur Text-Prompt steuert man mit einem Anfangs- und einem Endbild. Was zwischen den Frames passiert, interpretiert Dream Machine — sehr nützlich für präzise Animation in Werbe-Mockups.

Der **Loop-Modus** generiert nahtlos zyklische Clips — perfekt für Social-Media-Hintergründe, Produkt-Hero-Videos und Web-Background-Animation.

Die **Camera-Motion-Presets** (Dolly, Pan, Tilt, Orbit) machen Kamera-Steuerung explizit — kein Prompt-Engineering nötig, um konsistente Cinematic-Bewegungen zu bekommen.

Die **API** ist preislich konkurrenzfähig — 5-Sek-Clips ab $0,15 — und spiegelt die Web-Modelle. Für Engineering-Pipelines ein praktischer Pfad.

Schwächen: Die **maximale Clip-Länge** liegt bei 10 Sekunden — Sora 2 schafft 60, Kling sogar 2 Min. **Native-Audio** ist noch nicht verfügbar — wer Sound braucht, muss separat ergänzen. **4K-Output** verdoppelt die Credit-Kosten.

Empfohlen für Workflows, in denen Photon und Dream Machine als integrierter Bild-zu-Video-Stack genutzt werden — und für Social-Media-Teams, die Geschwindigkeit über maximale Clip-Länge stellen."""},

    {'slug':'opus-clip','name':'Opus Clip','vendor':'Opus Clip','category':'video-audio',
     'tagline':'KI-Editor für Long-zu-Short-Form: Aus 60-Min-Podcasts oder YouTube-Videos werden virale 30-Sek-Clips mit Captions, Highlights und Hook-Optimierung.',
     'price':'Free 60 Min/Mon. · Pro ab $19 / Mon.','api':True,'dsgvo':'bedingt','origin':'USA',
     'rating':4.7,'reviews':9180,
     'pros':['Spart 80% der manuellen Schnitt-Arbeit','ClipAnything: jeder Moment durchsuchbar','Auto-Captions in 28 Sprachen','Direkter Multi-Plattform-Export'],
     'cons':['Hook-Auswahl manchmal generisch','Datenresidenz USA','Längere Videos brauchen 5–15 Min Verarbeitungszeit','Brand-Templates erst in Pro-Tarif'],
     'usecases':['Podcast-zu-Reels','YouTube-Long-zu-Short','Social-Media-Promo-Clips','Webinar-Highlights'],
     'launched':'2023-03-15','lastUpdated':'2026-05-08',
     'website':'https://www.opus.pro/','domain':'opus.pro',
     'features':"""- **ClipGenius** identifiziert virale Momente in Long-Form-Videos.
- **ClipAnything**: Volltextsuche im Video für gezielten Clip-Schnitt.
- **Auto-Captions** in 28 Sprachen mit Style-Templates.
- **Hook-Optimization** mit AI-generierten Pre-Roll-Texten.
- **Multi-Plattform-Export**: TikTok-, Reels-, Shorts-, LinkedIn-Format.
- **Brand-Templates** für konsistente Visual-Identity.
- **API** für Workflow-Integration.""",
     'pricing':"""- **Free** · 60 Minuten Verarbeitung / Mon., Watermark.
- **Starter** · $19 / Mon. — 300 Min / Mon., kein Watermark.
- **Pro** · $39 / Mon. — 1.200 Min / Mon., Brand-Templates, AI Reframe.
- **Business** · $99 / Mon. — 4.000 Min / Mon., Team-Workspaces.
- **Enterprise** · auf Anfrage — SSO, höhere Volumen, Custom-Branding.
- **API** in Pro+ Tarifen enthalten.""",
     'overview':"""**Opus Clip** ist seit März 2023 der **De-facto-Standard für Long-zu-Short-Form-Conversion** — 60-Min-Podcasts, 90-Min-Webinare oder 20-Min-YouTube-Videos werden in dutzende virale 30-Sek-Clips umgewandelt, mit Captions, Hook-Texten und Plattform-spezifischer Aspect-Ratio.

Die **Kernfunktion** ist **ClipGenius**: Eine KI scannt das Long-Form-Video, identifiziert die emotional und inhaltlich stärksten Momente, schneidet sie als Standalone-Clips zusammen und generiert einen Hook-Text als Vorspann. Was manuell zwei Tage Schnittarbeit wäre, ist hier ein Workflow von 10 Minuten — inklusive Verarbeitungszeit.

**ClipAnything** (seit Mitte 2024) ist die Erweiterung: Statt nur viralen Momenten zu vertrauen, kann jeder Moment per Volltextsuche im Video gefunden und als Clip exportiert werden. „Finde den Moment, in dem über DSGVO gesprochen wird" — und 30 Sekunden später ist der passende Clip fertig.

Die **Auto-Captions** funktionieren in 28 Sprachen (inkl. Deutsch mit hoher Genauigkeit) mit Style-Templates für TikTok-, Reels- und Shorts-Optik. Wort-für-Wort-Hervorhebung, Karaoke-Style oder simple Untertitel — alles konfigurierbar.

Die **Hook-Optimization** generiert AI-Pre-Roll-Texte, die in den ersten 1–2 Sekunden des Clips erscheinen — der wichtigste Faktor für Stop-Scroll-Verhalten auf TikTok und Reels. Die Vorschläge sind nicht immer brilliant, aber als Startpunkt deutlich schneller als blank script.

**Multi-Plattform-Export** generiert dieselbe inhaltliche Sequenz in TikTok-, Reels-, Shorts-, LinkedIn- und Twitter-Aspect-Ratio mit Plattform-spezifischen Caption-Styles.

Die **Brand-Templates** (in Pro-Tarifen) ermöglichen konsistente Visual-Identity über alle Clips — Logo-Position, Caption-Font, Farbschema, Intro-Outro.

Schwächen: Die **Hook-Auswahl** ist manchmal generisch — wer Premium-Quality braucht, schreibt Hooks selbst. **Längere Videos** (90+ Min.) brauchen 5–15 Min Verarbeitungszeit. **Brand-Templates** sind erst ab Pro-Tarif verfügbar — Starter-User müssen manuell anpassen.

Empfohlen für Podcast-Hosts, YouTube-Creators und B2B-Marketers, die regelmäßig Long-Form-Content produzieren und systematisch in Short-Form-Reichweite umwandeln wollen."""},

    {'slug':'adobe-podcast','name':'Adobe Podcast','vendor':'Adobe','category':'video-audio',
     'tagline':'Adobes KI-getriebener Audio-Cleanup-Service — schmutzige Audio-Aufnahmen in Studio-Quality verwandeln, plus eingebauter Browser-Recorder mit Multi-Track-Editing.',
     'price':'Free unbegrenztes Enhance · Pro in CC enthalten','api':False,'dsgvo':'ja','origin':'USA',
     'rating':4.7,'reviews':12340,
     'pros':['Beste KI-Audio-Cleanup im Markt (Enhance)','Komplett kostenlos, ohne Watermark','Browser-basiert, kein Download nötig','Multi-Track-Editor inklusive'],
     'cons':['Sprache leicht „künstlich" bei aggressivem Enhance','Effekte begrenzt im Vergleich zu Audacity oder Audition','API nicht öffentlich','Datenresidenz USA bleibt'],
     'usecases':['Podcast-Audio-Cleanup','Voice-Over-Restauration','Interview-Aufnahmen','Webinar-Audio-Optimierung'],
     'launched':'2022-10-19','lastUpdated':'2026-05-08',
     'website':'https://podcast.adobe.com/','domain':'adobe.com',
     'features':"""- **Enhance**: Studio-Quality-Cleanup für jede Audio-Aufnahme.
- **Multi-Track-Editor** im Browser mit Drag-and-Drop.
- **Mic Check**: Live-Analyse der Aufnahme-Qualität.
- **Recording-Sessions** für Remote-Interviews mit Audio-Sync.
- **Auto-Transcription** mit Speaker-Identification.
- **Click-Removal** und **Plosive-Reduction**.
- **Export** als WAV, MP3 oder direkt zu Podcast-Plattformen.""",
     'pricing':"""- **Adobe Podcast Enhance** · komplett kostenlos, unbegrenzt, ohne Watermark.
- **Recording-Sessions** · kostenlos in Beta.
- **Premium-Features** · in Adobe Creative Cloud (ab €24,19 / Mon.) enthalten.
- **Adobe Audition** für komplexere Edits · in CC All Apps inkludiert.
- **Enterprise** · über CC for Teams, EU-Datenresidenz möglich.""",
     'overview':"""**Adobe Podcast** ist Adobes KI-getriebener Audio-Service — gestartet Oktober 2022 mit dem Killer-Feature **Enhance**, seitdem zur am häufigsten empfohlenen Audio-Cleanup-Anwendung der Branche gewachsen. Was an dem Tool verblüfft: Es ist **vollständig kostenlos**, ohne Watermark, ohne Limit, ohne Account-Friktion.

**Enhance** ist das Killer-Feature: Eine Audio-Aufnahme — schmutzig, hallend, mit Hintergrundgeräuschen, vielleicht aus einer schlechten Zoom-Session — wird in Studio-Quality verwandelt. Hintergrund-Geräusche verschwinden, Halligkeit wird neutralisiert, die Stimme klingt wie aus einem professionellen Podcast-Studio. Für Podcaster, Voice-Over-Künstler:innen und Webinar-Hosts ein massiv beschleunigender Workflow gegenüber manuellen DAW-Sessions in Audacity oder Audition.

Der **Multi-Track-Editor** im Browser ist eine kompetente Komplett-Alternative für simple Podcast-Edits — Drag-and-Drop von Tracks, Trim, Fade, Volume-Automation. Was bei Audacity 10 Klicks brauchte, ist hier ein Browser-Workflow von 3 Klicks.

**Recording-Sessions** ermöglichen Remote-Interviews mit Audio-Sync — jede:r Teilnehmer:in nimmt lokal in höchster Qualität auf, die Tracks werden serverseitig synchronisiert. Konkurrent zu Riverside.fm und Squadcast, kostenlos in Beta.

**Auto-Transcription** mit Speaker-Identification ist sauber und schnell — für Show-Notes-Produktion und Such-Index praktisch.

**Mic Check** analysiert eine kurze Test-Aufnahme und gibt konkrete Empfehlungen für Mikrofon-Positionierung, Raum-Akustik und Aufnahme-Pegel — ein versteckter Hebel für bessere Source-Quality.

Die **Integration** in das Adobe-Ökosystem ist die strategische Stärke: Wer **Premiere Pro** oder **Audition** im Stack hat, bekommt Enhance auch dort als Filter.

Schwächen: Bei **aggressivem Enhance** klingt die Sprache leicht „künstlich" — die De-Reverberation ist manchmal zu aggressiv. **Effekte** (EQ, Compression, Reverb) sind im Browser-Editor begrenzt — wer komplexere Mixes braucht, geht zu Audition. **API ist nicht öffentlich** — Engineering-Pipelines müssen manuell gegen die UI arbeiten.

Empfohlen für Podcaster, Voice-Over-Künstler:innen und Webinar-Hosts, die regelmäßig Audio-Cleanup brauchen — und für jeden, der die einfachste, kostenlose Variante sucht, schmutzige Audio-Aufnahmen in publishable Quality zu verwandeln."""},
]

DOMAINS = {t['slug']: t['domain'] for t in TOOLS}

r = requests.post(f'{BASE}/auth/login',
    data={'grant_type':'password','username':ENV['EMAIL'],'password':ENV['PW']},
    headers={'Content-Type':'application/x-www-form-urlencoded'}, verify=False)
H = {'Authorization': f'Bearer {r.json()["access_token"]}'}
JH = {**H, 'Content-Type':'application/json'}
print('✓ Logged in')

cts = requests.get(f'{BASE}/{SITE}/contenttypes/', headers=JH, verify=False).json()
tool_ct = next(c for c in cts if c.get('display_identifier') == 'tool')
TOOL_CT_ID = tool_ct['id']

items, page = [], 1
while True:
    r = requests.get(f'{BASE}/{SITE}/elements/?type_id={TOOL_CT_ID}&size=200&page={page}',
        headers=JH, verify=False).json()
    items += r.get('items', [])
    if not r.get('has_next'): break
    page += 1
existing_by_slug = {el['data'].get('slug'): el for el in items}
print(f'  · {len(existing_by_slug)} tool slugs already in CMS')

def fetch_logo(domain: str, size: int = 128) -> bytes:
    url = f'https://www.google.com/s2/favicons?domain={domain}&sz={size}'
    r = requests.get(url, timeout=30); r.raise_for_status(); return r.content

for tool in TOOLS:
    slug = tool['slug']
    domain = DOMAINS[slug]
    el = existing_by_slug.get(slug)

    if not el:
        payload = {'type_id': TOOL_CT_ID, 'published': True, 'data': {
            'slug': slug, 'name': tool['name'], 'vendor': tool['vendor'], 'category': tool['category'],
            'tagline': tool['tagline'], 'price': tool['price'], 'api': tool['api'], 'dsgvo': tool['dsgvo'],
            'origin': tool['origin'], 'rating': tool['rating'], 'reviews': tool['reviews'],
            'pros': tool['pros'], 'cons': tool['cons'], 'usecases': tool['usecases'],
            'launched': tool['launched'], 'lastUpdated': tool['lastUpdated'],
            'website': tool['website'], 'features': tool['features'], 'pricing': tool['pricing'],
        }}
        r = requests.post(f'{BASE}/{SITE}/elements/',
            json=payload, headers=JH, verify=False)
        if not r.ok:
            print(f'✗ {slug}: create failed: {r.status_code} {r.text[:200]}'); continue
        el = r.json()
        existing_by_slug[slug] = el
        print(f'✓ {slug}: created (id={el["id"]})')
        if not el.get('published'):
            requests.patch(f'{BASE}/{SITE}/elements/{el["id"]}',
                json={'published': True}, headers=JH, verify=False)
    else:
        print(f'· {slug}: exists (id={el["id"]})')

    existing_data = el.get('data', {})
    patches = {}

    if not existing_data.get('post_id'):
        post_payload = {
            'title': f'{tool["name"]} im Überblick',
            'slug': f'{slug}-uebersicht',
            'content': tool['overview'],
            'status': 'published',
        }
        r = requests.post(f'{BASE}/{SITE}/posts/', json=post_payload, headers=JH, verify=False)
        if r.ok:
            patches['post_id'] = r.json()['id']
            print(f'  ✓ post #{patches["post_id"]} ({len(tool["overview"])} chars)')
        else:
            print(f'  ✗ post failed: {r.status_code} {r.text[:200]}')

    if not existing_data.get('logo_id'):
        try:
            png = fetch_logo(domain)
            local = LOGOS_DIR / f'{slug}.png'
            local.write_bytes(png)
            with open(local, 'rb') as fh:
                files = {'file': (f'{slug}-logo.png', fh, 'image/png')}
                data = {
                    'name': f'{tool["name"]} Logo',
                    'alt_text': f'Logo von {tool["name"]}',
                    'description': f'Offizielles Logo von {tool["name"]} ({domain}).',
                }
                rl = requests.post(f'{BASE}/{SITE}/media/',
                    files=files, data=data, headers=H, verify=False, timeout=120)
            if rl.ok:
                patches['logo_id'] = rl.json()['id']
                print(f'  ✓ logo #{patches["logo_id"]} ({len(png):,} bytes from {domain})')
            else:
                print(f'  ✗ logo upload failed: {rl.status_code} {rl.text[:200]}')
        except Exception as e:
            print(f'  ✗ logo fetch failed: {e}')

    if patches:
        new_data = {**existing_data, **patches}
        if isinstance(new_data.get('post_id'), dict):
            new_data['post_id'] = patches.get('post_id', existing_data.get('post_id'))
        r = requests.patch(f'{BASE}/{SITE}/elements/{el["id"]}',
            json={'data': new_data}, headers=JH, verify=False)
        if r.ok:
            print(f'  ✓ patched fields: {list(patches.keys())}')

print('\n✓ Done.')
