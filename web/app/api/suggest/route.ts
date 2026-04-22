import { NextResponse } from 'next/server';
import { suggestCms } from '@/lib/cms';

export async function GET(req: Request) {
  const { searchParams } = new URL(req.url);
  const q = searchParams.get('q') ?? '';
  const size = Number(searchParams.get('size') ?? 8);
  if (q.trim().length < 2) return NextResponse.json([]);
  try {
    const suggestions = await suggestCms(q, size);
    return NextResponse.json(suggestions, {
      headers: { 'Cache-Control': 'public, s-maxage=60, stale-while-revalidate=300' },
    });
  } catch (err) {
    return NextResponse.json([], { status: 200 });
  }
}
