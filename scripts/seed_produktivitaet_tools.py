#!/usr/bin/env python3
"""Seed 7 produktivitaet-category tools end-to-end (data + features + pricing + overview Post + logo + website).
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
    {'slug':'mem','name':'Mem','vendor':'Mem Labs','category':'produktivitaet',
     'tagline':'KI-natives Notiz-System mit selbstorganisierender Wissensdatenbank — Notizen schreiben, KI sortiert und verknüpft automatisch.',
     'price':'Free · Mem+ ab $14,99 / Mon.','api':False,'dsgvo':'bedingt','origin':'USA',
     'rating':4.3,'reviews':1820,
     'pros':['Auto-Tagging und Auto-Linking','Mem-Chat über die eigene Bibliothek','Schneller Capture aus jedem Kontext','Integriert mit Slack, Twitter, RSS'],
     'cons':['Kein lokaler Speicher (Cloud-only)','Mobile-App weniger ausgereift als Desktop','Premium teuer im Vergleich zu Notion','Kein deutscher Sprach-Support für Auto-Tags'],
     'usecases':['Persönliches Wissensmanagement','Recherche-Notizen','Brainstorming','Lebenslange Wissensbasis'],
     'launched':'2021-03-15','lastUpdated':'2026-04-25',
     'website':'https://get.mem.ai/','domain':'mem.ai',
     'features':"""- **Auto-Tagging**: KI vergibt Themen-Tags ohne manuelles Setup.
- **Auto-Linking** zwischen verwandten Notizen, ohne `[[wiki-links]]`.
- **Mem-Chat**: Frage stellen, KI antwortet aus der eigenen Bibliothek.
- **Smart Write**: kontextbewusster Schreibassistent in jeder Notiz.
- **Daily Notes** mit automatischer Tageszusammenfassung.
- **Capture-Quellen**: Slack, Twitter/X, Email-Forward, Browser-Extension.
- **Templates** für wiederkehrende Notiz-Typen (Meeting, Reading, Idea).""",
     'pricing':"""- **Free** · 100 Notizen, Basis-KI, Capture-Tools.
- **Mem+** · $14,99 / Mon. ($10 jährlich) — unbegrenzte Notizen, vollständige KI-Suite.
- **Teams** · $20 / Sitz / Mon. — geteilte Sammlungen, gemeinsame Bibliothek.
- **Enterprise** · auf Anfrage — SSO, Audit-Logs, Custom-Onboarding.
- 7-Tage-Trial für Mem+.
- Studierenden-Discount auf Antrag.""",
     'overview':"""**Mem** war 2021 eines der ersten konsequent KI-nativen Notiz-Tools — und hat sich seither vom „Roam-Killer" zum eigenständigen Wissensmanagement-System entwickelt. Die zentrale Idee: keine manuellen Tags, keine `[[wiki-links]]`, keine Ordnerstruktur. Notizen werden geschrieben, die KI sortiert und verknüpft sie selbst.

Das funktioniert über **Auto-Tagging** und **Auto-Linking**: Beim Schreiben analysiert ein Embedding-Modell den Text, vergibt Themen-Tags und schlägt Verknüpfungen zu thematisch verwandten Notizen vor. Wer eine Idee zu einem Projekt notiert, sieht in der Seitenleiste verwandte Gedanken aus den letzten Wochen — ohne sie aktiv zu suchen.

**Mem-Chat** ist der zweite Hebel: ein Chat-Interface, das ausschließlich auf der eigenen Bibliothek operiert. „Was habe ich über Kundenfeedback der letzten zwei Monate notiert?" liefert eine Synthese mit Quellenangaben. Für Recherchen, Reviews und Wochenrückblicke ein massiver Zeitgewinn.

Die **Capture-Quellen** sind breit: Slack-Nachrichten, Tweets, Bookmarks, weitergeleitete E-Mails — alles landet in der Mem-Bibliothek und wird automatisch verschlagwortet. Die Browser-Extension speichert Webseiten-Excerpts inklusive Quellenlink.

Schwächen: Mem ist Cloud-only, was für Datenschutz-sensitive Workflows ein Showstopper ist. Die Mobile-Apps hinken dem Desktop in der Polish nach. Auto-Tagging funktioniert in englischsprachigem Korpus deutlich besser als in deutschem.

