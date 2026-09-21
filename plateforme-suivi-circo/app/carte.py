"""Carte scolaire : montée pédagogique, divisions, E/D, salles, postes hors classe.

Le constat de rentrée est repris des fiches école (lignes de classe saisies dans
l'organisation pédagogique) ; il peut être saisi à la main école par école.
Les prévisions se calculent par montée pédagogique, selon le type d'école :

* maternelle  : PS saisis, MS = PS constat, GS = MS constat ;
* élémentaire : CP saisis (arrivées de GS), CE1 = CP, CE2 = CE1, CM1 = CE2, CM2 = CM1 ;
* primaire    : PS saisis puis montée interne complète, CP = GS de la même école.
"""
from .db import get_db
from .referentiels import CYCLES  # noqa: F401  (import conservé pour les gabarits)

NIVEAUX_CARTE = [("ps", "PS"), ("ms", "MS"), ("gs", "GS"), ("cp", "CP"),
                 ("ce1", "CE1"), ("ce2", "CE2"), ("cm1", "CM1"), ("cm2", "CM2")]
MATERNELLE = ["ps", "ms", "gs"]
ELEMENTAIRE = ["cp", "ce1", "ce2", "cm1", "cm2"]
TOUS = MATERNELLE + ELEMENTAIRE
COL_EFF = {n: f"eff_{n}" for n, _ in NIVEAUX_CARTE}

# Mots-clés de secteur servant à rattacher une élémentaire à ses maternelles.
SECTEURS = ["KANGANI", "TREVANI", "MAIRIE", "PLATEAU"]

POSTES_DEFAUT = [
    ("Coordonnateur REP / REP+", ""), ("CPC", "Généraliste"), ("CPC", "Spécialisé"),
    ("CPC", "Sans CAFIPEMF"), ("ERUN", ""), ("RASED", "Maître E"), ("RASED", "Maître G"),
    ("RASED", "Psychologue"), ("UPE2A", ""),
    ("APAJH – ITSP « Itinérant spécialisé » (lien ASH)", ""),
    ("TR-ZIL brigade de remplacement", ""), ("Secrétaire de circonscription", "Administratif"),
]

CHAMPS_SAISIE = ["constat_manuel", "c_ps", "c_ms", "c_gs", "c_cp", "c_ce1", "c_ce2", "c_cm1", "c_cm2",
                 "div_constat", "div_cp_ce1", "div_ce2_cm1_cm2", "div_rotation", "div_mat", "div_elem",
                 "ps_prevus", "cp_prevus", "ouverture", "fermeture", "nb_salles", "observations"]


def niveaux_du_type(type_ecole):
    if type_ecole == "Maternelle":
        return MATERNELLE
    if type_ecole == "Élémentaire":
        return ELEMENTAIRE
    return TOUS


def _sans_accent(texte):
    import unicodedata
    return "".join(c for c in unicodedata.normalize("NFD", str(texte))
                   if unicodedata.category(c) != "Mn").upper()


def secteurs_de(nom):
    return [k for k in SECTEURS if k in _sans_accent(nom)]


def lignes_ecole(ecole_id):
    """Enseignants devant classe d'une école (une ligne = une division)."""
    return get_db().execute(
        "SELECT * FROM enseignants WHERE ecole_id = ? AND actif = 1 AND dans_organisation = 1",
        (ecole_id,)).fetchall()


def carte_ecole(ecole, campagne):
    """Retourne la ligne de carte scolaire d'une école, créée à la volée si absente."""
    db = get_db()
    ligne = db.execute("SELECT * FROM carte_scolaire WHERE ecole_id = ? AND campagne = ?",
                       (ecole["id"], campagne)).fetchone()
    if ligne is None:
        db.execute("INSERT INTO carte_scolaire (ecole_id, campagne) VALUES (?, ?)", (ecole["id"], campagne))
        db.commit()
        ligne = db.execute("SELECT * FROM carte_scolaire WHERE ecole_id = ? AND campagne = ?",
                           (ecole["id"], campagne)).fetchone()
    return ligne


