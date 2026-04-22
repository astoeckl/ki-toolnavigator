'use client';
import Link from 'next/link';
import { useState } from 'react';
import type { Tool } from '@/lib/types';
import { Chip, SectionLabel, Thumb } from '@/components/ui';
import { Prose } from '@/components/Prose';

type Props = {
  t: Tool;
  catName: string;
  related: Tool[];
  overviewHtml: string | null;
  featuresHtml: string | null;
  pricingHtml: string | null;
};

const TABS = [
  { id: 'uebersicht', label: 'Übersicht' },
  { id: 'funktionen', label: 'Funktionen' },
  { id: 'preise',     label: 'Preise' },
];

export function ToolTabs({ t, catName, related, overviewHtml, featuresHtml, pricingHtml }: Props) {
  const [tab, setTab] = useState('uebersicht');
  return (
    <>
      <nav style={{ marginTop: 48, display: 'flex', gap: 0, borderBottom: '1px solid var(--line)' }}>
        {TABS.map((tb) => (
          <a key={tb.id} onClick={() => setTab(tb.id)} style={{
            padding: '12px 18px', cursor: 'pointer',
            fontFamily: 'Inter Tight, sans-serif', fontSize: 13,
            color: tab === tb.id ? 'var(--ink-strong)' : '#8a8580',
            borderBottom: tab === tb.id ? '2px solid var(--accent)' : '2px solid transparent',
            marginBottom: -1, fontWeight: tab === tb.id ? 600 : 400,
          }}>{tb.label}</a>
        ))}
      </nav>

      {tab === 'funktionen' ? (
        <div style={{ paddingTop: 36 }}>
          {featuresHtml ? (
            <Prose html={featuresHtml} />
          ) : (
            <p style={{ fontSize: 16, lineHeight: 1.75, color: 'var(--ink)', fontStyle: 'italic' }}>
              Funktionsliste folgt in Kürze.
            </p>
          )}
        </div>
      ) : tab === 'preise' ? (
        <div style={{ paddingTop: 36 }}>
          {pricingHtml ? (
            <Prose html={pricingHtml} />
          ) : (
            <p style={{ fontSize: 16, lineHeight: 1.75, color: 'var(--ink)', fontStyle: 'italic' }}>
              Preisangaben folgen in Kürze.
            </p>
          )}
        </div>
      ) : tab === 'uebersicht' ? (
        <div id="zusammenfassung" style={{ paddingTop: 36, scrollMarginTop: 100 }}>
          {overviewHtml ? (
            <Prose html={overviewHtml} dropCap />
          ) : (
            <p style={{ fontSize: 16, lineHeight: 1.75, color: 'var(--ink)', fontStyle: 'italic' }}>
              Übersichtstext folgt in Kürze.
            </p>
          )}

          {(() => {
            const sshot =
              typeof t.screenshot_id === 'string' ? t.screenshot_id :
              (t.screenshot_id && typeof t.screenshot_id === 'object') ? (t.screenshot_id.url ?? null) :
              null;
            if (!sshot) {
              return (
                <>
                  <SectionLabel id="screenshot">Bildergalerie</SectionLabel>
                  <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 12 }}>
                    <Thumb name={`${t.name} UI`} slug={`${t.slug}-1`} aspect="4/3" label="UI · Hauptansicht" />
                    <Thumb name={`${t.name} Ansicht 2`} slug={`${t.slug}-2`} aspect="4/3" label="UI · Einstellungen" />
                    <Thumb name={`${t.name} Ansicht 3`} slug={`${t.slug}-3`} aspect="4/3" label="UI · API-Playground" />
                  </div>
                </>
              );
            }
            return (
              <>
                <SectionLabel id="screenshot">Screenshot</SectionLabel>
                <figure style={{ margin: 0, border: '1px solid var(--line)', padding: 0 }}>
                  <img
                    src={sshot}
                    alt={`Screenshot der ${t.name}-Website`}
                    style={{ display: 'block', width: '100%', height: 'auto', aspectRatio: '16 / 10', objectFit: 'cover', objectPosition: 'top center' }}
                  />
                  <figcaption style={{
                    padding: '8px 14px',
                    borderTop: '1px solid var(--line)',
                    fontFamily: 'JetBrains Mono, monospace', fontSize: 10,
                    letterSpacing: '0.06em', textTransform: 'uppercase',
                    color: '#8a8580',
                    display: 'flex', justifyContent: 'space-between', gap: 12,
                  }}>
                    <span>{t.name} · Website-Screenshot</span>
                    <span>1280 × 800</span>
                  </figcaption>
                </figure>
              </>
            );
          })()}

          <SectionLabel id="pro-contra">Pro & Contra</SectionLabel>
          <div className="grid-pro-contra">
            <div>
              <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#2F6A44', letterSpacing: '0.08em', textTransform: 'uppercase', marginBottom: 10 }}>+ Pro</div>
              <ul style={{ paddingLeft: 16, margin: 0 }}>
                {t.pros.map((p, i) => <li key={i} style={{ fontSize: 14, lineHeight: 1.65, padding: '3px 0' }}>{p}</li>)}
              </ul>
            </div>
            <div>
              <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#8A2F2F', letterSpacing: '0.08em', textTransform: 'uppercase', marginBottom: 10 }}>− Contra</div>
              <ul style={{ paddingLeft: 16, margin: 0 }}>
                {t.cons.map((p, i) => <li key={i} style={{ fontSize: 14, lineHeight: 1.65, padding: '3px 0' }}>{p}</li>)}
              </ul>
            </div>
          </div>

          <SectionLabel id="anwendungsfaelle">Anwendungsfälle</SectionLabel>
          <div style={{ display: 'flex', gap: 8, flexWrap: 'wrap' }}>
            {t.usecases.map((u) => <Chip key={u} accent>{u}</Chip>)}
          </div>

          <SectionLabel id="verwandte-tools">Verwandte Tools</SectionLabel>
          <div className="grid-3">
            {related.map((r) => (
              <Link key={r.slug} href={`/tool/${r.slug}`} style={{ padding: 16, border: '1px solid var(--line)', display: 'flex', flexDirection: 'column', gap: 8 }}>
                <h4 style={{ fontFamily: 'Fraunces, serif', fontSize: 18, fontWeight: 500, margin: 0 }}>{r.name}</h4>
                <p style={{ margin: 0, fontSize: 12, color: 'var(--ink)', lineHeight: 1.4 }}>{r.tagline}</p>
              </Link>
            ))}
          </div>
        </div>
      ) : null}
    </>
  );
}