Empfohlen für Wissensarbeiter:innen, die viel kapieren, aber wenig Lust auf manuelle Pflegearbeit haben — und für jeden, der eine lebenslange durchsuchbare Notizen-Bibliothek aufbauen will."""},

    {'slug':'reflect','name':'Reflect','vendor':'Reflect Notes','category':'produktivitaet',
     'tagline':'Notizen-App mit Daily Notes, Backlinks und tief integriertem GPT — schnelle Capture, klares Schreiben, KI als Sparringspartner.',
     'price':'Ab $10 / Mon. · 14-Tage-Trial','api':False,'dsgvo':'bedingt','origin':'USA',
     'rating':4.6,'reviews':1340,
     'pros':['End-to-End-Verschlüsselung als Standard','Native Apps für Mac, iOS, Web','GPT-Integration mit eigenen Custom Prompts','Sehr schnelles UI, fast keyboard-first'],
     'cons':['Kein Free-Tarif','Keine kollaborativen Features','Kein Android (Stand 2026)','Wenige Datei-Export-Formate'],
     'usecases':['Daily Journal','Recherche-Notizen','Schreibvorbereitung','Persönliches Wiki'],
     'launched':'2021-08-01','lastUpdated':'2026-04-22',
     'website':'https://reflect.app/','domain':'reflect.app',
     'features':"""- **Daily Notes** mit automatischen Datums-Verlinkungen.
- **Bidirectional Backlinks** wie in Roam und Logseq.
- **End-to-End-Verschlüsselung** für alle Notizen.
- **GPT-Integration** mit Custom Prompts (Summary, Outliner, Critic, Translator).
- **Native Apps** für macOS, iOS, Windows, Web.
- **Voice Memos** mit automatischer Transkription via Whisper.
- **Apple-Calendar-Sync** für Tages-Kontext.""",
     'pricing':"""- **Free Trial** · 14 Tage Vollzugriff, ohne Zahlungsmittel.
- **Personal** · $10 / Mon. ($120 jährlich, $96 mit 20 % Rabatt) — alle Features.
- **Lifetime** · einmalig $300 — alle künftigen Updates inkludiert.
- Keine Team- oder Enterprise-Tarife.
- Studierende auf Antrag mit 50 % Discount.""",
     'overview':"""**Reflect** ist die Antwort auf eine spezifische Frage: Wie sieht eine Notiz-App aus, wenn sie Daily Journaling, Bidirectional Backlinks und KI-Schreibhilfe von Anfang an integriert hat — und nicht als Plugin auf eine ältere Architektur draufgepfropft? Reflect ist seit 2021 am Markt und hat sich eine kleine, aber loyale Fanbase aufgebaut.

Der **Daily-Notes-Workflow** ist der Kern: Jeder Tag bekommt automatisch eine eigene Seite, Datumsverweise werden automatisch verlinkt, die Tagesseite ist Capture-Pad und Tagesplaner zugleich. Gedanken, Aufgaben, Meeting-Notizen — alles landet zuerst hier, später wandert es in thematische Seiten.

Die **GPT-Integration** ist überraschend tief: Mit `/` lassen sich Custom Prompts auslösen — vom „Summarize this page" bis zum eigenen „Critique my argument as a senior editor". Die Prompts sind editierbar, Power-User bauen sich eigene Schreibwerkzeuge.

**End-to-End-Verschlüsselung** ist Standard, nicht Add-On — für Coaches, Therapeuten und Berater, die persönliche Klienten-Notizen führen, ein zentrales Argument. Die Schlüssel liegen lokal, Reflect-Server sehen nur Chiffretext.

Schwächen: Es gibt keinen Free-Tarif, was die Eintrittshürde erhöht. Kollaboration fehlt komplett (bewusste Design-Entscheidung). Und Android-Nutzer:innen müssen weiterhin auf die Web-App ausweichen.

