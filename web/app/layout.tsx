import './globals.css';
import type { Metadata } from 'next';
import { Suspense } from 'react';
import Script from 'next/script';
import { Header } from '@/components/Header';
import { Footer } from '@/components/Footer';
import { CompareProvider } from '@/components/CompareContext';
import { CookieConsent } from '@/components/CookieConsent';
import { AnalyticsPageview } from '@/components/AnalyticsPageview';
import { JsonLd } from '@/components/JsonLd';
import {
  DEFAULT_OG_IMAGE, OG_LOCALE, PUBLISHER, SITE_DESCRIPTION, SITE_NAME,
  SITE_TAGLINE, SITE_URL, absolute, organizationLd, websiteLd,
} from '@/lib/seo';

const GA_ID = 'G-SYFKP9HY66';

export const metadata: Metadata = {
  // Makes every relative canonical/OG URL in child routes resolve absolutely.
  metadataBase: new URL(SITE_URL),
  title: {
    default: `${SITE_NAME} — ${SITE_TAGLINE}`,
    // Child pages set a bare title; the brand suffix is appended here.
    template: `%s · ${SITE_NAME}`,
  },
  description: SITE_DESCRIPTION,
  applicationName: SITE_NAME,
  authors: [{ name: PUBLISHER.name, url: PUBLISHER.url }],
  creator: PUBLISHER.name,
  publisher: PUBLISHER.brand,
  category: 'technology',
  // No canonical here on purpose: a layout-level canonical is inherited by every
  // page that doesn't set its own, which would point them all at "/". Each route
  // declares its own canonical via pageMetadata().
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      'max-snippet': -1,
      'max-image-preview': 'large',
      'max-video-preview': -1,
    },
  },
  openGraph: {
    type: 'website',
    url: SITE_URL,
    siteName: SITE_NAME,
    locale: OG_LOCALE,
    title: `${SITE_NAME} — ${SITE_TAGLINE}`,
    description: SITE_DESCRIPTION,
    images: [{ url: absolute(DEFAULT_OG_IMAGE), width: 1200, height: 630, alt: SITE_NAME }],
  },
  twitter: {
    card: 'summary_large_image',
    title: `${SITE_NAME} — ${SITE_TAGLINE}`,
    description: SITE_DESCRIPTION,
    images: [absolute(DEFAULT_OG_IMAGE)],
  },
  formatDetection: { telephone: false, address: false, email: false },
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
        {/* Site-wide entity graph — referenced by @id from every page-level graph. */}
        <JsonLd data={[organizationLd(), websiteLd()]} />
      </head>
      <body suppressHydrationWarning>
        <Script
          src={`https://www.googletagmanager.com/gtag/js?id=${GA_ID}`}
          strategy="afterInteractive"
        />
        <Script id="ga4-init" strategy="afterInteractive">
          {`window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
// Consent Mode v2 — default to denied (EU-safe) BEFORE any measurement.
gtag('consent', 'default', {
  ad_storage: 'denied',
  ad_user_data: 'denied',
  ad_personalization: 'denied',
  analytics_storage: 'denied',
  wait_for_update: 500
});
// Re-apply a previously stored opt-in before the first hit.
try {
  if (localStorage.getItem('ki-consent') === 'granted') {
    gtag('consent', 'update', {
      ad_storage: 'granted', ad_user_data: 'granted',
      ad_personalization: 'granted', analytics_storage: 'granted'
    });
  }
} catch (e) {}
gtag('js', new Date());
gtag('set', 'url_passthrough', true);
// send_page_view:false — page_views are sent by <AnalyticsPageview> on every
// route change (initial + client-side), so SPA navigation is measured too.
gtag('config', '${GA_ID}', { send_page_view: false });`}
        </Script>
        <Suspense fallback={null}>
          <AnalyticsPageview />
        </Suspense>
        <CompareProvider>
          <Header />
          <main className="page-content">{children}</main>
          <Footer />
          <CookieConsent />
        </CompareProvider>
      </body>
    </html>
  );
}
