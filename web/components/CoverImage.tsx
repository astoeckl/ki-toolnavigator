import Image from 'next/image';

type Props = {
  src: string;
  alt: string;
  /** CSS aspect-ratio for the box, e.g. "3 / 2". */
  aspect: string;
  /** Layout-slot hint for srcset selection. Getting this wrong makes Next
   *  download a far larger file than the slot needs — always pass the real widths. */
  sizes: string;
  /** Set on the LCP image only; disables lazy loading and preloads it. */
  priority?: boolean;
  bordered?: boolean;
  /** "cover" crops to fill (default); "contain" fits the whole image inside. */
  fit?: 'cover' | 'contain';
  objectPosition?: string;
  /** Inner padding on the image itself — useful for logos that should not touch
   *  the frame. Not set on the box: `fill` positions against the padding box, so
   *  container padding would have no effect. */
  padding?: number;
  background?: string;
};

/** Remote CMS image in a fixed-ratio box: no layout shift, AVIF/WebP, lazy by default. */
export function CoverImage({
  src, alt, aspect, sizes, priority = false, bordered = false,
  fit = 'cover', objectPosition, padding, background,
}: Props) {
  return (
    <div
      style={{
        position: 'relative',
        width: '100%',
        aspectRatio: aspect,
        overflow: 'hidden',
        border: bordered ? '1px solid var(--line)' : undefined,
        background: background ?? 'var(--bg-alt)',
      }}
    >
      <Image
        src={src}
        alt={alt}
        fill
        sizes={sizes}
        priority={priority}
        style={{ objectFit: fit, objectPosition, padding }}
      />
    </div>
  );
}
