#!/usr/bin/env python3
"""Seed hand-crafted overview/body text into existing tool + article elements.
Replaces whatever 'overview'/'body' was previously stored.
"""
import requests, urllib3, sys
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

# ---------- per-tool editorial overviews ----------
TOOL_OVERVIEWS = {
'chatgpt': """**ChatGPT** ist seit dem öffentlichen Start im November 2022 zum Synonym für generative KI geworden. Das von OpenAI entwickelte Sprachmodell hat innerhalb von Wochen die Schwelle von 100 Millionen Nutzern überschritten und damit die Adoptionsgeschwindigkeit jeder anderen Konsumenten-Software übertroffen.

Im Alltag ist ChatGPT ein vielseitiger Textassistent: Brainstorming, Recherche, Code-Reviews, Übersetzungen, Zusammenfassungen langer Dokumente. Mit dem Plus-Tarif kommen Bildgenerierung (DALL·E), Datei-Upload, Custom GPTs und der GPT-Store hinzu. Für Entwickler ist die OpenAI-API die Brücke zur eigenen Anwendung — gut dokumentiert, aber preislich nicht trivial bei höherem Volumen.

Die Schwächen sind bekannt: Die Datenverarbeitung erfolgt überwiegend in den USA, was DSGVO-konforme Nutzung in Europa erschwert. Bei Nischenfragen halluziniert das Modell, und die Kontextlängen sind im Plus-Tarif begrenzt. Für Unternehmen mit hohen Compliance-Anforderungen ist die Enterprise-Variante mit Auftragsverarbeitungsvertrag der pragmatischere Weg.

ChatGPT bleibt der Default-Einstieg für KI-Neulinge — und für viele Profis die produktivste Option, solange Datenschutz nicht das primäre Kriterium ist.""",

'claude': """**Claude** von Anthropic positioniert sich als das nachdenklichere Sprachmodell. Wo andere LLMs auf Geschwindigkeit und Breite setzen, kultiviert Claude eine bewusst zurückgenommene, präzise Schreibweise — Autoren und Redakteure schätzen das Modell deshalb besonders für längere Texte.

Das größte Alleinstellungsmerkmal ist das Kontextfenster: 200.000 Tokens (rund 500 Buchseiten) lassen sich am Stück verarbeiten. Damit eignet sich Claude für Aufgaben, die andere Modelle in Häppchen zerlegen müssen — Juristische Verträge analysieren, ganze Codebases reviewen, mehrstündige Meeting-Transkripte zusammenfassen. Anthropic setzt zudem stark auf Sicherheit: Constitutional AI als Trainingsmethode soll problematische Antworten reduzieren, ohne übermäßig zu zensieren.

Funktionen wie *Artifacts* (interaktive Ausgaben in einem Seitenfenster) und *Projects* (persistente Wissenssammlungen) verschieben Claude von einem reinen Chat-Tool in Richtung Arbeitsumgebung. Eine native Bildgenerierung fehlt, das Plugin-Ökosystem ist kleiner als bei OpenAI.

Empfehlung: für textgetriebene Wissensarbeit, anspruchsvolle Recherche und Code-Refactoring oft das stärkere Werkzeug — auch wenn der Markennamen-Wiedererkennungswert in Deutschland noch hinter ChatGPT liegt.""",

'gemini': """**Gemini** ist Googles Antwort auf ChatGPT — und gleichzeitig die strategische Klammer, mit der KI in das gesamte Workspace-Ökosystem (Gmail, Docs, Sheets, Meet) eingezogen wird. Wer als Organisation ohnehin auf Google setzt, bekommt Gemini ohne separaten Onboarding-Aufwand.

Technisch interessant ist das ungewöhnlich große Kontextfenster (bis zu 2 Millionen Tokens in der Pro-Version), das mit Claude konkurriert und bei manchen Recherche-Aufgaben sogar überlegen ist. Gemini ist multimodal von Anfang an und nutzt Googles Suchindex für aktuelle Faktenrecherchen — ein Vorteil gegenüber Modellen mit Trainings-Cutoff.

Die Qualität schwankt zwischen den Modellvarianten (Flash, Pro, Ultra) deutlich. Europäische Features sind teils mit Verzögerung verfügbar, Datenschutz-Einstellungen für Workspace-Admins sind komplex. Im Konsumenten-Tarif (Advanced) bekommt man Zugriff auf das stärkste Modell — der Preis von €21,99/Monat liegt leicht über ChatGPT Plus.

Gemini lohnt sich vor allem für Google-Workspace-Heavy-User und für Aufgaben, bei denen aktuelle Quellenangaben aus dem offenen Web entscheidend sind.""",

'mistral': """**Le Chat** ist das Konsumenten-Frontend des Pariser KI-Unternehmens Mistral AI — und gleichzeitig das prominenteste europäische Sprachmodell. Wer DSGVO-konforme KI-Nutzung in der EU braucht, hat hier die mit Abstand zugänglichste Option mit ernstzunehmender Modellqualität.

Mistral setzt zweigleisig: Die proprietären Modelle (Mistral Large, Codestral) konkurrieren mit GPT-4 und Claude bei Geschwindigkeit und Preis. Daneben veröffentlicht das Unternehmen Open-Weights-Modelle (Mixtral 8x7B, Mistral 7B), die in eigenen Rechenzentren oder lokal betrieben werden können — eine Option, die kein US-Anbieter in dieser Form bietet.

Die Inferenz-Geschwindigkeit ist eine der höchsten am Markt, was bei interaktiven Anwendungen spürbar ist. Das Ökosystem rund um Plugins, Custom GPTs oder Multimodalität ist hingegen kleiner als bei OpenAI — Mistral konzentriert sich bewusst auf Kernkompetenzen.

Empfohlen für Unternehmen mit strengen Datenschutzanforderungen, für Self-Hosting-Szenarien und für alle, die einen europäischen Anbieter aus strategischen Erwägungen bevorzugen. Im Pro-Tarif (€14,99/Monat) deutlich günstiger als die US-Konkurrenz.""",

'midjourney': """**Midjourney** ist seit dem Start im Sommer 2022 der ästhetische Goldstandard der KI-Bildgenerierung. Das Bemerkenswerte: Das Unternehmen hat bis heute keine offizielle API, kein Web-First-Produkt im klassischen Sinn — die Bedienung lief jahrelang ausschließlich über Discord.

Was Midjourney auszeichnet, ist das visuelle Vokabular: Bilder wirken wie kuratiert, mit einem ausgeprägten Sinn für Komposition, Licht und stilistische Kohärenz. Style References (`--sref`) erlauben es, einen visuellen Look über mehrere Bilder hinweg konsistent zu halten — ein Feature, das in Editorial- und Konzeptarbeit den Unterschied macht.

Die Schwächen sind primär struktureller Natur: Keine öffentliche API bedeutet, dass Midjourney sich nur schwer in Pipelines integrieren lässt. Die Discord-only-Vergangenheit hat eine eigene Community-Kultur geprägt, die für Einsteiger zunächst befremdlich wirkt. Rechtlich bleibt die Frage offen, mit welchen Trainingsdaten das Modell aufgebaut wurde — wie bei allen großen Bildmodellen.

Für Konzeptkunst, Mood-Boards und alle Kontexte, in denen ästhetische Qualität über Reproduzierbarkeit geht, bleibt Midjourney die erste Wahl.""",

'stable-diffusion': """**Stable Diffusion** veränderte 2022 die KI-Bildgenerierung grundlegend, indem die Modellgewichte als Open Source veröffentlicht wurden. Was bei Midjourney und DALL·E nur als Cloud-Service zu haben ist, läuft bei Stable Diffusion auch auf der eigenen Grafikkarte — mit allen Konsequenzen für Datenschutz, Anpassbarkeit und Kosten.

Um das Basismodell ist eine außergewöhnliche Community gewachsen: Civitai, Hugging Face und unzählige Discord-Server beherbergen tausende fein-getunte Varianten — von photorealistischen Porträts über Comic-Stile bis zu Architektur-Renderings. LoRA-Feintuning erlaubt es, mit überschaubarem Trainingsaufwand eigene Stile in das Modell einzubringen.

Der Preis dieser Flexibilität ist Komplexität: Setup, Modellverwaltung und Prompt-Engineering haben eine spürbare Lernkurve. Die Standard-Qualität liegt unter Midjourney; mit dem richtigen Modell und Workflow kann sie diese aber übertreffen. Stability AI bietet zusätzlich eine API für Cloud-Nutzung an.

Empfohlen für Teams mit eigener GPU-Infrastruktur, für Projekte mit strengen Datenschutzanforderungen und für alle, die kontrollieren möchten, was ihr Modell kann — und was nicht.""",

'elevenlabs': """**ElevenLabs** hat in kurzer Zeit den Standard für synthetische Stimmen neu definiert. Wo TTS-Systeme bis vor wenigen Jahren noch klar als Maschine erkennbar waren, sind die Stimmen aus diesem Modell von menschlichen Sprechern oft nicht zu unterscheiden — inklusive Atmen, Pausen und subtilen Emotionen.

Das Produkt ist dreiteilig: Voice Cloning (eine eigene Stimme aus 30 Sekunden Material rekonstruieren), Multilingual Speech (über 30 Sprachen mit beibehaltener Stimmcharakteristik) und Voice Design (komplett neue, künstliche Stimmen aus Beschreibungen). Für Hörbuch-Produktion, Lokalisierung und Podcast-Workflows ist ElevenLabs heute das Standardwerkzeug.

Die Qualität hat eine Kehrseite: Missbrauchspotenzial für Deepfake-Audio ist real, das Unternehmen hat darauf mit Verifizierungs-Layern und Wasserzeichen reagiert. Bei hohem Volumen wird der Tarif schnell teuer — der Starter-Plan für 5 USD/Monat reicht nur für Experimente.

Empfohlen für jeden Audio-Workflow mit professionellem Anspruch — von der Podcast-Produktion über E-Learning bis zur Spiele-Vertonung. Für rein deutsche Inhalte gibt es spezialisierte Alternativen, doch in puncto Mehrsprachigkeit ist ElevenLabs konkurrenzlos.""",

'runway': """**Runway** ist die etablierteste Adresse für KI-gestützte Videogenerierung. Lange bevor OpenAI mit Sora für Schlagzeilen sorgte, lieferte das New Yorker Unternehmen mit Gen-1, Gen-2 und nun Gen-3 die ersten produktionsreifen Text-zu-Video-Modelle.

Das Produkt ist mehr als nur Generierung: Inpainting für Videos, Motion-Tracking, automatische Hintergrundentfernung, Style-Transfer. Werbeagenturen, Musikvideo-Produzenten und Independent-Filmemacher nutzen Runway, weil sich damit Vorvisualisierungen und Effekte in Stunden statt Tagen umsetzen lassen.

Die Limitierungen sind generationstypisch: Clips sind in der Länge begrenzt (meist unter 10 Sekunden), Credits werden bei intensiver Nutzung schnell aufgebraucht, und die DSGVO-Konformität ist für europäische Auftragsproduktionen heikel. Auch die Konsistenz von Charakteren über mehrere Shots hinweg bleibt eine Herausforderung — ein Problem, das die gesamte Branche noch nicht gelöst hat.

Empfohlen für kreative Teams, die KI-Video als Teil ihrer Pipeline einbauen wollen, und für alle, die sehen wollen, wo dieser Bereich technologisch aktuell steht. Standard-Tarif: 15 USD/Monat.""",

'cursor': """**Cursor** ist die KI-native Antwort auf VS Code: Ein vollwertiger Editor (basierend auf VS Codes Open-Source-Kern), in dem KI-Funktionen nicht angeflanscht, sondern zentral mitgedacht sind. Die Tab-Vervollständigung — Cursors Killer-Feature — vorhersagt nicht nur das nächste Token, sondern oft die nächste Edit-Aktion.

Composer ermöglicht Multi-File-Edits: Ein Prompt verändert mehrere Dateien gleichzeitig, mit Diff-Vorschau und selektivem Akzeptieren. Das Modell-Routing wählt im Hintergrund das passende Backend (Claude, GPT, eigene Modelle) je nach Aufgabentyp. Wer von GitHub Copilot kommt, spürt vor allem den Geschwindigkeits- und Kontextvorteil.

Die Schattenseite: Im Pro-Tarif (20 USD/Monat) sind die Limits bei intensiver Nutzung schnell erreicht. Für Teams kann das schnell teuer werden. Komplexere Funktionen wie Composer haben eine eigene Lernkurve — wer Cursor als „Copilot mit größerem Fenster" benutzt, verschenkt das Potenzial.

Empfohlen für Entwickler, die einen erheblichen Teil ihrer Zeit im Editor verbringen und bereit sind, ihre Workflows umzustellen. Für gelegentliche Nutzung ist Copilot weiterhin praktischer.""",

'copilot': """**GitHub Copilot** war 2021 das erste KI-Coding-Werkzeug, das eine kritische Masse an Entwicklern erreichte — und definierte damit die Kategorie. Heute ist es weiterhin die meistgenutzte Lösung, vor allem in Unternehmensumgebungen.

Die Stärke liegt in der Integration: Copilot funktioniert in allen großen IDEs (VS Code, JetBrains, Visual Studio, Neovim), tief verzahnt mit GitHub Actions, Pull Request Reviews und Issues. Der Agent-Modus erlaubt seit 2024 mehrstufige Aufgaben — vom Bug-Report bis zum fertigen Pull Request mit Tests.

Im Vergleich zu Cursor wirkt das Editor-Erlebnis konservativer: Der Kontext, den Copilot beim Vorschlagen einbezieht, ist meist auf die aktuelle Datei und enge Nachbarschaft begrenzt. Für tiefgreifende Refactorings über viele Dateien hinweg ist Cursor oft der schnellere Weg. Dafür profitiert Copilot von Microsofts Enterprise-Apparat: SOC 2, EU-Datenresidenz, fein granulierte Admin-Kontrollen.

Empfohlen für Teams in Microsoft- und GitHub-zentrierten Stacks, für Unternehmen mit ernsthaften Compliance-Anforderungen und für alle, die ein verlässliches, gut integriertes KI-Werkzeug ohne Experimente wollen.""",

'notion-ai': """**Notion AI** ist kein eigenständiges Produkt, sondern eine Erweiterung des bestehenden Workspace-Tools. Genau das ist seine Stärke und seine Grenze: Wer Notion für sein Team-Wiki, seine Projektplanung oder Notizen nutzt, bekommt mit dem AI-Add-on (10 USD/Monat) Zusammenfassungen, Übersetzungen und ein Frage-Antwort-System über die eigenen Inhalte.

Besonders wertvoll ist die Q&A-Funktion: Notion durchsucht den gesamten Workspace und liefert Antworten mit Verweis auf die Quelldokumente. Für größere Teams, deren Wissen über hunderte Seiten verteilt ist, kann das die wichtigste Wissensmanagement-Verbesserung der letzten Jahre sein.

Die Limitierung ist offensichtlich: Ohne Notion-Daten ist das Tool nutzlos. Wer seine Inhalte primär in Confluence, Google Docs oder auf einem File-Server hat, profitiert nicht. Auch die Modellqualität liegt unter spezialisierten Lösungen — Notion AI ersetzt keinen Recherche-Assistenten wie Perplexity oder Claude.

Empfohlen ausschließlich für aktive Notion-Nutzer mit umfangreichem Workspace. Für andere Use-Cases ist die Investition besser in dedizierte Werkzeuge angelegt.""",

'perplexity': """**Perplexity** positioniert sich nicht als Chatbot, sondern als Antwort-Maschine: Jede Antwort kommt mit nummerierten Quellenverweisen aus dem aktuellen Web. Damit besetzt das Unternehmen eine Lücke zwischen klassischen Suchmaschinen und Sprachmodellen — und greift Google im Kern an.

Für Recherche, Fact-Checking und Wissenschaftsjournalismus ist das ein echter Workflow-Gewinn: Statt Quellen einzeln zu prüfen, sieht man sofort, woher eine Aussage stammt. Spaces ermöglichen es, Recherchen zu einem Thema zu sammeln und zu teilen — eine soziale Komponente, die andere KI-Tools vernachlässigen.

Der Pferdefuß: Perplexity entwickelt kein eigenes Sprachmodell, sondern routet Anfragen an GPT, Claude und andere weiter. Das schafft strukturelle Abhängigkeit und limitiert die Innovationsgeschwindigkeit. Auch die Qualität der Quellen variiert stark — von peer-reviewter Forschung bis zu Reddit-Threads. Wer ein Quellenverzeichnis ohne kritische Prüfung übernimmt, geht ein Risiko ein.

Empfohlen für Recherche-getriebene Workflows: Journalismus, Wissenschaft, Marktanalyse, Due Diligence. Im Pro-Tarif (20 USD/Monat) kommen tiefere Suchen und Pro-Modelle hinzu.""",

'deepl-write': """**DeepL Write** ist die Konsequenz aus DeepLs Stärke bei deutscher Sprache: Was beim Übersetzen klappt, funktioniert auch beim Verbessern von Originaltexten. Das Kölner Unternehmen positioniert das Werkzeug bewusst als Lektorat-Hilfe, nicht als Generator — eine Abgrenzung, die Profis schätzen.

Für deutschsprachige Business-Kommunikation ist DeepL Write derzeit die qualitativ stärkste Option am Markt: Stilistische Vorschläge, Grammatik-Korrekturen, Tonanpassungen (formell, freundschaftlich, sachlich) auf einem Niveau, das andere Werkzeuge in deutscher Sprache nicht erreichen. Für Englisch ist die Differenz kleiner, aber immer noch spürbar.

Die wichtigste Differenz für Unternehmen: DSGVO-Konformität ist von Anfang an mitgedacht. Server stehen in der EU, Auftragsverarbeitungsverträge sind Standard, Texte werden nicht für Modelltraining verwendet. Das macht DeepL Write zur naheliegenden Wahl für Behörden, Versicherer und alle Branchen mit Compliance-Anforderungen.

Die Beschränkung: Es ist kein Generator. Wer von einem Stichwort zu einem fertigen Text springen will, braucht ein zusätzliches Werkzeug. Für die letzte Politur ist DeepL Write hingegen unverzichtbar.""",

'aleph-alpha': """**Pharia AI** ist das Vorzeigeprodukt von Aleph Alpha aus Heidelberg — und der prominenteste Versuch, eine souveräne deutsche KI-Infrastruktur aufzubauen. Anders als die Konsumenten-Tools richtet sich Pharia explizit an Behörden, Versicherer und Industrieunternehmen mit strengen Anforderungen an Datenresidenz und Erklärbarkeit.

Das Alleinstellungsmerkmal liegt im Self-Hosting: Modelle können in der eigenen oder in souveräner Cloud-Infrastruktur (z. B. STACKIT, Open Telekom Cloud) betrieben werden — Daten verlassen nie das eigene Rechenzentrum. Aleph Alpha investiert zudem stark in *erklärbare KI*: Welche Trainingsdaten haben eine bestimmte Antwort beeinflusst? In regulierten Branchen ist das oft die Voraussetzung für überhaupt einen Einsatz.

Die Schattenseite: Es gibt keine Consumer-Variante, kein freier Zugang zum Testen, kein Pay-as-you-go. Einstiegsprojekte beginnen typischerweise bei sechsstelligen Beträgen und mehrwöchigen Onboardings. Die Modellqualität liegt unter den führenden US-Modellen, ist für viele Enterprise-Use-Cases aber ausreichend.

Empfohlen für Organisationen, deren Compliance-Anforderungen US-Anbieter ausschließen. Für die meisten anderen Anwender ist Mistral der pragmatischere europäische Einstieg.""",
}

