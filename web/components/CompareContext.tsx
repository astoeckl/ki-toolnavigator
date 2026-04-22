'use client';
import { createContext, useCallback, useContext, useEffect, useState, type ReactNode } from 'react';

type Ctx = {
  compareList: string[];
  toggle: (slug: string) => void;
  has: (slug: string) => boolean;
  remove: (slug: string) => void;
  clear: () => void;
};

const CompareContext = createContext<Ctx | null>(null);
const STORAGE_KEY = 'ki_compare';
const MAX = 4;
const DEFAULTS = ['chatgpt', 'claude', 'mistral'];

export function CompareProvider({ children }: { children: ReactNode }) {
  const [compareList, setCompareList] = useState<string[]>(DEFAULTS);

  useEffect(() => {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      if (raw) setCompareList(JSON.parse(raw));
    } catch {}
  }, []);

  useEffect(() => {
    try { localStorage.setItem(STORAGE_KEY, JSON.stringify(compareList)); } catch {}
  }, [compareList]);

  const toggle = useCallback((slug: string) => {
    setCompareList((prev) => {
      if (prev.includes(slug)) return prev.filter((s) => s !== slug);
      if (prev.length >= MAX) return prev;
      return [...prev, slug];
    });
  }, []);

  const has = useCallback((slug: string) => compareList.includes(slug), [compareList]);
  const remove = useCallback((slug: string) => setCompareList((p) => p.filter((s) => s !== slug)), []);
  const clear = useCallback(() => setCompareList([]), []);

  return (
    <CompareContext.Provider value={{ compareList, toggle, has, remove, clear }}>
      {children}
    </CompareContext.Provider>
  );
}

export function useCompare(): Ctx {
  const ctx = useContext(CompareContext);
  if (!ctx) throw new Error('useCompare must be used inside CompareProvider');
  return ctx;
}
