import type { Article, Category, CmsElement, Media, Post, SearchHit, Tool } from './types';

const BASE = process.env.COGNITOR_BASE_URL ?? 'https://backend.cognitor.dev';
const SITE = process.env.COGNITOR_SITE ?? 'ki-toolnavigator-site';
const EMAIL = process.env.COGNITOR_EMAIL;
const PASSWORD = process.env.COGNITOR_PASSWORD;

// Public Cognitor read endpoint requires the site-prefixed identifier
const typeId = (key: string) => `${SITE}_${key}`;

async function fetchType<T>(key: string, revalidate = 60): Promise<(T & { _updated_at?: string; _id?: number })[]> {
  const url = `${BASE}/public/${SITE}/elements/?type=${typeId(key)}&limit=500`;
  const res = await fetch(url, { next: { revalidate, tags: [`cms:${key}`] } });
  if (!res.ok) throw new Error(`CMS fetch failed for "${key}": ${res.status} ${res.statusText}`);
  const items = (await res.json()) as CmsElement<T>[];
  // Inject CMS metadata so consumers can use it for "last changed" UI
  // without re-fetching or losing data when the editor doesn't manually update fields.
  return items.map((el) => ({ ...el.data, _updated_at: el.updated_at, _id: el.id }));
}

// ---- Auth (server-only) — token cached in module scope ----
let cachedToken: { value: string; expires: number } | null = null;

async function getToken(): Promise<string> {
  // 50-min cache; tokens are short-lived but we re-login eagerly
  if (cachedToken && cachedToken.expires > Date.now() + 5 * 60_000) return cachedToken.value;
  if (!EMAIL || !PASSWORD) throw new Error('COGNITOR_EMAIL/COGNITOR_PASSWORD not set in env');
  const body = new URLSearchParams({ grant_type: 'password', username: EMAIL, password: PASSWORD });
  const res = await fetch(`${BASE}/auth/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body,
    cache: 'no-store',
  });
  if (!res.ok) throw new Error(`Cognitor login failed: ${res.status}`);
  const data = await res.json();
  cachedToken = { value: data.access_token, expires: Date.now() + 50 * 60_000 };
  return cachedToken.value;
}

// ---- Search (Cognitor full-text search, no auth required) ----
export type SearchResponse = { results: SearchHit[]; total?: number; page?: number; size?: number };

export async function searchCms(q: string, opts: { size?: number; page?: number } = {}): Promise<SearchResponse> {
  if (!q.trim()) return { results: [], total: 0 };
  const params = new URLSearchParams({
    q,
    size: String(opts.size ?? 20),
    page: String(opts.page ?? 1),
    highlight: 'true',
    published_only: 'true',
    locale: 'de',
  });
  const url = `${BASE}/search/sites/${SITE}?${params}`;
  const res = await fetch(url, { next: { revalidate: 30 } });
  if (!res.ok) throw new Error(`Search failed: ${res.status}`);
  const data = await res.json();
  return Array.isArray(data) ? { results: data } : data;
}

export async function suggestCms(q: string, size = 8): Promise<string[]> {
  if (!q.trim()) return [];
  const params = new URLSearchParams({ q, size: String(size), locale: 'de' });
  const res = await fetch(`${BASE}/search/sites/${SITE}/suggest?${params}`, { cache: 'no-store' });
  if (!res.ok) return [];
  const data = await res.json();
  return Array.isArray(data) ? data : (data.suggestions ?? []);
}

/** Public media metadata — does not require auth. */
export async function getMedia(id: number, revalidate = 300): Promise<Media | null> {
  const res = await fetch(`${BASE}/public/${SITE}/media/${id}`, {
    next: { revalidate, tags: [`cms:media:${id}`] },
  });
  if (res.status === 404) return null;
  if (!res.ok) return null;
  return (await res.json()) as Media;
}

/** Build the public view URL for a media id (a plain image link, no auth). */
export function mediaUrl(id: number): string {
  return `${BASE}/public/${SITE}/media/${id}/view`;
}

export async function getPost(id: number, revalidate = 60): Promise<Post | null> {
  const token = await getToken();
  const res = await fetch(`${BASE}/${SITE}/posts/${id}`, {
    headers: { Authorization: `Bearer ${token}` },
    next: { revalidate, tags: [`cms:post:${id}`] },
  });
  if (res.status === 404) return null;
  if (!res.ok) throw new Error(`Post fetch failed for id=${id}: ${res.status}`);
  return (await res.json()) as Post;
}

export async function getCategories(): Promise<Category[]> {
  const cats = await fetchType<Category>('category');
  return cats.sort((a, b) => (a.order ?? 999) - (b.order ?? 999));
}

export async function getTools(): Promise<Tool[]> {
  return fetchType<Tool>('tool');
}

export async function getArticles(): Promise<Article[]> {
  return fetchType<Article>('article');
}

export async function getAll() {
  const [categories, tools, articles] = await Promise.all([
    getCategories(),
    getTools(),
    getArticles(),
  ]);
  return { categories, tools, articles };
}

export async function getTool(slug: string): Promise<Tool | undefined> {
  const tools = await getTools();
  return tools.find((t) => t.slug === slug);
}

export async function getCategory(slug: string): Promise<Category | undefined> {
  const cats = await getCategories();
  return cats.find((c) => c.slug === slug);
}

export async function getArticle(slug: string): Promise<Article | undefined> {
  const articles = await getArticles();
  return articles.find((a) => a.slug === slug);
}
