#!/usr/bin/env python3
"""Add 12 more tools across all categories with complete data:
  · element (slug, name, vendor, category, tagline, price, api, dsgvo, origin, …)
  · website
  · features (Markdown)
  · pricing (Markdown)
  · overview Post + post_id reference
  · logo (Google Favicon V2)

Idempotent: every step skips work it already did.
After this, run:
  scripts/capture_tool_screenshots.mjs   (extend TOOLS list first)
  scripts/upload_screenshots.py
  scripts/generate_tool_images.py        (extend TOOL_CUES first)
"""
import requests, urllib3, sys
from pathlib import Path

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ROOT = Path(__file__).resolve().parent.parent
LOGOS_DIR = ROOT / 'logos'
LOGOS_DIR.mkdir(exist_ok=True)
ENV = {l.split('=',1)[0].strip(): l.split('=',1)[1].strip()
       for l in (ROOT/'.env').read_text().splitlines() if '=' in l and not l.startswith('#')}
BASE, SITE = ENV['BASEURL'], ENV['SITE']

# -------------------- 12 new tools --------------------
TOOLS = [
    {
        'slug':'llama','name':'Llama','vendor':'Meta','category':'sprachmodelle',
        'tagline':'Metas Open-Weights-Sprachmodelle — von 1B bis 405B Parametern, lokal lauffähig.',
        'price':'Open Source · API über Drittanbieter ab $0.10 / 1 M Token','api':True,'dsgvo':'ja','origin':'USA',
        'rating':4.5,'reviews':1980,
        'pros':['Vollständig Open Weights','Größenstufen für jeden Use-Case','Starker Reasoning-Score (Llama 3.3)','Kann lokal/on-prem laufen'],
        'cons':['Kein offizieller Chat-Client','Multimodalität noch begrenzt','Lizenz keine echte OSS (Llama Community License)'],
        'usecases':['Self-Hosting','Forschung','Embedded LLMs','RAG-Backends'],
        'launched':'2023-02-24','lastUpdated':'2026-04-09',
        'website':'https://llama.com',
        'logo_domain':'meta.com',
        'features':"""- **Llama 3.3 70B & 405B** — Spitzenleistung bei Reasoning & Code, frei verfügbar.
- **Open Weights** unter Llama-Community-License (kommerziell nutzbar bis 700 M MAU).
- **Llama Stack** — offizielles Ökosystem für Inference, Fine-Tuning, Agenten.
- **Llama Guard** für Output-Sicherheit.
- **Multimodale Varianten** (Llama 3.2 Vision) für Bildeingaben.
- **Verfügbar über Hugging Face, Together AI, Groq, AWS Bedrock, Vertex AI.**""",
        'pricing':"""- **Self-Hosted** — kostenlos, benötigt GPU-Hardware (z. B. A100, H100 für 70B-Modelle).
- **Together AI** · ab $0.10 / 1 M Token (Llama 3.3 70B).
- **Groq** · extrem schnelle Inferenz, ähnlich günstig.
- **AWS Bedrock / Vertex AI** · pay-as-you-go, mit EU-Datenresidenz.
- **Lizenz** kostenlos für die meisten kommerziellen Anwendungen.""",
        'overview':"""**Llama** von Meta ist die wichtigste Open-Weights-Modellfamilie der letzten zwei Jahre. Anders als ChatGPT oder Claude wird Llama nicht als fertiges Produkt verkauft — Meta veröffentlicht die Modellgewichte unter einer eigenen Lizenz, die kommerzielle Nutzung erlaubt, solange das Unternehmen nicht über 700 Millionen monatliche Nutzer hat.

Mit Llama 3.3 (Dezember 2024) und der angekündigten Llama-4-Generation hat Meta die Lücke zu den geschlossenen Spitzenmodellen weitgehend geschlossen. Reasoning-Benchmarks erreichen GPT-4-Niveau bei deutlich niedrigeren Inferenzkosten, da das Modell auch in spezialisierten Cloud-Diensten wie Together AI oder Groq läuft.

Für Unternehmen ist das interessant aus drei Gründen: erstens **Self-Hosting** (Daten verlassen die eigene Infrastruktur nicht), zweitens **vorhersagbare Kosten** ohne Token-Vendor-Lock-in, drittens **Anpassbarkeit** durch Feintuning auf eigene Daten.

Schwächen liegen vor allem im Ökosystem: Es gibt keinen offiziellen Meta-Chat-Client, die Tool-Use- und Function-Calling-Konventionen sind über Drittanbieter implementiert, und die Lizenz ist trotz Offenheit keine reine Open-Source-Lizenz im OSI-Sinn.""",
        'cue':'A stylized llama silhouette with a tightly wound coil of string forming the body, a magenta dot as the eye — open, friendly, weaving.',
        'screenshot_url':'https://llama.com/',
    },
    {
        'slug':'cohere','name':'Cohere Command','vendor':'Cohere','category':'sprachmodelle',
        'tagline':'Enterprise-LLM aus Toronto — RAG-first, mehrsprachig, mit nativer EU-Verfügbarkeit.',
        'price':'API ab $0.50 / 1 M Token (Command R)','api':True,'dsgvo':'ja','origin':'CA / EU',
        'rating':4.3,'reviews':460,
        'pros':['Klarer Enterprise-Fokus','Embed-Modell weltklasse','Verfügbar in EU-Cloud-Regionen','Mehrsprachigkeit (100+ Sprachen)'],
        'cons':['Kein eigener Chat-Client','Schwächer in reinen Conversational-Benchmarks','Branding für Endnutzer kaum bekannt'],
        'usecases':['RAG-Pipelines','Enterprise-Suche','Mehrsprachige Klassifikation','Reranking'],
        'launched':'2021-11-16','lastUpdated':'2026-04-04',
        'website':'https://cohere.com',
        'logo_domain':'cohere.com',
        'features':"""- **Command R / R+ / R7B** — drei Größen für jeden Latenz-/Kostenpunkt.
- **Embed v3** — eines der stärksten multilingualen Embedding-Modelle.
- **Rerank 3** — präzises Re-Ranking für RAG-Pipelines.
- **Tool Use & Function Calling** mit nativer JSON-Mode-Unterstützung.
- **Citations** als First-Class-Feature in der Antwort-API.
- **Verfügbar auf AWS, Google Cloud, Azure, Oracle Cloud — auch in EU-Regionen.**""",
        'pricing':"""- **Free** · 1.000 API-Calls/Monat zum Ausprobieren.
- **Command R** · $0.50 / 1 M Input · $1.50 / 1 M Output Token.
- **Command R+** · $2.50 / 1 M Input · $10.00 / 1 M Output (für Top-Performance).
- **Command R7B** · $0.04 / 1 M Token (für Edge-/Mobile-Deployments).
- **Enterprise / On-Prem** · individuell, mit DPA, EU-Datenresidenz und Single-Tenant-Optionen.""",
        'overview':"""**Cohere** ist die wohl pragmatischste Wahl für Unternehmen, die einen LLM-Anbieter mit klarem B2B-Fokus suchen. Das kanadische Startup wurde 2019 von Aidan Gomez (einem Co-Autor des „Attention is All You Need"-Papers) und ehemaligen Google-Brain-Forschern gegründet — und hat von Anfang an konsequent auf Enterprise statt Consumer gesetzt.

Die Command-Familie liefert solide Reasoning- und Chat-Qualität, aber die wirklichen Stärken liegen bei zwei spezialisierten Modellen: **Embed** und **Rerank**. Wer eine RAG-Pipeline (Retrieval-Augmented Generation) baut, kommt an Cohere kaum vorbei — die Embeddings dominieren in mehrsprachigen Benchmarks, das Rerank-Modell hebt die Trefferqualität spürbar.

Strategisch wichtig: Cohere ist über alle drei US-Hyperscaler **plus Oracle Cloud** verfügbar, mit **EU-Datenresidenz-Optionen**. Damit eignet sich der Anbieter besonders gut für deutschsprachige Konzerne mit DSGVO-Anforderungen.

Was fehlt: ein bekanntes Endkundenprodukt. Wer einfach „nur einen Chatbot" sucht, wird hier nicht fündig — Cohere setzt voll auf API + Plattform.""",
        'cue':'A stylized graph with three concentric arcs meeting at a single magenta point — a quiet emblem of retrieval and ranking.',
        'screenshot_url':'https://cohere.com/',
    },
    {
        'slug':'recraft','name':'Recraft','vendor':'Recraft','category':'bildgenerierung',
        'tagline':'Bildgenerator für Designer — Vektor- und Raster-Outputs mit konsistenter Markenpalette.',
        'price':'Freemium — Pro ab $10 / Mon.','api':True,'dsgvo':'bedingt','origin':'USA',
        'rating':4.4,'reviews':380,
        'pros':['SVG-/Vector-Output (echte Pfade, nicht nur Bitmap)','Brand-Style-Library','Recraft V3 mit klarer Typografie','API für Production'],
        'cons':['Kleinere Community als Midjourney','Style-Bandbreite eher minimalistisch'],
        'usecases':['Icon-Sets','Marketing-Visuals','Vector-Illustrationen','Logo-Konzepte'],
        'launched':'2023-08-01','lastUpdated':'2026-04-12',
        'website':'https://www.recraft.ai',
        'logo_domain':'recraft.ai',
        'features':"""- **Recraft V3** — eigenes Modell mit fotorealistischer und vektorhafter Generierung in einem.
- **Vector Mode** — direkter SVG-Export mit sauberen Pfaden, keine Auto-Trace-Konvertierung.
- **Style Library** — eigene Markenstile speichern und konsistent wiederverwenden.
- **Image Editor** mit Inpainting, Removal und Replace.
- **Mockup Generator** für Produkt-Visualisierungen.
- **API** für skalierte Produktion (Marketing, E-Commerce).""",
        'pricing':"""- **Free** · 50 Credits/Tag, nur persönliche Nutzung.
- **Basic** · $10 / Monat · 1.000 Credits, kommerzielle Nutzung.
- **Advanced** · $33 / Monat · 5.000 Credits, Priority Queue.
- **Pro** · $60 / Monat · 10.000 Credits, höchste Modelle.
- **API** · pay-as-you-go ab $0.04 / Bild (Recraft V3).""",
        'overview':"""**Recraft** hat eine ungewöhnliche Nische besetzt: Während Midjourney und Stable Diffusion Bitmap-Bilder erzeugen, liefert Recraft auf Wunsch **echte Vector-SVGs** — also skalierbare Pfade, nicht nur hochauflösende Pixel. Das macht das Tool für Designer, Brand-Teams und alle, die Output direkt in Figma oder Illustrator weiterverarbeiten, deutlich nützlicher.

Mit Recraft V3 (Ende 2024) erreichte das eigene Modell einen Sprung in der Typografie-Qualität, der vor allem für Plakate, Headlines und Logo-artige Kompositionen relevant ist. Recraft V3 belegte zeitweise Platz 1 im Artificial-Analysis-Image-Arena-Ranking, vor DALL·E 3 und Midjourney.

Die **Brand Style Library** ist das zweite Alleinstellungsmerkmal: Eigene visuelle Stile lassen sich speichern und auf neue Prompts anwenden — ein Workflow, den große Marken brauchen, der bei General-Purpose-Tools wie Midjourney aber nur über umständliche Style-References funktioniert.

Schwächen: Die Community ist deutlich kleiner als bei den großen Marken, und die stilistische Bandbreite tendiert zum Aufgeräumten. Wer wilde, expressive Looks sucht, ist anderswo besser aufgehoben.""",
        'cue':'A stylized vector pen tool with three control-point handles, one tinted magenta, drawing a smooth curve — the essence of vector design.',
        'screenshot_url':'https://www.recraft.ai/',
    },
    {
        'slug':'pika','name':'Pika','vendor':'Pika Labs','category':'video-audio',
        'tagline':'Verspieltes Text-zu-Video mit starken Effekt-Presets — schnelle Social-Clips in Sekunden.',
        'price':'Freemium — Standard $10 / Mon.','api':False,'dsgvo':'bedingt','origin':'USA',
        'rating':4.2,'reviews':720,
        'pros':['Pika 2.2 mit deutlich verbesserter Bewegungskohärenz','Pikaffects (kreative Effekt-Bibliothek)','Lipsync für gesprochene Videos','Sehr aktive Discord-Community'],
        'cons':['Keine offizielle API','Clip-Länge weiterhin auf 10 s begrenzt','Output qualitativ teils hinter Runway/Sora'],
        'usecases':['Social-Media-Clips','Werbung','Musikvideo-Snippets','Mood-Pieces'],
        'launched':'2023-04-01','lastUpdated':'2026-04-15',
        'website':'https://pika.art',
        'logo_domain':'pika.art',
        'features':"""- **Pika 2.2** — neueste Modellgeneration mit längerer Bewegungs-Kohärenz.
- **Pikaffects** — kuratierte Effekte (Explode, Squish, Crush, Inflate) per Klick.
- **Lipsync** — Audio auf einen Avatar oder eine Figur mappen.
- **Image-to-Video** — eigenes Bild als Startframe.
- **Modify Region** — gezielt Bildteile per Maske animieren.
- **Verschiedene Aspect Ratios** (9:16, 16:9, 1:1).""",
        'pricing':"""- **Basic (Free)** · 250 Credits einmalig zum Ausprobieren.
- **Standard** · $10 / Mon. · 700 Credits/Monat, kommerzielle Nutzung.
- **Pro** · $35 / Mon. · 2.300 Credits, Pika Effects, Lipsync.
- **Fancy** · $95 / Mon. · 6.000 Credits, höchste Auflösungen.
- **Annual** mit ~20 % Rabatt; keine API für externe Integration.""",
        'overview':"""**Pika** ist der spielerische Gegenspieler zu Runway und OpenAI Sora im Bereich der KI-Videogenerierung. Wo Runway eher auf Filmemacher zielt und Sora technologisch dominiert, hat Pika seine Nische in der Social-Media-Kreation gefunden — schnelle, oft humorvolle Clips, die in TikTok- und Instagram-Feeds funktionieren.

Mit Pika 2.2 (Anfang 2026) hat das Team die Bewegungs-Kohärenz und die Konsistenz von Charakteren über mehrere Frames spürbar verbessert. Charakteristisch sind die **Pikaffects** — eine Bibliothek vorgefertigter visueller Effekte (Crush, Explode, Inflate), die mit einem Klick auf jedes Eingangsbild angewandt werden. Das senkt die Einstiegshürde für Nutzer, die nicht stundenlang Prompts feinschleifen wollen.

Die **Lipsync-Funktion** war Anfang 2024 das erste massentaugliche Feature ihrer Art und brachte Pika eine eigene Welle an Memes und Trends. Heute ist sie in vielen Tools verfügbar, Pikas Implementierung gilt aber weiterhin als besonders unkompliziert.

Limitierungen: Es gibt **keine öffentliche API**, was Pika als Backend-Komponente in Pipelines unbrauchbar macht. Die Clip-Länge bleibt auf 10 Sekunden beschränkt, höhere Auflösungen kosten viele Credits.""",
        'cue':'A small abstract film clip frame with a tiny magenta star bursting at one corner — playful, kinetic motion.',
        'screenshot_url':'https://pika.art/',
    },
    {
        'slug':'heygen','name':'HeyGen','vendor':'HeyGen','category':'video-audio',
        'tagline':'KI-Avatare aus dem Browser — Live-Streaming-Avatare und Real-Time-Translation inklusive.',
        'price':'Freemium — Creator $24 / Mon.','api':True,'dsgvo':'bedingt','origin':'USA',
        'rating':4.5,'reviews':1620,
        'pros':['Sehr realistische Mimik','Über 700 Stock-Avatare in 175+ Sprachen','Live-Streaming-Avatare (Interactive Avatar)','Real-Time-Translation in Webinaren'],
        'cons':['Custom-Avatare benötigen Studio-Aufnahme','Höhere Tarife sehr teuer','US-Datenresidenz Standard'],
        'usecases':['Trainingsvideos','Marketing','Customer-Onboarding','Live-Events mit Übersetzung'],
        'launched':'2020-11-15','lastUpdated':'2026-04-18',
        'website':'https://www.heygen.com',
        'logo_domain':'heygen.com',
        'features':"""- **700+ Stock-Avatare** — divers besetzt, 175+ Sprachen.
- **Avatar IV** — fotorealistische, hochaufgelöste Generationen.
- **Interactive Avatar** — Live-Streaming-Avatare mit Echtzeit-Antworten.
- **Real-Time Translation** — Live-Stimme in Live-Output anderer Sprache.
- **Brand Kits & Custom Voice Clones** für konsistente Markenkommunikation.
- **API + Webhooks** für skalierbare Produktion.""",
        'pricing':"""- **Free** · 3 Min. Video/Mon., HeyGen-Wasserzeichen.
- **Creator** · $24 / Mon. · 30 Min., kommerzielle Nutzung, kein Wasserzeichen.
- **Team** · $69 / Sitz/Mon. · 90 Min., Brand Kits, Team-Workspace.
- **Enterprise** · auf Anfrage · API, Custom Avatars, SOC 2.
- **API** · pay-as-you-go ab $0.30 / Min. (je Modell).""",
        'overview':"""**HeyGen** ist neben Synthesia der zweite Spitzenanbieter für Avatar-basierte KI-Videos. Beide Plattformen erreichen mittlerweile eine Realismus-Stufe, bei der Endkunden in vielen Anwendungen nicht mehr erkennen, dass kein echter Mensch vor der Kamera stand. Der Unterschied liegt im Schwerpunkt: HeyGen geht in Richtung Geschwindigkeit, Skalierbarkeit und Self-Service, Synthesia eher in Richtung Enterprise-Compliance und kuratierter Workflow.

Das spannendste neuere Feature ist der **Interactive Avatar**: Ein KI-Avatar führt im Live-Stream eine echte Konversation mit dem Publikum, übersetzt simultan zwischen mehreren Sprachen und reagiert auf Chat-Eingaben. Das eröffnet Anwendungsfelder vom Customer-Support bis zum mehrsprachigen Webinar.

Die Stock-Avatar-Bibliothek ist mit 700+ Personen die größte am Markt, und die Sprachen-Abdeckung (175+) ist beeindruckend. Eigene Avatare lassen sich aus drei Minuten Video-Aufnahme erstellen, höchste Qualität gibt es im Studio-Modus.

Schwächen: Die Top-Tarife werden bei mehr als 30 Minuten Output schnell teuer, und für streng regulierte deutsche Kunden ist die US-Datenresidenz im Default-Tarif ein Hindernis — Enterprise löst das, kostet aber entsprechend.""",
        'cue':'A simple human silhouette inside a thin rectangular frame, with a small magenta speech-glow at the mouth — a synthetic presenter, calm and clean.',
        'screenshot_url':'https://www.heygen.com/',
    },
    {
        'slug':'descript','name':'Descript','vendor':'Descript','category':'video-audio',
        'tagline':'Audio- und Videoschnitt im Text-Editor-Modus — schneiden = Tippen, KI macht den Rest.',
        'price':'Freemium — Hobbyist $24 / Mon.','api':False,'dsgvo':'bedingt','origin':'USA',
        'rating':4.5,'reviews':2480,
        'pros':['Text-basierter Audio-/Video-Edit','Overdub Voice Clone','Studio Sound (Noise Removal in einem Klick)','Multitrack mit Live-Transkription'],
        'cons':['Performance bei sehr langen Projekten','Voice-Clone-Tarife teuer','Kein offizieller API-Zugang'],
        'usecases':['Podcast-Produktion','Video-Schulungen','Interview-Edits','Social-Cuts aus Long-Form-Content'],
        'launched':'2017-12-01','lastUpdated':'2026-04-13',
        'website':'https://www.descript.com',
        'logo_domain':'descript.com',
        'features':"""- **Text-basiertes Editing** — Wörter im Transkript löschen ⇒ entsprechende Audio-/Video-Stelle wird entfernt.
- **Overdub** — Voice-Clone für Korrekturen ohne Neu-Aufnahme.
- **Studio Sound** — KI-Noise-Removal auf Studio-Niveau in Sekunden.
- **Eye Contact** — Blickrichtung in Kamera „korrigieren" für Talking-Heads.
- **Underlord** — KI-Editor-Agent, der ganze Episoden automatisch schneidet.
- **AI Speakers** — Skript zu Voice-Over in 80+ Sprachen.""",
        'pricing':"""- **Free** · 1 Stunde Transkription/Mon., Wasserzeichen, kein Voice Clone.
- **Hobbyist** · $24 / Mon. · 10 Std. Transkription, kein Wasserzeichen.
- **Creator** · $35 / Mon. · 30 Std., Multitrack, Studio Sound.
- **Business** · $60 / Mon. · 40 Std., Brand Templates, SSO.
- **Enterprise** · individuell · höchste Limits, API auf Anfrage.""",
        'overview':"""**Descript** hat die Audio- und Video-Bearbeitung in den letzten Jahren neu definiert: Statt mit Wellenformen und Timeline-Knipsern zu arbeiten, schneidet man im **Transkript** — ein gelöschtes Wort entfernt automatisch die entsprechende Audio-Sekunde. Wer einmal so produziert hat, kehrt selten zu Audacity oder Premiere zurück, wenn es um Sprache geht.

Die Magie steckt im KI-Backbone: **Overdub** klont die eigene Stimme und ermöglicht Korrekturen ohne erneutes Mikrofon-Setup. **Studio Sound** entfernt Hintergrundlärm, Hall und Echo in einem einzigen Klick und bringt das Audio auf ein Niveau, für das früher ein Recording-Studio nötig war. **Eye Contact** richtet den Blick eines Sprechers in die Kamera, selbst wenn er auf dem zweiten Monitor abgelesen hat.

Mit **Underlord** (2024 hinzugekommen) hat Descript einen agentischen KI-Editor eingeführt, der ganze Podcast-Episoden auf Wunsch automatisch schneidet — Versprecher raus, Werbeblöcke an die richtige Stelle, Kapitelmarken setzen.

Schwächen: Bei sehr großen Projekten (mehrstündige Multi-Track-Sessions) merkt man die App-Architektur. Voice-Clone und höhere Stunden-Limits sind in den teureren Tarifen hinter Paywalls. Eine offizielle API fehlt — wer Descripts Magie programmatisch nutzen möchte, ist auf Web-UI-Workflows angewiesen.""",
        'cue':'An abstract waveform morphing into typed text characters, the active cursor tinted magenta — text becoming sound.',
        'screenshot_url':'https://www.descript.com/',
    },
    {
        'slug':'replit','name':'Replit Agent','vendor':'Replit','category':'coding',
        'tagline':'Browser-IDE mit autonomem Agenten — App-Idee in Worten beschreiben, deployt zurückbekommen.',
        'price':'Freemium — Core $20 / Mon.','api':False,'dsgvo':'bedingt','origin':'USA',
        'rating':4.3,'reviews':1380,
        'pros':['Komplette Cloud-IDE im Browser','Integriertes Hosting + Datenbank','Replit Agent baut komplette Apps','Sehr niedrige Einstiegshürde'],
        'cons':['Bei großen Projekten weniger geeignet','Performance abhängig von Cloud-Tier','Vendor-Lock-in (eigenes Hosting)'],
        'usecases':['Prototyping','Lehre','Hackathons','MVP-Bau','No-Code-/Low-Code-Workflows'],
        'launched':'2016-01-01','lastUpdated':'2026-04-20',
        'website':'https://replit.com',
        'logo_domain':'replit.com',
        'features':"""- **Replit Agent** — beschreibt eine App in natürlicher Sprache, Replit baut + deployt sie.
- **Browser-IDE** mit Multi-Sprache-Support (Python, JS, TS, Go, Rust, …).
- **Replit Hosting** + Datenbank inklusive — von Idee zu Public-URL in Minuten.
- **Multiplayer-Editing** wie Google Docs für Code.
- **Templates & Community** mit Millionen Forks.
- **Mobile App** für unterwegs (iOS/Android).""",
        'pricing':"""- **Free** · 3 Public Repls, geteilte Compute-Quota.
- **Core** · $20 / Mon. · Private Repls, 25 Agent-Checkpoints, 50 Std. Compute.
- **Teams** · $40 / Sitz/Mon. · zentrale Verwaltung, Geheimnis-Management.
- **Enterprise** · auf Anfrage · SSO, SOC 2, dedizierte Compute-Pools.
- **Agent-Credits** · zusätzlich kaufbar (~$25 für 25 Checkpoints).""",
        'overview':"""**Replit** war ursprünglich eine browserbasierte IDE für Lehre und Prototyping — Schulen, Universitäten und Bootcamps nutzen die Plattform seit Jahren als Zero-Setup-Coding-Umgebung. Mit dem Launch des **Replit Agent** im Herbst 2024 hat sich die Positionierung dramatisch verändert: Heute beschreibt man eine App-Idee in einem Satz, der Agent baut Frontend, Backend, Datenbank-Schema und stellt das Ergebnis unter einer öffentlichen URL bereit.

Das macht Replit zum direktesten Kontrahenten von Lovable, v0 und ähnlichen „Idea-to-App"-Plattformen. Im Gegensatz zu reinen Generatoren bleibt aber alles im **vollwertigen Code** — Nutzer können jederzeit in den Editor wechseln und manuell weiterbauen, der Agent setzt nur den Startpunkt und übernimmt iterative Erweiterungen.

Replit eignet sich besonders für **Prototyping**, **MVP-Bau**, **Hackathons** und **Lehre**. Für Production-Anwendungen mit Compliance-Anforderungen oder hohem Traffic ist die eigene Infrastruktur des Unternehmens fast immer die bessere Wahl — Replit-Hosting hat klare Limits und schafft Vendor-Lock-in.

Limitierungen: Bei großen Codebases (ab ~10.000 Zeilen) merkt man die Browser-Architektur, sehr große Agent-Aufgaben verbrauchen viele Checkpoints (= Geld), und enterprise-typische Tools wie SSO oder Audit-Logs gibt es erst im Top-Tarif.""",
        'cue':'A small browser window outline with a thin curved arrow exiting to the right, a magenta dot at the arrow tip — code becoming live deploy.',
        'screenshot_url':'https://replit.com/',
    },
    {
        'slug':'zapier','name':'Zapier','vendor':'Zapier','category':'agenten',
        'tagline':'Marktführer der Workflow-Automation — jetzt mit AI Actions, AI Agents und Tables-Datenbank.',
        'price':'Freemium — Pro ab $19,99 / Mon.','api':True,'dsgvo':'ja','origin':'USA',
        'rating':4.4,'reviews':4120,
        'pros':['7.000+ App-Integrationen','AI Actions für jeden Schritt','Zapier Agents für autonome Workflows','EU-Datenresidenz auf Wunsch'],
        'cons':['Bei hohem Volumen schnell teuer','Komplexere Logik schwerer zu debuggen','Branding bisweilen US-zentrisch'],
        'usecases':['CRM-Sync','Marketing-Automation','AI-Pipelines','Internes Tooling ohne Code'],
        'launched':'2011-08-01','lastUpdated':'2026-04-19',
        'website':'https://zapier.com',
        'logo_domain':'zapier.com',
        'features':"""- **7.000+ Integrationen** — größtes Ökosystem unter den Workflow-Tools.
- **AI Actions** — OpenAI, Claude, Gemini & Co. als Schritt in jedem Zap.
- **Zapier Agents** — autonome Agenten, die Trigger interpretieren und Aktionen wählen.
- **Zapier Tables** — eigene Datenbank im Workflow.
- **Zapier Interfaces** — einfache Web-Frontends ohne Code.
- **EU-Datenresidenz** in Frankfurt für Enterprise-Tarife.""",
        'pricing':"""- **Free** · 100 Tasks/Monat, 5 Zaps, Single-Step-Limits.
- **Professional** · $19,99 / Mon. · 750 Tasks, Multi-Step, Premium Apps.
- **Team** · $69 / Mon. · 2.000 Tasks, geteilte Zaps, Folder.
- **Enterprise** · auf Anfrage · SSO, SAML, EU-Datenresidenz, Audit-Logs.
- **Agents** als Add-on mit eigenem Credit-Modell.""",
        'overview':"""**Zapier** ist das Synonym für Workflow-Automation — seit 2011 baut das Unternehmen die Brücke zwischen SaaS-Tools, die nicht miteinander reden wollen. Mit über 7.000 Integrationen ist das Ökosystem nicht nur das größte am Markt, sondern auch das tiefste: Selbst nischige B2B-Tools haben fast immer einen Zapier-Connector.

Mit **AI Actions** (2023) und **Zapier Agents** (2024) hat das Unternehmen die Plattform konsequent in Richtung KI weiterentwickelt. AI Actions erlauben es, in jedem Schritt eines Zaps ein Sprachmodell aufzurufen — etwa zur Klassifizierung eingehender E-Mails, zur Zusammenfassung von Lead-Daten oder zur Routing-Entscheidung. Zapier Agents gehen einen Schritt weiter: Sie interpretieren ein Trigger-Ereignis selbstständig und entscheiden, welche Aktionen aus dem App-Katalog die richtigen sind.

Die direkte Konkurrenz heißt **Make** (visuell-mächtig, günstig pro Operation) und **n8n** (open-source, self-hostable). Zapier punktet mit Reichweite und Polish, verliert aber bei sehr großem Volumen wegen seines Per-Task-Pricing-Modells.

Für deutsche Konzerne wichtig: Zapier bietet seit 2024 **EU-Datenresidenz in Frankfurt** als Enterprise-Option an, mit AVV nach DSGVO-Standard. Das schließt eine wichtige Compliance-Lücke, die zuvor viele Kunden zu n8n oder Make trieb.""",
        'cue':'Two small clouds connected by a thin lightning bolt, the bolt tinted magenta — connection across silos.',
        'screenshot_url':'https://zapier.com/',
    },
    {
        'slug':'otter','name':'Otter.ai','vendor':'Otter','category':'produktivitaet',
        'tagline':'Live-Transkription für Meetings — automatische Notizen, Action Items, Zusammenfassungen.',
        'price':'Freemium — Pro $16,99 / Mon.','api':True,'dsgvo':'bedingt','origin':'USA',
        'rating':4.4,'reviews':3290,
        'pros':['Live-Transkription in Zoom/Meet/Teams','Otter AI Chat — Fragen über die Meeting-Inhalte','Automatische Action Items','Sehr gute Sprecher-Identifikation'],
        'cons':['Nicht-englische Sprachen schwächer','Free-Tarif bewirbt sich aktiv selbst','US-Hosting Standard'],
        'usecases':['Meeting-Notizen','Sales-Calls','Interview-Transkripte','Lehre & Vorlesungen'],
        'launched':'2018-02-01','lastUpdated':'2026-04-11',
        'website':'https://otter.ai',
        'logo_domain':'otter.ai',
        'features':"""- **Live-Transkription** in Zoom, Google Meet, Microsoft Teams.
- **OtterPilot** — virtueller Teilnehmer, der für Sie ins Meeting geht.
- **Otter AI Chat** — Fragen zu vergangenen Meetings stellen.
- **Sprecher-Identifikation** — auch bei vielen Teilnehmern zuverlässig.
- **Auto Summary** mit Action Items und Entscheidungen.
- **Workspace** zum Teilen von Transkripten im Team.""",
        'pricing':"""- **Free** · 300 Minuten/Mon., max. 30 Min./Meeting, 3 Audio-Imports.
- **Pro** · $16,99 / Mon. · 1.200 Min./Mon., 90 Min./Meeting, 10 Imports.
- **Business** · $30 / Sitz/Mon. · 6.000 Min., 4 Std./Meeting, Admin-Tools.
- **Enterprise** · auf Anfrage · SSO, SCIM, erweitertes Sicherheitspaket.""",
        'overview':"""**Otter.ai** hat die Meeting-Transkription für Wissensarbeiter zum Mainstream gemacht. Was 2018 als smartes Diktiergerät startete, ist heute ein vollwertiger KI-Assistent, der für jeden virtuellen Termin automatisch teilnimmt, mitschreibt, zusammenfasst und Aufgaben extrahiert.

Der eigentliche Hebel ist **OtterPilot**: Statt manuell ein Recording zu starten, schickt man den OtterPilot als Calendar-Bot ins Meeting — er erscheint als zusätzlicher Teilnehmer, transkribiert live und liefert binnen Minuten nach Ende eine vollständige Zusammenfassung samt Action Items in den Posteingang. Für Sales-Teams, Customer Success und alle, die viele Calls führen, ist das transformativ.

Mit **Otter AI Chat** lassen sich gespeicherte Meetings nachträglich befragen: „Was hat der Kunde zum Pricing gesagt?" oder „Welche Open Items gab es zur Roadmap?" Antworten kommen mit Zeitstempel-Quellen aus dem Original-Audio.

Die Hauptkonkurrenz heißt **Granola** (lokaler, eleganter, ohne Bot-Teilnehmer) und **Fireflies** (vergleichbares Feature-Set, etwas günstiger). Otter punktet mit Reichweite — Integrationen in alle großen Meeting-Plattformen sind ausgereift, die Sprecher-Identifikation ist State-of-the-Art.

Limitierungen: Deutsch und andere nicht-englische Sprachen werden inzwischen unterstützt, sind aber qualitativ noch hinter Englisch. Das US-Hosting ist für streng regulierte Kunden ein Hindernis — Enterprise-Verträge können DPA und SCC-Klauseln einschließen.""",
        'cue':'A small abstract microphone with three short text-line segments rising from it, the topmost line tinted magenta — speech turned into structured note.',
        'screenshot_url':'https://otter.ai/',
    },
    {
        'slug':'hex','name':'Hex','vendor':'Hex','category':'daten-analyse',
        'tagline':'Kollaborative Daten-Notebooks mit AI-Copilot — SQL, Python und visuelle Apps in einem.',
        'price':'Freemium — Pro $24 / Sitz / Mon.','api':True,'dsgvo':'bedingt','origin':'USA',
        'rating':4.6,'reviews':610,
        'pros':['Notebook + Dashboard in einem Tool','Hex Magic AI für SQL/Python-Generierung','Granulare Berechtigungen','Native Snowflake/Databricks/BigQuery-Anbindung'],
        'cons':['Pro-Tarif relativ teuer','Kein Self-Hosting','Lernkurve für klassische Excel-Nutzer'],
        'usecases':['Ad-hoc-Analysen','Internal Apps','Data-Storytelling','Reporting für Stakeholder'],
        'launched':'2019-01-01','lastUpdated':'2026-04-08',
        'website':'https://hex.tech',
        'logo_domain':'hex.tech',
        'features':"""- **Hex Magic** — KI generiert SQL-Queries, Python-Cells und Visualisierungen aus natürlicher Sprache.
- **Notebook + App** — gleicher Code als Notebook arbeiten, als Web-App veröffentlichen.
- **Live-Kollaboration** wie Google Docs für Daten.
- **Native Connectors** zu Snowflake, BigQuery, Redshift, Databricks, Postgres.
- **Reactive Cells** — Änderungen propagieren automatisch downstream.
- **Granular Sharing** mit Row-Level-Permissions.""",
        'pricing':"""- **Community (Free)** · unbegrenzt persönliche Notebooks, Public-Sharing.
- **Pro** · $24 / Sitz / Mon. · Private Workspaces, App-Hosting.
- **Team** · $50 / Sitz / Mon. · Schedules, Reviews, Approvals.
- **Enterprise** · auf Anfrage · SSO, SAML, Customer-Managed Keys.
- **Hex Magic** AI-Credits inklusive ab Pro.""",
        'overview':"""**Hex** versucht die ewige Lücke zwischen Daten-Notebooks (Jupyter, Colab) und Business-Intelligence-Tools (Tableau, Looker) zu schließen. Das Resultat ist eine Plattform, in der Data Scientists ihre gewohnten SQL- und Python-Workflows behalten, das Endergebnis aber direkt als interaktive Web-App für Stakeholder bereitstellen können — ohne Übergabe an Frontend-Engineering.

Der KI-Layer **Hex Magic** ist mittlerweile einer der besten am Markt: Statt nur Code-Vervollständigung à la Copilot bekommt man Vorschläge auf Schema-Ebene („Welche Tabellen passen zu deiner Frage?"), generierte SQL-Queries, automatische Chart-Vorschläge und sogar Erklärungen zu Notebook-Outputs. Für Teams, die viele Ad-hoc-Analysen liefern, ist das ein erheblicher Produktivitäts-Hebel.

Die **Notebook-zu-App-Pipeline** ist das wichtigste Differenzierungsmerkmal: Statt einer Analyse als Bild oder PDF zu teilen, veröffentlicht man sie als interaktive App mit Filtern, Parametern und Berechtigungen. Stakeholder können selbst Werte ändern, ohne im Notebook-Code zu landen.

Konkurrenz: **Mode** (BI-näher, von Thoughtspot übernommen), **Deepnote** (eher Notebook-pur), **Streamlit** (mehr Engineering-Aufwand). Hex steht in der Mitte und punktet vor allem dort, wo SQL/Python und Stakeholder-Konsumption beide gebraucht werden.

Schwächen: Die Pro-Tarife sind pro Sitz teurer als Konkurrenten, Self-Hosting gibt es nicht, und für reine Excel-Heavy-User ist die Lernkurve spürbar.""",
        'cue':'A stylized hexagonal grid with three cells highlighted in line-art, one cell tinted magenta — modular analytics blocks.',
        'screenshot_url':'https://hex.tech/',
    },
    {
        'slug':'jasper','name':'Jasper','vendor':'Jasper','category':'marketing',
        'tagline':'KI-Marketingplattform für Brands — Brand Voice, Workflows, Content Repurposing.',
        'price':'Creator $39 / Mon., Pro $59','api':True,'dsgvo':'bedingt','origin':'USA',
        'rating':4.0,'reviews':2740,
        'pros':['Brand Voice & Style Guides','Marketing-spezifische Templates','Workflows für Kampagnen','API + Integrationen (HubSpot, Webflow, Surfer)'],
        'cons':['Kein klares Modell-USP gegenüber ChatGPT','Pricing höher als General-Purpose-Tools','Qualität schwankt zwischen Output-Typen'],
        'usecases':['Blog-Artikel','Werbeanzeigen','E-Mail-Kampagnen','Social-Posts','SEO-Briefings'],
        'launched':'2021-02-01','lastUpdated':'2026-04-02',
        'website':'https://www.jasper.ai',
        'logo_domain':'jasper.ai',
        'features':"""- **Brand Voice** — eigener Tone-of-Voice, in jedem Output durchgesetzt.
- **Style Guide** mit Wortlisten, Verbote, Lieblings-Phrasings.
- **Marketing Templates** für 50+ Use-Cases (Ads, Emails, SEO, Social).
- **Jasper Workflows** — mehrstufige Kampagnen-Pipelines.
- **Knowledge Base** — eigene Dokumente als Wissensquelle für Outputs.
- **Integrations** mit HubSpot, Salesforce, Webflow, Surfer SEO.""",
        'pricing':"""- **Creator** · $39 / Sitz / Mon. · 1 Brand Voice, 1 Knowledge Asset.
- **Pro** · $59 / Sitz / Mon. · 3 Brand Voices, 10 Knowledge Assets, Workflows.
- **Business** · auf Anfrage · unbegrenzt Brand Voices, SSO, API.
- **API** · pay-as-you-go ab $0.50 / 1.000 Wörter.
- **Annual** mit ~20 % Rabatt.""",
        'overview':"""**Jasper** war einer der ersten Anbieter, der GPT-3 für Marketing-Teams in eine produkttaugliche Form gebracht hat. Die Plattform startete 2021 als „Conversion.ai" und wuchs binnen eines Jahres auf hunderte Millionen Dollar Umsatz — ein Fall, der zeigt, wie groß die Lücke zwischen Roh-LLMs und produktiven Marketing-Workflows war.

Mittlerweile hat sich das Spielfeld verändert: ChatGPT, Claude und andere General-Purpose-Tools sind günstiger, oft besser, und können fast alles, was Jasper konnte. Der USP von Jasper ist heute **Brand Voice + Style Guide + Workflow-Automation in einem Tool** — wer für mehrere Marken konsistente Outputs in großem Volumen braucht, findet hier eine bessere Plattform als in „rohen" LLMs.

**Brand Voice** ist das wichtigste Feature: Eine Marke wird mit Beispieltexten, gewünschten Adjektiven, verbotenen Wörtern und stilistischen Vorgaben definiert; Jasper setzt diese Vorgaben in jedem Output zuverlässig durch. Für Agenturen, die für mehrere Kunden parallel arbeiten, ein erheblicher Produktivitäts-Vorteil.

**Workflows** orchestrieren mehrstufige Kampagnen — etwa „Briefing → Outline → Long-Form-Artikel → Social-Cuts → E-Mail-Promo" — als wiederholbare Pipelines.

Schwächen: Jasper kämpft seit dem Aufkommen freier ChatGPT-Funktionen mit der Daseinsberechtigung. Die Tarife sind teurer als die Konkurrenz, und für Solo-Nutzer ohne Brand-Konsistenz-Anspruch gibt es kaum Gründe, statt direkt mit Claude oder GPT zu arbeiten.""",
        'cue':'A stylized speech-bubble with a thin frame around it (the brand boundary), one corner tinted magenta — voice with structure.',
        'screenshot_url':'https://www.jasper.ai/',
    },
    {
        'slug':'consensus','name':'Consensus','vendor':'Consensus','category':'forschung',
        'tagline':'KI-Suche durch 200 Mio. Studien — Antworten direkt aus peer-reviewter Forschung.',
        'price':'Freemium — Premium $11,99 / Mon.','api':True,'dsgvo':'bedingt','origin':'USA',
        'rating':4.6,'reviews':820,
        'pros':['Antworten ausschließlich aus peer-reviewten Papern','Consensus Meter — wissenschaftlicher Konsens auf einen Blick','Studien-Snapshots mit Sample Size & Population','Über 200 Mio. Studien indexiert'],
        'cons':['Englische Forschung dominant','Pro-Modi für tiefe Reviews benötigt','Geistes-/Sozialwissenschaften schwächer abgedeckt'],
        'usecases':['Literaturrecherche','Evidence-Based Practice','Faktencheck','Studienvorbereitung'],
        'launched':'2022-08-01','lastUpdated':'2026-04-14',
        'website':'https://consensus.app',
        'logo_domain':'consensus.app',
        'features':"""- **200 Mio. Studien** aus Semantic Scholar indexiert.
- **Consensus Meter** — visualisiert wissenschaftlichen Konsens (Ja/Nein/Mixed).
- **Studien-Snapshots** mit Population, Sample Size, Methodik.
- **AI-generierte Top-Sätze** aus den relevantesten Papern.
- **Search Filters** (Studientyp, Jahr, Sample Size, Open Access).
- **API** für Integration in Wissensplattformen.""",
        'pricing':"""- **Free** · 20 AI-Searches/Mon., Basis-Filter.
- **Premium** · $11,99 / Mon. · unbegrenzte AI-Searches, alle Filter, Citation-Export.
- **Teams** · ab $9,99 / Sitz / Mon. (jährlich) — geteilte Bibliotheken.
- **Enterprise** · auf Anfrage — SSO, API, Single-Tenant-Optionen.
- **Studierenden-Rabatt** verfügbar.""",
        'overview':"""**Consensus** ist eine Antwort auf ein konkretes Problem: Sprachmodelle wie ChatGPT generieren auf wissenschaftliche Fragen häufig plausible, aber nicht immer korrekte Antworten — oft mit halluzinierten Studien-Verweisen. Consensus dreht das Modell um: Statt aus dem trainierten Wissen des LLMs zu antworten, durchsucht die Plattform den Index von **Semantic Scholar** (~200 Millionen wissenschaftlicher Paper) und konstruiert die Antwort aus den tatsächlichen Findings.

Das **Consensus Meter** ist das markanteste Feature: Bei strittigen Fragen visualisiert die Plattform, wie viele Studien sie bestätigen, ablehnen oder als gemischt einstufen — ein einfacher Indikator für den wissenschaftlichen Konsens, ohne dass man ein Dutzend Abstracts selbst lesen muss.

Pro Studie bekommt man einen **Snapshot** mit Stichprobengröße, untersuchter Population, Methodik und einem AI-generierten Kernsatz. Wer tiefer einsteigen möchte, klickt sich direkt zum Open-Access-PDF oder zum Verlag durch. **Citation Export** in BibTeX, EndNote und APA macht die Plattform für die akademische Praxis nutzbar.

Konkurrenz: **Elicit** (ähnlich, mehr Workflow-Tools für systematische Reviews), **Scite** (Schwerpunkt Citation-Sentiment), **Semantic Scholar** selbst (Index ohne KI-Layer). Consensus punktet mit der niedrigsten Einstiegshürde und dem klarsten UX für Nicht-Akademiker.

Schwächen: Englischsprachige biomedizinische und naturwissenschaftliche Forschung ist sehr gut abgedeckt — Geistes- und Sozialwissenschaften schwächer. Für tiefere systematische Reviews ist Elicit oft das geeignetere Tool.""",
        'cue':'A stylized scale balance with three small dots on each pan, one central dot tinted magenta — measuring consensus.',
        'screenshot_url':'https://consensus.app/',
    },
]

