#!/usr/bin/env python3
"""Build scripts/pending_tools.json with 7 additional marketing AI tools."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent

TOOLS = [
    {
        'slug': 'hubspot-breeze', 'name': 'HubSpot Breeze',
        'vendor': 'HubSpot', 'category': 'marketing',
        'tagline': 'HubSpots KI-Schicht über dem CRM — Breeze Copilot, spezialisierte Breeze Agents und Breeze Intelligence für Marketing, Sales und Service in einer Plattform.',
        'price': 'In HubSpot-Tarifen enthalten · Credits für Agents',
        'api': True, 'dsgvo': 'bedingt', 'origin': 'USA', 'rating': 4.4, 'reviews': 6820,
        'pros': [
            'Tief im HubSpot-CRM verankert — Daten als Kontext out-of-the-box',
            'Spezialisierte Agents (Content, Social, Prospecting, Customer)',
            'Breeze Intelligence reichert Kontakte und Firmen automatisch an',
            'EU-Datenresidenz für HubSpot-Daten verfügbar',
        ],
        'cons': [
            'Voller Nutzen nur mit HubSpot als CRM',
            'Agent-Credits können bei hohem Volumen teuer werden',
            'Funktionstiefe einzelner Agents hinter Spezial-Tools',
            'Lock-in an das HubSpot-Ökosystem',
        ],
        'usecases': [
            'Content- und Social-Erstellung im CRM', 'Lead-Anreicherung und Prospecting',
            'Marketing-Kampagnen-Automation', 'Kundenservice-Agents',
        ],
        'launched': '2024-09-18', 'lastUpdated': '2026-06-20',
        'website': 'https://www.hubspot.com/products/artificial-intelligence', 'domain': 'hubspot.com',
        'stealth': False,
        'cover_cue': 'A hand-drawn central hub circle with several spokes ending in small task-icons (content, social, lead), one spoke tinted magenta — an AI layer woven through a CRM.',
        'features': """- **Breeze Copilot**: konversationeller Assistent im gesamten HubSpot-CRM.
- **Breeze Agents**: spezialisierte Agents für Content, Social, Prospecting und Customer.
- **Breeze Intelligence**: automatische Anreicherung von Kontakten und Firmen mit Buyer-Intent.
- **Content-Erstellung** für Blog, E-Mail, Landing-Pages und Ads im Markenton.
- **Workflow-Automation** mit KI-Triggern und -Aktionen.
- **Native CRM-Daten** als Kontext für jede Generierung.
- **EU-Datenresidenz** für HubSpot-Daten optional.""",
        'pricing': """- **HubSpot-Tarife** · Breeze-Grundfunktionen in Marketing/Sales/Service Hub enthalten.
- **Starter** · ab ca. 15 € / Sitz / Mon. mit Breeze-Basics.
- **Professional / Enterprise** · volle Agent- und Intelligence-Funktionen.
- **Breeze Credits** für Agent-Aktionen und Intelligence-Anreicherung.
- **Free CRM** · limitierte Breeze-Funktionen.""",
        'overview': """**HubSpot Breeze** ist die KI-Schicht, die HubSpot 2024 über sein gesamtes CRM gelegt und seitdem kontinuierlich ausgebaut hat. Statt einzelner KI-Features bündelt HubSpot unter der Marke „Breeze" drei Ebenen: **Breeze Copilot** (ein konversationeller Assistent im ganzen Produkt), **Breeze Agents** (spezialisierte, teilautonome Agents) und **Breeze Intelligence** (Daten-Anreicherung und Buyer-Intent). Für die große Zahl an Unternehmen, die HubSpot ohnehin als Marketing- und Sales-CRM nutzen, ist das der kürzeste Weg zu produktiver KI.

Der entscheidende Vorteil ist der **Kontext aus dem CRM**. Breeze hat out-of-the-box Zugriff auf Kontakte, Deals, E-Mail-Verläufe, Tickets und Kampagnen — als strukturierte Daten mit Beziehungswissen. Was bei generischen KI-Tools ein eigener Daten-Integrationsaufwand wäre, ist hier konstitutiv: Der Content-Agent kennt die Zielgruppe, der Prospecting-Agent kennt die Pipeline, der Customer-Agent kennt die Ticket-Historie.

Die **Breeze Agents** sind das Herzstück der aktuellen Ausbaustufe. Der **Content Agent** erstellt Blogposts, Landing-Pages, Case Studies und E-Mails im Markenton; der **Social Agent** plant und schreibt Social-Posts; der **Prospecting Agent** recherchiert Leads und entwirft Outreach-Sequenzen; der **Customer Agent** beantwortet Support-Anfragen autonom. Sie arbeiten teilautonom und greifen auf CRM-Daten und Marken-Richtlinien zurück.

**Breeze Intelligence** ist die Daten-Ebene: Kontakte und Firmen werden automatisch mit Firmographics, Buyer-Intent-Signalen und fehlenden Feldern angereichert — vergleichbar mit dedizierten Enrichment-Tools, aber direkt im CRM. Für Marketing- und Sales-Teams, die Lead-Scoring und Segmentierung betreiben, spart das einen separaten Datendienst.

