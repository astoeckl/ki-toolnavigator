#!/usr/bin/env python3
"""Build scripts/pending_tools.json with 2 user-submitted tools: Gardmi + Dooken."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent

TOOLS = [
    {
        'slug': 'gardmi', 'name': 'Gardmi',
        'vendor': 'Gardmi', 'category': 'produktivitaet',
        'tagline': 'Kostenloser browserbasierter Garten- und Grundstücksplaner — ein KI-Assistent liefert einen ersten maßstäblichen 2D-Entwurf, der editierbar bleibt und in synchroner 3D-Ansicht prüfbar ist.',
        'price': 'Kostenlos · kein Pflichtkonto · PNG/PDF-Export ohne Anmeldung',
        'api': False, 'dsgvo': 'bedingt', 'origin': 'k. A.', 'rating': 4.2, 'reviews': 90,
        'pros': [
            'Kostenlos und ohne Pflichtkonto nutzbar',
            'KI-Ersten-Entwurf als editierbaren, maßstäblichen 2D-Plan (kein statisches Bild)',
            'Synchrone 3D-Ansicht; Objekte (Gebäude, Wege, Pflanzen) bleiben editierbar',
            'PNG/PDF-Export ohne Anmeldung',
        ],
        'cons': [
            'Ersetzt keine Vermessung, Grenz-/Leitungsprüfung, Fachplanung oder Genehmigung',
            'KI-Entwurf ist ein Entwurf — Maße und Vorschriften selbst prüfen',
            'Anbieter beansprucht ausdrücklich keinen bestimmten DSGVO-Status',
            'Nische; Katasterdaten nur regional verfügbar',
        ],
        'usecases': [
            'Erster Garten- oder Grundstücksentwurf', 'Ideen maßstäblich visualisieren (2D + 3D)',
            'Flächen, Wege und Pflanzungen planen', 'Export für Absprachen mit Fachleuten',
        ],
        'launched': '2024-09-01', 'lastUpdated': '2026-07-13',
        'website': 'https://gardmi.com/de/ai-landscape-design/', 'domain': 'gardmi.com',
        'stealth': False,
        'cover_cue': 'A hand-drawn top-down garden plot with a dotted property boundary, a small house rectangle, a curved path and two tree circles, one tree tinted magenta — an editable scaled garden plan.',
        'features': """- **KI-Assistent „Bo"**: erzeugt aus einer natürlichsprachlichen Beschreibung einen ersten Entwurf.
- **Maßstäblicher 2D-Plan** mit realen Maßen (CAD-artige, editierbare Objekte).
- **Synchrone 3D-Ansicht** zum Prüfen des Entwurfs.
- **Editierbare Objekte**: Gebäude, Wege, Flächen, Pflanzen und mehr bleiben anpassbar.
- **Referenz-Abstands-/Schutzzonen** aus dem Gardmi-Katalog, Überschneidungen rot markiert.
- **PNG/PDF-Export** ohne Pflichtkonto; Katasterdaten-Laden regional verfügbar.
- **Browserbasiert** — keine Installation nötig.""",
        'pricing': """- **Kostenlos** · ohne Kreditkarte, ohne Pflichtkonto, ohne Trial-Beschränkung.
- **Export** (PNG/PDF) ohne Anmeldung möglich.
- Kein öffentlich beworbenes Bezahlmodell bekannt.""",
        'overview': """**Gardmi** ist ein kostenloser, browserbasierter **Garten- und Grundstücksplaner**, der als Nischen-Vorschlag für dieses Verzeichnis eingereicht wurde. Der Ansatz unterscheidet sich bewusst von reinen KI-Bildgeneratoren: Statt eines hübschen, aber statischen Renderings erzeugt Gardmi einen **editierbaren, maßstäblichen Plan**.

Der Einstieg läuft über den KI-Assistenten **„Bo"**: Nutzer:innen beschreiben ihr Vorhaben in natürlicher Sprache, und Bo erstellt einen ersten Entwurf — Grundstücks-Zonierung, Gebäude-Layouts, Wege, Flächen, Pflanzungen, teils bis zu Entwässerungselementen. Entscheidend ist, dass dieser Entwurf anschließend als **maßstäblicher 2D-Plan** weiterbearbeitet werden kann: Jedes Objekt — Gebäude, Weg, Baum, Pflanzfläche — bleibt editierbar, mit realen Maßen, ähnlich einer leichten CAD-Umgebung. Eine **synchrone 3D-Ansicht** erlaubt es, den Entwurf räumlich zu prüfen.

