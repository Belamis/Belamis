"""Élèves et leurs suivis (équipes éducatives, PPRE, signalements…)."""
from flask import Blueprint, abort, current_app, flash, g, redirect, render_template, request, url_for

from ..db import get_db
from ..referentiels import AESH, MDPH, NIVEAUX, SEXES_ELEVE, STATUTS_SUIVI, TYPES_SUIVI_ELEVE
from .helpers import (champ, champ_bool, champ_date, champ_id, debut_validation, erreurs_flash,
                      get_or_404, liste_ecoles, login_required, pagination, role_required,
                      valider_choix)

bp = Blueprint("eleves", __name__, url_prefix="/eleves")

FILTRES_DISPOSITIF = {
    "ppre": "el.ppre = 1", "pap": "el.pap = 1", "pai": "el.pai = 1", "pps": "el.pps = 1",
    "rased": "el.rased = 1", "aesh": "el.aesh != 'Non'", "mdph": "el.mdph != 'Aucun dossier'",
    "tous": "(el.ppre OR el.pap OR el.pai OR el.pps OR el.rased OR el.aesh != 'Non' OR el.mdph != 'Aucun dossier')",
    "aucun": "NOT (el.ppre OR el.pap OR el.pai OR el.pps OR el.rased OR el.aesh != 'Non' OR el.mdph != 'Aucun dossier')",
}


def _enseignants_de(ecole_id=None):
    sql = "SELECT id, nom, prenom, salle, ecole_id FROM enseignants WHERE actif = 1 AND dans_organisation = 1"
    params = []
    if ecole_id:
        sql += " AND ecole_id = ?"
        params.append(ecole_id)
    return get_db().execute(sql + " ORDER BY nom, prenom", params).fetchall()


@bp.route("/")
@login_required
def liste():
    q = (request.args.get("q") or "").strip()
    ecole_id = request.args.get("ecole") or ""
    niveau = request.args.get("niveau") or ""
    dispositif = request.args.get("dispositif") or ""
    archives = request.args.get("archives") == "1"
    page = request.args.get("page", 1, type=int)

    where = " WHERE el.actif = ?"
    params = [0 if archives else 1]
    if q:
        where += " AND (el.nom LIKE ? OR el.prenom LIKE ?)"
        params += [f"%{q}%"] * 2
    if ecole_id.isdigit():
        where += " AND el.ecole_id = ?"
        params.append(int(ecole_id))
    if niveau:
        where += " AND el.niveau = ?"
        params.append(niveau)
    if dispositif in FILTRES_DISPOSITIF:
        where += " AND " + FILTRES_DISPOSITIF[dispositif]

    db = get_db()
    total = db.execute(f"SELECT COUNT(*) FROM eleves el {where}", params).fetchone()[0]
    pag = pagination(page, total, current_app.config["PAR_PAGE"])
    eleves = db.execute(
        f"""SELECT el.*, ec.nom AS ecole_nom, en.nom AS ens_nom, en.prenom AS ens_prenom,
              (SELECT MAX(date) FROM suivis_eleves s WHERE s.eleve_id = el.id) AS dernier_suivi,
              (SELECT COUNT(*) FROM suivis_eleves s WHERE s.eleve_id = el.id) AS nb_suivis
            FROM eleves el LEFT JOIN ecoles ec ON ec.id = el.ecole_id
            LEFT JOIN enseignants en ON en.id = el.enseignant_id
            {where} ORDER BY el.nom, el.prenom LIMIT ? OFFSET ?""",
        params + [current_app.config["PAR_PAGE"], pag["offset"]],
    ).fetchall()
    return render_template(
        "eleves/liste.html", eleves=eleves, ecoles=liste_ecoles(), pag=pag, q=q, ecole_id=ecole_id,
        niveau=niveau, dispositif=dispositif, archives=archives,
    )