Strategisch ist der **EU-Datenresidenz**-Aspekt relevant: HubSpot bietet europäische Daten-Hosting-Optionen, was Breeze für DSGVO-bewusste Unternehmen zugänglicher macht als rein US-gehostete Punktlösungen — auch wenn die KI-Verarbeitung selbst genauer geprüft werden sollte.

Schwächen ergeben sich aus der Plattform-Bindung. Der **volle Nutzen** entsteht nur, wenn HubSpot das zentrale CRM ist — wer Salesforce oder ein anderes System nutzt, verschenkt den Kontext-Vorteil. Die **Agent-Credits** können bei hohem Volumen ins Geld gehen, und die **Funktionstiefe** einzelner Agents (etwa bei der Content-Qualität) liegt hinter spezialisierten Tools wie Jasper oder Copy.ai. Und es bleibt ein **Lock-in** an das HubSpot-Ökosystem.

Empfohlen für Unternehmen, die HubSpot bereits als Marketing-/Sales-/Service-CRM einsetzen und KI ohne separates Tool-Stack-Projekt direkt im Arbeitsfluss wollen. Für Teams ohne HubSpot oder mit höchsten Ansprüchen an eine einzelne Disziplin sind spezialisierte Punktlösungen die bessere Wahl.""",
    },
    {
        'slug': 'adcreative', 'name': 'AdCreative.ai',
        'vendor': 'AdCreative.ai', 'category': 'marketing',
        'tagline': 'KI-Generator für konversionsstarke Werbeanzeigen — Banner, Social-Ad-Creatives und Produktfotos in Marken-Stil, mit Conversion-Score und Performance-Daten.',
        'price': 'Ab $39 / Mon. · gestaffelt nach Credits',
        'api': True, 'dsgvo': 'bedingt', 'origin': 'USA', 'rating': 4.4, 'reviews': 7240,
        'pros': [
            'Schnelle, markenkonforme Ad-Creatives in vielen Formaten',
            'Conversion-Score sagt erwartete Performance voraus',
            'Brand-Kit hält Logo, Farben und Schrift konsistent',
            'Direkte Anbindung an Meta/Google Ads',
        ],
        'cons': [
            'Credit-Pricing wird bei hohem Volumen teuer',
            'Creatives wirken teils generisch ohne manuelle Nacharbeit',
            'Conversion-Score ist Heuristik, kein garantierter Erfolg',
            'Datenresidenz USA',
        ],
        'usecases': [
            'Performance-Ad-Creatives für Meta/Google', 'Banner-Sets in vielen Größen',
            'Produktfoto-Generierung', 'A/B-Test-Varianten in Serie',
        ],
        'launched': '2021-06-15', 'lastUpdated': '2026-06-20',
        'website': 'https://www.adcreative.ai/', 'domain': 'adcreative.ai',
        'stealth': False,
        'cover_cue': 'A hand-drawn ad banner rectangle with a small upward conversion-arrow and a star-rating, the arrow tinted magenta — performance ad creative scored for conversion.',
        'features': """- **Ad-Creative-Generierung** für Social, Display und Banner in vielen Formaten.
- **Conversion-Score**: KI-Bewertung der erwarteten Performance pro Creative.
- **Brand-Kit** für konsistente Logos, Farben und Schriften.
- **Produktfoto-Generierung** und Hintergrund-Austausch.
- **Text-/Headline-Generierung** passend zum Creative.
- **Integrationen** mit Meta Ads, Google Ads, Shopify.
- **API** für Creative-Generierung in eigenen Workflows.""",
        'pricing': """- **Starter** · ab $39 / Mon. — begrenzte Credits, ein Brand.
- **Premium** · ca. $149 / Mon. — mehr Credits, mehrere Brands.
- **Scale / Ultimate** · ab $299 / Mon. — hohe Volumen, Team-Funktionen.
- **Credits** = generierte Creatives; Pläne staffeln nach Volumen.
- **API** in höheren Tarifen, Enterprise auf Anfrage.""",
        'overview': """**AdCreative.ai** ist einer der populärsten KI-Generatoren für **Werbeanzeigen** — gestartet 2021 und seitdem zu einem festen Werkzeug vieler Performance-Marketing-Teams geworden. Der Fokus ist eng und klar: schnell viele markenkonforme Ad-Creatives produzieren, die auf Conversion optimiert sind — nicht künstlerische Bilder, sondern verkaufende Anzeigen.

Der **Workflow** ist auf Geschwindigkeit ausgelegt. Nach dem Anlegen eines **Brand-Kits** (Logo, Farben, Schriften) generiert AdCreative.ai aus einem Produkt oder einer Kampagnen-Beschreibung dutzende Creative-Varianten in allen relevanten Formaten — Quadrat für Feed, Hochformat für Stories/Reels, Banner für Display. Was manuell Stunden im Design-Tool wäre, sind hier Minuten.

