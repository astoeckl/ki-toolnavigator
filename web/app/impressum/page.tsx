import { Breadcrumb } from '@/components/ui';

export const metadata = { title: 'Impressum · KI-Toolnavigator' };

export default function ImpressumPage() {
  return (
    <div>
      <Breadcrumb items={[{ label: 'Start', href: '/' }, { label: 'Impressum' }]} />

      <div style={{ borderBottom: '1px solid var(--line)', paddingBottom: 32, marginBottom: 40 }}>
        <div style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#8a8580', letterSpacing: '0.08em', textTransform: 'uppercase', marginBottom: 12 }}>
          Offenlegung · § 25 Mediengesetz · § 5 ECG
        </div>
        <h1 className="h-editorial-md" style={{ fontFamily: 'Fraunces, serif', fontWeight: 400, margin: 0 }}>
          Impressum
        </h1>
      </div>

      <article className="prose" style={{ maxWidth: 680 }}>
        <h2>Medieninhaber und für den Inhalt verantwortlich</h2>
        <p>
          <strong>Dr. Andreas Stöckl</strong><br />
          Tiefenbachweg 2<br />
          4213 Unterweitersdorf<br />
          Österreich
        </p>
        <p>
          E-Mail: <a href="mailto:andreas@stoeckl.ai">andreas@stoeckl.ai</a>
        </p>

        <h2>Unternehmensgegenstand</h2>
        <p>
          Redaktionelle Information über Werkzeuge aus dem Bereich der Künstlichen
          Intelligenz — Verzeichnis, Vergleich und Einordnung. Keine kommerziellen
          Angebote, keine Werbung, keine Tracking-Cookies.
        </p>

        <h2>Haftung für Inhalte</h2>
        <p>
          Die Inhalte dieser Seiten wurden mit größter Sorgfalt erstellt. Für die Richtigkeit,
          Vollständigkeit und Aktualität der Inhalte kann jedoch keine Gewähr übernommen werden.
          Als Diensteanbieter bin ich gemäß § 7 Abs. 1 TMG (Deutschland) bzw. § 18 ECG (Österreich)
          für eigene Inhalte auf diesen Seiten nach den allgemeinen Gesetzen verantwortlich.
          Nach §§ 8 bis 10 TMG bzw. §§ 13 bis 17 ECG bin ich als Diensteanbieter jedoch nicht
          verpflichtet, übermittelte oder gespeicherte fremde Informationen zu überwachen oder
          nach Umständen zu forschen, die auf eine rechtswidrige Tätigkeit hinweisen.
        </p>

        <h2>Haftung für Links</h2>
        <p>
          Dieses Angebot enthält Links zu externen Websites Dritter, auf deren Inhalte ich
          keinen Einfluss habe. Deshalb kann ich für diese fremden Inhalte auch keine Gewähr
          übernehmen. Für die Inhalte der verlinkten Seiten ist stets der jeweilige Anbieter
          oder Betreiber der Seiten verantwortlich. Die verlinkten Seiten wurden zum Zeitpunkt
          der Verlinkung auf mögliche Rechtsverstöße überprüft. Rechtswidrige Inhalte waren
          zum Zeitpunkt der Verlinkung nicht erkennbar. Eine permanente inhaltliche Kontrolle
          ist jedoch ohne konkrete Anhaltspunkte einer Rechtsverletzung nicht zumutbar. Bei
          Bekanntwerden von Rechtsverletzungen werden derartige Links umgehend entfernt.
        </p>

        <h2>Urheberrecht</h2>
        <p>
          Die durch den Seitenbetreiber erstellten Inhalte und Werke auf diesen Seiten
          unterliegen dem österreichischen Urheberrecht. Vervielfältigung, Bearbeitung,
          Verbreitung und jede Art der Verwertung außerhalb der Grenzen des Urheberrechts
          bedürfen der schriftlichen Zustimmung des jeweiligen Autors. Downloads und Kopien
          dieser Seite sind nur für den privaten, nicht kommerziellen Gebrauch gestattet.
        </p>
        <p>
          Soweit die Inhalte auf dieser Seite nicht vom Betreiber erstellt wurden, werden
          die Urheberrechte Dritter beachtet. Insbesondere sind Inhalte Dritter als solche
          gekennzeichnet. Sollten Sie trotzdem auf eine Urheberrechtsverletzung aufmerksam
          werden, bitte ich um einen entsprechenden Hinweis. Bei Bekanntwerden von
          Rechtsverletzungen werden derartige Inhalte umgehend entfernt.
        </p>

        <h2>Bild- und Textquellen</h2>
        <ul>
          <li>
            Abstrakte Cover-Illustrationen: generiert mit <em>Nano Banana</em> (Fal.ai) über
            die <a href="https://backend.cognitor.dev" target="_blank" rel="noreferrer">Cognitor-CMS-Plattform</a>.
          </li>
          <li>
            Tool-Logos: offizielle Apple-Touch-Icons der jeweiligen Hersteller-Websites,
            eingebunden nur als Verweis im Sinne einer redaktionellen Berichterstattung.
          </li>
          <li>
            Website-Screenshots: eigene Aufnahmen der öffentlich zugänglichen Startseiten
            der jeweiligen Anbieter, aufgenommen mit Playwright zum Zweck der Einordnung.
          </li>
          <li>
            Artikel- und Tool-Texte: eigene redaktionelle Inhalte.
          </li>
        </ul>

        <h2 id="datenschutz">Datenschutz</h2>
        <p>
          Diese Website verarbeitet keine personenbezogenen Daten von Besucherinnen und
          Besuchern. Es werden keine Tracking-Cookies, keine Analytics-Dienste und keine
          externen Werbe-Skripte geladen. Serverseitig werden lediglich anonyme
          Zugriffsprotokolle (IP-Adresse, User-Agent, Zeitstempel) zur Absicherung des
          Hosting-Betriebs durch <em>Netlify</em> erhoben. Für inhaltliche Recherchen wird
          über serverseitige API-Calls auf das redaktionell gepflegte{' '}
          <em>Cognitor-CMS</em> zugegriffen; dabei werden keine Nutzerdaten übertragen.
        </p>

        <h2>Hosting</h2>
        <p>
          Das Hosting dieser Website erfolgt über <strong>Netlify, Inc.</strong>,
          44 Montgomery Street, Suite 300, San Francisco, California 94104, USA.
          Das CMS-Backend wird von <strong>Cognitor</strong> in der EU betrieben.
        </p>

        <h2>Copyright</h2>
        <p>© 2026 Dr. Andreas Stöckl — alle Rechte vorbehalten.</p>
      </article>
    </div>
  );
}
