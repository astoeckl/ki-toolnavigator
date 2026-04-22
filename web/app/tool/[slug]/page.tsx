import Link from 'next/link';
import { notFound } from 'next/navigation';
import { getCategories, getPost, getTool, getTools } from '@/lib/cms';
import { renderMarkdown } from '@/lib/markdown';
import { Badge, Breadcrumb, DataRow, SectionLabel, Thumb } from '@/components/ui';
import { ScrollSpyTOC } from '@/components/ScrollSpyTOC';
import { ToolActions } from './ToolActions';
import { ToolTabs } from './ToolTabs';

export async function generateStaticParams() {
  const tools = await getTools();
  return tools.map((t) => ({ slug: t.slug }));
}

export default async function ToolPage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const t = await getTool(slug);
  if (!t) notFound();
  const categories = await getCategories();
  const cat = categories.find((c) => c.slug === t.category);
  const tools = await getTools();
  const related = tools.filter((x) => x.category === t.category && x.slug !== t.slug).slice(0, 3);

  // The public elements endpoint inlines the full Post under `post_id`; if it ever
  // returns just an integer, fetch via getPost (server-side, auth).
  let overviewPost: Awaited<ReturnType<typeof getPost>> = null;
  if (t.post_id && typeof t.post_id === 'object') {
    overviewPost = t.post_id;
  } else if (typeof t.post_id === 'number') {
    overviewPost = await getPost(t.post_id);
  }
  const overviewHtml = overviewPost?.content ? renderMarkdown(overviewPost.content) : null;
  const featuresHtml = t.features ? renderMarkdown(t.features) : null;
  const pricingHtml  = t.pricing  ? renderMarkdown(t.pricing)  : null;

  return (
    <div>
      <Breadcrumb items={[
        { label: 'Start', href: '/' },
        { label: 'Verzeichnis', href: '/verzeichnis' },
        { label: cat?.name ?? '', href: `/kategorie/${cat?.slug}` },
        { label: t.name },
      ]} />

      <div className="layout-3col">
        <aside className="sidebar-sticky only-desktop" style={{ position: 'sticky', top: 80, alignSelf: 'start' }}>
          <ScrollSpyTOC items={[
            { label: 'Zusammenfassung',  hash: '#zusammenfassung' },
            { label: 'Screenshot',       hash: '#screenshot' },
            { label: 'Pro & Contra',     hash: '#pro-contra' },
            { label: 'Anwendungsfälle',  hash: '#anwendungsfaelle' },
            { label: 'Verwandte Tools',  hash: '#verwandte-tools' },
          ]} />

        </aside>

        <main>
          <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#8a8580', letterSpacing: '0.08em', textTransform: 'uppercase', marginBottom: 10 }}>
            {cat?.name} · {t.vendor}
          </div>
          <h1 className="h-editorial-lg" style={{ fontFamily: 'Fraunces, serif', fontWeight: 400, margin: 0 }}>{t.name}</h1>
          <p style={{ fontFamily: 'Fraunces, serif', fontSize: 'clamp(18px, 2.4vw, 22px)', lineHeight: 1.4, color: 'var(--ink)', marginTop: 18, maxWidth: 620, fontStyle: 'italic' }}>{t.tagline}</p>

          <div style={{ marginTop: 28, display: 'flex', gap: 20, alignItems: 'center', flexWrap: 'wrap' }}>
            <Badge kind={t.dsgvo} />
            <span style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#8a8580' }}>· {t.origin}</span>
          </div>

          <ToolActions slug={t.slug} website={t.website} />

          <ToolTabs
            t={t}
            catName={cat?.name ?? ''}
            related={related}
            overviewHtml={overviewHtml}
            featuresHtml={featuresHtml}
            pricingHtml={pricingHtml}
          />
        </main>

        <aside>
          <div style={{ border: '1px solid var(--ink-strong)', padding: 0 }}>
            <div style={{ padding: '14px 18px', borderBottom: '1px solid var(--ink-strong)', background: 'var(--ink-strong)', color: 'var(--bg)' }}>
              <div style={{ fontFamily: 'Fraunces, serif', fontSize: 18, fontWeight: 500 }}>{t.name}</div>
              <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 10, letterSpacing: '0.06em', color: 'rgba(255,255,255,0.7)', textTransform: 'uppercase', marginTop: 2 }}>Tool-Steckbrief</div>
            </div>
            <div style={{ padding: 18 }}>
              {(() => {
                const logo =
                  typeof t.logo_id === 'string' ? t.logo_id :
                  (t.logo_id && typeof t.logo_id === 'object') ? (t.logo_id.url ?? null) :
                  null;
                if (!logo) {
                  return <Thumb name={t.name} slug={t.slug + '-info'} aspect="4/3" label="Produkt · Logo" />;
                }
                return (
                  <div style={{
                    aspectRatio: '4 / 3',
                    display: 'flex', alignItems: 'center', justifyContent: 'center',
                    background: 'var(--bg-alt)', border: '1px solid var(--line)',
                    padding: 24,
                  }}>
                    <img
                      src={logo}
                      alt={`${t.name} Logo`}
                      style={{ maxWidth: '70%', maxHeight: '70%', width: 'auto', height: 'auto', objectFit: 'contain' }}
                    />
                  </div>
                );
              })()}
              <div style={{ marginTop: 14 }}>
                <DataRow label="Anbieter" value={t.vendor} />
                <DataRow label="Kategorie" value={cat?.name} />
                <DataRow label="Herkunft" value={t.origin} mono />
                <DataRow label="Preis" value={t.price} />
                <DataRow label="API" value={t.api ? 'Ja' : 'Nein'} mono />
                <DataRow label="DSGVO" value={t.dsgvo === 'ja' ? 'Konform' : t.dsgvo === 'bedingt' ? 'Bedingt' : 'Kein Nachweis'} />
                <DataRow label="Launch" value={new Date(t.launched).toLocaleDateString('de-DE')} mono />
                <DataRow label="Aktualisiert" value={new Date(t._updated_at ?? t.lastUpdated).toLocaleDateString('de-DE')} mono />
              </div>
            </div>
          </div>

          <div style={{ marginTop: 20, fontFamily: 'JetBrains Mono, monospace', fontSize: 10, color: '#8a8580', letterSpacing: '0.04em', textTransform: 'uppercase', lineHeight: 1.6 }}>
            Artikel zuletzt bearbeitet<br />
            am {new Date(t._updated_at ?? t.lastUpdated).toLocaleDateString('de-DE')} durch Redaktion<br />
            <a style={{ color: 'var(--accent)', borderBottom: '1px dotted var(--accent)' }}>Verlauf ansehen</a>
          </div>
        </aside>
      </div>
    </div>
  );
}