Das namensgebende Differenzierungsmerkmal ist der **Conversion-Score**: Eine KI bewertet jedes generierte Creative nach erwarteter Performance, basierend auf einem Trainingsdatensatz erfolgreicher Anzeigen. Das hilft Teams, aus dutzenden Varianten die vielversprechendsten vorzuselektieren, bevor Budget in Tests fließt. Wichtig: Der Score ist eine **Heuristik**, kein garantierter Erfolg — die reale Performance entscheidet weiter der Markt.

Über die reine Bild-Generierung hinaus bietet AdCreative.ai **Headline- und Text-Generierung** passend zum Creative, **Produktfoto-Generierung** mit Hintergrund-Austausch und direkte **Integrationen** zu Meta Ads, Google Ads und Shopify — so wandern Creatives ohne Umweg in die Kampagne. Eine **API** erlaubt die Generierung in eigenen Workflows, etwa für E-Commerce-Kataloge mit tausenden Produkten.

Schwächen sind typisch für das Segment. Das **Credit-Pricing** wird bei hohem Output teuer — wer täglich hunderte Creatives generiert, landet schnell in den oberen Tarifen. Die Creatives wirken **ohne manuelle Nacharbeit teils generisch** — als Ausgangspunkt stark, für Premium-Marken oft nachbearbeitungsbedürftig. Und die **Datenresidenz** liegt in den USA.

Empfohlen für Performance-Marketing-Teams, E-Commerce-Marken und Agenturen, die in Serie konversionsorientierte Ad-Creatives brauchen und Varianten schnell testen wollen. Für hochwertige Brand-Kampagnen mit eigenem Look ergänzt es das Design-Team, ersetzt es aber nicht.""",
    },
    {
        'slug': 'clay', 'name': 'Clay',
        'vendor': 'Clay', 'category': 'marketing',
        'tagline': 'GTM-Plattform für Daten-Anreicherung und KI-Outbound — kombiniert 100+ Datenquellen mit KI-Research-Agents, um Leads anzureichern und hochpersonalisierte Kampagnen zu bauen.',
        'price': 'Free-Tier · Pro ab $149 / Mon. (Credits)',
        'api': True, 'dsgvo': 'bedingt', 'origin': 'USA', 'rating': 4.7, 'reviews': 3940,
        'pros': [
            '100+ Enrichment-Quellen in einem Waterfall kombinierbar',
            'KI-Research-Agent „Claygent" recherchiert pro Lead im Web',
            'Hochpersonalisierte Outbound-Nachrichten in Serie',
            'Sehr flexibel, tabellen-basiert, mit großer Community',
        ],
        'cons': [
            'Steile Lernkurve — mächtig, aber komplex',
            'Credit-Pricing kann schnell eskalieren',
            'Datenqualität schwankt je Quelle',
            'Datenresidenz USA, DSGVO-Sorgfalt bei Outbound nötig',
        ],
        'usecases': [
            'Lead-Listen anreichern und scoren', 'Personalisierte Outbound-Kampagnen',
            'GTM-Datenpipelines bauen', 'Account-Research automatisieren',
        ],
        'launched': '2021-01-19', 'lastUpdated': '2026-06-20',
        'website': 'https://www.clay.com/', 'domain': 'clay.com',
        'stealth': False,
        'cover_cue': 'A hand-drawn spreadsheet grid where several columns flow in from different source-pipes and merge into one enriched row, one cell tinted magenta — waterfall data enrichment.',
        'features': """- **Waterfall-Enrichment** über 100+ Datenquellen (Apollo, LinkedIn, Clearbit u.v.m.).
- **Claygent**: KI-Research-Agent, der pro Zeile das Web durchsucht.
- **Tabellen-Interface** mit Formeln, Spalten und Integrationen.
- **Personalisierte Nachrichten** in Serie generieren.
- **CRM-Sync** (HubSpot, Salesforce) und Outreach-Tools.
- **Templates** und große Community-Bibliothek.
- **API** und Webhooks für eigene Pipelines.""",
        'pricing': """- **Free** · begrenzte Credits zum Ausprobieren.
- **Starter** · ca. $149 / Mon. — mehr Credits, Kern-Enrichment.
- **Pro** · ca. $349 / Mon. — Claygent, höhere Volumen.
- **Enterprise** · auf Anfrage — SSO, höhere Limits, Support.
- **Credits** = Enrichment-/KI-Aktionen; Volumen treibt den Preis.""",
        'overview': """**Clay** ist die in den letzten Jahren am schnellsten gewachsene **GTM-Daten-Plattform** (Go-to-Market) — gestartet 2021 und 2025/26 zum De-facto-Standard für datengetriebenes, KI-gestütztes Outbound geworden. Im Kern ist Clay eine extrem flexible, tabellenbasierte Oberfläche, die Daten-Anreicherung, Web-Research und KI-Generierung in einem Workflow vereint.

Das namensgebende Konzept ist das **Waterfall-Enrichment**: Statt sich auf eine einzige Datenquelle zu verlassen, kombiniert Clay über 100 Anbieter (Apollo, LinkedIn, Clearbit, Hunter und viele mehr) in einer Kaskade — fehlt eine E-Mail bei Quelle A, fragt Clay automatisch Quelle B, dann C. Das hebt die Trefferquote bei Kontaktdaten deutlich über das, was eine Einzelquelle liefert. Für Sales- und Marketing-Teams, die saubere, vollständige Lead-Listen brauchen, ist das der zentrale Mehrwert.

