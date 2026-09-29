# -*- coding: utf-8 -*-
# Assemble les sujets du 2nd concours interne spécifique Mayotte dans data/mayotte.js.
# Sources des sujets : data/mayotte/{fr,ms,oral}.json. Lancer : python3 data/build_mayotte.py
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
DOSSIER = os.environ.get("MAYOTTE_DIR") or os.path.join(HERE, "mayotte")

DOMAINES = {
    "francais": "Écrit de français",
    "maths": "Écrit de maths-sciences",
    "oral": "Oraux d’admission",
}
TYPES = {
    "oral-qcm": "Compréhension orale (QCM)",
    "synthese": "Compréhension écrite et rédaction",
    "langue": "Connaissance de la langue",
    "didactique-fr": "Didactique du français",
    "probleme": "Problème complexe",
    "calcul": "Exercices de mathématiques",
    "sciences": "Sciences et technologie",
    "didactique-maths": "Didactique des mathématiques",
    "qualite": "Qualité de l’écrit",
    "expose": "Exposé",
    "entretien": "Entretien avec le jury",
    "valeurs": "Valeurs de la République",
}

GUIDE = """
<p>Le <strong>second concours interne spécifique à Mayotte</strong> est organisé par l’académie de Mayotte selon l’arrêté du 19 juillet 2016 et le décret n° 2007-1290 du 29 août 2007 (modifié par le décret n° 2023-928 du 7 octobre 2023). Son format n’est <strong>pas</strong> celui du CRPE BAC+3 : deux écrits sur 40 points, puis trois oraux.</p>

<h4>Les écrits d’admissibilité (4 heures chacun)</h4>
<table class="tab">
<tr><th>Épreuve</th><th>Parties</th><th>Points</th></tr>
<tr><td rowspan="4">Français : langue, langage, culture<br><small>sans calculatrice</small></td><td>1. Compréhension orale d’un texte didactique : lu deux fois, puis QCM (30 min)</td><td>8</td></tr>
<tr><td>2. Compréhension écrite et rédaction : réponse construite sur un corpus</td><td>12</td></tr>
<tr><td>3. Connaissance de la langue et didactique à partir de productions d’élèves</td><td>14</td></tr>
<tr><td>Correction syntaxique et qualité écrite</td><td>6</td></tr>
<tr><td rowspan="4">Mathématiques, sciences et technologie<br><small>calculatrice autorisée</small></td><td>1. Problème complexe : extraire et organiser l’information de plusieurs documents</td><td>10</td></tr>
<tr><td>2. Exercices : vrai/faux, QCM, géométrie, Scratch, probabilités, sciences</td><td>12</td></tr>
<tr><td>3. Didactique des mathématiques : analyse de productions d’élèves</td><td>14</td></tr>
<tr><td>Qualité syntaxique et écrite</td><td>4</td></tr>
</table>
<p>Chaque écrit est noté sur 40 ; <strong>une note de 10 ou moins est éliminatoire</strong>.</p>

<h4>Les oraux d’admission</h4>
<ul>
<li><strong>Mise en situation professionnelle</strong> (/50) : 1 h de préparation ; exposé de 10 min (/20) puis entretien de 20 min (/30). Tu choisis un dossier de 5 pages au plus parmi trois, chacun dans une discipline différente de l’école primaire.</li>
<li><strong>Étude de cas</strong> sur le système éducatif et la dimension éthique du métier (/50) : 1 h de préparation ; exposé de 10 min (/15), entretien de 20 min (/25), et 10 points pour les valeurs de la République. Le dossier de 4 pages au plus décrit une situation ordinaire de l’école primaire, avec trois questions. Les <strong>particularités de Mayotte</strong> sont attendues.</li>
<li><strong>Épreuve au choix</strong> (/20) : langue vivante (allemand, anglais, arabe ou espagnol : 20 min de préparation, 20 min d’épreuve, niveau B2 attendu) ou EPS (danse de 2 min au plus avec une note d’intention, ou 1 500 m ; puis 15 min d’entretien).</li>
</ul>

<h4>Ce qui tombe : les annales 2023 à 2025</h4>
<ul>
<li><strong>Compréhension orale</strong> : toujours un texte sur la lecture. En 2023, l’enseignement explicite de la compréhension (Maryse Bianco, conférence de consensus de 2016) ; en 2024, le décodage et la fluence (guide orange du CP, Stanislas Dehaene) ; en 2025, le vocabulaire et les connaissances sur le monde (<em>Lector &amp; Lectrix</em>, Sylvie Cèbe et Roland Goigoux).</li>
<li><strong>Corpus</strong> : l’enfance et l’école. En 2023, Vallès, Rousseau et des textes sur la lecture littéraire ; en 2024, Annie Ernaux, Jeanne Benameur, Prévert et un texte de didactique (question : la relation entre l’école, la famille et l’enfant) ; en 2025, Twain, Saint-Exupéry, Vallès, Bazin et Alain-Fournier (question : le regard de l’enfant sur le monde).</li>
<li><strong>Langue et didactique</strong> : une production d’élève de CM à analyser (erreurs classées, annotations de l’enseignant, consigne probable, grille d’autoévaluation, remédiation), la nature et la fonction des mots et des propositions, les propositions coordonnées et juxtaposées, les réécritures en changeant de personne, la formation des mots (dérivation), les valeurs des temps (impératif en 2024).</li>
<li><strong>Problème complexe</strong> : Mayotte en contexte. En 2023, la nutrition et l’IMC ; en 2024, l’eau et l’énergie du dessalement ; en 2025, la crise de l’eau et la croissance de la population.</li>
<li><strong>Exercices</strong> : vrai/faux justifiés, QCM, suites de motifs, Thalès (le puits du berger), probabilités et Scratch, fonction affine (°C et °F), et une question de sciences (le poids sur Mars, la respiration).</li>
<li><strong>Didactique des mathématiques</strong> : des situations de maternelle (les boîtes d’œufs), le dénombrement d’une grande collection, la droite graduée (évaluations repères de CM1), les problèmes de partage (schéma en barres), et la multiplication d’un décimal par 10 (« on ajoute un zéro », une règle fausse).</li>
</ul>

<h4>Ce que le jury attend (rapports 2023 et 2025)</h4>
<ul>
<li>Lire le sujet <strong>en profondeur</strong> et garder un temps pour relire sa copie ; soigner l’écriture et la présentation, comme au tableau.</li>
<li>À l’oral, <strong>poser une problématique</strong>, annoncer un plan, conclure avec une ouverture ; ne pas <strong>paraphraser</strong> les documents un par un, mais les croiser ; répondre aux trois questions.</li>
<li>Maîtriser les <strong>savoirs à enseigner</strong> (par exemple la différence entre nombre et chiffre) et le vocabulaire du métier : ne pas confondre <em>programmation</em> et <em>progression</em>, ni un Bulletin officiel et les programmes.</li>
<li>Connaître les <strong>ressources institutionnelles</strong> : programmes, socle commun, guides fondamentaux (dits « guides orange »), Eduscol. Le jury reproche à des candidats de proposer des vidéos YouTube.</li>
<li>Connaître le <strong>système éducatif</strong> et les <strong>spécificités de Mayotte</strong>, se positionner en futur fonctionnaire, garant des valeurs de la République et de la <strong>laïcité</strong>.</li>
<li>S’exprimer dans une langue orale correcte, sans familiarités : le rapport 2025 cite des fautes comme « je leurs explique » et des erreurs d’accord en genre.</li>
<li>Avoir été contractuel n’assure pas la réussite ; les candidats issus d’une licence des métiers de l’éducation sont, selon le rapport 2025, bien préparés.</li>
</ul>

<h4>Quelques chiffres</h4>
<ul>
<li>Session 2023 : 143 inscrits, 52 présents, 22 admissibles, 11 admis.</li>
<li>Session 2025 : 81 inscrits, 10 admissibles, 8 admis. Moyenne à l’admissibilité : 9,13/20 ; à l’admission : 11,63/20.</li>
<li>Session 2027 (calendrier de l’académie) : inscriptions du 1<sup>er</sup> octobre au 25 novembre 2026 ; écrits les 5 et 6 avril 2027 ; oraux du 24 mai au 3 juin 2027.</li>
</ul>
<p class="doc-src">Sources : académie de Mayotte, pages « 2nd concours interne de recrutement de professeurs des écoles – spécifique Mayotte » et « Consultation des sujets antérieurs » ; rapports de jury 2023 et 2025 ; devenirenseignant.gouv.fr. Les sujets de Belamis sont des sujets originaux construits sur ce modèle, pas des annales.</p>
"""


