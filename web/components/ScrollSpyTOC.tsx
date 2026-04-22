'use client';
import { useEffect, useState } from 'react';
import { AnchorLink } from './AnchorLink';

export type TocItem = {
  /** Display label */
  label: string;
  /** Anchor hash including the leading `#` */
  hash: string;
  /** Optional small prefix shown before the label (e.g. "01") */
  num?: string;
};

type Props = {
  items: TocItem[];
  /** Optional uppercase eyebrow (e.g. "Inhalt", "Inhaltsverzeichnis") */
  eyebrow?: string;
};

/** A vertical TOC that updates the active item as the user scrolls past
 *  the matching `<h2 id="…">` (or any element) in the document. */
export function ScrollSpyTOC({ items, eyebrow = 'Inhalt' }: Props) {
  const [activeHash, setActiveHash] = useState<string>(items[0]?.hash ?? '');

  useEffect(() => {
    const targets = items
      .map((it) => ({ id: it.hash.slice(1), el: document.getElementById(it.hash.slice(1)) }))
      .filter((t): t is { id: string; el: HTMLElement } => !!t.el);
    if (targets.length === 0) return;

    // Active = the LAST section whose top has crossed `offset` (pixels from viewport top).
    // Falls back to first if none has crossed yet.
    const offset = 120;
    const compute = () => {
      let activeId = targets[0].id;
      for (const t of targets) {
        const top = t.el.getBoundingClientRect().top;
        if (top - offset <= 0) activeId = t.id;
        else break;
      }
      setActiveHash((prev) => (prev === '#' + activeId ? prev : '#' + activeId));
    };
    // Lightweight throttle via timestamp — avoids requestAnimationFrame which
    // is unreliable inside some preview iframes.
    let last = 0;
    const onScroll = () => {
      const now = Date.now();
      if (now - last < 60) return;
      last = now;
      compute();
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll);
    compute();
    // Final compute slightly later in case the layout settles after fonts/images.
    const t1 = setTimeout(compute, 200);
    return () => {
      window.removeEventListener('scroll', onScroll);
      window.removeEventListener('resize', onScroll);
      clearTimeout(t1);
    };
  }, [items]);

  return (
    <>
      <div style={{
        fontFamily: 'JetBrains Mono, monospace', fontSize: 11,
        color: '#8a8580', letterSpacing: '0.08em', textTransform: 'uppercase',
        marginBottom: 14,
      }}>
        {eyebrow}
      </div>
      <ul style={{ listStyle: 'none', padding: 0, margin: 0, borderLeft: '1px solid var(--line)' }}>
        {items.map((it) => {
          const active = it.hash === activeHash;
          return (
            <li key={it.hash} style={{
              padding: '6px 14px', fontSize: 13,
              borderLeft: active ? '2px solid var(--accent)' : '2px solid transparent',
              marginLeft: -1,
              color: active ? 'var(--accent)' : 'var(--ink)',
              transition: 'color 0.15s, border-color 0.15s',
            }}>
              {it.num && (
                <span style={{
                  fontFamily: 'JetBrains Mono, monospace', fontSize: 10,
                  marginRight: 8, color: '#8a8580',
                }}>{it.num}</span>
              )}
              <AnchorLink href={it.hash} style={{ color: 'inherit', cursor: 'pointer' }}>
                {it.label}
              </AnchorLink>
            </li>
          );
        })}
      </ul>
    </>
  );
}
