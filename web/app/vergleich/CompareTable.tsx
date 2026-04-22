'use client';
import Link from 'next/link';
import type { ReactNode } from 'react';
import type { Category, Tool } from '@/lib/types';
import { EDITORIAL_DATE_SHORT } from '@/lib/site';
import { Badge, Thumb } from '@/components/ui';
import { useCompare } from '@/components/CompareContext';

/** Resolve tool cover URL from media_id (public endpoint returns a string). */
function toolCover(t: Tool): string | null {
  if (typeof t.media_id === 'string') return t.media_id;
  if (t.media_id && typeof t.media_id === 'object') return t.media_id.url ?? null;
  return null;
}

type Props = { tools: Tool[]; categories: Category[] };

export function CompareTable({ tools, categories }: Props) {
  const { compareList, remove } = useCompare();
  const items = compareList.length
    ? compareList.map((s) => tools.find((t) => t.slug === s)).filter(Boolean) as Tool[]
    : tools.slice(0, 3);

  const rows: { label: string; mono?: boolean; get: (t: Tool) => ReactNode }[] = [
    { label: 'Anbieter',     get: (t) => t.vendor, mono: true },
    { label: 'Herkunft',     get: (t) => t.origin, mono: true },
    { label: 'Kategorie',    get: (t) => categories.find((c) => c.slug === t.category)?.name },
    { label: 'Preis',        get: (t) => t.price },
    { label: 'API',          get: (t) => (t.api ? 'Ja' : 'Nein'), mono: true },
    { label: 'DSGVO',        get: (t) => <Badge kind={t.dsgvo} /> },
    { label: 'Launch',       get: (t) => new Date(t.launched).toLocaleDateString('de-DE'), mono: true },
    { label: 'Aktualisiert', get: (t) => new Date(t._updated_at ?? t.lastUpdated).toLocaleDateString('de-DE'), mono: true },
  ];

  return (
    <>
      <div style={{ borderBottom: '1px solid var(--line)', paddingBottom: 32, marginBottom: 40 }}>
        <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#8a8580', letterSpacing: '0.08em', textTransform: 'uppercase', marginBottom: 12 }}>Direktvergleich</div>
        <h1 className="h-editorial-md" style={{ fontFamily: 'Fraunces, serif', fontWeight: 400, margin: 0, textWrap: 'balance' as const }}>
          {items.map((t) => t.name).join(' vs. ')}
        </h1>
        <p style={{ fontFamily: 'Fraunces, serif', fontSize: 18, lineHeight: 1.5, color: 'var(--ink)', marginTop: 16, maxWidth: 720 }}>
          Tabellarische Gegenüberstellung der wichtigsten Merkmale — gepflegt von der Redaktion am{' '}
          {EDITORIAL_DATE_SHORT}.
        </p>
      </div>

      <div className="table-scroll" style={{ border: '1px solid var(--line)' }}>
        <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: 13 }}>
          <thead>
            <tr>
              <th style={{ padding: 16, textAlign: 'left', borderBottom: '1px solid var(--ink-strong)', width: 180, fontFamily: 'JetBrains Mono, monospace', fontSize: 10, letterSpacing: '0.08em', textTransform: 'uppercase', color: '#8a8580', verticalAlign: 'bottom' }}>Merkmal</th>
              {items.map((t) => {
                const cover = toolCover(t);
                return (
                <th key={t.slug} style={{ padding: 16, textAlign: 'left', borderBottom: '1px solid var(--ink-strong)', verticalAlign: 'bottom', borderLeft: '1px solid var(--line)' }}>
                  {cover ? (
                    <img src={cover} alt={t.name} style={{ display: 'block', width: '100%', height: 'auto', aspectRatio: '4 / 3', objectFit: 'cover', border: '1px solid var(--line)' }} />
                  ) : (
                    <Thumb name={t.name} slug={`${t.slug}-cmp`} aspect="4/3" label="" />
                  )}
                  <h3 style={{ fontFamily: 'Fraunces, serif', fontSize: 22, fontWeight: 500, margin: '12px 0 4px', letterSpacing: '-0.01em' }}>
                    <Link href={`/tool/${t.slug}`}>{t.name}</Link>
                  </h3>
                  <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 10, color: '#8a8580', letterSpacing: '0.04em', textTransform: 'uppercase', marginBottom: 8 }}>{t.vendor}</div>
                  <a onClick={() => remove(t.slug)} style={{ cursor: 'pointer', fontSize: 11, color: '#8a8580', fontFamily: 'JetBrains Mono, monospace', borderBottom: '1px dotted #8a8580', letterSpacing: '0.04em', textTransform: 'uppercase' }}>× Entfernen</a>
                </th>
                );
              })}
              {items.length < 4 && (
                <th style={{ padding: 16, borderBottom: '1px solid var(--ink-strong)', borderLeft: '1px solid var(--line)', verticalAlign: 'middle', background: 'var(--bg-alt)', width: 180 }}>
                  <Link href="/verzeichnis" style={{ fontFamily: 'Fraunces, serif', fontSize: 16, fontStyle: 'italic', color: 'var(--accent)' }}>+ Tool hinzufügen</Link>
                </th>
              )}
            </tr>
          </thead>
          <tbody>
            {rows.map((r) => (
              <tr key={r.label}>
                <td style={{ padding: '14px 16px', borderBottom: '1px dotted var(--line)', fontFamily: 'JetBrains Mono, monospace', fontSize: 11, letterSpacing: '0.04em', textTransform: 'uppercase', color: '#8a8580' }}>{r.label}</td>
                {items.map((t) => (
                  <td key={t.slug} style={{ padding: '14px 16px', borderBottom: '1px dotted var(--line)', borderLeft: '1px solid var(--line)', fontFamily: r.mono ? 'JetBrains Mono, monospace' : 'Inter Tight, sans-serif', color: 'var(--ink-strong)' }}>
                    {r.get(t)}
                  </td>
                ))}
                {items.length < 4 && <td style={{ borderBottom: '1px dotted var(--line)', borderLeft: '1px solid var(--line)', background: 'var(--bg-alt)' }} />}
              </tr>
            ))}
            <tr>
              <td style={{ padding: '14px 16px', borderBottom: '1px dotted var(--line)', fontFamily: 'JetBrains Mono, monospace', fontSize: 11, letterSpacing: '0.04em', textTransform: 'uppercase', color: '#8a8580', verticalAlign: 'top' }}>Stärken</td>
              {items.map((t) => (
                <td key={t.slug} style={{ padding: '14px 16px', borderBottom: '1px dotted var(--line)', borderLeft: '1px solid var(--line)', verticalAlign: 'top' }}>
                  <ul style={{ padding: 0, margin: 0, listStyle: 'none' }}>
                    {t.pros.map((p, i) => <li key={i} style={{ fontSize: 12, lineHeight: 1.5, padding: '2px 0', color: 'var(--ink)' }}>+ {p}</li>)}
                  </ul>
                </td>
              ))}
              {items.length < 4 && <td style={{ borderBottom: '1px dotted var(--line)', borderLeft: '1px solid var(--line)', background: 'var(--bg-alt)' }} />}
            </tr>
            <tr>
              <td style={{ padding: '14px 16px', fontFamily: 'JetBrains Mono, monospace', fontSize: 11, letterSpacing: '0.04em', textTransform: 'uppercase', color: '#8a8580', verticalAlign: 'top' }}>Schwächen</td>
              {items.map((t) => (
                <td key={t.slug} style={{ padding: '14px 16px', borderLeft: '1px solid var(--line)', verticalAlign: 'top' }}>
                  <ul style={{ padding: 0, margin: 0, listStyle: 'none' }}>
                    {t.cons.map((p, i) => <li key={i} style={{ fontSize: 12, lineHeight: 1.5, padding: '2px 0', color: 'var(--ink)' }}>− {p}</li>)}
                  </ul>
                </td>
              ))}
              {items.length < 4 && <td style={{ borderLeft: '1px solid var(--line)', background: 'var(--bg-alt)' }} />}
            </tr>
          </tbody>
        </table>
      </div>

    </>
  );
}