def calculer(ecole, carte, enseignants):
    """Calcule une ligne complète de carte scolaire (constat, prévisions, mesures, salles)."""
    auto = {n: sum(p[COL_EFF[n]] or 0 for p in enseignants) for n, _ in NIVEAUX_CARTE}
    manuel = bool(carte["constat_manuel"])
    constat = {n: (carte[f"c_{n}"] or 0) if manuel else auto[n] for n, _ in NIVEAUX_CARTE}
    niveaux = niveaux_du_type(ecole["type"])
    total_c = sum(constat[n] for n in niveaux)

    div_auto = len(enseignants)
    div = carte["div_constat"] if carte["div_constat"] is not None else div_auto

    def a_cp_ce1(p):
        return (p["eff_cp"] or 0) > 0 or (p["eff_ce1"] or 0) > 0

    def a_maternelle(p):
        return any((p[COL_EFF[n]] or 0) > 0 for n in MATERNELLE)

    div_cp_ce1 = carte["div_cp_ce1"] if carte["div_cp_ce1"] is not None else sum(1 for p in enseignants if a_cp_ce1(p))
    div_ce2 = (carte["div_ce2_cm1_cm2"] if carte["div_ce2_cm1_cm2"] is not None
               else sum(1 for p in enseignants if not a_cp_ce1(p)))
    div_rot = (carte["div_rotation"] if carte["div_rotation"] is not None
               else sum(1 for p in enseignants if p["dispositif"] == "Duo"))
    div_mat = (carte["div_mat"] if carte["div_mat"] is not None
               else sum(1 for p in enseignants if a_maternelle(p)))
    div_elem = (carte["div_elem"] if carte["div_elem"] is not None
                else sum(1 for p in enseignants if not a_maternelle(p)))

    prev = {n: 0 for n, _ in NIVEAUX_CARTE}
    if ecole["type"] == "Maternelle":
        prev["ps"] = carte["ps_prevus"] or 0
        prev["ms"], prev["gs"] = constat["ps"], constat["ms"]
    elif ecole["type"] == "Élémentaire":
        prev["cp"] = carte["cp_prevus"] or 0
        prev["ce1"], prev["ce2"] = constat["cp"], constat["ce1"]
        prev["cm1"], prev["cm2"] = constat["ce2"], constat["cm1"]
    else:
        prev["ps"] = carte["ps_prevus"] or 0
        prev["ms"], prev["gs"], prev["cp"] = constat["ps"], constat["ms"], constat["gs"]
        prev["ce1"], prev["ce2"] = constat["cp"], constat["ce1"]
        prev["cm1"], prev["cm2"] = constat["ce2"], constat["cm1"]
    total_p = sum(prev[n] for n in niveaux)

    ouv, ferm = carte["ouverture"] or 0, carte["fermeture"] or 0
    div_apres = div + ouv - ferm
    salles = carte["nb_salles"] if carte["nb_salles"] is not None else (ecole["nb_salles"] or 0)
    arrondi = lambda x: round(x, 1)  # noqa: E731

    return {
        "ecole": ecole, "carte": carte, "niveaux": niveaux, "auto": auto, "manuel": manuel,
        "constat": constat, "prev": prev, "total_c": total_c, "total_p": total_p,
        "div": div, "div_auto": div_auto, "div_cp_ce1": div_cp_ce1, "div_ce2_cm1_cm2": div_ce2,
        "div_rotation": div_rot, "div_mat": div_mat, "div_elem": div_elem,
        "ouverture": ouv, "fermeture": ferm, "div_apres": div_apres,
        "ed": arrondi(total_c / div) if div else None,
        "ed_avant": arrondi(total_p / div) if div else None,
        "ed_apres": arrondi(total_p / div_apres) if div_apres else None,
        "evolution": total_p - total_c,
        "pct": arrondi((total_p - total_c) / total_c * 100) if total_c else None,
        "salles": salles, "salles_necessaires": div_apres, "ecart_salles": salles - div_apres,
    }


