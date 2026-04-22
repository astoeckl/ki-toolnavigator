# KI-Toolnavigator

Kuratiertes deutsches Verzeichnis für KI-Tools — Next.js 16 App Router, inhaltsverwaltet über das Cognitor-CMS, deployed auf Netlify.

Live: **https://ki-toolnavigator.com**

## Stack

- **Next.js 16** (App Router, Server Components, ISR 60 s)
- **TypeScript**
- **Cognitor CMS** (https://backend.cognitor.dev) — Content Types `tool`, `article`, `category` + referenzierte Posts für Long-Text
- **Fal.ai / Nano Banana** (über Cognitor) für Cover-Illustrationen
- **Playwright** für Website-Screenshots (produziert `screenshots/*.jpg`, werden ins CMS hochgeladen)
- **Netlify** Hosting (`@netlify/plugin-nextjs`)

## Repo-Struktur

```
.
├── web/                 Next.js App (App Router + Server Components)
│   ├── app/             Routes: / · /verzeichnis · /tool/[slug] · /artikel/[slug]
│   │                    · /kategorie/[slug] · /vergleich · /suche · /aenderungen · /impressum
│   ├── components/      UI (Wordmark, SearchBar, ScrollSpyTOC, Prose, …)
│   ├── lib/             cms.ts (fetch helpers), markdown.ts, types.ts
│   └── app/api/         Route Handlers: /api/search, /api/suggest (Cognitor-Proxy)
├── scripts/             Python + Node helpers for CMS seeding & asset generation
├── design/              original HTML/JSX prototype (see design/ki-toolnavigator/README.md)
└── KI-Toolnavigator.html legacy single-file React prototype (pre-dynamic)
```

## Environment

Server-seitige `.env` für Scripts + `web/.env.local` für Next.js. **Nicht eingecheckt** — beide `.env` und `.env.local` sind im `.gitignore`.

```
# Cognitor
BASEURL=https://backend.cognitor.dev
EMAIL=<cognitor-user>
PW=<cognitor-password>
TENANT=<tenant-identifier>
SITE=<site-identifier>

# Netlify (CI/manual deploy)
NETLIFY_AUTH_TOKEN=<netlify-personal-access-token>
```

`web/.env.local`:
```
COGNITOR_BASE_URL=https://backend.cognitor.dev
COGNITOR_SITE=<site-identifier>
COGNITOR_EMAIL=<cognitor-user>
COGNITOR_PASSWORD=<cognitor-password>
```

## Lokales Entwickeln

```bash
cd web
npm install
npm run dev       # http://localhost:3030
```

## Seeding / Asset-Pipelines

Alle Skripte sind idempotent (überspringen Elemente, die bereits gepatcht sind).

| Script | Zweck |
|---|---|
| `scripts/seed_cms.py` | Initiale 4 Content-Types + 14 Ur-Tools + 9 Kategorien + 6 Artikel |
| `scripts/seed_new_tools.py` | 15 weitere Tools (GPT, Claude, Grok, Flux, Suno, Synthesia, n8n, …) |
| `scripts/extend_schema.py` | Fügt `overview`-Feld auf Tools hinzu |
| `scripts/seed_overviews.py` | Hand-verfasste Übersichts-Markdown pro Tool/Artikel |
| `scripts/migrate_tool_posts.py` | Wandelt inline `overview` → eigenständige Cognitor-Posts mit `post_id`-Referenz |
| `scripts/migrate_article_posts.py` | Dasselbe für Artikel-Body |
| `scripts/seed_tool_features_pricing.py` | `features` + `pricing` Markdown |
| `scripts/seed_tool_websites.py` | Offizielle Hersteller-URLs (29 Tools) |
| `scripts/generate_article_images.py` | Nano-Banana-Cover pro Artikel (Brand-Style) |
| `scripts/generate_tool_images.py` | Nano-Banana-Cover pro Tool |
| `scripts/upload_tool_logos.py` | Offizielle Logos via Google-Favicon-Service, ins Cognitor-Media-Library |
| `scripts/capture_tool_screenshots.mjs` | Playwright-Headless für echte Website-Screenshots |
| `scripts/upload_screenshots.py` | Upload + Patch `screenshot_id` |

## Deploy

```bash
cd web
export NETLIFY_AUTH_TOKEN=...
./node_modules/.bin/netlify deploy --build --prod
```

CMS-Edits greifen automatisch nach max. 60 s (ISR).

## Lizenz

© 2026 Dr. Andreas Stöckl — alle Rechte vorbehalten.
