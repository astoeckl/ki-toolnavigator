import type { Metadata } from 'next';
import { notFound } from 'next/navigation';
import Link from 'next/link';
import { getCategories, getTools } from '@/lib/cms';
import { getEditorialDates } from '@/lib/site';
import type { Tool } from '@/lib/types';
import { Badge, Breadcrumb, Button, SectionLabel, Thumb } from '@/components/ui';
import { CoverImage } from '@/components/CoverImage';
import { JsonLd } from '@/components/JsonLd';
import { breadcrumbLd, collectionPageLd, pageMetadata, summarize } from '@/lib/seo';
import { CategoryToolActions } from './CategoryToolActions';

function toolCover(t: Tool): string | null {
  if (typeof t.media_id === 'string') return t.media_id;
  if (t.media_id && typeof t.media_id === 'object') return t.media_id.url ?? null;
  return null;
}

export async function generateStaticParams() {
  const cats = await getCategories();
  return cats.map((c) => ({ slug: c.slug }));
}

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }): Promise<Metadata> {
  const { slug } = await params;
  const [categories, tools] = await Promise.all([getCategories(), getTools()]);
  const cat = categories.find((c) => c.slug === slug);
  if (!cat) return { title: 'Kategorie nicht gefunden', robots: { index: false, follow: false } };

  const items = tools.filter((t) => t.category === cat.slug);
  const names = items.slice(0, 4).map((t) => t.name).join(', ');

  return pageMetadata({
    // Kept short so the "· KI-Toolnavigator" suffix still fits in a SERP title.
    title: `${cat.name}: die besten KI-Tools`,
    description: summarize(
      `${cat.desc} ${items.length} Tools redaktionell geprüft${names ? ` — u. a. ${names}` : ''}. Mit Preisen, Funktionen und DSGVO-Einschätzung.`,
    ),
    path: `/kategorie/${cat.slug}`,
    image: firstCover(items),
    imageAlt: cat.name,
    keywords: [cat.name, `${cat.name} KI-Tools`, 'KI-Tools Vergleich', 'DSGVO', ...items.slice(0, 6).map((t) => t.name)],
  });
}

/** First tool cover in the category, used as the share image. */
function firstCover(items: Tool[]): string | null {
  for (const t of items) {
    const c = toolCover(t);
    if (c) return c;
  }
  return null;
}

export default async function CategoryPage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const [categories, tools] = await Promise.all([getCategories(), getTools()]);
  const cat = categories.find((c) => c.slug === slug);
  if (!cat) notFound();
  const items = tools.filter((t) => t.category === cat.slug);
  const editorial = await getEditorialDates(cat.slug);

  return (
    <div>
      <JsonLd data={[
        collectionPageLd(cat, items, { description: summarize(cat.desc, 300) }),
        breadcrumbLd([
          { name: 'Start', path: '/' },
          { name: 'Verzeichnis', path: '/verzeichnis' },
          { name: cat.name, path: `/kategorie/${cat.slug}` },
        ]),
      ]} />

      <Breadcrumb items={[
        { label: 'Start', href: '/' },
        { label: 'Verzeichnis', href: '/verzeichnis' },
        { label: cat.name },
      ]} />

      <div style={{ borderBottom: '1px solid var(--line)', paddingBottom: 40, marginBottom: 40 }}>
        <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#8a8580', letterSpacing: '0.08em', textTransform: 'uppercase', marginBottom: 14 }}>Kategorie</div>
        <h1 className="h-editorial-md" style={{ fontFamily: 'Fraunces, serif', fontWeight: 400, margin: 0, textWrap: 'balance' as const }}>{cat.name}</h1>
        <p style={{ fontFamily: 'Fraunces, serif', fontSize: 'clamp(17px, 2.4vw, 20px)', lineHeight: 1.5, color: 'var(--ink)', marginTop: 20, maxWidth: 720 }}>{cat.desc}</p>
        <div style={{ marginTop: 20, fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#8a8580', letterSpacing: '0.04em', textTransform: 'uppercase' }}>
          {items.length} Tools · zuletzt überprüft am {editorial.label}
        </div>
      </div>

      <div className="layout-kategorie">
        <div>
          <SectionLabel num="A">Top-Tools dieser Kategorie</SectionLabel>
          {items.length === 0 ? (
            <p style={{ fontFamily: 'Fraunces, serif', fontStyle: 'italic', color: 'var(--ink)', fontSize: 16 }}>
              Noch keine Tools in dieser Kategorie verzeichnet — die Redaktion arbeitet daran.
            </p>
          ) : (
            <div className="grid-2">
              {items.map((t) => {
                const cover = toolCover(t);
                return (
                <article key={t.slug} style={{ border: '1px solid var(--line)', padding: 20, display: 'flex', flexDirection: 'column', gap: 12 }}>
                  {cover ? (
                    <CoverImage
                      src={cover}
                      alt={`${t.name} — Vorschaubild`}
                      aspect="3 / 2"
                      sizes="(max-width: 540px) 92vw, (max-width: 900px) 47vw, (max-width: 1303px) calc((100vw - 424px) / 2), 408px"
                      bordered
                    />
                  ) : (
                    <Thumb name={t.name} slug={t.slug} aspect="3/2" />
                  )}
                  <div>
                    <Badge kind={t.dsgvo} />
                  </div>
                  <Link href={`/tool/${t.slug}`}>
                    <h3 style={{ fontFamily: 'Fraunces, serif', fontSize: 24, fontWeight: 500, margin: 0, letterSpacing: '-0.01em' }}>{t.name}</h3>
                  </Link>
                  <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 10, color: '#8a8580', letterSpacing: '0.04em', textTransform: 'uppercase' }}>{t.vendor} · {t.origin}</div>
                  <p style={{ margin: 0, fontSize: 13, lineHeight: 1.5, color: 'var(--ink)' }}>{t.tagline}</p>
                  <CategoryToolActions slug={t.slug} />
                </article>
                );
              })}
            </div>
          )}
        </div>

        <aside>
          <div style={{ border: '1px solid var(--line)', padding: 20 }}>
            <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#8a8580', letterSpacing: '0.08em', textTransform: 'uppercase', marginBottom: 12 }}>Siehe auch</div>
            <ul style={{ listStyle: 'none', padding: 0, margin: 0 }}>
              {categories.filter((c) => c.slug !== cat.slug).slice(0, 5).map((c) => (
                <li key={c.slug} style={{ padding: '6px 0', borderBottom: '1px dotted var(--line)' }}>
                  <Link href={`/kategorie/${c.slug}`} style={{ color: 'var(--accent)', fontSize: 13, borderBottom: '1px dotted var(--accent)' }}>{c.name}</Link>
                </li>
              ))}
            </ul>
          </div>
          <div style={{ border: '1px solid var(--line)', padding: 20, marginTop: 20 }}>
            <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#8a8580', letterSpacing: '0.08em', textTransform: 'uppercase', marginBottom: 12 }}>Auswahlhilfe</div>
            <p style={{ fontSize: 13, lineHeight: 1.5, margin: '0 0 12px', color: 'var(--ink)' }}>
              Wählen Sie <b>2 bis 4 Tools</b> zum direkten Vergleich aus — Preise, Funktionen, DSGVO und mehr in tabellarischer Gegenüberstellung.
            </p>
            <Button variant="primary" href="/vergleich">Zum Vergleich →</Button>
          </div>
        </aside>
      </div>
    </div>
  );
}