Praktisch relevant ist die **Referenzdarstellung von Abstands- und Schutzzonen** aus Gardmis Katalog: Überschneidungen werden rot markiert, was ein erstes Gefühl für mögliche Konflikte gibt. Der **Export** als PNG oder PDF funktioniert ohne Pflichtkonto, und Katasterdaten lassen sich regional einladen, wo verfügbar. Das gesamte Tool läuft im Browser, ohne Installation, und ist kostenlos.

**Wichtig — und vom Anbieter selbst transparent kommuniziert — sind die Grenzen.** Gardmi ersetzt ausdrücklich **keine Vermessung, keine Leitungs- oder Grenzprüfung, keine Entwässerungs- oder Fachplanung, keine Genehmigung und keine Prüfung lokaler Vorschriften**. Der KI-Assistent „kann Fehler machen"; der erzeugte Plan ist ein **Entwurf**, keine offizielle Genehmigung. Maße, Abstände und rechtliche Anforderungen müssen vor einer Umsetzung unabhängig geprüft werden. Der Anbieter **beansprucht zudem ausdrücklich keinen bestimmten DSGVO-Status** und bittet darum, Datenschutz und Eignung unabhängig anhand der öffentlich zugänglichen Informationen zu bewerten — diese Einschätzung sollte man vor einer Nutzung mit personenbezogenen oder grundstücksbezogenen Daten also selbst treffen.

Empfohlen als niedrigschwelliger, kostenloser Einstieg, um eine **erste Garten- oder Grundstücksidee maßstäblich zu visualisieren** — für Hausbesitzer:innen, Bauherr:innen und Planer:innen, die schnell einen bearbeitbaren Entwurf brauchen, bevor Fachleute mit Vermessung, Genehmigung und Fachplanung übernehmen. Als Werkzeug für die verbindliche Planung ist es nicht gedacht; seine Stärke liegt im schnellen, editierbaren Erstentwurf.""",
    },
    {
        'slug': 'dooken', 'name': 'Dooken',
        'vendor': 'Dooken', 'category': 'marketing',
        'tagline': 'Deutscher KI-Generator für verkaufsstarke Static Ads — erzeugt aus Produktbildern komplette Werbeanzeigen mit Text, Layout und Bildbearbeitung, mit branchenerprobten „Angles" statt reiner Prompt-Lotterie.',
        'price': '10 Ads gratis (ohne Kreditkarte) · danach kostenpflichtige Pläne',
        'api': False, 'dsgvo': 'bedingt', 'origin': 'Deutschland', 'rating': 4.6, 'reviews': 780,
        'pros': [
            'Komplette Static Ads (Text, Layout, Bildbearbeitung) — nicht nur Bilder',
            'Branchen-„Angles" als bewährte Aufhänger statt reiner Prompt-Lotterie',
            '10 Ads gratis ohne Kreditkarte zum Testen',
            'Deutscher Anbieter (Made in Germany) mit Impressum/Datenschutz',
        ],
        'cons': [
            'Nur statische Ads — kein Video',
            'Performance-Versprechen laut Anbieter, abhängig von Branche und Produkt',
            'Lernt aus Konto-Daten — Datenfluss der Bildverarbeitung selbst prüfen',
            'Junges Tool, öffentliche Preistabelle wenig transparent',
        ],
        'usecases': [
            'Static Ads für D2C-Brands', 'Ad-Produktion für Agenturen',
            'Meta-Ads-Creatives in Serie', 'On-Brand-Varianten zum Durchtesten',
        ],
        'launched': '2025-02-01', 'lastUpdated': '2026-07-13',
        'website': 'https://www.dooken.de/', 'domain': 'dooken.de',
        'stealth': False,
        'cover_cue': 'A hand-drawn product box on a small ad canvas with a headline bar and a price tag, a thin magenta target-arrow pointing at the product — a complete static ad, not just an image.',
        'features': """- **Static-Ad-Generierung** aus eigenen Produktbildern — komplett mit Text, Layout und Bildbearbeitung.
- **Branchen-„Angles"**: bewährte Problem-Aufhänger, die laut Anbieter in der jeweiligen Branche konvertieren.
- **On-Brand-Varianten** in Minuten zum Durchtesten (A/B).
- **Lernt aus den Daten des eigenen Kontos** und soll sich mit der Zeit verbessern.
- **Fokus auf Performance** (ROAS) statt nur ästhetischer Bilder — laut Anbieter.
- **Made in Germany**, mit Impressum, Datenschutz und AGB.
- **10 Ads gratis** zum Start, ohne Kreditkarte.""",
        'pricing': """- **Gratis-Start** · die ersten 10 Ads kostenlos, ohne Kreditkarte.
