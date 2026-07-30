'use client';

import { useEffect, useState } from 'react';

const STORAGE_KEY = 'ki-consent';

/** Google Consent Mode v2 banner.
 *  Default consent is set to "denied" in the root layout before GA loads;
 *  this banner flips analytics/ads consent to "granted" on opt-in and persists
 *  the choice in localStorage so it isn't shown again. */
export function CookieConsent() {
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    try {
      const stored = localStorage.getItem(STORAGE_KEY);
      if (stored !== 'granted' && stored !== 'denied') setVisible(true);
    } catch {
      setVisible(true);
    }
  }, []);

  // Re-open the banner when the footer's "Cookie-Einstellungen" link is used.
  useEffect(() => {
    const open = () => setVisible(true);
    window.addEventListener('ki:open-consent', open);
    return () => window.removeEventListener('ki:open-consent', open);
  }, []);

  const decide = (granted: boolean) => {
    try {
      localStorage.setItem(STORAGE_KEY, granted ? 'granted' : 'denied');
    } catch {}
    const value = granted ? 'granted' : 'denied';
    const gtag = (window as unknown as { gtag?: (...a: unknown[]) => void }).gtag;
    if (typeof gtag === 'function') {
      gtag('consent', 'update', {
        ad_storage: value,
        ad_user_data: value,
        ad_personalization: value,
        analytics_storage: value,
      });
    }
    setVisible(false);
  };

  if (!visible) return null;

  const btnBase: React.CSSProperties = {
    fontFamily: "'JetBrains Mono', monospace",
    fontSize: 12,
    letterSpacing: '0.04em',
    textTransform: 'uppercase',
    padding: '10px 18px',
    borderRadius: 2,
    cursor: 'pointer',
    border: '1px solid var(--ink-strong)',
    whiteSpace: 'nowrap',
  };

  return (
    <div
      role="dialog"
      aria-label="Cookie-Einwilligung"
      aria-live="polite"
      style={{
        position: 'fixed',
        left: 16,
        right: 16,
        bottom: 16,
        zIndex: 1000,
        margin: '0 auto',
        maxWidth: 760,
        background: 'var(--bg)',
        border: '1px solid var(--line)',
        boxShadow: '0 8px 30px rgba(23,20,15,0.14)',
        borderRadius: 4,
        padding: 'clamp(16px, 3vw, 22px)',
        display: 'flex',
        flexWrap: 'wrap',
        alignItems: 'center',
        gap: 16,
      }}
    >
      <p
        style={{
          flex: '1 1 320px',
          margin: 0,
          fontFamily: "'Inter Tight', system-ui, sans-serif",
          fontSize: 14,
          lineHeight: 1.55,
          color: 'var(--ink)',
        }}
      >
        Wir nutzen Google Analytics, um die Nutzung dieser Seite zu verstehen und sie
        zu verbessern. Analyse-Cookies werden nur mit Ihrer Einwilligung gesetzt. Mehr
        dazu in der{' '}
        <a
          href="/impressum#datenschutz"
          style={{ color: 'var(--accent)', borderBottom: '1px dotted var(--accent)' }}
        >
          Datenschutzerklärung
        </a>
        .
      </p>
      <div style={{ display: 'flex', gap: 10, flexWrap: 'wrap' }}>
        <button
          type="button"
          onClick={() => decide(false)}
          style={{ ...btnBase, background: 'transparent', color: 'var(--ink-strong)' }}
        >
          Ablehnen
        </button>
        <button
          type="button"
          onClick={() => decide(true)}
          style={{ ...btnBase, background: 'var(--accent)', color: '#fff', borderColor: 'var(--accent)' }}
        >
          Akzeptieren
        </button>
      </div>
    </div>
  );
}
