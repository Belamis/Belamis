"""Calculs statistiques (fiche école, tableau de bord, exports) à partir des lignes de classe."""
from collections import OrderedDict

from .db import get_db
from .referentiels import (NIVEAUX_EFFECTIFS, STATUTS_AVEC_CLASSE, STATUTS_CODES,
                           TRANCHES_ANCIENNETE)

COLS_EFF = [c for c, _, _ in NIVEAUX_EFFECTIFS]
COLS_HORS_ULIS = [c for c, _, cy in NIVEAUX_EFFECTIFS if cy]


def total_classe(ligne):
    """Effectif d'une ligne de classe, hors ULIS (les élèves ULIS sont déjà comptés dans leur classe)."""
    return sum(ligne[c] or 0 for c in COLS_HORS_ULIS)


def personnels_ecole(ecole_id):
    db = get_db()
    dans_org = db.execute(
        "SELECT * FROM enseignants WHERE ecole_id = ? AND actif = 1 AND dans_organisation = 1 "
        "ORDER BY eff_ps > 0 DESC, eff_ms > 0 DESC, eff_gs > 0 DESC, eff_cp > 0 DESC, eff_ce1 > 0 DESC, "
        "eff_ce2 > 0 DESC, eff_cm1 > 0 DESC, eff_cm2 > 0 DESC, salle, nom, prenom", (ecole_id,)).fetchall()
    hors_org = db.execute(
        "SELECT * FROM enseignants WHERE ecole_id = ? AND actif = 1 AND dans_organisation = 0 "
        "ORDER BY statut, nom, prenom", (ecole_id,)).fetchall()
    return dans_org, hors_org


def stats_ecole(ecole, dans_org, hors_org):
    """Reproduit le bloc « Statistiques — calculées automatiquement » de la fiche école."""
    eff = OrderedDict((c, sum(l[c] or 0 for l in dans_org)) for c in COLS_EFF)
    classes = OrderedDict((c, sum(1 for l in dans_org if (l[c] or 0) > 0)) for c in COLS_EFF)
    total_eleves = sum(eff[c] for c in COLS_HORS_ULIS)
    total_classes = sum(classes.values())

    anciennetes = [l["anciennete"] for l in dans_org if l["anciennete"] is not None]
    anc_moy = round(sum(anciennetes) / len(anciennetes), 1) if anciennetes else None
    tranches = [(lib, sum(1 for a in anciennetes if lo <= a <= hi)) for lib, lo, hi in TRANCHES_ANCIENNETE]

    statuts = []
    for code in STATUTS_CODES:
        h = sum(1 for l in dans_org if l["statut"] == code and l["sexe"] == "H")
        f = sum(1 for l in dans_org if l["statut"] == code and l["sexe"] == "F")
        n = sum(1 for l in dans_org if l["statut"] == code)
        if n:
            statuts.append({"statut": code, "hommes": h, "femmes": f, "total": n})
    tot_h = sum(s["hommes"] for s in statuts)
    tot_f = sum(s["femmes"] for s in statuts)

    dispositifs = []
    for d in ("Duo", "Solo"):
        lignes = [l for l in dans_org if l["dispositif"] == d]
        dispositifs.append({
            "dispositif": d, "nb": len(lignes),
            "cp": sum(1 for l in lignes if l["eff_cp"]), "ce1": sum(1 for l in lignes if l["eff_ce1"]),
        })

    controles = [
        {"libelle": "Nb enseignants = Σ statuts", "ok": len(dans_org) == sum(s["total"] for s in statuts),
         "a": len(dans_org), "b": sum(s["total"] for s in statuts)},
        {"libelle": "Nb classes (info. générales) = Σ classes par niveau",
         "ok": ecole["nb_classes"] == total_classes, "a": ecole["nb_classes"], "b": total_classes},
        {"libelle": "Effectif total élèves > 0", "ok": total_eleves > 0, "a": total_eleves, "b": ""},
        {"libelle": "Sexe renseigné pour tous les personnels",
         "ok": all(l["sexe"] for l in dans_org + hors_org),
         "a": sum(1 for l in dans_org + hors_org if l["sexe"]), "b": len(dans_org) + len(hors_org)},
    ]
    return {
        "effectifs": eff, "classes": classes, "total_eleves": total_eleves, "total_classes": total_classes,
        "total_ulis": eff["eff_ulis"], "nb_enseignants": len(dans_org), "nb_hors_org": len(hors_org),
        "anciennete_moyenne": anc_moy, "tranches": tranches, "statuts": statuts,
        "total_hommes": tot_h, "total_femmes": tot_f, "dispositifs": dispositifs, "controles": controles,
        "cycles": {
            1: eff["eff_ps"] + eff["eff_ms"] + eff["eff_gs"],
            2: eff["eff_cp"] + eff["eff_ce1"] + eff["eff_ce2"],
            3: eff["eff_cm1"] + eff["eff_cm2"],
        },
        "eleves_par_classe": round(total_eleves / total_classes, 1) if total_classes else None,
    }


