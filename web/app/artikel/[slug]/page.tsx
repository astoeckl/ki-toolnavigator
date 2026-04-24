import Link from 'next/link';
import { notFound } from 'next/navigation';
import { getArticle, getArticles, getMedia, getPost, mediaUrl } from '@/lib/cms';
import { renderMarkdown, toSlug } from '@/lib/markdown';
import { Breadcrumb, Chip, Thumb } from '@/components/ui';
import { Prose } from '@/components/Prose';
import { ScrollSpyTOC } from '@/components/ScrollSpyTOC';

export async function generateStaticParams() {
  const articles = await getArticles();
  return articles.map((a) => ({ slug: a.slug }));
}

export default async function ArticlePage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const a = await getArticle(slug);
  if (!a) notFound();
  const articles = await getArticles();

  // The public elements endpoint resolves `post_id` (a reference field) into the
  // full Post object inline. If the API ever returns just an integer (e.g. auth
  // endpoint, or unresolved), fall back to fetching it via getPost().
  let post: Awaited<ReturnType<typeof getPost>> = null;
  if (a.post_id && typeof a.post_id === 'object') {
    post = a.post_id; // already resolved
  } else if (typeof a.post_id === 'number') {
    post = await getPost(a.post_id);
  }
  const lead = post?.short_description ?? null;

  // Resolve cover image — Cognitor's public elements endpoint resolves a
  // `format: media_id` reference to the asset URL string directly.
  // Auth API may return the integer id or an inlined Media object instead.
  let coverUrl: string | null = null;
  const coverAlt = a.title;
  if (typeof a.media_id === 'string' && a.media_id) {
    coverUrl = a.media_id;
  } else if (a.media_id && typeof a.media_id === 'object') {
    coverUrl = a.media_id.url ?? (a.media_id.id ? mediaUrl(a.media_id.id) : null);
  } else if (typeof a.media_id === 'number') {
    const media = await getMedia(a.media_id);
    coverUrl = media?.url ?? mediaUrl(a.media_id);
  }

  return (
    <div>
      <Breadcrumb items={[
        { label: 'Start', href: '/' },
        { label: 'Artikel' },
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
              <img
                src={coverUrl}
                alt={coverAlt}
                style={{ display: 'block', width: '100%', height: 'auto', aspectRatio: '16 / 9', objectFit: 'cover' }}
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
        </aside>
      </div>
    </div>
  );
}