Die KI-Komponente ist **Claygent** — ein Research-Agent, der für jede Zeile einer Tabelle eigenständig das Web durchsucht und Fragen beantwortet: „Welche Tech-Stack nutzt diese Firma?", „Hat das Unternehmen kürzlich eine Finanzierung erhalten?", „Wer ist die für X zuständige Person?". Diese recherchierten Signale fließen direkt in die Personalisierung ein.

Daraus entsteht der eigentliche Anwendungsfall: **hochpersonalisiertes Outbound in Serie**. Clay reichert eine Lead-Liste an, recherchiert pro Account relevante Trigger und generiert dann personalisierte Nachrichten, die echte Recherche statt generischer Platzhalter nutzen — und synchronisiert das Ergebnis nach HubSpot, Salesforce oder in ein Outreach-Tool.

Die **Flexibilität** ist Clays Stärke und Schwäche zugleich. Das Tabellen-Interface mit Formeln, Spalten-Integrationen und Webhooks ist mächtig genug für komplexe GTM-Pipelines — aber die **Lernkurve ist steil**. Clay hat eine große, aktive Community mit Templates, die den Einstieg erleichtert, aber Gelegenheitsnutzer:innen sind anfangs überfordert.

Weitere Schwächen: Das **Credit-Pricing** kann schnell eskalieren, weil jede Enrichment- und KI-Aktion zählt — große Kampagnen werden teuer. Die **Datenqualität** schwankt je Quelle (das Waterfall mildert das, eliminiert es aber nicht). Und bei **Outbound** ist DSGVO-Sorgfalt geboten: Datenresidenz USA, und kaltes E-Mail-Outreach an EU-Kontakte unterliegt strengen Regeln, die Clay nicht automatisch löst.

Empfohlen für Sales- und Marketing-/RevOps-Teams, die datengetriebenes Outbound und saubere, angereicherte Lead-Listen brauchen und bereit sind, sich in ein mächtiges Werkzeug einzuarbeiten. Für einfache Anwendungsfälle ist Clay überdimensioniert; seine Stärke entfaltet sich bei anspruchsvollen, personalisierten GTM-Pipelines.""",
    },
    {
        'slug': 'mutiny', 'name': 'Mutiny',
        'vendor': 'Mutiny', 'category': 'marketing',
        'tagline': 'KI-gestützte Website-Personalisierung für B2B — erstellt maßgeschneiderte Landing-Pages und Account-spezifische Erlebnisse ohne Entwickler, optimiert auf Pipeline statt Klicks.',
        'price': 'Enterprise · Pricing auf Anfrage',
        'api': True, 'dsgvo': 'bedingt', 'origin': 'USA', 'rating': 4.5, 'reviews': 980,
        'pros': [
            'No-Code-Website-Personalisierung nach Branche, Firma, Quelle',
            'KI generiert ganze Account-spezifische Landing-Pages',
            'Auf Pipeline/Revenue optimiert, nicht nur auf Klicks',
            'Tiefe Integration mit CRM und ABM-Stack',
        ],
        'cons': [
            'Enterprise-Pricing, für kleine Teams kaum zugänglich',
            'Voller Nutzen erst mit hohem Traffic und ABM-Strategie',
            'Setup und Datenanbindung aufwändig',
            'Datenresidenz USA',
        ],
        'usecases': [
            'B2B-Website-Personalisierung', 'Account-spezifische Landing-Pages (ABM)',
            'Conversion-Optimierung nach Segment', 'Personalisierte Kampagnen-Ziele',
        ],
        'launched': '2020-04-01', 'lastUpdated': '2026-06-20',
        'website': 'https://www.mutinyhq.com/', 'domain': 'mutinyhq.com',
        'stealth': False,
        'cover_cue': 'A hand-drawn browser window that splits into three tailored variants fanning out, each with a different small visitor-icon, one variant tinted magenta — website personalization by audience.',
        'features': """- **No-Code-Personalisierung** der Website nach Branche, Firmengröße, Quelle, Account.
- **KI-Landing-Page-Generierung** für einzelne Accounts (1:1-ABM).
- **Audience-Builder** mit Firmographics und Intent-Daten.
- **Playbooks** für bewährte Personalisierungs-Muster.
- **A/B-Testing** auf Conversion und Pipeline.
- **Integrationen** mit Salesforce, HubSpot, 6sense, Clearbit.
- **Analytics** auf Revenue-Beitrag statt nur Klicks.""",
        'pricing': """- **Enterprise** · individuelles Pricing nach Traffic und Funktionsumfang.
