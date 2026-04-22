import './globals.css';
import type { Metadata } from 'next';
import { Header } from '@/components/Header';
import { Footer } from '@/components/Footer';
import { CompareProvider } from '@/components/CompareContext';

export const metadata: Metadata = {
  title: 'KI-Toolnavigator — Das kuratierte Verzeichnis für Künstliche Intelligenz',
  description:
    'KI-Tools, geprüft, verglichen und erklärt — auf Deutsch, nach DSGVO-Kriterien sortierbar. Ein Verzeichnis von ampunkt.technology.',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="de" suppressHydrationWarning>
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="" />
        <link
          href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..700;1,9..144,300..700&family=Inter+Tight:wght@300..700&family=JetBrains+Mono:wght@400;500&display=swap"
          rel="stylesheet"
        />
      </head>
      <body suppressHydrationWarning>
        <CompareProvider>
          <div className="top-banner">
            Redaktioneller Stand: 19. April 2026 · ein Projekt von{' '}
            <a href="#" target="_blank" rel="noreferrer">ampunkt.technology</a>{' '}
            · Inhalte aus Cognitor CMS · ISR 60s
          </div>
          <Header />
          <main className="page-content">{children}</main>
          <Footer />
        </CompareProvider>
      </body>
    </html>
  );
}