- **Kostenpflichtige Pläne** · für laufende Nutzung (Details über den Anbieter).
- **Zielgruppe** · D2C-Brands und Agenturen.
- **60-Sekunden-Setup** laut Anbieter.""",
        'overview': """**Dooken** ist ein **deutscher KI-Generator für Static Ads**, der von seinem Gründer — einem langjährigen Meta-Ads-Media-Buyer — als Einreichung für dieses Verzeichnis vorgeschlagen wurde. Das Tool positioniert sich bewusst neben den bereits gelisteten KI-Ad-Generatoren und setzt einen eigenen Schwerpunkt: nicht nur Bilder, sondern **komplette Werbeanzeigen** aus Produktbildern — mit Text, Layout und Bildbearbeitung in einem.

Der zentrale Anspruch, den der Anbieter formuliert, ist **Performance statt Ästhetik**. Die Argumentation: „Hübsche" KI-Bilder aus generischen Tools kennen weder Marke noch Branche und führen zur „Prompt-Lotterie" — schön anzusehen, aber ohne verlässlichen Return on Ad Spend (ROAS). Dooken arbeitet stattdessen mit **branchenerprobten „Angles"** — bewährten Aufhängern bzw. Blickwinkeln, die laut Anbieter in der jeweiligen Branche konvertieren. Aus einem Produktbild entstehen so **dutzende On-Brand-Varianten in Minuten**, die sich im Testen gegeneinander messen lassen. Das Tool soll zudem **aus den Daten des eigenen Kontos lernen** und sich mit der Zeit verbessern.

Diese Performance-Versprechen sind **Angaben des Anbieters** und sollten als solche gelesen werden: Ob ein bestimmter „Angle" tatsächlich konvertiert, hängt von Branche, Produkt, Zielgruppe und Angebot ab und lässt sich nur im realen Test messen. Der konzeptionelle Fokus — komplette, test-fähige Ad-Varianten statt einzelner hübscher Bilder — ist aber ein sinnvoller Unterschied zu reinen Bildgeneratoren und deckt sich mit der Praxis erfahrener Media-Buyer.

Praktisch niedrigschwellig ist der **Gratis-Einstieg**: Die ersten 10 Ads sind kostenlos und ohne Kreditkarte nutzbar, das Setup dauert laut Anbieter rund 60 Sekunden. Für die laufende Nutzung gibt es kostenpflichtige Pläne; die Zielgruppe sind **D2C-Brands und Agenturen**. Laut eigener Angabe nutzen über 800 Brands das Tool.

Als **deutscher Anbieter** („Made in Germany") mit Impressum, Datenschutzerklärung und AGB ist Dooken datenschutzrechtlich zunächst günstiger positioniert als viele US-Tools — die konkrete Verarbeitung der Produktbilder und der Kontodaten in der KI-Pipeline sollte man dennoch unabhängig prüfen, weshalb der DSGVO-Status hier als „bedingt" geführt wird.

Schwächen: Dooken erzeugt **nur statische Ads**, kein Video. Das **Performance-Versprechen** ist anbieterseitig und produktabhängig. Und das Tool **lernt aus Konto-Daten**, was den Datenfluss zu einem prüfenswerten Punkt macht. Als junges Produkt ist die öffentliche Preistransparenz begrenzt.

Empfohlen für D2C-Brands und Performance-Marketing-Teams, die schnell test-fähige Static-Ad-Varianten aus Produktbildern brauchen und einen deutschen Anbieter mit Performance-Fokus bevorzugen — als Ergänzung oder Alternative zu breiter aufgestellten Ad-Creative-Generatoren. Wer Video-Ads oder eine etablierte Enterprise-Plattform braucht, schaut sich zusätzlich die größeren Anbieter an.""",
    },
]

out = ROOT / 'scripts' / 'pending_tools.json'
out.write_text(json.dumps(TOOLS, ensure_ascii=False, indent=2))
print(f'wrote {len(TOOLS)} records to {out.relative_to(ROOT)}')
for t in TOOLS:
    print(f'  - {t["slug"]:10} {t["category"]:14} ov={len(t["overview"])}c  origin={t["origin"]}')
