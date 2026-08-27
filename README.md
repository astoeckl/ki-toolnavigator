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
│   ├── app/             Routes: / · /verzeichnis · /tool/[slug] · /artikel · /artikel/[slug]
│   │                    · /kategorie/[slug] · /vergleich · /suche · /aenderungen · /impressum
│   │                    + sitemap.ts, robots.ts (aus dem CMS generiert)
│   ├── components/      UI (Wordmark, SearchBar, ScrollSpyTOC, Prose, CoverImage, JsonLd, …)
│   ├── lib/             cms.ts (fetch helpers), markdown.ts, types.ts, seo.ts
│   ├── public/          og-default.png (Share-Karte, generiert)
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
| `scripts/generate_og_image.mjs` | Rendert die Default-Share-Karte nach `web/public/og-default.png` (nur bei Marken-/Claim-Änderung nötig) |

## SEO

Zentral in `web/lib/seo.ts`:

- `pageMetadata()` baut Title, Description, Canonical, OpenGraph und Twitter-Card in einem Aufruf — jede Route ruft es in `generateMetadata()` auf.
- Titel-Template (`%s · KI-Toolnavigator`) und `metadataBase` liegen im Root-Layout, Canonicals bewusst **nicht** (sonst erben sie alle Unterseiten als `/`).
- JSON-LD über `<JsonLd>`: site-weit `Organization` + `WebSite` (inkl. `SearchAction`), pro Route `SoftwareApplication` + `Review` (Pro/Contra), `Article`, `CollectionPage`, `ItemList`, `BreadcrumbList`.
- `sitemap.xml` und `robots.txt` werden aus dem CMS erzeugt (stündliches Revalidate, `lastmod` aus `_updated_at`).
- `/suche` ist `noindex, follow`; `/verzeichnis` kanonisiert Filter-Parameter auf den nackten Pfad.

### Bilder

Alle CMS-Assets laufen über `next/image` — Wrapper ist `components/CoverImage.tsx` (fixes Seitenverhältnis, kein Layout-Shift, `fill` + AVIF/WebP, lazy außer beim Artikel-Aufmacher). Die erlaubten Remote-Hosts stehen in `next.config.js`.

Wichtig beim Ändern von Layouts: **`sizes` muss den echten Slot beschreiben.** Die Content-Spalte ist auf `1240px − 2 × 32px = 1176px` gedeckelt, der Pixel-Zweig greift also ab 1304px Viewport. Eine zu grobe Angabe kostet direkt Bandbreite — mit `33vw` statt `376px` lud der Browser 1080px-Varianten für einen 374px-Slot. Gemessen: 10 Kategorie-Cover 1619 KB → 69 KB (−96 %).

**Bewusst nicht ausgezeichnet:** `aggregateRating`. Die Felder `rating`/`reviews` im CMS sind redaktionelle Schätzwerte, werden nirgends auf der Seite angezeigt und dürften nach Googles Review-Snippet-Richtlinie nicht als Nutzerbewertungen ausgegeben werden. Ebenso kein `Offer` — die Preise liegen als Fließtext vor und lassen sich nicht verlässlich in Zahlen parsen.

## Deploy

```bash
cd web
export NETLIFY_AUTH_TOKEN=...
./node_modules/.bin/netlify deploy --build --prod
```

CMS-Edits greifen automatisch nach max. 60 s (ISR).

## Lizenz

© 2026 Dr. Andreas Stöckl — alle Rechte vorbehalten.
