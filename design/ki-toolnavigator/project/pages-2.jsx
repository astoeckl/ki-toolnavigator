// KI-Toolnavigator — Tool-Detail, Vergleich, Artikel

function ToolPage({ nav, slug, toggleCompare, compareList }) {
  const { tools, categories } = window.KI_DATA;
  const t = tools.find(x => x.slug === slug) || tools[0];
  const cat = categories.find(c => c.slug === t.category);
  const related = tools.filter(x => x.category === t.category && x.slug !== t.slug).slice(0, 3);

  const [tab, setTab] = React.useState('uebersicht');
  const tabs = [
    { id: 'uebersicht', label: 'Übersicht' },
    { id: 'funktionen', label: 'Funktionen' },
    { id: 'preise',     label: 'Preise' },
    { id: 'community',  label: 'Community (14)' },
    { id: 'versionen',  label: 'Versionen' },
  ];

  return (
    <div>
      <Breadcrumb items={[
        { label: 'Start', to: { page: 'home' } },
        { label: 'Verzeichnis', to: { page: 'directory' } },
        { label: cat?.name, to: { page: 'category', slug: cat?.slug } },
        { label: t.name },
      ]} onNav={nav} />

      <div style={{ display: 'grid', gridTemplateColumns: '200px 1fr 300px', gap: 48 }}>
        {/* TOC links */}
        <aside style={{ position: 'sticky', top: 20, alignSelf: 'start' }}>
          <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#8a8580', letterSpacing: '0.08em', textTransform: 'uppercase', marginBottom: 14 }}>Inhalt</div>
          <ul style={{ listStyle: 'none', padding: 0, margin: 0, borderLeft: '1px solid var(--line)' }}>
            {['Zusammenfassung', 'Bildergalerie', 'Pro & Contra', 'Anwendungsfälle', 'Preise & Lizenzen', 'Kommentare', 'Verwandte Tools'].map((s, i) => (
              <li key={i} style={{ padding: '6px 14px', fontSize: 13, borderLeft: i === 0 ? '2px solid var(--accent)' : 'none', marginLeft: -1, color: i === 0 ? 'var(--accent)' : 'var(--ink)' }}>
                <a style={{ cursor: 'pointer', color: 'inherit' }}>{s}</a>
              </li>
            ))}
          </ul>

          <div style={{ marginTop: 28, fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#8a8580', letterSpacing: '0.08em', textTransform: 'uppercase', marginBottom: 12 }}>Aktionen</div>
          <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
            {['Bearbeiten', 'Diskussion', 'Verlauf', 'Beobachten', 'PDF-Export'].map(a => (
              <a key={a} style={{ cursor: 'pointer', fontSize: 12, color: 'var(--accent)', borderBottom: '1px dotted var(--accent)', display: 'inline-block', width: 'fit-content' }}>{a}</a>
            ))}
          </div>
        </aside>

        {/* Hauptinhalt */}
        <main>
          <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#8a8580', letterSpacing: '0.08em', textTransform: 'uppercase', marginBottom: 10 }}>
            {cat?.name} · {t.vendor}
          </div>
          <h1 style={{ fontFamily: 'Fraunces, serif', fontWeight: 400, fontSize: 72, letterSpacing: '-0.03em', margin: 0, lineHeight: 0.98 }}>{t.name}</h1>
          <p style={{ fontFamily: 'Fraunces, serif', fontSize: 22, lineHeight: 1.4, color: 'var(--ink)', marginTop: 18, maxWidth: 620, textWrap: 'pretty', fontStyle: 'italic' }}>{t.tagline}</p>

          <div style={{ marginTop: 28, display: 'flex', gap: 20, alignItems: 'center', flexWrap: 'wrap' }}>
            <Stars rating={t.rating} size={16} />
            <span style={{ fontFamily: 'Fraunces, serif', fontSize: 18 }}>{t.rating}</span>
            <span style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#8a8580' }}>aus {t.reviews} Bewertungen</span>
            <div style={{ width: 1, height: 20, background: 'var(--line)' }} />
            <Badge kind={t.dsgvo} />
            <span style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#8a8580' }}>· {t.origin}</span>
          </div>

          <div style={{ marginTop: 24, display: 'flex', gap: 10, flexWrap: 'wrap' }}>
            <Button variant="primary" onClick={() => window.open('https://' + t.slug + '.example', '_blank')}>Website besuchen ↗</Button>
            <Button variant="ghost" onClick={() => toggleCompare(t.slug)}>{compareList.includes(t.slug) ? '✓ im Vergleichskorb' : '+ Zum Vergleich hinzufügen'}</Button>
          </div>

          {/* Tabs */}
          <nav style={{ marginTop: 48, display: 'flex', gap: 0, borderBottom: '1px solid var(--line)' }}>
            {tabs.map(tb => (
              <a key={tb.id} onClick={() => setTab(tb.id)} style={{
                padding: '12px 18px', cursor: 'pointer',
                fontFamily: 'Inter Tight, sans-serif', fontSize: 13,
                color: tab === tb.id ? 'var(--ink-strong)' : '#8a8580',
                borderBottom: tab === tb.id ? '2px solid var(--accent)' : '2px solid transparent',
                marginBottom: -1, fontWeight: tab === tb.id ? 600 : 400,
              }}>{tb.label}</a>
            ))}
          </nav>

          {tab === 'uebersicht' && (
            <div style={{ paddingTop: 36 }}>
              {/* Drop-cap Fließtext im Editorial-Stil */}
              <p style={{ fontSize: 16, lineHeight: 1.75, color: 'var(--ink-strong)', margin: 0, textWrap: 'pretty' }}>
                <span style={{ float: 'left', fontFamily: 'Fraunces, serif', fontSize: 72, lineHeight: 0.9, marginRight: 12, marginTop: 4, color: 'var(--accent)' }}>{t.name[0]}</span>
                {t.name} von {t.vendor} zählt zu den relevantesten Werkzeugen im Bereich <i>{cat?.name}</i>. Seit dem Start {new Date(t.launched).toLocaleDateString('de-DE', { month: 'long', year: 'numeric' })} hat sich das Produkt zu einem festen Bestandteil vieler Workflows entwickelt — insbesondere durch die schnelle Weiterentwicklung und die Anbindung an etablierte Arbeitsumgebungen. Das letzte Update datiert vom {new Date(t.lastUpdated).toLocaleDateString('de-DE')}.
              </p>
              <p style={{ fontSize: 16, lineHeight: 1.75, color: 'var(--ink)', marginTop: 18, textWrap: 'pretty' }}>
                Nutzer schätzen vor allem die <b>Kernkompetenz</b> im Bereich {t.usecases[0]?.toLowerCase()}. Gleichzeitig sind die Grenzen bekannt: {t.cons[0]?.toLowerCase()} stellt für europäische Organisationen teils eine Hürde dar. Im direkten Vergleich mit den Wettbewerbern dieser Kategorie positioniert sich {t.name} durch sein Ökosystem und die Breite der Integrationen.
              </p>

              <SectionLabel>Bildergalerie</SectionLabel>
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 12 }}>
                <Thumb name={t.name + ' UI'} slug={t.slug + '-1'} aspect="4/3" label="UI · Hauptansicht" />
                <Thumb name={t.name + ' Ansicht 2'} slug={t.slug + '-2'} aspect="4/3" label="UI · Einstellungen" />
                <Thumb name={t.name + ' Ansicht 3'} slug={t.slug + '-3'} aspect="4/3" label="UI · API-Playground" />
              </div>

              <SectionLabel>Pro & Contra</SectionLabel>
              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 32 }}>
                <div>
                  <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#2F6A44', letterSpacing: '0.08em', textTransform: 'uppercase', marginBottom: 10 }}>+ Pro</div>
                  <ul style={{ paddingLeft: 16, margin: 0 }}>
                    {t.pros.map((p, i) => <li key={i} style={{ fontSize: 14, lineHeight: 1.65, padding: '3px 0' }}>{p}</li>)}
                  </ul>
                </div>
                <div>
                  <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#8A2F2F', letterSpacing: '0.08em', textTransform: 'uppercase', marginBottom: 10 }}>− Contra</div>
                  <ul style={{ paddingLeft: 16, margin: 0 }}>
                    {t.cons.map((p, i) => <li key={i} style={{ fontSize: 14, lineHeight: 1.65, padding: '3px 0' }}>{p}</li>)}
                  </ul>
                </div>
              </div>

              <SectionLabel>Anwendungsfälle</SectionLabel>
              <div style={{ display: 'flex', gap: 8, flexWrap: 'wrap' }}>
                {t.usecases.map(u => <Chip key={u} accent>{u}</Chip>)}
              </div>

              <SectionLabel>Community-Kommentare</SectionLabel>
              <ul style={{ listStyle: 'none', padding: 0, margin: 0 }}>
                {[
                  { user: 'Martina K.', role: 'Produktmanagerin', days: 3, text: 'Für unser Team der tägliche Begleiter bei Recherche und Textentwürfen. Die API-Integration in unsere eigenen Tools war in zwei Tagen erledigt.' },
                  { user: 'Jens W.',    role: 'Entwickler',        days: 8, text: 'Solide, aber die Limits im Pro-Plan sind bei größeren Projekten schnell erreicht. Für kleinere Teams trotzdem die Empfehlung.' },
                  { user: 'S. Albrecht', role: 'Agentur',           days: 14, text: 'Wir nutzen es hauptsächlich für Briefings und erste Textentwürfe. Das Ergebnis ist stark vom Prompt abhängig — mit Prompt-Bibliothek steigt die Qualität deutlich.' },
                ].map((c, i) => (
                  <li key={i} style={{ padding: '18px 0', borderBottom: '1px solid var(--line)' }}>
                    <div style={{ display: 'flex', gap: 12, alignItems: 'baseline', marginBottom: 6 }}>
                      <b style={{ fontFamily: 'Fraunces, serif', fontSize: 16 }}>{c.user}</b>
                      <span style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 10, color: '#8a8580', letterSpacing: '0.04em', textTransform: 'uppercase' }}>{c.role} · vor {c.days} Tagen</span>
                    </div>
                    <p style={{ margin: 0, fontSize: 14, lineHeight: 1.6, color: 'var(--ink)' }}>{c.text}</p>
                  </li>
                ))}
              </ul>
              <a style={{ display: 'inline-block', marginTop: 14, fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: 'var(--accent)', letterSpacing: '0.06em', textTransform: 'uppercase', cursor: 'pointer', borderBottom: '1px solid var(--accent)' }}>Alle 14 Kommentare ansehen →</a>

              <SectionLabel>Verwandte Tools</SectionLabel>
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 20 }}>
                {related.map(r => (
                  <a key={r.slug} onClick={() => nav({ page: 'tool', slug: r.slug })} style={{ cursor: 'pointer', padding: 16, border: '1px solid var(--line)', display: 'flex', flexDirection: 'column', gap: 8 }}>
                    <h4 style={{ fontFamily: 'Fraunces, serif', fontSize: 18, fontWeight: 500, margin: 0 }}>{r.name}</h4>
                    <p style={{ margin: 0, fontSize: 12, color: 'var(--ink)', lineHeight: 1.4 }}>{r.tagline}</p>
                    <Stars rating={r.rating} />
                  </a>
                ))}
              </div>
            </div>
          )}

          {tab !== 'uebersicht' && (
            <div style={{ paddingTop: 40, textAlign: 'center', color: '#8a8580', fontSize: 14, fontStyle: 'italic', fontFamily: 'Fraunces, serif' }}>
              Inhalt für „{tabs.find(x => x.id === tab).label}" in Arbeit — Tab umschalten auf <a onClick={() => setTab('uebersicht')} style={{ color: 'var(--accent)', borderBottom: '1px dotted var(--accent)', cursor: 'pointer' }}>Übersicht</a>.
            </div>
          )}
        </main>

        {/* Infobox rechts — Wiki-Steckbrief */}
        <aside>
          <div style={{ border: '1px solid var(--ink-strong)', padding: 0 }}>
            <div style={{ padding: '14px 18px', borderBottom: '1px solid var(--ink-strong)', background: 'var(--ink-strong)', color: 'var(--bg)' }}>
              <div style={{ fontFamily: 'Fraunces, serif', fontSize: 18, fontWeight: 500 }}>{t.name}</div>
              <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 10, letterSpacing: '0.06em', color: 'rgba(255,255,255,0.7)', textTransform: 'uppercase', marginTop: 2 }}>Tool-Steckbrief</div>
            </div>
            <div style={{ padding: 18 }}>
              <Thumb name={t.name} slug={t.slug + '-info'} aspect="4/3" label="Produkt · Logo" />
              <div style={{ marginTop: 14 }}>
                <DataRow label="Anbieter" value={t.vendor} />
                <DataRow label="Kategorie" value={cat?.name} />
                <DataRow label="Herkunft" value={t.origin} mono />
                <DataRow label="Preis" value={t.price} />
                <DataRow label="API" value={t.api ? 'Ja' : 'Nein'} mono />
                <DataRow label="DSGVO" value={t.dsgvo === 'ja' ? 'Konform' : t.dsgvo === 'bedingt' ? 'Bedingt' : 'Kein Nachweis'} />
                <DataRow label="Launch" value={new Date(t.launched).toLocaleDateString('de-DE')} mono />
                <DataRow label="Aktualisiert" value={new Date(t.lastUpdated).toLocaleDateString('de-DE')} mono />
                <DataRow label="Bewertung" value={t.rating + ' / 5'} mono />
              </div>
            </div>
          </div>

          <div style={{ marginTop: 20, fontFamily: 'JetBrains Mono, monospace', fontSize: 10, color: '#8a8580', letterSpacing: '0.04em', textTransform: 'uppercase', lineHeight: 1.6 }}>
            Artikel zuletzt bearbeitet<br />
            am {new Date(t.lastUpdated).toLocaleDateString('de-DE')} durch Redaktion<br />
            <a style={{ color: 'var(--accent)', borderBottom: '1px dotted var(--accent)', cursor: 'pointer' }}>Verlauf ansehen</a>
          </div>
        </aside>
      </div>
    </div>
  );
}

