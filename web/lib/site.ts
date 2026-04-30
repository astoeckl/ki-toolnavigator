/** Editorial-stand date resolved from the latest tool change.
 *  Server-only — relies on getTools() which uses Next.js fetch ISR (60s revalidate). */
import { getTools } from './cms';

const MONTHS_DE = [
  'Januar', 'Februar', 'März', 'April', 'Mai', 'Juni',
  'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember',
];

export type EditorialDates = { label: string; short: string; iso: string };

function format(d: Date): EditorialDates {
  const day = d.getUTCDate();
  const mon = d.getUTCMonth();
  const year = d.getUTCFullYear();
  const dd = String(day).padStart(2, '0');
  const mm = String(mon + 1).padStart(2, '0');
  return {
    label: `${day}. ${MONTHS_DE[mon]} ${year}`,
    short: `${dd}.${mm}.${year}`,
    iso: d.toISOString().slice(0, 10),
  };
}

/** Returns the most recent `lastUpdated` across all tools (or all tools in `category`). */
export async function getEditorialDates(category?: string): Promise<EditorialDates> {
  const tools = await getTools();
  const pool = category ? tools.filter((t) => t.category === category) : tools;
  let latest: Date | null = null;
  for (const t of pool) {
    const raw = (t as unknown as { lastUpdated?: string }).lastUpdated
      ?? (t as unknown as { _updated_at?: string })._updated_at;
    if (!raw) continue;
    const d = new Date(raw);
    if (Number.isNaN(d.getTime())) continue;
    if (!latest || d > latest) latest = d;
  }
  // Fallback when nothing parses — never crash a render.
  return format(latest ?? new Date());
}
