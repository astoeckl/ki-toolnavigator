import { marked } from 'marked';

marked.setOptions({
  gfm: true,
  breaks: false,
});

/** Stable, deterministic slug for a heading text — must match toSlug() used by the TOC. */
export function toSlug(text: string): string {
  return text
    .toLowerCase()
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')        // strip diacritics
    .replace(/ä/g, 'ae').replace(/ö/g, 'oe').replace(/ü/g, 'ue').replace(/ß/g, 'ss')
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '');
}

/** Custom renderer: inject id attributes on h2/h3 so the TOC can anchor-link to them. */
const renderer = new marked.Renderer();
const baseHeading = renderer.heading.bind(renderer);
renderer.heading = function ({ tokens, depth, ...rest }: any) {
  const text = this.parser.parseInline(tokens);
  const raw = tokens.map((t: any) => ('text' in t ? t.text : '')).join('');
  const id = toSlug(raw);
  return `<h${depth} id="${id}">${text}</h${depth}>\n`;
};

/** Render a Markdown string to HTML — server-side only. */
export function renderMarkdown(md: string): string {
  return marked.parse(md, { async: false, renderer }) as string;
}
