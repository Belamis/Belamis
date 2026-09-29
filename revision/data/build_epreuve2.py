# -*- coding: utf-8 -*-
# Assemble les sujets de la 2e épreuve (HG-EMC, sciences, arts, anglais) dans data/epreuve2.js.
# Lancer : python3 data/build_epreuve2.py
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import sujets_hg

DOMAINES = {
    "hg": "Histoire-géographie-EMC",
    "sciences": "Sciences et technologie",
    "arts": "Arts",
    "anglais": "Anglais",
}
TYPES = {
    "histoire": "Histoire", "geographie": "Géographie", "emc": "EMC", "reperes": "Repères et définitions",
    "physique": "Physique-chimie", "svt": "Sciences de la vie et de la Terre", "techno": "Technologie",
    "demarche": "Démarche scientifique", "conceptions": "Conceptions d’élèves",
    "arts-plastiques": "Arts plastiques", "musique": "Éducation musicale", "hda": "Histoire des arts",
    "comprehension": "Anglais : compréhension", "expression": "Anglais : expression",
}

sujets = list(sujets_hg.SUJETS)
for fichier, dom in (("e2_sciences.json", "sciences"), ("e2_arts.json", "arts"), ("e2_anglais.json", "anglais")):
    chemin = os.path.join(HERE, fichier)
    if not os.path.exists(chemin):
        print("absent :", fichier)
        continue
    for s in json.load(open(chemin))["sujets"]:
        s["domaine"] = dom
        sujets.append(s)

# contrôles : barèmes et types
for s in sujets:
    tot = 0
    for p in s["parties"]:
        pt = round(sum(q["points"] for q in p["questions"]), 6)
        assert abs(pt - p["points"]) < 1e-6, (s["id"], p["id"], pt, p["points"])
        for q in p["questions"]:
            assert q["type"] in TYPES, (s["id"], q["type"])
        tot += p["points"]
    s["total"] = round(tot, 6)
    if not s.get("entrainement"):
        assert abs(tot - 20) < 1e-6, (s["id"], tot)
    s.setdefault("titre", s["id"])

ids = [s["id"] for s in sujets]
assert len(ids) == len(set(ids)), "identifiants en double"

data = {"types": TYPES, "domaines": DOMAINES, "guide": sujets_hg.GUIDE, "sujets": sujets}
out = "/* Généré par build_epreuve2.py : 2e épreuve d'admissibilité du CRPE BAC+3. */\n"
out += "window.BELAMIS_EPREUVE2 = " + json.dumps(data, ensure_ascii=False) + ";\n"
open(os.path.join(HERE, "epreuve2.js"), "w").write(out)
from collections import Counter
c = Counter(s["domaine"] for s in sujets)
print({d: c[d] for d in DOMAINES}, "questions :", sum(len(p["questions"]) for s in sujets for p in s["parties"]), "taille :", len(out) // 1024, "Ko")
