export const meta = {
  name: 'weekly-tool-discovery',
  description: 'Discover newly-launched/updated AI tools, dedupe against the live KI-Toolnavigator catalogue, and write full German editorial records to scripts/pending_tools.json ready for the seed pipeline.',
  whenToUse: 'Weekly (Sundays) to keep the AI-tools directory current. Produces draft records; the deterministic seed/deploy tail runs separately.',
  phases: [
    { title: 'Snapshot', detail: 'read the live catalogue (existing slugs) from the CMS' },
    { title: 'Research', detail: 'parallel web sweeps across categories + launch trackers' },
    { title: 'Select', detail: 'dedupe + rank; pick genuinely-new, notable tools' },
    { title: 'Author', detail: 'write a full German editorial record per selected tool' },
    { title: 'Write', detail: 'persist scripts/pending_tools.json' },
  ],
}

// ---- args: { max?: number, todayISO?: string, categories?: string[] } ----
const MAX = (args && args.max) || 5
const TODAY = (args && args.todayISO) || '2026 (this year)'
const CATEGORIES = [
  'sprachmodelle', 'bildgenerierung', 'video-audio', 'coding', 'agenten',
  'produktivitaet', 'daten-analyse', 'marketing', 'forschung',
]

// ---------- schemas ----------
const CANDIDATES_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  required: ['candidates'],
  properties: {
    candidates: {
      type: 'array',
      items: {
        type: 'object',
        additionalProperties: false,
        required: ['name', 'vendor', 'category', 'website', 'why_notable', 'recency'],
        properties: {
          name: { type: 'string' },
          vendor: { type: 'string' },
          category: { type: 'string', enum: CATEGORIES },
          website: { type: 'string' },
          why_notable: { type: 'string' },
          recency: { type: 'string', description: 'When launched or significantly updated (month/year).' },
        },
      },
    },
  },
}

const SELECTION_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  required: ['selected'],
  properties: {
    selected: {
      type: 'array',
      items: {
        type: 'object',
        additionalProperties: false,
        required: ['slug', 'name', 'vendor', 'category', 'website', 'reason'],
        properties: {
          slug: { type: 'string', description: 'kebab-case, unique, not in existing list' },
          name: { type: 'string' },
          vendor: { type: 'string' },
          category: { type: 'string', enum: CATEGORIES },
          website: { type: 'string' },
          reason: { type: 'string', description: 'one line: why notable + why genuinely new' },
        },
      },
    },
  },
}

const RECORD_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  required: ['slug', 'name', 'vendor', 'category', 'tagline', 'price', 'api', 'dsgvo',
    'origin', 'rating', 'reviews', 'pros', 'cons', 'usecases', 'launched',
    'lastUpdated', 'website', 'domain', 'features', 'pricing', 'overview', 'cover_cue'],
  properties: {
    slug: { type: 'string' },
    name: { type: 'string' },
    vendor: { type: 'string' },
    category: { type: 'string', enum: CATEGORIES },
    tagline: { type: 'string' },
    price: { type: 'string' },
    api: { type: 'boolean' },
    dsgvo: { type: 'string', enum: ['ja', 'bedingt', 'nein'] },
    origin: { type: 'string' },
    rating: { type: 'number' },
    reviews: { type: 'integer' },
    pros: { type: 'array', items: { type: 'string' }, minItems: 3, maxItems: 4 },
    cons: { type: 'array', items: { type: 'string' }, minItems: 3, maxItems: 4 },
    usecases: { type: 'array', items: { type: 'string' }, minItems: 3, maxItems: 4 },
    launched: { type: 'string', description: 'YYYY-MM-DD' },
    lastUpdated: { type: 'string', description: 'YYYY-MM-DD' },
    website: { type: 'string' },
    domain: { type: 'string', description: 'bare domain for favicon, e.g. example.com' },
    features: { type: 'string', description: 'German markdown bullet list' },
    pricing: { type: 'string', description: 'German markdown bullet list' },
    overview: { type: 'string', minLength: 900, description: 'German editorial overview, ~900-1400 words, no headings' },
    stealth: { type: 'boolean', description: 'true if the site is Cloudflare/Akamai-protected and needs Chrome-channel capture' },
    cover_cue: { type: 'string', description: 'one-sentence abstract brand-style symbol description for the cover image' },
  },
}

