#!/usr/bin/env python3
"""Seed 7 bildgenerierung-category tools end-to-end (data + features + pricing + overview Post + logo + website).
Idempotent. Then run capture_tool_screenshots.mjs, upload_screenshots.py, generate_tool_images.py.
"""
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
    {'slug':'gpt-image','name':'GPT Image','vendor':'OpenAI','category':'bildgenerierung',
     'tagline':'OpenAIs flagship Bildmodell direkt in ChatGPT, Sora und über die API — fotorealistisch, textstark, instruktionsgenau.',
     'price':'In ChatGPT-Plus enthalten · API ab $0,04 / Bild','api':True,'dsgvo':'bedingt','origin':'USA',
     'rating':4.7,'reviews':5210,
     'pros':['Sehr starke Texttreue im Bild (Schilder, Logos)','Multi-Turn-Editing per Chat','Hohe Instruktionstreue bei Layouts','Native API mit Per-Bild-Pricing'],
     'cons':['Pro-Bild-Kosten höher als Open-Source-Modelle','Style-Kontrolle weniger feingranular als Midjourney','Inhaltsfilter strenger als bei FLUX/SDXL','Datenresidenz USA'],
     'usecases':['Marketing-Visuals','Konzept-Mockups','Editorial-Illustrationen','Social-Media-Posts'],
     'launched':'2025-03-25','lastUpdated':'2026-04-29',
     'website':'https://openai.com/index/introducing-4o-image-generation/','domain':'openai.com',
     'features':"""- **Text-im-Bild**: Schilder, Logos und Beschriftungen werden zuverlässig korrekt gerendert.
- **Multi-Turn-Editing**: Bilder im Chat-Verlauf iterativ verfeinern.
- **Instruct-following** auf Niveau eines guten Sprachmodells.
- **Bildvarianten** und **Inpainting** über die API.
- **Sora Images**-Oberfläche mit Mood-Boards und Sammlungen.
- **API mit Per-Bild-Pricing** ab ca. $0,04 (low) bis $0,19 (high quality).
- **C2PA-Wasserzeichen** für Inhalts-Provenienz.""",
     'pricing':"""- **ChatGPT Free** · einzelne Bilder pro Tag.
- **ChatGPT Plus** · $20 / Mon. — großzügiges Bilder-Kontingent in Sora Images.
- **ChatGPT Pro** · $200 / Mon. — Priority Access, höhere Limits.
- **API low** · ca. $0,04 / Bild (1024×1024).
- **API medium/high** · $0,07–$0,19 / Bild je nach Größe und Quality.
- **Enterprise** · auf Anfrage — SSO, EU-Datenresidenz, BAA.""",
     'overview':"""**GPT Image** (intern als gpt-image-1 / dall·e-4 entwickelt) ist seit März 2025 OpenAIs flagship Bildgenerator und der Standard für viele Marketing- und Editorial-Workflows geworden. Was das Modell von der vorherigen DALL·E-3-Generation und auch von vielen Konkurrenten abhebt, ist die **Texttreue**: Schilder, Logos, Beschriftungen, Code-Snippets im Bild — alles wird zuverlässig korrekt gerendert.

Der zweite große Fortschritt ist die **Instruktionstreue**: Komplexe Prompts mit fünf, sechs Anforderungen (Bildausschnitt, Stil, Komposition, Farben, Stimmung) werden deutlich präziser umgesetzt als bei früheren Modellen. Wer für Briefings produziert, spart Iterationsrunden.

**Multi-Turn-Editing** im ChatGPT-Interface ist der Killer-Workflow: Erst ein Mood-Bild generieren, dann „Mach das Hemd dunkler", „Setze die Person auf einen Bürostuhl", „Tausche den Hintergrund gegen ein Loft" — jede Iteration baut auf dem vorigen Bild auf, statt von vorn zu starten. **Sora Images** als dedizierte Oberfläche bündelt das mit Sammlungen und Mood-Boards.

Über die **API** ist GPT Image klar pay-per-use: low-Quality ab $0,04, high ab $0,19 pro Bild. Für Volumen-Workflows (Produktfotos, Variationen) eine planbare Kostenkurve.

Schwächen: Style-Kontrolle ist weniger feingranular als bei Midjourney — kein Style-Reference und keine Stylize-Achse. Die Inhaltsfilter sind strenger als bei FLUX oder SDXL, was für Werbung und Editorial selten stört, für künstlerische Arbeit aber einschränkend wirkt.

Empfohlen für Teams, die ChatGPT bereits als Sprachmodell-Basis nutzen — und für jeden, der hohe Texttreue im Bild und schnelle Iterationen über alles andere stellt."""},

    {'slug':'nano-banana','name':'Nano Banana','vendor':'Google DeepMind','category':'bildgenerierung',
     'tagline':'Googles Gemini 2.5 Flash Image — der „Nano Banana"-Codename ist legendär: extrem schnell, charakter-konsistent, Multi-Image-Editing.',
     'price':'In Gemini-App enthalten · API ab $0,039 / Bild','api':True,'dsgvo':'bedingt','origin':'USA',
     'rating':4.8,'reviews':6840,
     'pros':['Charakter-Konsistenz über mehrere Bilder hinweg','Sehr schnelle Generierung (~2 Sek.)','Multi-Image-Composition als Stärke','Native Google-Workspace-Integration'],
     'cons':['Texttreue noch unter GPT Image','Inhaltsfilter im Free-Tarif streng','EU-Datenresidenz erst Enterprise','Style-Diversität geringer als FLUX'],
     'usecases':['Storyboards','Produktvarianten','Marketing-Visuals','Konsistente Charaktere'],
     'launched':'2025-08-26','lastUpdated':'2026-04-28',
     'website':'https://deepmind.google/models/gemini-image/','domain':'deepmind.google',
     'features':"""- **Charakter-Konsistenz**: dieselbe Person in mehreren Szenen, ohne Style-Drift.
- **Multi-Image-Editing**: bis zu 14 Referenzbilder pro Prompt verschmelzen.
- **Sehr schnelle Generierung**, typisch 2–3 Sekunden pro Bild.
- **Conversational Editing** in der Gemini-App und in AI Studio.
- **Native Workspace-Integration** (Slides, Docs, Sheets).
- **API** in der Gemini API mit Per-Bild-Pricing.
- **SynthID-Wasserzeichen** unsichtbar in jedem Bild.""",
     'pricing':"""- **Gemini App** · Free mit Tageslimit, in Gemini Advanced ($20/Mon.) deutlich höher.
- **Google AI Studio** · Free zum Experimentieren.
- **API** · $0,039 / Bild (1024 px) bzw. $30 / 1 Mio. Output-Tokens (1290 Tokens/Bild).
- **Workspace Enterprise** · Bilder im Slides- und Docs-Editor inkludiert.
- **Vertex AI** · Enterprise-Pricing mit EU-Region.
- Bildgenerierung in der Gemini-Web-App ohne Aufpreis.""",
     'overview':"""**Nano Banana** war der inoffizielle Codename, unter dem Googles Gemini 2.5 Flash Image im August 2025 anonym auf LMArena getestet wurde — und das Modell überholte dort schlagartig alle Konkurrenten. Inzwischen ist „Nano Banana" so etabliert, dass Google den Spitznamen offiziell mitführt; der Produktname bleibt **Gemini Image**.

Die zwei großen Stärken sind **Charakter-Konsistenz** und **Multi-Image-Editing**. Charakter-Konsistenz heißt: Eine einmal generierte Person sieht in zehn weiteren Bildern erkennbar gleich aus — andere Pose, andere Szene, gleicher Mensch. Für Storyboards, Comics, Produktkataloge mit Models ein Game-Changer. Multi-Image-Editing erlaubt das Hineinmischen mehrerer Referenzbilder in einen Prompt: „Setze diese Person (Bild 1) in dieses Wohnzimmer (Bild 2) und gib ihr diesen Pullover (Bild 3)" funktioniert verblüffend gut.

Die **Geschwindigkeit** ist die zweite überraschende Stärke: 2–3 Sekunden pro Bild ermöglichen Workflows, die bei langsameren Modellen unmöglich wären — etwa Live-Variantenexploration im Kundengespräch.

**Conversational Editing** in der Gemini-App funktioniert wie bei ChatGPT: Bild generieren, dann im Chat verfeinern. Die **Workspace-Integration** macht Bildgenerierung direkt in Slides und Docs verfügbar — ohne Tool-Wechsel.

Schwächen: Die **Texttreue** ist noch unter GPT Image — wer Schilder oder Logos im Bild braucht, sollte die Konkurrenz testen. Die Inhaltsfilter im kostenlosen Gemini-Tarif sind spürbar konservativer als bei der API. Und der Style-Pool ist tendenziell „kommerziell-clean" — für künstlerisch-experimentelle Arbeit greift FLUX besser.

Empfohlen für alle, die Charakter-Konsistenz oder Multi-Image-Workflows brauchen — und für Workspace-Nutzer:innen, die Bildgenerierung als integriertes Feature wollen statt eines weiteren Tools."""},

    {'slug':'leonardo-ai','name':'Leonardo AI','vendor':'Canva (Leonardo)','category':'bildgenerierung',
     'tagline':'Mid-Tier-Workhorse mit eigenem Modellzoo, Live-Canvas und Realtime-Generierung — seit der Canva-Übernahme tief integriert.',
     'price':'Free · Apprentice ab $12 / Mon.','api':True,'dsgvo':'bedingt','origin':'Australien',
     'rating':4.5,'reviews':4920,
     'pros':['Großer Modell-Katalog (Phoenix, Lightning, Kino)','Live-Canvas mit Realtime-Edits','Brand-Kit für Style-Konsistenz','Canva-Integration nahtlos'],
     'cons':['Pro-Bild-Quality unter SOTA-Modellen','Token-System statt Bilder-Quoten verwirrt','API-Pricing weniger transparent','Mobile-App schwächer als Web'],
     'usecases':['Marketing-Visuals','Game-Assets','Stock-Ähnliches','Rapid Prototyping'],
     'launched':'2022-12-01','lastUpdated':'2026-04-25',
     'website':'https://leonardo.ai/','domain':'leonardo.ai',
     'features':"""- **Eigene Modellfamilie**: Phoenix, Lightning, Kino, Anime XL, Vision XL.
- **Live-Canvas** mit Realtime-Generierung beim Skizzieren.
- **AI Image Generator** mit Prompt-Helper und Style-Presets.
- **Universal Upscaler** für 4× Auflösung mit Detail-Refinement.
- **Brand Kit** für Logos, Fonts und Farben pro Workspace.
- **Canva-Integration**: direkt aus Canva auf Leonardo zugreifen.
- **API** mit Pay-per-Image und Webhook-Workflows.""",
     'pricing':"""- **Free** · 150 Token / Tag, eingeschränkte Modelle.
- **Apprentice** · $12 / Mon. ($10 jährlich) — 8.500 Token / Mon., kommerzielle Lizenz.
- **Artisan** · $30 / Mon. — 25.000 Token, höhere Auflösungen.
- **Maestro** · $60 / Mon. — 60.000 Token, Priority-Generierung.
- **API** · custom Pay-per-Image, ab $0,002 / Token.
- **Canva-Integration** in den Canva-Pro/Teams-Tarifen enthalten.""",
     'overview':"""**Leonardo AI** ist seit der Canva-Übernahme 2024 das Mid-Tier-Workhorse der Bildgenerierung — nicht das absolute SOTA-Modell, dafür aber ein riesiger Werkzeugkasten zu fairen Preisen und mit erstklassiger Canva-Integration.

Die zentrale Stärke ist der **Modellzoo**: Phoenix für realistische Bilder, Lightning für Speed, Kino für cinematischen Look, Anime XL für Manga-Stil, Vision XL für Fotorealismus. Wer einen bestimmten Look sucht, hat bei Leonardo eine größere Auswahl als bei den meisten Konkurrenten — und kann Modelle pro Projekt mischen.

Der **Live-Canvas** ist der zweite Hebel: Eine Skizze wird in Echtzeit zu einem fertigen Bild — Striche werden interpretiert, Komposition erhalten, der Stil wird über ein Modell kontrolliert. Für Designer ein deutlich intuitiverer Workflow als reines Prompting.

Das **Brand Kit** macht Leonardo für Marketing-Teams attraktiv: Logos, Fonts und Farben werden hochgeladen, Generierungen respektieren die Brand-Vorgaben. **Canva-Integration** schließt den Kreis — Bilder fließen direkt in Posts, Slides oder Print-Designs.

Schwächen: Pro-Bild-Quality ist gut, aber unter GPT Image, Nano Banana und FLUX 1.1. Das **Token-System** statt klarer Bilder-Quoten verwirrt viele User — ein Bild kann je nach Modell und Auflösung 1 bis 30 Token kosten. Mobile-Apps sind funktional, aber weniger ausgereift als das Web.

Empfohlen für Marketing-Teams im Canva-Ökosystem und für Game-/Concept-Artists, die einen breiten Modellzoo statt eines einzigen besten Modells brauchen — eine sehr planbare Mid-Tier-Lösung."""},

    {'slug':'krea','name':'Krea','vendor':'Krea AI','category':'bildgenerierung',
     'tagline':'Realtime-Canvas für KI-Bilder und Video — zeichnen, prompten, im Sekundentakt iterieren statt warten.',
     'price':'Free · Pro ab $10 / Mon.','api':True,'dsgvo':'bedingt','origin':'USA',
     'rating':4.6,'reviews':2630,
     'pros':['Echte Realtime-Generierung beim Tippen','Aggregator: GPT Image, FLUX, Kling, Veo in einem UI','3D-Modus und Video-Modus inkludiert','Krea Train für eigene Custom-Modelle'],
     'cons':['Pro-Tarif für Realtime-Speed nötig','UX überwältigend für Einsteiger','Pricing pro Sekunde / Compute','Kein Brand-Kit oder Style-Locking'],
     'usecases':['Live-Konzeption','Mood-Boards','Storyboards','Video-Konzepte'],
     'launched':'2023-08-01','lastUpdated':'2026-04-26',
     'website':'https://www.krea.ai/','domain':'krea.ai',
     'features':"""- **Realtime-Mode**: Bild verändert sich live beim Tippen am Prompt.
- **Multi-Model-Aggregator**: GPT Image, FLUX, Imagen, Recraft in einem UI.
- **Video-Mode**: Veo, Kling, Hailuo, Sora in derselben Oberfläche.
- **3D-Mode** für Asset-Generierung mit Krea 3D.
- **Krea Train**: eigene LoRAs aus 5–10 Bildern in 15 Min.
- **Canvas-Editor** mit Layern, Masken und Inpainting.
- **API** für Realtime-Workflows in eigenen Apps.""",
     'pricing':"""- **Free** · 10 Generationen / Tag, kein Realtime, Watermark.
- **Basic** · $10 / Mon. ($96 jährlich) — Realtime, 1.000 Gens, ohne Watermark.
- **Pro** · $35 / Mon. — 5.000 Gens, höhere Auflösungen, Krea Train.
- **Max** · $60 / Mon. — 12.000 Gens, Priority-Compute.
- **API** · Pay-per-Compute, ab $0,008 / Bild.
- Edu- und Studi-Discount auf Antrag.""",
     'overview':"""**Krea** verfolgt einen anderen Ansatz als alle anderen Bildgeneratoren: **Realtime**. Statt Prompt eingeben, Knopf drücken, 5–30 Sekunden warten und Ergebnis sehen, generiert Krea während des Tippens — das Bild verändert sich live mit jedem Wort, das hinzukommt oder weggenommen wird.

Der Effekt ist gestalterisch überraschend: Statt zu „prompten" kuratiert man visuell, weil sofort sichtbar ist, was jede Wortwahl bewirkt. Für Mood-Board-Arbeit, Concept-Exploration und schnelle Iterationen ein Workflow, den kein anderes Tool in dieser Form bietet.

Krea ist außerdem ein **Multi-Model-Aggregator**: GPT Image, FLUX, Imagen, Recraft, Veo, Kling, Hailuo, Sora — alles in einer Oberfläche, mit einheitlichem Asset-Management. Wer mit mehreren SOTA-Modellen arbeitet, spart das Tool-Hopping.

**Krea Train** ist der dritte Hebel: 5–10 Referenzbilder hochladen, 15 Minuten warten, eigenes LoRA bekommen. Für Charaktere, Produkte oder Markenwelten in eigenem Stil eine deutlich niedrigschwellige Alternative zu Custom-Diffusers-Trainings.

Der **Canvas-Editor** funktioniert wie eine Mini-Photoshop-App: Layer, Masken, Inpainting, Outpainting — alles im Browser, alles mit KI im Hintergrund. Bilder lassen sich kombinieren und nachbearbeiten ohne Tool-Wechsel.

Schwächen: Die **UX** ist für Einsteiger:innen überwältigend — drei Modi (Image, Video, 3D), zehn Modelle, dutzende Bedienelemente. Realtime-Speed gibt's erst im Pro-Tarif. Und das Pricing pro Compute statt pro Bild ist für Einsteiger schwer planbar.

Empfohlen für visuelle Konzepter:innen, Designer und Creative Directors, die im interaktiven Loop denken — und für jeden, der mit mehreren KI-Modellen parallel arbeitet und nicht ständig zwischen Tools wechseln will."""},

    {'slug':'reve','name':'Reve','vendor':'Reve','category':'bildgenerierung',
     'tagline':'Reve Image 1.0 hat im März 2025 die Bench-Spitze übernommen — exzellente Texttreue, präzise Komposition und fotografische Qualität.',
     'price':'Free (10 Bilder/Tag) · Pro ab $9 / Mon.','api':True,'dsgvo':'bedingt','origin':'USA',
     'rating':4.7,'reviews':1840,
     'pros':['Sehr präzise Text-im-Bild-Renderung','Fotografische Detailtiefe','Niedriger Einstiegspreis','API mit klarem Per-Bild-Pricing'],
     'cons':['Stylistisch enger als FLUX oder Midjourney','Noch wenige Community-LoRAs','UI weniger ausgereift','Datenresidenz USA'],
     'usecases':['Editorial-Bilder','Produktvisualisierung','Konzept-Mockups','Plakate mit Text'],
     'launched':'2025-03-26','lastUpdated':'2026-04-22',
     'website':'https://reve.com/','domain':'reve.com',
     'features':"""- **Reve Image 1.0**: SOTA-Modell mit exzellenter Komposition.
- **Text-im-Bild**: präzise Schilder, Logos, Sätze in beliebiger Sprache.
- **Aspect-Ratios** von 1:1 bis 21:9 nativ unterstützt.
- **Image-Edit-Mode** mit Inpainting und Style-Transfer.
- **API** mit Per-Bild-Pricing und Webhooks.
- **Reference-Image-Mode** für stilistische Konsistenz.
- **Negative-Prompts** für feingranulare Kontrolle.""",
     'pricing':"""- **Free** · 10 Bilder / Tag, Watermark, Standard-Auflösung.
- **Pro** · $9 / Mon. ($90 jährlich) — 800 Bilder / Mon., kein Watermark.
- **Studio** · $25 / Mon. — 3.000 Bilder, Priority-Generierung.
- **API** · ab $0,03 / Bild Standard, $0,06 / Bild High Detail.
- **Enterprise** · auf Anfrage — Custom-Quotas, SSO, dedizierte Modell-Instanzen.
- 30-Tage-Geld-zurück-Garantie auf Pro-Jahresabos.""",
     'overview':"""**Reve** kam im März 2025 fast aus dem Nichts und übernahm mit **Reve Image 1.0** prompt die Spitze mehrerer Benchmark-Leaderboards. Hinter dem Tool steht ein kleines Team aus Ex-Google-Brain-Forschern, die ein Bildmodell mit Fokus auf **Komposition, Texttreue und fotografische Qualität** trainiert haben — drei Dimensionen, die viele andere Modelle als Schwächen haben.

Die **Texttreue** ist das herausstechende Merkmal: Schilder, Logos, ganze Plakate mit komplexem Layout werden zuverlässig korrekt gerendert — auch in nicht-lateinischen Schriften. Wer für Editorial, Print oder Display-Werbung produziert, hat hier oft das beste Tool zur Hand.

Die **fotografische Qualität** ist die zweite Stärke: Hauttöne, Beleuchtung, Material-Texturen — alles wirkt natürlicher als bei den meisten Konkurrenzmodellen. Die Detailtiefe in 1024×1024-Output ist auf Niveau, das man früher nur mit Midjourney v6 oder FLUX 1.1 Pro bekam.

**Reference-Image-Mode** und **Negative Prompts** geben weitere Kontrolle. Der **Image-Edit-Mode** mit Inpainting funktioniert solide, ist aber noch nicht auf dem Niveau eines Photoshop-AI-Workflows.

Schwächen: Stilistisch ist Reve relativ eng — es kann Realismus, Editorial und „cinematic look" exzellent, aber Comic, Anime oder experimentelle Stile sind nicht die Stärke. Die Community ist noch klein, es gibt wenige LoRAs oder Custom-Modelle. Die UI ist funktional, aber an manchen Stellen rough.

Empfohlen für Editorial-Designer, Marketing-Teams mit Print-Anforderungen und alle, die das beste Tool für „Bild mit lesbarem Text" suchen — Reve ist hier 2026 die führende Option."""},

    {'slug':'magnific','name':'Magnific','vendor':'Magnific (Freepik)','category':'bildgenerierung',
     'tagline':'KI-Upscaler und Re-Imaginer — vergrößert auf 16K, fügt halluzinierte Details hinzu, transformiert Stile, ändert Beleuchtung.',
     'price':'Pro ab $39 / Mon. · 7-Tage-Trial','api':True,'dsgvo':'bedingt','origin':'Spanien',
     'rating':4.8,'reviews':2410,
     'pros':['Vergrößert mit halluzinierten Details, nicht nur Pixeln','Relight: Beleuchtung nachträglich ändern','Restyle: kompletter Style-Wechsel mit Komposition-Erhalt','Native Photoshop-Plugin'],
     'cons':['Sehr teuer im Vergleich zu klassischen Upscalern','Halluzinationen können Originalen widersprechen','Pricing pro Token statt pro Bild','Lernkurve für Slider-Settings'],
     'usecases':['Foto-Upscale','Style-Restyle','Beleuchtung ändern','Print-Vorbereitung'],
     'launched':'2024-02-01','lastUpdated':'2026-04-24',
     'website':'https://magnific.ai/','domain':'magnific.ai',
     'features':"""- **Upscale & Enhance** auf bis zu 16K Auflösung mit Detail-Halluzination.
- **Relight**: Beleuchtungsrichtung und Lichtstimmung nachträglich ändern.
- **Restyle**: kompletter Stilwechsel bei Erhalt der Komposition.
- **Magnific Mystic** als hauseigenes Generator-Modell.
- **Photoshop-Plugin** mit nativer Layer-Integration.
- **Sliders** für Creativity, Resemblance, HDR, Detail.
- **API** für Volumen-Workflows mit Webhooks.""",
     'pricing':"""- **Pro** · $39 / Mon. ($35 jährlich) — 5.500 Token, kommerzielle Lizenz.
- **Premium** · $99 / Mon. — 19.000 Token, Priority-Compute.
- **Business** · $299 / Mon. — 70.000 Token, höhere parallele Limits.
- **API** · Pay-per-Token, ab $0,015 / Token.
- **Token-Verbrauch** typisch 5–15 pro 4K-Upscale, 20–40 für 16K.
- 7-Tage-Trial für Pro ohne Zahlungsmittel.""",
     'overview':"""**Magnific** ist nicht der klassische „Bild generieren"-Tool, sondern der **Spezialist für Bild-Veredelung**: Upscaling, Re-Lighting, Re-Styling. Was Magnific von simplen Upscalern (Topaz, Gigapixel) unterscheidet, ist die **Halluzination**: Statt nur Pixel zu interpolieren, fügt Magnific tatsächlich neue Details hinzu — Hauttextur, Stoff-Webung, Pflanzen-Details — die im Original nicht existieren, aber plausibel sind.

Die zwei Slider **Creativity** und **Resemblance** sind die zentrale Steuerung: Hohe Creativity bedeutet starke Detail-Halluzination, hohe Resemblance bedeutet maximale Treue zum Original. Die Kunst liegt im richtigen Mix für den jeweiligen Anwendungsfall.

**Relight** ist die zweite Killer-Funktion: Ein Foto bekommt nachträglich neue Beleuchtung — von Tageslicht auf Goldener-Stunde, von Studio-Setup auf Cinematic Side-Light, von Kunstlicht auf Natur. Für Produktfotografie, Portraits und Stockbilder ein massiver Workflow-Hebel.

**Restyle** transformiert den ganzen Stil eines Bildes (Foto → Illustration, Realismus → Anime, modern → impressionistisch) bei weitestgehender Erhaltung der Komposition. Für Mood-Boards und Style-Frames der schnellste Weg zur visuellen Variantenerstellung.

Das **Photoshop-Plugin** integriert Magnific direkt in den Pro-Workflow — Layer aktivieren, Slider setzen, Ergebnis als neue Layer.

Schwächen: Magnific ist **teuer** — $39/Mon. ist deutlich über klassischen Upscalern, das Token-System macht Verbrauch schwer planbar. Die Halluzinationen können bei Personen-Bildern unerwünschte Veränderungen produzieren (Augenfarbe, Gesichtszüge) — Resemblance hochsetzen oder nachbessern.

Empfohlen für Foto-Profis, Werbe-Studios und Print-Designer, die regelmäßig Bilder veredeln müssen — und für jeden, der Upscaling nicht als „mehr Pixel", sondern als „mehr Wow" versteht."""},

    {'slug':'freepik-ai','name':'Freepik AI','vendor':'Freepik','category':'bildgenerierung',
     'tagline':'Design-Bundle aus AI Image, Mystic, Magnific Upscale und Stock-Asset-Bibliothek — alles unter einem Abo.',
     'price':'Free · Premium ab $9 / Mon.','api':True,'dsgvo':'ja','origin':'Spanien',
     'rating':4.4,'reviews':3870,
     'pros':['Mehrere Modelle in einem UI (Mystic, FLUX, Imagen, Reve)','Magnific-Integration im Premium-Tarif','Riesige Stock-Bibliothek dazu','EU-Anbieter mit DSGVO-Zertifizierung'],
     'cons':['Modell-Limits je nach Tarif unterschiedlich','UI etwas überladen mit Templates und Stock','Pro-Tarife stark gestaffelt','Mobile-App schwächer als Web'],
     'usecases':['Marketing-Visuals','Social-Media-Posts','Print-Layouts','Slideshow-Assets'],
     'launched':'2010-04-01','lastUpdated':'2026-04-27',
     'website':'https://www.freepik.com/ai','domain':'freepik.com',
     'features':"""- **AI Image Generator** mit Mystic, FLUX, Imagen, Reve und GPT Image.
- **Magnific Upscaler** im Premium-Tarif inkludiert.
- **AI Editor** mit Inpainting, Outpainting und Background-Removal.
- **Pikaso**: Sketch-to-Image im Realtime-Modus.
- **Stock-Bibliothek** mit 150 Mio. Vektoren, Bildern, Templates.
- **AI Video** und **AI Voice** als Bundle-Features.
- **Brand-Kit** und Team-Workspaces in höheren Tarifen.""",
     'pricing':"""- **Free** · 10 AI-Generationen / Tag, eingeschränkte Modelle, mit Attribution.
- **Premium** · $9 / Mon. ($108 jährlich) — 200 AI-Credits, Magnific-Upscale.
- **Premium+** · $14 / Mon. — 400 Credits, Mystic-Premium-Modell.
- **Pro** · $25 / Mon. — 1.500 Credits, AI-Video, kommerzielle Lizenz.
- **Teams** · $20 / Sitz / Mon. — geteilte Bibliothek, Brand-Kit.
- **API** · Pay-per-Credit, ab $0,012 / Credit.""",
     'overview':"""**Freepik** war 15 Jahre lang die größte Stock-Asset-Plattform Europas — und hat sich seit 2023 konsequent zur **AI-Suite** weiterentwickelt. Statt nur Vektoren und Bilder zu verkaufen, bietet Freepik heute einen ganzen Werkzeugkasten: AI Image Generator, AI Editor, Magnific Upscaler, AI Video — alles unter einem Abo, mit kohärenter Stockbibliothek im Hintergrund.

Der **AI Image Generator** aggregiert mehrere Top-Modelle: Mystic (Freepik-eigen), FLUX, Imagen, Reve und GPT Image. Wer das richtige Modell für den jeweiligen Job sucht, hat alles in einer Oberfläche — keine zehn Tabs, kein Tool-Wechsel.

Die **Magnific-Integration** ist der vielleicht stärkste Differentiator: Magnific kostet als Standalone $39/Mon., bei Freepik Premium ist sie ab $9/Mon. enthalten (mit Credit-Limit). Für Casual-User der günstigste Weg zum Magnific-Workflow.

**Pikaso** ist der Realtime-Modus von Freepik: Skizzieren, Prompt anpassen, sofort sehen, was passiert. Vergleichbar mit Krea, aber tiefer in die Freepik-Asset-Welt integriert.

Die **Stock-Bibliothek** mit 150 Mio. Assets bleibt ein zentraler Vorteil: Wer ein Vektor-Icon oder eine Foto-Background braucht, muss nicht zu einer separaten Plattform.

Als **EU-Anbieter** mit DSGVO-Zertifizierung ist Freepik für viele Agenturen und Behörden der bevorzugte Stack — Daten bleiben in Europa, AVV ist Standard.

Schwächen: Die UI ist mit Templates, Stock und AI etwas überladen — Einsteiger:innen brauchen Zeit zur Orientierung. Modell-Limits variieren stark nach Tarif, die Wahl des richtigen Plans erfordert Rechnen. Mobile-Apps sind funktional, aber weniger ausgereift.

Empfohlen für Marketing-Teams und Designer, die Bildgenerierung, Editing, Upscaling und Stock-Assets aus einem Tool wollen — und für DSGVO-sensible Workflows in Europa."""},
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