Empfohlen für Solo-Wissensarbeiter:innen, denen Schnelligkeit, Datenschutz und KI-Integration wichtiger sind als Team-Features — eine sehr ausgereifte Alternative zu Roam, Logseq und Obsidian."""},

    {'slug':'tana','name':'Tana','vendor':'Tana','category':'produktivitaet',
     'tagline':'Outliner mit Supertags und KI-Inferenz — verwandelt Notizen in eine strukturierte Datenbank, die sich wie Plain-Text anfühlt.',
     'price':'Free · Plus ab $8 / Mon.','api':True,'dsgvo':'bedingt','origin':'Norwegen',
     'rating':4.7,'reviews':1680,
     'pros':['Supertags strukturieren ohne Friction','Live-Views als gefilterte Listen','KI-Inferenz für Datenextraktion','Aktive Community + viele Templates'],
     'cons':['Lernkurve am steilsten unter den Notiz-Tools','Mobile-Apps spät hinzugekommen','Komplexere Workflows fühlen sich „programmiert" an','Datenresidenz EU verfügbar erst Plus-Tier'],
     'usecases':['Persönliches CRM','Projekt-Tracking','Reading-Notes','Habit-Tracking'],
     'launched':'2022-05-01','lastUpdated':'2026-04-19',
     'website':'https://tana.inc/','domain':'tana.inc',
     'features':"""- **Supertags**: jedes Stück Information wird typisiert (Person, Meeting, Buch, …).
- **Live-Views**: gefilterte Listen aller Notizen mit gleichem Supertag.
- **KI-Inferenz**: extrahiert Felder aus Fließtext (Datum, Person, Aufgabe).
- **Daily Pages** als zentraler Capture-Punkt.
- **Search-Operators** für komplexe Queries über die ganze Bibliothek.
- **Templates** als Supertag-Definitionen mit Pflichtfeldern.
- **API** zum Anbinden externer Datenquellen.""",
     'pricing':"""- **Free** · unbegrenzte Workspaces, eingeschränkte KI-Quoten.
- **Plus** · $8 / Mon. ($96 jährlich) — vollständige KI, Voice-Notes, Premium-Support.
- **Pro** · $20 / Mon. — höhere Quoten, Priority Support.
- **Teams** · $14 / Sitz / Mon. — geteilte Workspaces.
- **Enterprise** · auf Anfrage — SSO, EU-Datenresidenz, SLA.
- Kostenloser **Tana University**-Onboarding-Kurs.""",
     'overview':"""**Tana** ist das vielleicht ambitionierteste Notiz-Tool der letzten Jahre. Statt sich an Notion (Datenbank-orientiert) oder Roam (Outliner mit Backlinks) anzulehnen, kombiniert es beide Ansätze über das zentrale Konzept der **Supertags**: Jeder Bullet wird durch ein Supertag typisiert (Person, Meeting, Buch, Idee, …), und alle Bullets desselben Supertags bilden automatisch eine Datenbank.

Der Effekt ist eindrucksvoll: Eine schnell hingeworfene Notiz wie „Treffen mit #person Marc nächste Woche zu #meeting Q3-Planung" wird automatisch in zwei Datenbanken eingefügt — die Personenliste mit Marc und die Meeting-Liste mit Q3-Planung. **Live-Views** zeigen jederzeit alle Notizen eines Typs als sortierbare Liste.

Die **KI-Inferenz** ist die zweite Stärke: Felder eines Supertags (etwa Datum, Ort, Teilnehmer) werden aus Fließtext extrahiert, ohne dass man sie manuell befüllen muss. Wer ein Meeting-Protokoll diktiert, bekommt am Ende eine strukturierte Meeting-Notiz mit Action-Items.

**Daily Pages** funktionieren wie in Roam und Reflect — Tagesseite als Capture-Pad, später wandert alles in thematische Strukturen. Der Workflow lässt sich mit etwas Übung extrem schnell machen.

Schwächen: Die Lernkurve ist die steilste unter den hier vorgestellten Tools. Wer Tana nicht 2–3 Wochen ernsthaft probiert, sieht den Mehrwert nicht — der Aha-Effekt kommt verzögert. Mobile-Apps sind erst spät dazugekommen und nicht ganz auf Desktop-Niveau.

Empfohlen für strukturierungs-affine Wissensarbeiter:innen, die eine durchsuchbare und typisierte Wissensbasis statt einer reinen Sammlung wollen — und bereit sind, die Lernkurve zu investieren."""},

    {'slug':'glean','name':'Glean','vendor':'Glean Technologies','category':'produktivitaet',
     'tagline':'Enterprise-Search-Plattform mit KI-Assistent — findet alles im Unternehmen quer über Slack, Drive, Confluence, Salesforce und mehr.',
     'price':'Auf Anfrage (Enterprise)','api':True,'dsgvo':'ja','origin':'USA',
     'rating':4.8,'reviews':1090,
     'pros':['100+ vorgefertigte Konnektoren','Permission-aware: respektiert Quell-Berechtigungen','Glean Apps als No-Code-Workflows','EU-Hosting verfügbar'],
     'cons':['Nur Enterprise (typisch ab $20–30 / Sitz / Mon.)','Setup-Phase mehrwöchig','Keine Self-Service-Onboarding-Option','Volle Power erst ab ~200 Mitarbeitenden'],
     'usecases':['Unternehmensweite Suche','Wissens-Onboarding','Customer-Support','HR-Self-Service'],
     'launched':'2019-09-01','lastUpdated':'2026-04-23',
     'website':'https://www.glean.com/','domain':'glean.com',
     'features':"""- **Enterprise-Search** über Slack, Google Drive, Confluence, Notion, Salesforce, GitHub und 100+ weitere Quellen.
