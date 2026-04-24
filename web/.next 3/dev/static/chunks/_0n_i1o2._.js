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
"[project]/app/tool/[slug]/ToolActions.tsx [app-client] (ecmascript)", ((__turbopack_context__) => {
"use strict";

__turbopack_context__.s([
    "ToolActions",
    ()=>ToolActions
]);
var __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__ = __turbopack_context__.i("[project]/node_modules/next/dist/compiled/react/jsx-dev-runtime.js [app-client] (ecmascript)");
var __TURBOPACK__imported__module__$5b$project$5d2f$components$2f$ui$2e$tsx__$5b$app$2d$client$5d$__$28$ecmascript$29$__ = __turbopack_context__.i("[project]/components/ui.tsx [app-client] (ecmascript)");
var __TURBOPACK__imported__module__$5b$project$5d2f$components$2f$CompareContext$2e$tsx__$5b$app$2d$client$5d$__$28$ecmascript$29$__ = __turbopack_context__.i("[project]/components/CompareContext.tsx [app-client] (ecmascript)");
;
var _s = __turbopack_context__.k.signature();
'use client';
;
;
function ToolActions({ slug }) {
    _s();
    const { has, toggle } = (0, __TURBOPACK__imported__module__$5b$project$5d2f$components$2f$CompareContext$2e$tsx__$5b$app$2d$client$5d$__$28$ecmascript$29$__["useCompare"])();
    return /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
        style: {
            marginTop: 24,
            display: 'flex',
            gap: 10,
            flexWrap: 'wrap'
        },
        children: [
            /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])(__TURBOPACK__imported__module__$5b$project$5d2f$components$2f$ui$2e$tsx__$5b$app$2d$client$5d$__$28$ecmascript$29$__["Button"], {
                variant: "primary",
                onClick: ()=>window.open(`https://${slug}.example`, '_blank'),
                children: "Website besuchen ↗"
            }, void 0, false, {
                fileName: "[project]/app/tool/[slug]/ToolActions.tsx",
                lineNumber: 9,
                columnNumber: 7
            }, this),
            /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])(__TURBOPACK__imported__module__$5b$project$5d2f$components$2f$ui$2e$tsx__$5b$app$2d$client$5d$__$28$ecmascript$29$__["Button"], {
                variant: "ghost",
                onClick: ()=>toggle(slug),
                children: has(slug) ? '✓ im Vergleichskorb' : '+ Zum Vergleich hinzufügen'
            }, void 0, false, {
                fileName: "[project]/app/tool/[slug]/ToolActions.tsx",
                lineNumber: 12,
                columnNumber: 7
            }, this)
        ]
    }, void 0, true, {
        fileName: "[project]/app/tool/[slug]/ToolActions.tsx",
        lineNumber: 8,
        columnNumber: 5
    }, this);
}
_s(ToolActions, "B9NNGeEjYHPG9yvnC1wDfZkReW0=", false, function() {
    return [
        __TURBOPACK__imported__module__$5b$project$5d2f$components$2f$CompareContext$2e$tsx__$5b$app$2d$client$5d$__$28$ecmascript$29$__["useCompare"]
    ];
});
_c = ToolActions;
var _c;
__turbopack_context__.k.register(_c, "ToolActions");
if (typeof globalThis.$RefreshHelpers$ === 'object' && globalThis.$RefreshHelpers !== null) {
    __turbopack_context__.k.registerExports(__turbopack_context__.m, globalThis.$RefreshHelpers$);
}
}),
"[project]/components/Prose.tsx [app-client] (ecmascript)", ((__turbopack_context__) => {
"use strict";

/** Editorial prose with Fraunces serif H2s, accent drop-cap, and pull-quotes. */ __turbopack_context__.s([
    "Prose",
    ()=>Prose
]);
var __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__ = __turbopack_context__.i("[project]/node_modules/next/dist/compiled/react/jsx-dev-runtime.js [app-client] (ecmascript)");
;
function Prose({ html, dropCap = false }) {
    return /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
        className: 'prose' + (dropCap ? ' prose--drop-cap' : ''),
        dangerouslySetInnerHTML: {
            __html: html
        }
    }, void 0, false, {
        fileName: "[project]/components/Prose.tsx",
        lineNumber: 6,
        columnNumber: 5
    }, this);
}
_c = Prose;
var _c;
__turbopack_context__.k.register(_c, "Prose");
if (typeof globalThis.$RefreshHelpers$ === 'object' && globalThis.$RefreshHelpers !== null) {
    __turbopack_context__.k.registerExports(__turbopack_context__.m, globalThis.$RefreshHelpers$);
}
}),
"[project]/app/tool/[slug]/ToolTabs.tsx [app-client] (ecmascript)", ((__turbopack_context__) => {
"use strict";

__turbopack_context__.s([
    "ToolTabs",
    ()=>ToolTabs
]);
var __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__ = __turbopack_context__.i("[project]/node_modules/next/dist/compiled/react/jsx-dev-runtime.js [app-client] (ecmascript)");
var __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$client$2f$app$2d$dir$2f$link$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__ = __turbopack_context__.i("[project]/node_modules/next/dist/client/app-dir/link.js [app-client] (ecmascript)");
var __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$index$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__ = __turbopack_context__.i("[project]/node_modules/next/dist/compiled/react/index.js [app-client] (ecmascript)");
var __TURBOPACK__imported__module__$5b$project$5d2f$components$2f$ui$2e$tsx__$5b$app$2d$client$5d$__$28$ecmascript$29$__ = __turbopack_context__.i("[project]/components/ui.tsx [app-client] (ecmascript)");
var __TURBOPACK__imported__module__$5b$project$5d2f$components$2f$Prose$2e$tsx__$5b$app$2d$client$5d$__$28$ecmascript$29$__ = __turbopack_context__.i("[project]/components/Prose.tsx [app-client] (ecmascript)");
;
var _s = __turbopack_context__.k.signature();
'use client';
;
;
;
;
const TABS = [
    {
        id: 'uebersicht',
        label: 'Übersicht'
    },
    {
        id: 'funktionen',
        label: 'Funktionen'
    },
    {
        id: 'preise',
        label: 'Preise'
    }
];
function ToolTabs({ t, catName, related, overviewHtml, featuresHtml, pricingHtml }) {
    _s();
    const [tab, setTab] = (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$index$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["useState"])('uebersicht');
    return /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])(__TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["Fragment"], {
        children: [
            /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("nav", {
                style: {
                    marginTop: 48,
                    display: 'flex',
                    gap: 0,
                    borderBottom: '1px solid var(--line)'
                },
                children: TABS.map((tb)=>/*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("a", {
                        onClick: ()=>setTab(tb.id),
                        style: {
                            padding: '12px 18px',
                            cursor: 'pointer',
                            fontFamily: 'Inter Tight, sans-serif',
                            fontSize: 13,
                            color: tab === tb.id ? 'var(--ink-strong)' : '#8a8580',
                            borderBottom: tab === tb.id ? '2px solid var(--accent)' : '2px solid transparent',
                            marginBottom: -1,
                            fontWeight: tab === tb.id ? 600 : 400
                        },
                        children: tb.label
                    }, tb.id, false, {
                        fileName: "[project]/app/tool/[slug]/ToolTabs.tsx",
                        lineNumber: 29,
                        columnNumber: 11
                    }, this))
            }, void 0, false, {
                fileName: "[project]/app/tool/[slug]/ToolTabs.tsx",
                lineNumber: 27,
                columnNumber: 7
            }, this),
            tab === 'funktionen' ? /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                style: {
                    paddingTop: 36
                },
                children: featuresHtml ? /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])(__TURBOPACK__imported__module__$5b$project$5d2f$components$2f$Prose$2e$tsx__$5b$app$2d$client$5d$__$28$ecmascript$29$__["Prose"], {
                    html: featuresHtml
                }, void 0, false, {
                    fileName: "[project]/app/tool/[slug]/ToolTabs.tsx",
                    lineNumber: 42,
                    columnNumber: 13
                }, this) : /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("p", {
                    style: {
                        fontSize: 16,
                        lineHeight: 1.75,
                        color: 'var(--ink)',
                        fontStyle: 'italic'
                    },
                    children: "Funktionsliste folgt in Kürze."
                }, void 0, false, {
                    fileName: "[project]/app/tool/[slug]/ToolTabs.tsx",
                    lineNumber: 44,
                    columnNumber: 13
                }, this)
            }, void 0, false, {
                fileName: "[project]/app/tool/[slug]/ToolTabs.tsx",
                lineNumber: 40,
                columnNumber: 9
            }, this) : tab === 'preise' ? /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                style: {
                    paddingTop: 36
                },
                children: pricingHtml ? /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])(__TURBOPACK__imported__module__$5b$project$5d2f$components$2f$Prose$2e$tsx__$5b$app$2d$client$5d$__$28$ecmascript$29$__["Prose"], {
                    html: pricingHtml
                }, void 0, false, {
                    fileName: "[project]/app/tool/[slug]/ToolTabs.tsx",
                    lineNumber: 52,
                    columnNumber: 13
                }, this) : /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("p", {
                    style: {
                        fontSize: 16,
                        lineHeight: 1.75,
                        color: 'var(--ink)',
                        fontStyle: 'italic'
                    },
                    children: "Preisangaben folgen in Kürze."
                }, void 0, false, {
                    fileName: "[project]/app/tool/[slug]/ToolTabs.tsx",
                    lineNumber: 54,
                    columnNumber: 13
                }, this)
            }, void 0, false, {
                fileName: "[project]/app/tool/[slug]/ToolTabs.tsx",
                lineNumber: 50,
                columnNumber: 9
            }, this) : tab === 'uebersicht' ? /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                id: "zusammenfassung",
                style: {
                    paddingTop: 36,
                    scrollMarginTop: 100
                },
                children: [
                    overviewHtml ? /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])(__TURBOPACK__imported__module__$5b$project$5d2f$components$2f$Prose$2e$tsx__$5b$app$2d$client$5d$__$28$ecmascript$29$__["Prose"], {
                        html: overviewHtml,
                        dropCap: true
                    }, void 0, false, {
                        fileName: "[project]/app/tool/[slug]/ToolTabs.tsx",
                        lineNumber: 62,
                        columnNumber: 13
                    }, this) : /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("p", {
                        style: {
                            fontSize: 16,
                            lineHeight: 1.75,
                            color: 'var(--ink)',
                            fontStyle: 'italic'
                        },
                        children: "Übersichtstext folgt in Kürze."
                    }, void 0, false, {
                        fileName: "[project]/app/tool/[slug]/ToolTabs.tsx",
                        lineNumber: 64,
                        columnNumber: 13
                    }, this),
                    (()=>{
                        const sshot = typeof t.screenshot_id === 'string' ? t.screenshot_id : t.screenshot_id && typeof t.screenshot_id === 'object' ? t.screenshot_id.url ?? null : null;
                        if (!sshot) {
                            return /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])(__TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["Fragment"], {
                                children: [
                                    /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])(__TURBOPACK__imported__module__$5b$project$5d2f$components$2f$ui$2e$tsx__$5b$app$2d$client$5d$__$28$ecmascript$29$__["SectionLabel"], {
                                        id: "screenshot",
                                        children: "Bildergalerie"
                                    }, void 0, false, {
                                        fileName: "[project]/app/tool/[slug]/ToolTabs.tsx",
                                        lineNumber: 77,
                                        columnNumber: 19
                                    }, this),
                                    /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                                        style: {
                                            display: 'grid',
                                            gridTemplateColumns: 'repeat(3, 1fr)',
                                            gap: 12
                                        },
                                        children: [
                                            /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])(__TURBOPACK__imported__module__$5b$project$5d2f$components$2f$ui$2e$tsx__$5b$app$2d$client$5d$__$28$ecmascript$29$__["Thumb"], {
                                                name: `${t.name} UI`,
                                                slug: `${t.slug}-1`,
                                                aspect: "4/3",
                                                label: "UI · Hauptansicht"
                                            }, void 0, false, {
                                                fileName: "[project]/app/tool/[slug]/ToolTabs.tsx",
                                                lineNumber: 79,
                                                columnNumber: 21
                                            }, this),
                                            /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])(__TURBOPACK__imported__module__$5b$project$5d2f$components$2f$ui$2e$tsx__$5b$app$2d$client$5d$__$28$ecmascript$29$__["Thumb"], {
                                                name: `${t.name} Ansicht 2`,
                                                slug: `${t.slug}-2`,
                                                aspect: "4/3",
                                                label: "UI · Einstellungen"
                                            }, void 0, false, {
                                                fileName: "[project]/app/tool/[slug]/ToolTabs.tsx",
                                                lineNumber: 80,
                                                columnNumber: 21
                                            }, this),
                                            /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])(__TURBOPACK__imported__module__$5b$project$5d2f$components$2f$ui$2e$tsx__$5b$app$2d$client$5d$__$28$ecmascript$29$__["Thumb"], {
                                                name: `${t.name} Ansicht 3`,
                                                slug: `${t.slug}-3`,
                                                aspect: "4/3",
                                                label: "UI · API-Playground"
                                            }, void 0, false, {
                                                fileName: "[project]/app/tool/[slug]/ToolTabs.tsx",
                                                lineNumber: 81,
                                                columnNumber: 21
                                            }, this)
                                        ]
                                    }, void 0, true, {
                                        fileName: "[project]/app/tool/[slug]/ToolTabs.tsx",
                                        lineNumber: 78,
                                        columnNumber: 19
                                    }, this)
                                ]
                            }, void 0, true);
                        }
                        return /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])(__TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["Fragment"], {
                            children: [
                                /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])(__TURBOPACK__imported__module__$5b$project$5d2f$components$2f$ui$2e$tsx__$5b$app$2d$client$5d$__$28$ecmascript$29$__["SectionLabel"], {
                                    id: "screenshot",
                                    children: "Screenshot"
                                }, void 0, false, {
                                    fileName: "[project]/app/tool/[slug]/ToolTabs.tsx",
                                    lineNumber: 88,
                                    columnNumber: 17
                                }, this),
                                /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("figure", {
                                    style: {
                                        margin: 0,
                                        border: '1px solid var(--line)',
                                        padding: 0
                                    },
                                    children: [
                                        /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("img", {
                                            src: sshot,
                                            alt: `Screenshot der ${t.name}-Website`,
                                            style: {
                                                display: 'block',
                                                width: '100%',
                                                height: 'auto',
                                                aspectRatio: '16 / 10',
                                                objectFit: 'cover',
                                                objectPosition: 'top center'
                                            }
                                        }, void 0, false, {
                                            fileName: "[project]/app/tool/[slug]/ToolTabs.tsx",
                                            lineNumber: 90,
                                            columnNumber: 19
                                        }, this),
                                        /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("figcaption", {
                                            style: {
                                                padding: '8px 14px',
                                                borderTop: '1px solid var(--line)',
                                                fontFamily: 'JetBrains Mono, monospace',
                                                fontSize: 10,
                                                letterSpacing: '0.06em',
                                                textTransform: 'uppercase',
                                                color: '#8a8580',
                                                display: 'flex',
                                                justifyContent: 'space-between',
                                                gap: 12
                                            },
                                            children: [
                                                /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("span", {
                                                    children: [
                                                        t.name,
                                                        " · Website-Screenshot"
                                                    ]
                                                }, void 0, true, {
                                                    fileName: "[project]/app/tool/[slug]/ToolTabs.tsx",
                                                    lineNumber: 103,
                                                    columnNumber: 21
                                                }, this),
                                                /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("span", {
                                                    children: "1280 × 800"
                                                }, void 0, false, {
                                                    fileName: "[project]/app/tool/[slug]/ToolTabs.tsx",
                                                    lineNumber: 104,
                                                    columnNumber: 21
                                                }, this)
                                            ]
                                        }, void 0, true, {
                                            fileName: "[project]/app/tool/[slug]/ToolTabs.tsx",
                                            lineNumber: 95,
                                            columnNumber: 19
                                        }, this)
                                    ]
                                }, void 0, true, {
                                    fileName: "[project]/app/tool/[slug]/ToolTabs.tsx",
                                    lineNumber: 89,
                                    columnNumber: 17
                                }, this)
                            ]
                        }, void 0, true);
                    })(),
                    /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])(__TURBOPACK__imported__module__$5b$project$5d2f$components$2f$ui$2e$tsx__$5b$app$2d$client$5d$__$28$ecmascript$29$__["SectionLabel"], {
                        id: "pro-contra",
                        children: "Pro & Contra"
                    }, void 0, false, {
                        fileName: "[project]/app/tool/[slug]/ToolTabs.tsx",
                        lineNumber: 111,
                        columnNumber: 11
                    }, this),
                    /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                        className: "grid-pro-contra",
                        children: [
                            /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                                children: [
                                    /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                                        style: {
                                            fontFamily: 'JetBrains Mono, monospace',
                                            fontSize: 11,
                                            color: '#2F6A44',
                                            letterSpacing: '0.08em',
                                            textTransform: 'uppercase',
                                            marginBottom: 10
                                        },
                                        children: "+ Pro"
                                    }, void 0, false, {
                                        fileName: "[project]/app/tool/[slug]/ToolTabs.tsx",
                                        lineNumber: 114,
                                        columnNumber: 15
                                    }, this),
                                    /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("ul", {
                                        style: {
                                            paddingLeft: 16,
                                            margin: 0
                                        },
                                        children: t.pros.map((p, i)=>/*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("li", {
                                                style: {
                                                    fontSize: 14,
                                                    lineHeight: 1.65,
                                                    padding: '3px 0'
                                                },
                                                children: p
                                            }, i, false, {
                                                fileName: "[project]/app/tool/[slug]/ToolTabs.tsx",
                                                lineNumber: 116,
                                                columnNumber: 39
                                            }, this))
                                    }, void 0, false, {
                                        fileName: "[project]/app/tool/[slug]/ToolTabs.tsx",
                                        lineNumber: 115,
                                        columnNumber: 15
                                    }, this)
                                ]
                            }, void 0, true, {
                                fileName: "[project]/app/tool/[slug]/ToolTabs.tsx",
                                lineNumber: 113,
                                columnNumber: 13
                            }, this),
                            /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                                children: [
                                    /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                                        style: {
                                            fontFamily: 'JetBrains Mono, monospace',
                                            fontSize: 11,
                                            color: '#8A2F2F',
                                            letterSpacing: '0.08em',
                                            textTransform: 'uppercase',
                                            marginBottom: 10
                                        },
                                        children: "− Contra"
                                    }, void 0, false, {
                                        fileName: "[project]/app/tool/[slug]/ToolTabs.tsx",
                                        lineNumber: 120,
                                        columnNumber: 15
                                    }, this),
                                    /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("ul", {
                                        style: {
                                            paddingLeft: 16,
                                            margin: 0
                                        },
                                        children: t.cons.map((p, i)=>/*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("li", {
                                                style: {
                                                    fontSize: 14,
                                                    lineHeight: 1.65,
                                                    padding: '3px 0'
                                                },
                                                children: p
                                            }, i, false, {
                                                fileName: "[project]/app/tool/[slug]/ToolTabs.tsx",
                                                lineNumber: 122,
                                                columnNumber: 39
                                            }, this))
                                    }, void 0, false, {
                                        fileName: "[project]/app/tool/[slug]/ToolTabs.tsx",
                                        lineNumber: 121,
                                        columnNumber: 15
                                    }, this)
                                ]
                            }, void 0, true, {
                                fileName: "[project]/app/tool/[slug]/ToolTabs.tsx",
                                lineNumber: 119,
                                columnNumber: 13
                            }, this)
                        ]
                    }, void 0, true, {
                        fileName: "[project]/app/tool/[slug]/ToolTabs.tsx",
                        lineNumber: 112,
                        columnNumber: 11
                    }, this),
                    /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])(__TURBOPACK__imported__module__$5b$project$5d2f$components$2f$ui$2e$tsx__$5b$app$2d$client$5d$__$28$ecmascript$29$__["SectionLabel"], {
                        id: "anwendungsfaelle",
                        children: "Anwendungsfälle"
                    }, void 0, false, {
                        fileName: "[project]/app/tool/[slug]/ToolTabs.tsx",
                        lineNumber: 127,
                        columnNumber: 11
                    }, this),
                    /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                        style: {
                            display: 'flex',
                            gap: 8,
                            flexWrap: 'wrap'
                        },
                        children: t.usecases.map((u)=>/*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])(__TURBOPACK__imported__module__$5b$project$5d2f$components$2f$ui$2e$tsx__$5b$app$2d$client$5d$__$28$ecmascript$29$__["Chip"], {
                                accent: true,
                                children: u
                            }, u, false, {
                                fileName: "[project]/app/tool/[slug]/ToolTabs.tsx",
                                lineNumber: 129,
                                columnNumber: 36
                            }, this))
                    }, void 0, false, {
                        fileName: "[project]/app/tool/[slug]/ToolTabs.tsx",
                        lineNumber: 128,
                        columnNumber: 11
                    }, this),
                    /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])(__TURBOPACK__imported__module__$5b$project$5d2f$components$2f$ui$2e$tsx__$5b$app$2d$client$5d$__$28$ecmascript$29$__["SectionLabel"], {
                        id: "verwandte-tools",
                        children: "Verwandte Tools"
                    }, void 0, false, {
                        fileName: "[project]/app/tool/[slug]/ToolTabs.tsx",
                        lineNumber: 132,
                        columnNumber: 11
                    }, this),
                    /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                        className: "grid-3",
                        children: related.map((r)=>/*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])(__TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$client$2f$app$2d$dir$2f$link$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["default"], {
                                href: `/tool/${r.slug}`,
                                style: {
                                    padding: 16,
                                    border: '1px solid var(--line)',
                                    display: 'flex',
                                    flexDirection: 'column',
                                    gap: 8
                                },
                                children: [
                                    /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("h4", {
                                        style: {
                                            fontFamily: 'Fraunces, serif',
                                            fontSize: 18,
                                            fontWeight: 500,
                                            margin: 0
                                        },
                                        children: r.name
                                    }, void 0, false, {
                                        fileName: "[project]/app/tool/[slug]/ToolTabs.tsx",
                                        lineNumber: 136,
                                        columnNumber: 17
                                    }, this),
                                    /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("p", {
                                        style: {
                                            margin: 0,
                                            fontSize: 12,
                                            color: 'var(--ink)',
                                            lineHeight: 1.4
                                        },
                                        children: r.tagline
                                    }, void 0, false, {
                                        fileName: "[project]/app/tool/[slug]/ToolTabs.tsx",
                                        lineNumber: 137,
                                        columnNumber: 17
                                    }, this)
                                ]
                            }, r.slug, true, {
                                fileName: "[project]/app/tool/[slug]/ToolTabs.tsx",
                                lineNumber: 135,
                                columnNumber: 15
                            }, this))
                    }, void 0, false, {
                        fileName: "[project]/app/tool/[slug]/ToolTabs.tsx",
                        lineNumber: 133,
                        columnNumber: 11
                    }, this)
                ]
            }, void 0, true, {
                fileName: "[project]/app/tool/[slug]/ToolTabs.tsx",
                lineNumber: 60,
                columnNumber: 9
            }, this) : null
        ]
    }, void 0, true);
}
_s(ToolTabs, "sd2Z3hWD1yRaL0wwEI110+Kg+Yc=");
_c = ToolTabs;
var _c;
__turbopack_context__.k.register(_c, "ToolTabs");
if (typeof globalThis.$RefreshHelpers$ === 'object' && globalThis.$RefreshHelpers !== null) {
    __turbopack_context__.k.registerExports(__turbopack_context__.m, globalThis.$RefreshHelpers$);
}
}),
]);

//# sourceMappingURL=_0n_i1o2._.js.map