def charger():
    sujets = []
    for nom in ("fr.json", "ms.json", "oral.json"):
        chemin = os.path.join(DOSSIER, nom)
        if not os.path.exists(chemin):
            print("absent :", nom)
            continue
        sujets += json.load(open(chemin, encoding="utf-8"))["sujets"]
    return sujets


def verifier(sujets):
    ids = set()
    for s in sujets:
        assert s["id"] not in ids, s["id"]
        ids.add(s["id"])
        assert s["domaine"] in DOMAINES, (s["id"], s["domaine"])
        tot = 0
        for p in s["parties"]:
            pt = round(sum(q["points"] for q in p["questions"]), 6)
            assert abs(pt - p["points"]) < 1e-6, (s["id"], p["id"], pt, p["points"])
            tot += p["points"]
            qids = set()
            for q in p["questions"]:
                assert q["type"] in TYPES, (s["id"], q["type"])
                assert q["id"] not in qids, (s["id"], p["id"], q["id"])
                qids.add(q["id"])
                if "options" in q:
                    b = q["bonnes"]
                    assert b and all(0 <= i < len(q["options"]) for i in b), (s["id"], q["id"])
            if "audio" in p:
                assert p["audio"]["titre"] and p["audio"]["texte"], s["id"]
        assert abs(tot - s["total"]) < 1e-6, (s["id"], tot, s["total"])
        if s["domaine"] != "oral":
            assert s["total"] == 40 and s["eliminatoire"] == 10 and s["duree"] == 14400, s["id"]
        else:
            assert s["total"] == 50 and s["duree"] == 3600, s["id"]


ordre = {"francais": 0, "maths": 1, "oral": 2}
sujets = charger()
verifier(sujets)
sujets.sort(key=lambda s: (ordre[s["domaine"]], s["id"]))
data = {
    "domaines": DOMAINES,
    "types": TYPES,
    "guide": GUIDE,
    "guideTitre": "Le concours spécifique Mayotte : format, annales 2023-2025 et conseils des jurys",
    "sujets": sujets,
}
sortie = os.environ.get("MAYOTTE_OUT") or os.path.join(HERE, "mayotte.js")
with open(sortie, "w", encoding="utf-8") as f:
    f.write("/* Généré par data/build_mayotte.py : 2nd concours interne spécifique Mayotte. */\n")
    f.write("window.BELAMIS_MAYOTTE = " + json.dumps(data, ensure_ascii=False) + ";\n")
n = {d: sum(1 for s in sujets if s["domaine"] == d) for d in DOMAINES}
print(n, "questions :", sum(len(p["questions"]) for s in sujets for p in s["parties"]), "taille :", os.path.getsize(sortie) // 1024, "Ko")