// ---------- Phase 1: Snapshot ----------
phase('Snapshot')
const snapshotRaw = await agent(
  `Run exactly this command and return ONLY the JSON it prints (no prose):\n\n` +
  `cd "/Users/astoeckl/Documents/tool navigator" && python3 scripts/list_slugs.py\n\n` +
  `The output is a JSON object {"count":N,"tools":[{slug,name,vendor,category}]}. Return it verbatim.`,
  { label: 'snapshot:catalogue', phase: 'Snapshot',
    schema: { type: 'object', additionalProperties: true, required: ['count', 'tools'],
      properties: { count: { type: 'integer' }, tools: { type: 'array', items: { type: 'object', additionalProperties: true } } } } }
)
const existingSlugs = new Set((snapshotRaw.tools || []).map((t) => (t.slug || '').toLowerCase()))
const existingNames = new Set((snapshotRaw.tools || []).map((t) => (t.name || '').toLowerCase()))
log(`Catalogue snapshot: ${existingSlugs.size} existing tools.`)

// ---------- Phase 2: Research (parallel, multi-angle) ----------
phase('Research')
const ANGLES = [
  ...CATEGORIES.map((c) => ({
    key: `cat:${c}`,
    prompt: `Find AI tools in the category "${c}" that were newly launched OR significantly updated recently (around ${TODAY}). ` +
      `Use web search. Prefer notable, real, generally-available products with a working website. ` +
      `Return up to 5 candidates with name, vendor, the SAME category "${c}", website (full URL), a one-line why_notable, and recency (month/year of launch/update).`,
  })),
  {
    key: 'launch-trackers',
    prompt: `Search launch trackers and AI-news roundups (Product Hunt, There's An AI For That, Hacker News, TechCrunch AI, Ben's Bites) for notable AI tools launched or majorly updated recently (around ${TODAY}). ` +
      `Return up to 8 candidates. For each, pick the single best-fitting category from this exact list: ${CATEGORIES.join(', ')}. ` +
      `Include name, vendor, that category, website (full URL), one-line why_notable, recency.`,
  },
]
const research = await parallel(ANGLES.map((a) => () =>
  agent(a.prompt, { label: `research:${a.key}`, phase: 'Research', schema: CANDIDATES_SCHEMA })
    .then((r) => (r && r.candidates) || [])
    .catch(() => [])
))
const allCandidates = research.flat().filter(Boolean)
log(`Gathered ${allCandidates.length} raw candidates across ${ANGLES.length} angles.`)

// dedupe candidates by name (plain code) + drop ones already in catalogue
const seen = new Set()
const freshCandidates = []
for (const c of allCandidates) {
  const n = (c.name || '').trim().toLowerCase()
  if (!n || seen.has(n)) continue
  seen.add(n)
  if (existingNames.has(n)) continue
  freshCandidates.push(c)
}
log(`${freshCandidates.length} candidates after dedupe vs. catalogue.`)

if (freshCandidates.length === 0) {
  log('No new candidates found this week. Writing empty pending list.')
  await agent(
    `Write the file "/Users/astoeckl/Documents/tool navigator/scripts/pending_tools.json" with exactly this content:\n[]\n` +
    `Then reply DONE.`,
    { label: 'write:empty', phase: 'Write' })
  return { count: 0, tools: [], summary: 'No new tools found this week.' }
}

// ---------- Phase 3: Select ----------
phase('Select')
const selection = await agent(
  `You curate a high-quality German AI-tools directory. From the candidate list below, select the ${MAX} BEST genuinely-new, notable tools to add this week.\n\n` +
  `Rules:\n` +
  `- Do NOT select anything whose slug or name already exists. Existing slugs: ${[...existingSlugs].join(', ')}\n` +
  `- Assign each a unique kebab-case slug not in that list.\n` +
  `- Keep the category to one of: ${CATEGORIES.join(', ')}.\n` +
  `- Prefer real, generally-available, distinctive tools over thin wrappers or vaporware.\n` +
  `- Spread across categories where possible; at most ${MAX} total.\n\n` +
  `Candidates (JSON):\n${JSON.stringify(freshCandidates, null, 0)}`,
  { label: 'select:curate', phase: 'Select', schema: SELECTION_SCHEMA }
)
let selected = (selection.selected || []).filter((s) => !existingSlugs.has((s.slug || '').toLowerCase()))
selected = selected.slice(0, MAX)
log(`Selected ${selected.length} tool(s): ${selected.map((s) => s.slug).join(', ')}`)

