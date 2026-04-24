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
"[project]/components/AnchorLink.tsx [app-client] (ecmascript)", ((__turbopack_context__) => {
"use strict";

__turbopack_context__.s([
    "AnchorLink",
    ()=>AnchorLink
]);
var __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__ = __turbopack_context__.i("[project]/node_modules/next/dist/compiled/react/jsx-dev-runtime.js [app-client] (ecmascript)");
'use client';
;
function AnchorLink({ href, children, style, className }) {
    const onClick = (e)=>{
        if (!href.startsWith('#')) return;
        const id = href.slice(1);
        const el = document.getElementById(id);
        if (!el) return;
        e.preventDefault();
        // Compute absolute target Y, subtract scroll-margin so the sticky header doesn't hide it
        const targetY = Math.max(0, el.getBoundingClientRect().top + window.scrollY - 90);
        // Use the positional form: works in real browsers AND in preview iframes
        // where requestAnimationFrame doesn't fire and `behavior: 'smooth'` is ignored.
        window.scrollTo(0, targetY);
        history.replaceState(null, '', href);
    };
    return /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("a", {
        href: href,
        onClick: onClick,
        style: style,
        className: className,
        children: children
    }, void 0, false, {
        fileName: "[project]/components/AnchorLink.tsx",
        lineNumber: 24,
        columnNumber: 5
    }, this);
}
_c = AnchorLink;
var _c;
__turbopack_context__.k.register(_c, "AnchorLink");
if (typeof globalThis.$RefreshHelpers$ === 'object' && globalThis.$RefreshHelpers !== null) {
    __turbopack_context__.k.registerExports(__turbopack_context__.m, globalThis.$RefreshHelpers$);
}
}),
"[project]/components/ScrollSpyTOC.tsx [app-client] (ecmascript)", ((__turbopack_context__) => {
"use strict";

__turbopack_context__.s([
    "ScrollSpyTOC",
    ()=>ScrollSpyTOC
]);
var __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__ = __turbopack_context__.i("[project]/node_modules/next/dist/compiled/react/jsx-dev-runtime.js [app-client] (ecmascript)");
var __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$index$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__ = __turbopack_context__.i("[project]/node_modules/next/dist/compiled/react/index.js [app-client] (ecmascript)");
var __TURBOPACK__imported__module__$5b$project$5d2f$components$2f$AnchorLink$2e$tsx__$5b$app$2d$client$5d$__$28$ecmascript$29$__ = __turbopack_context__.i("[project]/components/AnchorLink.tsx [app-client] (ecmascript)");
;
var _s = __turbopack_context__.k.signature();
'use client';
;
;
function ScrollSpyTOC({ items, eyebrow = 'Inhalt' }) {
    _s();
    const [activeHash, setActiveHash] = (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$index$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["useState"])(items[0]?.hash ?? '');
    (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$index$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["useEffect"])({
        "ScrollSpyTOC.useEffect": ()=>{
            const targets = items.map({
                "ScrollSpyTOC.useEffect.targets": (it)=>({
                        id: it.hash.slice(1),
                        el: document.getElementById(it.hash.slice(1))
                    })
            }["ScrollSpyTOC.useEffect.targets"]).filter({
                "ScrollSpyTOC.useEffect.targets": (t)=>!!t.el
            }["ScrollSpyTOC.useEffect.targets"]);
            if (targets.length === 0) return;
            // Active = the LAST section whose top has crossed `offset` (pixels from viewport top).
            // Falls back to first if none has crossed yet.
            const offset = 120;
            const compute = {
                "ScrollSpyTOC.useEffect.compute": ()=>{
                    let activeId = targets[0].id;
                    for (const t of targets){
                        const top = t.el.getBoundingClientRect().top;
                        if (top - offset <= 0) activeId = t.id;
                        else break;
                    }
                    setActiveHash({
                        "ScrollSpyTOC.useEffect.compute": (prev)=>prev === '#' + activeId ? prev : '#' + activeId
                    }["ScrollSpyTOC.useEffect.compute"]);
                }
            }["ScrollSpyTOC.useEffect.compute"];
            // Lightweight throttle via timestamp — avoids requestAnimationFrame which
            // is unreliable inside some preview iframes.
            let last = 0;
            const onScroll = {
                "ScrollSpyTOC.useEffect.onScroll": ()=>{
                    const now = Date.now();
                    if (now - last < 60) return;
                    last = now;
                    compute();
                }
            }["ScrollSpyTOC.useEffect.onScroll"];
            window.addEventListener('scroll', onScroll, {
                passive: true
            });
            window.addEventListener('resize', onScroll);
            compute();
            // Final compute slightly later in case the layout settles after fonts/images.
            const t1 = setTimeout(compute, 200);
            return ({
                "ScrollSpyTOC.useEffect": ()=>{
                    window.removeEventListener('scroll', onScroll);
                    window.removeEventListener('resize', onScroll);
                    clearTimeout(t1);
                }
            })["ScrollSpyTOC.useEffect"];
        }
    }["ScrollSpyTOC.useEffect"], [
        items
    ]);
    return /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])(__TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["Fragment"], {
        children: [
            /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                style: {
                    fontFamily: 'JetBrains Mono, monospace',
                    fontSize: 11,
                    color: '#8a8580',
                    letterSpacing: '0.08em',
                    textTransform: 'uppercase',
                    marginBottom: 14
                },
                children: eyebrow
            }, void 0, false, {
                fileName: "[project]/components/ScrollSpyTOC.tsx",
                lineNumber: 66,
                columnNumber: 7
            }, this),
            /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("ul", {
                style: {
                    listStyle: 'none',
                    padding: 0,
                    margin: 0,
                    borderLeft: '1px solid var(--line)'
                },
                children: items.map((it)=>{
                    const active = it.hash === activeHash;
                    return /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("li", {
                        style: {
                            padding: '6px 14px',
                            fontSize: 13,
                            borderLeft: active ? '2px solid var(--accent)' : '2px solid transparent',
                            marginLeft: -1,
                            color: active ? 'var(--accent)' : 'var(--ink)',
                            transition: 'color 0.15s, border-color 0.15s'
                        },
                        children: [
                            it.num && /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("span", {
                                style: {
                                    fontFamily: 'JetBrains Mono, monospace',
                                    fontSize: 10,
                                    marginRight: 8,
                                    color: '#8a8580'
                                },
                                children: it.num
                            }, void 0, false, {
                                fileName: "[project]/components/ScrollSpyTOC.tsx",
                                lineNumber: 85,
                                columnNumber: 17
                            }, this),
                            /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])(__TURBOPACK__imported__module__$5b$project$5d2f$components$2f$AnchorLink$2e$tsx__$5b$app$2d$client$5d$__$28$ecmascript$29$__["AnchorLink"], {
                                href: it.hash,
                                style: {
                                    color: 'inherit',
                                    cursor: 'pointer'
                                },
                                children: it.label
                            }, void 0, false, {
                                fileName: "[project]/components/ScrollSpyTOC.tsx",
                                lineNumber: 90,
                                columnNumber: 15
                            }, this)
                        ]
                    }, it.hash, true, {
                        fileName: "[project]/components/ScrollSpyTOC.tsx",
                        lineNumber: 77,
                        columnNumber: 13
                    }, this);
                })
            }, void 0, false, {
                fileName: "[project]/components/ScrollSpyTOC.tsx",
                lineNumber: 73,
                columnNumber: 7
            }, this)
        ]
    }, void 0, true);
}
_s(ScrollSpyTOC, "aXukSyo45Cv5vFSG9o/H1M0kU1c=");
_c = ScrollSpyTOC;
var _c;
__turbopack_context__.k.register(_c, "ScrollSpyTOC");
if (typeof globalThis.$RefreshHelpers$ === 'object' && globalThis.$RefreshHelpers !== null) {
    __turbopack_context__.k.registerExports(__turbopack_context__.m, globalThis.$RefreshHelpers$);
}
}),
]);

//# sourceMappingURL=components_09gwqm0._.js.map