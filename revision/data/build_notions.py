# -*- coding: utf-8 -*-
# Assemble la bibliothèque « Révision des notions » (une fiche par notion) dans data/notions.js.
# Sources : data/notions/*.json. Lancer : python3 data/build_notions.py
import glob, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
TYPES = {"quiz": "Quiz", "application": "Application"}
PAQUETS = {
    "fr": ("fr_", {"grammaire": "Grammaire", "conjugaison": "Conjugaison", "orthographe": "Orthographe",
                   "lexique": "Lexique", "texte": "Texte et méthode"}),
    "ma": ("ma_", {"nombres": "Nombres", "calcul": "Calcul et fonctions", "geometrie": "Géométrie",
                   "grandeurs": "Grandeurs et mesures", "donnees": "Données et probabilités"}),
}

ids = set()
sortie = {}
for cle, (prefixe, domaines) in PAQUETS.items():
    sujets = []
    for chemin in sorted(glob.glob(os.path.join(HERE, "notions", prefixe + "*.json"))):
        sujets += json.load(open(chemin, encoding="utf-8"))["sujets"]
    for s in sujets:
        assert s["id"] not in ids, s["id"]
        ids.add(s["id"])
        assert s["domaine"] in domaines, (s["id"], s["domaine"])
        tot = 0
        for p in s["parties"]:
            pt = round(sum(q["points"] for q in p["questions"]), 6)
            assert abs(pt - p["points"]) < 1e-6, (s["id"], p["id"])
            tot += p["points"]
            for q in p["questions"]:
                assert q["type"] in TYPES, (s["id"], q["type"])
                if q["type"] == "quiz":
                    assert q["bonnes"] and all(0 <= i < len(q["options"]) for i in q["bonnes"]), (s["id"], q["id"])
        assert abs(tot - s["total"]) < 1e-6, s["id"]
        s["revision"] = True
        s["fiche"] = True
    ordre = {d: i for i, d in enumerate(domaines)}
    sujets.sort(key=lambda s: (ordre[s["domaine"]], s.get("num", 0), s["id"]))
    utilises = {s["domaine"] for s in sujets}
    sortie[cle] = {"domaines": {d: l for d, l in domaines.items() if d in utilises}, "types": TYPES, "sujets": sujets}
    print(cle, len(sujets), "fiches")

chemin = os.path.join(HERE, "notions.js")
with open(chemin, "w", encoding="utf-8") as f:
    f.write("/* Généré par data/build_notions.py : révision des notions, une fiche par notion. */\n")
    f.write("window.BELAMIS_NOTIONS = " + json.dumps(sortie, ensure_ascii=False) + ";\n")
print("taille :", os.path.getsize(chemin) // 1024, "Ko")
