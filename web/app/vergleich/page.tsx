import type { Metadata } from 'next';
import { getCategories, getTools } from '@/lib/cms';
import { getEditorialDates } from '@/lib/site';
import { Breadcrumb } from '@/components/ui';
import { JsonLd } from '@/components/JsonLd';
import { breadcrumbLd, pageMetadata } from '@/lib/seo';
import { CompareTable } from './CompareTable';

export async function generateMetadata(): Promise<Metadata> {
  const tools = await getTools();
  return pageMetadata({
    title: 'KI-Tools vergleichen — Preis, API & DSGVO nebeneinander',
    description:
      `Direktvergleich von ${tools.length} KI-Tools: Preismodell, API-Verfügbarkeit, Herkunft und `
      + 'DSGVO-Einschätzung in einer Tabelle.',
    path: '/vergleich',
    keywords: ['KI-Tools Vergleich', 'KI Vergleichstabelle', 'DSGVO KI-Tools', 'KI-Tools Preise'],
  });
}

export default async function ComparePage() {
  const [tools, categories, editorial] = await Promise.all([
    getTools(),
    getCategories(),
    getEditorialDates(),
  ]);
  return (
    <div>
      <JsonLd data={breadcrumbLd([
        { name: 'Start', path: '/' },
        { name: 'Verzeichnis', path: '/verzeichnis' },
        { name: 'Vergleich', path: '/vergleich' },
      ])} />

      <Breadcrumb items={[
        { label: 'Start', href: '/' },
        { label: 'Verzeichnis', href: '/verzeichnis' },
        { label: 'Vergleich' },
      ]} />
      <CompareTable tools={tools} categories={categories} editorialDate={editorial.short} />
    </div>
  );
}