def lignes_campagne(campagne, type_ecole=None):
    """Toutes les lignes calculées d'une campagne, éventuellement filtrées par type d'école."""
    sql = "SELECT * FROM ecoles"
    params = []
    if type_ecole:
        sql += " WHERE type = ?"
        params.append(type_ecole)
    sql += " ORDER BY nom"
    resultat = []
    for ecole in get_db().execute(sql, params).fetchall():
        resultat.append(calculer(ecole, carte_ecole(ecole, campagne), lignes_ecole(ecole["id"])))
    return resultat


def totaux(lignes):
    """Agrège une liste de lignes calculées."""
    t = {k: sum(l[k] for l in lignes) for k in
         ("total_c", "total_p", "div", "div_apres", "ouverture", "fermeture", "div_cp_ce1",
          "div_ce2_cm1_cm2", "div_rotation", "div_mat", "div_elem", "salles", "salles_necessaires")}
    t["constat"] = {n: sum(l["constat"][n] for l in lignes) for n, _ in NIVEAUX_CARTE}
    t["prev"] = {n: sum(l["prev"][n] for l in lignes) for n, _ in NIVEAUX_CARTE}
    t["evolution"] = t["total_p"] - t["total_c"]
    t["pct"] = round(t["evolution"] / t["total_c"] * 100, 1) if t["total_c"] else None
    t["ed"] = round(t["total_c"] / t["div"], 1) if t["div"] else None
    t["ed_avant"] = round(t["total_p"] / t["div"], 1) if t["div"] else None
    t["ed_apres"] = round(t["total_p"] / t["div_apres"], 1) if t["div_apres"] else None
    t["ecart_salles"] = t["salles"] - t["salles_necessaires"]
    t["nb_ecoles"] = len(lignes)
    return t


def gs_rattaches(ligne, toutes_maternelles):
    """GS du constat des maternelles du même secteur (aide à la saisie des CP prévus)."""
    secteurs = secteurs_de(ligne["ecole"]["nom"])
    if not secteurs:
        return {"nb": 0, "noms": []}
    liees = [m for m in toutes_maternelles if set(secteurs_de(m["ecole"]["nom"])) & set(secteurs)]
    return {"nb": sum(m["constat"]["gs"] for m in liees), "noms": [m["ecole"]["nom"] for m in liees]}


def postes(campagne):
    """Postes hors classe d'une campagne, créés depuis le modèle au premier accès."""
    db = get_db()
    lignes = db.execute("SELECT * FROM postes_hors_classe WHERE campagne = ? ORDER BY rang, id",
                        (campagne,)).fetchall()
    if not lignes:
        for rang, (poste, specialite) in enumerate(POSTES_DEFAUT):
            db.execute("INSERT INTO postes_hors_classe (campagne, rang, poste, specialite) VALUES (?, ?, ?, ?)",
                       (campagne, rang, poste, specialite))
        db.commit()
        lignes = db.execute("SELECT * FROM postes_hors_classe WHERE campagne = ? ORDER BY rang, id",
                            (campagne,)).fetchall()
    return [dict(l, apres=(l["supports"] or 0) + (l["ouverture"] or 0) - (l["fermeture"] or 0))
            for l in map(dict, lignes)]


def totaux_postes(lignes):
    return {k: sum(l[k] or 0 for l in lignes) for k in
            ("supports", "affectations", "ouverture", "fermeture", "apres")}


def campagnes():
    """Campagnes déjà saisies, la plus récente d'abord."""
    lignes = get_db().execute(
        "SELECT campagne FROM carte_scolaire UNION SELECT campagne FROM postes_hors_classe "
        "ORDER BY campagne DESC").fetchall()
    return [l["campagne"] for l in lignes]
