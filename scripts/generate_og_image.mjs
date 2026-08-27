#!/usr/bin/env node
/**
 * Renders the default OpenGraph/Twitter share card to web/public/og-default.png (1200×630).
 * Static output — re-run only when the brand or claim changes:
 *   node scripts/generate_og_image.mjs
 */
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const OUT = join(ROOT, 'web', 'public', 'og-default.png');

// Playwright lives in web/node_modules — resolve it from there, not from repo root.
const require = createRequire(join(ROOT, 'web', 'package.json'));
const { chromium } = require('playwright');

const HTML = `<!doctype html>
<html lang="de"><head><meta charset="utf-8">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400..600&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<style>
  * { box-sizing: border-box; margin: 0; }
  body {
    width: 1200px; height: 630px; background: #FAF8F5; color: #17140F;
    font-family: 'Fraunces', Georgia, serif;
    display: flex; flex-direction: column; justify-content: space-between;
    padding: 68px 76px; position: relative; overflow: hidden;
  }
  .rule { position: absolute; left: 0; right: 0; height: 1px; background: #DDD7CC; }
  .eyebrow {
    font-family: 'JetBrains Mono', monospace; font-size: 19px; font-weight: 500;
    letter-spacing: 0.16em; text-transform: uppercase; color: #8a8580;
  }
  h1 { font-size: 92px; font-weight: 400; line-height: 1.02; letter-spacing: -0.028em; max-width: 940px; }
  h1 .dot { color: #A01E78; }
  p { font-size: 32px; line-height: 1.35; color: #5A5550; max-width: 820px; margin-top: 26px; font-weight: 400; }
  footer { display: flex; align-items: center; justify-content: space-between; }
  .brand { display: flex; align-items: center; gap: 18px; }
  .brand span {
    font-family: 'JetBrains Mono', monospace; font-size: 20px; font-weight: 500;
    letter-spacing: 0.1em; text-transform: uppercase; color: #17140F;
  }
  .url { font-family: 'JetBrains Mono', monospace; font-size: 20px; letter-spacing: 0.06em; color: #A01E78; }
</style></head>
<body>
  <div class="rule" style="top:0;height:8px;background:#17140F"></div>
  <div>
    <div class="eyebrow">Kuratiertes Verzeichnis · Deutsch · DSGVO-geprüft</div>
    <h1 style="margin-top:34px">KI-Tools, geprüft,<br>verglichen und erklärt<span class="dot">.</span></h1>
    <p>Redaktionelle Steckbriefe zu Funktionen, Preisen und Datenschutz — für den deutschsprachigen Raum.</p>
  </div>
  <footer>
    <div class="brand">
      <svg width="52" height="52" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M10 52 L54 52 L22 10 Z" stroke="#17140F" stroke-width="4" fill="none" stroke-linejoin="miter"/>
        <line x1="22" y1="10" x2="40" y2="44" stroke="#17140F" stroke-width="4"/>
        <circle cx="40" cy="44" r="6" fill="#A01E78"/>
      </svg>
      <span>KI-Toolnavigator</span>
    </div>
    <div class="url">ki-toolnavigator.com</div>
  </footer>
</body></html>`;

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1200, height: 630 }, deviceScaleFactor: 1 });
await page.setContent(HTML, { waitUntil: 'networkidle' });
await page.evaluate(() => document.fonts.ready);
await page.screenshot({ path: OUT, type: 'png' });
await browser.close();
console.log(`wrote ${OUT}`);
