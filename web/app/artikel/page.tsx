import type { Metadata } from 'next';
import Link from 'next/link';
import { getArticles } from '@/lib/cms';
import type { Article } from '@/lib/types';
import { Breadcrumb, Chip, SectionLabel, Thumb } from '@/components/ui';
import { CoverImage } from '@/components/CoverImage';
import { JsonLd } from '@/components/JsonLd';
import { breadcrumbLd, itemListLd, pageMetadata } from '@/lib/seo';

function cover(a: Article): string | null {
  if (typeof a.media_id === 'string') return a.media_id || null;
  if (a.media_id && typeof a.media_id === 'object') return a.media_id.url ?? null;
  return null;
}

/** Newest first — `date` is the editorial publication date. */
function byDateDesc(a: Article, b: Article) {
  return new Date(b.date).getTime() - new Date(a.date).getTime();
}

const fmtDate = (iso: string) =>
  new Date(iso).toLocaleDateString('de-DE', { day: '2-digit', month: 'long', year: 'numeric' });

export async function generateMetadata(): Promise<Metadata> {
  const articles = await getArticles();
  return pageMetadata({
    title: 'Artikel — KI verstehen, eingeordnet und erklärt',
    description:
      `${articles.length} redaktionelle Hintergrundartikel zu Künstlicher Intelligenz: Grundlagen, `
      + 'Sprachmodelle, Datenschutz und die Entwicklungen, die den Markt bewegen.',
    path: '/artikel',
    image: cover(articles.slice().sort(byDateDesc)[0] ?? ({} as Article)),
    keywords: ['KI Artikel', 'Künstliche Intelligenz erklärt', 'KI Grundlagen', 'KI Hintergrund'],
  });
}

export default async function ArticleIndexPage() {
  const articles = (await getArticles()).slice().sort(byDateDesc);
  const [lead, ...rest] = articles;
  const categories = [...new Set(articles.map((a) => a.category).filter(Boolean))];

  return (
    <div>
      <JsonLd data={[
        itemListLd(articles.map((a) => ({ name: a.title, path: `/artikel/${a.slug}` })), 'Artikel im KI-Toolnavigator'),
        breadcrumbLd([{ name: 'Start', path: '/' }, { name: 'Artikel', path: '/artikel' }]),
      ]} />

      <Breadcrumb items={[{ label: 'Start', href: '/' }, { label: 'Artikel' }]} />

      <div style={{ borderBottom: '1px solid var(--line)', paddingBottom: 40, marginBottom: 44 }}>
        <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#8a8580', letterSpacing: '0.08em', textTransform: 'uppercase', marginBottom: 14 }}>
          Aus der Redaktion
        </div>
        <h1 className="h-editorial-md" style={{ fontFamily: 'Fraunces, serif', fontWeight: 400, margin: 0, textWrap: 'balance' as const }}>
          Artikel
        </h1>
        <p style={{ fontFamily: 'Fraunces, serif', fontSize: 'clamp(17px, 2.4vw, 20px)', lineHeight: 1.5, color: 'var(--ink)', marginTop: 20, maxWidth: 720 }}>
          Hintergrund statt Hype: Einordnungen zu Grundlagen, Sprachmodellen, Datenschutz und den
          Entwicklungen, die den KI-Markt gerade wirklich verändern.
        </p>
        <div style={{ marginTop: 20, display: 'flex', gap: 8, flexWrap: 'wrap', alignItems: 'center' }}>
          <span style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#8a8580', letterSpacing: '0.04em', textTransform: 'uppercase' }}>
            {articles.length} Artikel ·
          </span>
          {categories.map((c) => <Chip key={c}>{c}</Chip>)}
        </div>
      </div>

      {lead && (
        <>
          <SectionLabel num="01">Zuletzt erschienen</SectionLabel>
          <Link href={`/artikel/${lead.slug}`} className="layout-editorial-lead" style={{ marginBottom: 56, display: 'grid' }}>
            {cover(lead) ? (
              <CoverImage
                src={cover(lead)!}
                alt={lead.title}
                aspect="4 / 3"
                sizes="(max-width: 900px) 94vw, (max-width: 1303px) 46vw, 574px"
                priority
                bordered
              />
            ) : (
              <Thumb name={lead.title} slug={lead.slug} aspect="4/3" label="Titelbild · Illustration" />
            )}
            <div>
              <Chip>{lead.category}</Chip>
              <h2 style={{ fontFamily: 'Fraunces, serif', fontSize: 34, fontWeight: 400, margin: '14px 0', letterSpacing: '-0.02em', lineHeight: 1.08, textWrap: 'balance' as const }}>
                {lead.title}
              </h2>
              <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#8a8580', letterSpacing: '0.04em', textTransform: 'uppercase' }}>
                {fmtDate(lead.date)} · {lead.readTime} Min. Lesezeit
              </div>
            </div>
          </Link>
        </>
      )}

      {rest.length > 0 && (
        <>
          <SectionLabel num="02">Alle Artikel</SectionLabel>
          <div className="grid-3" style={{ marginBottom: 72 }}>
            {rest.map((a) => (
              <Link key={a.slug} href={`/artikel/${a.slug}`} style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
                {cover(a) ? (
                  <CoverImage
                    src={cover(a)!}
                    alt={a.title}
                    aspect="4 / 3"
                    sizes="(max-width: 540px) 92vw, (max-width: 900px) 47vw, (max-width: 1303px) 31vw, 376px"
                    bordered
                  />
                ) : (
                  <Thumb name={a.title} slug={a.slug} aspect="4/3" />
                )}
                <Chip>{a.category}</Chip>
                <h3 style={{ fontFamily: 'Fraunces, serif', fontSize: 20, fontWeight: 500, margin: 0, letterSpacing: '-0.01em', lineHeight: 1.22, textWrap: 'balance' as const }}>
                  {a.title}
                </h3>
                <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 10, color: '#8a8580', letterSpacing: '0.04em', textTransform: 'uppercase' }}>
                  {fmtDate(a.date)} · {a.readTime} Min. Lesezeit
                </div>
              </Link>
            ))}
          </div>
        </>
      )}
    </div>
  );
}
