#!/usr/bin/env python3
"""Update existing AutoGen, Copilot Studio, GitHub Copilot entries with
Microsoft Build 2026 announcements (June 2-3, 2026)."""
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
print('✓ Logged in')

UPDATES = [
    # ---------------- Microsoft AutoGen → Agent Framework convergence ----------------
    {
        'eid': 20053, 'pid': 707,
        'data_patch': {
            'tagline': 'Forschungs-Framework für Multi-Agent-Systeme aus Microsoft Research — seit Build 2026 offiziell im neuen Microsoft Agent Framework (MAF 1.0) aufgegangen, der Konvergenz aus AutoGen und Semantic Kernel.',
            'lastUpdated': '2026-06-03',
        },
        'post_append': """

---

**Update Juni 2026 — Microsoft Build 2026:** AutoGen ist mit Build 2026 offiziell in das neue **Microsoft Agent Framework (MAF 1.0)** übergegangen — der formellen Konvergenz von **AutoGen** (Multi-Agent-Konversationen) und **Semantic Kernel** (Enterprise-Orchestrierung) zu einem einzigen, kommerziell unterstützten SDK für Python und .NET. Die bewährten AutoGen-Konzepte (GroupChat, Magentic-One) leben dort als stabile Multi-Agent-Orchestrierung weiter, ergänzt um ein einheitliches Agent-Harness mit Skills, Memory und Middleware. Bestehende AutoGen-Projekte bekommen damit einen klaren, produktionsreifen Migrationspfad — eigenständige AutoGen-Releases laufen aus. Wer neu startet, sollte direkt das **Microsoft Agent Framework** verwenden (eigener Eintrag im Verzeichnis)."""
    },
    # ---------------- Microsoft Copilot Studio — Build 2026 enhancements ----------------
    {
        'eid': 20055, 'pid': 709,
        'data_patch': {
            'lastUpdated': '2026-06-03',
        },
        'post_append': """

---

**Update Juni 2026 — Microsoft Build 2026:** Copilot Studio wurde auf Build 2026 deutlich erweitert. **Claude-Modelle** (Anthropic, via Microsoft Foundry) sind jetzt als Option in Custom Agents wählbar — neben den bisherigen Azure-OpenAI-Modellen und der neuen hauseigenen **MAI-Modellfamilie**. Mit **Frontier Tuning** (Private Preview, Roll-out in den kommenden Monaten) lassen sich Agents per Reinforcement Learning innerhalb der Compliance-Grenze auf eigene Daten und Prozesse abstimmen. Governance kommt über die neue **Agent Control Specification (ACS)** dazu — ein offener Standard mit definierten Interception-Points für Policies. Und mit **Windows 365 for Agents** (Preview) können Copilot-Studio-Agents in verwalteten Cloud-PCs Computer-Use-Aufgaben ausführen. Abgerechnet wird zunehmend über die neuen **Copilot Credits** ($0,01/Credit)."""
    },
    # ---------------- GitHub Copilot — Build 2026 desktop app + SDK ----------------
    {
        'eid': 19898, 'pid': 560,
        'data_patch': {
            'lastUpdated': '2026-06-03',
        },
        'post_append': """

---

**Update Juni 2026 — Microsoft Build 2026:** GitHub Copilot hat auf Build 2026 den Sprung von der IDE-Erweiterung zum eigenständigen **Agent-Cockpit** gemacht. Die neue **GitHub Copilot App** (Technical Preview, native Desktop-App für Windows, macOS und Linux) führt mehrere isolierte Agent-Sessions parallel — mit den Modi **Interactive / Plan / Autopilot**, **Agent Merge** (autonome PR-Auflösung), modellspezifischer Auswahl pro Session und Geräte-übergreifendem Handoff (pause/resume). Dazu kommt ein offizielles **GitHub Copilot SDK** (GA), um eigene Werkzeuge auf Copilot aufzusetzen, sowie das neue, leichte **MAI-Code-1-Flash**-Modell von Microsoft, das direkt in Copilot und VS Code eingebaut ist. Multi-Agent-Support in VS Code und tiefere GitHub-Azure-Integration runden das Update ab."""
    },
]

for upd in UPDATES:
    r = requests.get(f'{BASE}/{SITE}/elements/{upd["eid"]}', headers=H, verify=False)
    el = r.json()
    new_data = {**el['data'], **upd['data_patch']}
    rp = requests.patch(f'{BASE}/{SITE}/elements/{upd["eid"]}', json={'data': new_data}, headers=H, verify=False)
    print(f'element {upd["eid"]} ({new_data.get("slug")}): patch {rp.status_code}')
    r = requests.get(f'{BASE}/{SITE}/posts/{upd["pid"]}', headers=H, verify=False)
    post = r.json()
    new_content = post['content'] + upd['post_append']
    rpp = requests.patch(f'{BASE}/{SITE}/posts/{upd["pid"]}', json={'content': new_content}, headers=H, verify=False)
    print(f'  post {upd["pid"]}: patch {rpp.status_code} · {len(new_content)} chars total')

print('\n✓ Done.')
