#!/usr/bin/env node
/**
 * Capture website screenshots for every tool we list.
 * Saves JPGs into ./screenshots/<slug>.jpg.
 * Skips a tool if its screenshot already exists (idempotent).
 *
 * Run from repo root:  node scripts/capture_tool_screenshots.mjs
 */
import { chromium } from 'playwright';
import { mkdirSync, existsSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const OUT = resolve(ROOT, 'screenshots');
mkdirSync(OUT, { recursive: true });

const TOOLS = [
  { slug: 'chatgpt',          url: 'https://chatgpt.com' },
  { slug: 'claude',           url: 'https://www.anthropic.com/claude' },
  { slug: 'gemini',           url: 'https://deepmind.google/technologies/gemini/' },
  { slug: 'mistral',          url: 'https://chat.mistral.ai/' },
  { slug: 'midjourney',       url: 'https://www.midjourney.com/home' },
  { slug: 'stable-diffusion', url: 'https://stability.ai/stable-image' },
  { slug: 'elevenlabs',       url: 'https://elevenlabs.io/' },
  { slug: 'runway',           url: 'https://runwayml.com/' },
  { slug: 'cursor',           url: 'https://cursor.com/' },
  { slug: 'copilot',          url: 'https://github.com/features/copilot' },
  { slug: 'notion-ai',        url: 'https://www.notion.so/product/ai' },
  { slug: 'perplexity',       url: 'https://www.perplexity.ai/' },
  { slug: 'deepl-write',      url: 'https://www.deepl.com/write' },
  { slug: 'aleph-alpha',      url: 'https://aleph-alpha.com/' },
  // ---- new tools ----
  { slug: 'ms-copilot',       url: 'https://www.microsoft.com/en-us/microsoft-copilot' },
  { slug: 'grok',             url: 'https://grok.com/' },
  { slug: 'deepseek',         url: 'https://www.deepseek.com/' },
  { slug: 'flux',             url: 'https://bfl.ai/' },
  { slug: 'ideogram',         url: 'https://ideogram.ai/' },
  { slug: 'adobe-firefly',    url: 'https://firefly.adobe.com/' },
  { slug: 'suno',             url: 'https://suno.com/' },
  { slug: 'synthesia',        url: 'https://www.synthesia.io/' },
  { slug: 'windsurf',         url: 'https://windsurf.com/' },
  { slug: 'n8n',              url: 'https://n8n.io/' },
  { slug: 'make',             url: 'https://www.make.com/' },
  { slug: 'notebooklm',       url: 'https://notebooklm.google.com/' },
  { slug: 'julius',           url: 'https://julius.ai/' },
  { slug: 'neuroflash',       url: 'https://neuroflash.com/de/' },
  { slug: 'elicit',           url: 'https://elicit.com/' },
  // ---- April 2026 batch ----
  { slug: 'llama',            url: 'https://llama.com/' },
  { slug: 'cohere',           url: 'https://cohere.com/' },
  { slug: 'recraft',          url: 'https://www.recraft.ai/' },
  { slug: 'pika',             url: 'https://pika.art/' },
  { slug: 'heygen',           url: 'https://www.heygen.com/' },
  { slug: 'descript',         url: 'https://www.descript.com/' },
  { slug: 'replit',           url: 'https://replit.com/' },
  { slug: 'zapier',           url: 'https://zapier.com/' },
  { slug: 'otter',            url: 'https://otter.ai/' },
  { slug: 'hex',              url: 'https://hex.tech/' },
  { slug: 'jasper',           url: 'https://www.jasper.ai/' },
  { slug: 'consensus',        url: 'https://consensus.app/' },
  // ---- Marketing batch April 2026 ----
  { slug: 'copy-ai',           url: 'https://www.copy.ai/' },
  { slug: 'writesonic',        url: 'https://writesonic.com/' },
  { slug: 'surfer-seo',        url: 'https://surferseo.com/' },
  { slug: 'frase',             url: 'https://www.frase.io/' },
  { slug: 'anyword',           url: 'https://anyword.com/' },
  { slug: 'typeface',          url: 'https://www.typeface.ai/' },
  { slug: 'canva-magic',       url: 'https://www.canva.com/magic/' },
  // ---- Agenten batch April 2026 ----
  { slug: 'manus',             url: 'https://manus.im/' },
  { slug: 'devin',             url: 'https://devin.ai/' },
  { slug: 'lindy',             url: 'https://www.lindy.ai/' },
  { slug: 'crewai',            url: 'https://www.crewai.com/' },
  { slug: 'langchain',         url: 'https://www.langchain.com/' },
  { slug: 'relevance-ai',      url: 'https://relevanceai.com/' },
  { slug: 'activepieces',      url: 'https://www.activepieces.com/' },
  // ---- Daten & Analyse batch April 2026 ----
  { slug: 'powerbi-copilot',   url: 'https://www.microsoft.com/en-us/power-platform/products/power-bi' },
  { slug: 'thoughtspot',       url: 'https://www.thoughtspot.com/' },
  { slug: 'databricks-genie',  url: 'https://www.databricks.com/product/ai-bi' },
  { slug: 'rows',              url: 'https://rows.com/' },
  { slug: 'akkio',             url: 'https://www.akkio.com/' },
  { slug: 'vanna-ai',          url: 'https://vanna.ai/' },
  { slug: 'dataiku',           url: 'https://www.dataiku.com/' },
  // ---- Coding batch April 2026 ----
  { slug: 'claude-code',       url: 'https://www.anthropic.com/claude-code' },
  { slug: 'codex-cli',         url: 'https://developers.openai.com/codex/cli/' },
  { slug: 'bolt',              url: 'https://bolt.new/' },
  { slug: 'v0',                url: 'https://v0.app/' },
  { slug: 'tabnine',           url: 'https://www.tabnine.com/' },
  { slug: 'continue',          url: 'https://www.continue.dev/' },
  { slug: 'aider',             url: 'https://aider.chat/' },
  // ---- Wissenschaft & Forschung batch April 2026 ----
  { slug: 'scispace',          url: 'https://typeset.io/' },
  { slug: 'scite',             url: 'https://scite.ai/' },
  { slug: 'researchrabbit',    url: 'https://www.researchrabbitapp.com/' },
  { slug: 'connected-papers',  url: 'https://www.connectedpapers.com/' },
  { slug: 'semantic-scholar',  url: 'https://www.semanticscholar.org/' },
  { slug: 'litmaps',           url: 'https://www.litmaps.com/' },
  { slug: 'scholarcy',         url: 'https://www.scholarcy.com/' },
  // ---- Produktivität & Wissen batch April 2026 ----
  { slug: 'mem',               url: 'https://get.mem.ai/' },
  { slug: 'reflect',           url: 'https://reflect.app/' },
  { slug: 'tana',              url: 'https://tana.inc/' },
  { slug: 'glean',             url: 'https://www.glean.com/' },
  { slug: 'motion',            url: 'https://www.usemotion.com/' },
  { slug: 'reclaim',           url: 'https://reclaim.ai/' },
  { slug: 'granola',           url: 'https://www.granola.ai/' },
  // ---- Bildgenerierung batch April 2026 ----
  { slug: 'gpt-image',         url: 'https://platform.openai.com/docs/guides/image-generation' },
  { slug: 'nano-banana',       url: 'https://deepmind.google/models/gemini-image/' },
  { slug: 'leonardo-ai',       url: 'https://leonardo.ai/' },
  { slug: 'krea',              url: 'https://www.krea.ai/' },
  { slug: 'reve',              url: 'https://reve.com/' },
  { slug: 'magnific',          url: 'https://magnific.ai/',          stealth: true },
  { slug: 'freepik-ai',        url: 'https://www.freepik.com/',       stealth: true },
];

const VIEWPORT = { width: 1280, height: 800 };

// Some sites (Cloudflare-protected: freepik.com, magnific.ai, …) refuse the bundled
// Playwright Chromium. The installed Chrome channel + a couple of stealth tweaks
// pass them. Mark such tools with `stealth: true`.
const COOKIE_BUTTONS = [
  'button:has-text("Accept all cookies")',
  'button:has-text("Accept All")',
  'button:has-text("Accept all")',
  'button:has-text("Reject all")',
  'button:has-text("Alle akzeptieren")',
  'button:has-text("Alle Cookies akzeptieren")',
  'button:has-text("Alle ablehnen")',
  '[aria-label="Accept all"]',
];

async function captureOne(browsers, tool) {
  const out = resolve(OUT, `${tool.slug}.jpg`);
  if (existsSync(out)) {
    console.log(`  ·  ${tool.slug.padEnd(20)} already exists, skipping`);
    return { ok: true, skipped: true };
  }
  const browser = tool.stealth ? browsers.chrome : browsers.chromium;
  const ctx = await browser.newContext({
    viewport: VIEWPORT,
    locale: tool.stealth ? 'en-US' : 'de-DE',
    userAgent:
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    extraHTTPHeaders: tool.stealth ? {
      'Accept-Language': 'en-US,en;q=0.9',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
      'Referer': 'https://www.google.com/',
    } : undefined,
  });
  if (tool.stealth) {
    await ctx.addInitScript(() => {
      Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
      Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] });
    });
  }
  const page = await ctx.newPage();
  try {
    console.log(`  →  ${tool.slug.padEnd(20)} ${tool.url}${tool.stealth ? '  [stealth]' : ''}`);
    await page.goto(tool.url, {
      waitUntil: 'domcontentloaded',
      timeout: 30000,
      referer: tool.stealth ? 'https://www.google.com/' : undefined,
    });
    await page.waitForTimeout(3000);
    if (tool.stealth) {
      // Best-effort cookie banner dismissal
      for (const sel of COOKIE_BUTTONS) {
        try {
          const btn = await page.$(sel);
          if (btn) { await btn.click({ timeout: 2000 }); break; }
        } catch {}
      }
      // Best-effort overlay close (e.g. "Freepik is now Magnific" promo box)
      try {
        const closes = await page.$$('button[aria-label="Close"]');
        for (const c of closes) { try { await c.click({ timeout: 1000 }); } catch {} }
      } catch {}
      await page.waitForTimeout(2000);
    }
    await page.screenshot({ path: out, type: 'jpeg', quality: 88, fullPage: false });
    console.log(`     ✓  saved ${out.split('/').slice(-2).join('/')}`);
    return { ok: true };
  } catch (err) {
    console.log(`     ✗  ${err.message.split('\n')[0]}`);
    return { ok: false, err: err.message };
  } finally {
    await ctx.close();
  }
}

(async () => {
  const chromiumBrowser = await chromium.launch({ headless: true });
  // Chrome channel is optional — only launch if at least one tool wants stealth.
  const wantsStealth = TOOLS.some((t) => t.stealth);
  let chromeBrowser = null;
  if (wantsStealth) {
    try {
      chromeBrowser = await chromium.launch({
        headless: true,
        channel: 'chrome',
        args: ['--disable-blink-features=AutomationControlled'],
      });
    } catch (err) {
      console.log(`(stealth disabled: 'chrome' channel not installed — ${err.message.split('\n')[0]})`);
    }
  }
  const browsers = { chromium: chromiumBrowser, chrome: chromeBrowser ?? chromiumBrowser };
  console.log('Capturing screenshots into', OUT);
  let okCount = 0, skipCount = 0, failCount = 0;
  for (const tool of TOOLS) {
    const r = await captureOne(browsers, tool);
    if (r.skipped) skipCount++;
    else if (r.ok) okCount++;
    else failCount++;
  }
  await chromiumBrowser.close();
  if (chromeBrowser) await chromeBrowser.close();
  console.log(`\nDone: ${okCount} new · ${skipCount} skipped · ${failCount} failed`);
  if (failCount) process.exit(2);
})();
