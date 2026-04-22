// Shared UI components for KI-Toolnavigator

function Chip({ children, accent, mono = true, onClick }) {
  return (
    <span onClick={onClick} style={{
      display: 'inline-flex',
      alignItems: 'center',
      padding: '3px 8px',
      border: '1px solid ' + (accent ? 'var(--accent)' : 'var(--line)'),
      color: accent ? 'var(--accent)' : 'var(--ink)',
      fontFamily: mono ? 'JetBrains Mono, monospace' : 'Inter Tight, sans-serif',
      fontSize: 11,
      letterSpacing: mono ? '0.04em' : '0',
      textTransform: mono ? 'uppercase' : 'none',
      cursor: onClick ? 'pointer' : 'default',
      background: 'transparent',
      whiteSpace: 'nowrap',
    }}>{children}</span>
  );
}

function Stars({ rating, size = 12 }) {
  const filled = Math.round(rating);
  return (
    <span style={{ display: 'inline-flex', gap: 1, color: 'var(--accent)', fontSize: size, letterSpacing: -1 }}>
      {'★★★★★'.split('').map((c, i) => (
        <span key={i} style={{ opacity: i < filled ? 1 : 0.18 }}>{c}</span>
      ))}
    </span>
  );
}

function Badge({ kind, children }) {
  const map = {
    ja:      { bg: '#E8F3EC', fg: '#2F6A44', label: 'DSGVO-konform' },
    bedingt: { bg: '#FBF1DE', fg: '#8A6A1F', label: 'DSGVO bedingt' },
    nein:    { bg: '#F5E3E3', fg: '#8A2F2F', label: 'kein DSGVO-Nachweis' },
  };
  const v = map[kind] || { bg: '#F0EDE8', fg: '#5A5550', label: children };
  return (
    <span style={{
      display: 'inline-block', padding: '2px 8px',
      background: v.bg, color: v.fg,
      fontFamily: 'JetBrains Mono, monospace', fontSize: 10,
      letterSpacing: '0.06em', textTransform: 'uppercase',
    }}>{children || v.label}</span>
  );
}

function Thumb({ name, slug, aspect = '4/3', label }) {
  // Striped SVG placeholder with monospace label — pro Tool pseudo-einzigartig
  const hueSeed = (slug || name).split('').reduce((a, c) => a + c.charCodeAt(0), 0);
  const rot = (hueSeed % 90) - 45;
  const stripe = hueSeed % 3 === 0 ? 'horizontal' : hueSeed % 3 === 1 ? 'diagonal' : 'vertical';
  return (
    <div style={{
      aspectRatio: aspect,
      background: 'var(--bg-alt)',
      border: '1px solid var(--line)',
      position: 'relative',
      overflow: 'hidden',
    }}>
      <svg width="100%" height="100%" style={{ position: 'absolute', inset: 0 }} preserveAspectRatio="none">
        <defs>
          <pattern id={'p-' + slug} patternUnits="userSpaceOnUse" width="8" height="8" patternTransform={stripe === 'diagonal' ? 'rotate(45)' : stripe === 'horizontal' ? 'rotate(0)' : 'rotate(90)'}>
            <rect width="8" height="8" fill="transparent" />
            <line x1="0" y1="0" x2="0" y2="8" stroke="var(--line)" strokeWidth="1" />
          </pattern>
        </defs>
        <rect width="100%" height="100%" fill={'url(#p-' + slug + ')'} />
      </svg>
      <div style={{
        position: 'absolute', inset: 0,
        display: 'flex', alignItems: 'center', justifyContent: 'center',
        fontFamily: 'JetBrains Mono, monospace', fontSize: 10,
        color: '#a8a39c', letterSpacing: '0.1em', textTransform: 'uppercase',
      }}>
        {label || (name + ' · screenshot')}
      </div>
    </div>
  );
}

function Breadcrumb({ items, onNav }) {
  return (
    <nav style={{
      fontFamily: 'JetBrains Mono, monospace',
      fontSize: 11, letterSpacing: '0.04em',
      color: '#8a8580', textTransform: 'uppercase',
      marginBottom: 28,
    }}>
      {items.map((it, i) => (
        <span key={i}>
          {i > 0 && <span style={{ margin: '0 8px', opacity: 0.5 }}>/</span>}
          {it.to ? (
            <a onClick={() => onNav(it.to)} style={{ color: 'inherit', cursor: 'pointer', textDecoration: 'none', borderBottom: '1px dotted #b8b3ac' }}>{it.label}</a>
          ) : (
            <span style={{ color: 'var(--ink-strong)' }}>{it.label}</span>
          )}
        </span>
      ))}
    </nav>
  );
}

function SectionLabel({ num, children }) {
  return (
    <div style={{
      display: 'flex', alignItems: 'baseline', gap: 14,
      borderBottom: '1px solid var(--line)',
      paddingBottom: 10, marginBottom: 28,
    }}>
      {num && (
        <span style={{
          fontFamily: 'JetBrains Mono, monospace',
          fontSize: 11, letterSpacing: '0.08em',
          color: '#8a8580',
        }}>§ {num}</span>
      )}
      <h2 style={{
        fontFamily: 'Fraunces, Georgia, serif',
        fontWeight: 500, fontSize: 22,
        letterSpacing: '-0.01em', margin: 0,
        color: 'var(--ink-strong)',
      }}>{children}</h2>
    </div>
  );
}

function Button({ children, variant = 'primary', onClick, icon }) {
  const styles = {
    primary: { background: 'var(--ink-strong)', color: 'var(--bg)', border: '1px solid var(--ink-strong)' },
    ghost:   { background: 'transparent', color: 'var(--ink-strong)', border: '1px solid var(--line)' },
    accent:  { background: 'var(--accent)', color: '#fff', border: '1px solid var(--accent)' },
  };
  return (
    <button onClick={onClick} style={{
      ...styles[variant],
      padding: '9px 16px',
      fontFamily: 'Inter Tight, sans-serif', fontSize: 13,
      fontWeight: 500, letterSpacing: '0.01em',
      cursor: 'pointer', display: 'inline-flex', alignItems: 'center', gap: 8,
    }}>
      {icon} {children}
    </button>
  );
}

function DataRow({ label, value, mono }) {
  return (
    <div style={{
      display: 'grid', gridTemplateColumns: '120px 1fr',
      padding: '9px 0', borderBottom: '1px dotted var(--line)',
      fontSize: 13,
    }}>
      <span style={{
        fontFamily: 'JetBrains Mono, monospace',
        fontSize: 11, letterSpacing: '0.04em',
        color: '#8a8580', textTransform: 'uppercase',
        paddingTop: 1,
      }}>{label}</span>
      <span style={{
        fontFamily: mono ? 'JetBrains Mono, monospace' : 'Inter Tight, sans-serif',
        color: 'var(--ink-strong)',
      }}>{value}</span>
    </div>
  );
}

Object.assign(window, { Chip, Stars, Badge, Thumb, Breadcrumb, SectionLabel, Button, DataRow });
