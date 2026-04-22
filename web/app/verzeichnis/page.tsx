import { getCategories, getTools } from '@/lib/cms';
import { Breadcrumb } from '@/components/ui';
import { DirectoryClient } from './DirectoryClient';

export const metadata = { title: 'Verzeichnis · KI-Toolnavigator' };

export default async function DirectoryPage({
  searchParams,
}: {
  searchParams: Promise<{ q?: string; cat?: string }>;
}) {
  const params = await searchParams;
  const [tools, categories] = await Promise.all([getTools(), getCategories()]);
  return (
    <div>
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