- **Glean Assistant**: Chat über alle verbundenen Quellen mit Zitations-Belegen.
- **Glean Apps**: No-Code-Workflows mit Promptkette, Tools und Datenquellen.
- **Permission-aware Indexing**: User sieht nur, was er auch in der Quelle dürfte.
- **Custom-Skills** zum Abfragen interner APIs und Datenbanken.
- **Browser-Extension** für In-Context-Suche auf jeder Webseite.
- **EU-Hosting** für DSGVO-relevante Datenresidenz.""",
     'pricing':"""- **Keine öffentliche Preisliste** — Enterprise-Sales-Modell.
- Marktpreis typisch **$20–30 / Sitz / Mon.** (Branchenschätzung).
- Mindestabnahme oft 250+ Sitze; Setup-Fee separat.
- **POC** über 4–8 Wochen mit Glean Customer Engineering.
- **Enterprise+** · Custom-AI-Modelle on-premise (auf Anfrage).
- Discount für Bildungseinrichtungen und Non-Profits verhandelbar.""",
     'overview':"""**Glean** ist das wohl ausgereifteste Werkzeug der „Enterprise-Search 2.0"-Welle — also der Wiederbelebung der alten Idee unternehmensweiter Volltext-Suche durch KI-Assistenten. Während Konkurrenten wie Microsoft Copilot stark an die eigene Suite gebunden sind, ist Glean konsequent **Multi-Cloud und Multi-Tool**: 100+ Konnektoren decken die typische Enterprise-Software-Landschaft ab.

Das wichtigste Architektur-Prinzip ist **permission-aware indexing**: Glean indexiert keine Daten, die der suchende User in der Quelle nicht sehen dürfte. Salesforce-Opportunities sind nur für berechtigte Sales-User auffindbar, vertrauliche HR-Dokumente bleiben HR-intern. Das löst eines der größten Probleme klassischer Enterprise-Search.

Der **Glean Assistant** ist die Konversations-Schicht: ein Chat-Interface, das jede Antwort mit Zitaten aus den Quellen belegt — Slack-Threads, Confluence-Seiten, PDFs, Salesforce-Records. Für Onboarding neuer Mitarbeitender, Customer-Support und schnelle „Wer weiß was?"-Fragen extrem wertvoll.

**Glean Apps** sind No-Code-Workflows: Eine Prompt-Kette greift auf bestimmte Datenquellen zu, ruft Custom-Skills auf (etwa interne APIs) und liefert strukturierte Antworten — etwa „Erstelle einen Wettbewerbsbericht zu X" oder „Fasse alle offenen Support-Tickets dieser Woche zusammen".

Schwächen: Glean ist explizit Enterprise — keine Self-Service-Onboarding-Option, Sales-getriebenes Pricing, Setup-Phase typisch 4–8 Wochen. Für Teams unter ~200 Mitarbeitenden lohnt sich der Aufwand selten.

