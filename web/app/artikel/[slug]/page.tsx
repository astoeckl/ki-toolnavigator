import type { Metadata } from 'next';
import Link from 'next/link';
import { notFound } from 'next/navigation';
import { getArticle, getArticles, getMedia, getPost, mediaUrl } from '@/lib/cms';
import { renderMarkdown, toSlug } from '@/lib/markdown';
import { Breadcrumb, Chip, Thumb } from '@/components/ui';
import { Prose } from '@/components/Prose';
import { CoverImage } from '@/components/CoverImage';
import { ScrollSpyTOC } from '@/components/ScrollSpyTOC';
import { JsonLd } from '@/components/JsonLd';
import { articleLd, breadcrumbLd, keywordList, pageMetadata, summarize } from '@/lib/seo';
import type { Article, Post } from '@/lib/types';

export async function generateStaticParams() {
  const articles = await getArticles();
  return articles.map((a) => ({ slug: a.slug }));
}

/** Resolve `post_id` — the public endpoint inlines the Post, the auth API returns an id. */
async function resolvePost(a: Article): Promise<Post | null> {
  if (a.post_id && typeof a.post_id === 'object') return a.post_id;
  if (typeof a.post_id === 'number') return getPost(a.post_id);
  return null;
}

/** Resolve `media_id` to a usable cover URL across all three shapes the CMS may return. */
async function resolveCover(a: Article): Promise<string | null> {
  if (typeof a.media_id === 'string' && a.media_id) return a.media_id;
  if (a.media_id && typeof a.media_id === 'object') {
    return a.media_id.url ?? (a.media_id.id ? mediaUrl(a.media_id.id) : null);
  }
  if (typeof a.media_id === 'number') {
    const media = await getMedia(a.media_id);
    return media?.url ?? mediaUrl(a.media_id);
  }
  return null;
}

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }): Promise<Metadata> {
  const { slug } = await params;
  const a = await getArticle(slug);
  if (!a) return { title: 'Artikel nicht gefunden', robots: { index: false, follow: false } };

  const post = await resolvePost(a);
  const cover = await resolveCover(a);
  // Some articles carry no lead text yet — fall back to a constructed sentence so
  // the page never ships without a meta description.
  const description =
    summarize(post?.short_description ?? post?.content)
    || summarize(`${a.title} — Hintergrundartikel im KI-Toolnavigator${a.category ? ` zum Thema ${a.category}` : ''}. `
        + `${a.readTime} Minuten Lesezeit, redaktionell recherchiert.`);

  return pageMetadata({
    title: a.title,
    description,
    path: `/artikel/${a.slug}`,
    image: cover,
    imageAlt: a.title,
    type: 'article',
    keywords: keywordList(post?.keywords),
    publishedTime: a.date ? new Date(a.date).toISOString() : undefined,
    modifiedTime: new Date(a._updated_at ?? a.date).toISOString(),
    authors: [a.author].filter(Boolean),
  });
}

