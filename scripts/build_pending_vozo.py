#!/usr/bin/env python3
"""Build scripts/pending_tools.json with Vozo (AI video translation & dubbing)."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent

TOOLS = [
    {
        'slug': 'vozo', 'name': 'Vozo',
        'vendor': 'Honeybee Technology Ltd', 'category': 'video-audio',
        'tagline': 'KI-Videoübersetzung und -Synchronisation in über 160 Sprachen — klont die Originalstimme statt einer generischen KI-Stimme, übersetzt eingeblendeten Text im Bild („Visual Translate“) und synchronisiert die Lippenbewegungen.',
        'price': 'Free (20 AI-Punkte) · Creator 29 $/Mon. · Studio 99 $/Mon.',
        'api': True, 'dsgvo': 'bedingt', 'origin': 'USA', 'rating': 4.4, 'reviews': 420,
        'pros': [
            'Stimmklonung (VoiceREAL™): die Originalstimme bleibt erhalten, statt generischer TTS-Stimme',
            '„Visual Translate“ übersetzt auch Text im Bild (Folien, Grafiken) und erhält Layout und Animation',
            'Lippensynchronisation (LipREAL™) für natürlich wirkende Ergebnisse',
            '160+ Sprachen inkl. Dialekte/regionaler Varianten; kostenloser Einstieg ohne Kreditkarte',
        ],
        'cons': [
            'US-Anbieter (Honeybee Technology Ltd, Delaware) — Recht und Gerichtsstand USA',
            'Punkte-Modell: Dubbing, Lipsync und Visual Translate verbrauchen unterschiedlich schnell Kontingent',
            'Watermark und 3-Projekt-Limit im Free-Tarif, Videolänge je Tarif begrenzt',
            'Stimmklonung wirft Persönlichkeits- und Urheberrechtsfragen auf — Einwilligung der Sprecher nötig',
        ],
        'usecases': [
            'Kurse und Tutorials mehrsprachig ausspielen',
            'Marketing- und Produktvideos lokalisieren',
            'Social-Media-Inhalte in weitere Märkte bringen',
            'Interviews und Serien synchronisieren',
        ],
        'launched': '2023-05-01', 'lastUpdated': '2026-09-07',
        'website': 'https://www.vozo.ai/', 'domain': 'vozo.ai',
        'stealth': False,
        'cover_cue': 'A hand-drawn film frame showing a speaking face in profile, with three small speech bubbles in different scripts fanning out from the mouth and a tiny slide-with-text icon beside it, one bubble tinted magenta — one video, many languages.',
        'features': """- **Videoübersetzung und Synchronisation** in **über 160 Sprachen**, inklusive Dialekten und regionaler Varianten.
- **Stimmklonung (VoiceREAL™)**: überträgt Klang, Intonation und Sprechtempo der Originalstimme in die Zielsprache; **VoiceNATIVE™** optimiert stattdessen auf möglichst natürliche muttersprachliche Wirkung.
- **Visual Translate**: erkennt eingeblendeten Text im Video (Folien, Grafiken, Overlays), entfernt ihn und setzt ihn übersetzt neu — unter Erhalt von Layout, Stil und Animation.
- **Lippensynchronisation (LipREAL™)**: gleicht die übersetzte Sprache an die Mundbewegungen der Sprecher an.
- **Untertitel**: Generierung sowie Import/Export als SRT, ASS und VTT.
- **Editor** zum Korrekturlesen und Nachschärfen der Übersetzung, Glossar und Marken-Vorgaben (ab Studio).
- **Weitere Werkzeuge**: Talking Photo, Voice Studio, Shorts Generator; Team-Workspaces und API.""",
        'pricing': """- **Free** · 0 $ — 20 AI-Punkte zum Testen (ca. 6 Min. Dubbing, 2 Min. Lipsync, 2 Min. Visual Translate), max. 3 Projekte, 1 Platz, bis 20 Min. Videolänge, mit Wasserzeichen.
- **Creator** · 29 $ / Monat — 150 AI-Punkte (ca. 50 Min. Dubbing, 15 Min. Lipsync, 15 Min. Visual Translate), alle Werkzeuge, bis 60 Min. Videolänge, **ohne Wasserzeichen**.
- **Studio** · 99 $ / Monat — 600 AI-Punkte (ca. 200 Min. Dubbing), 3 Plätze, bis 120 Min. Videolänge, Bulk-Upload, Glossar und Marken-Governance, schnellere Verarbeitung.
- **Studio XL / Enterprise** · für größere Produktionsvolumen auf Anfrage; Punkte-Pakete jederzeit nachkaufbar. Jahreszahlung günstiger.""",
        'overview': """**Vozo** ist ein KI-Werkzeug für **Videoübersetzung und Synchronisation** in über 160 Sprachen. Im Verzeichnis stehen mit **HeyGen**, **Synthesia**, **ElevenLabs** und **Descript** bereits Tools, die Teile davon abdecken — Vozo grenzt sich vor allem über zwei Funktionen ab, die in dieser Kombination selten sind.