def effectifs_par_ecole():
    """Table écoles × niveaux (feuille « EFFECTIFS PAR NIVEAUX »)."""
    somme_eff = ", ".join(f"COALESCE(SUM(e.{c}), 0) AS {c}" for c in COLS_EFF)
    somme_cl = ", ".join(f"COALESCE(SUM(e.{c} > 0), 0) AS cl_{c}" for c in COLS_EFF)
    lignes = get_db().execute(
        f"""SELECT ec.id, ec.nom, ec.type, ec.commune, ec.nb_classes, ec.date_maj, {somme_eff}, {somme_cl},
              COALESCE(SUM(e.id IS NOT NULL), 0) AS nb_enseignants
            FROM ecoles ec LEFT JOIN enseignants e
              ON e.ecole_id = ec.id AND e.actif = 1 AND e.dans_organisation = 1
            GROUP BY ec.id ORDER BY ec.commune, ec.nom""").fetchall()
    resultat = []
    for l in lignes:
        d = dict(l)
        d["cycle1"] = d["eff_ps"] + d["eff_ms"] + d["eff_gs"]
        d["cycle2"] = d["eff_cp"] + d["eff_ce1"] + d["eff_ce2"]
        d["cycle3"] = d["eff_cm1"] + d["eff_cm2"]
        d["total"] = d["cycle1"] + d["cycle2"] + d["cycle3"]
        d["nb_classes_calc"] = sum(d[f"cl_{c}"] for c in COLS_EFF)
        resultat.append(d)
    totaux = {k: sum(d[k] for d in resultat) for k in
              COLS_EFF + [f"cl_{c}" for c in COLS_EFF] + ["cycle1", "cycle2", "cycle3", "total",
                                                            "nb_enseignants", "nb_classes_calc", "nb_classes"]}
    return resultat, totaux


def synthese_circonscription():
    """Chiffres du tableau de bord (feuille « BORD »)."""
    db = get_db()
    ecoles, totaux = effectifs_par_ecole()
    nb_personnels = db.execute(
        "SELECT COUNT(*) FROM enseignants WHERE actif = 1 AND statut != 'AESH'").fetchone()[0]
    par_niveau = []
    for c, lib, cy in NIVEAUX_EFFECTIFS:
        nb_el, nb_cl = totaux[c], totaux[f"cl_{c}"]
        par_niveau.append({"niveau": lib, "cycle": cy, "eleves": nb_el, "classes": nb_cl,
                           "ratio": round(nb_el / nb_cl, 1) if nb_cl else None})
    return {
        "nb_ecoles": len(ecoles),
        "eleves_hors_ulis": totaux["total"],
        "eleves_ulis": totaux["eff_ulis"],
        "classes": totaux["nb_classes_calc"],
        "enseignants": totaux["nb_enseignants"],
        "personnels": nb_personnels,
        "cycles": {1: totaux["cycle1"], 2: totaux["cycle2"], 3: totaux["cycle3"]},
        "par_niveau": par_niveau,
        "ecoles": ecoles,
        "totaux": totaux,
    }


def est_statut_avec_classe(statut):
    return statut in STATUTS_AVEC_CLASSE
