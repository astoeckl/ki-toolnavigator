// KI-Toolnavigator — Seiten: Home, Verzeichnis, Kategorie

function HomePage({ nav, search, setSearch }) {
  const { tools, categories, articles, recentChanges } = window.KI_DATA;
  const featured = tools.slice(0, 3);
  const newest = tools.slice(-3).reverse();

  return (
    <div>
      {/* Hero — Editorial */}
      <section style={{ padding: '72px 0 56px', borderBottom: '1px solid var(--line)' }}>
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 380px', gap: 72, alignItems: 'end' }}>
          <div>
            <div style={{
              fontFamily: 'JetBrains Mono, monospace',
              fontSize: 11, letterSpacing: '0.08em',
              color: '#8a8580', textTransform: 'uppercase',
              marginBottom: 20,
            }}>Ausgabe Nr. 47 · {new Date().toLocaleDateString('de-DE', { day: '2-digit', month: 'long', year: 'numeric' })}</div>
            <h1 style={{
              fontFamily: 'Fraunces, Georgia, serif',
              fontWeight: 400, fontSize: 'clamp(48px, 6vw, 84px)',
              lineHeight: 0.98, letterSpacing: '-0.025em',
              margin: 0, color: 'var(--ink-strong)',
              textWrap: 'balance',
            }}>
              Das kuratierte<br />
              <span style={{ fontStyle: 'italic' }}>Verzeichnis</span> für<br />
              Künstliche Intelligenz.
            </h1>
            <p style={{
              fontFamily: 'Fraunces, Georgia, serif',
              fontSize: 20, lineHeight: 1.5,
              color: 'var(--ink)', marginTop: 32, maxWidth: 620,
              textWrap: 'pretty',
            }}>
              Über <b>{tools.length * 18}</b> KI-Tools, redaktionell geprüft, verglichen und erklärt — auf Deutsch, nach DSGVO-Kriterien sortierbar, von einer Community aus <b>1.240</b> Mitwirkenden gepflegt.
            </p>
            <div style={{ marginTop: 36, display: 'flex', gap: 12, alignItems: 'center' }}>
              <div style={{
                display: 'flex', alignItems: 'center',
                border: '1px solid var(--ink-strong)',
                padding: '2px', flex: '0 1 460px',
              }}>
                <input
                  value={search}
                  onChange={e => setSearch(e.target.value)}
                  onKeyDown={e => { if (e.key === 'Enter') nav({ page: 'directory' }); }}
                  placeholder="Tool, Kategorie oder Use-Case suchen …"
                  style={{
                    flex: 1, padding: '12px 14px', border: 'none', outline: 'none',
                    fontFamily: 'Inter Tight, sans-serif', fontSize: 14,
                    background: 'transparent', color: 'var(--ink-strong)',
                  }}
                />
                <Button variant="primary" onClick={() => nav({ page: 'directory' })}>Suchen →</Button>
              </div>
            </div>
            <div style={{ display: 'flex', gap: 14, marginTop: 20, flexWrap: 'wrap' }}>
              <span style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#8a8580', textTransform: 'uppercase', letterSpacing: '0.06em', paddingTop: 4 }}>Populär:</span>
              {['ChatGPT', 'Claude', 'Midjourney', 'DSGVO', 'Coding-Assistent'].map(t => (
                <Chip key={t} onClick={() => { setSearch(t); nav({ page: 'directory' }); }}>{t}</Chip>
              ))}
            </div>
          </div>

          {/* Rechts: Info-Kasten im Zeitungsstil */}
          <aside style={{ borderLeft: '1px solid var(--line)', paddingLeft: 32 }}>
            <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, letterSpacing: '0.08em', color: '#8a8580', textTransform: 'uppercase', marginBottom: 14 }}>In Zahlen</div>
            {[
              ['Tools gelistet', '252'],
              ['Kategorien', '9'],
              ['Artikel', '184'],
              ['Redaktionelle Updates', '38 / Monat'],
              ['DSGVO-konform', '62 Tools'],
              ['EU-Anbieter', '31 Tools'],
            ].map(([k, v]) => (
              <div key={k} style={{ display: 'flex', justifyContent: 'space-between', padding: '8px 0', borderBottom: '1px dotted var(--line)', fontSize: 13 }}>
                <span style={{ color: 'var(--ink)' }}>{k}</span>
                <span style={{ fontFamily: 'Fraunces, serif', color: 'var(--ink-strong)', fontSize: 16 }}>{v}</span>
              </div>
            ))}
          </aside>
        </div>
      </section>

      {/* Kategorien */}
      <section style={{ padding: '56px 0', borderBottom: '1px solid var(--line)' }}>
        <SectionLabel num="01">Kategorien</SectionLabel>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '1px', background: 'var(--line)', border: '1px solid var(--line)' }}>
          {categories.map(c => (
            <a key={c.slug} onClick={() => nav({ page: 'category', slug: c.slug })} style={{
              padding: '24px 24px 22px', background: 'var(--bg)', cursor: 'pointer',
              display: 'flex', flexDirection: 'column', gap: 10,
              transition: 'background 0.15s',
            }} onMouseEnter={e => e.currentTarget.style.background = 'var(--bg-alt)'} onMouseLeave={e => e.currentTarget.style.background = 'var(--bg)'}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'baseline' }}>
                <h3 style={{ fontFamily: 'Fraunces, serif', fontSize: 20, fontWeight: 500, margin: 0, letterSpacing: '-0.01em' }}>{c.name}</h3>
                <span style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: 'var(--accent)' }}>{c.count}</span>
              </div>
              <p style={{ margin: 0, fontSize: 13, color: 'var(--ink)', lineHeight: 1.5 }}>{c.desc}</p>
            </a>
          ))}
        </div>
      </section>

      {/* Featured + Recent Changes */}
      <section style={{ padding: '56px 0', borderBottom: '1px solid var(--line)', display: 'grid', gridTemplateColumns: '1fr 340px', gap: 56 }}>
        <div>
          <SectionLabel num="02">Redaktionsempfehlung</SectionLabel>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 24 }}>
            {featured.map(t => (
              <a key={t.slug} onClick={() => nav({ page: 'tool', slug: t.slug })} style={{ cursor: 'pointer', display: 'flex', flexDirection: 'column', gap: 12 }}>
                <Thumb name={t.name} slug={t.slug} aspect="3/2" />
                <div style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
                  <Chip>{window.KI_DATA.categories.find(c => c.slug === t.category)?.name}</Chip>
                  <Stars rating={t.rating} />
                </div>
                <h4 style={{ fontFamily: 'Fraunces, serif', fontSize: 22, fontWeight: 500, margin: 0, letterSpacing: '-0.01em' }}>{t.name}</h4>
                <p style={{ margin: 0, fontSize: 13, lineHeight: 1.5, color: 'var(--ink)' }}>{t.tagline}</p>
              </a>
            ))}
          </div>
        </div>

        {/* Wiki-typisches "Letzte Änderungen" */}
        <aside style={{ borderLeft: '1px solid var(--line)', paddingLeft: 32 }}>
          <div style={{
            fontFamily: 'JetBrains Mono, monospace', fontSize: 11,
            letterSpacing: '0.08em', color: '#8a8580', textTransform: 'uppercase',
            marginBottom: 18,
          }}>Letzte Änderungen</div>
          <ul style={{ listStyle: 'none', padding: 0, margin: 0 }}>
            {recentChanges.map((r, i) => (
              <li key={i} style={{ padding: '10px 0', borderBottom: '1px dotted var(--line)', fontSize: 13, lineHeight: 1.5 }}>
                <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 10, color: '#8a8580', letterSpacing: '0.04em' }}>{r.time}</div>
                <div style={{ marginTop: 2 }}>
                  <b style={{ color: 'var(--ink-strong)' }}>{r.user}</b> {r.action}{' '}
                  <a style={{ color: 'var(--accent)', cursor: 'pointer', borderBottom: '1px dotted var(--accent)' }}>{r.target}</a>
                  <span style={{ color: 'var(--ink)' }}> — {r.detail}</span>
                </div>
              </li>
            ))}
          </ul>
          <a onClick={() => nav({ page: 'directory' })} style={{
            display: 'inline-block', marginTop: 16,
            fontFamily: 'JetBrains Mono, monospace', fontSize: 11,
            color: 'var(--accent)', letterSpacing: '0.06em',
            textTransform: 'uppercase', cursor: 'pointer',
            borderBottom: '1px solid var(--accent)',
          }}>Alle Änderungen →</a>
        </aside>
      </section>

      {/* Lange Artikel im Editorial-Stil */}
      <section style={{ padding: '56px 0 88px' }}>
        <SectionLabel num="03">Aus der Redaktion</SectionLabel>
        <div style={{ display: 'grid', gridTemplateColumns: '2fr 1fr', gap: 56 }}>
          {/* Hauptartikel */}
          <a onClick={() => nav({ page: 'article', slug: articles[0].slug })} style={{ cursor: 'pointer', display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 28, alignItems: 'start' }}>
            <Thumb name={articles[0].title} slug={articles[0].slug} aspect="4/3" label="Titelbild · Illustration" />
            <div>
              <Chip>{articles[0].category}</Chip>
              <h3 style={{ fontFamily: 'Fraunces, serif', fontSize: 34, fontWeight: 400, margin: '14px 0 14px', letterSpacing: '-0.02em', lineHeight: 1.08, textWrap: 'balance' }}>{articles[0].title}</h3>
              <p style={{ fontSize: 14, lineHeight: 1.6, color: 'var(--ink)', margin: 0 }}>
                Eine kompakte Einführung in die Grundlagen, Teilgebiete und heutigen Anwendungsfelder der Künstlichen Intelligenz — mit besonderem Blick auf den europäischen Kontext.
              </p>
              <div style={{ marginTop: 16, fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#8a8580', letterSpacing: '0.04em', textTransform: 'uppercase' }}>
                {articles[0].author} · {articles[0].readTime} Min. Lesezeit
              </div>
            </div>
          </a>
          {/* Weitere */}
          <ul style={{ listStyle: 'none', padding: 0, margin: 0 }}>
            {articles.slice(1, 5).map(a => (
              <li key={a.slug} style={{ padding: '18px 0', borderBottom: '1px solid var(--line)' }}>
                <a onClick={() => nav({ page: 'article', slug: a.slug })} style={{ cursor: 'pointer' }}>
                  <Chip>{a.category}</Chip>
                  <h4 style={{ fontFamily: 'Fraunces, serif', fontSize: 19, fontWeight: 500, margin: '8px 0 6px', letterSpacing: '-0.01em', lineHeight: 1.2, textWrap: 'balance' }}>{a.title}</h4>
                  <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 10, color: '#8a8580', letterSpacing: '0.04em', textTransform: 'uppercase' }}>{a.author} · {a.readTime} Min.</div>
                </a>
              </li>
            ))}
          </ul>
        </div>
      </section>
    </div>
  );
}