Die erste ist die **Stimmklonung**. Statt die übersetzte Tonspur mit einer generischen KI-Stimme zu belegen, überträgt **VoiceREAL™** Klangfarbe, Intonation und Sprechtempo der Originalsprecher:innen in die Zielsprache — die Person klingt also weiterhin nach sich selbst, nur eben auf Spanisch oder Japanisch. Alternativ optimiert **VoiceNATIVE™** auf maximal natürliche muttersprachliche Wirkung, wenn Verständlichkeit wichtiger ist als Wiedererkennbarkeit. Da Vozo Dialekte und regionale Varianten unterstützt, lassen sich Zielsprachen entsprechend feiner wählen — für den deutschsprachigen Raum etwa mit Blick auf regionale Klangfarben, wobei die konkrete Auswahl je Sprache variiert und man das für den eigenen Anwendungsfall prüfen sollte.

Die zweite Besonderheit ist **Visual Translate**: Vozo erkennt Text, der **im Videobild** eingeblendet ist — Folien, Beschriftungen, Grafik-Overlays —, entfernt ihn und setzt ihn übersetzt wieder ein, unter Erhalt von Layout, Stil und Animation. Genau dieser Schritt ist bei klassischen Dubbing-Werkzeugen der teure Rest, der manuell in einem Videoschnittprogramm nachgebaut werden muss. Für Schulungsvideos, Software-Demos und Präsentationsaufzeichnungen, die stark mit Bildschirmtext arbeiten, ist das der praktisch relevanteste Unterschied. Ergänzt wird das durch **Lippensynchronisation (LipREAL™)**, die die übersetzte Sprache an die Mundbewegungen angleicht.

Rundherum gibt es die üblichen Bausteine: Untertitel-Generierung mit Import und Export als SRT, ASS und VTT, einen Editor zum Korrekturlesen, Glossare und Marken-Vorgaben in den größeren Tarifen sowie Team-Workspaces und eine API.

Das **Preismodell** arbeitet mit Punkten: Der **Free-Tarif** gibt 20 AI-Punkte (rund 6 Minuten Dubbing) für maximal drei Projekte und setzt ein Wasserzeichen. **Creator** (29 $/Monat) entfernt das Wasserzeichen und bringt 150 Punkte, **Studio** (99 $/Monat) 600 Punkte plus Bulk-Upload und Governance-Funktionen. Wichtig zu verstehen: Dubbing, Lipsync und Visual Translate verbrauchen die Punkte **unterschiedlich schnell** — 150 Punkte reichen für etwa 50 Minuten Dubbing, aber nur rund 15 Minuten Lipsync. Wer viel synchronisiert, sollte vorab durchrechnen.

Beim **Datenschutz** ist Nüchternheit angebracht. Die Website wirbt mit „GDPR compliant" und einem **SOC-2-Type-II**-Testat, was für Sicherheitsprozesse spricht. Betreiber ist laut Nutzungsbedingungen jedoch die **Honeybee Technology Ltd, registriert in Delaware (USA)**, mit US-Recht und Gerichtsstand. Für die Verarbeitung heißt das: Videomaterial — und damit Stimmen und Gesichter identifizierbarer Personen — wird bei einem US-Anbieter verarbeitet. Das ist mit Auftragsverarbeitungsvertrag gangbar, aber kein EU-Setup; im Verzeichnis steht der Eintrag deshalb auf **„bedingt"**.

Ein Punkt, der über den Datenschutz hinausgeht: **Stimmklonung berührt Persönlichkeitsrechte**. Wer die Stimme anderer Personen klont — Referent:innen, Kund:innen, Mitarbeitende —, braucht deren informierte Einwilligung; bei fremdem Material kommen zusätzlich Urheber- und Leistungsschutzrechte ins Spiel. Vozo liefert die Technik, die rechtliche Absicherung bleibt beim Anwender.

Empfohlen für Teams, die bestehende Videos in mehrere Märkte bringen wollen und dabei Wert darauf legen, dass die Originalstimme erhalten bleibt — besonders bei **Kursen, Tutorials und Produktdemos mit viel Text im Bild**, wo Visual Translate die manuelle Nachbearbeitung spart. Wer dagegen Videos mit synthetischen Avataren von Grund auf erzeugen will, ist bei Synthesia oder HeyGen besser aufgehoben; für reine Sprachsynthese ohne Video genügt ElevenLabs.""",
    },
]

out = ROOT / 'scripts' / 'pending_tools.json'
out.write_text(json.dumps(TOOLS, ensure_ascii=False, indent=2))
print(f'wrote {len(TOOLS)} record(s) to {out.relative_to(ROOT)}')
for t in TOOLS:
    print(f'  - {t["slug"]:6} {t["category"]:12} ov={len(t["overview"])}c  dsgvo={t["dsgvo"]}  origin={t["origin"]}')
