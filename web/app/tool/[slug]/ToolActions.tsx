'use client';
import { Button } from '@/components/ui';
import { useCompare } from '@/components/CompareContext';

type Props = { slug: string; website?: string };

export function ToolActions({ slug, website }: Props) {
  const { has, toggle } = useCompare();
  return (
    <div className="tool-hero-actions" style={{ marginTop: 24, display: 'flex', gap: 10, flexWrap: 'wrap' }}>
      {website && (
        <Button variant="primary" onClick={() => window.open(website, '_blank', 'noopener,noreferrer')}>
          Website besuchen ↗
        </Button>
      )}
      <Button variant="ghost" onClick={() => toggle(slug)}>
        {has(slug) ? '✓ im Vergleichskorb' : '+ Zum Vergleich hinzufügen'}
      </Button>
    </div>
  );
}
