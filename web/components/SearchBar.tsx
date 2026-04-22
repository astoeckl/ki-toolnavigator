'use client';
import { useRouter } from 'next/navigation';
import { useEffect, useId, useRef, useState } from 'react';

type Variant = 'hero' | 'inline' | 'header';
type Props = { variant?: Variant; placeholder?: string; defaultValue?: string };

const styles: Record<Variant, { container: React.CSSProperties; input: React.CSSProperties; button?: React.CSSProperties }> = {
  hero: {
    container: { border: '1px solid var(--ink-strong)', padding: 2, flex: '0 1 460px' },
    input: { fontSize: 14, padding: '12px 14px' },
    button: { background: 'var(--ink-strong)', color: 'var(--bg)', padding: '11px 18px', border: 'none', cursor: 'pointer', fontFamily: 'Inter Tight, sans-serif', fontSize: 13, fontWeight: 500 },
  },
  inline: {
    container: { border: '1px solid var(--line)', padding: 2 },
    input: { fontSize: 13, padding: '10px 14px' },
  },
  header: {
    container: { border: '1px solid var(--line)', padding: 2, width: '100%', maxWidth: 260 },
    input: { fontSize: 12, padding: '7px 10px', minWidth: 0 },
  },
};

export function SearchBar({ variant = 'inline', placeholder, defaultValue = '' }: Props) {
  const router = useRouter();
  const [q, setQ] = useState(defaultValue);
  const [open, setOpen] = useState(false);
  const [activeIdx, setActiveIdx] = useState(-1);
  const [suggestions, setSuggestions] = useState<string[]>([]);
  const wrapRef = useRef<HTMLDivElement>(null);
  const debounceRef = useRef<ReturnType<typeof setTimeout> | null>(null);
  const listboxId = useId();

  // Close on outside click
  useEffect(() => {
    function onDoc(e: MouseEvent) {
      if (!wrapRef.current?.contains(e.target as Node)) setOpen(false);
    }
    document.addEventListener('mousedown', onDoc);
    return () => document.removeEventListener('mousedown', onDoc);
  }, []);

  // Debounced suggest fetch
  useEffect(() => {
    if (debounceRef.current) clearTimeout(debounceRef.current);
    if (q.trim().length < 2) {
      setSuggestions([]);
      return;
    }
    debounceRef.current = setTimeout(async () => {
      try {
        const res = await fetch(`/api/suggest?q=${encodeURIComponent(q)}`);
        const data = await res.json();
        if (Array.isArray(data)) {
          setSuggestions(data);
          setOpen(data.length > 0);
          setActiveIdx(-1);
        }
      } catch {
        // silent
      }
    }, 180);
    return () => { if (debounceRef.current) clearTimeout(debounceRef.current); };
  }, [q]);

  const submit = (value: string) => {
    if (!value.trim()) return;
    setOpen(false);
    router.push(`/suche?q=${encodeURIComponent(value.trim())}`);
  };

  const onKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'ArrowDown') {
      e.preventDefault();
      if (suggestions.length > 0) {
        setOpen(true);
        setActiveIdx((i) => Math.min(suggestions.length - 1, i + 1));
      }
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      setActiveIdx((i) => Math.max(-1, i - 1));
    } else if (e.key === 'Enter') {
      e.preventDefault();
      submit(activeIdx >= 0 ? suggestions[activeIdx] : q);
    } else if (e.key === 'Escape') {
      setOpen(false);
    }
  };

  const v = styles[variant];
  const showButton = variant === 'hero';

  return (
    <div ref={wrapRef} style={{
      position: 'relative',
      flex: variant === 'hero' ? '0 1 460px' : variant === 'header' ? '1 1 180px' : 'initial',
      maxWidth: variant === 'hero' ? 460 : variant === 'header' ? 260 : '100%',
      width: '100%',
    }}>
      <div style={{ display: 'flex', alignItems: 'center', background: 'var(--bg)', ...v.container }}>
        <input
          value={q}
          onChange={(e) => { setQ(e.target.value); setOpen(true); }}
          onFocus={() => { if (suggestions.length > 0) setOpen(true); }}
          onKeyDown={onKeyDown}
          placeholder={placeholder ?? 'Tool, Kategorie oder Use-Case suchen …'}
          aria-autocomplete="list"
          aria-controls={listboxId}
          aria-expanded={open}
          role="combobox"
          style={{
            flex: 1, border: 'none', outline: 'none', background: 'transparent',
            color: 'var(--ink-strong)', fontFamily: 'Inter Tight, sans-serif', ...v.input,
          }}
        />
        {showButton && (
          <button onClick={() => submit(q)} style={v.button}>Suchen →</button>
        )}
      </div>

      {open && suggestions.length > 0 && (
        <ul id={listboxId} role="listbox" style={{
          position: 'absolute', top: 'calc(100% + 4px)', left: 0, right: 0,
          width: 'auto',
          minWidth: 0,
          maxWidth: '100vw',
          margin: 0, padding: 0, listStyle: 'none',
          background: 'var(--bg)',
          border: '1px solid var(--ink-strong)',
          boxShadow: '4px 4px 0 var(--ink-strong)',
          zIndex: 100,
        }}>
          {suggestions.map((s, i) => (
            <li key={i} role="option" aria-selected={i === activeIdx}
                onMouseEnter={() => setActiveIdx(i)}
                onMouseDown={(e) => { e.preventDefault(); submit(s); }}
                style={{
                  padding: '10px 14px',
                  fontSize: 13,
                  cursor: 'pointer',
                  background: i === activeIdx ? 'var(--bg-alt)' : 'transparent',
                  borderBottom: i < suggestions.length - 1 ? '1px dotted var(--line)' : 'none',
                  fontFamily: 'Inter Tight, sans-serif',
                  wordBreak: 'break-word',
                  overflowWrap: 'anywhere',
                  display: 'flex', gap: 6, alignItems: 'baseline',
                }}>
              <span style={{
                fontFamily: 'JetBrains Mono, monospace', fontSize: 10, color: '#8a8580',
                letterSpacing: '0.06em', textTransform: 'uppercase', marginRight: 10,
              }}>↗</span>
              {s}
            </li>
          ))}
          <li style={{
            padding: '8px 14px', fontFamily: 'JetBrains Mono, monospace',
            fontSize: 10, letterSpacing: '0.06em', color: '#8a8580',
            textTransform: 'uppercase', borderTop: '1px solid var(--line)',
            background: 'var(--bg-alt)',
          }}>
            Vorschläge: Cognitor Search
          </li>
        </ul>
      )}
    </div>
  );
}
