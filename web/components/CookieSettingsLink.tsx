'use client';

/** Footer link that re-opens the cookie consent banner so a visitor can change
 *  their earlier choice. Dispatches a window event that CookieConsent listens for.
 *  Rendered as an <a> to inherit the footer's link styling. */
export function CookieSettingsLink() {
  const open = () => window.dispatchEvent(new Event('ki:open-consent'));
  return (
    <a
      role="button"
      tabIndex={0}
      onClick={open}
      onKeyDown={(e) => {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          open();
        }
      }}
    >
      Cookie-Einstellungen
    </a>
  );
}
