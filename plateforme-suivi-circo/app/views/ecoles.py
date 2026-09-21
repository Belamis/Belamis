"""Écoles : liste, fiche complète (signalétique + organisation pédagogique + statistiques), saisie."""
from flask import Blueprint, flash, g, redirect, render_template, request, url_for

from ..db import get_db
from ..referentiels import EDUCATION_PRIORITAIRE, TYPES_ECOLE
from ..stats import personnels_ecole, stats_ecole
from .helpers import (champ, champ_date, champ_int, debut_validation, erreurs_flash, get_or_404,
                      login_required, role_required, valider_choix)

bp = Blueprint("ecoles", __name__, url_prefix="/ecoles")


@bp.route("/")
@login_required
def liste():
    q = (request.args.get("q") or "").strip()
    type_ = request.args.get("type") or ""
    ep = request.args.get("ep") or ""
    sql = """SELECT ec.*,
               (SELECT COUNT(*) FROM enseignants e WHERE e.ecole_id = ec.id AND e.actif = 1 AND e.dans_organisation = 1) AS nb_enseignants,
               (SELECT COALESCE(SUM(eff_ps+eff_ms+eff_gs+eff_cp+eff_ce1+eff_ce2+eff_cm1+eff_cm2), 0)
                  FROM enseignants e WHERE e.ecole_id = ec.id AND e.actif = 1 AND e.dans_organisation = 1) AS nb_eleves,
               (SELECT COUNT(*) FROM eleves e WHERE e.ecole_id = ec.id AND e.actif = 1) AS nb_eleves_suivis
             FROM ecoles ec WHERE 1 = 1"""
    params = []
    if q:
        sql += " AND (ec.nom LIKE ? OR ec.commune LIKE ? OR ec.rne LIKE ? OR ec.directeur LIKE ?)"
        params += [f"%{q}%"] * 4
    if type_:
        sql += " AND ec.type = ?"
        params.append(type_)
    if ep:
        sql += " AND ec.education_prioritaire = ?"
        params.append(ep)
    sql += " ORDER BY ec.commune, ec.nom"
    ecoles = get_db().execute(sql, params).fetchall()
    return render_template("ecoles/liste.html", ecoles=ecoles, q=q, type_=type_, ep=ep)


@bp.route("/<int:ident>")
@login_required
def fiche(ident):
    ecole = get_or_404("ecoles", ident)
    dans_org, hors_org = personnels_ecole(ident)
    stats = stats_ecole(ecole, dans_org, hors_org)
    eleves = get_db().execute(
        """SELECT el.*, en.nom AS ens_nom, en.prenom AS ens_prenom
           FROM eleves el LEFT JOIN enseignants en ON en.id = el.enseignant_id
           WHERE el.ecole_id = ? AND el.actif = 1 ORDER BY el.niveau, el.nom, el.prenom""", (ident,)).fetchall()
    return render_template("ecoles/fiche.html", ecole=ecole, dans_org=dans_org, hors_org=hors_org,
                           stats=stats, eleves=eleves)


def _lire_formulaire():
    debut_validation()
    d = {
        "nom": champ("nom"),
        "type": valider_choix(champ("type", "Primaire"), TYPES_ECOLE, "type"),
        "rne": champ("rne").upper(),
        "commune": champ("commune"),
        "adresse": champ("adresse"),
        "telephone": champ("telephone"),
        "email": champ("email"),
        "horaires": champ("horaires"),
        "apc": champ("apc"),
        "directeur": champ("directeur"),
        "secretaire": champ("secretaire"),
        "ots": champ("ots"),
        "faex_nom": champ("faex_nom"),
        "faex_telephone": champ("faex_telephone"),
        "faex_email": champ("faex_email"),
        "faex_pct": champ("faex_pct"),
        "education_prioritaire": valider_choix(
            champ("education_prioritaire", "Hors EP"), EDUCATION_PRIORITAIRE, "éducation prioritaire"),
        "nb_salles": champ_int("nb_salles"),
        "nb_classes": champ_int("nb_classes"),
        "decharge_direction": champ_int("decharge_direction"),
        "date_maj": champ_date("date_maj"),
        "notes": champ("notes"),
    }
    if not d["nom"]:
        g.erreurs.append("Le nom de l'école est obligatoire.")
    if not 0 <= d["decharge_direction"] <= 100:
        g.erreurs.append("La décharge de direction est un pourcentage entre 0 et 100.")
    return d


COLONNES = ["nom", "type", "rne", "commune", "adresse", "telephone", "email", "horaires", "apc", "directeur",
            "secretaire", "ots", "faex_nom", "faex_telephone", "faex_email", "faex_pct", "education_prioritaire",
            "nb_salles", "nb_classes", "decharge_direction", "date_maj", "notes"]


@bp.route("/nouvelle", methods=("GET", "POST"))
@role_required("saisie")
def creer():
    if request.method == "POST":
        d = _lire_formulaire()
        if not erreurs_flash():
            db = get_db()
            cur = db.execute(
                f"INSERT INTO ecoles ({', '.join(COLONNES)}) VALUES ({', '.join(':' + c for c in COLONNES)})", d)
            db.commit()
            flash("École créée. Vous pouvez maintenant saisir son organisation pédagogique.", "succes")
            return redirect(url_for("ecoles.fiche", ident=cur.lastrowid))
        return render_template("ecoles/form.html", ecole=d, titre="Nouvelle école")
    return render_template("ecoles/form.html", ecole=None, titre="Nouvelle école")


@bp.route("/<int:ident>/modifier", methods=("GET", "POST"))
@role_required("saisie")
def modifier(ident):
    ecole = get_or_404("ecoles", ident)
    if request.method == "POST":
        d = _lire_formulaire()
        if not erreurs_flash():
            d["id"] = ident
            db = get_db()
            db.execute(
                "UPDATE ecoles SET " + ", ".join(f"{c}=:{c}" for c in COLONNES)
                + ", modifie_le=datetime('now') WHERE id=:id", d)
            db.commit()
            flash("Fiche école mise à jour.", "succes")
            return redirect(url_for("ecoles.fiche", ident=ident))
        return render_template("ecoles/form.html", ecole=d, titre="Modifier la fiche école")
    return render_template("ecoles/form.html", ecole=ecole, titre="Modifier la fiche école")


@bp.route("/<int:ident>/supprimer", methods=("POST",))
@role_required()
def supprimer(ident):
    db = get_db()
    get_or_404("ecoles", ident)
    lies = db.execute(
        "SELECT (SELECT COUNT(*) FROM enseignants WHERE ecole_id = ?) + "
        "(SELECT COUNT(*) FROM eleves WHERE ecole_id = ?)", (ident, ident)).fetchone()[0]
    if lies:
        flash("Impossible de supprimer : des personnels ou des élèves sont rattachés à cette école.", "erreur")
        return redirect(url_for("ecoles.fiche", ident=ident))
    db.execute("DELETE FROM ecoles WHERE id = ?", (ident,))
    db.commit()
    flash("École supprimée.", "succes")
    return redirect(url_for("ecoles.liste"))
