1:"$Sreact.fragment"
2:I[45910,["/_next/static/chunks/1584_b4q0.7v3.js","/_next/static/chunks/0d3shmwh5_nmn.js","/_next/static/chunks/0-ag_4mc4snem.js"],"Breadcrumb"]
3:I[48511,["/_next/static/chunks/1584_b4q0.7v3.js","/_next/static/chunks/0d3shmwh5_nmn.js","/_next/static/chunks/0-ag_4mc4snem.js"],"ScrollSpyTOC"]
4:I[45910,["/_next/static/chunks/1584_b4q0.7v3.js","/_next/static/chunks/0d3shmwh5_nmn.js","/_next/static/chunks/0-ag_4mc4snem.js"],"Chip"]
a:I[22016,["/_next/static/chunks/1584_b4q0.7v3.js","/_next/static/chunks/0d3shmwh5_nmn.js","/_next/static/chunks/0-ag_4mc4snem.js"],""]
b:I[97367,["/_next/static/chunks/1584_b4q0.7v3.js","/_next/static/chunks/0d3shmwh5_nmn.js"],"OutletBoundary"]
c:"$Sreact.suspense"
:HL["https://cognotor.s3.eu-central-1.amazonaws.com/uploads/site_49/cover_rag_erklaert.png","image"]
5:Tbed,<h2 id="was-ist-rag">Was ist RAG?</h2>
<p>Retrieval-Augmented Generation (RAG) verbindet ein Sprachmodell mit einer externen Wissensquelle. Statt sich nur auf das im Modell „eingebackene&quot; Wissen zu verlassen, ruft das System für jede Anfrage relevante Dokumente aus einer Datenbank ab und übergibt sie dem Modell als Kontext.</p>
<p>Der Vorteil ist offensichtlich: Aktuelle Information, eigene Unternehmensdaten und nachprüfbare Quellen — ohne das Modell neu trainieren zu müssen. RAG ist heute der Standard für Unternehmens-Chatbots, Wissens-Suche und domänenspezifische Assistenten.</p>
<h2 id="architektur">Architektur</h2>
<p>Ein typisches RAG-System besteht aus fünf Komponenten:</p>
<ol>
<li><strong>Ingestion-Pipeline</strong> — Dokumente werden in Chunks zerlegt, eingebettet und gespeichert.</li>
<li><strong>Vektordatenbank</strong> — speichert die Embeddings und erlaubt Ähnlichkeitssuche.</li>
<li><strong>Retriever</strong> — findet zur Anfrage passende Chunks.</li>
<li><strong>Reranker</strong> — sortiert die Treffer feiner (optional, aber qualitätssteigernd).</li>
<li><strong>Generator</strong> — das Sprachmodell, das mit Anfrage + Kontext die Antwort erzeugt.</li>
</ol>
<p>Die schwierigste Komponente ist meist nicht das Modell, sondern die Ingestion: Wie schneidet man Dokumente sinnvoll? Wie geht man mit Tabellen, Bildern, mehrsprachigen Inhalten um?</p>
<blockquote>
<p>RAG verlagert das Schwierige vom Training in den Datenpipeline-Bau.</p>
</blockquote>
<h2 id="vektordatenbanken">Vektordatenbanken</h2>
<p>Vektordatenbanken speichern hochdimensionale Embeddings (typischerweise 768 bis 3072 Dimensionen) und unterstützen schnelle Approximate-Nearest-Neighbor-Suche. Die wichtigsten Optionen 2026:</p>
<ul>
<li><strong>Pinecone</strong> — managed, gut skalierbar, teuer.</li>
<li><strong>Weaviate</strong> — Open Source, mit Hybrid-Suche (Vektor + Volltext).</li>
<li><strong>Qdrant</strong> — Open Source, Rust-basiert, sehr schnell.</li>
<li><strong>pgvector</strong> — Postgres-Erweiterung; wenn schon Postgres im Stack ist, oft die pragmatischste Wahl.</li>
</ul>
<p>Für mittelgroße Anwendungen (unter 10 Millionen Chunks) reicht pgvector meist aus. Erst bei höherer Skalierung lohnen sich spezialisierte Lösungen.</p>
<h2 id="evaluierung">Evaluierung</h2>
<p>RAG-Systeme zu evaluieren ist anspruchsvoll, weil zwei Schritte gleichzeitig getestet werden: Hat der Retriever die richtigen Dokumente gefunden? Hat der Generator daraus die richtige Antwort gebaut?</p>
<p>Standardmetriken:</p>
<ul>
<li><strong>Recall@k</strong> — wie oft taucht das relevante Dokument unter den Top-k auf?</li>
<li><strong>Faithfulness</strong> — bleibt die Antwort im Rahmen der gefundenen Quellen?</li>
<li><strong>Answer Relevance</strong> — beantwortet die Antwort tatsächlich die Frage?</li>
</ul>
<p>Frameworks wie <em>Ragas</em> oder <em>DeepEval</em> automatisieren diese Messungen mit eigenen LLM-Judges. Die Ergebnisse sind nicht perfekt, aber deutlich besser als kein Monitoring.</p>
0:{"rsc":["$","$1","c",{"children":[["$","div",null,{"children":[["$","$L2",null,{"items":[{"label":"Start","href":"/"},{"label":"Artikel"},{"label":"Retrieval-Augmented Generation erklärt"}]}],["$","div",null,{"className":"layout-3col-article","children":[["$","aside",null,{"className":"sidebar-sticky only-desktop","style":{"position":"sticky","top":80,"alignSelf":"start"},"children":["$","$L3",null,{"eyebrow":"Inhaltsverzeichnis","items":[{"label":"Was ist RAG?","hash":"#was-ist-rag","num":"01"},{"label":"Architektur","hash":"#architektur","num":"02"},{"label":"Vektordatenbanken","hash":"#vektordatenbanken","num":"03"},{"label":"Evaluierung","hash":"#evaluierung","num":"04"}]}]}],["$","article",null,{"style":{"maxWidth":680},"children":[["$","$L4",null,{"children":"Technik"}],["$","h1",null,{"className":"h-editorial-md","style":{"fontFamily":"Fraunces, serif","fontWeight":400,"margin":"18px 0 18px","textWrap":"balance"},"children":"Retrieval-Augmented Generation erklärt"}],["$","div",null,{"style":{"fontFamily":"JetBrains Mono, monospace","fontSize":11,"color":"#8a8580","letterSpacing":"0.04em","textTransform":"uppercase"},"children":["Dr. T. Müller"," · ","22. Februar 2026"," · ",12," Min. Lesezeit"]}],["$","figure",null,{"style":{"margin":"32px 0","border":"1px solid var(--line)","padding":0},"children":[["$","img",null,{"src":"https://cognotor.s3.eu-central-1.amazonaws.com/uploads/site_49/cover_rag_erklaert.png","alt":"Retrieval-Augmented Generation erklärt","style":{"display":"block","width":"100%","height":"auto","aspectRatio":"16 / 9","objectFit":"cover"}}],["$","figcaption",null,{"style":{"padding":"8px 14px","borderTop":"1px solid var(--line)","fontFamily":"JetBrains Mono, monospace","fontSize":10,"letterSpacing":"0.06em","textTransform":"uppercase","color":"#8a8580","display":"flex","justifyContent":"space-between"},"children":[["$","span",null,{"children":"Aufmacher · Illustration"}],["$","span",null,{"children":"Cognitor Media (Nano Banana)"}]]}]]}],"",["$","div",null,{"className":"prose prose--drop-cap","dangerouslySetInnerHTML":{"__html":"$5"}}],"$L6"]}],"$L7"]}]]}],["$L8"],"$L9"]}],"isPartial":false,"staleTime":300,"varyParams":null,"buildId":"RoAP3uZo_eUG6jf3r5Wxj"}
6:["$","div",null,{"style":{"marginTop":56,"paddingTop":20,"borderTop":"1px solid var(--line)","display":"flex","gap":16,"flexWrap":"wrap","alignItems":"center"},"children":[["$","div",null,{"style":{"fontFamily":"JetBrains Mono, monospace","fontSize":11,"color":"#8a8580","letterSpacing":"0.08em","textTransform":"uppercase"},"children":"Verweise:"}],["$","$L4",null,{"children":"Grundlagen"}],["$","$L4",null,{"children":"Sprachmodelle"}],["$","$L4",null,{"children":"DSGVO"}],["$","$L4",null,{"children":"Geschichte"}]]}]
7:["$","aside",null,{"children":[["$","div",null,{"style":{"fontFamily":"JetBrains Mono, monospace","fontSize":11,"color":"#8a8580","letterSpacing":"0.08em","textTransform":"uppercase","marginBottom":14},"children":"Weitere Artikel"}],["$","ul",null,{"style":{"listStyle":"none","padding":0,"margin":0},"children":[["$","li","was-ist-ki",{"style":{"padding":"14px 0","borderBottom":"1px dotted var(--line)"},"children":["$","$La",null,{"href":"/artikel/was-ist-ki","children":[["$","h4",null,{"style":{"fontFamily":"Fraunces, serif","fontSize":16,"fontWeight":500,"margin":0,"letterSpacing":"-0.01em","lineHeight":1.25},"children":"Was ist Künstliche Intelligenz?"}],["$","div",null,{"style":{"fontFamily":"JetBrains Mono, monospace","fontSize":10,"color":"#8a8580","letterSpacing":"0.04em","textTransform":"uppercase","marginTop":4},"children":["Redaktion"," · ",8," Min."]}]]}]}],["$","li","llm-vergleich",{"style":{"padding":"14px 0","borderBottom":"1px dotted var(--line)"},"children":["$","$La",null,{"href":"/artikel/llm-vergleich","children":[["$","h4",null,{"style":{"fontFamily":"Fraunces, serif","fontSize":16,"fontWeight":500,"margin":0,"letterSpacing":"-0.01em","lineHeight":1.25},"children":"Große Sprachmodelle im Vergleich 2026"}],["$","div",null,{"style":{"fontFamily":"JetBrains Mono, monospace","fontSize":10,"color":"#8a8580","letterSpacing":"0.04em","textTransform":"uppercase","marginTop":4},"children":["M. Hartmann"," · ",14," Min."]}]]}]}],["$","li","dsgvo-ki",{"style":{"padding":"14px 0","borderBottom":"1px dotted var(--line)"},"children":["$","$La",null,{"href":"/artikel/dsgvo-ki","children":[["$","h4",null,{"style":{"fontFamily":"Fraunces, serif","fontSize":16,"fontWeight":500,"margin":0,"letterSpacing":"-0.01em","lineHeight":1.25},"children":"DSGVO und KI: Was Unternehmen 2026 wissen müssen"}],["$","div",null,{"style":{"fontFamily":"JetBrains Mono, monospace","fontSize":10,"color":"#8a8580","letterSpacing":"0.04em","textTransform":"uppercase","marginTop":4},"children":["Dr. S. Klein"," · ",11," Min."]}]]}]}],["$","li","prompt-engineering",{"style":{"padding":"14px 0","borderBottom":"1px dotted var(--line)"},"children":["$","$La",null,{"href":"/artikel/prompt-engineering","children":[["$","h4",null,{"style":{"fontFamily":"Fraunces, serif","fontSize":16,"fontWeight":500,"margin":0,"letterSpacing":"-0.01em","lineHeight":1.25},"children":"Prompt Engineering: Techniken und Muster"}],["$","div",null,{"style":{"fontFamily":"JetBrains Mono, monospace","fontSize":10,"color":"#8a8580","letterSpacing":"0.04em","textTransform":"uppercase","marginTop":4},"children":["J. Weber"," · ",16," Min."]}]]}]}]]}]]}]
8:["$","script","script-0",{"src":"/_next/static/chunks/0-ag_4mc4snem.js","async":true}]
9:["$","$Lb",null,{"children":["$","$c",null,{"name":"Next.MetadataOutlet","children":"$@d"}]}]
d:null