Empfohlen für mittelgroße bis große Unternehmen mit fragmentierter Tool-Landschaft, in denen Mitarbeitende viel Zeit mit „Wer hat das nochmal gesagt?" verlieren — Glean ist hier eines der wenigen Tools, die ihren Preis wirklich wert sind."""},

    {'slug':'motion','name':'Motion','vendor':'Motion (Usemotion Inc.)','category':'produktivitaet',
     'tagline':'KI-Calendar und Task-Manager in einem — plant Aufgaben automatisch in freie Zeitfenster und re-priorisiert dynamisch.',
     'price':'Ab $19 / Mon. · 7-Tage-Trial','api':False,'dsgvo':'bedingt','origin':'USA',
     'rating':4.4,'reviews':2960,
     'pros':['Auto-Scheduling für Tasks und Habits','Project-Templates mit Abhängigkeiten','Meeting-Booking-Pages integriert','Sync mit Google, Outlook, iCloud'],
     'cons':['Kein Free-Tarif','Mobile-Apps weniger ausgereift als Web','Auto-Scheduling braucht Lernzeit','Pricing höher als reine Calendar-Tools'],
     'usecases':['Time-Blocking','Projekt-Management','Meeting-Booking','Persönliches Habit-Tracking'],
     'launched':'2019-07-01','lastUpdated':'2026-04-21',
     'website':'https://www.usemotion.com/','domain':'usemotion.com',
     'features':"""- **Auto-Scheduling**: KI legt Tasks in freie Zeitfenster, beachtet Deadlines und Prioritäten.
- **Project Manager** mit Abhängigkeiten und automatischer Ressourcenplanung.
- **Meeting Booker** als personalisierter Calendly-Ersatz.
- **Habits** als wiederkehrende Tasks mit flexiblen Slots.
- **Smart Inbox**: KI sortiert eingehende Tasks nach Dringlichkeit.
- **Calendar-Sync** mit Google, Outlook und iCloud (bidirektional).
- **Team-Workspaces** mit gemeinsamer Workload-Sicht.""",
     'pricing':"""- **7-Tage-Trial** · Vollzugriff ohne Zahlungsmittel.
- **Individual** · $19 / Mon. ($228 jährlich) bzw. $34 monatlich.
- **Team** · $12 / Sitz / Mon. (jährlich) — geteilte Projekte, Workload-Sicht.
- **Enterprise** · auf Anfrage — SSO, Custom-Onboarding, SLA.
- Kein Free-Tarif.
- **AI Email** als optionales Add-On verfügbar.""",
     'overview':"""**Motion** kombiniert drei Tools, die viele Wissensarbeiter:innen sonst getrennt nutzen — Calendar, Task-Manager und Meeting-Booker — in einem KI-getriebenen Werkzeug. Die zentrale These: Wenn die KI weiß, wann freie Zeit ist und welche Tasks anstehen, kann sie einen viel besseren Tagesplan erstellen als der Mensch selbst.

Der Kern ist das **Auto-Scheduling**: Tasks werden mit Dauer, Deadline und Priorität erfasst, Motion legt sie automatisch in freie Calendar-Slots. Wenn ein neues Meeting reinkommt, schiebt Motion betroffene Tasks dynamisch um — ohne dass man manuell jonglieren muss. Wer mit unvollständigen Tagesplänen hadert, gewinnt hier spürbar.

Der **Project Manager** ergänzt das um Team-Funktionen: Aufgaben mit Abhängigkeiten, Workload-Sicht über alle Team-Mitglieder, automatische Ressourcenplanung. Für kleine Teams (5–20 Personen) ist das ein voller Asana-Ersatz, ohne den manuellen Pflege-Overhead.

Die **Meeting-Booking-Page** ersetzt Calendly: personalisierte Buchungs-Slots, die auf den dynamischen Calendar zugreifen — und sich nach jeder Änderung neu kalibrieren. Klassische Booking-Tools sehen daneben statisch aus.

Schwächen: Es gibt keinen Free-Tarif, $19/Monat ist im persönlichen Bereich spürbar. Auto-Scheduling braucht etwa 1–2 Wochen, bis man die Prioritäts-Settings im Griff hat — anfangs verschiebt Motion Aufgaben aus unerwarteten Gründen. Mobile-Apps sind funktional, aber weniger poliert als das Web.

Empfohlen für Solo-Knowledge-Worker:innen mit voller Calendar und vielen kleinen Tasks — und für kleine Teams, die ein integriertes Tool statt Asana + Calendly + Calendar suchen."""},

    {'slug':'reclaim','name':'Reclaim','vendor':'Reclaim.ai','category':'produktivitaet',
     'tagline':'KI-Calendar-Assistent für Teams: schützt Fokuszeit, plant Habits und Meetings dynamisch um — Add-On zu Google Calendar.',
     'price':'Free · Pro ab $10 / Sitz / Mon.','api':False,'dsgvo':'bedingt','origin':'USA',
     'rating':4.6,'reviews':2240,
     'pros':['Add-On zu Google/Microsoft Calendar — kein Tool-Wechsel','Smart 1:1s mit Team-Mitgliedern','Habits werden automatisch verschoben','Solider Free-Tarif'],
     'cons':['Microsoft-Calendar-Support später als Google','Komplexe Habits brauchen Konfigurations-Geduld','Keine eigene Project-Management-Schicht','Kein Notion- oder Asana-Sync nativ'],
     'usecases':['Fokuszeit-Schutz','Smart 1:1s','Habit-Tracking','Team-Calendar-Optimierung'],
     'launched':'2019-09-01','lastUpdated':'2026-04-20',
     'website':'https://reclaim.ai/','domain':'reclaim.ai',
     'features':"""- **Smart Habits**: wiederkehrende Aktivitäten finden eigene Slots im Calendar.
- **Smart 1:1s**: optimaler Zeitpunkt unter Berücksichtigung beider Calendars.
- **Focus Time** wird automatisch geschützt und im Status angezeigt.
- **Buffer Time** zwischen Meetings, einstellbar pro Meeting-Typ.
- **Tasks** mit Auto-Scheduling, Sync mit Asana, Linear, Todoist, ClickUp.
- **No-Meeting-Days** als globaler Schutz vor Meeting-Wahn.
- **Calendar Sync** für Google Workspace und Microsoft 365.""",
     'pricing':"""- **Free Lite** · Smart Habits, Smart 1:1s, Basis-Tasks (1 Calendar).
- **Starter** · $10 / Sitz / Mon. ($96 jährlich) — Team-Features, 8 Habits.
- **Business** · $15 / Sitz / Mon. — unbegrenzte Habits, Premium-Support.
- **Enterprise** · ab $30 / Sitz / Mon. — SSO, SCIM, Audit-Logs.
- Bezahlt-Tarife mit 14-Tage-Trial.
- **Education-Discount** für Studierende und Lehrende auf Antrag.""",
     'overview':"""**Reclaim** verfolgt einen anderen Ansatz als Motion: Statt einen eigenen Calendar zu sein, ist Reclaim ein **intelligenter Layer über Google Calendar** (und mittlerweile Microsoft 365). Wer den eigenen Calendar nicht aufgeben will, bekommt dieselben KI-Vorteile ohne Tool-Wechsel.

**Smart Habits** sind das zentrale Feature: Wiederkehrende Aktivitäten — Lunch, Workout, Deep Work, Reading — bekommen flexible Slots, die Reclaim dynamisch in den Calendar legt und bei Konflikten verschiebt. Ein Meeting platzt nicht mehr in die Lunch-Pause; das Workout wird auf morgen verlegt, statt komplett zu entfallen.

**Smart 1:1s** lösen das nervige Problem wiederkehrender Bilateral-Termine: Reclaim findet den optimalen Zeitpunkt, der beiden Calendars passt — und re-plant automatisch, wenn einer der Beteiligten ein Konflikt-Meeting bekommt. Für Manager mit 8+ direkten Reports ein massiver Zeitgewinn.

**Focus Time** wird als geschützter Block angelegt und automatisch im Status (Slack, Microsoft Teams) angezeigt. Kollegen sehen, dass jetzt nicht der richtige Moment für Pings ist. **Buffer Time** zwischen Meetings ist konfigurierbar pro Meeting-Typ — nach langen Reviews hat man automatisch 15 Minuten zur Atmung.

Die **Task-Integration** verbindet Reclaim mit Asana, Linear, Todoist und ClickUp — Tasks aus diesen Tools werden automatisch im Calendar verplant. Die Vision: ein einziger durchgängiger Tagesplan.

Schwächen: Der Microsoft-Calendar-Support ist erst seit 2024 vollständig. Die Konfiguration komplexer Habits (mit Working-Hours, Buffer, Min-Slots) ist eine Lernaufgabe. Und der Free-Tarif funktioniert nur mit einem einzigen Calendar.

Empfohlen für alle, die Google Calendar oder Outlook intensiv nutzen und nicht das ganze Tool wechseln wollen — eine elegante Erweiterung statt einer Disruption."""},

    {'slug':'granola','name':'Granola','vendor':'Granola','category':'produktivitaet',
     'tagline':'Mac-native KI-Notizen für Meetings — hört zu, transkribiert, fasst zusammen, ohne Bot im Call.',
     'price':'Free (25 Meetings) · Pro ab $14 / Mon.','api':False,'dsgvo':'bedingt','origin':'UK',
     'rating':4.8,'reviews':2810,
     'pros':['Kein Bot im Meeting (lokale Audio-Aufnahme)','Sehr schnelle Zusammenfassungen','Custom Templates für Meeting-Typen','Natives Mac-UI, fühlt sich wie eine Apple-App an'],
     'cons':['Nur macOS (Stand 2026)','Audio bleibt lokal, aber Notizen Cloud-only','Kein deutscher Whisper-Modus optimiert','Pricing pro Meeting-Quote nicht ganz transparent'],
     'usecases':['1:1s und Stand-ups','Sales-Calls','User-Interviews','Investor-Updates'],
     'launched':'2024-01-01','lastUpdated':'2026-04-26',
     'website':'https://www.granola.ai/','domain':'granola.ai',
     'features':"""- **Lokale Audio-Aufnahme** ohne Bot im Call (Zoom, Meet, Teams, FaceTime).
- **Live-Transkription** während des Meetings, sichtbar als Live-Stream.
- **Templates** für Meeting-Typen (Standup, 1:1, Sales-Demo, User-Interview).
- **Augmented Notes**: eigene Stichpunkte werden mit KI-Kontext angereichert.
- **Folder-Struktur** mit Auto-Tagging nach Teilnehmenden.
- **Slack- und Notion-Export** mit einem Klick.
- **Apple Watch Companion** für „Done"-Trigger ohne Mac-Wechsel.""",
     'pricing':"""- **Free** · 25 Meetings pro Monat, alle Kernfeatures.
- **Pro** · $14 / Mon. ($168 jährlich) — unbegrenzte Meetings.
- **Business** · $20 / Sitz / Mon. — Team-Workspaces, geteilte Templates.
- **Enterprise** · auf Anfrage — SSO, Audit-Logs, Custom-Onboarding.
- Studierende und Lehrende auf Antrag mit 50 % Discount.
- **Free-Trial** für Pro über 14 Tage ohne Zahlungsmittel.""",
     'overview':"""**Granola** ist das aktuell heißeste Meeting-Tool für Mac-Nutzer:innen — und löst eines der größten Friktions-Probleme klassischer Meeting-AI: kein Bot mehr im Call. Statt einen virtuellen Teilnehmer mit Kamera und Mikro reinzulassen (Otter, Fireflies, Read.ai), nimmt Granola lokal über das Mikrofon des Mac auf — vollständig unsichtbar für die anderen Teilnehmer.

Der **Workflow** ist erfrischend einfach: Granola-App vor dem Meeting öffnen, eigene Stichpunkte tippen wie immer, am Ende auf „Done" drücken. Innerhalb von 30 Sekunden gibt es eine ausformulierte Zusammenfassung, die die eigenen Notizen mit dem KI-Verständnis des Gesprächs anreichert. Die so genannten **Augmented Notes** sind oft besser als reine KI-Summaries, weil sie die Akzent-Setzung des Notizenden bewahren.

Die **Templates** sind hochwertig kuratiert: Sales-Demo, User-Interview, Standup, 1:1, Investor-Update — jedes mit eigener Struktur und Prompt-Logik. Wer Custom-Templates baut, formuliert das gewünschte Output-Format einmalig in Plain-Text.

Die **Folder-Struktur** organisiert automatisch nach Teilnehmenden (aus dem Calendar-Event extrahiert), was nach 100+ Meetings den Unterschied zwischen „findbar" und „verloren" macht. **Slack- und Notion-Export** sind ein Klick weg.

Schwächen: Granola läuft nur auf macOS — Windows- und Linux-User schauen in die Röhre. Audio bleibt zwar lokal, die finalen Notizen werden aber in der Granola-Cloud gespeichert. Und der deutsche Whisper-Modus ist okay, aber für sehr fachliche Calls (Medizin, Recht) ist eine Nachkorrektur nötig.

Empfohlen für Mac-affine Knowledge-Worker:innen mit vielen Meetings — und für jeden, der den „Bot im Call"-Effekt seiner Kollegen einfach satt hat."""},
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
        # Create element with all base data; new elements default to published=False
        # so we explicitly publish below after creation.
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
        # Belt-and-braces publish flip — some Cognitor versions ignore `published` in POST.
        if not el.get('published'):
            requests.patch(f'{BASE}/{SITE}/elements/{el["id"]}',
                json={'published': True}, headers=JH, verify=False)
    else:
        print(f'· {slug}: exists (id={el["id"]})')

    existing_data = el.get('data', {})
    patches = {}

    # Overview Post
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

    # Logo
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
