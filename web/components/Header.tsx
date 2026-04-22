'use client';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { Wordmark } from './Logo';
import { SearchBar } from './SearchBar';

const NAV = [
  { href: '/',          label: 'Start',       match: (p: string) => p === '/' },
  { href: '/verzeichnis', label: 'Verzeichnis', match: (p: string) => p.startsWith('/verzeichnis') || p.startsWith('/kategorie') },
  { href: '/vergleich', label: 'Vergleich',   match: (p: string) => p.startsWith('/vergleich') },
  { href: '/artikel/was-ist-ki', label: 'Artikel', match: (p: string) => p.startsWith('/artikel') },
  { href: '/suche', label: 'Suche',     match: (p: string) => p.startsWith('/suche') },
];

export function Header() {
  const pathname = usePathname();
  return (
    <header className="site-header">
      <div className="site-header-inner">
        <Link href="/" style={{ display: 'inline-flex' }}>
          <Wordmark size={36} />
        </Link>
        <nav className="site-nav">
          {NAV.map((item, i) => (
            <Link key={i} href={item.href} className={item.match(pathname) ? 'active' : ''}>
              {item.label}
            </Link>
          ))}
        </nav>
        <div className="site-header-search" style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
          <SearchBar variant="header" placeholder="Suche …" />
        </div>
      </div>
    </header>
  );
}