# -------------------- Connection --------------------
r = requests.post(f'{BASE}/auth/login',
    data={'grant_type':'password','username':ENV['EMAIL'],'password':ENV['PW']},
    headers={'Content-Type':'application/x-www-form-urlencoded'}, verify=False)
H = {'Authorization': f'Bearer {r.json()["access_token"]}'}
HJ = {**H, 'Content-Type':'application/json'}
print('✓ Logged in')

cts = requests.get(f'{BASE}/{SITE}/contenttypes/', headers=HJ, verify=False).json()
tool_ct = next(c for c in cts if c.get('display_identifier') == 'tool')

# Existing slugs
items, page = [], 1
while True:
    r = requests.get(f'{BASE}/{SITE}/elements/?type_id={tool_ct["id"]}&size=200&page={page}',
        headers=HJ, verify=False).json()
    items += r.get('items', [])
    if not r.get('has_next'): break
    page += 1
existing = {el['data'].get('slug'): el for el in items}
print(f'  · {len(existing)} tools already in CMS')

def fetch_logo(domain: str, size: int = 256) -> bytes:
    url = f'https://www.google.com/s2/favicons?domain={domain}&sz={size}'
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    return r.content

# -------------------- Per-tool pipeline --------------------
created = patched = 0
for tool in TOOLS:
    slug = tool['slug']
    print(f'\n→ {slug}')

    # 1. element
    if slug in existing:
        print(f'  · element exists, will patch')
        el_id = existing[slug]['id']
        existing_data = existing[slug]['data']
    else:
        base_data = {k: tool[k] for k in (
            'slug','name','vendor','category','tagline','price','api','dsgvo','origin',
            'rating','reviews','pros','cons','usecases','launched','lastUpdated'
        )}
        r = requests.post(f'{BASE}/{SITE}/elements/',
            json={'type_id': tool_ct['id'], 'data': base_data, 'published': True},
            headers=HJ, verify=False)
        if not r.ok:
            print(f'  ✗ create failed: {r.status_code} {r.text[:200]}')
            continue
        el_id = r.json()['id']
        existing_data = base_data
        created += 1
        print(f'  ✓ element created (id={el_id})')

    # 2. overview Post + post_id (if needed)
    if not existing_data.get('post_id'):
        post_payload = {
            'title': f'{tool["name"]} — Übersicht',
            'content': tool['overview'],
            'short_description': tool['tagline'],
            'keywords': [tool['vendor'], tool['category']],
            'published': True,
            'locale': 'de',
        }
        r = requests.post(f'{BASE}/{SITE}/posts/', json=post_payload, headers=HJ, verify=False)
        if r.ok:
            pid = r.json()['id']
            existing_data['post_id'] = pid
            print(f'  ✓ overview Post #{pid}')
        else:
            print(f'  ✗ post create failed: {r.status_code} {r.text[:200]}')

    # 3. logo upload (if needed)
    if not existing_data.get('logo_id'):
        try:
            png = fetch_logo(tool['logo_domain'])
            local = LOGOS_DIR / f'{slug}.png'
            local.write_bytes(png)
            with open(local, 'rb') as fh:
                files = {'file': (f'{slug}-logo.png', fh, 'image/png')}
                data = {
                    'name': f'{tool["name"]} – Logo',
                    'alt_text': f'Logo von {tool["name"]}',
                    'description': f'Offizielles Logo von {tool["name"]} ({tool["logo_domain"]}).',
                }
                r = requests.post(f'{BASE}/{SITE}/media/',
                    files=files, data=data, headers=H, verify=False, timeout=120)
            if r.ok:
                lid = r.json().get('id')
                existing_data['logo_id'] = lid
                print(f'  ✓ logo #{lid}')
        except Exception as e:
            print(f'  ✗ logo: {e}')

    # 4. fields (website, features, pricing) — always set
    existing_data['website'] = tool['website']
    existing_data['features'] = tool['features']
    existing_data['pricing'] = tool['pricing']

    # 5. patch element
    r = requests.patch(f'{BASE}/{SITE}/elements/{el_id}',
        json={'data': existing_data}, headers=HJ, verify=False)
    if r.ok:
        patched += 1
        print(f'  ✓ patched (logo+post+website+features+pricing)')
    else:
        print(f'  ✗ patch failed: {r.status_code} {r.text[:200]}')

print(f'\n✓ Done — created {created}, patched {patched}')
print('\nNext steps:')
print('  1. Add to scripts/capture_tool_screenshots.mjs:')
for tool in TOOLS:
    print(f"     {{ slug: '{tool['slug']}', url: '{tool['screenshot_url']}' }},")
print('  2. Run: cd web && node ../scripts/capture_tool_screenshots.mjs (after copying it into web/)')
print('  3. Run: python3 scripts/upload_screenshots.py')
print('  4. Add to scripts/generate_tool_images.py TOOL_CUES:')
for tool in TOOLS:
    print(f"     '{tool['slug']}': '{tool['cue']}',")
print('  5. Run: python3 scripts/generate_tool_images.py')