export default async function ArticlePage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const a = await getArticle(slug);
  if (!a) notFound();
  const articles = await getArticles();
  const post = await resolvePost(a);
  const lead = post?.short_description ?? null;
  const coverUrl = await resolveCover(a);
  const coverAlt = a.title;

  return (
    <div>
      <JsonLd data={[
        articleLd(a, {
          description: summarize(post?.short_description ?? post?.content, 300) || a.title,
          image: coverUrl,
          post,
          wordCount: post?.content ? post.content.trim().split(/\s+/).length : undefined,
        }),
        breadcrumbLd([
          { name: 'Start', path: '/' },
          { name: 'Artikel', path: '/artikel' },
          { name: a.title, path: `/artikel/${a.slug}` },
        ]),
      ]} />

      <Breadcrumb items={[
        { label: 'Start', href: '/' },
        { label: 'Artikel', href: '/artikel' },
        { label: a.title },
      ]} />

      <div className="layout-3col-article">
        <aside className="sidebar-sticky only-desktop" style={{ position: 'sticky', top: 80, alignSelf: 'start' }}>
          <ScrollSpyTOC
            eyebrow="Inhaltsverzeichnis"
            items={a.toc.map((s, i) => ({
              label: s,
              hash: `#${toSlug(s)}`,
              num: String(i + 1).padStart(2, '0'),
            }))}
          />
        </aside>

        <article style={{ maxWidth: 680 }}>
          <Chip>{a.category}</Chip>
          <h1 className="h-editorial-md" style={{ fontFamily: 'Fraunces, serif', fontWeight: 400, margin: '18px 0 18px', textWrap: 'balance' as const }}>{a.title}</h1>
          <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#8a8580', letterSpacing: '0.04em', textTransform: 'uppercase' }}>
            {new Date(a.date).toLocaleDateString('de-DE', { day: '2-digit', month: 'long', year: 'numeric' })} · {a.readTime} Min. Lesezeit
          </div>

          <figure style={{ margin: '32px 0', border: '1px solid var(--line)', padding: 0 }}>
            {coverUrl ? (
              <CoverImage
                src={coverUrl}
                alt={coverAlt}
                aspect="16 / 9"
                sizes="(max-width: 900px) 94vw, (max-width: 1303px) calc(100vw - 640px), 600px"
                priority
              />
            ) : (
              <Thumb name={a.title} slug={a.slug} aspect="16/9" label="Illustration · Aufmacherbild" />
            )}
            <figcaption style={{
              padding: '8px 14px',
              borderTop: '1px solid var(--line)',
              fontFamily: 'JetBrains Mono, monospace', fontSize: 10,
              letterSpacing: '0.06em', textTransform: 'uppercase',
              color: '#8a8580',
              display: 'flex', justifyContent: 'space-between',
            }}>
              <span>Aufmacher · Illustration</span>
              <span>{coverUrl ? 'Cognitor Media (Nano Banana)' : 'Platzhalter — Bild folgt'}</span>
            </figcaption>
          </figure>

          {lead && (
            <p style={{ fontFamily: 'Fraunces, serif', fontSize: 'clamp(18px, 2.6vw, 22px)', lineHeight: 1.5, color: 'var(--ink-strong)', fontStyle: 'italic', margin: '0 0 28px' }}>
              {lead}
            </p>
          )}

          {post?.content ? (
            <Prose html={renderMarkdown(post.content)} dropCap />
          ) : (
            <p style={{ fontFamily: 'Fraunces, serif', fontSize: 18, color: 'var(--ink)', fontStyle: 'italic' }}>
              Inhalt für diesen Artikel ist in Bearbeitung.
            </p>
          )}

          <div style={{ marginTop: 56, paddingTop: 20, borderTop: '1px solid var(--line)', display: 'flex', gap: 16, flexWrap: 'wrap', alignItems: 'center' }}>
            <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#8a8580', letterSpacing: '0.08em', textTransform: 'uppercase' }}>Verweise:</div>
            <Chip>Grundlagen</Chip>
            <Chip>Sprachmodelle</Chip>
            <Chip>DSGVO</Chip>
            <Chip>Geschichte</Chip>
          </div>
        </article>

        <aside>
          <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#8a8580', letterSpacing: '0.08em', textTransform: 'uppercase', marginBottom: 14 }}>Weitere Artikel</div>
          <ul style={{ listStyle: 'none', padding: 0, margin: 0 }}>
            {articles.filter((x) => x.slug !== a.slug).slice(0, 4).map((x) => (
              <li key={x.slug} style={{ padding: '14px 0', borderBottom: '1px dotted var(--line)' }}>
                <Link href={`/artikel/${x.slug}`}>
                  <h4 style={{ fontFamily: 'Fraunces, serif', fontSize: 16, fontWeight: 500, margin: 0, letterSpacing: '-0.01em', lineHeight: 1.25 }}>{x.title}</h4>
                  <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 10, color: '#8a8580', letterSpacing: '0.04em', textTransform: 'uppercase', marginTop: 4 }}>{x.readTime} Min. Lesezeit</div>
                </Link>
              </li>
            ))}
          </ul>
          <Link
            href="/artikel"
            style={{
              display: 'inline-block', marginTop: 18,
              fontFamily: 'JetBrains Mono, monospace', fontSize: 11,
              letterSpacing: '0.06em', textTransform: 'uppercase',
              color: 'var(--accent)', borderBottom: '1px dotted var(--accent)',
            }}
          >
            Alle Artikel ansehen →
          </Link>
        </aside>
      </div>
    </div>
  );
}