if (selected.length === 0) {
  await agent(
    `Write the file "/Users/astoeckl/Documents/tool navigator/scripts/pending_tools.json" with exactly this content:\n[]\nThen reply DONE.`,
    { label: 'write:empty', phase: 'Write' })
  return { count: 0, tools: [], summary: 'Candidates found but none passed selection.' }
}

// ---------- Phase 4: Author (one full German record per tool, in parallel) ----------
phase('Author')
const records = await parallel(selected.map((s) => () =>
  agent(
    `Write a complete German editorial record for the AI tool below, for the "KI-Toolnavigator" directory. ` +
    `Match the house style of the existing catalogue: sober, knowledgeable, German, with concrete detail and honest trade-offs.\n\n` +
    `Tool: ${s.name} by ${s.vendor}\nWebsite: ${s.website}\nCategory: ${s.category}\nSlug (use exactly): ${s.slug}\nWhy notable: ${s.reason}\n\n` +
    `Research the tool with web search first to get facts right (real pricing, origin country, capabilities, launch date). Then produce the record.\n\n` +
    `Requirements:\n` +
    `- slug: "${s.slug}" exactly. category: "${s.category}" exactly.\n` +
    `- tagline: one punchy German sentence.\n` +
    `- price: short German pricing summary (e.g. "Free · Pro ab 20 $/Mon.").\n` +
    `- api (bool), dsgvo ("ja"|"bedingt"|"nein"), origin (country in German), rating (4.0–4.9 realistic), reviews (integer, plausible).\n` +
    `- pros/cons/usecases: 3–4 short German bullet strings each.\n` +
    `- launched / lastUpdated: YYYY-MM-DD (lastUpdated = today: ${TODAY}).\n` +
    `- domain: bare favicon domain (e.g. "example.com").\n` +
    `- features: German markdown bullet list (- …), 6–8 bullets.\n` +
    `- pricing: German markdown bullet list of the tiers.\n` +
    `- overview: 900–1400 words German editorial prose, NO markdown headings, paragraphs separated by blank lines, bolding sparingly with **…**. End with a recommendation.\n` +
    `- stealth: true ONLY if the marketing site is behind Cloudflare/Akamai bot-protection.\n` +
    `- cover_cue: one English sentence describing an abstract, hand-drawn brand-style symbol with a single magenta accent (matches the directory's editorial illustration style).`,
    { label: `author:${s.slug}`, phase: 'Author', schema: RECORD_SCHEMA }
  ).then((rec) => ({ ...rec, slug: s.slug, category: s.category }))
   .catch(() => null)
))
const finalRecords = records.filter(Boolean).filter((r) => !existingSlugs.has((r.slug || '').toLowerCase()))
log(`Authored ${finalRecords.length} full record(s).`)

// ---------- Phase 5: Write pending_tools.json ----------
phase('Write')
await agent(
  `Write the file "/Users/astoeckl/Documents/tool navigator/scripts/pending_tools.json".\n` +
  `Its content must be EXACTLY this JSON (a JSON array), nothing else:\n\n` +
  '```json\n' + JSON.stringify(finalRecords, null, 2) + '\n```\n\n' +
  `After writing, run \`python3 -c "import json;print(len(json.load(open('/Users/astoeckl/Documents/tool navigator/scripts/pending_tools.json'))))"\` to confirm it parses, then reply with the count.`,
  { label: 'write:pending', phase: 'Write' }
)

return {
  count: finalRecords.length,
  tools: finalRecords.map((r) => ({ slug: r.slug, name: r.name, category: r.category })),
  summary: `Wrote ${finalRecords.length} new tool record(s) to scripts/pending_tools.json: ` +
    finalRecords.map((r) => `${r.name} (${r.category})`).join(', '),
}
