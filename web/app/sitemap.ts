import type { MetadataRoute } from 'next';
import { getAll } from '@/lib/cms';
import { SITE_URL } from '@/lib/seo';

/** Rebuilt hourly so new CMS entries show up without a redeploy. */
export const revalidate = 3600;

const iso = (v?: string | null) => {
  if (!v) return undefined;
  const d = new Date(v);
  return Number.isNaN(d.getTime()) ? undefined : d;
};

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const { tools, articles, categories } = await getAll();

  const newest = (dates: (string | undefined)[]) => {
    const parsed = dates.map(iso).filter(Boolean) as Date[];
    return parsed.length ? new Date(Math.max(...parsed.map((d) => d.getTime()))) : new Date();
  };

  const allTouched = newest([
    ...tools.map((t) => t._updated_at ?? t.lastUpdated),
    ...articles.map((a) => a._updated_at ?? a.date),
  ]);

  const staticPages: MetadataRoute.Sitemap = [
    { url: SITE_URL,                   lastModified: allTouched, changeFrequency: 'daily',   priority: 1.0 },
    { url: `${SITE_URL}/verzeichnis`,  lastModified: allTouched, changeFrequency: 'daily',   priority: 0.9 },
    { url: `${SITE_URL}/vergleich`,    lastModified: allTouched, changeFrequency: 'weekly',  priority: 0.8 },
    { url: `${SITE_URL}/artikel`,      lastModified: allTouched, changeFrequency: 'weekly',  priority: 0.7 },
    { url: `${SITE_URL}/aenderungen`,  lastModified: allTouched, changeFrequency: 'daily',   priority: 0.4 },
    { url: `${SITE_URL}/impressum`,    lastModified: allTouched, changeFrequency: 'yearly',  priority: 0.2 },
  ];

  const categoryPages: MetadataRoute.Sitemap = categories.map((c) => ({
    url: `${SITE_URL}/kategorie/${c.slug}`,
    lastModified: newest(
      tools.filter((t) => t.category === c.slug).map((t) => t._updated_at ?? t.lastUpdated),
    ),
    changeFrequency: 'weekly',
    priority: 0.8,
  }));

  const toolPages: MetadataRoute.Sitemap = tools.map((t) => ({
    url: `${SITE_URL}/tool/${t.slug}`,
    lastModified: iso(t._updated_at ?? t.lastUpdated) ?? new Date(),
    changeFrequency: 'weekly',
    priority: 0.7,
  }));

  const articlePages: MetadataRoute.Sitemap = articles.map((a) => ({
    url: `${SITE_URL}/artikel/${a.slug}`,
    lastModified: iso(a._updated_at ?? a.date) ?? new Date(),
    changeFrequency: 'monthly',
    priority: 0.6,
  }));

  return [...staticPages, ...categoryPages, ...toolPages, ...articlePages];
}
