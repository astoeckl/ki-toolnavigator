'use client';
import { Button } from '@/components/ui';
import { useCompare } from '@/components/CompareContext';

export function CategoryToolActions({ slug }: { slug: string }) {
  const { has, toggle } = useCompare();
  return (
    <div style={{ display: 'flex', gap: 8, marginTop: 'auto' }}>
      <Button variant="ghost" href={`/tool/${slug}`}>Details →</Button>
      <Button variant="ghost" onClick={() => toggle(slug)}>
        {has(slug) ? '✓ im Korb' : '+ vergleichen'}
      </Button>
    </div>
  );
}