function ComparePage({ nav, compareList, toggleCompare }) {
  const { tools } = window.KI_DATA;
  const items = compareList.length
    ? compareList.map(s => tools.find(t => t.slug === s)).filter(Boolean)
    : [tools[0], tools[1], tools[3]]; // Default-Vergleich

  const rows = [
    { label: 'Anbieter',    get: t => t.vendor, mono: true },
    { label: 'Herkunft',    get: t => t.origin, mono: true },
    { label: 'Kategorie',   get: t => window.KI_DATA.categories.find(c => c.slug === t.category)?.name },
    { label: 'Preis',       get: t => t.price },
    { label: 'API',         get: t => t.api ? 'Ja' : 'Nein', mono: true },
    { label: 'DSGVO',       get: t => <Badge kind={t.dsgvo} /> },
    { label: 'Bewertung',   get: t => <span><Stars rating={t.rating} /> <span style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, marginLeft: 6 }}>{t.rating}</span></span> },
    { label: 'Launch',      get: t => new Date(t.launched).toLocaleDateString('de-DE'), mono: true },
    { label: 'Aktualisiert', get: t => new Date(t.lastUpdated).toLocaleDateString('de-DE'), mono: true },
  ];

  return (
    <div>
      <Breadcrumb items={[{ label: 'Start', to: { page: 'home' } }, { label: 'Verzeichnis', to: { page: 'directory' } }, { label: 'Vergleich' }]} onNav={nav} />

      <div style={{ borderBottom: '1px solid var(--line)', paddingBottom: 32, marginBottom: 40 }}>
        <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#8a8580', letterSpacing: '0.08em', textTransform: 'uppercase', marginBottom: 12 }}>Direktvergleich</div>
        <h1 style={{ fontFamily: 'Fraunces, serif', fontWeight: 400, fontSize: 64, letterSpacing: '-0.025em', margin: 0, lineHeight: 1, textWrap: 'balance' }}>
          {items.map(t => t.name).join(' vs. ')}
        </h1>
        <p style={{ fontFamily: 'Fraunces, serif', fontSize: 18, lineHeight: 1.5, color: 'var(--ink)', marginTop: 16, maxWidth: 720, textWrap: 'pretty' }}>
          Tabellarische Gegenüberstellung der wichtigsten Merkmale — gepflegt von der Redaktion am {new Date().toLocaleDateString('de-DE')}.
        </p>
      </div>

      <div style={{ overflowX: 'auto', border: '1px solid var(--line)' }}>
        <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: 13 }}>
          <thead>
            <tr>
              <th style={{ padding: 16, textAlign: 'left', borderBottom: '1px solid var(--ink-strong)', width: 180, fontFamily: 'JetBrains Mono, monospace', fontSize: 10, letterSpacing: '0.08em', textTransform: 'uppercase', color: '#8a8580', verticalAlign: 'bottom' }}>Merkmal</th>
              {items.map(t => (
                <th key={t.slug} style={{ padding: 16, textAlign: 'left', borderBottom: '1px solid var(--ink-strong)', verticalAlign: 'bottom', borderLeft: '1px solid var(--line)' }}>
                  <Thumb name={t.name} slug={t.slug + '-cmp'} aspect="4/3" label="" />
                  <h3 style={{ fontFamily: 'Fraunces, serif', fontSize: 22, fontWeight: 500, margin: '12px 0 4px', letterSpacing: '-0.01em' }}>
                    <a onClick={() => nav({ page: 'tool', slug: t.slug })} style={{ cursor: 'pointer', color: 'inherit' }}>{t.name}</a>
                  </h3>
                  <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 10, color: '#8a8580', letterSpacing: '0.04em', textTransform: 'uppercase', marginBottom: 8 }}>{t.vendor}</div>
                  <a onClick={() => toggleCompare(t.slug)} style={{ cursor: 'pointer', fontSize: 11, color: '#8a8580', fontFamily: 'JetBrains Mono, monospace', borderBottom: '1px dotted #8a8580', letterSpacing: '0.04em', textTransform: 'uppercase' }}>× Entfernen</a>
                </th>
              ))}
              {items.length < 4 && (
                <th style={{ padding: 16, borderBottom: '1px solid var(--ink-strong)', borderLeft: '1px solid var(--line)', verticalAlign: 'middle', background: 'var(--bg-alt)', width: 180 }}>
                  <a onClick={() => nav({ page: 'directory' })} style={{ cursor: 'pointer', fontFamily: 'Fraunces, serif', fontSize: 16, fontStyle: 'italic', color: 'var(--accent)' }}>+ Tool hinzufügen</a>
                </th>
              )}
            </tr>
          </thead>
          <tbody>
            {rows.map(r => (
              <tr key={r.label}>
                <td style={{ padding: '14px 16px', borderBottom: '1px dotted var(--line)', fontFamily: 'JetBrains Mono, monospace', fontSize: 11, letterSpacing: '0.04em', textTransform: 'uppercase', color: '#8a8580' }}>{r.label}</td>
                {items.map(t => (
                  <td key={t.slug} style={{ padding: '14px 16px', borderBottom: '1px dotted var(--line)', borderLeft: '1px solid var(--line)', fontFamily: r.mono ? 'JetBrains Mono, monospace' : 'Inter Tight, sans-serif', color: 'var(--ink-strong)' }}>
                    {r.get(t)}
                  </td>
                ))}
                {items.length < 4 && <td style={{ borderBottom: '1px dotted var(--line)', borderLeft: '1px solid var(--line)', background: 'var(--bg-alt)' }} />}
              </tr>
            ))}
            <tr>
              <td style={{ padding: '14px 16px', borderBottom: '1px dotted var(--line)', fontFamily: 'JetBrains Mono, monospace', fontSize: 11, letterSpacing: '0.04em', textTransform: 'uppercase', color: '#8a8580', verticalAlign: 'top' }}>Stärken</td>
              {items.map(t => (
                <td key={t.slug} style={{ padding: '14px 16px', borderBottom: '1px dotted var(--line)', borderLeft: '1px solid var(--line)', verticalAlign: 'top' }}>
                  <ul style={{ padding: 0, margin: 0, listStyle: 'none' }}>
                    {t.pros.map((p, i) => <li key={i} style={{ fontSize: 12, lineHeight: 1.5, padding: '2px 0', color: 'var(--ink)' }}>+ {p}</li>)}
                  </ul>
                </td>
              ))}
              {items.length < 4 && <td style={{ borderBottom: '1px dotted var(--line)', borderLeft: '1px solid var(--line)', background: 'var(--bg-alt)' }} />}
            </tr>
            <tr>
              <td style={{ padding: '14px 16px', fontFamily: 'JetBrains Mono, monospace', fontSize: 11, letterSpacing: '0.04em', textTransform: 'uppercase', color: '#8a8580', verticalAlign: 'top' }}>Schwächen</td>
              {items.map(t => (
                <td key={t.slug} style={{ padding: '14px 16px', borderLeft: '1px solid var(--line)', verticalAlign: 'top' }}>
                  <ul style={{ padding: 0, margin: 0, listStyle: 'none' }}>
                    {t.cons.map((p, i) => <li key={i} style={{ fontSize: 12, lineHeight: 1.5, padding: '2px 0', color: 'var(--ink)' }}>− {p}</li>)}
                  </ul>
                </td>
              ))}
              {items.length < 4 && <td style={{ borderLeft: '1px solid var(--line)', background: 'var(--bg-alt)' }} />}
            </tr>
          </tbody>
        </table>
      </div>

      <div style={{ marginTop: 28, fontFamily: 'Fraunces, serif', fontSize: 16, lineHeight: 1.6, color: 'var(--ink)', fontStyle: 'italic', maxWidth: 780, textWrap: 'pretty' }}>
        <b style={{ color: 'var(--ink-strong)', fontStyle: 'normal' }}>Redaktionelle Einschätzung.</b> Für deutschsprachige Unternehmen mit hohen Datenschutz-Anforderungen ist unter den hier verglichenen Tools besonders <a onClick={() => nav({ page: 'tool', slug: 'mistral' })} style={{ color: 'var(--accent)', fontStyle: 'normal', cursor: 'pointer', borderBottom: '1px solid var(--accent)' }}>Le Chat</a> interessant. Wer das breiteste Ökosystem sucht, greift weiterhin zu ChatGPT.
      </div>
    </div>
  );
}

