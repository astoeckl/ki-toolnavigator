/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  experimental: {
    // Allow Server Components to fetch the CMS without ETag-based caching surprises
    staleTimes: { dynamic: 60, static: 300 },
  },
};
module.exports = nextConfig;
