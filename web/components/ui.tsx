'use client';
import Link from 'next/link';
import type { CSSProperties, ReactNode } from 'react';

type ChipProps = { children: ReactNode; accent?: boolean; mono?: boolean; onClick?: () => void };
export function Chip({ children, accent, mono = true, onClick }: ChipProps) {
  return (
    <span onClick={onClick} style={{
      display: 'inline-flex', alignItems: 'center', padding: '3px 8px',
      border: '1px solid ' + (accent ? 'var(--accent)' : 'var(--line)'),
      color: accent ? 'var(--accent)' : 'var(--ink)',
      fontFamily: mono ? 'JetBrains Mono, monospace' : 'Inter Tight, sans-serif',
      fontSize: 11, letterSpacing: mono ? '0.04em' : '0',
      textTransform: mono ? 'uppercase' : 'none',
      cursor: onClick ? 'pointer' : 'default', background: 'transparent', whiteSpace: 'nowrap',
    }}>{children}</span>
  );
}

export function Stars({ rating, size = 12 }: { rating: number; size?: number }) {
  const filled = Math.round(rating);
  return (
    <span style={{ display: 'inline-flex', gap: 1, color: 'var(--accent)', fontSize: size, letterSpacing: -1 }}>
      {'★★★★★'.split('').map((c, i) => (
        <span key={i} style={{ opacity: i < filled ? 1 : 0.18 }}>{c}</span>
      ))}
    </span>
  );
}

const dsgvoMap = {
  ja:      { bg: '#E8F3EC', fg: '#2F6A44', label: 'DSGVO-konform' },
  bedingt: { bg: '#FBF1DE', fg: '#8A6A1F', label: 'DSGVO bedingt' },
  nein:    { bg: '#F5E3E3', fg: '#8A2F2F', label: 'kein DSGVO-Nachweis' },
} as const;
type BadgeProps = { kind?: keyof typeof dsgvoMap; children?: ReactNode };
export function Badge({ kind, children }: BadgeProps) {
  const v = (kind && dsgvoMap[kind]) || { bg: '#F0EDE8', fg: '#5A5550', label: children };
  return (
    <span style={{
      display: 'inline-block', padding: '2px 8px', background: v.bg, color: v.fg,
      fontFamily: 'JetBrains Mono, monospace', fontSize: 10,
      letterSpacing: '0.06em', textTransform: 'uppercase',
    }}>{children || v.label}</span>
  );
}

type ThumbProps = { name: string; slug: string; aspect?: string; label?: string };
export function Thumb({ name, slug, aspect = '4/3', label }: ThumbProps) {
  const hueSeed = (slug || name).split('').reduce((a, c) => a + c.charCodeAt(0), 0);
  const stripe = hueSeed % 3 === 0 ? 'horizontal' : hueSeed % 3 === 1 ? 'diagonal' : 'vertical';
  const patternId = 'p-' + (slug || name).replace(/[^a-z0-9]/gi, '');
  const transform = stripe === 'diagonal' ? 'rotate(45)' : stripe === 'horizontal' ? 'rotate(0)' : 'rotate(90)';
  return (
    <div style={{
      aspectRatio: aspect, background: 'var(--bg-alt)',
      border: '1px solid var(--line)', position: 'relative', overflow: 'hidden',
    }}>
      <svg width="100%" height="100%" style={{ position: 'absolute', inset: 0 }} preserveAspectRatio="none">
        <defs>
          <pattern id={patternId} patternUnits="userSpaceOnUse" width="8" height="8" patternTransform={transform}>
            <rect width="8" height="8" fill="transparent" />
            <line x1="0" y1="0" x2="0" y2="8" stroke="#DDD7CC" strokeWidth="1" />
          </pattern>
        </defs>
        <rect width="100%" height="100%" fill={`url(#${patternId})`} />
      </svg>
      <div style={{
        position: 'absolute', inset: 0, display: 'flex', alignItems: 'center', justifyContent: 'center',
        fontFamily: 'JetBrains Mono, monospace', fontSize: 10,
        color: '#a8a39c', letterSpacing: '0.1em', textTransform: 'uppercase',
      }}>
        {label ?? `${name} · screenshot`}
      </div>
    </div>
  );
}

