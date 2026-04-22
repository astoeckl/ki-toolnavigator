'use client';
import type { CSSProperties, ReactNode } from 'react';

type Props = { href: string; children: ReactNode; style?: CSSProperties; className?: string };

/** Anchor link that explicitly scrolls the target into view + updates the URL hash.
 *  Works around environments where the browser's default hash-jump doesn't fire
 *  (e.g. nested iframes, custom scroll roots). */
export function AnchorLink({ href, children, style, className }: Props) {
  const onClick = (e: React.MouseEvent<HTMLAnchorElement>) => {
    if (!href.startsWith('#')) return;
    const id = href.slice(1);
    const el = document.getElementById(id);
    if (!el) return;
    e.preventDefault();
    // Compute absolute target Y, subtract scroll-margin so the sticky header doesn't hide it
    const targetY = Math.max(0, el.getBoundingClientRect().top + window.scrollY - 90);
    // Use the positional form: works in real browsers AND in preview iframes
    // where requestAnimationFrame doesn't fire and `behavior: 'smooth'` is ignored.
    window.scrollTo(0, targetY);
    history.replaceState(null, '', href);
  };
  return (
    <a href={href} onClick={onClick} style={style} className={className}>
      {children}
    </a>
  );
}
