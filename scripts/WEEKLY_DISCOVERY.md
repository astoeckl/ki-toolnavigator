# Weekly KI-Toolnavigator tool discovery (headless runbook)

You are running **unattended** (headless, no human watching). Your goal: find a
small number of newly-launched or significantly-updated AI tools, add them to the
KI-Toolnavigator directory end-to-end, deploy, and commit — at the same quality
bar as the existing catalogue.

Work in: `/Users/astoeckl/Documents/tool navigator`. Use today's real date for
any date fields (format YYYY-MM-DD).

## Step 1 — Discover & draft (prefer the workflow)

Run the **weekly-tool-discovery** workflow via the Workflow tool, invoking it by
script path (named resolution does not cover `.claude/workflows/`):
`Workflow({ scriptPath: "/Users/astoeckl/Documents/tool navigator/scripts/weekly-tool-discovery.workflow.js", args: { max: 5, todayISO: "<TODAY>" } })`.
It snapshots the live catalogue, researches new tools across all 9 categories +
launch trackers, dedupes, authors full German records, and writes
`scripts/pending_tools.json`.

If the Workflow tool is unavailable, do it manually instead:
1. `python3 scripts/list_slugs.py` → the existing catalogue. **Never duplicate an existing slug or tool.**
2. Web-search for AI tools launched or majorly updated in the **last ~2 weeks** across these categories:
   `sprachmodelle, bildgenerierung, video-audio, coding, agenten, produktivitaet, daten-analyse, marketing, forschung`
   plus launch trackers (Product Hunt, There's An AI For That, TechCrunch AI, Ben's Bites).
3. Pick up to **5** genuinely-new, notable, generally-available tools.
4. Write `scripts/pending_tools.json` — a JSON **array** of full records. Each record must
   include every field in the `REQUIRED` list at the top of `scripts/seed_pending_tools.py`
   (German `tagline`, `pros`/`cons`/`usecases` of 3–4 bullets, German markdown `features`
   and `pricing`, a **900–1400 word German `overview`** with no headings), plus `domain`
   (bare favicon domain), and optionally `stealth: true` and a `cover_cue` (one English
   sentence describing an abstract magenta-accented brand symbol).

If nothing genuinely new and notable is found, write `[]` to
`scripts/pending_tools.json` and **stop** — do not deploy an empty batch.

## Step 2 — Seed + assets + deploy

Run: `bash scripts/weekly_discovery_run.sh`

This seeds CMS elements/posts/logos, registers the slugs in the capture + cover
scripts, captures screenshots, uploads them, generates cover images, deploys to
Netlify (`--build --prod`), and commits + pushes. It is idempotent and no-ops if
there is nothing to add.

## Step 3 — Fix blocked screenshots (use judgment)

Some sites defeat the bundled browser. After capture, spot-check the new
`screenshots/<slug>.jpg`. If one is a Cloudflare/Akamai **403 "Access Denied"**
page, a **blank** page, a **login wall**, or an endless SPA loader:
- set `stealth: true` for that slug in `scripts/capture_tool_screenshots.mjs` (routes via the Chrome channel + cookie dismissal), **or**
- swap its URL to a marketing/overview page that renders (e.g. a `/pricing` page, a blog announcement, or a `labs.*` page),

then delete that one `screenshots/<slug>.jpg`, re-run the capture (`cp scripts/capture_tool_screenshots.mjs web/capture_tmp.mjs && (cd web && node capture_tmp.mjs) && rm web/capture_tmp.mjs`), `python3 scripts/upload_screenshots.py`, `python3 scripts/generate_tool_images.py`, redeploy, and amend/commit.

Prior fixes for reference (see git log): Magnific & Higgsfield & Agentforce → `stealth`;
Kling → `app.klingai.com` pricing page; Whisk → blog announcement URL; Hailuo → `hailuoai.com` + stealth;
R Discovery → `researcher.life` parent. Logos that 404 on the favicon service can be skipped.

## Step 4 — Verify & report

For each newly-added slug, `curl -s -o /dev/null -w "%{http_code}" https://ki-toolnavigator.com/tool/<slug>`
and confirm **200**. Print a concise summary: each tool's name, category, and URL.

## Guardrails

- **Never** commit `.env` (it is gitignored — keep it that way).
- Cap at **5** new tools per run.
- Do not modify tools that already exist unless an update is clearly warranted (e.g. a major new version).
- Everything is in git and Netlify deploys are reversible — prefer shipping a smaller, correct batch over a large, sloppy one.
