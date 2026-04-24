(globalThis["TURBOPACK"] || (globalThis["TURBOPACK"] = [])).push([typeof document === "object" ? document.currentScript : undefined,
"[project]/components/ui.tsx [app-client] (ecmascript)", ((__turbopack_context__) => {
"use strict";

__turbopack_context__.s([
    "Badge",
    ()=>Badge,
    "Breadcrumb",
    ()=>Breadcrumb,
    "Button",
    ()=>Button,
    "Chip",
    ()=>Chip,
    "DataRow",
    ()=>DataRow,
    "SectionLabel",
    ()=>SectionLabel,
    "Stars",
    ()=>Stars,
    "Thumb",
    ()=>Thumb
]);
var __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__ = __turbopack_context__.i("[project]/node_modules/next/dist/compiled/react/jsx-dev-runtime.js [app-client] (ecmascript)");
var __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$client$2f$app$2d$dir$2f$link$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__ = __turbopack_context__.i("[project]/node_modules/next/dist/client/app-dir/link.js [app-client] (ecmascript)");
'use client';
;
;
function Chip({ children, accent, mono = true, onClick }) {
    return /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("span", {
        onClick: onClick,
        style: {
            display: 'inline-flex',
            alignItems: 'center',
            padding: '3px 8px',
            border: '1px solid ' + (accent ? 'var(--accent)' : 'var(--line)'),
            color: accent ? 'var(--accent)' : 'var(--ink)',
            fontFamily: mono ? 'JetBrains Mono, monospace' : 'Inter Tight, sans-serif',
            fontSize: 11,
            letterSpacing: mono ? '0.04em' : '0',
            textTransform: mono ? 'uppercase' : 'none',
            cursor: onClick ? 'pointer' : 'default',
            background: 'transparent',
            whiteSpace: 'nowrap'
        },
        children: children
    }, void 0, false, {
        fileName: "[project]/components/ui.tsx",
        lineNumber: 8,
        columnNumber: 5
    }, this);
}
_c = Chip;
function Stars({ rating, size = 12 }) {
    const filled = Math.round(rating);
    return /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("span", {
        style: {
            display: 'inline-flex',
            gap: 1,
            color: 'var(--accent)',
            fontSize: size,
            letterSpacing: -1
        },
        children: '★★★★★'.split('').map((c, i)=>/*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("span", {
                style: {
                    opacity: i < filled ? 1 : 0.18
                },
                children: c
            }, i, false, {
                fileName: "[project]/components/ui.tsx",
                lineNumber: 25,
                columnNumber: 9
            }, this))
    }, void 0, false, {
        fileName: "[project]/components/ui.tsx",
        lineNumber: 23,
        columnNumber: 5
    }, this);
}
_c1 = Stars;
const dsgvoMap = {
    ja: {
        bg: '#E8F3EC',
        fg: '#2F6A44',
        label: 'DSGVO-konform'
    },
    bedingt: {
        bg: '#FBF1DE',
        fg: '#8A6A1F',
        label: 'DSGVO bedingt'
    },
    nein: {
        bg: '#F5E3E3',
        fg: '#8A2F2F',
        label: 'kein DSGVO-Nachweis'
    }
};
function Badge({ kind, children }) {
    const v = kind && dsgvoMap[kind] || {
        bg: '#F0EDE8',
        fg: '#5A5550',
        label: children
    };
    return /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("span", {
        style: {
            display: 'inline-block',
            padding: '2px 8px',
            background: v.bg,
            color: v.fg,
            fontFamily: 'JetBrains Mono, monospace',
            fontSize: 10,
            letterSpacing: '0.06em',
            textTransform: 'uppercase'
        },
        children: children || v.label
    }, void 0, false, {
        fileName: "[project]/components/ui.tsx",
        lineNumber: 40,
        columnNumber: 5
    }, this);
}
_c2 = Badge;
function Thumb({ name, slug, aspect = '4/3', label }) {
    const hueSeed = (slug || name).split('').reduce((a, c)=>a + c.charCodeAt(0), 0);
    const stripe = hueSeed % 3 === 0 ? 'horizontal' : hueSeed % 3 === 1 ? 'diagonal' : 'vertical';
    const patternId = 'p-' + (slug || name).replace(/[^a-z0-9]/gi, '');
    const transform = stripe === 'diagonal' ? 'rotate(45)' : stripe === 'horizontal' ? 'rotate(0)' : 'rotate(90)';
    return /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
        style: {
            aspectRatio: aspect,
            background: 'var(--bg-alt)',
            border: '1px solid var(--line)',
            position: 'relative',
            overflow: 'hidden'
        },
        children: [
            /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("svg", {
                width: "100%",
                height: "100%",
                style: {
                    position: 'absolute',
                    inset: 0
                },
                preserveAspectRatio: "none",
                children: [
                    /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("defs", {
                        children: /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("pattern", {
                            id: patternId,
                            patternUnits: "userSpaceOnUse",
                            width: "8",
                            height: "8",
                            patternTransform: transform,
                            children: [
                                /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("rect", {
                                    width: "8",
                                    height: "8",
                                    fill: "transparent"
                                }, void 0, false, {
                                    fileName: "[project]/components/ui.tsx",
                                    lineNumber: 62,
                                    columnNumber: 13
                                }, this),
                                /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("line", {
                                    x1: "0",
                                    y1: "0",
                                    x2: "0",
                                    y2: "8",
                                    stroke: "#DDD7CC",
                                    strokeWidth: "1"
                                }, void 0, false, {
                                    fileName: "[project]/components/ui.tsx",
                                    lineNumber: 63,
                                    columnNumber: 13
                                }, this)
                            ]
                        }, void 0, true, {
                            fileName: "[project]/components/ui.tsx",
                            lineNumber: 61,
                            columnNumber: 11
                        }, this)
                    }, void 0, false, {
                        fileName: "[project]/components/ui.tsx",
                        lineNumber: 60,
                        columnNumber: 9
                    }, this),
                    /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("rect", {
                        width: "100%",
                        height: "100%",
                        fill: `url(#${patternId})`
                    }, void 0, false, {
                        fileName: "[project]/components/ui.tsx",
                        lineNumber: 66,
                        columnNumber: 9
                    }, this)
                ]
            }, void 0, true, {
                fileName: "[project]/components/ui.tsx",
                lineNumber: 59,
                columnNumber: 7
            }, this),
            /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                style: {
                    position: 'absolute',
                    inset: 0,
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    fontFamily: 'JetBrains Mono, monospace',
                    fontSize: 10,
                    color: '#a8a39c',
                    letterSpacing: '0.1em',
                    textTransform: 'uppercase'
                },
                children: label ?? `${name} · screenshot`
            }, void 0, false, {
                fileName: "[project]/components/ui.tsx",
                lineNumber: 68,
                columnNumber: 7
            }, this)
        ]
    }, void 0, true, {
        fileName: "[project]/components/ui.tsx",
        lineNumber: 55,
        columnNumber: 5
    }, this);
}
_c3 = Thumb;
function Breadcrumb({ items }) {
    return /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("nav", {
        style: {
            fontFamily: 'JetBrains Mono, monospace',
            fontSize: 11,
            letterSpacing: '0.04em',
            color: '#8a8580',
            textTransform: 'uppercase',
            marginBottom: 28
        },
        children: items.map((it, i)=>/*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("span", {
                children: [
                    i > 0 && /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("span", {
                        style: {
                            margin: '0 8px',
                            opacity: 0.5
                        },
                        children: "/"
                    }, void 0, false, {
                        fileName: "[project]/components/ui.tsx",
                        lineNumber: 89,
                        columnNumber: 21
                    }, this),
                    it.href ? /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])(__TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$client$2f$app$2d$dir$2f$link$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["default"], {
                        href: it.href,
                        style: {
                            color: 'inherit',
                            textDecoration: 'none',
                            borderBottom: '1px dotted #b8b3ac'
                        },
                        children: it.label
                    }, void 0, false, {
                        fileName: "[project]/components/ui.tsx",
                        lineNumber: 91,
                        columnNumber: 13
                    }, this) : /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("span", {
                        style: {
                            color: 'var(--ink-strong)'
                        },
                        children: it.label
                    }, void 0, false, {
                        fileName: "[project]/components/ui.tsx",
                        lineNumber: 93,
                        columnNumber: 13
                    }, this)
                ]
            }, i, true, {
                fileName: "[project]/components/ui.tsx",
                lineNumber: 88,
                columnNumber: 9
            }, this))
    }, void 0, false, {
        fileName: "[project]/components/ui.tsx",
        lineNumber: 82,
        columnNumber: 5
    }, this);
}
_c4 = Breadcrumb;
function SectionLabel({ num, children, id }) {
    return /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
        style: {
            display: 'flex',
            alignItems: 'baseline',
            gap: 14,
            borderBottom: '1px solid var(--line)',
            paddingBottom: 10,
            marginBottom: 28,
            marginTop: num ? 0 : 36
        },
        children: [
            num && /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("span", {
                style: {
                    fontFamily: 'JetBrains Mono, monospace',
                    fontSize: 11,
                    letterSpacing: '0.08em',
                    color: '#8a8580'
                },
                children: [
                    "§ ",
                    num
                ]
            }, void 0, true, {
                fileName: "[project]/components/ui.tsx",
                lineNumber: 109,
                columnNumber: 9
            }, this),
            /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("h2", {
                id: id,
                style: {
                    fontFamily: 'Fraunces, Georgia, serif',
                    fontWeight: 500,
                    fontSize: 22,
                    letterSpacing: '-0.01em',
                    margin: 0,
                    color: 'var(--ink-strong)',
                    scrollMarginTop: 100
                },
                children: children
            }, void 0, false, {
                fileName: "[project]/components/ui.tsx",
                lineNumber: 114,
                columnNumber: 7
            }, this)
        ]
    }, void 0, true, {
        fileName: "[project]/components/ui.tsx",
        lineNumber: 103,
        columnNumber: 5
    }, this);
}
_c5 = SectionLabel;
const buttonStyles = {
    primary: {
        background: 'var(--ink-strong)',
        color: 'var(--bg)',
        border: '1px solid var(--ink-strong)'
    },
    ghost: {
        background: 'transparent',
        color: 'var(--ink-strong)',
        border: '1px solid var(--line)'
    },
    accent: {
        background: 'var(--accent)',
        color: '#fff',
        border: '1px solid var(--accent)'
    }
};
function Button({ children, variant = 'primary', onClick, href, type = 'button', icon }) {
    const style = {
        ...buttonStyles[variant],
        padding: '9px 16px',
        fontFamily: 'Inter Tight, sans-serif',
        fontSize: 13,
        fontWeight: 500,
        letterSpacing: '0.01em',
        cursor: 'pointer',
        display: 'inline-flex',
        alignItems: 'center',
        gap: 8,
        textDecoration: 'none'
    };
    if (href) return /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])(__TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$client$2f$app$2d$dir$2f$link$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["default"], {
        href: href,
        style: style,
        children: [
            icon,
            children
        ]
    }, void 0, true, {
        fileName: "[project]/components/ui.tsx",
        lineNumber: 146,
        columnNumber: 20
    }, this);
    return /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("button", {
        type: type,
        onClick: onClick,
        style: style,
        children: [
            icon,
            children
        ]
    }, void 0, true, {
        fileName: "[project]/components/ui.tsx",
        lineNumber: 147,
        columnNumber: 10
    }, this);
}
_c6 = Button;
function DataRow({ label, value, mono }) {
    return /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
        style: {
            display: 'grid',
            gridTemplateColumns: '120px 1fr',
            padding: '9px 0',
            borderBottom: '1px dotted var(--line)',
            fontSize: 13
        },
        children: [
            /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("span", {
                style: {
                    fontFamily: 'JetBrains Mono, monospace',
                    fontSize: 11,
                    letterSpacing: '0.04em',
                    color: '#8a8580',
                    textTransform: 'uppercase',
                    paddingTop: 1
                },
                children: label
            }, void 0, false, {
                fileName: "[project]/components/ui.tsx",
                lineNumber: 156,
                columnNumber: 7
            }, this),
            /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("span", {
                style: {
                    fontFamily: mono ? 'JetBrains Mono, monospace' : 'Inter Tight, sans-serif',
                    color: 'var(--ink-strong)'
                },
                children: value
            }, void 0, false, {
                fileName: "[project]/components/ui.tsx",
                lineNumber: 161,
                columnNumber: 7
            }, this)
        ]
    }, void 0, true, {
        fileName: "[project]/components/ui.tsx",
        lineNumber: 152,
        columnNumber: 5
    }, this);
}
_c7 = DataRow;
var _c, _c1, _c2, _c3, _c4, _c5, _c6, _c7;
__turbopack_context__.k.register(_c, "Chip");
__turbopack_context__.k.register(_c1, "Stars");
__turbopack_context__.k.register(_c2, "Badge");
__turbopack_context__.k.register(_c3, "Thumb");
__turbopack_context__.k.register(_c4, "Breadcrumb");
__turbopack_context__.k.register(_c5, "SectionLabel");
__turbopack_context__.k.register(_c6, "Button");
__turbopack_context__.k.register(_c7, "DataRow");
if (typeof globalThis.$RefreshHelpers$ === 'object' && globalThis.$RefreshHelpers !== null) {
    __turbopack_context__.k.registerExports(__turbopack_context__.m, globalThis.$RefreshHelpers$);
}
}),
"[project]/lib/site.ts [app-client] (ecmascript)", ((__turbopack_context__) => {
"use strict";

/** Build-time constants — stable across SSR & client hydration. */ __turbopack_context__.s([
    "EDITORIAL_DATE_LABEL",
    ()=>EDITORIAL_DATE_LABEL,
    "EDITORIAL_DATE_SHORT",
    ()=>EDITORIAL_DATE_SHORT
]);
const EDITORIAL_DATE_LABEL = '19. April 2026';
const EDITORIAL_DATE_SHORT = '19.04.2026';
if (typeof globalThis.$RefreshHelpers$ === 'object' && globalThis.$RefreshHelpers !== null) {
    __turbopack_context__.k.registerExports(__turbopack_context__.m, globalThis.$RefreshHelpers$);
}
}),
"[project]/app/vergleich/CompareTable.tsx [app-client] (ecmascript)", ((__turbopack_context__) => {
"use strict";

__turbopack_context__.s([
    "CompareTable",
    ()=>CompareTable
]);
var __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__ = __turbopack_context__.i("[project]/node_modules/next/dist/compiled/react/jsx-dev-runtime.js [app-client] (ecmascript)");
var __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$client$2f$app$2d$dir$2f$link$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__ = __turbopack_context__.i("[project]/node_modules/next/dist/client/app-dir/link.js [app-client] (ecmascript)");
var __TURBOPACK__imported__module__$5b$project$5d2f$lib$2f$site$2e$ts__$5b$app$2d$client$5d$__$28$ecmascript$29$__ = __turbopack_context__.i("[project]/lib/site.ts [app-client] (ecmascript)");
var __TURBOPACK__imported__module__$5b$project$5d2f$components$2f$ui$2e$tsx__$5b$app$2d$client$5d$__$28$ecmascript$29$__ = __turbopack_context__.i("[project]/components/ui.tsx [app-client] (ecmascript)");
var __TURBOPACK__imported__module__$5b$project$5d2f$components$2f$CompareContext$2e$tsx__$5b$app$2d$client$5d$__$28$ecmascript$29$__ = __turbopack_context__.i("[project]/components/CompareContext.tsx [app-client] (ecmascript)");
;
var _s = __turbopack_context__.k.signature();
'use client';
;
;
;
;
/** Resolve tool cover URL from media_id (public endpoint returns a string). */ function toolCover(t) {
    if (typeof t.media_id === 'string') return t.media_id;
    if (t.media_id && typeof t.media_id === 'object') return t.media_id.url ?? null;
    return null;
}
function CompareTable({ tools, categories }) {
    _s();
    const { compareList, remove } = (0, __TURBOPACK__imported__module__$5b$project$5d2f$components$2f$CompareContext$2e$tsx__$5b$app$2d$client$5d$__$28$ecmascript$29$__["useCompare"])();
    const items = compareList.length ? compareList.map((s)=>tools.find((t)=>t.slug === s)).filter(Boolean) : tools.slice(0, 3);
    const rows = [
        {
            label: 'Anbieter',
            get: (t)=>t.vendor,
            mono: true
        },
        {
            label: 'Herkunft',
            get: (t)=>t.origin,
            mono: true
        },
        {
            label: 'Kategorie',
            get: (t)=>categories.find((c)=>c.slug === t.category)?.name
        },
        {
            label: 'Preis',
            get: (t)=>t.price
        },
        {
            label: 'API',
            get: (t)=>t.api ? 'Ja' : 'Nein',
            mono: true
        },
        {
            label: 'DSGVO',
            get: (t)=>/*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])(__TURBOPACK__imported__module__$5b$project$5d2f$components$2f$ui$2e$tsx__$5b$app$2d$client$5d$__$28$ecmascript$29$__["Badge"], {
                    kind: t.dsgvo
                }, void 0, false, {
                    fileName: "[project]/app/vergleich/CompareTable.tsx",
                    lineNumber: 30,
                    columnNumber: 42
                }, this)
        },
        {
            label: 'Launch',
            get: (t)=>new Date(t.launched).toLocaleDateString('de-DE'),
            mono: true
        },
        {
            label: 'Aktualisiert',
            get: (t)=>new Date(t._updated_at ?? t.lastUpdated).toLocaleDateString('de-DE'),
            mono: true
        }
    ];
    return /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])(__TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["Fragment"], {
        children: [
            /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                style: {
                    borderBottom: '1px solid var(--line)',
                    paddingBottom: 32,
                    marginBottom: 40
                },
                children: [
                    /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                        style: {
                            fontFamily: 'JetBrains Mono, monospace',
                            fontSize: 11,
                            color: '#8a8580',
                            letterSpacing: '0.08em',
                            textTransform: 'uppercase',
                            marginBottom: 12
                        },
                        children: "Direktvergleich"
                    }, void 0, false, {
                        fileName: "[project]/app/vergleich/CompareTable.tsx",
                        lineNumber: 38,
                        columnNumber: 9
                    }, this),
                    /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("h1", {
                        className: "h-editorial-md",
                        style: {
                            fontFamily: 'Fraunces, serif',
                            fontWeight: 400,
                            margin: 0,
                            textWrap: 'balance'
                        },
                        children: items.map((t)=>t.name).join(' vs. ')
                    }, void 0, false, {
                        fileName: "[project]/app/vergleich/CompareTable.tsx",
                        lineNumber: 39,
                        columnNumber: 9
                    }, this),
                    /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("p", {
                        style: {
                            fontFamily: 'Fraunces, serif',
                            fontSize: 18,
                            lineHeight: 1.5,
                            color: 'var(--ink)',
                            marginTop: 16,
                            maxWidth: 720
                        },
                        children: [
                            "Tabellarische Gegenüberstellung der wichtigsten Merkmale — gepflegt von der Redaktion am",
                            ' ',
                            __TURBOPACK__imported__module__$5b$project$5d2f$lib$2f$site$2e$ts__$5b$app$2d$client$5d$__$28$ecmascript$29$__["EDITORIAL_DATE_SHORT"],
                            "."
                        ]
                    }, void 0, true, {
                        fileName: "[project]/app/vergleich/CompareTable.tsx",
                        lineNumber: 42,
                        columnNumber: 9
                    }, this)
                ]
            }, void 0, true, {
                fileName: "[project]/app/vergleich/CompareTable.tsx",
                lineNumber: 37,
                columnNumber: 7
            }, this),
            /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                className: "table-scroll",
                style: {
                    border: '1px solid var(--line)'
                },
                children: /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("table", {
                    style: {
                        width: '100%',
                        borderCollapse: 'collapse',
                        fontSize: 13
                    },
                    children: [
                        /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("thead", {
                            children: /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("tr", {
                                children: [
                                    /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("th", {
                                        style: {
                                            padding: 16,
                                            textAlign: 'left',
                                            borderBottom: '1px solid var(--ink-strong)',
                                            width: 180,
                                            fontFamily: 'JetBrains Mono, monospace',
                                            fontSize: 10,
                                            letterSpacing: '0.08em',
                                            textTransform: 'uppercase',
                                            color: '#8a8580',
                                            verticalAlign: 'bottom'
                                        },
                                        children: "Merkmal"
                                    }, void 0, false, {
                                        fileName: "[project]/app/vergleich/CompareTable.tsx",
                                        lineNumber: 52,
                                        columnNumber: 15
                                    }, this),
                                    items.map((t)=>{
                                        const cover = toolCover(t);
                                        return /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("th", {
                                            style: {
                                                padding: 16,
                                                textAlign: 'left',
                                                borderBottom: '1px solid var(--ink-strong)',
                                                verticalAlign: 'bottom',
                                                borderLeft: '1px solid var(--line)'
                                            },
                                            children: [
                                                cover ? /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("img", {
                                                    src: cover,
                                                    alt: t.name,
                                                    style: {
                                                        display: 'block',
                                                        width: '100%',
                                                        height: 'auto',
                                                        aspectRatio: '4 / 3',
                                                        objectFit: 'cover',
                                                        border: '1px solid var(--line)'
                                                    }
                                                }, void 0, false, {
                                                    fileName: "[project]/app/vergleich/CompareTable.tsx",
                                                    lineNumber: 58,
                                                    columnNumber: 21
                                                }, this) : /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])(__TURBOPACK__imported__module__$5b$project$5d2f$components$2f$ui$2e$tsx__$5b$app$2d$client$5d$__$28$ecmascript$29$__["Thumb"], {
                                                    name: t.name,
                                                    slug: `${t.slug}-cmp`,
                                                    aspect: "4/3",
                                                    label: ""
                                                }, void 0, false, {
                                                    fileName: "[project]/app/vergleich/CompareTable.tsx",
                                                    lineNumber: 60,
                                                    columnNumber: 21
                                                }, this),
                                                /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("h3", {
                                                    style: {
                                                        fontFamily: 'Fraunces, serif',
                                                        fontSize: 22,
                                                        fontWeight: 500,
                                                        margin: '12px 0 4px',
                                                        letterSpacing: '-0.01em'
                                                    },
                                                    children: /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])(__TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$client$2f$app$2d$dir$2f$link$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["default"], {
                                                        href: `/tool/${t.slug}`,
                                                        children: t.name
                                                    }, void 0, false, {
                                                        fileName: "[project]/app/vergleich/CompareTable.tsx",
                                                        lineNumber: 63,
                                                        columnNumber: 21
                                                    }, this)
                                                }, void 0, false, {
                                                    fileName: "[project]/app/vergleich/CompareTable.tsx",
                                                    lineNumber: 62,
                                                    columnNumber: 19
                                                }, this),
                                                /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                                                    style: {
                                                        fontFamily: 'JetBrains Mono, monospace',
                                                        fontSize: 10,
                                                        color: '#8a8580',
                                                        letterSpacing: '0.04em',
                                                        textTransform: 'uppercase',
                                                        marginBottom: 8
                                                    },
                                                    children: t.vendor
                                                }, void 0, false, {
                                                    fileName: "[project]/app/vergleich/CompareTable.tsx",
                                                    lineNumber: 65,
                                                    columnNumber: 19
                                                }, this),
                                                /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("a", {
                                                    onClick: ()=>remove(t.slug),
                                                    style: {
                                                        cursor: 'pointer',
                                                        fontSize: 11,
                                                        color: '#8a8580',
                                                        fontFamily: 'JetBrains Mono, monospace',
                                                        borderBottom: '1px dotted #8a8580',
                                                        letterSpacing: '0.04em',
                                                        textTransform: 'uppercase'
                                                    },
                                                    children: "× Entfernen"
                                                }, void 0, false, {
                                                    fileName: "[project]/app/vergleich/CompareTable.tsx",
                                                    lineNumber: 66,
                                                    columnNumber: 19
                                                }, this)
                                            ]
                                        }, t.slug, true, {
                                            fileName: "[project]/app/vergleich/CompareTable.tsx",
                                            lineNumber: 56,
                                            columnNumber: 17
                                        }, this);
                                    }),
                                    items.length < 4 && /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("th", {
                                        style: {
                                            padding: 16,
                                            borderBottom: '1px solid var(--ink-strong)',
                                            borderLeft: '1px solid var(--line)',
                                            verticalAlign: 'middle',
                                            background: 'var(--bg-alt)',
                                            width: 180
                                        },
                                        children: /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])(__TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$client$2f$app$2d$dir$2f$link$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["default"], {
                                            href: "/verzeichnis",
                                            style: {
                                                fontFamily: 'Fraunces, serif',
                                                fontSize: 16,
                                                fontStyle: 'italic',
                                                color: 'var(--accent)'
                                            },
                                            children: "+ Tool hinzufügen"
                                        }, void 0, false, {
                                            fileName: "[project]/app/vergleich/CompareTable.tsx",
                                            lineNumber: 72,
                                            columnNumber: 19
                                        }, this)
                                    }, void 0, false, {
                                        fileName: "[project]/app/vergleich/CompareTable.tsx",
                                        lineNumber: 71,
                                        columnNumber: 17
                                    }, this)
                                ]
                            }, void 0, true, {
                                fileName: "[project]/app/vergleich/CompareTable.tsx",
                                lineNumber: 51,
                                columnNumber: 13
                            }, this)
                        }, void 0, false, {
                            fileName: "[project]/app/vergleich/CompareTable.tsx",
                            lineNumber: 50,
                            columnNumber: 11
                        }, this),
                        /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("tbody", {
                            children: [
                                rows.map((r)=>/*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("tr", {
                                        children: [
                                            /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("td", {
                                                style: {
                                                    padding: '14px 16px',
                                                    borderBottom: '1px dotted var(--line)',
                                                    fontFamily: 'JetBrains Mono, monospace',
                                                    fontSize: 11,
                                                    letterSpacing: '0.04em',
                                                    textTransform: 'uppercase',
                                                    color: '#8a8580'
                                                },
                                                children: r.label
                                            }, void 0, false, {
                                                fileName: "[project]/app/vergleich/CompareTable.tsx",
                                                lineNumber: 80,
                                                columnNumber: 17
                                            }, this),
                                            items.map((t)=>/*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("td", {
                                                    style: {
                                                        padding: '14px 16px',
                                                        borderBottom: '1px dotted var(--line)',
                                                        borderLeft: '1px solid var(--line)',
                                                        fontFamily: r.mono ? 'JetBrains Mono, monospace' : 'Inter Tight, sans-serif',
                                                        color: 'var(--ink-strong)'
                                                    },
                                                    children: r.get(t)
                                                }, t.slug, false, {
                                                    fileName: "[project]/app/vergleich/CompareTable.tsx",
                                                    lineNumber: 82,
                                                    columnNumber: 19
                                                }, this)),
                                            items.length < 4 && /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("td", {
                                                style: {
                                                    borderBottom: '1px dotted var(--line)',
                                                    borderLeft: '1px solid var(--line)',
                                                    background: 'var(--bg-alt)'
                                                }
                                            }, void 0, false, {
                                                fileName: "[project]/app/vergleich/CompareTable.tsx",
                                                lineNumber: 86,
                                                columnNumber: 38
                                            }, this)
                                        ]
                                    }, r.label, true, {
                                        fileName: "[project]/app/vergleich/CompareTable.tsx",
                                        lineNumber: 79,
                                        columnNumber: 15
                                    }, this)),
                                /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("tr", {
                                    children: [
                                        /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("td", {
                                            style: {
                                                padding: '14px 16px',
                                                borderBottom: '1px dotted var(--line)',
                                                fontFamily: 'JetBrains Mono, monospace',
                                                fontSize: 11,
                                                letterSpacing: '0.04em',
                                                textTransform: 'uppercase',
                                                color: '#8a8580',
                                                verticalAlign: 'top'
                                            },
                                            children: "Stärken"
                                        }, void 0, false, {
                                            fileName: "[project]/app/vergleich/CompareTable.tsx",
                                            lineNumber: 90,
                                            columnNumber: 15
                                        }, this),
                                        items.map((t)=>/*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("td", {
                                                style: {
                                                    padding: '14px 16px',
                                                    borderBottom: '1px dotted var(--line)',
                                                    borderLeft: '1px solid var(--line)',
                                                    verticalAlign: 'top'
                                                },
                                                children: /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("ul", {
                                                    style: {
                                                        padding: 0,
                                                        margin: 0,
                                                        listStyle: 'none'
                                                    },
                                                    children: t.pros.map((p, i)=>/*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("li", {
                                                            style: {
                                                                fontSize: 12,
                                                                lineHeight: 1.5,
                                                                padding: '2px 0',
                                                                color: 'var(--ink)'
                                                            },
                                                            children: [
                                                                "+ ",
                                                                p
                                                            ]
                                                        }, i, true, {
                                                            fileName: "[project]/app/vergleich/CompareTable.tsx",
                                                            lineNumber: 94,
                                                            columnNumber: 43
                                                        }, this))
                                                }, void 0, false, {
                                                    fileName: "[project]/app/vergleich/CompareTable.tsx",
                                                    lineNumber: 93,
                                                    columnNumber: 19
                                                }, this)
                                            }, t.slug, false, {
                                                fileName: "[project]/app/vergleich/CompareTable.tsx",
                                                lineNumber: 92,
                                                columnNumber: 17
                                            }, this)),
                                        items.length < 4 && /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("td", {
                                            style: {
                                                borderBottom: '1px dotted var(--line)',
                                                borderLeft: '1px solid var(--line)',
                                                background: 'var(--bg-alt)'
                                            }
                                        }, void 0, false, {
                                            fileName: "[project]/app/vergleich/CompareTable.tsx",
                                            lineNumber: 98,
                                            columnNumber: 36
                                        }, this)
                                    ]
                                }, void 0, true, {
                                    fileName: "[project]/app/vergleich/CompareTable.tsx",
                                    lineNumber: 89,
                                    columnNumber: 13
                                }, this),
                                /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("tr", {
                                    children: [
                                        /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("td", {
                                            style: {
                                                padding: '14px 16px',
                                                fontFamily: 'JetBrains Mono, monospace',
                                                fontSize: 11,
                                                letterSpacing: '0.04em',
                                                textTransform: 'uppercase',
                                                color: '#8a8580',
                                                verticalAlign: 'top'
                                            },
                                            children: "Schwächen"
                                        }, void 0, false, {
                                            fileName: "[project]/app/vergleich/CompareTable.tsx",
                                            lineNumber: 101,
                                            columnNumber: 15
                                        }, this),
                                        items.map((t)=>/*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("td", {
                                                style: {
                                                    padding: '14px 16px',
                                                    borderLeft: '1px solid var(--line)',
                                                    verticalAlign: 'top'
                                                },
                                                children: /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("ul", {
                                                    style: {
                                                        padding: 0,
                                                        margin: 0,
                                                        listStyle: 'none'
                                                    },
                                                    children: t.cons.map((p, i)=>/*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("li", {
                                                            style: {
                                                                fontSize: 12,
                                                                lineHeight: 1.5,
                                                                padding: '2px 0',
                                                                color: 'var(--ink)'
                                                            },
                                                            children: [
                                                                "− ",
                                                                p
                                                            ]
                                                        }, i, true, {
                                                            fileName: "[project]/app/vergleich/CompareTable.tsx",
                                                            lineNumber: 105,
                                                            columnNumber: 43
                                                        }, this))
                                                }, void 0, false, {
                                                    fileName: "[project]/app/vergleich/CompareTable.tsx",
                                                    lineNumber: 104,
                                                    columnNumber: 19
                                                }, this)
                                            }, t.slug, false, {
                                                fileName: "[project]/app/vergleich/CompareTable.tsx",
                                                lineNumber: 103,
                                                columnNumber: 17
                                            }, this)),
                                        items.length < 4 && /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("td", {
                                            style: {
                                                borderLeft: '1px solid var(--line)',
                                                background: 'var(--bg-alt)'
                                            }
                                        }, void 0, false, {
                                            fileName: "[project]/app/vergleich/CompareTable.tsx",
                                            lineNumber: 109,
                                            columnNumber: 36
                                        }, this)
                                    ]
                                }, void 0, true, {
                                    fileName: "[project]/app/vergleich/CompareTable.tsx",
                                    lineNumber: 100,
                                    columnNumber: 13
                                }, this)
                            ]
                        }, void 0, true, {
                            fileName: "[project]/app/vergleich/CompareTable.tsx",
                            lineNumber: 77,
                            columnNumber: 11
                        }, this)
                    ]
                }, void 0, true, {
                    fileName: "[project]/app/vergleich/CompareTable.tsx",
                    lineNumber: 49,
                    columnNumber: 9
                }, this)
            }, void 0, false, {
                fileName: "[project]/app/vergleich/CompareTable.tsx",
                lineNumber: 48,
                columnNumber: 7
            }, this)
        ]
    }, void 0, true);
}
_s(CompareTable, "ocayJK8zIyLMMHvcJJtgDle0CGo=", false, function() {
    return [
        __TURBOPACK__imported__module__$5b$project$5d2f$components$2f$CompareContext$2e$tsx__$5b$app$2d$client$5d$__$28$ecmascript$29$__["useCompare"]
    ];
});
_c = CompareTable;
var _c;
__turbopack_context__.k.register(_c, "CompareTable");
if (typeof globalThis.$RefreshHelpers$ === 'object' && globalThis.$RefreshHelpers !== null) {
    __turbopack_context__.k.registerExports(__turbopack_context__.m, globalThis.$RefreshHelpers$);
}
}),
]);

//# sourceMappingURL=_093s1~b._.js.map