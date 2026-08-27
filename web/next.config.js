/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  images: {
    // Every cover, screenshot and logo is served from the Cognitor media library
    // (S3). The backend host is the fallback shape produced by lib/cms.ts#mediaUrl().
    remotePatterns: [
      { protocol: 'https', hostname: 'cognotor.s3.eu-central-1.amazonaws.com', pathname: '/uploads/**' },
      { protocol: 'https', hostname: 'backend.cognitor.dev', pathname: '/public/**' },
    ],
    formats: ['image/avif', 'image/webp'],
    // Card grids top out around 400px wide; the article cover and tool screenshot
    // are the only images that need the large end of the ladder.
    deviceSizes: [640, 750, 828, 1080, 1200, 1920],
    imageSizes: [80, 128, 200, 256, 384],
    minimumCacheTTL: 2678400, // 31 days — CMS assets get a new filename on change
  },
  experimental: {
    // Allow Server Components to fetch the CMS without ETag-based caching surprises
    staleTimes: { dynamic: 60, static: 300 },
  },
};
module.exports = nextConfig;
