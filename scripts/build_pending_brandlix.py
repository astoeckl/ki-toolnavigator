#!/usr/bin/env python3
"""Build scripts/pending_tools.json with Brandlix (AI social media agent)."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent

TOOLS = [
    {
        'slug': 'brandlix', 'name': 'Brandlix',
        'vendor': 'Brandlix', 'category': 'marketing',
        'tagline': 'KI-„Mitarbeiter" für Social Media statt bloßem Redaktionskalender — plant die Woche, schreibt Beiträge plattformgerecht aus dem Markenprofil, erzeugt Bilder/Videos/Karussells und beantwortet DMs und Kommentare, jede Aktion vorab zur Freigabe.',
        'price': 'Kostenloser Tarif · kostenpflichtige Pläne',
        'api': False, 'dsgvo': 'bedingt', 'origin': 'k. A.', 'rating': 4.3, 'reviews': 120,
        'pros': [
            'Agentischer End-to-End-Ansatz: plant, entscheidet, schreibt und postet',
            'Brand-Voice-KI schreibt aus Tonfall, Leistungen und FAQ des Kunden',
            'Erzeugt Bilder, Videos und Karussells selbst; Unified Inbox für DMs/Kommentare',
            'Freigabe-Schritt vor jeder Aktion (optional Full-Autopilot); 10 Plattformen',
        ],
        'cons': [
            'Autonomie erfordert Kontrolle — Qualität hängt stark vom Markenprofil ab',
            'Anbieter macht keine DSGVO-/Hosting-Angaben auf der Website (unabhängig prüfen)',
            'Herkunft/Betreiber öffentlich nicht ausgewiesen',
            'Junges Tool; Zuverlässigkeit je Plattform-API kann schwanken',
        ],
        'usecases': [
            'Social-Media-Betreuung für KMU und Creator', 'Wöchentliche Content-Planung und -Erstellung',
            'Community-Management (DMs/Kommentare)', 'Plattformgerechtes Ausschreiben aus dem Markenprofil',
        ],
        'launched': '2025-03-01', 'lastUpdated': '2026-08-10',
        'website': 'https://brandlix.io', 'domain': 'brandlix.io',
        'stealth': False,
        'cover_cue': 'A hand-drawn small robot figure at a desk arranging several platform tiles into a weekly row, with a tiny approval checkmark above one tile tinted magenta — an AI employee running social media with sign-off.',
        'features': """- **Wochenplanung**: entscheidet, was wann auf welcher Plattform erscheint (kein leerer Kalender).
- **Brand-Voice-KI**: schreibt Beiträge plattformgerecht aus Tonfall, Leistungen und FAQ des Markenprofils.
- **Native Medien-Erzeugung**: Bilder, Videos und Karussells.
- **Unified Inbox**: beantwortet DMs und Kommentare, mit Sentiment-Analyse und Auto-Reply.
- **Freigabe-Workflow**: jede Aktion vorab zur Freigabe — optional „Full Autopilot".
- **10 Plattformen**: u. a. Instagram, LinkedIn, Facebook, TikTok, Pinterest, YouTube, Threads, Bluesky, WordPress.
- **Analytics & Wochenbericht**: Reichweite/Engagement, „Best Time to Post", A/B-Tests, wöchentliche Zusammenfassung.""",
        'pricing': """- **Kostenloser Tarif** · zum Ausprobieren, ohne Kreditkarte, Setup in wenigen Minuten.
- **Kostenpflichtige Pläne** · gestaffelt nach Umfang (Details beim Anbieter, alle mit Free-Trial).
- **Zielgruppe** · Creator, KMU und Agenturen.""",
        'overview': """**Brandlix** positioniert sich als **„KI-Mitarbeiter" für Social Media** — nicht als weiteres Planungs-Tool mit leerem Redaktionskalender, sondern als agentisches System, das den Social-Media-Workflow möglichst vollständig übernimmt: planen, entscheiden, schreiben, gestalten, posten, antworten und berichten. Damit grenzt es sich bewusst von reinen Schedulern wie Buffer oder Hootsuite ab, deren eigentliche Arbeit — das Entscheiden und Schreiben — beim Nutzer bleibt.

Der Kern ist die **Wochenplanung mit Entscheidungslogik**: Brandlix legt fest, was wann auf welcher Plattform erscheint, statt nur leere Slots zu befüllen. Die Inhalte schreibt eine **Brand-Voice-KI** plattformgerecht aus dem Markenprofil des Kunden — Tonfall, Leistungen, FAQ fließen ein, sodass ein LinkedIn-Post anders klingt als ein TikTok-Text, aber beide zur Marke passen.

Für die visuelle Seite erzeugt Brandlix **Bilder, Videos und Karussells selbst**, statt nur Text zu liefern — ein Unterschied zu klassischen Copy-Tools. Auf der Interaktionsseite bündelt eine **Unified Inbox** DMs und Kommentare über alle Kanäle, mit Sentiment-Analyse und Auto-Reply, sodass auch das Community-Management abgedeckt ist. Wöchentlich liefert das System einen **Bericht**, was es getan hat, ergänzt um Analytics wie Reichweite, Engagement, „Best Time to Post" und A/B-Tests.

Wichtig für die Kontrolle: Laut Anbieter geht **jede Aktion vorab zur Freigabe** — der Mensch behält das letzte Wort, bevor etwas veröffentlicht wird. Wer will, kann in einen **Full-Autopilot-Modus** wechseln, in dem Brandlix eigenständig generiert, plant und postet. Unterstützt werden **zehn Plattformen** (u. a. Instagram, LinkedIn, Facebook, TikTok, Pinterest, YouTube, Threads, Bluesky, WordPress). Ein **kostenloser Tarif** erlaubt das Ausprobieren ohne Kreditkarte.

Bei den Grenzen ist Ehrlichkeit angebracht. Der **agentische Anspruch** ist zugleich das Risiko: Ein System, das eigenständig entscheidet und schreibt, ist nur so gut wie das hinterlegte Markenprofil und die menschliche Kontrolle im Freigabe-Schritt — ungeprüfter Full-Autopilot auf zehn Kanälen kann off-brand oder unpassend werden. Beim **Datenschutz** macht die Website keine konkreten DSGVO- oder Hosting-Angaben, und **Herkunft bzw. Betreiber** sind öffentlich nicht ausgewiesen; wer personenbezogene Daten oder Kundeninhalte verarbeitet, sollte den DSGVO-Status daher unabhängig klären (der Anbieter signalisiert Bereitschaft, dazu offen Auskunft zu geben). Als **junges Tool** hängt die Zuverlässigkeit zudem von den jeweiligen Plattform-APIs ab, die sich häufig ändern.

Empfohlen für Creator, KMU und kleine Agenturen, die Social Media nicht nur einplanen, sondern **erstellen und betreuen** lassen wollen — und die den Freigabe-Schritt konsequent nutzen. Der kostenlose Tarif macht einen eigenen Eindruck risikolos möglich; die Datenschutz-Eignung für den konkreten Einsatz sollte man vorab selbst bewerten.""",
    },
]

out = ROOT / 'scripts' / 'pending_tools.json'
out.write_text(json.dumps(TOOLS, ensure_ascii=False, indent=2))
print(f'wrote {len(TOOLS)} record(s) to {out.relative_to(ROOT)}')
for t in TOOLS:
    print(f'  - {t["slug"]:10} {t["category"]:10} ov={len(t["overview"])}c')
