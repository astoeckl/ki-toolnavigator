import Link from 'next/link';
import { getAll } from '@/lib/cms';
import { getEditorialDates } from '@/lib/site';
import { Chip, SectionLabel, Thumb } from '@/components/ui';
import { HeroSearch } from './_home/HeroSearch';
import type { Article, Tool } from '@/lib/types';

/** Extract the resolved cover URL from any entity that carries a `media_id`
 *  reference (the public CMS endpoint resolves it to a URL string). */
function coverUrl(e: { media_id?: Article['media_id'] | Tool['media_id'] }): string | null {
  if (typeof e.media_id === 'string') return e.media_id;
  if (e.media_id && typeof e.media_id === 'object') return e.media_id.url ?? null;
  return null;
}
const articleCover = coverUrl;
const toolCover = coverUrl;

export default async function HomePage() {
  const { tools, categories, articles } = await getAll();
  const editorial = await getEditorialDates();
  const featured = tools.slice(0, 3);

  // Last updates derived from each entity's CMS `_updated_at` timestamp —
  // dynamically reflects any edit in the Cognitor backend (after ISR window).
  const fmt = (iso: string) => {
    const d = new Date(iso);
    const days = Math.floor((Date.now() - d.getTime()) / 86_400_000);
    if (days < 1) return 'heute';
    if (days < 2) return 'gestern';
    if (days < 7) return `vor ${days} Tagen`;
    return d.toLocaleDateString('de-DE', { day: '2-digit', month: 'short', year: 'numeric' });
  };
  const recentUpdates = [
    ...tools.map((t) => ({
      when: t._updated_at ?? t.lastUpdated,
      label: `${t.name} (${t.vendor}) — Eintrag aktualisiert`,
    })),
    ...articles.map((a) => ({
      when: a._updated_at ?? a.date,
      label: `${a.title} — Artikel`,
    })),
  ]
    .filter((e) => e.when)
    .sort((a, b) => new Date(b.when).getTime() - new Date(a.when).getTime())
    .slice(0, 7)
    .map((e) => `${fmt(e.when)} · ${e.label}`);

  return (
    <div>
      {/* Hero */}
      <section style={{ padding: 'clamp(40px, 6vw, 72px) 0 clamp(32px, 5vw, 56px)', borderBottom: '1px solid var(--line)' }}>
        <div className="layout-hero">
          <div>
            <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, letterSpacing: '0.08em', color: '#8a8580', textTransform: 'uppercase', marginBottom: 20 }}>
              Ausgabe Nr. 47 · {editorial.label}
            </div>
            <h1 className="h-editorial-xl" style={{
              fontFamily: 'Fraunces, Georgia, serif',
              fontWeight: 400,
              margin: 0, color: 'var(--ink-strong)', textWrap: 'balance' as const,
            }}>
              Das kuratierte<br />
              <span style={{ fontStyle: 'italic' }}>Verzeichnis</span> für<br />
              Künstliche Intelligenz.
            </h1>
            <p style={{ fontFamily: 'Fraunces, Georgia, serif', fontSize: 20, lineHeight: 1.5, color: 'var(--ink)', marginTop: 32, maxWidth: 620 }}>
              Über <b>{tools.length}</b> KI-Tools, geprüft, verglichen und erklärt — auf Deutsch,
              nach DSGVO-Kriterien sortierbar.
            </p>
            <HeroSearch />
          </div>

          <aside className="aside-divider">
            <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, letterSpacing: '0.08em', color: '#8a8580', textTransform: 'uppercase', marginBottom: 14 }}>In Zahlen</div>
            {[
              ['Tools gelistet', String(tools.length)],
              ['Kategorien', String(categories.length)],
              ['Artikel', String(articles.length)],
              ['DSGVO-konform', `${tools.filter((t) => t.dsgvo === 'ja').length} Tools`],
              ['DSGVO bedingt', `${tools.filter((t) => t.dsgvo === 'bedingt').length} Tools`],
              ['EU-Anbieter', `${tools.filter((t) => t.origin.startsWith('EU')).length} Tools`],
              ['Mit öffentlicher API', `${tools.filter((t) => t.api).length} Tools`],
            ].map(([k, v]) => (
              <div key={k} style={{ display: 'flex', justifyContent: 'space-between', padding: '8px 0', borderBottom: '1px dotted var(--line)', fontSize: 13 }}>
                <span style={{ color: 'var(--ink)' }}>{k}</span>
                <span style={{ fontFamily: 'Fraunces, serif', color: 'var(--ink-strong)', fontSize: 16 }}>{v}</span>
              </div>
            ))}
          </aside>
        </div>
      </section>

      {/* Kategorien */}
      <section style={{ padding: 'clamp(32px, 5vw, 56px) 0', borderBottom: '1px solid var(--line)' }}>
        <SectionLabel num="01">Kategorien</SectionLabel>
        <div className="grid-cats">
          {categories.map((c) => {
            const count = tools.filter((t) => t.category === c.slug).length;
            return (
              <Link key={c.slug} href={`/kategorie/${c.slug}`} style={{
                padding: '24px 24px 22px', background: 'var(--bg)',
                display: 'flex', flexDirection: 'column', gap: 10,
              }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'baseline' }}>
                  <h3 style={{ fontFamily: 'Fraunces, serif', fontSize: 20, fontWeight: 500, margin: 0, letterSpacing: '-0.01em' }}>{c.name}</h3>
                  <span style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: 'var(--accent)' }}>{count}</span>
                </div>
                <p style={{ margin: 0, fontSize: 13, color: 'var(--ink)', lineHeight: 1.5 }}>{c.desc}</p>
              </Link>
            );
          })}
        </div>
      </section>

      {/* Featured + Recent Changes */}
      <section className="layout-featured" style={{ padding: 'clamp(32px, 5vw, 56px) 0', borderBottom: '1px solid var(--line)' }}>
        <div>
          <SectionLabel num="02">Redaktionsempfehlung</SectionLabel>
          <div className="grid-3">
            {featured.map((t) => {
              const cover = toolCover(t);
              return (
                <Link key={t.slug} href={`/tool/${t.slug}`} style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
                  {cover ? (
                    <img
                      src={cover}
                      alt={t.name}
                      style={{ display: 'block', width: '100%', height: 'auto', aspectRatio: '3 / 2', objectFit: 'cover', border: '1px solid var(--line)' }}
                    />
                  ) : (
                    <Thumb name={t.name} slug={t.slug} aspect="3/2" />
                  )}
                  <div style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
                    <Chip>{categories.find((c) => c.slug === t.category)?.name}</Chip>
                  </div>
                  <h4 style={{ fontFamily: 'Fraunces, serif', fontSize: 22, fontWeight: 500, margin: 0, letterSpacing: '-0.01em' }}>{t.name}</h4>
                  <p style={{ margin: 0, fontSize: 13, lineHeight: 1.5, color: 'var(--ink)' }}>{t.tagline}</p>
                </Link>
              );
            })}
          </div>
        </div>

        <aside style={{ borderLeft: '1px solid var(--line)', paddingLeft: 32 }}>
          <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, letterSpacing: '0.08em', color: '#8a8580', textTransform: 'uppercase', marginBottom: 18 }}>Letzte Änderungen</div>
          <ul style={{ listStyle: 'none', padding: 0, margin: 0 }}>
            {recentUpdates.map((line, i) => (
              <li key={i} style={{ padding: '10px 0', borderBottom: '1px dotted var(--line)', fontSize: 13, lineHeight: 1.5, color: 'var(--ink)' }}>
                {line}
              </li>
            ))}
          </ul>
          <Link href="/aenderungen" style={{
            display: 'inline-block', marginTop: 16,
            fontFamily: 'JetBrains Mono, monospace', fontSize: 11,
            color: 'var(--accent)', letterSpacing: '0.06em',
            textTransform: 'uppercase', borderBottom: '1px solid var(--accent)',
          }}>Alle Änderungen →</Link>
        </aside>
      </section>

      {/* Aus der Redaktion */}
      <section style={{ padding: 'clamp(32px, 5vw, 56px) 0 clamp(56px, 8vw, 88px)' }}>
        <SectionLabel num="03">Aus der Redaktion</SectionLabel>
        <div className="layout-editorial">
          <Link href={`/artikel/${articles[0].slug}`} className="layout-editorial-lead">
            {articleCover(articles[0]) ? (
              <img
                src={articleCover(articles[0])!}
                alt={articles[0].title}
                style={{ display: 'block', width: '100%', height: 'auto', aspectRatio: '4 / 3', objectFit: 'cover', border: '1px solid var(--line)' }}
              />
            ) : (
              <Thumb name={articles[0].title} slug={articles[0].slug} aspect="4/3" label="Titelbild · Illustration" />
            )}
            <div>
              <Chip>{articles[0].category}</Chip>
              <h3 style={{ fontFamily: 'Fraunces, serif', fontSize: 34, fontWeight: 400, margin: '14px 0 14px', letterSpacing: '-0.02em', lineHeight: 1.08, textWrap: 'balance' as const }}>{articles[0].title}</h3>
              <p style={{ fontSize: 14, lineHeight: 1.6, color: 'var(--ink)', margin: 0 }}>
                Eine kompakte Einführung in die Grundlagen, Teilgebiete und heutigen Anwendungsfelder
                der Künstlichen Intelligenz — mit besonderem Blick auf den europäischen Kontext.
              </p>
              <div style={{ marginTop: 16, fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#8a8580', letterSpacing: '0.04em', textTransform: 'uppercase' }}>
                {articles[0].readTime} Min. Lesezeit
              </div>
            </div>
          </Link>
          <ul style={{ listStyle: 'none', padding: 0, margin: 0 }}>
            {articles.slice(1, 5).map((a) => {
              const cover = articleCover(a);
              return (
                <li key={a.slug} style={{ padding: '18px 0', borderBottom: '1px solid var(--line)' }}>
                  <Link href={`/artikel/${a.slug}`} className="grid-cover-row">
                    {cover ? (
                      <img
                        src={cover}
                        alt={a.title}
                        style={{ display: 'block', width: '100%', aspectRatio: '4 / 3', objectFit: 'cover', border: '1px solid var(--line)' }}
                      />
                    ) : (
                      <div style={{ width: '100%', aspectRatio: '4 / 3', border: '1px solid var(--line)', background: 'var(--bg-alt)' }} />
                    )}
                    <div>
                      <Chip>{a.category}</Chip>
                      <h4 style={{ fontFamily: 'Fraunces, serif', fontSize: 17, fontWeight: 500, margin: '6px 0 4px', letterSpacing: '-0.01em', lineHeight: 1.2, textWrap: 'balance' as const }}>{a.title}</h4>
                      <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 10, color: '#8a8580', letterSpacing: '0.04em', textTransform: 'uppercase' }}>{a.readTime} Min. Lesezeit</div>
                    </div>
                  </Link>
                </li>
              );
            })}
          </ul>
        </div>
      </section>
    </div>
  );
}
