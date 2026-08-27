/** Central SEO constants, metadata builders and JSON-LD factories.
 *  Server-safe — no client-only APIs, importable from any Server Component. */
import type { Metadata } from 'next';
import type { Article, Category, Post, Tool } from './types';

export const SITE_URL = (process.env.NEXT_PUBLIC_SITE_URL ?? 'https://ki-toolnavigator.com').replace(/\/+$/, '');
export const SITE_NAME = 'KI-Toolnavigator';
export const SITE_TAGLINE = 'Das kuratierte Verzeichnis für Künstliche Intelligenz';
export const SITE_DESCRIPTION =
  'KI-Tools, geprüft, verglichen und erklärt — auf Deutsch, nach DSGVO-Kriterien sortierbar. '
  + 'Redaktionelle Steckbriefe zu Preisen, Funktionen und Datenschutz.';
export const OG_LOCALE = 'de_DE';
/** All content is produced by one editorial team; there are no individual bylines. */
export const EDITORIAL_BYLINE = `${SITE_NAME} Redaktion`;
export const DEFAULT_OG_IMAGE = '/og-default.png';

export const PUBLISHER = {
  name: 'Dr. Andreas Stöckl',
  brand: 'ampunkt.technology',
  url: 'https://ampunkt.technology',
};

/** Absolute URL for a site-relative path; passes through URLs that are already absolute. */
export function absolute(path?: string | null): string {
  // "/" resolves to the bare origin — that is the form Next emits for the root
  // canonical, and sitemap/breadcrumb entries must match it exactly.
  if (!path || path === '/') return SITE_URL;
  if (/^https?:\/\//i.test(path)) return path;
  return `${SITE_URL}${path.startsWith('/') ? path : `/${path}`}`;
}

/** Strip Markdown/HTML noise and cut on a word boundary — for meta descriptions. */
export function summarize(input?: string | null, max = 158): string {
  if (!input) return '';
  const text = input
    .replace(/```[\s\S]*?```/g, ' ')
    .replace(/<[^>]+>/g, ' ')
    .replace(/!\[[^\]]*\]\([^)]*\)/g, ' ')
    .replace(/\[([^\]]+)\]\([^)]*\)/g, '$1')
    .replace(/^[#>\s-]+/gm, ' ')
    .replace(/[*_`~]/g, '')
    .replace(/\s+/g, ' ')
    .trim();
  if (text.length <= max) return text;
  const cut = text.slice(0, max - 1);
  const lastSpace = cut.lastIndexOf(' ');
  return `${(lastSpace > max * 0.6 ? cut.slice(0, lastSpace) : cut).replace(/[,;:.\-–—\s]+$/, '')}…`;
}

/** The CMS returns `keywords` as an array on some records and a comma-separated
 *  string on others — normalise both into a clean string[]. */
export function keywordList(v: unknown): string[] {
  if (Array.isArray(v)) return v.map((k) => String(k).trim()).filter(Boolean);
  if (typeof v === 'string') return v.split(',').map((k) => k.trim()).filter(Boolean);
  return [];
}

type PageMetaInput = {
  title: string;
  description: string;
  /** Site-relative path, e.g. `/tool/claude`. Used for the canonical + og:url. */
  path: string;
  /** Absolute or site-relative image URL. Falls back to the default OG card. */
  image?: string | null;
  imageAlt?: string;
  type?: 'website' | 'article';
  keywords?: string[] | null;
  noindex?: boolean;
  /** ISO date — only meaningful for `type: 'article'`. */
  publishedTime?: string;
  modifiedTime?: string;
  authors?: string[];
};

/** Build a complete Metadata object: canonical + OpenGraph + Twitter in one place. */
export function pageMetadata(input: PageMetaInput): Metadata {
  const { title, description, path, image, imageAlt, type = 'website', keywords, noindex } = input;
  const url = absolute(path);
  const usingDefault = !image;
  const ogImage = absolute(image || DEFAULT_OG_IMAGE);
  // Only the generated default card has known dimensions — declaring 1200×630
  // for a CMS asset of a different size makes previews crop badly.
  const ogImageEntry = usingDefault
    ? { url: ogImage, width: 1200, height: 630, alt: imageAlt ?? title }
    : { url: ogImage, alt: imageAlt ?? title };

  return {
    title,
    description,
    ...(keywords && keywords.length ? { keywords } : {}),
    alternates: { canonical: url },
    ...(noindex ? { robots: { index: false, follow: true } } : {}),
    openGraph: {
      type,
      url,
      siteName: SITE_NAME,
      locale: OG_LOCALE,
      title,
      description,
      images: [ogImageEntry],
      ...(type === 'article'
        ? {
            publishedTime: input.publishedTime,
            modifiedTime: input.modifiedTime,
            authors: input.authors,
          }
        : {}),
    },
    twitter: {
      card: 'summary_large_image',
      title,
      description,
      images: [ogImage],
    },
  };
}

// ---------------------------------------------------------------------------
// JSON-LD factories. Each returns a plain object for <JsonLd data={…} />.
// Deliberately omitted: aggregateRating. The `rating`/`reviews` fields are
// editorial estimates, not user reviews collected by this site — emitting them
// as AggregateRating would violate Google's review-snippet policy.
// ---------------------------------------------------------------------------

const publisherLd = () => ({
  '@type': 'Organization',
  '@id': `${SITE_URL}/#organization`,
  name: SITE_NAME,
  url: SITE_URL,
  logo: { '@type': 'ImageObject', url: absolute('/icon.svg') },
  founder: { '@type': 'Person', name: PUBLISHER.name },
  sameAs: [PUBLISHER.url],
});

export function organizationLd() {
  return { '@context': 'https://schema.org', ...publisherLd() };
}

export function websiteLd() {
  return {
    '@context': 'https://schema.org',
    '@type': 'WebSite',
    '@id': `${SITE_URL}/#website`,
    url: SITE_URL,
    name: SITE_NAME,
    description: SITE_DESCRIPTION,
    inLanguage: 'de',
    publisher: { '@id': `${SITE_URL}/#organization` },
    potentialAction: {
      '@type': 'SearchAction',
      target: { '@type': 'EntryPoint', urlTemplate: `${SITE_URL}/suche?q={search_term_string}` },
      'query-input': 'required name=search_term_string',
    },
  };
}

/** True for the house byline (or a missing one) as opposed to a named guest author. */
export function isEditorial(author?: string | null): boolean {
  return /^\s*(redaktion)?\s*$/i.test(author ?? '');
}

export type Crumb = { name: string; path?: string };

export function breadcrumbLd(items: Crumb[]) {
  return {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: items.map((c, i) => ({
      '@type': 'ListItem',
      position: i + 1,
      name: c.name,
      ...(c.path ? { item: absolute(c.path) } : {}),
    })),
  };
}

/** True only when the tool is free outright. The CMS stores pricing as prose
 *  ("Free · Premium ab $20 / Mon."), so anything mentioning a figure, a monthly
 *  tier or an enterprise plan is not claimed as free — and no numeric Offer is
 *  emitted at all, because a parsed-from-prose price would frequently be wrong. */
function fullyFree(price?: string): boolean {
  if (!price) return false;
  if (/\d/.test(price)) return false;
  if (/\bab\b|\bfrom\b|premium|pro\b|plus\b|enterprise|tarif|plän|plan|credits|pay-per|anfrage|abo/i.test(price)) return false;
  return /^\s*(kostenlos|gratis|free|open source)/i.test(price);
}

export function softwareApplicationLd(t: Tool, opts: { categoryName?: string; image?: string | null; description: string }) {
  const url = absolute(`/tool/${t.slug}`);
  return {
    '@context': 'https://schema.org',
    '@type': 'SoftwareApplication',
    '@id': `${url}#software`,
    name: t.name,
    url,
    description: opts.description,
    applicationCategory: opts.categoryName ?? 'BusinessApplication',
    operatingSystem: 'Web',
    inLanguage: 'de',
    ...(opts.image ? { image: absolute(opts.image) } : {}),
    ...(t.website ? { sameAs: [t.website], installUrl: t.website } : {}),
    ...(t.launched ? { datePublished: t.launched } : {}),
    ...(t._updated_at || t.lastUpdated ? { dateModified: (t._updated_at ?? t.lastUpdated).slice(0, 10) } : {}),
    author: { '@type': 'Organization', name: t.vendor },
    publisher: { '@type': 'Organization', name: t.vendor },
    ...(t.usecases?.length ? { featureList: t.usecases } : {}),
    ...(fullyFree(t.price) ? { isAccessibleForFree: true } : {}),
  };
}

/** The editorial verdict as a first-party Review — legitimate, unlike a faked aggregate. */
export function reviewLd(t: Tool, opts: { description: string; pros?: string[]; cons?: string[] }) {
  const url = absolute(`/tool/${t.slug}`);
  return {
    '@context': 'https://schema.org',
    '@type': 'Review',
    '@id': `${url}#review`,
    itemReviewed: { '@id': `${url}#software`, '@type': 'SoftwareApplication', name: t.name },
    url,
    reviewBody: opts.description,
    ...(opts.pros?.length ? { positiveNotes: { '@type': 'ItemList', itemListElement: opts.pros.map((p, i) => ({ '@type': 'ListItem', position: i + 1, name: p })) } } : {}),
    ...(opts.cons?.length ? { negativeNotes: { '@type': 'ItemList', itemListElement: opts.cons.map((c, i) => ({ '@type': 'ListItem', position: i + 1, name: c })) } } : {}),
    author: { '@id': `${SITE_URL}/#organization` },
    publisher: { '@id': `${SITE_URL}/#organization` },
    ...(t._updated_at || t.lastUpdated ? { datePublished: (t._updated_at ?? t.lastUpdated).slice(0, 10) } : {}),
  };
}

export function articleLd(a: Article, opts: { description: string; image?: string | null; post?: Post | null; wordCount?: number }) {
  const url = absolute(`/artikel/${a.slug}`);
  return {
    '@context': 'https://schema.org',
    '@type': 'Article',
    '@id': `${url}#article`,
    headline: a.title,
    description: opts.description,
    url,
    mainEntityOfPage: { '@type': 'WebPage', '@id': url },
    inLanguage: 'de',
    ...(opts.image ? { image: [absolute(opts.image)] } : {}),
    ...(a.date ? { datePublished: new Date(a.date).toISOString() } : {}),
    dateModified: new Date(a._updated_at ?? a.date).toISOString(),
    // The editorial team is the publication itself, so reference the Organization
    // (which carries a url and sameAs). A genuine named guest author would still
    // get a Person — but without an author page on the site, so no url.
    author: isEditorial(a.author)
      ? { '@id': `${SITE_URL}/#organization` }
      : { '@type': 'Person', name: a.author },
    publisher: { '@id': `${SITE_URL}/#organization` },
    ...(a.category ? { articleSection: a.category } : {}),
    ...(opts.wordCount ? { wordCount: opts.wordCount } : {}),
    ...(keywordList(opts.post?.keywords).length
      ? { keywords: keywordList(opts.post?.keywords).join(', ') }
      : {}),
  };
}

export function collectionPageLd(cat: Category, tools: Tool[], opts: { description: string }) {
  const url = absolute(`/kategorie/${cat.slug}`);
  return {
    '@context': 'https://schema.org',
    '@type': 'CollectionPage',
    '@id': `${url}#collection`,
    name: cat.name,
    description: opts.description,
    url,
    inLanguage: 'de',
    isPartOf: { '@id': `${SITE_URL}/#website` },
    mainEntity: {
      '@type': 'ItemList',
      numberOfItems: tools.length,
      itemListElement: tools.map((t, i) => ({
        '@type': 'ListItem',
        position: i + 1,
        url: absolute(`/tool/${t.slug}`),
        name: t.name,
      })),
    },
  };
}

export function itemListLd(items: { name: string; path: string }[], name: string) {
  return {
    '@context': 'https://schema.org',
    '@type': 'ItemList',
    name,
    numberOfItems: items.length,
    itemListElement: items.map((it, i) => ({
      '@type': 'ListItem',
      position: i + 1,
      name: it.name,
      url: absolute(it.path),
    })),
  };
}
