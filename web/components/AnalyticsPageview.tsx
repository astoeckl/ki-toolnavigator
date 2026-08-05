'use client';

import { usePathname, useSearchParams } from 'next/navigation';
import { useEffect } from 'react';

/** Sends a GA4 page_view on every App-Router route change (initial load + each
 *  client-side navigation). The root config sets send_page_view:false so this is
 *  the single source of page_views — no double counting of the entry page.
 *  Consent Mode still applies: a page_view sent while consent is denied is a
 *  cookieless ping; once granted, hits carry the analytics cookie. */
export function AnalyticsPageview() {
  const pathname = usePathname();
  const searchParams = useSearchParams();

  useEffect(() => {
    const gtag = (window as unknown as { gtag?: (...a: unknown[]) => void }).gtag;
    if (typeof gtag !== 'function') return;
    gtag('event', 'page_view', {
      page_location: window.location.href,
      page_title: document.title,
    });
    // pathname/searchParams drive re-fires on navigation
  }, [pathname, searchParams]);

  return null;
}