type Crumb = { label: string; href?: string };
export function Breadcrumb({ items }: { items: Crumb[] }) {
  return (
    <nav style={{
      fontFamily: 'JetBrains Mono, monospace',
      fontSize: 11, letterSpacing: '0.04em',
      color: '#8a8580', textTransform: 'uppercase', marginBottom: 28,
    }}>
      {items.map((it, i) => (
        <span key={i}>
          {i > 0 && <span style={{ margin: '0 8px', opacity: 0.5 }}>/</span>}
          {it.href ? (
            <Link href={it.href} style={{ color: 'inherit', textDecoration: 'none', borderBottom: '1px dotted #b8b3ac' }}>{it.label}</Link>
          ) : (
            <span style={{ color: 'var(--ink-strong)' }}>{it.label}</span>
          )}
        </span>
      ))}
    </nav>
  );
}

export function SectionLabel({ num, children, id }: { num?: string; children: ReactNode; id?: string }) {
  return (
    <div style={{
      display: 'flex', alignItems: 'baseline', gap: 14,
      borderBottom: '1px solid var(--line)',
      paddingBottom: 10, marginBottom: 28, marginTop: num ? 0 : 36,
    }}>
      {num && (
        <span style={{
          fontFamily: 'JetBrains Mono, monospace',
          fontSize: 11, letterSpacing: '0.08em', color: '#8a8580',
        }}>§ {num}</span>
      )}
      <h2 id={id} style={{
        fontFamily: 'Fraunces, Georgia, serif',
        fontWeight: 500, fontSize: 22, letterSpacing: '-0.01em',
        margin: 0, color: 'var(--ink-strong)',
        scrollMarginTop: 100,
      }}>{children}</h2>
    </div>
  );
}

type ButtonProps = {
  children: ReactNode;
  variant?: 'primary' | 'ghost' | 'accent';
  onClick?: () => void;
  href?: string;
  type?: 'button' | 'submit';
  icon?: ReactNode;
};
const buttonStyles: Record<string, CSSProperties> = {
  primary: { background: 'var(--ink-strong)', color: 'var(--bg)', border: '1px solid var(--ink-strong)' },
  ghost:   { background: 'transparent', color: 'var(--ink-strong)', border: '1px solid var(--line)' },
  accent:  { background: 'var(--accent)', color: '#fff', border: '1px solid var(--accent)' },
};
export function Button({ children, variant = 'primary', onClick, href, type = 'button', icon }: ButtonProps) {
  const style: CSSProperties = {
    ...buttonStyles[variant],
    padding: '9px 16px',
    fontFamily: 'Inter Tight, sans-serif', fontSize: 13,
    fontWeight: 500, letterSpacing: '0.01em',
    cursor: 'pointer', display: 'inline-flex', alignItems: 'center', gap: 8,
    textDecoration: 'none',
  };
  if (href) return <Link href={href} style={style}>{icon}{children}</Link>;
  return <button type={type} onClick={onClick} style={style}>{icon}{children}</button>;
}

export function DataRow({ label, value, mono }: { label: string; value: ReactNode; mono?: boolean }) {
  return (
    <div style={{
      display: 'grid', gridTemplateColumns: '120px 1fr',
      padding: '9px 0', borderBottom: '1px dotted var(--line)', fontSize: 13,
    }}>
      <span style={{
        fontFamily: 'JetBrains Mono, monospace',
        fontSize: 11, letterSpacing: '0.04em',
        color: '#8a8580', textTransform: 'uppercase', paddingTop: 1,
      }}>{label}</span>
      <span style={{
        fontFamily: mono ? 'JetBrains Mono, monospace' : 'Inter Tight, sans-serif',
        color: 'var(--ink-strong)',
      }}>{value}</span>
    </div>
  );
}
