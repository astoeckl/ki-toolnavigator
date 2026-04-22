/** Editorial prose with Fraunces serif H2s, accent drop-cap, and pull-quotes. */
type ProseProps = { html: string; dropCap?: boolean };

export function Prose({ html, dropCap = false }: ProseProps) {
  return (
    <div
      className={'prose' + (dropCap ? ' prose--drop-cap' : '')}
      dangerouslySetInnerHTML={{ __html: html }}
    />
  );
}