- **Kein öffentlicher Self-Service-Tarif** — Demo/Sales-Prozess.
- **Onboarding** und Customer-Success im Paket.
- **Add-ons** für KI-Generierung und zusätzliche Integrationen.""",
        'overview': """**Mutiny** ist eine Plattform für **KI-gestützte Website-Personalisierung im B2B** — gestartet 2020 und etabliert als eines der bekanntesten Werkzeuge im Account-Based-Marketing (ABM). Die Grundidee: Eine statische Website zeigt allen Besucher:innen dasselbe, obwohl ein Fortune-500-CFO und ein Startup-Gründer völlig unterschiedliche Botschaften brauchen. Mutiny macht die Website **dynamisch** — ohne dass Entwickler:innen für jede Variante Code schreiben.

Der **No-Code-Ansatz** ist das Kernversprechen. Marketer:innen definieren Zielgruppen — nach Branche, Firmengröße, Traffic-Quelle, bekanntem Account — und passen für jede Gruppe Überschriften, Texte, Bilder, Call-to-Actions und ganze Seitenabschnitte an. Ein Besucher aus dem Finanzsektor sieht Finanz-Sprache und passende Logos, ein Tech-Besucher etwas anderes. Das geschieht über eine visuelle Oberfläche, nicht im Code.

Die KI-Ausbaustufe geht weiter: Mutiny generiert mittlerweile **ganze Account-spezifische Landing-Pages** für 1:1-ABM-Kampagnen. Für eine Liste von Ziel-Accounts entstehen automatisch maßgeschneiderte Seiten, die den Firmennamen, relevante Use-Cases und passende Referenzen enthalten — Personalisierung, die manuell nicht skalierbar wäre.

Der entscheidende konzeptionelle Unterschied zu klassischen A/B-Test-Tools ist die **Optimierungs-Metrik**: Mutiny misst nicht nur Klicks oder oberflächliche Conversions, sondern den Beitrag zur **Pipeline und zum Revenue**. Das passt zur B2B-Realität, in der ein Lead erst Monate später zu Umsatz wird, und macht die Ergebnisse für Sales-orientierte Organisationen glaubwürdiger.

Die **Integrationen** sind entsprechend B2B-lastig: Salesforce, HubSpot, 6sense, Clearbit und andere ABM-/Intent-Datenquellen speisen die Zielgruppen-Definitionen. **Playbooks** liefern bewährte Personalisierungs-Muster als Startpunkt.

Die Schwächen sind die einer Enterprise-Plattform. Das **Pricing** ist individuell und enterprise-orientiert — für kleine Teams kaum zugänglich, kein öffentlicher Self-Service-Tarif. Der **volle Nutzen** entsteht erst bei substanziellem Website-Traffic und einer echten ABM-Strategie; ohne genug Besucher pro Segment fehlt die statistische Basis. **Setup und Datenanbindung** sind aufwändig, und die **Datenresidenz** liegt in den USA.

Empfohlen für B2B-Marketing-Teams mit ABM-Strategie, nennenswertem Website-Traffic und der Notwendigkeit, unterschiedliche Zielgruppen differenziert anzusprechen. Für kleine Websites oder B2C ohne Account-Logik ist Mutiny überdimensioniert.""",
    },
    {
        'slug': 'persado', 'name': 'Persado',
        'vendor': 'Persado', 'category': 'marketing',
        'tagline': 'Enterprise-KI für Sprach- und Message-Optimierung — generiert und testet markenkonforme, conversion-optimierte Werbebotschaften, mit Fokus auf regulierte Branchen.',
        'price': 'Enterprise · Pricing auf Anfrage',
        'api': True, 'dsgvo': 'bedingt', 'origin': 'USA', 'rating': 4.3, 'reviews': 540,
        'pros': [
            'Auf Daten von Milliarden Marketing-Interaktionen trainiert',
            'Compliance-/Brand-Guardrails für regulierte Branchen',
            'Messbarer Uplift durch sprachliche Optimierung',
            'Integration in bestehende CRM-/Kampagnen-Kanäle',
        ],
        'cons': [
            'Reines Enterprise-Produkt, hohe Einstiegshürde',
            'Fokus auf Message-Optimierung, kein Allround-Tool',
            'Setup und Daten-Anbindung aufwändig',
            'Datenresidenz USA',
        ],
        'usecases': [
            'E-Mail- und SMS-Botschaften optimieren', 'Conversion-Copy für regulierte Branchen',
            'Sprach-Tests in großem Maßstab', 'Markenkonforme Kampagnen-Texte',
        ],
        'launched': '2012-09-01', 'lastUpdated': '2026-06-20',
        'website': 'https://www.persado.com/', 'domain': 'persado.com',
        'stealth': False,
        'cover_cue': 'A hand-drawn balance scale weighing two speech bubbles of words, the heavier winning bubble tinted magenta — language optimized for conversion within guardrails.',
        'features': """- **Generative Message-Optimierung** für E-Mail, SMS, Web, Push und Ads.
- **Trainiert auf Milliarden** realer Marketing-Interaktionen.
- **Compliance- und Brand-Guardrails** für regulierte Branchen (Finanz, Pharma).
- **Sprach-Tests** mit gemessenem Conversion-Uplift.
- **Tone- und Emotion-Steuerung** pro Zielgruppe.
- **Integration** in CRM, ESP und Kampagnen-Tools.
- **Agentic-Creative-Workflows** (neuere Ausbaustufe).""",
        'pricing': """- **Enterprise** · individuelles Pricing nach Volumen und Kanälen.
