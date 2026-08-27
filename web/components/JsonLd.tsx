/** Renders one or more schema.org graphs as <script type="application/ld+json">.
 *  Server Component — the JSON is inlined into the HTML, so crawlers see it
 *  without executing any JavaScript. */
export function JsonLd({ data }: { data: object | object[] }) {
  const graphs = Array.isArray(data) ? data : [data];
  return (
    <>
      {graphs.map((g, i) => (
        <script
          key={i}
          type="application/ld+json"
          // `<` escaped so a stray "</script>" inside CMS text cannot break out.
          dangerouslySetInnerHTML={{ __html: JSON.stringify(g).replace(/</g, '\\u003c') }}
        />
      ))}
    </>
  );
}
