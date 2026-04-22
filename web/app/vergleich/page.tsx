import { getCategories, getTools } from '@/lib/cms';
import { Breadcrumb } from '@/components/ui';
import { CompareTable } from './CompareTable';

export const metadata = { title: 'Vergleich · KI-Toolnavigator' };

export default async function ComparePage() {
  const [tools, categories] = await Promise.all([getTools(), getCategories()]);
  return (
    <div>
      <Breadcrumb items={[
        { label: 'Start', href: '/' },
        { label: 'Verzeichnis', href: '/verzeichnis' },
        { label: 'Vergleich' },
      ]} />
      <CompareTable tools={tools} categories={categories} />
    </div>
  );
}