- **Kein Self-Service** — Demo- und Sales-Prozess.
- **Onboarding**, Modell-Tuning und Customer-Success im Paket.
- **Branchen-Pakete** für Finanz, Versicherung, Pharma, Retail.""",
        'overview': """**Persado** ist ein Enterprise-Pionier der **KI-gestützten Sprach- und Message-Optimierung** — bereits 2012 gegründet und damit lange vor der aktuellen Generative-AI-Welle aktiv. Der Fokus ist spezifisch: Nicht Bilder oder ganze Kampagnen, sondern die **Wörter selbst** — Betreffzeilen, Call-to-Actions, Werbebotschaften — werden generiert, getestet und auf Conversion optimiert.

Die Grundlage ist ein über Jahre aufgebauter **Datensatz aus Milliarden realer Marketing-Interaktionen**. Persado weiß aus diesen Daten, welche sprachlichen Formulierungen, emotionalen Töne und Strukturen in welchem Kontext besser konvertieren. Daraus generiert das System Botschafts-Varianten und sagt deren Performance voraus — und der gemessene **Conversion-Uplift** gegenüber von Menschen geschriebenen Botschaften ist Persados zentrales Verkaufsargument.

Der strategisch wichtigste Differenzierer ist der Fokus auf **regulierte Branchen**. Banken, Versicherungen und Pharma-Unternehmen dürfen nicht beliebig formulieren — es gibt rechtliche und Compliance-Grenzen für Werbeaussagen. Persado baut **Compliance- und Brand-Guardrails** ein, sodass generierte Botschaften innerhalb der erlaubten Sprache bleiben. Genau das macht das Tool für große, regulierte Organisationen attraktiv, die generischen Text-Generatoren aus Compliance-Gründen nicht trauen können.

Die **Tone- und Emotion-Steuerung** erlaubt es, Botschaften pro Zielgruppe zu variieren — dringlicher, vertrauensbildender, exklusiver — und die Wirkung zu messen. In der neueren Ausbaustufe positioniert sich Persado zunehmend als **agentische Creative-Plattform**, die ganze Botschafts-Workflows orchestriert statt einzelner Texte.

Die **Integration** läuft über bestehende Kanäle: CRM, E-Mail-Service-Provider, Push- und SMS-Systeme. Persado ersetzt nicht den Versand, sondern optimiert die Inhalte, die durch diese Kanäle gehen.

Die Schwächen sind die eines fokussierten Enterprise-Produkts. Persado ist **kein Allround-Tool** — es optimiert Botschaften, generiert aber keine Bilder, Landing-Pages oder Social-Strategien. Die **Einstiegshürde** ist hoch: Enterprise-Pricing, Sales-Prozess, aufwändiges Onboarding und Daten-Anbindung. Für kleine und mittlere Unternehmen ist es praktisch nicht zugänglich. Die **Datenresidenz** liegt in den USA.

Empfohlen für große Marketing-Organisationen — besonders in regulierten Branchen wie Finanzdienstleistung, Versicherung und Pharma — die Botschaften über E-Mail, SMS und Web in großem Maßstab sprachlich optimieren und dabei Compliance sicherstellen müssen. Für allgemeines Content-Marketing sind flexible Generatoren wie Jasper oder Copy.ai passender.""",
    },
    {
        'slug': 'smartly', 'name': 'Smartly',
        'vendor': 'Smartly', 'category': 'marketing',
        'tagline': 'KI-Werbeplattform aus Finnland — automatisiert Creative-Produktion, Media-Buying und Optimierung für Paid Social und Display über alle großen Kanäle hinweg.',
        'price': 'Enterprise · Pricing auf Anfrage',
        'api': True, 'dsgvo': 'ja', 'origin': 'Finnland', 'rating': 4.3, 'reviews': 1320,
        'pros': [
            'End-to-End: Creative, Media-Buying und Optimierung in einer Plattform',
            'KI-Creative-Skalierung über Meta, TikTok, Google, Pinterest u.v.m.',
            'EU-Anbieter (Helsinki) mit DSGVO-Konformität',
            'Starke Automatisierung für große Werbebudgets',
        ],
        'cons': [
            'Enterprise-Pricing, für kleine Budgets ungeeignet',
            'Komplexe Plattform mit Einarbeitungsaufwand',
            'Voller Nutzen erst bei hohem Ad-Spend',
            'Weniger geeignet für Einzel-Creatives',
        ],
        'usecases': [
            'Paid-Social-Kampagnen at Scale', 'Automatisierte Creative-Produktion',
            'Cross-Channel-Media-Buying', 'Performance-Optimierung großer Budgets',
        ],
        'launched': '2013-05-01', 'lastUpdated': '2026-06-20',
        'website': 'https://www.smartly.io/', 'domain': 'smartly.io',
        'stealth': False,
        'cover_cue': 'A hand-drawn fan of ad cards being auto-arranged across several channel-icons by a thin robotic arm, one card tinted magenta — automated cross-channel advertising.',
        'features': """- **Creative-Automatisierung**: dynamische Ad-Varianten aus Vorlagen und Feeds.
