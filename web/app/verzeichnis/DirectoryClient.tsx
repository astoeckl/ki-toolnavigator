'use client';
import Link from 'next/link';
import { useMemo, useState } from 'react';
import type { Category, Tool } from '@/lib/types';
import { Badge, Button, Thumb } from '@/components/ui';
import { useCompare } from '@/components/CompareContext';

/** Resolve tool cover URL from media_id (public endpoint returns a string). */
function toolCover(t: Tool): string | null {
  if (typeof t.media_id === 'string') return t.media_id;
  if (t.media_id && typeof t.media_id === 'object') return t.media_id.url ?? null;
  return null;
}

type Props = {
  tools: Tool[];
  categories: Category[];
  initialSearch: string;
  initialCategory: string;
};

export function DirectoryClient({ tools, categories, initialSearch, initialCategory }: Props) {
  const [view, setView] = useState<'list' | 'grid'>('list');
  const [catFilter, setCatFilter] = useState(initialCategory);
  const [search, setSearch] = useState(initialSearch);
  const [dsgvoOnly, setDsgvoOnly] = useState(false);
  const [euOnly, setEuOnly] = useState(false);
  const [sort, setSort] = useState<'name' | 'newest'>('newest');
  const { compareList, has, toggle, remove } = useCompare();

  const filtered = useMemo(() => {
    return tools
      .filter((t) => !search || (t.name + t.tagline + t.vendor).toLowerCase().includes(search.toLowerCase()))
      .filter((t) => catFilter === 'all' || t.category === catFilter)
      .filter((t) => !dsgvoOnly || t.dsgvo === 'ja')
      .filter((t) => !euOnly || t.origin.startsWith('EU'))
      .sort((a, b) => {
        if (sort === 'name') return a.name.localeCompare(b.name);
        if (sort === 'newest') return new Date(b.lastUpdated).getTime() - new Date(a.lastUpdated).getTime();
        return 0;
      });
  }, [tools, search, catFilter, dsgvoOnly, euOnly, sort]);

  return (
    <div className="layout-directory">
      <aside>
        <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, letterSpacing: '0.08em', color: '#8a8580', textTransform: 'uppercase', marginBottom: 14 }}>Kategorien</div>
        <ul style={{ listStyle: 'none', padding: 0, margin: 0 }}>
          <li style={{ padding: '6px 0' }}>
            <a onClick={() => setCatFilter('all')} style={{
              cursor: 'pointer', fontSize: 13,
              color: catFilter === 'all' ? 'var(--accent)' : 'var(--ink-strong)',
              fontWeight: catFilter === 'all' ? 600 : 400,
              borderBottom: catFilter === 'all' ? '1px solid var(--accent)' : 'none',
              paddingBottom: 1,
            }}>Alle Tools <span style={{ color: '#8a8580', fontFamily: 'JetBrains Mono, monospace', fontSize: 11 }}>({tools.length})</span></a>
          </li>
          {categories.map((c) => (
            <li key={c.slug} style={{ padding: '6px 0' }}>
              <a onClick={() => setCatFilter(c.slug)} style={{
                cursor: 'pointer', fontSize: 13,
                color: catFilter === c.slug ? 'var(--accent)' : 'var(--ink-strong)',
                fontWeight: catFilter === c.slug ? 600 : 400,
                borderBottom: catFilter === c.slug ? '1px solid var(--accent)' : 'none',
                paddingBottom: 1,
              }}>{c.name} <span style={{ color: '#8a8580', fontFamily: 'JetBrains Mono, monospace', fontSize: 11 }}>({tools.filter((t) => t.category === c.slug).length})</span></a>
            </li>
          ))}
        </ul>

        <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, letterSpacing: '0.08em', color: '#8a8580', textTransform: 'uppercase', marginTop: 36, marginBottom: 14 }}>Filter</div>
        <label style={{ display: 'flex', gap: 10, alignItems: 'center', fontSize: 13, padding: '6px 0', cursor: 'pointer' }}>
          <input type="checkbox" checked={dsgvoOnly} onChange={(e) => setDsgvoOnly(e.target.checked)} style={{ accentColor: 'var(--accent)' }} />
          Nur DSGVO-konform
        </label>
        <label style={{ display: 'flex', gap: 10, alignItems: 'center', fontSize: 13, padding: '6px 0', cursor: 'pointer' }}>
          <input type="checkbox" checked={euOnly} onChange={(e) => setEuOnly(e.target.checked)} style={{ accentColor: 'var(--accent)' }} />
          Nur EU-Anbieter
        </label>

        {compareList.length > 0 && (
          <div style={{ marginTop: 36, padding: 16, border: '1px solid var(--accent)', background: 'var(--bg)' }}>
            <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, letterSpacing: '0.08em', color: 'var(--accent)', textTransform: 'uppercase', marginBottom: 10 }}>Vergleichskorb ({compareList.length}/4)</div>
            {compareList.map((slug) => {
              const t = tools.find((x) => x.slug === slug);
              return t && (
                <div key={slug} style={{ display: 'flex', justifyContent: 'space-between', padding: '4px 0', fontSize: 13 }}>
                  <span>{t.name}</span>
                  <a onClick={() => remove(slug)} style={{ cursor: 'pointer', color: '#8a8580' }}>×</a>
                </div>
              );
            })}
            <div style={{ marginTop: 10 }}><Button variant="accent" href="/vergleich">Vergleichen →</Button></div>
          </div>
        )}
      </aside>

      <div>
        <div style={{ display: 'flex', alignItems: 'end', justifyContent: 'space-between', marginBottom: 32, flexWrap: 'wrap', gap: 16 }}>
          <div>
            <h1 className="h-editorial-sm" style={{ fontFamily: 'Fraunces, serif', fontWeight: 400, margin: 0 }}>
              {catFilter === 'all' ? 'Alle Tools' : categories.find((c) => c.slug === catFilter)?.name}
            </h1>
            <div style={{ marginTop: 10, fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#8a8580', letterSpacing: '0.04em', textTransform: 'uppercase' }}>
              {filtered.length} Einträge{search && ` · Suche: „${search}"`}
            </div>
          </div>
          <div style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
            <select value={sort} onChange={(e) => setSort(e.target.value as typeof sort)} style={{
              padding: '9px 12px', border: '1px solid var(--line)', background: 'var(--bg)',
              fontFamily: 'Inter Tight, sans-serif', fontSize: 13, cursor: 'pointer',
            }}>
              <option value="newest">Sortierung: Zuletzt aktualisiert</option>
              <option value="name">Sortierung: Name A–Z</option>
            </select>
            <div style={{ display: 'flex', border: '1px solid var(--line)' }}>
              {(['list', 'grid'] as const).map((v) => (
                <button key={v} onClick={() => setView(v)} style={{
                  padding: '8px 12px', border: 'none',
                  background: view === v ? 'var(--ink-strong)' : 'transparent',
                  color: view === v ? 'var(--bg)' : 'var(--ink)',
                  fontFamily: 'JetBrains Mono, monospace', fontSize: 11,
                  letterSpacing: '0.04em', textTransform: 'uppercase', cursor: 'pointer',
                }}>{v === 'list' ? 'Liste' : 'Raster'}</button>
              ))}
            </div>
          </div>
        </div>

        <div style={{ marginBottom: 16, display: 'flex', alignItems: 'center', border: '1px solid var(--line)', padding: 2 }}>
          <input
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            placeholder="In diesem Verzeichnis suchen …"
            style={{ flex: 1, padding: '10px 14px', border: 'none', outline: 'none', background: 'transparent', fontFamily: 'Inter Tight, sans-serif', fontSize: 13 }}
          />
          {search && <a onClick={() => setSearch('')} style={{ padding: '0 14px', cursor: 'pointer', color: '#8a8580', fontFamily: 'JetBrains Mono, monospace', fontSize: 11 }}>Zurücksetzen ×</a>}
        </div>

        {view === 'list' ? (
          <ul style={{ listStyle: 'none', padding: 0, margin: 0, border: '1px solid var(--line)', borderBottom: 'none' }}>
            {filtered.map((t) => {
              const cover = toolCover(t);
              return (
              <li key={t.slug} className="directory-list-row">
                <div style={{ width: 80 }}>
                  {cover ? (
                    <img src={cover} alt={t.name} style={{ display: 'block', width: 80, height: 60, objectFit: 'cover', border: '1px solid var(--line)' }} />
                  ) : (
                    <Thumb name={t.name} slug={t.slug} aspect="4/3" label="" />
                  )}
                </div>
                <div>
                  <Link href={`/tool/${t.slug}`}>
                    <div style={{ display: 'flex', alignItems: 'baseline', gap: 12 }}>
                      <h3 style={{ fontFamily: 'Fraunces, serif', fontSize: 22, fontWeight: 500, margin: 0, letterSpacing: '-0.01em' }}>{t.name}</h3>
                      <span style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#8a8580', letterSpacing: '0.04em' }}>{t.vendor}</span>
                    </div>
                    <p style={{ margin: '4px 0 0', fontSize: 13, color: 'var(--ink)', lineHeight: 1.45 }}>{t.tagline}</p>
                  </Link>
                </div>
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                  <Badge kind={t.dsgvo} />
                  <span style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 10, color: '#8a8580', letterSpacing: '0.04em' }}>{t.origin}</span>
                </div>
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6, alignItems: 'end' }}>
                  <label style={{ display: 'flex', alignItems: 'center', gap: 6, fontSize: 11, fontFamily: 'JetBrains Mono, monospace', color: '#8a8580', cursor: 'pointer', letterSpacing: '0.04em', textTransform: 'uppercase' }}>
                    <input type="checkbox" checked={has(t.slug)} onChange={() => toggle(t.slug)} style={{ accentColor: 'var(--accent)' }} />
                    Vergleichen
                  </label>
                </div>
              </li>
              );
            })}
          </ul>
        ) : (
          <div className="grid-3">
            {filtered.map((t) => {
              const cover = toolCover(t);
              return (
              <Link key={t.slug} href={`/tool/${t.slug}`} style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
                {cover ? (
                  <img src={cover} alt={t.name} style={{ display: 'block', width: '100%', height: 'auto', aspectRatio: '4 / 3', objectFit: 'cover', border: '1px solid var(--line)' }} />
                ) : (
                  <Thumb name={t.name} slug={t.slug} aspect="4/3" />
                )}
                <div>
                  <Badge kind={t.dsgvo} />
                </div>
                <h3 style={{ fontFamily: 'Fraunces, serif', fontSize: 22, fontWeight: 500, margin: 0, letterSpacing: '-0.01em' }}>{t.name}</h3>
                <p style={{ margin: 0, fontSize: 13, color: 'var(--ink)', lineHeight: 1.45 }}>{t.tagline}</p>
              </Link>
              );
            })}
          </div>
        )}
      </div>
    </div>
  );
}
