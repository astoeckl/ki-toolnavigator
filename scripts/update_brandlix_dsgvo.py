#!/usr/bin/env python3
"""Update Brandlix entry after the vendor disclosed operator, Art. 27 EU rep and
full-EU hosting (2026-08-10). Keeps dsgvo='bedingt' but for substantive reasons."""
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
JH = {'Authorization': f'Bearer {r.json()["access_token"]}', 'Content-Type':'application/json'}
print('✓ Logged in')

EID, PID = 47847, 782

# ---- 1. Patch structured fields ----
el = requests.get(f'{BASE}/{SITE}/elements/{EID}', headers=JH, verify=False).json()
data = el['data']
data['origin'] = 'Vereinigte Arabische Emirate'
data['dsgvo'] = 'bedingt'
data['lastUpdated'] = '2026-08-10'
data['pros'] = [
    'Agentischer End-to-End-Ansatz: plant, entscheidet, schreibt und postet',
    'Brand-Voice-KI schreibt aus Tonfall, Leistungen und FAQ des Kunden',
    'Erzeugt Bilder/Videos/Karussells; Unified Inbox; Freigabe vor jeder Aktion; 10 Plattformen',
    'Hosting vollständig in der EU (Hetzner FI, Neon & DigitalOcean Frankfurt) + EU-Vertreter nach Art. 27 DSGVO',
]
data['cons'] = [
    'Verantwortlicher sitzt in den VAE (Drittland) — Controller außerhalb der EU',
    'Backups über Cloudflare R2 (US-Unternehmen) in der Kette',
    'Autonomie erfordert Kontrolle — Qualität hängt stark vom Markenprofil ab',
    'Junges Tool; Zuverlässigkeit je Plattform-API kann schwanken',
]
rp = requests.patch(f'{BASE}/{SITE}/elements/{EID}', json={'data': data}, headers=JH, verify=False)
print('element patch:', rp.status_code, '| origin=', data['origin'], '| dsgvo=', data['dsgvo'])

# ---- 2. Fix the outdated DSGVO paragraph in the overview post ----
post = requests.get(f'{BASE}/{SITE}/posts/{PID}', headers=JH, verify=False).json()
content = post['content']
old = ("Beim **Datenschutz** macht die Website keine konkreten DSGVO- oder Hosting-Angaben, "
       "und **Herkunft bzw. Betreiber** sind öffentlich nicht ausgewiesen; wer personenbezogene "
       "Daten oder Kundeninhalte verarbeitet, sollte den DSGVO-Status daher unabhängig klären "
       "(der Anbieter signalisiert Bereitschaft, dazu offen Auskunft zu geben).")
new = ("Beim **Datenschutz** hat der Anbieter nach der Aufnahme konkrete Angaben nachgereicht "
       "(Stand 10. August 2026): Betreiber ist die **Fresh Wave Trading L.L.C mit Sitz in Dubai (VAE)**, "
       "als **EU-Vertreter nach Art. 27 DSGVO** ist die K&H Vertriebs GmbH (Frankfurt/Oder) benannt. "
       "Das **Hosting liegt vollständig in der EU** — Anwendungsserver bei Hetzner (Helsinki), Datenbank "
       "bei Neon sowie Cache/Job-Queue bei DigitalOcean (jeweils Frankfurt am Main), Backups über "
       "Cloudflare R2 — und laut Anbieter besteht **kein Datenbestand außerhalb der EU**. Das ist eine "
       "deutliche Verbesserung gegenüber dem Ausgangszustand ohne Angaben. Der Eintrag bleibt dennoch "
       "bei **DSGVO „bedingt“**, weil der **Verantwortliche in einem Drittland (VAE)** sitzt und für die "
       "**Backups mit Cloudflare ein US-Unternehmen** in der Kette steht — beides sollte man je nach "
       "eigener Risikoabwägung prüfen. Die Angaben stammen vom Anbieter und sind im Impressum "
       "(brandlix.io/imprint) hinterlegt.")

if old in content:
    content = content.replace(old, new)
    status = 'replaced inline'
else:
    content = content + "\n\n---\n\n**Update (10. August 2026):** " + new
    status = 'appended (inline target not found)'
rpp = requests.patch(f'{BASE}/{SITE}/posts/{PID}', json={'content': content}, headers=JH, verify=False)
print('post patch:', rpp.status_code, '|', status, '|', len(content), 'chars')
print('\n✓ Done.')