- **Media-Buying** über Meta, TikTok, Google, Pinterest, Snap u.v.m.
- **KI-Optimierung** von Budget, Gebot und Creative in Echtzeit.
- **Dynamic Product Ads** aus Produktkatalogen.
- **Reporting** über alle Kanäle hinweg vereint.
- **Brand-Konsistenz** über Templates und Asset-Management.
- **EU-Hosting** und DSGVO-Konformität.""",
        'pricing': """- **Enterprise** · Pricing nach Ad-Spend und Modulen.
- **Kein Self-Service** — Demo- und Sales-Prozess.
- **Module** für Creative, Media-Buying und Analytics kombinierbar.
- **Managed-Service-Optionen** für große Werbetreibende.""",
        'overview': """**Smartly** (vormals Smartly.io) ist eine **KI-Werbeplattform aus Finnland** — 2013 in Helsinki gegründet und zu einem der führenden Anbieter für die Automatisierung von Paid-Social- und Display-Werbung in großem Maßstab geworden. Anders als Punktlösungen, die nur Creatives generieren, deckt Smartly den **gesamten Werbe-Lebenszyklus** ab: Creative-Produktion, Media-Buying und Optimierung in einer Plattform.

Die **Creative-Automatisierung** ist die erste Säule. Aus Vorlagen, Produktkatalogen und Daten-Feeds generiert Smartly dynamisch dutzende bis tausende Ad-Varianten — angepasst an Format, Zielgruppe und Kanal. Für Werbetreibende mit großen Produktsortimenten (E-Commerce, Reise, Retail) bedeutet das, dass jede Produktvariante automatisch ihr passendes Creative bekommt, ohne manuelle Design-Arbeit pro Anzeige.

Die zweite Säule ist das **Media-Buying** über alle großen Kanäle: Meta, TikTok, Google, Pinterest, Snapchat und weitere. Statt jeden Kanal separat in dessen eigenem Werbe-Manager zu bedienen, orchestriert Smartly Kampagnen kanalübergreifend aus einer Oberfläche — mit vereintem Reporting, das den fragmentierten Blick der einzelnen Plattform-Dashboards ersetzt.

Die dritte Säule ist die **KI-Optimierung**: Budget-Allokation, Gebote und Creative-Auswahl werden in Echtzeit auf Performance optimiert. Schlecht laufende Varianten werden automatisch zurückgefahren, gut laufende skaliert — kontinuierlich und über Kanäle hinweg.

Strategisch relevant ist die **EU-Herkunft**: Als finnischer Anbieter mit EU-Hosting ist Smartly für europäische Werbetreibende, die Wert auf DSGVO-Konformität und einen EU-Vertragspartner legen, eine naheliegende Wahl gegenüber rein US-amerikanischen Plattformen — ein echtes Unterscheidungsmerkmal in diesem von US-Anbietern dominierten Segment.

Die Schwächen ergeben sich aus der Enterprise-Ausrichtung. Das **Pricing** orientiert sich am Ad-Spend und ist für kleine Budgets ungeeignet — Smartly lohnt sich erst bei substanziellen Werbeausgaben. Die **Plattform ist komplex** und erfordert Einarbeitung; sie ist auf Teams ausgelegt, nicht auf Einzelpersonen. Und für die Produktion **einzelner Creatives** ohne Media-Buying-Bedarf ist sie überdimensioniert — dafür sind Tools wie AdCreative.ai passender.

Empfohlen für große Werbetreibende und Agenturen, die Paid-Social- und Display-Kampagnen über mehrere Kanäle mit hohem Budget automatisiert produzieren, ausspielen und optimieren wollen — und für europäische Teams, die einen DSGVO-konformen EU-Anbieter bevorzugen.""",
    },
    {
        'slug': 'brandwatch', 'name': 'Brandwatch',
        'vendor': 'Brandwatch (Cision)', 'category': 'marketing',
        'tagline': 'KI-Plattform für Social Listening und Consumer Intelligence — analysiert Millionen Online-Gespräche in Echtzeit und verbindet sie mit Social-Media-Management.',
        'price': 'Enterprise · Pricing auf Anfrage',
        'api': True, 'dsgvo': 'bedingt', 'origin': 'Großbritannien', 'rating': 4.2, 'reviews': 2480,
        'pros': [
            'Sehr breite Datenabdeckung über soziale Medien und Web',
            'KI-Assistent „Iris" fasst Trends und Sentiment zusammen',
            'Social Listening und Social Management in einer Suite',
            'Etabliert, mit starkem Reporting und Dashboards',
        ],
        'cons': [
            'Enterprise-Pricing, hohe Einstiegshürde',
            'Komplexe Oberfläche mit Lernkurve',
            'Datenqualität und -abdeckung je Plattform unterschiedlich',
            'Setup und Query-Aufbau zeitaufwändig',
        ],
        'usecases': [
            'Social Listening und Markenbeobachtung', 'Sentiment- und Trend-Analyse',
            'Krisen-Früherkennung', 'Wettbewerbs- und Marktforschung',
        ],
        'launched': '2007-01-01', 'lastUpdated': '2026-06-20',
        'website': 'https://www.brandwatch.com/', 'domain': 'brandwatch.com',
        'stealth': False,
        'cover_cue': 'A hand-drawn radar-circle picking up many small chat-bubble blips from across a network, one blip tinted magenta — listening to online conversations at scale.',
        'features': """- **Social Listening** über soziale Medien, News, Blogs und Foren.
