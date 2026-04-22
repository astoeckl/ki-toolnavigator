'use client';
import { useRouter } from 'next/navigation';
import { Chip } from '@/components/ui';
import { SearchBar } from '@/components/SearchBar';

export function HeroSearch() {
  const router = useRouter();
  return (
    <>
      <div style={{ marginTop: 36 }}>
        <SearchBar variant="hero" />
      </div>
      <div style={{ display: 'flex', gap: 14, marginTop: 20, flexWrap: 'wrap' }}>
        <span style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#8a8580', textTransform: 'uppercase', letterSpacing: '0.06em', paddingTop: 4 }}>Populär:</span>
        {['ChatGPT', 'Claude', 'Midjourney', 'DSGVO', 'Coding-Assistent'].map((t) => (
          <Chip key={t} onClick={() => router.push(`/suche?q=${encodeURIComponent(t)}`)}>{t}</Chip>
        ))}
      </div>
    </>
  );
}
