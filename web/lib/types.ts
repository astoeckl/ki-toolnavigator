/** Metadata injected by lib/cms.ts on every fetched entity. */
export type CmsMeta = {
  /** ISO timestamp when the underlying CMS element was last modified. */
  _updated_at?: string;
  /** Internal CMS element id. */
  _id?: number;
};

export type Category = {
  slug: string;
  name: string;
  count: number;
  desc: string;
  order?: number;
} & CmsMeta;

export type DsgvoStatus = 'ja' | 'bedingt' | 'nein';

export type Tool = {
  slug: string;
  name: string;
  vendor: string;
  category: string;
  tagline: string;
  price: string;
  api: boolean;
  dsgvo: DsgvoStatus;
  origin: string;
  rating: number;
  reviews: number;
  pros: string[];
  cons: string[];
  usecases: string[];
  launched: string;
  lastUpdated: string;
  /** The CMS public endpoint resolves the `post_id` reference and inlines the
   *  full Post object here. With auth, this would be just a number. */
  post_id?: Post | number;
  /** Cover image reference (resolved to URL string by the public endpoint). */
  media_id?: string | Media | number;
  /** Real website screenshot of the tool (resolved to URL string). */
  screenshot_id?: string | Media | number;
  /** Official logo of the tool (resolved to URL string). */
  logo_id?: string | Media | number;
  /** Markdown: key features of the tool. */
  features?: string;
  /** Markdown: pricing tiers. */
  pricing?: string;
  /** Official website / product URL. */
  website?: string;
} & CmsMeta;

export type Media = {
  id?: number;
  filename?: string;
  name?: string;
  url?: string;
  file_size?: number;
  media_type?: string;
  description?: string;
  keywords?: string;
  alt_text?: string;
  status?: string;
};

export type Post = {
  /** Present when the field is fetched standalone (auth API). The resolved object on
   *  the public elements endpoint may omit the id. */
  id?: number;
  title: string;
  content: string;
  short_description?: string | null;
  keywords?: string[] | null;
  published?: boolean;
  locale?: string;
  author_id?: number | null;
  site_id?: number;
  created_at?: string;
};

export type Article = {
  slug: string;
  title: string;
  category: string;
  author: string;
  date: string;
  readTime: number;
  toc: string[];
  /** The CMS public endpoint resolves the `post_id` reference and inlines the
   *  full Post object here. With auth, this would be just a number. */
  post_id?: Post | number;
  /** Cover image reference.
   *  - Public endpoint resolves it to the asset URL (string).
   *  - Auth endpoint may return the integer id, or an inlined Media object. */
  media_id?: string | Media | number;
} & CmsMeta;

export type CmsElement<T> = {
  id: number;
  type_identifier: string;
  data: T;
  updated_at: string;
  tags?: string[];
};

/** Result row from Cognitor's `/search/sites/{site}` endpoint. */
export type SearchHit = {
  id: number;
  doc_type: 'content_element' | 'post' | 'media' | string;
  title: string;
  content: string;
  description?: string;
  keywords?: string;
  score: number;
  highlight?: Record<string, string[]>;
  /** Identifier of the parent content type for content_element hits — e.g. "tool", "article", "category". */
  content_type_identifier?: string | null;
  filename?: string | null;
  media_type?: string | null;
  url?: string | null;
  is_reference_match?: boolean;
};
