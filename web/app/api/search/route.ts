import { NextResponse } from 'next/server';
import { searchCms } from '@/lib/cms';

export async function GET(req: Request) {
  const { searchParams } = new URL(req.url);
  const q = searchParams.get('q') ?? '';
  const size = Number(searchParams.get('size') ?? 20);
  const page = Number(searchParams.get('page') ?? 1);
  try {
    const data = await searchCms(q, { size, page });
    return NextResponse.json(data, {
      headers: { 'Cache-Control': 'public, s-maxage=30, stale-while-revalidate=120' },
    });
  } catch (err) {
    return NextResponse.json({ results: [], total: 0, error: String(err) }, { status: 500 });
  }
}
