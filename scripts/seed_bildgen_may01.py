#!/usr/bin/env python3
"""Seed 7 additional image-generation tools end-to-end (May 2026 batch)."""
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
    {'slug':'playground','name':'Playground','vendor':'Playground AI','category':'bildgenerierung',
     'tagline':'Browser-Studio mit FLUX, Stable Diffusion und einem aufgeräumten Layered-Editor — Pixar-bis-Photoreal in einer Oberfläche, ohne lokale Installation.',
     'price':'Free 50 Bilder/Tag · Pro ab $15 / Mon.','api':True,'dsgvo':'bedingt','origin':'USA',
     'rating':4.5,'reviews':6420,
     'pros':['FLUX, SDXL und eigene Modelle in einem UI','Layered-Editor für Komposition','Sehr großzügiger Free-Tarif','Klares, einfach zu bedienendes Studio'],
     'cons':['Geschwindigkeit bei FLUX teils zäh','Kein eigenes Frontier-Modell mehr','Keine EU-Datenresidenz','Eigene Mixer- und Style-Modelle dezent zurückgefahren'],
     'usecases':['Marketing-Visuals','Mood-Boards','Social-Media-Posts','Konzept-Art'],
     'launched':'2022-12-05','lastUpdated':'2026-05-01',
     'website':'https://playground.com/','domain':'playground.com',
     'features':"""- **Modell-Auswahl** zwischen FLUX 1.1, SDXL, Stable Diffusion 3 und legacy Playground-Modellen.
- **Layered Editor** mit Inpainting, Outpainting und Masken-Stack.
- **Filter und Style-Modes** für schnelle Look-Anpassung.
- **Mixer-Tool** für Style-Transfer zwischen Bildern.
- **Canvas-Mode** für freihändiges Composing größerer Werke.
- **API-Endpunkt** mit denselben Modellen wie im Web-Studio.
- **Community-Feed** mit Remix-Funktion.""",
     'pricing':"""- **Free** · 50 Bilder / Tag, alle Modelle, kommerzielle Nutzung erlaubt.
- **Pro** · $15 / Mon. — 1.000 Bilder / Tag, schnelle Queues, erweiterte Editoren.
- **Pro Plus** · $45 / Mon. — 4.000 Bilder / Tag, Priority-Inferenz.
- **API** · Pay-per-Image ab $0,001 (SDXL) bis $0,02 (FLUX 1.1 Pro).
- **Enterprise** · auf Anfrage — White-Label, höhere Rate-Limits.""",
     'overview':"""**Playground** ist seit Ende 2022 eines der populärsten Web-Studios für SD-basierte Bildgenerierung — und hat sich nach mehreren Strategieschwenks 2024/25 als **Aggregator und Editor-Plattform** für Open-Weight-Modelle etabliert. Statt eines eigenen Frontier-Modells bietet das Tool eine einheitliche Oberfläche für FLUX 1.1, SDXL, Stable Diffusion 3 und legacy Playground-Modelle.

Der **Layered Editor** ist das Differenzierungsmerkmal: Inpainting, Outpainting und Masken-Stack lassen sich miteinander kombinieren — ähnlich wie in Photoshop, aber mit AI-Generierung pro Layer. Wer komplexe Komposit-Werke baut, hat hier einen klaren Workflow-Vorteil gegenüber reinen „Prompt-zu-Bild"-Tools.

Der **Free-Tarif** ist ungewöhnlich großzügig: 50 Bilder pro Tag, alle Modelle, kommerzielle Nutzung erlaubt. Für Hobbyisten und kleine Projekte ist Playground damit oft der erste Anlaufpunkt, bevor ein Pro-Abo nötig wird.

Der **Mixer-Tool** transferiert Stil von Bild A auf Bild B — funktioniert besonders gut für Brand-Consistency und Style-Frames in Werbe-Workflows. Der **Canvas-Mode** erlaubt freihändiges Composing über größere Flächen, was klassische 1024×1024-Generatoren nicht können.

Die **API** spiegelt das Web-Studio mit denselben Modellen — pragmatisch für Teams, die im UI prototypen und dann in Produktion gehen wollen.

Schwächen: Die **Geschwindigkeit** mit FLUX ist teils zäh — wer viel iteriert, wartet spürbar. Die ehemals bekannten Playground-eigenen Mixer- und Style-Modelle wurden 2025 dezent zurückgefahren — die Plattform ist heute primär ein FLUX/SD-Hub. **Keine EU-Datenresidenz** bei aktuell stark US-zentriertem Hosting.

Empfohlen für Designer:innen, Marketers und Konzept-Künstler:innen, die einen sauberen Layered-Workflow mit Open-Weight-Modellen brauchen — und für jeden, der kostenlosen Zugang zu FLUX und SDXL ohne Lokalinstallation sucht."""},

    {'slug':'lexica','name':'Lexica','vendor':'Lexica','category':'bildgenerierung',
     'tagline':'Stable-Diffusion-basierter Generator mit der wahrscheinlich besten Prompt-Suchmaschine — Millionen kuratierte Prompts plus saubere Generation in einem Tool.',
     'price':'Starter $10 / Mon. · Pro $35 / Mon.','api':True,'dsgvo':'bedingt','origin':'USA',
     'rating':4.4,'reviews':5180,
     'pros':['Riesige öffentliche Prompt-Bibliothek','Sehr klare, fokussierte Oberfläche','API-Zugang in allen Tarifen','Reverse-Image-Search für ähnliche Prompts'],
     'cons':['Eigenes Modell hinter FLUX und Nano Banana','Kein Free-Tarif mit Bildgenerierung','Tools wie Inpainting weniger ausgereift','EU-Hosting nicht angeboten'],
     'usecases':['Prompt-Recherche','Mood-Board-Generierung','Style-Exploration','Kommerzielle Visuals'],
     'launched':'2022-09-25','lastUpdated':'2026-05-01',
     'website':'https://lexica.art/','domain':'lexica.art',
     'features':"""- **Prompt-Search** über Millionen öffentlich generierte Bilder mit Prompt-Volltext-Suche.
- **Reverse-Image-Search**: ähnliche Prompts und Bilder zu einem Upload finden.
- **Lexica Aperture** als hauseigenes SD-basiertes Modell.
- **API mit identischen Modellen** wie im Web.
- **High-Resolution-Output** bis 2.048 px.
- **Aspect-Ratio-Vorgaben** für Social-Media, Print und Hero-Images.
- **Outpainting und Variations** für Iteration.""",
     'pricing':"""- **Free** · nur Browse + Search, keine Bildgenerierung.
- **Starter** · $10 / Mon. — 1.000 Bilder, kommerzielle Nutzung, API-Zugang.
- **Pro** · $35 / Mon. — 7.000 Bilder, Priority-Generierung.
- **Max** · $90 / Mon. — 30.000 Bilder, höchste Concurrency.
- **API**: enthalten in allen Tarifen, Pay-as-you-go für Überschreitungen.""",
     'overview':"""**Lexica** wurde 2022 als reine Prompt-Suchmaschine für Stable-Diffusion-Bilder bekannt — und entwickelte sich danach zu einem vollwertigen Generator mit eigenem **Lexica Aperture**-Modell. Der USP bleibt aber dieselbe Stärke: die wahrscheinlich beste **Prompt-Datenbank** im Markt.

Die **Prompt-Search** indexiert Millionen öffentlich generierte Bilder mit ihren Prompts — wer nach „cinematic studio portrait, soft window light, analog film grain" sucht, bekommt sofort Beispiele plus die exakten Prompts dazu, die zu diesen Looks geführt haben. Für Prompt-Engineering und Style-Recherche ist das ein massiv beschleunigender Workflow.

Die **Reverse-Image-Search** geht noch einen Schritt weiter: Ein Foto-Upload findet ähnliche generierte Bilder samt Prompts — perfekt, um existierende Looks zu rekonstruieren oder als Referenz für eigene Projekte zu nutzen.

**Lexica Aperture** ist ein SD-basiertes Modell, das in den meisten Vergleichen hinter FLUX und Nano Banana liegt — aber für Standard-Generierung schnell und stabil ist. Wer absolute Spitzenqualität braucht, greift zu Cloud-Modellen anderer Anbieter; wer eine integrierte Prompt-Such-und-Generations-Pipeline will, ist hier richtig.

Die **Oberfläche** ist auffallend klar: Suchleiste oben, Bilder-Grid darunter, Prompt-Editor rechts. Keine 17 Sub-Menüs, kein Onboarding-Wizard. Das macht Lexica besonders attraktiv für Teams, die schnell Mood-Boards bauen.

Die **API** ist in allen Tarifen enthalten und bietet dieselben Modelle wie das Web-Studio — pragmatisch für Anwendungen, die SD-basierte Generierung mit Prompt-Search kombinieren wollen.

Schwächen: Das **eigene Modell** ist nicht mehr Frontier — Konkurrenten holen schneller auf als Lexica releast. **Inpainting und Outpainting** sind funktional, aber weniger ausgereift als bei spezialisierten Editoren. **Kein Free-Tarif** für Bildgenerierung — wer einsteigt, zahlt ab Tag 1.

Empfohlen für alle, die regelmäßig Prompts recherchieren oder iterieren — und für Teams, die Mood-Boards in Serie bauen, wo Geschwindigkeit und Variation wichtiger sind als absolute Top-Qualität."""},

    {'slug':'whisk','name':'Google Whisk','vendor':'Google','category':'bildgenerierung',
     'tagline':'Googles Experimental-Tool für visuelles Remixen — Bilder werden zu „Subjekt + Szene + Stil" und zu neuen Bildern kombiniert, powered by Imagen 3 + Gemini.',
     'price':'Free in Public Preview','api':False,'dsgvo':'bedingt','origin':'USA',
     'rating':4.3,'reviews':2890,
     'pros':['Bilder statt Text als Input — schneller Einstieg','Subjekt-/Szene-/Stil-Trennung sehr nützlich','Hohe Imagen-3-Qualität','Komplett kostenlos in Public Preview'],
     'cons':['Public Preview, Limits können sich ändern','Nur Englisch-UI','Kein API-Zugang','Datenresidenz USA'],
     'usecases':['Visuelle Brainstorming-Sessions','Mood-Board-Iteration','Style-Studien','Schnelles Concept-Art'],
     'launched':'2024-12-16','lastUpdated':'2026-05-01',
     'website':'https://labs.google/fx/tools/whisk','domain':'labs.google',
     'features':"""- **Subject-Image-Input** für die Hauptfigur des Bildes.
- **Scene-Image-Input** für Hintergrund und Setting.
- **Style-Image-Input** für visuellen Look und Atmosphäre.
- **Auto-Prompt** schreibt Gemini-generierten Prompt aus den Bildern.
- **Iteratives Remix** mit Variations-Galerie pro Edit.
- **Direkte Gallery-Integration** in Google Labs.
- **Imagen-3-Backbone** für die finale Bildgenerierung.""",
     'pricing':"""- **Free** · komplett kostenlos in Public Preview, mit fairen Tageslimits.
- **Limits**: typisch 50–100 Generierungen / Tag, schwankend je nach Nachfrage.
- **Bezahlmodell** noch nicht angekündigt — Roadmap deutet auf Workspace-Bundle.
- **Watermark**: SynthID-2.0 ist aktiv, kein sichtbares Logo.
- **Enterprise**-Pricing wird voraussichtlich über Vertex AI laufen.""",
     'overview':"""**Google Whisk** ist seit Dezember 2024 das wahrscheinlich originellste Bildgenerierungs-Experiment aus den Google Labs. Statt eines Text-Prompts werden **drei Bilder** als Input genutzt: ein Subjekt-Bild, ein Szene-Bild und ein Stil-Bild. Gemini schreibt im Hintergrund einen passenden Prompt, Imagen 3 generiert das Endbild. Das Ergebnis: Eine Form von visuellem Brainstorming, die mit reinen Text-Tools nur schwer zu erreichen ist.

Der **Workflow** ist erfrischend anders. Statt zu beschreiben, was man will, lädt man Beispiele hoch — eine Postkarte, ein Foto, ein Gemälde. Whisk extrahiert daraus die jeweils relevante Information (Form, Setting, Look) und kombiniert sie. Das macht das Tool besonders stark für **Designer:innen ohne Prompt-Erfahrung** und für die schnelle Exploration im Konzept-Stadium.

Das **Auto-Prompt-Feature** ist transparent: Gemini zeigt den generierten Prompt an, lässt sich editieren und neu generieren. Wer Prompt-Engineering lernen will, sieht hier in Echtzeit, wie professionelle Bildbeschreibungen formuliert werden.

Die **Bildqualität** liegt auf Imagen-3-Niveau — solide, aber nicht ganz auf Nano-Banana-Pro-2-Niveau. Für Konzept-Arbeit reicht das in 90% der Fälle; für finale Production-Bilder muss meist nachbearbeitet werden.

Die **Iterative Remix-Variation** erzeugt pro Edit eine kleine Galerie — gut, um schnell Alternativen zu vergleichen, ohne jede Variation einzeln zu prompten.

Schwächen: Whisk bleibt **Public Preview** — Limits ändern sich, Features kommen und gehen. **Nur Englisch-UI**, deutsche Beschreibungen werden teils nicht ideal verstanden. **Kein API-Zugang** macht das Tool nur für Web-Workflows brauchbar. **Datenresidenz USA**, was für DSGVO-sensible Workflows ein Ausschlusskriterium ist.

Empfohlen für Designer:innen und Konzept-Künstler:innen, die visuelle Brainstorming-Sessions führen — und für jeden, der mit Bildern statt Text-Beschreibungen arbeiten will, weil das schneller und direkter ist."""},

    {'slug':'higgsfield','name':'Higgsfield','vendor':'Higgsfield AI','category':'bildgenerierung',
     'tagline':'Cinematic-First-Bildgenerator mit über 80 Kamerabewegungs- und Style-Effekten — von Bullet-Time bis Tilt-Shift in einem Klick auf jedes Foto anwendbar.',
     'price':'Free 25 Credits/Tag · Pro $9 / Mon.','api':False,'dsgvo':'bedingt','origin':'USA',
     'rating':4.6,'reviews':4140,
     'pros':['80+ Cinematic-Effekte als Presets','Image-to-Video direkt aus dem Studio','Sehr starke Charakter-Konsistenz','Aktive Community und ständige neue Effekte'],
     'cons':['Effekt-Bibliothek eher westlich-cinematic','Kein API-Zugang','Hohe Credit-Kosten für längere Videos','Datenresidenz USA'],
     'usecases':['Social-Media-Reels','Music-Videos','Werbe-Mockups','Storyboard-Animation'],
     'launched':'2024-04-30','lastUpdated':'2026-05-01',
     'website':'https://higgsfield.ai/','domain':'higgsfield.ai',
     'features':"""- **80+ Cinematic-Presets**: Bullet-Time, Tilt-Shift, Anime-Sketch, Vintage-Film, Film-Noir und mehr.
- **Image-to-Image** mit Style-Vererbung über mehrere Frames.
- **Image-to-Video** für Motion-Effekte aus Standbildern.
- **Charakter-Konsistenz** über mehrere Generierungen.
- **Storyboard-Mode** für sequenzielle Frames.
- **Community-Effekte**, ständig erweitert via User-Submission.
- **Bulk-Edit-Mode** für Batch-Anwendungen auf mehrere Bilder.""",
     'pricing':"""- **Free** · 25 Credits / Tag, basisnahe Effekte, Watermark.
- **Pro** · $9 / Mon. — 200 Credits / Mon., alle Effekte, kein Watermark.
- **Creator** · $29 / Mon. — 800 Credits / Mon., HD-Output.
- **Studio** · $79 / Mon. — 3.000 Credits / Mon., 4K-Output, Priority.
- **Credits**: 1 Bild = 1 Credit, 1 Sek. Video = ca. 3–5 Credits.
- **Enterprise** · auf Anfrage — Bulk-Pricing, Custom-Modelle.""",
     'overview':"""**Higgsfield** wurde 2024 als spezialisierter Cinematic-Generator gestartet und hat sich seitdem zu einem der **viralsten Bildgenerierungs-Tools** entwickelt — fast jeder kennt die „Bullet-Time"-Selfies, die seit 2025 die Social-Media-Feeds füllen, viele davon entstehen hier.

Der **USP** ist die kuratierte Bibliothek von über 80 Cinematic-Presets — Kamerabewegungen, Filmlooks, Genre-Stile. Wer ein Foto hochlädt, wählt einen Effekt und bekommt das Bild im neuen Look zurück. Komplexes Prompting ist nicht nötig: Der Effekt ist das Modell.

Die **Charakter-Konsistenz** ist überraschend stark: Eine Person in 20 verschiedenen Cinematic-Effekten bleibt erkennbar dieselbe. Für Personal-Brand-Inhalte, Profilbilder und Look-Books in Serie ein klarer Vorteil gegenüber generischen Generatoren.

Die **Image-to-Video**-Funktion macht aus einem Standbild ein 2–8 Sekunden langes Video mit der gewählten Kamerabewegung — Bullet-Time wird wirklich zu einer Kamerafahrt. Für Social-Reels und Werbe-Mockups ein massiver Zeitgewinn.

Der **Storyboard-Mode** generiert sequenzielle Frames, die als zusammenhängende Szene wirken — gut für Music-Videos und schnelle Werbe-Storyboards.

Die **Community** ist aktiv und erweitert die Effekt-Bibliothek wöchentlich. Wer einen spezifischen Look kennt, findet ihn meist als bereits existierendes Preset.

Schwächen: Die **Effekt-Bibliothek** ist stark westlich-cinematic geprägt — japanische Anime-Looks, koreanische K-Drama-Stile sind weniger ausgebaut. **Kein API-Zugang**, was Higgsfield als reines Web-Tool positioniert. **Credit-Kosten** für längere Videos addieren sich schnell — wer monatlich viel Video-Output braucht, landet im Studio-Tarif.

Empfohlen für Content-Creators, Marketers und Social-Media-Teams, die schnell virale Cinematic-Looks brauchen — und für jeden, der Selfies oder Personenbilder in stilisierten Cinematic-Versionen produzieren will, ohne komplexes Editing-Setup."""},

    {'slug':'civitai','name':'Civitai','vendor':'Civitai','category':'bildgenerierung',
     'tagline':'Größte Community-Plattform für Stable-Diffusion-Modelle, LoRAs und Checkpoints — Browse, Download, Generate in einem Hub mit 4 Millionen+ Nutzern.',
     'price':'Free unbegrenzt · Supporter ab $10 / Mon.','api':True,'dsgvo':'bedingt','origin':'USA',
     'rating':4.5,'reviews':18920,
     'pros':['Unschlagbare Modell-Auswahl: 100.000+ Checkpoints und LoRAs','On-Site-Generierung mit jedem Modell','Aktive Community mit täglich neuen Modellen','API für externe Anwendungen'],
     'cons':['Inhalts-Diversität enthält viel NSFW (lässt sich filtern)','Inhalts-Filter erfordern Account-Setup','Nicht alle Community-Modelle gut dokumentiert','Geschwindigkeit der Free-Generierung schwankend'],
     'usecases':['SD-Modell-Browsing','LoRA-Auswahl','Style-Exploration','Community-Sharing'],
     'launched':'2022-11-20','lastUpdated':'2026-05-01',
     'website':'https://civitai.com/','domain':'civitai.com',
     'features':"""- **100.000+ Checkpoints und LoRAs** in einer durchsuchbaren Bibliothek.
- **On-Site-Generierung** mit dem Buzz-Credit-System.
- **Model-Pages** mit Beispielen, Triggers und Prompt-Hints.
- **Image-Feed** mit Filter nach Modell, Style, Aspect-Ratio.
- **Bounties und Contests** für Community-Modelle.
- **Training-Service** für eigene LoRAs (Cloud-GPU).
- **API** für Generierung von außerhalb.""",
     'pricing':"""- **Free** · unbegrenzte Generierung mit täglichem Buzz-Reset, Standard-Queue.
- **Bronze** · $10 / Mon. — Buzz-Bonus, Priority-Queue, Profil-Badge.
- **Silver** · $25 / Mon. — größerer Buzz-Bonus, Early-Access zu Features.
- **Gold** · $50 / Mon. — höchster Buzz-Bonus, exklusive Modelle.
- **API**: Pay-as-you-go über Buzz-Credits.
- **Training**: 4–12 Buzz pro LoRA-Trainings-Step.""",
     'overview':"""**Civitai** ist die mit Abstand größte Community-Plattform für Stable-Diffusion-basierte Modelle, LoRAs und Checkpoints — gestartet Ende 2022, heute mit über 4 Millionen registrierten Nutzern und mehr als 100.000 verfügbaren Modellen das **De-facto-Repository** für die Open-Source-Bildgenerierung.

Wer mit SD oder FLUX produziert, kommt um Civitai praktisch nicht herum. Hier finden sich nicht nur die offiziellen Modelle (SDXL, SD3, FLUX 1.1), sondern auch tausende fine-tuned Varianten — für anime-style Portraits, photorealistische Personen, spezifische Marken-Looks, historische Filmästhetik. Die Bandbreite an verfügbaren **LoRAs** (kleine Trainings-Aufsätze für spezifische Konzepte) ist im offenen Web nicht zu schlagen.

Die **On-Site-Generierung** ist seit 2024 möglich: Statt Modelle herunterzuladen und lokal zu betreiben, kann jedes Modell direkt im Browser verwendet werden — bezahlt über das **Buzz**-Credit-System, das in Free-Tarifen täglich nachgefüllt wird. Für Hobbyisten oft ausreichend, ohne Pro-Abo.

Die **Model-Pages** sind editorisch wertvoll: Trainingsdaten, empfohlene Triggers, Beispiel-Prompts, Sampler-Empfehlungen — alles dokumentiert. Für Prompt-Engineers und Workflow-Bauer:innen ein wichtiger Lernort.

Der **Training-Service** ermöglicht eigene LoRAs ohne lokale GPU — Hochladen von 10–30 Beispielbildern, ein paar Klicks, fertig in 1–3 Stunden. Für Brand-LoRAs oder Personen-LoRAs ein erschwinglicher Workflow.

Die **API** ist für Power-User attraktiv — alle Civitai-Modelle in eigenen Anwendungen verwendbar, Pay-as-you-go über Buzz.

Schwächen: Civitai hat einen **größeren NSFW-Anteil** als andere Plattformen — die Filter funktionieren, müssen aber im Account-Setup aktiviert werden. **Nicht alle Community-Modelle** sind gleich gut dokumentiert; bei manchen muss man durch Beispielbilder navigieren, um die Triggers zu verstehen.

Empfohlen für jeden, der mit SD oder FLUX ernsthaft arbeitet — als unverzichtbare Modell-Bibliothek, als Inspirations-Quelle und als Plattform für eigene Trainings."""},

    {'slug':'openart','name':'OpenArt','vendor':'OpenArt AI','category':'bildgenerierung',
     'tagline':'Multi-Modell-Studio mit eigenem Charakter-Konsistenz-System — eigene Charaktere trainieren und in beliebiger Story konsistent reproduzieren.',
     'price':'Free 50 Credits/Mon. · Pro ab $14 / Mon.','api':True,'dsgvo':'bedingt','origin':'USA',
     'rating':4.4,'reviews':3470,
     'pros':['Marktführend bei Charakter-Konsistenz','Großer Modell-Mix unter einem Dach','Storyboard-Modus für sequenzielle Bilder','API für externe Workflows'],
     'cons':['Charakter-Training kostet Credits','Editor unter Konkurrenten-Niveau','Pro-Tarif notwendig für regelmäßige Nutzung','Datenresidenz USA'],
     'usecases':['Charakter-Design','Story-Illustration','Game-Character-Konzepte','Comic-Generierung'],
     'launched':'2022-08-08','lastUpdated':'2026-05-01',
     'website':'https://openart.ai/','domain':'openart.ai',
     'features':"""- **Character-Training**: 4–10 Bilder einer Person/Figur → konsistente Reproduktion.
- **Modell-Auswahl**: FLUX, SDXL, Nano Banana, GPT Image, eigene Custom-Modelle.
- **Storyboard-Modus** für mehrere Frames mit derselben Hauptfigur.
- **Style-Transfer** zwischen Bildern.
- **Prompt-Library** mit kategorisierten Vorlagen.
- **API** für Charakter-konsistente Generierung in eigenen Apps.
- **Video-Mode** als Beta — Image-to-Video mit Charakter-Persistenz.""",
     'pricing':"""- **Free** · 50 Credits / Mon., Standard-Queue, kein Charakter-Training.
- **Hobby** · $14 / Mon. — 5.000 Credits, Charakter-Training, Standard-Modelle.
- **Pro** · $28 / Mon. — 14.000 Credits, alle Modelle, Priority-Queue.
- **Studio** · $56 / Mon. — 38.000 Credits, höchste Concurrency, Beta-Features.
- **API**: Pay-as-you-go ab $0,002 / Generierung.
- **Charakter-Training** kostet 1.000–3.000 Credits einmalig.""",
     'overview':"""**OpenArt** ist seit 2022 als Modell-Aggregator und Bildgenerierungs-Studio aktiv — und hat sich 2024/25 mit einem starken **Charakter-Konsistenz-System** als Spezialist für **Story-Illustration und Comic-Generierung** positioniert.

Der **Charakter-Training**-Workflow ist die zentrale Stärke: 4–10 Bilder einer Person, Figur oder Charakter-Studie hochladen, OpenArt trainiert daraus einen Charakter-Token, der in beliebigen neuen Generierungen konsistent reproduziert wird — auch über verschiedene Modelle (FLUX, SDXL, Nano Banana) hinweg. Für Comic-Künstler:innen, Game-Designer:innen und Personal-Branding-Workflows ein massiv beschleunigender Workflow gegenüber generischen Bildgeneratoren.

Der **Modell-Mix** ist breit: Neben den offenen FLUX/SDXL-Modellen sind auch **proprietäre Cloud-Modelle** wie Nano Banana und GPT Image über OpenArt verfügbar — bezahlt über das einheitliche Credit-System. Wer Modelle vergleichen will, ohne mehrere Abos zu führen, hat hier einen pragmatischen Hub.

Der **Storyboard-Modus** ist eine logische Erweiterung der Charakter-Konsistenz: Sequenzielle Frames mit derselben Hauptfigur in unterschiedlichen Szenen werden in einem zusammenhängenden Workflow generiert. Für Storyboarding und narrative Visualisierung ein klarer Vorteil gegenüber Tools, die nur Einzelbilder können.

Die **API** spiegelt das Web-Studio — wer eigene Anwendungen mit Charakter-Konsistenz baut (Avatar-Generatoren, Comic-Apps, Game-NPCs), hat hier einen direkten Weg.

Der **Video-Mode** als Beta erweitert die Charakter-Konsistenz auf bewegte Bilder — der Charakter bleibt in einem 4-Sekunden-Clip erkennbar identisch. Noch nicht auf Nano-Banana-Pro-2-Niveau, aber funktional für Mockups.

Schwächen: Das **Charakter-Training** ist nicht im Free-Tarif verfügbar und kostet Credits — schnelle Einmal-Tests sind im Pro-Abo billiger. Der **interne Editor** (Inpainting, Outpainting) liegt unter dem Niveau von Photoshop oder Magnific.

Empfohlen für Comic-Künstler:innen, Game-Designer:innen und Personal-Branding-Teams, die wiederkehrende Charaktere in vielen Bildern brauchen — und für jeden, der einen Modell-Aggregator mit Storytelling-Fokus sucht."""},

    {'slug':'luma-photon','name':'Luma Photon','vendor':'Luma Labs','category':'bildgenerierung',
     'tagline':'Lumas eigenes Bildmodell — schnell, fotoreal, mit perfektem Plug-In in den Dream-Machine-Video-Workflow für die Image-to-Video-Pipeline.',
     'price':'Free 30 Credits/Mon. · Standard ab $10 / Mon.','api':True,'dsgvo':'bedingt','origin':'USA',
     'rating':4.5,'reviews':3120,
     'pros':['Sehr schnelle Inferenz (1–2 Sek)','Direkter Dream-Machine-Video-Übergang','Photorealismus auf Nano-Banana-Niveau','API mit demselben Modell wie Web-UI'],
     'cons':['Style-Diversität geringer als FLUX','Texttreue noch unter SOTA','Brandneuere Modell-Versionen kommen seltener als Konkurrenz','Datenresidenz USA'],
     'usecases':['Video-Storyboard-Frames','Marketing-Visuals','Schnelle Foto-Mockups','Konzept-Art für Game-Cinematics'],
     'launched':'2024-12-03','lastUpdated':'2026-05-01',
     'website':'https://lumalabs.ai/photon','domain':'lumalabs.ai',
     'features':"""- **Photon Flash** für schnelle Iteration (1–2 Sek pro Bild).
- **Photon Pro** für höchste Qualität (3–5 Sek pro Bild).
- **Image-to-Video-Bridge** zu Dream Machine ohne Re-Encode.
- **Reference-Image-Input** für Style-Transfer.
- **Multi-Aspect-Ratio**-Output bis 4K.
- **Prompt-Enhancer** integriert, optional zuschaltbar.
- **API mit identischem Modell** wie Web-UI.""",
     'pricing':"""- **Free** · 30 Credits / Mon., Photon Flash, kein API.
- **Standard** · $10 / Mon. — 1.000 Credits, Photon Flash + Pro, API-Zugang.
- **Plus** · $30 / Mon. — 4.000 Credits, höhere Concurrency.
- **Unlimited** · $95 / Mon. — unbegrenzte Generierung, Priority-Queue.
- **API**: Pay-as-you-go ab $0,003 (Flash) bis $0,02 (Pro) / Bild.
- **Enterprise** · auf Anfrage — Volumen-Pricing, Custom-Modelle.""",
     'overview':"""**Luma Photon** wurde im Dezember 2024 als Lumas eigenständiges Bildmodell gestartet — als Komplement zur **Dream Machine**-Video-Pipeline, die das Unternehmen zuvor bereits zur Spitze der Video-Generierung gebracht hatte. Die strategische Idee: Statt User für die Bild-Komponente zu Konkurrenten zu schicken, bietet Luma eine durchgängige **Bild-zu-Video-Pipeline** in einem Tool und einem Pricing.

Die **Geschwindigkeit** ist das auffälligste Merkmal: Photon Flash liefert Bilder in 1–2 Sekunden — schneller als die meisten Frontier-Modelle. Für Iterations-lastige Workflows (Mood-Boards, Storyboarding) ein massiver Produktivitäts-Vorteil. Photon Pro braucht 3–5 Sekunden, liefert aber Qualität auf Nano-Banana- oder FLUX-Niveau.

Der **Image-to-Video-Übergang** zu Dream Machine ist das eigentliche Killer-Feature: Generiertes Bild auswählen, einen Klick — und Dream Machine animiert es ohne Re-Encode oder Qualitätsverlust. Für Storyboarding und Mockup-Workflows ein durchgängiger Pfad, den Konkurrenten nur mit mehreren Tools abbilden.

Der **Reference-Image-Input** erlaubt Style-Transfer von Bild A auf Generierung B — funktional, aber nicht ganz so präzise wie das Multi-Image-Composition-System von Nano Banana Pro 2 oder GPT Image 2.

Der **Prompt-Enhancer** schreibt knappe Briefings zu detaillierten Prompts um — optional, aber für Einsteiger:innen oft nützlich.

Die **API** spiegelt das Web-Studio mit identischen Modellen — pragmatisch für Anwendungen, die Photon-Bilder in eigene Pipelines einbinden.

Schwächen: Die **Style-Diversität** ist geringer als bei FLUX — wer experimentell-künstlerisch arbeitet, hat dort mehr Spielraum. Die **Texttreue** liegt noch hinter GPT Image 2 und Nano Banana Pro 2 — Schilder, Plakate, mehrsprachige Beschriftungen sind nicht Photons Stärke. **Modell-Releases** kommen seltener als bei OpenAI oder Google — Photon hat bisher nur einen großen Versions-Sprung erlebt.

Empfohlen für Video-Creators und Storyboard-Künstler:innen, die ihre Standbilder in derselben Pipeline animieren wollen — und für jeden, der schnellere Iteration über absolute Spitzenqualität stellt."""},
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
