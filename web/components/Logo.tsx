type LogoProps = { size?: number; color?: string; accent?: string };

export function LogoB({ size = 40, color = '#111', accent = 'var(--accent)' }: LogoProps) {
  return (
    <svg width={size} height={size} viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M10 54 L54 54 L22 10 Z" stroke={color} strokeWidth="3" fill="none" strokeLinejoin="miter" />
      <line x1="22" y1="10" x2="40" y2="46" stroke={color} strokeWidth="3" />
      <circle cx="40" cy="46" r="5.5" fill={accent} />
    </svg>
  );
}

export function Wordmark({ size = 40, color = '#111', accent = 'var(--accent)' }: LogoProps) {
  return (
    <div style={{ display: 'inline-flex', alignItems: 'center', gap: 12, lineHeight: 1 }}>
      <LogoB size={size} color={color} accent={accent} />
      <div style={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
        <span style={{
          fontFamily: 'Fraunces, Georgia, serif',
          fontWeight: 500,
          fontSize: size * 0.55,
          letterSpacing: '-0.02em',
          color,
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
