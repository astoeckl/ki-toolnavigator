import Link from 'next/link';
import { searchCms, getCategories } from '@/lib/cms';
import type { SearchHit } from '@/lib/types';
import { Breadcrumb, Chip } from '@/components/ui';
import { SearchBar } from '@/components/SearchBar';

export const metadata = { title: 'Suche · KI-Toolnavigator' };

/**
 * Map a Cognitor search hit to an internal route. We rely on:
 *   - content_type_identifier (for content_element hits) — "tool" | "article" | "category"
 *   - doc_type === "post"  → look up which content_element references it (skipped here:
 *                            the public elements API resolves post_id back to the parent
 *                            element via search if the parent element matches too;
 *                            posts that surface alone link to the parent slug if known)
 */
function hrefForHit(hit: SearchHit, ctx: { tools: { id: number; slug: string }[]; articles: { id: number; slug: string }[]; categories: { slug: string; name: string }[] }): string | null {
  if (hit.doc_type === 'content_element') {
    const ct = hit.content_type_identifier;
    const slugFromTitle = (kind: 'tool' | 'article' | 'category', titles: { id: number; slug: string }[]) => {
      const found = titles.find((x) => x.id === hit.id);
      return found ? `/${kind === 'category' ? 'kategorie' : kind}/${found.slug}` : null;
    };
    if (ct === 'tool') return slugFromTitle('tool', ctx.tools);
    if (ct === 'article') return slugFromTitle('article', ctx.articles);
    if (ct === 'category') {
      const found = ctx.categories.find((c) => c.name === hit.title);
      return found ? `/kategorie/${found.slug}` : null;
    }
  }
  if (hit.doc_type === 'post') {
    // Try to find a tool/article that owns a Post with this title
    const t = ctx.tools.find((x) => hit.title.startsWith(x.slug)) ;
    if (t) return `/tool/${t.slug}`;
    const a = ctx.articles.find((x) => x.slug);
    return a ? `/artikel/${a.slug}` : null;
  }
  return null;
}

const labelFor = (ct?: string | null, doc_type?: string) => {
  if (ct === 'tool') return 'Tool';
  if (ct === 'article') return 'Artikel';
  if (ct === 'category') return 'Kategorie';
  if (doc_type === 'post') return 'Beitrag';
  return doc_type ?? '—';
};

