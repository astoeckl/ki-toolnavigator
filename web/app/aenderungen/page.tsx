import Link from 'next/link';
import { getArticles, getCategories, getTools } from '@/lib/cms';
import { Breadcrumb, Chip } from '@/components/ui';

export const metadata = { title: 'Letzte Änderungen · KI-Toolnavigator' };

type Change = {
  when: string;        // ISO timestamp
  type: 'Tool' | 'Artikel' | 'Kategorie';
  title: string;
  detail: string;
  href: string;
};

const fmtAbsolute = (iso: string) =>
  new Date(iso).toLocaleString('de-DE', {
    day: '2-digit', month: '2-digit', year: 'numeric',
    hour: '2-digit', minute: '2-digit',
  }) + ' Uhr';

const fmtRelative = (iso: string) => {
  const ms = Date.now() - new Date(iso).getTime();
  const min = Math.floor(ms / 60_000);
  if (min < 1) return 'gerade eben';
  if (min < 60) return `vor ${min} Min.`;
  const h = Math.floor(min / 60);
  if (h < 24) return `vor ${h} Std.`;
  const d = Math.floor(h / 24);
  if (d === 1) return 'gestern';
  if (d < 7) return `vor ${d} Tagen`;
  if (d < 30) return `vor ${Math.floor(d / 7)} Wochen`;
  return `vor ${Math.floor(d / 30)} Monaten`;
};

const groupKey = (iso: string) => {
  const ms = Date.now() - new Date(iso).getTime();
  const d = Math.floor(ms / 86_400_000);
  if (d < 1) return 'Heute';
  if (d < 2) return 'Gestern';
  if (d < 7) return 'Diese Woche';
  if (d < 30) return 'Diesen Monat';
  return 'Älter';
};

export default async function ChangesPage() {
  const [tools, articles, categories] = await Promise.all([
    getTools(),
    getArticles(),
    getCategories(),
  ]);

  const all: Change[] = [
    ...tools.map<Change>((t) => ({
      when: t._updated_at ?? t.lastUpdated,
      type: 'Tool',
      title: t.name,
      detail: `${t.vendor} · ${categories.find((c) => c.slug === t.category)?.name ?? t.category}`,
      href: `/tool/${t.slug}`,
    })),
    ...articles.map<Change>((a) => ({
      when: a._updated_at ?? a.date,
      type: 'Artikel',
      title: a.title,
      detail: a.category,
      href: `/artikel/${a.slug}`,
    })),
    ...categories.map<Change>((c) => ({
      when: c._updated_at ?? '1970-01-01',
      type: 'Kategorie',
      title: c.name,
      detail: c.desc.slice(0, 80) + (c.desc.length > 80 ? '…' : ''),
      href: `/kategorie/${c.slug}`,
    })),
  ]
    .filter((c) => c.when)
    .sort((a, b) => new Date(b.when).getTime() - new Date(a.when).getTime());

  // Group by relative bucket
  const groups = new Map<string, Change[]>();
  for (const c of all) {
    const key = groupKey(c.when);
    if (!groups.has(key)) groups.set(key, []);
    groups.get(key)!.push(c);
  }

  return (
    <div>
      <Breadcrumb items={[{ label: 'Start', href: '/' }, { label: 'Letzte Änderungen' }]} />

      <div style={{ borderBottom: '1px solid var(--line)', paddingBottom: 32, marginBottom: 40 }}>
        <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#8a8580', letterSpacing: '0.08em', textTransform: 'uppercase', marginBottom: 12 }}>
          Activity-Feed · Cognitor CMS
        </div>
        <h1 style={{ fontFamily: 'Fraunces, serif', fontWeight: 400, fontSize: 'clamp(40px, 5vw, 64px)', letterSpacing: '-0.025em', margin: 0, lineHeight: 1, textWrap: 'balance' as const }}>
          Letzte Änderungen
        </h1>
        <p style={{ fontFamily: 'Fraunces, serif', fontSize: 18, lineHeight: 1.5, color: 'var(--ink)', marginTop: 16, maxWidth: 720 }}>
          Chronologische Übersicht aller Änderungen — Tools, Artikel und Kategorien,
          sortiert nach dem CMS-Bearbeitungszeitstempel. Aktualisiert sich automatisch nach
          jeder Änderung im Backend.
        </p>
        <div style={{ marginTop: 16, fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#8a8580', letterSpacing: '0.04em', textTransform: 'uppercase' }}>
          {all.length} Einträge · {tools.length} Tools · {articles.length} Artikel · {categories.length} Kategorien
        </div>
      </div>

      <div className="layout-aenderungen">
        {/* Group nav */}
        <aside className="sidebar-sticky only-desktop" style={{ position: 'sticky', top: 80, alignSelf: 'start' }}>
          <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#8a8580', letterSpacing: '0.08em', textTransform: 'uppercase', marginBottom: 14 }}>
            Zeitraum
          </div>
          <ul style={{ listStyle: 'none', padding: 0, margin: 0, borderLeft: '1px solid var(--line)' }}>
            {Array.from(groups.entries()).map(([key, items], i) => (
              <li key={key} style={{ padding: '6px 14px', fontSize: 13, borderLeft: i === 0 ? '2px solid var(--accent)' : 'none', marginLeft: -1, color: i === 0 ? 'var(--accent)' : 'var(--ink)' }}>
                <a href={`#${key.toLowerCase().replace(/\s/g, '-')}`} style={{ color: 'inherit' }}>
                  {key}{' '}
                  <span style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 10, color: '#8a8580' }}>
                    ({items.length})
                  </span>
                </a>
              </li>
            ))}
          </ul>
        </aside>

        {/* Activity feed */}
        <div>
          {Array.from(groups.entries()).map(([key, items]) => (
            <section key={key} id={key.toLowerCase().replace(/\s/g, '-')} style={{ marginBottom: 48 }}>
              <h2 style={{
                fontFamily: 'Fraunces, serif', fontSize: 22, fontWeight: 500,
                letterSpacing: '-0.01em', margin: 0,
                paddingBottom: 10, marginBottom: 22,
                borderBottom: '1px solid var(--line)',
                display: 'flex', alignItems: 'baseline', gap: 14,
              }}>
                <span style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#8a8580', letterSpacing: '0.08em', textTransform: 'uppercase' }}>
                  §
                </span>
                {key}
              </h2>
              <ul style={{ listStyle: 'none', padding: 0, margin: 0 }}>
                {items.map((c, i) => (
                  <li key={`${c.type}-${c.title}-${i}`} className="compare-row">
                    <div style={{
                      fontFamily: 'JetBrains Mono, monospace', fontSize: 11,
                      letterSpacing: '0.04em', color: '#8a8580', textTransform: 'uppercase',
                    }}>
                      <div>{fmtRelative(c.when)}</div>
                      <div style={{ fontSize: 10, marginTop: 2 }}>{fmtAbsolute(c.when)}</div>
                    </div>
                    <div>
                      <div style={{ display: 'flex', gap: 10, alignItems: 'baseline', marginBottom: 4 }}>
                        <Chip>{c.type}</Chip>
                        <Link href={c.href} style={{
                          fontFamily: 'Fraunces, serif', fontSize: 18, fontWeight: 500,
                          letterSpacing: '-0.01em', color: 'var(--ink-strong)',
                          borderBottom: '1px dotted var(--accent)',
                        }}>
                          {c.title}
                        </Link>
                      </div>
                      <div style={{ fontSize: 13, color: 'var(--ink)' }}>{c.detail}</div>
                    </div>
                  </li>
                ))}
              </ul>
            </section>
          ))}
        </div>
      </div>
    </div>
  );
}
