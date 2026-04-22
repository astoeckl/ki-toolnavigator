// KI-Toolnavigator Logo-Komponenten (Kompass-Metapher)
// Zwei Varianten: A — minimaler Kompass; B — Dreieck-Nadel mit Punkt

function LogoA({ size = 40, color = '#111', accent = 'var(--accent)' }) {
  // Kompass-Rose: Dreieckige Nordspitze mit Punkt, feine Kreuzlinien
  const s = size;
  return (
    <svg width={s} height={s} viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
      {/* Äußerer Kreis */}
      <circle cx="32" cy="32" r="30" stroke={color} strokeWidth="1.2" />
      {/* Feine Tick-Marken an Kardinalpunkten */}
      <line x1="32" y1="2" x2="32" y2="7" stroke={color} strokeWidth="1.2" />
      <line x1="32" y1="57" x2="32" y2="62" stroke={color} strokeWidth="1.2" />
      <line x1="2" y1="32" x2="7" y2="32" stroke={color} strokeWidth="1.2" />
      <line x1="57" y1="32" x2="62" y2="32" stroke={color} strokeWidth="1.2" />
      {/* Nordnadel — schwarzes Dreieck (Echo des ampunkt-Logos) */}
      <path d="M32 8 L24 38 L32 34 L40 38 Z" fill={color} />
      {/* Südnadel — hohles Dreieck */}
      <path d="M32 56 L24 26 L32 30 L40 26 Z" fill="none" stroke={color} strokeWidth="1.2" strokeLinejoin="round" />
      {/* Magenta-Punkt am Drehpunkt */}
      <circle cx="32" cy="32" r="3.2" fill={accent} />
    </svg>
  );
}

function LogoB({ size = 40, color = '#111', accent = 'var(--accent)' }) {
  // Direkte Adaption des ampunkt-Dreiecks als Navigator-Pfeil
  const s = size;
  return (
    <svg width={s} height={s} viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
      {/* Großes asymmetrisches Dreieck wie bei ampunkt. */}
      <path d="M10 54 L54 54 L22 10 Z" stroke={color} strokeWidth="3" fill="none" strokeLinejoin="miter" />
      {/* Innenlinie / Kompassnadel diagonal */}
      <line x1="22" y1="10" x2="40" y2="46" stroke={color} strokeWidth="3" />
      {/* Magenta-Punkt (wie bei ampunkt.) */}
      <circle cx="40" cy="46" r="5.5" fill={accent} />
    </svg>
  );
}

function Wordmark({ variant = 'A', size = 40, color = '#111', accent = 'var(--accent)' }) {
  const Logo = variant === 'B' ? LogoB : LogoA;
  return (
    <div style={{ display: 'inline-flex', alignItems: 'center', gap: 12, lineHeight: 1 }}>
      <Logo size={size} color={color} accent={accent} />
      <div style={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
        <span style={{
          fontFamily: 'Fraunces, Georgia, serif',
          fontWeight: 500,
          fontSize: size * 0.55,
          letterSpacing: '-0.02em',
          color: color,
        }}>
          ki<span style={{ color: accent }}>·</span>toolnavigator
        </span>
        <span style={{
          fontFamily: 'JetBrains Mono, monospace',
          fontSize: size * 0.22,
          letterSpacing: '0.2em',
          color: '#8a8580',
          textTransform: 'uppercase',
        }}>
          Das deutsche KI-Verzeichnis
        </span>
      </div>
    </div>
  );
}

Object.assign(window, { LogoA, LogoB, Wordmark });
