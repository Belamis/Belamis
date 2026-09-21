"""Carte scolaire : synthèse de circonscription, grilles de saisie, postes hors classe."""
from datetime import date

from flask import Blueprint, flash, redirect, render_template, request, url_for

from ..carte import (CHAMPS_SAISIE, NIVEAUX_CARTE, carte_ecole, gs_rattaches, lignes_campagne,
                     postes, totaux, totaux_postes)
from ..db import get_db, lire_parametres
from .helpers import login_required, role_required

bp = Blueprint("carte", __name__, url_prefix="/carte")

TYPES = [("Maternelle", "Écoles maternelles"), ("Élémentaire", "Écoles élémentaires"),
         ("Primaire", "Écoles primaires")]

CHAMPS_ENTIERS_NULLABLES = ("div_constat", "div_cp_ce1", "div_ce2_cm1_cm2", "div_rotation",
                            "div_mat", "div_elem", "nb_salles")


def campagne_courante():
    """Campagne par défaut : R n+1 de l'année scolaire en cours (rentrée suivante)."""
    params = lire_parametres()
    if params.get("campagne_carte"):
        return params["campagne_carte"]
    today = date.today()
    an = today.year + 1 if today.month >= 9 else today.year
    return f"R{an}"


@bp.route("/")
@login_required
def tableau():
    campagne = request.args.get("campagne") or campagne_courante()
    groupes = []
    for type_ecole, titre in TYPES:
        lignes = lignes_campagne(campagne, type_ecole)
        groupes.append({"type": type_ecole, "titre": titre, "lignes": lignes, "totaux": totaux(lignes)})
    toutes = [l for g in groupes for l in g["lignes"]]
    maternelles = next(g["lignes"] for g in groupes if g["type"] == "Maternelle")
    for g in groupes:
        if g["type"] == "Élémentaire":
            for l in g["lignes"]:
                l["gs_rattaches"] = gs_rattaches(l, maternelles)
    lignes_postes = postes(campagne)
    manquants = [l for l in toutes
                 if not (l["carte"]["cp_prevus"] if l["ecole"]["type"] == "Élémentaire"
                         else l["carte"]["ps_prevus"])]
    return render_template(
        "carte/tableau.html", campagne=campagne, groupes=groupes, general=totaux(toutes),
        postes=lignes_postes, totaux_postes=totaux_postes(lignes_postes), niveaux=NIVEAUX_CARTE,
        manquants=manquants, seuil_ed=float(lire_parametres().get("seuil_ed") or 26),
    )


def _entier(valeur, defaut=0, nullable=False):
    valeur = (valeur or "").strip()
    if not valeur:
        return None if nullable else defaut
    try:
        return int(float(valeur.replace(",", ".")))
    except ValueError:
        return None if nullable else defaut


@bp.route("/<campagne>/enregistrer", methods=("POST",))
@role_required("saisie")
def enregistrer(campagne):
    """Enregistre une section (un type d'école) de la grille de carte scolaire."""
    db = get_db()
    ids = request.form.getlist("ecole_id")
    for ecole_id in ids:
        ecole = db.execute("SELECT * FROM ecoles WHERE id = ?", (ecole_id,)).fetchone()
        if ecole is None:
            continue
        carte_ecole(ecole, campagne)  # crée la ligne si la campagne est nouvelle
        d = {"constat_manuel": 1 if request.form.get(f"constat_manuel_{ecole_id}") else 0,
             "observations": (request.form.get(f"observations_{ecole_id}") or "").strip()}
        for niveau, _ in NIVEAUX_CARTE:
            d[f"c_{niveau}"] = _entier(request.form.get(f"c_{niveau}_{ecole_id}"))
        for champ in ("ps_prevus", "cp_prevus", "ouverture", "fermeture"):
            d[champ] = _entier(request.form.get(f"{champ}_{ecole_id}"))
        for champ in CHAMPS_ENTIERS_NULLABLES:
            d[champ] = _entier(request.form.get(f"{champ}_{ecole_id}"), nullable=True)
        d["ecole_id"], d["campagne"] = ecole_id, campagne
        db.execute(
            "UPDATE carte_scolaire SET " + ", ".join(f"{c}=:{c}" for c in CHAMPS_SAISIE)
            + ", modifie_le=datetime('now') WHERE ecole_id=:ecole_id AND campagne=:campagne", d)
    db.commit()
    flash(f"Carte scolaire enregistrée ({len(ids)} école(s)).", "succes")
    return redirect(url_for("carte.tableau", campagne=campagne))


@bp.route("/<campagne>/postes", methods=("POST",))
@role_required("saisie")
def enregistrer_postes(campagne):
    postes(campagne)  # crée les lignes du modèle si la campagne est nouvelle
    db = get_db()
    for ident in request.form.getlist("poste_id"):
        valeurs = {c: _entier(request.form.get(f"{c}_{ident}")) for c in
                   ("supports", "affectations", "ouverture", "fermeture")}
        valeurs["id"] = ident
        db.execute("UPDATE postes_hors_classe SET supports=:supports, affectations=:affectations, "
                   "ouverture=:ouverture, fermeture=:fermeture WHERE id=:id", valeurs)
    db.commit()
    flash("Postes hors classe enregistrés.", "succes")
    return redirect(url_for("carte.tableau", campagne=campagne))