function DirectoryPage({ nav, search, setSearch, compareList, toggleCompare }) {
  const { tools, categories } = window.KI_DATA;
  const [view, setView] = React.useState('list');
  const [catFilter, setCatFilter] = React.useState('all');
  const [dsgvoOnly, setDsgvoOnly] = React.useState(false);
  const [euOnly, setEuOnly] = React.useState(false);
  const [sort, setSort] = React.useState('rating');

  const filtered = tools
    .filter(t => !search || (t.name + t.tagline + t.vendor).toLowerCase().includes(search.toLowerCase()))
    .filter(t => catFilter === 'all' || t.category === catFilter)
    .filter(t => !dsgvoOnly || t.dsgvo === 'ja')
    .filter(t => !euOnly || t.origin.startsWith('EU'))
    .sort((a, b) => {
      if (sort === 'rating') return b.rating - a.rating;
      if (sort === 'name') return a.name.localeCompare(b.name);
      if (sort === 'newest') return new Date(b.lastUpdated) - new Date(a.lastUpdated);
      return 0;
    });

  return (
    <div>
      <Breadcrumb items={[{ label: 'Start', to: { page: 'home' } }, { label: 'Verzeichnis' }]} onNav={nav} />

      <div style={{ display: 'grid', gridTemplateColumns: '240px 1fr', gap: 56 }}>
        {/* Sidebar — wiki-typische Navigation */}
        <aside>
          <div style={{
            fontFamily: 'JetBrains Mono, monospace', fontSize: 11,
            letterSpacing: '0.08em', color: '#8a8580',
            textTransform: 'uppercase', marginBottom: 14,
          }}>Kategorien</div>
          <ul style={{ listStyle: 'none', padding: 0, margin: 0 }}>
            <li style={{ padding: '6px 0' }}>
              <a onClick={() => setCatFilter('all')} style={{
                cursor: 'pointer', fontSize: 13,
                color: catFilter === 'all' ? 'var(--accent)' : 'var(--ink-strong)',
                fontWeight: catFilter === 'all' ? 600 : 400,
                borderBottom: catFilter === 'all' ? '1px solid var(--accent)' : 'none',
                paddingBottom: 1,
              }}>Alle Tools <span style={{ color: '#8a8580', fontFamily: 'JetBrains Mono, monospace', fontSize: 11 }}>({tools.length})</span></a>
            </li>
            {categories.map(c => (
              <li key={c.slug} style={{ padding: '6px 0' }}>
                <a onClick={() => setCatFilter(c.slug)} style={{
                  cursor: 'pointer', fontSize: 13,
                  color: catFilter === c.slug ? 'var(--accent)' : 'var(--ink-strong)',
                  fontWeight: catFilter === c.slug ? 600 : 400,
                  borderBottom: catFilter === c.slug ? '1px solid var(--accent)' : 'none',
                  paddingBottom: 1,
                }}>{c.name} <span style={{ color: '#8a8580', fontFamily: 'JetBrains Mono, monospace', fontSize: 11 }}>({c.count})</span></a>
              </li>
            ))}
          </ul>

          <div style={{
            fontFamily: 'JetBrains Mono, monospace', fontSize: 11,
            letterSpacing: '0.08em', color: '#8a8580',
            textTransform: 'uppercase', marginTop: 36, marginBottom: 14,
          }}>Filter</div>
          <label style={{ display: 'flex', gap: 10, alignItems: 'center', fontSize: 13, padding: '6px 0', cursor: 'pointer' }}>
            <input type="checkbox" checked={dsgvoOnly} onChange={e => setDsgvoOnly(e.target.checked)} style={{ accentColor: 'var(--accent)' }} />
            Nur DSGVO-konform
          </label>
          <label style={{ display: 'flex', gap: 10, alignItems: 'center', fontSize: 13, padding: '6px 0', cursor: 'pointer' }}>
            <input type="checkbox" checked={euOnly} onChange={e => setEuOnly(e.target.checked)} style={{ accentColor: 'var(--accent)' }} />
            Nur EU-Anbieter
          </label>

          {compareList.length > 0 && (
            <div style={{ marginTop: 36, padding: 16, border: '1px solid var(--accent)', background: 'var(--bg)' }}>
              <div style={{
                fontFamily: 'JetBrains Mono, monospace', fontSize: 11,
                letterSpacing: '0.08em', color: 'var(--accent)',
                textTransform: 'uppercase', marginBottom: 10,
              }}>Vergleichskorb ({compareList.length}/4)</div>
              {compareList.map(slug => {
                const t = tools.find(x => x.slug === slug);
                return t && (
                  <div key={slug} style={{ display: 'flex', justifyContent: 'space-between', padding: '4px 0', fontSize: 13 }}>
                    <span>{t.name}</span>
                    <a onClick={() => toggleCompare(slug)} style={{ cursor: 'pointer', color: '#8a8580' }}>×</a>
                  </div>
                );
              })}
              <Button variant="accent" onClick={() => nav({ page: 'compare' })}>Vergleichen →</Button>
            </div>
          )}
        </aside>

        {/* Main */}
        <div>
          <div style={{ display: 'flex', alignItems: 'end', justifyContent: 'space-between', marginBottom: 32, flexWrap: 'wrap', gap: 16 }}>
            <div>
              <h1 style={{
                fontFamily: 'Fraunces, serif', fontWeight: 400,
                fontSize: 48, letterSpacing: '-0.02em',
                margin: 0, lineHeight: 1,
              }}>
                {catFilter === 'all' ? 'Alle Tools' : categories.find(c => c.slug === catFilter)?.name}
              </h1>
              <div style={{ marginTop: 10, fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#8a8580', letterSpacing: '0.04em', textTransform: 'uppercase' }}>
                {filtered.length} Einträge{search && ` · Suche: „${search}"`}
              </div>
            </div>
            <div style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
              <select value={sort} onChange={e => setSort(e.target.value)} style={{
                padding: '9px 12px', border: '1px solid var(--line)', background: 'var(--bg)',
                fontFamily: 'Inter Tight, sans-serif', fontSize: 13, cursor: 'pointer',
              }}>
                <option value="rating">Sortierung: Bewertung</option>
                <option value="name">Sortierung: Name A–Z</option>
                <option value="newest">Sortierung: Zuletzt aktualisiert</option>
              </select>
              <div style={{ display: 'flex', border: '1px solid var(--line)' }}>
                {['list', 'grid'].map(v => (
                  <button key={v} onClick={() => setView(v)} style={{
                    padding: '8px 12px', border: 'none',
                    background: view === v ? 'var(--ink-strong)' : 'transparent',
                    color: view === v ? 'var(--bg)' : 'var(--ink)',
                    fontFamily: 'JetBrains Mono, monospace', fontSize: 11,
                    letterSpacing: '0.04em', textTransform: 'uppercase', cursor: 'pointer',
                  }}>{v === 'list' ? 'Liste' : 'Raster'}</button>
                ))}
              </div>
            </div>
          </div>

          <div style={{ marginBottom: 16, display: 'flex', alignItems: 'center', border: '1px solid var(--line)', padding: 2 }}>
            <input
              value={search}
              onChange={e => setSearch(e.target.value)}
              placeholder="In diesem Verzeichnis suchen …"
              style={{ flex: 1, padding: '10px 14px', border: 'none', outline: 'none', background: 'transparent', fontFamily: 'Inter Tight, sans-serif', fontSize: 13 }}
            />
            {search && <a onClick={() => setSearch('')} style={{ padding: '0 14px', cursor: 'pointer', color: '#8a8580', fontFamily: 'JetBrains Mono, monospace', fontSize: 11 }}>Zurücksetzen ×</a>}
          </div>

          {view === 'list' ? (
            <ul style={{ listStyle: 'none', padding: 0, margin: 0, border: '1px solid var(--line)', borderBottom: 'none' }}>
              {filtered.map(t => (
                <li key={t.slug} style={{ display: 'grid', gridTemplateColumns: '80px 1fr 160px 120px 110px', gap: 20, padding: '18px 20px', borderBottom: '1px solid var(--line)', alignItems: 'center' }}>
                  <div style={{ width: 80 }}><Thumb name={t.name} slug={t.slug} aspect="4/3" label="" /></div>
                  <div>
                    <a onClick={() => nav({ page: 'tool', slug: t.slug })} style={{ cursor: 'pointer' }}>
                      <div style={{ display: 'flex', alignItems: 'baseline', gap: 12 }}>
                        <h3 style={{ fontFamily: 'Fraunces, serif', fontSize: 22, fontWeight: 500, margin: 0, letterSpacing: '-0.01em' }}>{t.name}</h3>
                        <span style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#8a8580', letterSpacing: '0.04em' }}>{t.vendor}</span>
                      </div>
                      <p style={{ margin: '4px 0 0', fontSize: 13, color: 'var(--ink)', lineHeight: 1.45 }}>{t.tagline}</p>
                    </a>
                  </div>
                  <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                    <Badge kind={t.dsgvo} />
                    <span style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 10, color: '#8a8580', letterSpacing: '0.04em' }}>{t.origin}</span>
                  </div>
                  <div>
                    <Stars rating={t.rating} />
                    <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 10, color: '#8a8580', marginTop: 2 }}>{t.rating} / 5 · {t.reviews}</div>
                  </div>
                  <div style={{ display: 'flex', flexDirection: 'column', gap: 6, alignItems: 'end' }}>
                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, fontSize: 11, fontFamily: 'JetBrains Mono, monospace', color: '#8a8580', cursor: 'pointer', letterSpacing: '0.04em', textTransform: 'uppercase' }}>
                      <input type="checkbox" checked={compareList.includes(t.slug)} onChange={() => toggleCompare(t.slug)} style={{ accentColor: 'var(--accent)' }} />
                      Vergleichen
                    </label>
                  </div>
                </li>
              ))}
            </ul>
          ) : (
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 24 }}>
              {filtered.map(t => (
                <a key={t.slug} onClick={() => nav({ page: 'tool', slug: t.slug })} style={{ cursor: 'pointer', display: 'flex', flexDirection: 'column', gap: 10 }}>
                  <Thumb name={t.name} slug={t.slug} aspect="4/3" />
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                    <Badge kind={t.dsgvo} />
                    <Stars rating={t.rating} />
                  </div>
                  <h3 style={{ fontFamily: 'Fraunces, serif', fontSize: 22, fontWeight: 500, margin: 0, letterSpacing: '-0.01em' }}>{t.name}</h3>
                  <p style={{ margin: 0, fontSize: 13, color: 'var(--ink)', lineHeight: 1.45 }}>{t.tagline}</p>
                </a>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

function CategoryPage({ nav, slug, toggleCompare, compareList }) {
  const { categories, tools } = window.KI_DATA;
  const cat = categories.find(c => c.slug === slug) || categories[0];
  const items = tools.filter(t => t.category === cat.slug);

  return (
    <div>
      <Breadcrumb items={[{ label: 'Start', to: { page: 'home' } }, { label: 'Verzeichnis', to: { page: 'directory' } }, { label: cat.name }]} onNav={nav} />

      <div style={{ borderBottom: '1px solid var(--line)', paddingBottom: 40, marginBottom: 40 }}>
        <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#8a8580', letterSpacing: '0.08em', textTransform: 'uppercase', marginBottom: 14 }}>Kategorie</div>
        <h1 style={{ fontFamily: 'Fraunces, serif', fontWeight: 400, fontSize: 64, letterSpacing: '-0.025em', margin: 0, lineHeight: 1, textWrap: 'balance' }}>{cat.name}</h1>
        <p style={{ fontFamily: 'Fraunces, serif', fontSize: 20, lineHeight: 1.5, color: 'var(--ink)', marginTop: 20, maxWidth: 720 }}>{cat.desc}</p>
        <div style={{ marginTop: 20, fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#8a8580', letterSpacing: '0.04em', textTransform: 'uppercase' }}>
          {cat.count} Tools · zuletzt überprüft am 12. April 2026
        </div>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 280px', gap: 56 }}>
        <div>
          <SectionLabel num="A">Top-Tools dieser Kategorie</SectionLabel>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: 24 }}>
            {items.map(t => (
              <article key={t.slug} style={{ border: '1px solid var(--line)', padding: 20, display: 'flex', flexDirection: 'column', gap: 12 }}>
                <Thumb name={t.name} slug={t.slug} aspect="3/2" />
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <Badge kind={t.dsgvo} />
                  <Stars rating={t.rating} />
                </div>
                <a onClick={() => nav({ page: 'tool', slug: t.slug })} style={{ cursor: 'pointer' }}>
                  <h3 style={{ fontFamily: 'Fraunces, serif', fontSize: 24, fontWeight: 500, margin: 0, letterSpacing: '-0.01em' }}>{t.name}</h3>
                </a>
                <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 10, color: '#8a8580', letterSpacing: '0.04em', textTransform: 'uppercase' }}>{t.vendor} · {t.origin}</div>
                <p style={{ margin: 0, fontSize: 13, lineHeight: 1.5, color: 'var(--ink)' }}>{t.tagline}</p>
                <div style={{ display: 'flex', gap: 8, marginTop: 'auto' }}>
                  <Button variant="ghost" onClick={() => nav({ page: 'tool', slug: t.slug })}>Details →</Button>
                  <Button variant="ghost" onClick={() => toggleCompare(t.slug)}>{compareList.includes(t.slug) ? '✓ im Korb' : '+ vergleichen'}</Button>
                </div>
              </article>
            ))}
          </div>
        </div>

        {/* Seitenleiste im Wiki-Stil */}
        <aside>
          <div style={{ border: '1px solid var(--line)', padding: 20 }}>
            <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#8a8580', letterSpacing: '0.08em', textTransform: 'uppercase', marginBottom: 12 }}>Siehe auch</div>
            <ul style={{ listStyle: 'none', padding: 0, margin: 0 }}>
              {categories.filter(c => c.slug !== cat.slug).slice(0, 5).map(c => (
                <li key={c.slug} style={{ padding: '6px 0', borderBottom: '1px dotted var(--line)' }}>
                  <a onClick={() => nav({ page: 'category', slug: c.slug })} style={{ cursor: 'pointer', color: 'var(--accent)', fontSize: 13, borderBottom: '1px dotted var(--accent)' }}>{c.name}</a>
                </li>
              ))}
            </ul>
          </div>
          <div style={{ border: '1px solid var(--line)', padding: 20, marginTop: 20 }}>
            <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#8a8580', letterSpacing: '0.08em', textTransform: 'uppercase', marginBottom: 12 }}>Auswahlhilfe</div>
            <p style={{ fontSize: 13, lineHeight: 1.5, margin: 0, color: 'var(--ink)' }}>
              Wählen Sie <b>2 bis 4 Tools</b> zum direkten Vergleich aus — Preise, Funktionen, DSGVO und mehr in tabellarischer Gegenüberstellung.
            </p>
            <Button variant="primary" onClick={() => nav({ page: 'compare' })}>Zum Vergleich →</Button>
          </div>
        </aside>
      </div>
    </div>
  );
}

Object.assign(window, { HomePage, DirectoryPage, CategoryPage });
