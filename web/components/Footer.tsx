import Link from 'next/link';
import { Wordmark } from './Logo';
import { getCategories } from '@/lib/cms';

export async function Footer() {
  const categories = await getCategories();
  return (
    <footer className="site-footer">
      <div className="site-footer-inner">
        <div>
          <Wordmark size={34} />
          <p style={{ fontSize: 13, lineHeight: 1.6, color: 'var(--ink)', marginTop: 18, maxWidth: 360 }}>
            Ein Verzeichnis für Künstliche Intelligenz — kuratiert, verglichen,
            eingeordnet. Ein Projekt von <b>ampunkt.technology</b>.
          </p>
        </div>
        <div>
          <h5>Navigation</h5>
          <ul>
            <li><Link href="/">Startseite</Link></li>
            <li><Link href="/verzeichnis">Tool-Verzeichnis</Link></li>
            <li><Link href="/vergleich">Vergleich</Link></li>
            <li><Link href="/artikel/was-ist-ki">Artikel</Link></li>
          </ul>
        </div>
        <div>
          <h5>Kategorien</h5>
          <ul>
            {categories.slice(0, 5).map((c) => (
              <li key={c.slug}><Link href={`/kategorie/${c.slug}`}>{c.name}</Link></li>
            ))}
          </ul>
        </div>
        <div>
          <h5>Rechtliches</h5>
          <ul>
            <li><Link href="/impressum">Impressum</Link></li>
            <li><Link href="/impressum#datenschutz">Datenschutz</Link></li>
            <li><a href="mailto:andreas@stoeckl.ai">Kontakt</a></li>
          </ul>
        </div>
      </div>
      <div className="site-footer-bottom">
        <span>© 2026 Dr. Andreas Stöckl — alle Rechte vorbehalten</span>
        <span>www.ki-toolnavigator.com</span>
      </div>
    </footer>
  );
}