- **Iris**: KI-Assistent, der Trends, Sentiment und Anomalien zusammenfasst.
- **Consumer Intelligence** mit Segment- und Demografie-Analyse.
- **Social-Media-Management** (Publishing, Engagement) in derselben Suite.
- **Echtzeit-Alerts** zur Krisen-Früherkennung.
- **Dashboards und Reporting** für Stakeholder.
- **Bild- und Logo-Erkennung** in Social-Posts.""",
        'pricing': """- **Enterprise** · Pricing nach Datenvolumen und Modulen.
- **Kein Self-Service** — Demo- und Sales-Prozess.
- **Module**: Listening, Consumer Intelligence, Social Management einzeln/kombiniert.
- **Teil der Cision-Gruppe** mit PR-/Media-Monitoring-Erweiterungen.""",
        'overview': """**Brandwatch** ist eine der etabliertesten Plattformen für **Social Listening und Consumer Intelligence** — bereits 2007 in Großbritannien gegründet und heute Teil der Cision-Gruppe. Die Kernaufgabe: Millionen öffentlicher Online-Gespräche — auf sozialen Medien, in News, Blogs und Foren — in Echtzeit erfassen, analysieren und für Marketing-, PR- und Produkt-Teams nutzbar machen.

Das **Social Listening** ist die Grundfunktion. Brandwatch durchsucht kontinuierlich öffentliche Quellen nach Erwähnungen einer Marke, eines Produkts, eines Wettbewerbers oder eines Themas und macht sichtbar, **was, wo und in welchem Ton** über sie gesprochen wird. Daraus entstehen Sentiment-Analysen, Trend-Erkennung, Share-of-Voice-Vergleiche und demografische Einblicke in die Gesprächsteilnehmer:innen.

Die KI-Ausbaustufe heißt **Iris** — ein Assistent, der die enorme Datenmenge zusammenfasst: Statt selbst durch tausende Posts zu navigieren, bekommt man von Iris verdichtete Antworten auf Fragen wie „Was treibt den Sentiment-Einbruch dieser Woche?" oder „Welche Themen wachsen rund um unsere Marke?". Für Teams, die schnell von Rohdaten zu Erkenntnis kommen müssen, ist das ein wichtiger Beschleuniger.

Ein Vorteil gegenüber reinen Listening-Tools ist die **integrierte Suite**: Brandwatch verbindet Social Listening mit **Social-Media-Management** (Planung, Publishing, Community-Engagement) in derselben Plattform. Was an einer Stelle als Trend erkannt wird, kann an anderer direkt in eine Reaktion oder Kampagne überführt werden.

Konkrete Anwendungsfälle reichen von **Krisen-Früherkennung** (Echtzeit-Alerts, wenn die Erwähnungen oder das Sentiment ungewöhnlich ausschlagen) über **Wettbewerbsbeobachtung** bis zur **Marktforschung** für Produktentscheidungen. Bild- und Logo-Erkennung erfasst auch visuelle Marken-Erwähnungen, die rein textbasierte Tools übersehen.

Die Schwächen sind die einer Enterprise-Plattform. Das **Pricing** ist enterprise-orientiert und nicht öffentlich — eine hohe Einstiegshürde für kleinere Organisationen. Die **Oberfläche ist komplex**, und der Aufbau guter Such-Queries (Boolean-Logik, Filter) hat eine spürbare Lernkurve. Die **Datenqualität und -abdeckung** variiert je Plattform — je nachdem, welche APIs die sozialen Netzwerke offenlegen, was sich über die Jahre immer wieder verschoben hat. Die Datenverarbeitung als UK-/EU-Anbieter ist DSGVO-relevant zu prüfen.

Empfohlen für Marketing-, PR- und Insights-Teams mittlerer bis großer Organisationen, die systematisch verstehen wollen, wie über ihre Marke und ihren Markt gesprochen wird — und die Social Listening mit Social-Media-Management in einer Suite bündeln möchten. Für kleine Teams mit einfachem Monitoring-Bedarf gibt es leichtere, günstigere Alternativen.""",
    },
]

out = ROOT / 'scripts' / 'pending_tools.json'
out.write_text(json.dumps(TOOLS, ensure_ascii=False, indent=2))
print(f'wrote {len(TOOLS)} records to {out.relative_to(ROOT)}')
for t in TOOLS:
    print(f'  - {t["slug"]:16} {t["category"]:10} ov={len(t["overview"])}c  origin={t["origin"]}')