@bp.route("/<int:ident>")
@login_required
def fiche(ident):
    db = get_db()
    el = db.execute(
        """SELECT el.*, ec.nom AS ecole_nom, en.nom AS ens_nom, en.prenom AS ens_prenom
           FROM eleves el LEFT JOIN ecoles ec ON ec.id = el.ecole_id
           LEFT JOIN enseignants en ON en.id = el.enseignant_id WHERE el.id = ?""", (ident,)).fetchone()
    if el is None:
        abort(404)
    suivis = db.execute(
        "SELECT s.*, u.nom AS auteur FROM suivis_eleves s LEFT JOIN utilisateurs u ON u.id = s.auteur_id "
        "WHERE s.eleve_id = ? ORDER BY s.date DESC, s.id DESC", (ident,)).fetchall()
    return render_template("eleves/fiche.html", el=el, suivis=suivis)


def _lire_formulaire():
    debut_validation()
    d = {
        "nom": champ("nom").upper(),
        "prenom": champ("prenom"),
        "date_naissance": champ_date("date_naissance"),
        "sexe": valider_choix(champ("sexe"), SEXES_ELEVE, "sexe"),
        "ecole_id": champ_id("ecole_id"),
        "enseignant_id": champ_id("enseignant_id"),
        "niveau": champ("niveau"),
        "ppre": champ_bool("ppre"),
        "pap": champ_bool("pap"),
        "pai": champ_bool("pai"),
        "pps": champ_bool("pps"),
        "rased": champ_bool("rased"),
        "aesh": valider_choix(champ("aesh", "Non"), AESH, "AESH"),
        "mdph": valider_choix(champ("mdph", "Aucun dossier"), MDPH, "MDPH"),
        "situation": champ("situation"),
        "notes": champ("notes"),
        "actif": 1 if request.form.get("actif", "1") == "1" else 0,
    }
    if not d["nom"]:
        g.erreurs.append("Le nom est obligatoire.")
    if d["niveau"] and d["niveau"] not in NIVEAUX:
        g.erreurs.append("Niveau inattendu.")
    if d["enseignant_id"]:
        ens = get_db().execute("SELECT ecole_id FROM enseignants WHERE id = ?", (d["enseignant_id"],)).fetchone()
        if ens is None:
            g.erreurs.append("Enseignant·e introuvable.")
        elif d["ecole_id"] and ens["ecole_id"] and ens["ecole_id"] != d["ecole_id"]:
            g.erreurs.append("L'enseignant·e choisi·e n'exerce pas dans l'école sélectionnée.")
    return d


@bp.route("/nouveau", methods=("GET", "POST"))
@role_required("saisie")
def creer():
    if request.method == "POST":
        d = _lire_formulaire()
        if not erreurs_flash():
            db = get_db()
            cur = db.execute(
                """INSERT INTO eleves (nom, prenom, date_naissance, sexe, ecole_id, enseignant_id, niveau,
                   ppre, pap, pai, pps, rased, aesh, mdph, situation, notes, actif)
                   VALUES (:nom, :prenom, :date_naissance, :sexe, :ecole_id, :enseignant_id, :niveau,
                   :ppre, :pap, :pai, :pps, :rased, :aesh, :mdph, :situation, :notes, :actif)""", d)
            db.commit()
            flash("Élève créé·e.", "succes")
            return redirect(url_for("eleves.fiche", ident=cur.lastrowid))
        return render_template("eleves/form.html", el=d, ecoles=liste_ecoles(),
                               enseignants=_enseignants_de(), titre="Nouvel·le élève")
    pre = {"ecole_id": request.args.get("ecole", type=int), "enseignant_id": request.args.get("enseignant", type=int)}
    return render_template("eleves/form.html", el=pre, ecoles=liste_ecoles(),
                           enseignants=_enseignants_de(), titre="Nouvel·le élève")


@bp.route("/<int:ident>/modifier", methods=("GET", "POST"))
@role_required("saisie")
def modifier(ident):
    el = get_or_404("eleves", ident)
    if request.method == "POST":
        d = _lire_formulaire()
        if not erreurs_flash():
            d["id"] = ident
            db = get_db()
            db.execute(
                """UPDATE eleves SET nom=:nom, prenom=:prenom, date_naissance=:date_naissance, sexe=:sexe,
                   ecole_id=:ecole_id, enseignant_id=:enseignant_id, niveau=:niveau, ppre=:ppre, pap=:pap,
                   pai=:pai, pps=:pps, rased=:rased, aesh=:aesh, mdph=:mdph, situation=:situation,
                   notes=:notes, actif=:actif, modifie_le=datetime('now') WHERE id=:id""", d)
            db.commit()
            flash("Fiche mise à jour.", "succes")
            return redirect(url_for("eleves.fiche", ident=ident))
        return render_template("eleves/form.html", el=d, ecoles=liste_ecoles(),
                               enseignants=_enseignants_de(), titre="Modifier la fiche")
    return render_template("eleves/form.html", el=el, ecoles=liste_ecoles(),
                           enseignants=_enseignants_de(), titre="Modifier la fiche")