function ArticlePage({ nav, slug }) {
  const { articles } = window.KI_DATA;
  const a = articles.find(x => x.slug === slug) || articles[0];

  return (
    <div>
      <Breadcrumb items={[{ label: 'Start', to: { page: 'home' } }, { label: 'Artikel' }, { label: a.title }]} onNav={nav} />

      <div style={{ display: 'grid', gridTemplateColumns: '220px 1fr 260px', gap: 48 }}>
        {/* TOC */}
        <aside style={{ position: 'sticky', top: 20, alignSelf: 'start' }}>
          <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#8a8580', letterSpacing: '0.08em', textTransform: 'uppercase', marginBottom: 14 }}>Inhaltsverzeichnis</div>
          <ul style={{ listStyle: 'none', padding: 0, margin: 0, borderLeft: '1px solid var(--line)' }}>
            {a.toc.map((s, i) => (
              <li key={i} style={{ padding: '6px 14px', fontSize: 13, borderLeft: i === 0 ? '2px solid var(--accent)' : 'none', marginLeft: -1, color: i === 0 ? 'var(--accent)' : 'var(--ink)' }}>
                <span style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 10, marginRight: 8, color: '#8a8580' }}>{String(i + 1).padStart(2, '0')}</span>
                <a style={{ cursor: 'pointer', color: 'inherit' }}>{s}</a>
              </li>
            ))}
          </ul>
        </aside>

        {/* Artikelkörper */}
        <article style={{ maxWidth: 680 }}>
          <Chip>{a.category}</Chip>
          <h1 style={{ fontFamily: 'Fraunces, serif', fontWeight: 400, fontSize: 64, letterSpacing: '-0.025em', margin: '18px 0 18px', lineHeight: 1, textWrap: 'balance' }}>{a.title}</h1>
          <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#8a8580', letterSpacing: '0.04em', textTransform: 'uppercase' }}>
            {a.author} · {new Date(a.date).toLocaleDateString('de-DE', { day: '2-digit', month: 'long', year: 'numeric' })} · {a.readTime} Min. Lesezeit
          </div>

          <div style={{ margin: '32px 0', border: '1px solid var(--line)', padding: 0 }}>
            <Thumb name={a.title} slug={a.slug} aspect="16/9" label="Illustration · Aufmacherbild" />
          </div>

          <p style={{ fontFamily: 'Fraunces, serif', fontSize: 22, lineHeight: 1.5, color: 'var(--ink-strong)', fontStyle: 'italic', margin: '0 0 28px', textWrap: 'pretty' }}>
            Künstliche Intelligenz ist kein neues Phänomen — aber seit der Verbreitung großer Sprachmodelle ab 2022 ist das Thema in den Alltag von Millionen Menschen eingedrungen. Dieser Artikel ordnet ein.
          </p>

          <h2 id="h-1" style={{ fontFamily: 'Fraunces, serif', fontSize: 28, fontWeight: 500, letterSpacing: '-0.015em', margin: '40px 0 14px' }}>Definition</h2>
          <p style={{ fontSize: 16, lineHeight: 1.75, color: 'var(--ink-strong)', textWrap: 'pretty' }}>
            <span style={{ float: 'left', fontFamily: 'Fraunces, serif', fontSize: 72, lineHeight: 0.9, marginRight: 12, marginTop: 4, color: 'var(--accent)' }}>K</span>ünstliche Intelligenz bezeichnet Systeme, die Aufgaben lösen, die bislang menschliche Intelligenz erforderten. Der Begriff umfasst eine Vielzahl von Teildisziplinen — von regelbasierten Expertensystemen über maschinelles Lernen bis hin zu heutigen generativen Modellen. Eine allgemein akzeptierte Definition existiert nicht; in der Praxis überlappen sich technische und gesellschaftliche Perspektiven.
          </p>
          <p style={{ fontSize: 16, lineHeight: 1.75, color: 'var(--ink)', textWrap: 'pretty' }}>
            Der Mathematiker John McCarthy prägte den Begriff <i>Artificial Intelligence</i> 1955 für den Dartmouth-Workshop im Sommer 1956 — die Geburtsstunde des Forschungsfelds.
          </p>

          {/* Pullquote */}
          <blockquote style={{ margin: '32px 0', padding: '24px 32px', borderLeft: '2px solid var(--accent)', fontFamily: 'Fraunces, serif', fontSize: 26, lineHeight: 1.35, fontStyle: 'italic', color: 'var(--ink-strong)', textWrap: 'balance' }}>
            „Jede Maschine, deren Verhalten ausreichend komplex ist, erscheint ihrem Betrachter als intelligent."
            <div style={{ marginTop: 14, fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#8a8580', letterSpacing: '0.06em', textTransform: 'uppercase', fontStyle: 'normal' }}>— Arthur C. Clarke, zugeschrieben</div>
          </blockquote>

          <h2 id="h-2" style={{ fontFamily: 'Fraunces, serif', fontSize: 28, fontWeight: 500, letterSpacing: '-0.015em', margin: '40px 0 14px' }}>Teilgebiete</h2>
          <p style={{ fontSize: 16, lineHeight: 1.75, color: 'var(--ink-strong)', textWrap: 'pretty' }}>
            Das Feld gliedert sich grob in symbolische KI, subsymbolische Verfahren und hybride Ansätze. Für die heutige öffentliche Wahrnehmung am relevantesten sind <a onClick={() => nav({ page: 'article', slug: 'llm-vergleich' })} style={{ color: 'var(--accent)', borderBottom: '1px solid var(--accent)', cursor: 'pointer' }}>große Sprachmodelle</a> sowie generative Modelle für Bild, Audio und Video.
          </p>

          <h2 id="h-3" style={{ fontFamily: 'Fraunces, serif', fontSize: 28, fontWeight: 500, letterSpacing: '-0.015em', margin: '40px 0 14px' }}>Heutige Anwendungen</h2>
          <p style={{ fontSize: 16, lineHeight: 1.75, color: 'var(--ink-strong)', textWrap: 'pretty' }}>
            Von Chat-Assistenten über Programmier-Copiloten bis zu Bildgeneratoren ist KI in Produkten angekommen, die täglich hunderte Millionen Menschen nutzen. Das <a onClick={() => nav({ page: 'directory' })} style={{ color: 'var(--accent)', borderBottom: '1px solid var(--accent)', cursor: 'pointer' }}>Verzeichnis</a> dieser Seite listet die relevanten Werkzeuge — nach Kategorie und DSGVO-Status sortierbar.
          </p>

          {/* Footer */}
          <div style={{ marginTop: 56, paddingTop: 20, borderTop: '1px solid var(--line)', display: 'flex', gap: 16, flexWrap: 'wrap', alignItems: 'center' }}>
            <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#8a8580', letterSpacing: '0.08em', textTransform: 'uppercase' }}>Verweise:</div>
            <Chip>Grundlagen</Chip>
            <Chip>Sprachmodelle</Chip>
            <Chip>DSGVO</Chip>
            <Chip>Geschichte</Chip>
          </div>
        </article>

        {/* Meta-Leiste */}
        <aside>
          <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#8a8580', letterSpacing: '0.08em', textTransform: 'uppercase', marginBottom: 14 }}>Weitere Artikel</div>
          <ul style={{ listStyle: 'none', padding: 0, margin: 0 }}>
            {articles.filter(x => x.slug !== a.slug).slice(0, 4).map(x => (
              <li key={x.slug} style={{ padding: '14px 0', borderBottom: '1px dotted var(--line)' }}>
                <a onClick={() => nav({ page: 'article', slug: x.slug })} style={{ cursor: 'pointer' }}>
                  <h4 style={{ fontFamily: 'Fraunces, serif', fontSize: 16, fontWeight: 500, margin: 0, letterSpacing: '-0.01em', lineHeight: 1.25 }}>{x.title}</h4>
                  <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 10, color: '#8a8580', letterSpacing: '0.04em', textTransform: 'uppercase', marginTop: 4 }}>{x.author} · {x.readTime} Min.</div>
                </a>
              </li>
            ))}
          </ul>
        </aside>
      </div>
    </div>
  );
}

Object.assign(window, { ToolPage, ComparePage, ArticlePage });
