# -*- coding: utf-8 -*-
# Assemble les séances de révision (rappels de cours et quiz) de chaque concours dans data/revisions.js.
# Sources : data/revisions/*.json. Lancer : python3 data/build_revisions.py
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
DOSSIER = os.path.join(HERE, "revisions")

TYPES = {"quiz": "Quiz", "application": "Application"}
PAQUETS = {
    "bac3": (("bac3_fm.json", "bac3_e2.json"), {
        "francais": "Français", "maths": "Mathématiques", "hg": "Histoire-géo-EMC",
        "sciences": "Sciences", "arts": "Arts", "anglais": "Anglais"}),
    "myt2": (("myt2.json",), {"francais": "Français", "maths": "Maths-sciences", "oral": "Oraux"}),
    "p1": (("p1.json",), {"ecrit": "Écrit", "oral": "Oral et épreuve facultative"}),
}


def verifier(s, domaines, ids):
    assert s["id"] not in ids, s["id"]
    ids.add(s["id"])
    assert s["domaine"] in domaines, (s["id"], s["domaine"])
    assert s.get("revision") is True and 600 <= s["duree"] <= 3600, s["id"]
    tot = 0
    for p in s["parties"]:
        pt = round(sum(q["points"] for q in p["questions"]), 6)
        assert abs(pt - p["points"]) < 1e-6, (s["id"], p["id"], pt)
        tot += p["points"]
        for q in p["questions"]:
            assert q["type"] in TYPES, (s["id"], q["type"])
            if q["type"] == "quiz":
                b = q["bonnes"]
                assert b and all(0 <= i < len(q["options"]) for i in b), (s["id"], q["id"])
    assert abs(tot - s["total"]) < 1e-6, (s["id"], tot, s["total"])


ids = set()
sortie = {}
for cle, (fichiers, domaines) in PAQUETS.items():
    sujets = []
    for nom in fichiers:
        chemin = os.path.join(DOSSIER, nom)
        if not os.path.exists(chemin):
            print("absent :", nom)
            continue
        sujets += json.load(open(chemin, encoding="utf-8"))["sujets"]
    for s in sujets:
        verifier(s, domaines, ids)
    ordre = {d: i for i, d in enumerate(domaines)}
    sujets.sort(key=lambda s: (ordre[s["domaine"]], s.get("num", 0), s["id"]))
    utilises = {s["domaine"] for s in sujets}
    sortie[cle] = {"domaines": {d: l for d, l in domaines.items() if d in utilises}, "types": TYPES, "sujets": sujets}
    print(cle, len(sujets), "séances")

chemin = os.path.join(HERE, "revisions.js")
with open(chemin, "w", encoding="utf-8") as f:
    f.write("/* Généré par data/build_revisions.py : séances de révision conseillées, par concours. */\n")
    f.write("window.BELAMIS_REV = " + json.dumps(sortie, ensure_ascii=False) + ";\n")
print("taille :", os.path.getsize(chemin) // 1024, "Ko")
