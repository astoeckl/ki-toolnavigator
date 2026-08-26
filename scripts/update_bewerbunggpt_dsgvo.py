#!/usr/bin/env python3
"""Align BewerbungGPT's DSGVO rating with the NebenkostenPro precedent:
German controller + EU servers, but user content is forwarded to a non-EU AI API
→ 'bedingt' instead of 'ja'. Consistent treatment across the directory."""
import requests, urllib3
from pathlib import Path
urllib3.disable_warnings()
ROOT = Path(__file__).resolve().parent.parent
ENV = {l.split('=',1)[0].strip(): l.split('=',1)[1].strip()
       for l in (ROOT/'.env').read_text().splitlines() if '=' in l and not l.startswith('#')}
BASE, SITE = ENV['BASEURL'], ENV['SITE']
r = requests.post(f'{BASE}/auth/login',
    data={'grant_type':'password','username':ENV['EMAIL'],'password':ENV['PW']},
    headers={'Content-Type':'application/x-www-form-urlencoded'}, verify=False)
H = {'Authorization': f'Bearer {r.json()["access_token"]}', 'Content-Type':'application/json'}
print('OK logged in')

EID, PID = 50976, 783

# ---- 1. structured fields ----
el = requests.get(f'{BASE}/{SITE}/elements/{EID}', headers=H, verify=False).json()
d = el['data']
before = d.get('dsgvo')
d['dsgvo'] = 'bedingt'
d['lastUpdated'] = '2026-08-26'
d['cons'] = [
    'Eingegebene Bewerbungsdaten werden an Anthropics API (US-Anbieter, ohne Training) uebermittelt',
    'Fokus auf den deutschsprachigen Raum - fuer internationale Bewerbungen weniger geeignet',
    'KI-generierte Bewerbungsfotos ersetzen kein professionelles Shooting',
    'Anschreiben sollten vor dem Versand geprueft und geschaerft werden',
]
# restore proper German typography (avoid heredoc escaping issues)
d['cons'][0] = d['cons'][0].replace('uebermittelt', 'übermittelt')
d['cons'][1] = d['cons'][1].replace('fuer', 'für').replace(' - ', ' — ')
d['cons'][3] = d['cons'][3].replace('geprueft', 'geprüft').replace('geschaerft', 'geschärft')
rp = requests.patch(f'{BASE}/{SITE}/elements/{EID}', json={'data': d}, headers=H, verify=False)
print(f'element {EID}: dsgvo {before} -> {d["dsgvo"]} | patch {rp.status_code}')

# ---- 2. overview paragraph ----
post = requests.get(f'{BASE}/{SITE}/posts/{PID}', headers=H, verify=False).json()
content = post['content']
old = ('Beim **Datenschutz** ist die Ausgangslage günstig und über die öffentlich zugänglichen Angaben '
       'gut nachvollziehbar: Es handelt sich um einen **deutschen Anbieter** (EU) mit Impressum und '
       'Datenschutzerklärung, die **Server liegen in der EU**, und es wird bewusst datensparsam '
       'gearbeitet (Selfie wird nicht behalten). Die KI-Generierung selbst läuft laut Anbieter über die '
       '**API von Anthropic (Claude)**, ohne dass Inhalte fürs Training verwendet werden. Diese '
       'Verarbeitung über einen US-Anbieter ist der einzige nennenswerte Drittland-Aspekt — für die '
       'meisten Nutzer:innen unter den üblichen Auftragsverarbeitungs-Bedingungen unkritisch, aber ein '
       'Punkt, den man bei besonders sensiblen Daten kennen sollte. In Summe ist das ein solide '
       'DSGVO-konform aufgestelltes deutsches Tool.')
new = ('Beim **Datenschutz** ist die Ausgangslage günstig: Es handelt sich um einen **deutschen '
       'Anbieter** (EU) mit Impressum und Datenschutzerklärung, die **Server liegen in der EU**, und es '
       'wird bewusst datensparsam gearbeitet (Selfie wird nicht behalten). Einschränkend gilt: Die '
       'KI-Generierung läuft laut Anbieter über die **API von Anthropic (Claude)**, ohne dass Inhalte '
       'fürs Training verwendet werden — die eingegebenen Bewerbungsunterlagen (Lebenslauf, persönliche '
       'Angaben) werden damit an einen **US-Anbieter übermittelt**. Unter üblichen '
       'Auftragsverarbeitungs-Bedingungen ist das gangbar und für die meisten Nutzer:innen unkritisch. '
       'Weil dieses Verzeichnis den DSGVO-Status nach der **tatsächlichen Verarbeitungskette** vergibt '
       'und nicht nur nach dem Sitz des Anbieters, steht der Eintrag dennoch auf **„bedingt“** statt '
       '„ja“ — dieselbe Linie gilt für vergleichbare deutsche Tools, die Nutzerinhalte an KI-APIs '
       'außerhalb der EU weiterreichen. Wer besonders sensible Angaben verarbeitet, sollte das kennen; '
       'für eine normale Bewerbung ist es in aller Regel unproblematisch.')

if old in content:
    content = content.replace(old, new); status = 'replaced inline'
else:
    status = 'TARGET NOT FOUND - no change'
if status.startswith('replaced'):
    rpp = requests.patch(f'{BASE}/{SITE}/posts/{PID}', json={'content': content}, headers=H, verify=False)
    print(f'post {PID}: {rpp.status_code} | {status} | {len(content)} chars')
else:
    print(f'post {PID}: {status}')
print('Done.')