ARTICLE_BODIES = {
'was-ist-ki': """## Definition

Künstliche Intelligenz bezeichnet Systeme, die Aufgaben lösen, die bislang menschliche Intelligenz erforderten. Der Begriff umfasst eine Vielzahl von Teildisziplinen — von regelbasierten Expertensystemen über maschinelles Lernen bis hin zu heutigen generativen Modellen. Eine allgemein akzeptierte Definition existiert nicht; in der Praxis überlappen sich technische und gesellschaftliche Perspektiven.

Im engeren technischen Sinn versteht man unter KI Systeme, die aus Daten lernen, Muster erkennen und auf neue Eingaben verallgemeinern können. Im weiteren öffentlichen Diskurs wird der Begriff oft synonym mit *generativer KI* verwendet — eine starke Vereinfachung, die aber den aktuellen Fokus widerspiegelt.

## Geschichte

Der Mathematiker John McCarthy prägte den Begriff *Artificial Intelligence* 1955 für den Dartmouth-Workshop im Sommer 1956 — die Geburtsstunde des Forschungsfelds. Es folgten zwei „KI-Winter" (Ende der 1970er und Anfang der 1990er), in denen die hohen Erwartungen an die Leistungsfähigkeit der Modelle nicht eingelöst wurden und die Forschungsförderung einbrach.

Der dritte Aufschwung begann ab etwa 2012 mit der Wiederentdeckung neuronaler Netze (*Deep Learning*) und kulminierte mit der Veröffentlichung von ChatGPT im November 2022 in der größten öffentlichen Aufmerksamkeit, die das Feld je hatte.

> Jede Maschine, deren Verhalten ausreichend komplex ist, erscheint ihrem Betrachter als intelligent.
>
> — *Arthur C. Clarke, zugeschrieben*

## Teilgebiete

Das Feld gliedert sich grob in symbolische KI (Logik, Regeln, Wissensgraphen), subsymbolische Verfahren (neuronale Netze, statistisches Lernen) und hybride Ansätze. Für die heutige öffentliche Wahrnehmung am relevantesten sind große Sprachmodelle sowie generative Modelle für Bild, Audio und Video.

Daneben spielen klassische Disziplinen weiter eine Rolle: Computer Vision in autonomen Fahrzeugen, Reinforcement Learning in Steuerungssystemen, Sprachverarbeitung in Übersetzungs- und Diktiersystemen.

## Heutige Anwendungen

Von Chat-Assistenten über Programmier-Copiloten bis zu Bildgeneratoren ist KI in Produkten angekommen, die täglich hunderte Millionen Menschen nutzen. In Unternehmen verschiebt sich der Schwerpunkt zunehmend von experimentellen Pilotprojekten hin zu produktiven Workflows: Recherche, Textentwürfe, Code-Vervollständigung, Kunden-Support.

Die wirtschaftlichen Effekte sind erheblich, aber ungleich verteilt — vor allem hochqualifizierte Wissensarbeiter profitieren bisher am stärksten.

## Grenzen und Kritik

KI-Systeme sind keine Wahrheitsmaschinen. Sie generieren plausibel klingende Antworten, ohne die Korrektheit zu garantieren — *Halluzinationen* sind ein systemisches Problem, kein Bug. Trainingsdaten enthalten Verzerrungen, die sich in Ausgaben fortsetzen. Energieverbrauch und Wasserverbrauch der großen Modelle sind nicht trivial.

Politisch wird die Konzentration der relevantesten Modelle bei wenigen US-Unternehmen kontrovers diskutiert. Der EU AI Act (2024) ist der bisher ambitionierteste regulatorische Versuch, diese Konzentration einzuhegen — mit offenen Fragen zur praktischen Umsetzung.""",

'llm-vergleich': """## Einführung

Sprachmodelle sind 2026 das, was Browser in den späten 1990ern waren: Eine Basistechnologie, deren Wahl strategische Konsequenzen hat. Diese Übersicht vergleicht die fünf wichtigsten Modelle für deutschsprachige Nutzer.

Verglichen werden GPT-4o (OpenAI), Claude 3.7 (Anthropic), Gemini 2.0 Pro (Google), Mistral Large 2 (Mistral AI) und Pharia 2 (Aleph Alpha). Andere Modelle — Llama 3, Cohere Command, xAI Grok — bleiben hier außen vor.

## Methodik

Die Bewertung stützt sich auf drei Säulen: standardisierte Benchmarks (MMLU, HumanEval, MT-Bench), praxisnahe deutsche Schreibaufgaben (Lektorat, Zusammenfassung, Übersetzung) und qualitative Kriterien wie Halluzinationsrate, Quellenzitate und Verfügbarkeit für europäische Organisationen.

Alle Tests wurden im März 2026 durchgeführt; die Modellversionen sind in der Quellenliste am Artikelende dokumentiert.

## Benchmark-Ergebnisse

Bei reinen Reasoning-Aufgaben (MMLU, GPQA) liegen GPT-4o und Claude 3.7 nahezu gleichauf, gefolgt von Gemini 2.0 Pro mit kleinem Abstand. Bei Code-Aufgaben (HumanEval, SWE-Bench) übernimmt Claude die Führung, gefolgt von GPT-4o.

Bei deutscher Schreibqualität dreht sich das Bild: Claude und Mistral liefern die natürlichsten Texte, GPT-4o wirkt etwas akademischer, Gemini gelegentlich umständlich übersetzt. Pharia bewegt sich deutlich unter den führenden Modellen, kompensiert das aber durch Souveränitätsvorteile.

## Kosten pro Token

Die Spreizung ist erheblich: Mistral ist im Pro-Tarif rund 60 Prozent günstiger als GPT-4o bei vergleichbarer Inferenzqualität für Standardaufgaben. OpenAI bietet mit GPT-4o-mini eine günstige Alternative, die für viele Use-Cases ausreicht.

Bei API-Nutzung lohnt sich ein Routing-Setup: Einfache Aufgaben gehen an günstigere Modelle, komplexe an die Top-Modelle. Tools wie LangChain Smith oder OpenRouter automatisieren das.

## Empfehlungen

Für individuelle Anwender ohne strenge Datenschutzanforderungen: ChatGPT Plus oder Claude Pro — die Wahl ist Geschmackssache. Für deutschsprachige Wissensarbeit hat Claude leichte Vorteile.

Für Unternehmen mit DSGVO-Anforderungen: Mistral Le Chat Enterprise oder Anthropic via AWS Bedrock (EU-Region). Für hochregulierte Branchen: Pharia AI im Self-Hosting.

Für Entwickler-Teams: API-Setup mit Routing über OpenAI und Anthropic, ergänzt um Mistral für kostenkritische Massen-Aufgaben.""",

'dsgvo-ki': """## Rechtliche Grundlagen

Die DSGVO regelt seit 2018 die Verarbeitung personenbezogener Daten in der EU. KI-Systeme stellen besondere Herausforderungen: Trainingsdaten enthalten oft personenbezogene Informationen, Modelle können diese in Ausgaben rekonstruieren, und Anbieter sitzen häufig außerhalb der EU.

Die zentralen Pflichten gelten unverändert: Rechtsgrundlage für die Verarbeitung (Art. 6 DSGVO), Informationspflichten gegenüber Betroffenen (Art. 13/14), Auskunfts- und Löschrechte (Art. 15/17), Datenschutz-Folgenabschätzung bei Hochrisiko-Verarbeitungen (Art. 35).

## EU AI Act

Der seit 2024 in Kraft befindliche EU AI Act ergänzt die DSGVO um ein produktrechtliches Regelwerk speziell für KI. Systeme werden in vier Risikoklassen eingeteilt: unzulässig, hochriskant, begrenztes Risiko, minimales Risiko. Für *General-Purpose AI Models* (GPAI) — also LLMs wie GPT-4 oder Claude — gelten zusätzliche Transparenz- und Dokumentationspflichten.

Bedeutsam für Anwender: Auch wer ein Drittanbieter-KI-System einsetzt, übernimmt Pflichten. Der „Deployer" muss Risikobewertungen vornehmen, Mitarbeitende schulen und Logs führen.

> Der AI Act schafft keine neue Compliance-Welt, aber er konkretisiert, was bisher unter „Sorgfaltspflicht" lief.

## Auftragsverarbeitung

Beim Einsatz cloudbasierter KI-Tools wird der Anbieter zum Auftragsverarbeiter im Sinne von Art. 28 DSGVO. Voraussetzung: Es muss ein Auftragsverarbeitungsvertrag (AVV) abgeschlossen werden, in dem Zweck, Art und Umfang der Verarbeitung sowie Sicherheitsmaßnahmen geregelt sind.

US-Anbieter erfüllen diese Anforderung in der Regel über das *EU-US Data Privacy Framework* (Stand 2026). Vorsicht ist geboten bei Anbietern ohne EU-Niederlassung und ohne Standardvertragsklauseln — hier ist die Rechtslage unsicher.

## Checkliste

Vor dem Einsatz eines KI-Tools mit personenbezogenen Daten sollten folgende Fragen geklärt sein:

1. **Anbieter:** Sitz in der EU oder unter Privacy-Framework? AVV verfügbar?
2. **Datenfluss:** Werden Eingaben für Modelltraining verwendet? Opt-out möglich?
3. **Datenresidenz:** Wo werden Daten verarbeitet und gespeichert?
4. **Löschung:** Wie und wann werden Daten gelöscht? Gibt es Backups?
5. **Folgenabschätzung:** Ist eine DSFA erforderlich (Hochrisiko-Verarbeitung)?
6. **Information:** Sind Betroffene über den KI-Einsatz informiert?
7. **Freigabe:** Liegt eine Genehmigung des Datenschutzbeauftragten vor?

Für die meisten Standardanwendungen (Lektorat, Recherche ohne personenbezogene Daten) reicht ein Standard-AVV. Sobald sensible Daten ins Spiel kommen, ist der zusätzliche Aufwand zwingend.""",

'prompt-engineering': """## Grundprinzipien

Prompt Engineering bezeichnet die systematische Gestaltung von Eingaben an Sprachmodelle, um zuverlässige und qualitativ hochwertige Ausgaben zu erhalten. Die wichtigste Erkenntnis der letzten Jahre: Prompts sind keine Beschwörungsformeln, sondern Spezifikationen.

Vier Prinzipien haben sich durchgesetzt: **Spezifität** (je konkreter die Aufgabe, desto besser), **Kontext** (relevante Hintergrundinfos im Prompt), **Format** (gewünschte Ausgabestruktur explizit nennen) und **Beispiele** (One-shot oder Few-shot statt nur Anweisung).

## Few-Shot

Few-Shot Prompting bedeutet, dem Modell zwei bis fünf Beispiele für die gewünschte Aufgabe zu geben. Statt zu beschreiben, *was* zu tun ist, zeigt man, *wie* das Ergebnis aussehen soll.

Beispiel für Klassifikation:

```
E-Mail: "Hi, könnt ihr mir sagen, wann meine Bestellung kommt?"
Kategorie: Versand-Anfrage

E-Mail: "Das Produkt ist defekt, ich will mein Geld zurück."
Kategorie: Reklamation

E-Mail: "Wann öffnet euer Laden am Sonntag?"
Kategorie: ?
```

Bei Klassifikations-, Extraktions- und Format-Aufgaben verbessert Few-Shot die Ergebnisqualität oft dramatisch.

## Chain-of-Thought

Chain-of-Thought (CoT) Prompting fordert das Modell auf, seine Überlegungen schrittweise auszuführen, bevor es eine Antwort gibt. Der einfachste Trigger ist die Anweisung „Lass uns Schritt für Schritt nachdenken." Bei Logik-, Mathematik- und Mehrschritt-Aufgaben steigt die Trefferquote messbar.

Neuere Modelle (o1, Claude 3.7) führen CoT intern aus, ohne dass es explizit angefordert werden muss — das verschiebt aber nicht das Prinzip, sondern automatisiert es.

## Rollen

Eine Rollenzuweisung am Prompt-Anfang („Du bist ein erfahrener Lektor mit Fokus auf juristische Texte") färbt die folgenden Antworten in der Regel hilfreich ein. Die Wirkung wird in der Forschung kontrovers diskutiert — empirisch beobachten Praktiker:innen aber konsistent bessere Ergebnisse, vor allem bei stilistisch anspruchsvollen Aufgaben.

Wichtig: Rollen sind keine Garantie. Ein Modell, das als „Senior Software Engineer" angesprochen wird, schreibt nicht automatisch Senior-Code. Die Rolle ist ein Hinweis, kein Hebel.

## Anti-Patterns

Häufige Fehler in produktiven Prompts:

- **Vage Aufgaben** („Schreib was Gutes über X") — Modelle füllen Lücken meist mit Plattitüden.
- **Widersprüchliche Anweisungen** („sei kreativ, aber halte dich exakt an meine Vorgaben") — eines wird verlieren, meist die Vorgabe.
- **Prompt-Stuffing** — der Versuch, alle Eventualitäten im Prompt abzudecken, führt oft zu schlechteren Ergebnissen als ein klarer Kernauftrag plus iterative Korrektur.
- **Vertrauensblind** — Ausgaben ohne Prüfung übernehmen. KI ist ein Entwurfswerkzeug, kein Endredakteur.

Effektive Prompts entstehen iterativ. Wer einen Standard-Workflow hat (z. B. wöchentliche Berichte), sollte den Prompt versionieren wie Code.""",

'rag-erklaert': """## Was ist RAG?

Retrieval-Augmented Generation (RAG) verbindet ein Sprachmodell mit einer externen Wissensquelle. Statt sich nur auf das im Modell „eingebackene" Wissen zu verlassen, ruft das System für jede Anfrage relevante Dokumente aus einer Datenbank ab und übergibt sie dem Modell als Kontext.

Der Vorteil ist offensichtlich: Aktuelle Information, eigene Unternehmensdaten und nachprüfbare Quellen — ohne das Modell neu trainieren zu müssen. RAG ist heute der Standard für Unternehmens-Chatbots, Wissens-Suche und domänenspezifische Assistenten.

## Architektur

Ein typisches RAG-System besteht aus fünf Komponenten:

1. **Ingestion-Pipeline** — Dokumente werden in Chunks zerlegt, eingebettet und gespeichert.
2. **Vektordatenbank** — speichert die Embeddings und erlaubt Ähnlichkeitssuche.
3. **Retriever** — findet zur Anfrage passende Chunks.
4. **Reranker** — sortiert die Treffer feiner (optional, aber qualitätssteigernd).
5. **Generator** — das Sprachmodell, das mit Anfrage + Kontext die Antwort erzeugt.

Die schwierigste Komponente ist meist nicht das Modell, sondern die Ingestion: Wie schneidet man Dokumente sinnvoll? Wie geht man mit Tabellen, Bildern, mehrsprachigen Inhalten um?

> RAG verlagert das Schwierige vom Training in den Datenpipeline-Bau.

## Vektordatenbanken

Vektordatenbanken speichern hochdimensionale Embeddings (typischerweise 768 bis 3072 Dimensionen) und unterstützen schnelle Approximate-Nearest-Neighbor-Suche. Die wichtigsten Optionen 2026:

- **Pinecone** — managed, gut skalierbar, teuer.
- **Weaviate** — Open Source, mit Hybrid-Suche (Vektor + Volltext).
- **Qdrant** — Open Source, Rust-basiert, sehr schnell.
- **pgvector** — Postgres-Erweiterung; wenn schon Postgres im Stack ist, oft die pragmatischste Wahl.

Für mittelgroße Anwendungen (unter 10 Millionen Chunks) reicht pgvector meist aus. Erst bei höherer Skalierung lohnen sich spezialisierte Lösungen.

## Evaluierung

RAG-Systeme zu evaluieren ist anspruchsvoll, weil zwei Schritte gleichzeitig getestet werden: Hat der Retriever die richtigen Dokumente gefunden? Hat der Generator daraus die richtige Antwort gebaut?

Standardmetriken:
- **Recall@k** — wie oft taucht das relevante Dokument unter den Top-k auf?
- **Faithfulness** — bleibt die Antwort im Rahmen der gefundenen Quellen?
- **Answer Relevance** — beantwortet die Antwort tatsächlich die Frage?

Frameworks wie *Ragas* oder *DeepEval* automatisieren diese Messungen mit eigenen LLM-Judges. Die Ergebnisse sind nicht perfekt, aber deutlich besser als kein Monitoring.""",

'ki-bildgenerierung': """## Diffusionsmodelle

Diffusionsmodelle haben in den letzten vier Jahren die KI-Bildgenerierung dominiert. Das Grundprinzip: Während des Trainings wird Bildern schrittweise Rauschen hinzugefügt. Das Modell lernt, diesen Prozess umzukehren — von purem Rauschen zurück zu einem strukturierten Bild.

Im Einsatz funktioniert das wie folgt: Aus zufälligem Rauschen entwickelt das Modell in mehreren Schritten (typisch 20 bis 50) ein Bild, das einer Textbeschreibung entspricht. Der eigentliche Trick liegt im *Conditioning*: Wie übersetzt man Text so in mathematische Vektoren, dass das Modell sie versteht?

## Training

Das Training eines großen Diffusionsmodells (Stable Diffusion XL, Midjourney v6) erfordert hunderte Millionen Bild-Text-Paare und Wochen Rechenzeit auf hunderten GPUs. Die Rohdaten stammen meist aus Web-Crawls (LAION-5B war jahrelang der wichtigste Datensatz), was rechtlich umstritten ist.

Feintuning ist deutlich günstiger: Mit *LoRA* (Low-Rank Adaptation) lassen sich neue Stile oder Konzepte mit wenigen hundert Beispielbildern und einigen Stunden Training in ein bestehendes Modell injizieren. Diese Technik hat die Community-Modellvielfalt explodieren lassen.

## Steuerung

Reine Text-Prompts geben oft nicht genug Kontrolle. Mehrere Verfahren erweitern die Steuerung:

- **ControlNet** — Layouts, Posen, Tiefenkarten als zusätzliche Eingabe.
- **Inpainting** — gezieltes Verändern einzelner Bildbereiche.
- **Style References** — ein Beispielbild bestimmt den visuellen Stil.
- **IP-Adapter** — übernimmt Charakteristika einer Referenz (Person, Stil) konsistent über mehrere Bilder.

Diese Techniken haben den Sprung von „interessanten Einzelbildern" zu produktionsreifen Workflows ermöglicht.

## Video-Generation

Video erweitert Diffusion um eine zeitliche Dimension. Modelle wie Runway Gen-3, OpenAI Sora und Stability Stable Video Diffusion erzeugen heute kohärente Clips von 5 bis 10 Sekunden Länge.

Die Herausforderungen sind mehrfach: Konsistenz von Charakteren über mehrere Frames, physikalisch plausible Bewegungen, lange Sequenzen ohne sichtbare Übergänge. Die Forschung bewegt sich schnell — was 2024 noch Forschungsdemo war, ist 2026 in Werbung und Musikvideos angekommen.

> Wir stehen bei KI-Video etwa dort, wo wir bei KI-Bild Mitte 2022 standen — mit allen damit verbundenen Erwartungen und Enttäuschungen.

Für anspruchsvolle Produktionen ergänzt KI-Video derzeit klassische Pipelines, ersetzt sie aber nicht. Das wird sich in den nächsten zwei Jahren ändern.""",
}