export default async function SearchPage({
  searchParams,
}: {
  searchParams: Promise<{ q?: string }>;
}) {
  const { q = '' } = await searchParams;

  // Fetch search + minimal index for slug resolution in parallel
  const [searchResult, categories] = await Promise.all([
    q ? searchCms(q, { size: 30 }) : Promise.resolve({ results: [], total: 0 }),
    getCategories(),
  ]);

  // For mapping hit ids → slugs we need a lightweight index of tools/articles
  const [{ getTools, getArticles }] = await Promise.all([import('@/lib/cms')]);
  const [tools, articles] = await Promise.all([getTools(), getArticles()]);

  // Public elements endpoint doesn't expose ids in hit objects directly, so we
  // also build a name → slug index for fallback.
  const toolsIndex = tools.map((t) => ({ id: 0, slug: t.slug, name: t.name }));
  const articlesIndex = articles.map((a) => ({ id: 0, slug: a.slug, name: a.title }));

  return (
    <div>
      <Breadcrumb items={[{ label: 'Start', href: '/' }, { label: 'Suche' }]} />

      <div style={{ borderBottom: '1px solid var(--line)', paddingBottom: 32, marginBottom: 32 }}>
        <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#8a8580', letterSpacing: '0.08em', textTransform: 'uppercase', marginBottom: 12 }}>
          Volltextsuche · Cognitor
        </div>
        <h1 className="h-editorial-sm" style={{ fontFamily: 'Fraunces, serif', fontWeight: 400, margin: '0 0 22px', textWrap: 'balance' as const }}>
          {q ? <>Ergebnisse für „<span style={{ fontStyle: 'italic' }}>{q}</span>"</> : 'Suche'}
        </h1>
        <SearchBar variant="hero" defaultValue={q} />
        {q && (
          <div style={{ marginTop: 16, fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#8a8580', letterSpacing: '0.04em', textTransform: 'uppercase' }}>
            {searchResult.total ?? searchResult.results.length} Treffer
          </div>
        )}
      </div>

      {!q && (
        <p style={{ fontFamily: 'Fraunces, serif', fontStyle: 'italic', color: 'var(--ink)', fontSize: 18 }}>
          Geben Sie einen Suchbegriff ein — Tools, Artikel und Kategorien werden über die Cognitor-Volltextsuche durchsucht.
        </p>
      )}

      {q && searchResult.results.length === 0 && (
        <p style={{ fontFamily: 'Fraunces, serif', fontStyle: 'italic', color: 'var(--ink)', fontSize: 18 }}>
          Keine Treffer für „{q}". Versuchen Sie einen anderen Begriff.
        </p>
      )}

      <ul style={{ listStyle: 'none', padding: 0, margin: 0 }}>
        {searchResult.results.map((hit, i) => {
          const ct = hit.content_type_identifier;
          // Resolve href via name-match (since hit.id is a CMS internal id, not the slug)
          let href: string | null = null;
          if (ct === 'tool') {
            const t = tools.find((x) => x.name === hit.title);
            href = t ? `/tool/${t.slug}` : null;
          } else if (ct === 'article') {
            const a = articles.find((x) => x.title === hit.title);
            href = a ? `/artikel/${a.slug}` : null;
          } else if (ct === 'category') {
            const c = categories.find((x) => x.name === hit.title);
            href = c ? `/kategorie/${c.slug}` : null;
          } else if (hit.doc_type === 'post') {
            // Posts are owned by tool overviews ("X — Übersicht") or articles (matching title)
            const m = hit.title.match(/^(.+?)\s+—\s+Übersicht$/);
            if (m) {
              const t = tools.find((x) => x.name === m[1]);
              if (t) href = `/tool/${t.slug}`;
            } else {
              const a = articles.find((x) => x.title === hit.title);
              if (a) href = `/artikel/${a.slug}`;
            }
          }

          // Pick a snippet — prefer highlighted content, fallback to plain content
          const snippetHtml = hit.highlight?.content?.[0] ?? hit.highlight?.title?.[0] ?? null;
          const snippetText = hit.content?.slice(0, 240) ?? '';

          const Inner = (
            <article style={{
              padding: '22px 0', borderBottom: '1px solid var(--line)',
              display: 'flex', flexDirection: 'column', gap: 8,
              minWidth: 0, wordBreak: 'break-word', overflowWrap: 'anywhere',
            }}>
              <div style={{ display: 'flex', gap: 10, alignItems: 'center', flexWrap: 'wrap' }}>
                <Chip>{labelFor(ct, hit.doc_type)}</Chip>
                <span style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 10, color: '#8a8580', letterSpacing: '0.04em', textTransform: 'uppercase' }}>
                  Score {hit.score.toFixed(2)}
                </span>
              </div>
              <h3 style={{ fontFamily: 'Fraunces, serif', fontSize: 'clamp(20px, 3vw, 26px)', fontWeight: 500, margin: 0, letterSpacing: '-0.01em', lineHeight: 1.15 }}>
                <span dangerouslySetInnerHTML={{ __html: hit.highlight?.title?.[0] ?? hit.title }} />
              </h3>
              {hit.description && (
                <p style={{ margin: 0, fontFamily: 'Fraunces, serif', fontStyle: 'italic', color: 'var(--ink)', fontSize: 15, lineHeight: 1.5 }}>
                  {hit.description}
                </p>
              )}
              {snippetHtml ? (
                <p style={{ margin: 0, fontSize: 14, lineHeight: 1.6, color: 'var(--ink)' }}
                   dangerouslySetInnerHTML={{ __html: snippetHtml }} />
              ) : (
                snippetText && (
                  <p style={{ margin: 0, fontSize: 14, lineHeight: 1.6, color: 'var(--ink)' }}>
                    {snippetText}…
                  </p>
                )
              )}
              {href && (
                <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 10, color: 'var(--accent)', letterSpacing: '0.06em', textTransform: 'uppercase', wordBreak: 'break-all' }}>
                  {href} →
                </div>
              )}
            </article>
          );

          return (
            <li key={`${hit.doc_type}-${hit.id}-${i}`}>
              {href ? <Link href={href}>{Inner}</Link> : Inner}
            </li>
          );
        })}
      </ul>
    </div>
  );
}
