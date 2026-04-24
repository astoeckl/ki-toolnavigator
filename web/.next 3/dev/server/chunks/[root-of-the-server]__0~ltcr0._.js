module.exports = [
"[externals]/next/dist/compiled/next-server/app-route-turbo.runtime.dev.js [external] (next/dist/compiled/next-server/app-route-turbo.runtime.dev.js, cjs)", ((__turbopack_context__, module, exports) => {

const mod = __turbopack_context__.x("next/dist/compiled/next-server/app-route-turbo.runtime.dev.js", () => require("next/dist/compiled/next-server/app-route-turbo.runtime.dev.js"));

module.exports = mod;
}),
"[externals]/next/dist/compiled/next-server/app-page-turbo.runtime.dev.js [external] (next/dist/compiled/next-server/app-page-turbo.runtime.dev.js, cjs)", ((__turbopack_context__, module, exports) => {

const mod = __turbopack_context__.x("next/dist/compiled/next-server/app-page-turbo.runtime.dev.js", () => require("next/dist/compiled/next-server/app-page-turbo.runtime.dev.js"));

module.exports = mod;
}),
"[externals]/next/dist/server/app-render/work-unit-async-storage.external.js [external] (next/dist/server/app-render/work-unit-async-storage.external.js, cjs)", ((__turbopack_context__, module, exports) => {

const mod = __turbopack_context__.x("next/dist/server/app-render/work-unit-async-storage.external.js", () => require("next/dist/server/app-render/work-unit-async-storage.external.js"));

module.exports = mod;
}),
"[externals]/next/dist/server/app-render/work-async-storage.external.js [external] (next/dist/server/app-render/work-async-storage.external.js, cjs)", ((__turbopack_context__, module, exports) => {

const mod = __turbopack_context__.x("next/dist/server/app-render/work-async-storage.external.js", () => require("next/dist/server/app-render/work-async-storage.external.js"));

module.exports = mod;
}),
"[externals]/next/dist/shared/lib/no-fallback-error.external.js [external] (next/dist/shared/lib/no-fallback-error.external.js, cjs)", ((__turbopack_context__, module, exports) => {

const mod = __turbopack_context__.x("next/dist/shared/lib/no-fallback-error.external.js", () => require("next/dist/shared/lib/no-fallback-error.external.js"));

module.exports = mod;
}),
"[externals]/next/dist/server/app-render/after-task-async-storage.external.js [external] (next/dist/server/app-render/after-task-async-storage.external.js, cjs)", ((__turbopack_context__, module, exports) => {

const mod = __turbopack_context__.x("next/dist/server/app-render/after-task-async-storage.external.js", () => require("next/dist/server/app-render/after-task-async-storage.external.js"));

module.exports = mod;
}),
"[project]/lib/cms.ts [app-route] (ecmascript)", ((__turbopack_context__) => {
"use strict";

__turbopack_context__.s([
    "getAll",
    ()=>getAll,
    "getArticle",
    ()=>getArticle,
    "getArticles",
    ()=>getArticles,
    "getCategories",
    ()=>getCategories,
    "getCategory",
    ()=>getCategory,
    "getMedia",
    ()=>getMedia,
    "getPost",
    ()=>getPost,
    "getTool",
    ()=>getTool,
    "getTools",
    ()=>getTools,
    "mediaUrl",
    ()=>mediaUrl,
    "searchCms",
    ()=>searchCms,
    "suggestCms",
    ()=>suggestCms
]);
const BASE = process.env.COGNITOR_BASE_URL ?? 'https://backend.cognitor.dev';
const SITE = process.env.COGNITOR_SITE ?? 'ki-toolnavigator-site';
const EMAIL = process.env.COGNITOR_EMAIL;
const PASSWORD = process.env.COGNITOR_PASSWORD;
// Public Cognitor read endpoint requires the site-prefixed identifier
const typeId = (key)=>`${SITE}_${key}`;
async function fetchType(key, revalidate = 60) {
    const url = `${BASE}/public/${SITE}/elements/?type=${typeId(key)}&limit=500`;
    const res = await fetch(url, {
        next: {
            revalidate,
            tags: [
                `cms:${key}`
            ]
        }
    });
    if (!res.ok) throw new Error(`CMS fetch failed for "${key}": ${res.status} ${res.statusText}`);
    const items = await res.json();
    // Inject CMS metadata so consumers can use it for "last changed" UI
    // without re-fetching or losing data when the editor doesn't manually update fields.
    return items.map((el)=>({
            ...el.data,
            _updated_at: el.updated_at,
            _id: el.id
        }));
}
// ---- Auth (server-only) — token cached in module scope ----
let cachedToken = null;
async function getToken() {
    // 50-min cache; tokens are short-lived but we re-login eagerly
    if (cachedToken && cachedToken.expires > Date.now() + 5 * 60_000) return cachedToken.value;
    if (!EMAIL || !PASSWORD) throw new Error('COGNITOR_EMAIL/COGNITOR_PASSWORD not set in env');
    const body = new URLSearchParams({
        grant_type: 'password',
        username: EMAIL,
        password: PASSWORD
    });
    const res = await fetch(`${BASE}/auth/login`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body,
        cache: 'no-store'
    });
    if (!res.ok) throw new Error(`Cognitor login failed: ${res.status}`);
    const data = await res.json();
    cachedToken = {
        value: data.access_token,
        expires: Date.now() + 50 * 60_000
    };
    return cachedToken.value;
}
async function searchCms(q, opts = {}) {
    if (!q.trim()) return {
        results: [],
        total: 0
    };
    const params = new URLSearchParams({
        q,
        size: String(opts.size ?? 20),
        page: String(opts.page ?? 1),
        highlight: 'true',
        published_only: 'true',
        locale: 'de'
    });
    const url = `${BASE}/search/sites/${SITE}?${params}`;
    const res = await fetch(url, {
        next: {
            revalidate: 30
        }
    });
    if (!res.ok) throw new Error(`Search failed: ${res.status}`);
    const data = await res.json();
    return Array.isArray(data) ? {
        results: data
    } : data;
}
async function suggestCms(q, size = 8) {
    if (!q.trim()) return [];
    const params = new URLSearchParams({
        q,
        size: String(size),
        locale: 'de'
    });
    const res = await fetch(`${BASE}/search/sites/${SITE}/suggest?${params}`, {
        cache: 'no-store'
    });
    if (!res.ok) return [];
    const data = await res.json();
    return Array.isArray(data) ? data : data.suggestions ?? [];
}
async function getMedia(id, revalidate = 300) {
    const res = await fetch(`${BASE}/public/${SITE}/media/${id}`, {
        next: {
            revalidate,
            tags: [
                `cms:media:${id}`
            ]
        }
    });
    if (res.status === 404) return null;
    if (!res.ok) return null;
    return await res.json();
}
function mediaUrl(id) {
    return `${BASE}/public/${SITE}/media/${id}/view`;
}
async function getPost(id, revalidate = 60) {
    const token = await getToken();
    const res = await fetch(`${BASE}/${SITE}/posts/${id}`, {
        headers: {
            Authorization: `Bearer ${token}`
        },
        next: {
            revalidate,
            tags: [
                `cms:post:${id}`
            ]
        }
    });
    if (res.status === 404) return null;
    if (!res.ok) throw new Error(`Post fetch failed for id=${id}: ${res.status}`);
    return await res.json();
}
async function getCategories() {
    const cats = await fetchType('category');
    return cats.sort((a, b)=>(a.order ?? 999) - (b.order ?? 999));
}
async function getTools() {
    return fetchType('tool');
}
async function getArticles() {
    return fetchType('article');
}
async function getAll() {
    const [categories, tools, articles] = await Promise.all([
        getCategories(),
        getTools(),
        getArticles()
    ]);
    return {
        categories,
        tools,
        articles
    };
}
async function getTool(slug) {
    const tools = await getTools();
    return tools.find((t)=>t.slug === slug);
}
async function getCategory(slug) {
    const cats = await getCategories();
    return cats.find((c)=>c.slug === slug);
}
async function getArticle(slug) {
    const articles = await getArticles();
    return articles.find((a)=>a.slug === slug);
}
}),
"[project]/app/api/suggest/route.ts [app-route] (ecmascript)", ((__turbopack_context__) => {
"use strict";

__turbopack_context__.s([
    "GET",
    ()=>GET
]);
var __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$server$2e$js__$5b$app$2d$route$5d$__$28$ecmascript$29$__ = __turbopack_context__.i("[project]/node_modules/next/server.js [app-route] (ecmascript)");
var __TURBOPACK__imported__module__$5b$project$5d2f$lib$2f$cms$2e$ts__$5b$app$2d$route$5d$__$28$ecmascript$29$__ = __turbopack_context__.i("[project]/lib/cms.ts [app-route] (ecmascript)");
;
;
async function GET(req) {
    const { searchParams } = new URL(req.url);
    const q = searchParams.get('q') ?? '';
    const size = Number(searchParams.get('size') ?? 8);
    if (q.trim().length < 2) return __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$server$2e$js__$5b$app$2d$route$5d$__$28$ecmascript$29$__["NextResponse"].json([]);
    try {
        const suggestions = await (0, __TURBOPACK__imported__module__$5b$project$5d2f$lib$2f$cms$2e$ts__$5b$app$2d$route$5d$__$28$ecmascript$29$__["suggestCms"])(q, size);
        return __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$server$2e$js__$5b$app$2d$route$5d$__$28$ecmascript$29$__["NextResponse"].json(suggestions, {
            headers: {
                'Cache-Control': 'public, s-maxage=60, stale-while-revalidate=300'
            }
        });
    } catch (err) {
        return __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$server$2e$js__$5b$app$2d$route$5d$__$28$ecmascript$29$__["NextResponse"].json([], {
            status: 200
        });
    }
}
}),
];

//# sourceMappingURL=%5Broot-of-the-server%5D__0~ltcr0._.js.map