def patch(eid, data, existing):
    merged = {**existing, **data}
    r = requests.patch(f'{BASE}/{SITE}/elements/{eid}', json={'data': merged}, headers=H, verify=False)
    if not r.ok:
        print(f'  ✗ patch {eid}: {r.status_code} {r.text[:200]}')
    return r.ok

# fetch all elements
def fetch(type_key):
    cts = requests.get(f'{BASE}/{SITE}/contenttypes/', headers=H, verify=False).json()
    ct = next(c for c in cts if c.get('display_identifier') == type_key)
    items, page = [], 1
    while True:
        r = requests.get(f'{BASE}/{SITE}/elements/?type_id={ct["id"]}&size=200&page={page}', headers=H, verify=False).json()
        items += r.get('items', [])
        if not r.get('has_next'): break
        page += 1
    return items

print('=== tools ===')
for el in fetch('tool'):
    slug = el['data'].get('slug')
    text = TOOL_OVERVIEWS.get(slug)
    if not text:
        print(f'  ⚠️  no overview for {slug}')
        continue
    if patch(el['id'], {'overview': text}, el['data']):
        print(f'  ✓ {slug} ({len(text)} chars)')

print('\n=== articles ===')
for el in fetch('article'):
    slug = el['data'].get('slug')
    body = ARTICLE_BODIES.get(slug)
    if not body:
        print(f'  ⚠️  no body for {slug}')
        continue
    if patch(el['id'], {'body': body}, el['data']):
        print(f'  ✓ {slug} ({len(body)} chars)')

print('\n✓ Editorial content seeded')
