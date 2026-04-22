// KI-Toolnavigator — Datenmodell
window.KI_DATA = {
  categories: [
    { slug: 'sprachmodelle', name: 'Sprachmodelle & Chat', count: 47, desc: 'Allgemeine LLMs und Chat-Assistenten für Text, Recherche und Analyse.' },
    { slug: 'bildgenerierung', name: 'Bildgenerierung', count: 34, desc: 'Text-zu-Bild, Stilübertragung und generative Bildbearbeitung.' },
    { slug: 'video-audio', name: 'Video & Audio', count: 28, desc: 'Video-Synthese, Stimmklonung, Musik und Transkription.' },
    { slug: 'coding', name: 'Coding-Assistenten', count: 22, desc: 'KI-gestützte Entwicklungsumgebungen, Copiloten und Code-Review.' },
    { slug: 'agenten', name: 'Agenten & Automation', count: 19, desc: 'Autonome Agenten, Workflow-Automation und Orchestrierung.' },
    { slug: 'produktivitaet', name: 'Produktivität & Wissen', count: 41, desc: 'Notizen, Zusammenfassung, Wissensmanagement, Meetings.' },
    { slug: 'daten-analyse', name: 'Daten & Analyse', count: 17, desc: 'SQL-Assistenten, BI-Agenten, automatisierte Auswertung.' },
    { slug: 'marketing', name: 'Marketing & Content', count: 33, desc: 'Copywriting, SEO, Social-Media, Ad-Creative.' },
    { slug: 'forschung', name: 'Wissenschaft & Forschung', count: 12, desc: 'Literaturrecherche, wissenschaftliches Schreiben, Zitation.' }
  ],

  tools: [
    {
      slug: 'chatgpt', name: 'ChatGPT', vendor: 'OpenAI', category: 'sprachmodelle',
      tagline: 'Der bekannteste KI-Assistent für Dialog, Recherche und Textarbeit.',
      price: 'Freemium — Plus $20/Mon.', api: true, dsgvo: 'bedingt', origin: 'USA',
      rating: 4.6, reviews: 2841,
      pros: ['Größtes Ökosystem', 'Multimodal (Bild, Stimme, Dateien)', 'Custom GPTs & Store', 'Breite API-Verfügbarkeit'],
      cons: ['Datenverarbeitung außerhalb EU', 'Kontext-Limit in Plus-Tarif', 'Halluziniert bei Nischenfragen'],
      usecases: ['Recherche', 'Entwurf', 'Code-Review', 'Übersetzung', 'Brainstorming'],
      launched: '2022-11-30', lastUpdated: '2026-03-12'
    },
    {
      slug: 'claude', name: 'Claude', vendor: 'Anthropic', category: 'sprachmodelle',
      tagline: 'Sprachmodell mit Fokus auf lange Kontexte, Sorgfalt und nuancierte Texte.',
      price: 'Freemium — Pro $20/Mon.', api: true, dsgvo: 'bedingt', origin: 'USA',
      rating: 4.7, reviews: 1420,
      pros: ['200k+ Kontextfenster', 'Sehr gute Schreibqualität', 'Artifacts für interaktive Ausgaben', 'Projects für Wissenssammlungen'],
      cons: ['Kleineres Ökosystem', 'Weniger Plugins', 'Keine native Bildgenerierung'],
      usecases: ['Langtext-Analyse', 'Redaktion', 'Recherche', 'Prototyping'],
      launched: '2023-03-14', lastUpdated: '2026-04-02'
    },
    {
      slug: 'gemini', name: 'Gemini', vendor: 'Google', category: 'sprachmodelle',
      tagline: 'Googles multimodales Modell, tief in Workspace und Suche integriert.',
      price: 'Freemium — Advanced €21,99/Mon.', api: true, dsgvo: 'bedingt', origin: 'USA',
      rating: 4.3, reviews: 1987,
      pros: ['Integration in Gmail/Docs', 'Sehr großes Kontextfenster', 'Starke Recherche-Features', 'Multimodal'],
      cons: ['Qualität schwankt zwischen Modellen', 'Europäische Features teils eingeschränkt'],
      usecases: ['Google-Workspace-Nutzer', 'Recherche', 'Meeting-Zusammenfassung'],
      launched: '2023-12-06', lastUpdated: '2026-03-28'
    },
    {
      slug: 'mistral', name: 'Le Chat', vendor: 'Mistral AI', category: 'sprachmodelle',
      tagline: 'Europäisches LLM aus Paris — schnell, offen, DSGVO-freundlich.',
      price: 'Freemium — Pro €14,99/Mon.', api: true, dsgvo: 'ja', origin: 'EU (FR)',
      rating: 4.4, reviews: 612,
      pros: ['EU-Datenverarbeitung', 'Open-Source-Modelle verfügbar', 'Sehr schnelle Inferenz', 'Faire Preise'],
      cons: ['Kleineres Ökosystem', 'Weniger Integrationen', 'Weniger multimodal'],
      usecases: ['EU-Compliance', 'Self-Hosting', 'Chat', 'Coding'],
      launched: '2024-02-26', lastUpdated: '2026-04-08'
    },
    {
      slug: 'midjourney', name: 'Midjourney', vendor: 'Midjourney Inc.', category: 'bildgenerierung',
      tagline: 'Der Industriestandard für ästhetische Bildgenerierung.',
      price: 'Ab $10/Mon.', api: false, dsgvo: 'nein', origin: 'USA',
      rating: 4.5, reviews: 3210,
      pros: ['Ausgezeichnete Bildqualität', 'Starke Community', 'Style References (--sref)'],
      cons: ['Keine öffentliche API', 'Discord- und Web-only', 'Rechtliche Grauzone'],
      usecases: ['Konzeptkunst', 'Mood-Boards', 'Editorial', 'Ideation'],
      launched: '2022-07-12', lastUpdated: '2026-03-15'
    },
    {
      slug: 'stable-diffusion', name: 'Stable Diffusion', vendor: 'Stability AI', category: 'bildgenerierung',
      tagline: 'Offenes Bildmodell — lokal lauffähig, voll anpassbar.',
      price: 'Open Source / API ab $0.01', api: true, dsgvo: 'ja', origin: 'UK/DE',
      rating: 4.2, reviews: 1540,
      pros: ['Open Source', 'Lokal nutzbar', 'Riesige Modell-Community', 'LoRA-Feintuning'],
      cons: ['Setup anspruchsvoll', 'Qualität hängt vom Modell ab'],
      usecases: ['Lokale Generierung', 'Feintuning', 'Batch-Produktion'],
      launched: '2022-08-22', lastUpdated: '2026-02-19'
    },
    {
      slug: 'elevenlabs', name: 'ElevenLabs', vendor: 'ElevenLabs', category: 'video-audio',
      tagline: 'Realistische Stimmsynthese und Voice-Cloning in 30+ Sprachen.',
      price: 'Freemium — Starter $5/Mon.', api: true, dsgvo: 'bedingt', origin: 'USA/PL',
      rating: 4.7, reviews: 892,
      pros: ['Beste Stimmqualität am Markt', 'Sehr schnelle Generierung', 'Mehrsprachig'],
      cons: ['Missbrauchspotenzial', 'Teurer bei Volumen'],
      usecases: ['Podcasts', 'Hörbücher', 'Lokalisierung', 'Voice-Over'],
      launched: '2022-11-01', lastUpdated: '2026-04-01'
    },
    {
      slug: 'runway', name: 'Runway', vendor: 'Runway ML', category: 'video-audio',
      tagline: 'Text-zu-Video und Video-Bearbeitung mit KI — Gen-3 und neuer.',
      price: 'Freemium — Standard $15/Mon.', api: true, dsgvo: 'nein', origin: 'USA',
      rating: 4.3, reviews: 745,
      pros: ['Führend bei Text-zu-Video', 'Intuitive Oberfläche', 'Viele Effekte'],
      cons: ['Credits schnell aufgebraucht', 'Längen begrenzt'],
      usecases: ['Musikvideos', 'Werbung', 'Prototyping'],
      launched: '2018-11-01', lastUpdated: '2026-03-22'
    },
    {
      slug: 'cursor', name: 'Cursor', vendor: 'Anysphere', category: 'coding',
      tagline: 'KI-native IDE auf VS-Code-Basis — Code schreiben im Dialog.',
      price: 'Freemium — Pro $20/Mon.', api: false, dsgvo: 'bedingt', origin: 'USA',
      rating: 4.6, reviews: 1203,
      pros: ['Vollwertige IDE', 'Composer für Multi-File-Edits', 'Eigenes Modell-Routing', 'Tab-Vervollständigung stark'],
      cons: ['Pro-Limits spürbar', 'Komplexität für Einsteiger'],
      usecases: ['Tägliche Entwicklung', 'Refactoring', 'Prototyping'],
      launched: '2023-03-01', lastUpdated: '2026-04-10'
    },
    {
      slug: 'copilot', name: 'GitHub Copilot', vendor: 'GitHub/Microsoft', category: 'coding',
      tagline: 'Der Pionier der KI-Code-Vervollständigung — jetzt mit Agent-Modus.',
      price: 'Ab $10/Mon.', api: false, dsgvo: 'bedingt', origin: 'USA',
      rating: 4.4, reviews: 2198,
      pros: ['Tiefe GitHub-Integration', 'Alle großen IDEs', 'Chat + Agent'],
      cons: ['Kontext kleiner als Cursor', 'Enterprise-Preise'],
      usecases: ['IDE-Autocomplete', 'PR-Reviews', 'Tests'],
      launched: '2021-10-29', lastUpdated: '2026-03-30'
    },
    {
      slug: 'notion-ai', name: 'Notion AI', vendor: 'Notion Labs', category: 'produktivitaet',
      tagline: 'KI-Features direkt im Notion-Workspace — Q&A über alle Seiten.',
      price: '$10/Mon. Add-on', api: false, dsgvo: 'bedingt', origin: 'USA',
      rating: 4.2, reviews: 980,
      pros: ['Nahtlos in Notion', 'Q&A über Workspace', 'Schreiben im Kontext'],
      cons: ['Nur für Notion-Nutzer', 'Eingeschränkt ohne Notion-Daten'],
      usecases: ['Team-Wiki', 'Zusammenfassung', 'Meeting-Notizen'],
      launched: '2023-02-22', lastUpdated: '2026-02-28'
    },
    {
      slug: 'perplexity', name: 'Perplexity', vendor: 'Perplexity AI', category: 'forschung',
      tagline: 'Antwort-Maschine mit Quellenangaben — KI für Recherche.',
      price: 'Freemium — Pro $20/Mon.', api: true, dsgvo: 'bedingt', origin: 'USA',
      rating: 4.5, reviews: 1670,
      pros: ['Immer mit Quellen', 'Echtzeit-Websuche', 'Spaces für Themen'],
      cons: ['Qualität der Quellen variiert', 'Kein eigenes Modell'],
      usecases: ['Recherche', 'Fact-Checking', 'Literatur'],
      launched: '2022-12-07', lastUpdated: '2026-04-05'
    },
    {
      slug: 'deepl-write', name: 'DeepL Write', vendor: 'DeepL', category: 'marketing',
      tagline: 'Deutsches KI-Schreibwerkzeug aus Köln — perfekt für Business-Texte.',
      price: 'Freemium — Pro €8,99/Mon.', api: true, dsgvo: 'ja', origin: 'EU (DE)',
      rating: 4.6, reviews: 540,
      pros: ['Beste deutsche Sprachqualität', 'DSGVO-konform', 'Unternehmensserver in EU'],
      cons: ['Nur Textverbesserung, kein Generator', 'Begrenzte Kreativität'],
      usecases: ['E-Mails', 'Berichte', 'Lektorat'],
      launched: '2023-01-17', lastUpdated: '2026-03-08'
    },
    {
      slug: 'aleph-alpha', name: 'Pharia AI', vendor: 'Aleph Alpha', category: 'sprachmodelle',
      tagline: 'Souveräne KI aus Heidelberg — Fokus auf Behörden und Industrie.',
      price: 'Enterprise — auf Anfrage', api: true, dsgvo: 'ja', origin: 'EU (DE)',
      rating: 4.1, reviews: 89,
      pros: ['Deutscher Anbieter', 'Self-Hosting möglich', 'Erklärbare KI', 'Enterprise-Support'],
      cons: ['Keine Consumer-Version', 'Hohe Einstiegshürde'],
      usecases: ['Behörden', 'Versicherung', 'Industrie'],
      launched: '2021-04-15', lastUpdated: '2026-01-20'
    }
  ],

  articles: [
    { slug: 'was-ist-ki', title: 'Was ist Künstliche Intelligenz?', category: 'Grundlagen', author: 'Redaktion', date: '2026-04-02', readTime: 8, toc: ['Definition', 'Geschichte', 'Teilgebiete', 'Heutige Anwendungen', 'Grenzen und Kritik'] },
    { slug: 'llm-vergleich', title: 'Große Sprachmodelle im Vergleich 2026', category: 'Vergleich', author: 'M. Hartmann', date: '2026-03-28', readTime: 14, toc: ['Einführung', 'Methodik', 'Benchmark-Ergebnisse', 'Kosten pro Token', 'Empfehlungen'] },
    { slug: 'dsgvo-ki', title: 'DSGVO und KI: Was Unternehmen 2026 wissen müssen', category: 'Recht', author: 'Dr. S. Klein', date: '2026-03-15', readTime: 11, toc: ['Rechtliche Grundlagen', 'EU AI Act', 'Auftragsverarbeitung', 'Checkliste'] },
    { slug: 'prompt-engineering', title: 'Prompt Engineering: Techniken und Muster', category: 'Praxis', author: 'J. Weber', date: '2026-03-10', readTime: 16, toc: ['Grundprinzipien', 'Few-Shot', 'Chain-of-Thought', 'Rollen', 'Anti-Patterns'] },
    { slug: 'rag-erklaert', title: 'Retrieval-Augmented Generation erklärt', category: 'Technik', author: 'Dr. T. Müller', date: '2026-02-22', readTime: 12, toc: ['Was ist RAG?', 'Architektur', 'Vektordatenbanken', 'Evaluierung'] },
    { slug: 'ki-bildgenerierung', title: 'KI-Bildgenerierung: Von Diffusion zu Video', category: 'Technik', author: 'L. Schmidt', date: '2026-02-10', readTime: 9, toc: ['Diffusionsmodelle', 'Training', 'Steuerung', 'Video-Generation'] }
  ],

  recentChanges: [
    { time: 'vor 12 Min.', user: 'M. Hartmann', action: 'ergänzte', target: 'Claude', detail: 'Artifacts-Sektion' },
    { time: 'vor 47 Min.', user: 'Redaktion', action: 'aktualisierte', target: 'ChatGPT', detail: 'Preistabelle' },
    { time: 'vor 2 Std.', user: 'J. Weber', action: 'erstellte', target: 'Prompt Engineering', detail: 'neuer Artikel' },
    { time: 'vor 4 Std.', user: 'L. Schmidt', action: 'korrigierte', target: 'Midjourney', detail: 'Preisangabe' },
    { time: 'vor 6 Std.', user: 'Dr. S. Klein', action: 'ergänzte', target: 'DSGVO und KI', detail: 'EU AI Act §15' },
    { time: 'vor 1 Tag', user: 'Redaktion', action: 'erstellte', target: 'Pharia AI', detail: 'neuer Eintrag' },
    { time: 'vor 1 Tag', user: 'T. Müller', action: 'verlinkte', target: 'RAG', detail: 'Querverweis zu Vektordatenbanken' }
  ]
};
