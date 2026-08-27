import type { Metadata } from 'next';
import { getCategories, getTools } from '@/lib/cms';
import { Breadcrumb } from '@/components/ui';
import { JsonLd } from '@/components/JsonLd';
import { breadcrumbLd, itemListLd, pageMetadata } from '@/lib/seo';
import { DirectoryClient } from './DirectoryClient';

export async function generateMetadata(): Promise<Metadata> {
  const tools = await getTools();
  return pageMetadata({
    title: `Alle KI-Tools im Verzeichnis (${tools.length} geprüfte Einträge)`,
    description:
      `Das vollständige Verzeichnis: ${tools.length} KI-Tools, redaktionell geprüft und nach Kategorie, `
      + 'Preis und DSGVO-Konformität filterbar.',
    // Canonical points at the bare path — ?q= and ?cat= are filter views of the
    // same list and must not be indexed as separate URLs.
    path: '/verzeichnis',
    keywords: ['KI-Tools Verzeichnis', 'KI-Tools Liste', 'KI-Tools Deutsch', 'DSGVO KI-Tools'],
  });
}

export default async function DirectoryPage({
  searchParams,
}: {
  searchParams: Promise<{ q?: string; cat?: string }>;
}) {
  const params = await searchParams;
  const [tools, categories] = await Promise.all([getTools(), getCategories()]);
  return (
    <div>
      <JsonLd data={[
        itemListLd(tools.map((t) => ({ name: t.name, path: `/tool/${t.slug}` })), 'KI-Tool-Verzeichnis'),
        breadcrumbLd([{ name: 'Start', path: '/' }, { name: 'Verzeichnis', path: '/verzeichnis' }]),
      ]} />

      <Breadcrumb items={[{ label: 'Start', href: '/' }, { label: 'Verzeichnis' }]} />
      <DirectoryClient
        tools={tools}
        categories={categories}
        initialSearch={params.q ?? ''}
        initialCategory={params.cat ?? 'all'}
      />
    </div>
  );
}