@bp.route("/<int:ident>/archiver", methods=("POST",))
@role_required("saisie")
def archiver(ident):
    get_or_404("eleves", ident)
    db = get_db()
    actif = 1 if request.form.get("restaurer") else 0
    db.execute("UPDATE eleves SET actif = ?, modifie_le = datetime('now') WHERE id = ?", (actif, ident))
    db.commit()
    flash("Fiche restaurée." if actif else "Fiche archivée (départ, fin de scolarité…).", "succes")
    return redirect(url_for("eleves.fiche", ident=ident))


# ---------------------------------------------------------------- suivis ---

def _lire_suivi():
    debut_validation()
    return {
        "date": champ_date("date", obligatoire=True),
        "type": valider_choix(champ("type"), TYPES_SUIVI_ELEVE, "type de suivi"),
        "objet": champ("objet"),
        "compte_rendu": champ("compte_rendu"),
        "decisions": champ("decisions"),
        "participants": champ("participants"),
        "echeance": champ_date("echeance"),
        "statut": valider_choix(champ("statut", "Réalisé"), STATUTS_SUIVI, "statut"),
    }


@bp.route("/<int:ident>/suivis/nouveau", methods=("GET", "POST"))
@role_required("saisie")
def suivi_creer(ident):
    el = get_or_404("eleves", ident)
    if request.method == "POST":
        d = _lire_suivi()
        if not erreurs_flash():
            d.update(eleve_id=ident, auteur_id=g.user["id"])
            db = get_db()
            db.execute(
                """INSERT INTO suivis_eleves (eleve_id, date, type, objet, compte_rendu, decisions, participants,
                   echeance, statut, auteur_id)
                   VALUES (:eleve_id, :date, :type, :objet, :compte_rendu, :decisions, :participants,
                   :echeance, :statut, :auteur_id)""", d)
            db.commit()
            flash("Suivi enregistré.", "succes")
            return redirect(url_for("eleves.fiche", ident=ident))
        return render_template("eleves/suivi_form.html", el=el, suivi=d, titre="Nouveau suivi")
    return render_template("eleves/suivi_form.html", el=el, suivi=None, titre="Nouveau suivi")


@bp.route("/suivis/<int:sid>/modifier", methods=("GET", "POST"))
@role_required("saisie")
def suivi_modifier(sid):
    suivi = get_or_404("suivis_eleves", sid)
    el = get_or_404("eleves", suivi["eleve_id"])
    if request.method == "POST":
        d = _lire_suivi()
        if not erreurs_flash():
            d["id"] = sid
            db = get_db()
            db.execute(
                """UPDATE suivis_eleves SET date=:date, type=:type, objet=:objet, compte_rendu=:compte_rendu,
                   decisions=:decisions, participants=:participants, echeance=:echeance, statut=:statut,
                   modifie_le=datetime('now') WHERE id=:id""", d)
            db.commit()
            flash("Suivi mis à jour.", "succes")
            return redirect(url_for("eleves.fiche", ident=el["id"]))
        return render_template("eleves/suivi_form.html", el=el, suivi=d, titre="Modifier le suivi")
    return render_template("eleves/suivi_form.html", el=el, suivi=suivi, titre="Modifier le suivi")


@bp.route("/suivis/<int:sid>/supprimer", methods=("POST",))
@role_required("saisie")
def suivi_supprimer(sid):
    suivi = get_or_404("suivis_eleves", sid)
    db = get_db()
    db.execute("DELETE FROM suivis_eleves WHERE id = ?", (sid,))
    db.commit()
    flash("Suivi supprimé.", "succes")
    return redirect(url_for("eleves.fiche", ident=suivi["eleve_id"]))
