import { getCategories, getTools } from '@/lib/cms';
import { getEditorialDates } from '@/lib/site';
import { Breadcrumb } from '@/components/ui';
import { CompareTable } from './CompareTable';

export const metadata = { title: 'Vergleich · KI-Toolnavigator' };

export default async function ComparePage() {
  const [tools, categories, editorial] = await Promise.all([
    getTools(),
    getCategories(),
    getEditorialDates(),
  ]);
  return (
    <div>
      <Breadcrumb items={[
        { label: 'Start', href: '/' },
        { label: 'Verzeichnis', href: '/verzeichnis' },
        { label: 'Vergleich' },
      ]} />
      <CompareTable tools={tools} categories={categories} editorialDate={editorial.short} />
    </div>
  );
}
