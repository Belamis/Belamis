"""Personnels (enseignants, remplaçants, AESH) : fiche, ligne de classe, suivis."""
from flask import Blueprint, abort, current_app, flash, g, redirect, render_template, request, url_for

from ..db import get_db
from ..referentiels import (DISPOSITIFS_CLASSE, NIVEAUX_EFFECTIFS, SEXES, STATUTS_AVEC_CLASSE,
                            STATUTS_CODES, STATUTS_SUIVI, TYPES_SUIVI_ENSEIGNANT)
from ..stats import COLS_EFF, personnels_ecole
from .helpers import (champ, champ_bool, champ_date, champ_id, champ_int, debut_validation,
                      erreurs_flash, get_or_404, liste_ecoles, login_required, pagination,
                      role_required, valider_choix)

bp = Blueprint("enseignants", __name__, url_prefix="/enseignants")

SOMME_EFF = "(" + " + ".join(c for c in COLS_EFF if c != "eff_ulis") + ")"


@bp.route("/")
@login_required
def liste():
    q = (request.args.get("q") or "").strip()
    ecole_id = request.args.get("ecole") or ""
    statut = request.args.get("statut") or ""
    accompagnement = request.args.get("accompagnement") or ""
    org = request.args.get("org") or ""
    archives = request.args.get("archives") == "1"
    page = request.args.get("page", 1, type=int)

    where = " WHERE e.actif = ?"
    params = [0 if archives else 1]
    if q:
        where += " AND (e.nom LIKE ? OR e.prenom LIKE ? OR e.email LIKE ?)"
        params += [f"%{q}%"] * 3
    if ecole_id.isdigit():
        where += " AND e.ecole_id = ?"
        params.append(int(ecole_id))
    if statut:
        where += " AND e.statut = ?"
        params.append(statut)
    if accompagnement == "1":
        where += " AND e.accompagnement = 1"
    if org in ("0", "1"):
        where += " AND e.dans_organisation = ?"
        params.append(int(org))

    db = get_db()
    total = db.execute(f"SELECT COUNT(*) FROM enseignants e {where}", params).fetchone()[0]
    pag = pagination(page, total, current_app.config["PAR_PAGE"])
    enseignants = db.execute(
        f"""SELECT e.*, ec.nom AS ecole_nom, {SOMME_EFF} AS total_eleves,
              (SELECT MAX(date) FROM suivis_enseignants s WHERE s.enseignant_id = e.id
                 AND s.statut = 'Réalisé') AS derniere_visite,
              (SELECT COUNT(*) FROM suivis_enseignants s WHERE s.enseignant_id = e.id) AS nb_suivis
            FROM enseignants e LEFT JOIN ecoles ec ON ec.id = e.ecole_id
            {where} ORDER BY e.nom, e.prenom LIMIT ? OFFSET ?""",
        params + [current_app.config["PAR_PAGE"], pag["offset"]],
    ).fetchall()
    return render_template(
        "enseignants/liste.html", enseignants=enseignants, ecoles=liste_ecoles(), pag=pag,
        q=q, ecole_id=ecole_id, statut=statut, accompagnement=accompagnement, org=org, archives=archives,
    )


@bp.route("/<int:ident>")
@login_required
def fiche(ident):
    db = get_db()
    ens = db.execute(
        f"SELECT e.*, ec.nom AS ecole_nom, {SOMME_EFF} AS total_eleves FROM enseignants e "
        "LEFT JOIN ecoles ec ON ec.id = e.ecole_id WHERE e.id = ?", (ident,)).fetchone()
    if ens is None:
        abort(404)
    suivis = db.execute(
        "SELECT s.*, u.nom AS auteur FROM suivis_enseignants s LEFT JOIN utilisateurs u ON u.id = s.auteur_id "
        "WHERE s.enseignant_id = ? ORDER BY s.date DESC, s.id DESC", (ident,)).fetchall()
    eleves = db.execute(
        "SELECT id, nom, prenom, niveau, ppre, pap, pai, pps, rased, aesh FROM eleves "
        "WHERE enseignant_id = ? AND actif = 1 ORDER BY nom, prenom", (ident,)).fetchall()
    niveaux = [(lib, ens[c]) for c, lib, _ in NIVEAUX_EFFECTIFS if ens[c]]
    return render_template("enseignants/fiche.html", ens=ens, suivis=suivis, eleves=eleves, niveaux=niveaux)


COLONNES = ["nom", "prenom", "sexe", "email", "telephone", "ecole_id", "statut", "fonction", "anciennete",
            "dans_organisation", "dispositif", "salle", *COLS_EFF, "accompagnement", "observations", "actif"]


def _lire_formulaire():
    debut_validation()
    anc = champ("anciennete")
    d = {
        "nom": champ("nom").upper(),
        "prenom": champ("prenom"),
        "sexe": valider_choix(champ("sexe"), SEXES, "sexe"),
        "email": champ("email"),
        "telephone": champ("telephone"),
        "ecole_id": champ_id("ecole_id"),
        "statut": valider_choix(champ("statut", "PE"), STATUTS_CODES, "statut"),
        "fonction": champ("fonction"),
        "anciennete": int(anc) if anc.isdigit() else None,
        "dans_organisation": champ_bool("dans_organisation"),
        "dispositif": valider_choix(champ("dispositif"), DISPOSITIFS_CLASSE, "dispositif"),
        "salle": champ("salle"),
        "accompagnement": champ_bool("accompagnement"),
        "observations": champ("observations"),
        "actif": 1 if request.form.get("actif", "1") == "1" else 0,
    }
    for c in COLS_EFF:
        d[c] = champ_int(c)
        if d[c] < 0 or d[c] > 60:
            g.erreurs.append(f"Effectif invalide pour la colonne {c[4:].upper()}.")
    if not d["nom"]:
        g.erreurs.append("Le nom est obligatoire.")
    if anc and not anc.isdigit():
        g.erreurs.append("L'ancienneté est un nombre d'années.")
    if not d["dans_organisation"]:
        for c in COLS_EFF:
            d[c] = 0
        d["dispositif"] = ""
    return d


@bp.route("/nouveau", methods=("GET", "POST"))
@role_required("saisie")
def creer():
    if request.method == "POST":
        d = _lire_formulaire()
        if not erreurs_flash():
            db = get_db()
            cur = db.execute(
                f"INSERT INTO enseignants ({', '.join(COLONNES)}) VALUES ({', '.join(':' + c for c in COLONNES)})", d)
            db.commit()
            flash("Personnel créé.", "succes")
            if request.form.get("puis_nouveau"):
                return redirect(url_for("enseignants.creer", ecole=d["ecole_id"] or ""))
            return redirect(url_for("enseignants.fiche", ident=cur.lastrowid))
        return render_template("enseignants/form.html", ens=d, ecoles=liste_ecoles(), titre="Nouveau personnel")
    pre = {"ecole_id": request.args.get("ecole", type=int), "dans_organisation": 1, "statut": "PE"}
    return render_template("enseignants/form.html", ens=pre, ecoles=liste_ecoles(), titre="Nouveau personnel")


@bp.route("/<int:ident>/modifier", methods=("GET", "POST"))
@role_required("saisie")
def modifier(ident):
    ens = get_or_404("enseignants", ident)
    if request.method == "POST":
        d = _lire_formulaire()
        if not erreurs_flash():
            d["id"] = ident
            db = get_db()
            db.execute("UPDATE enseignants SET " + ", ".join(f"{c}=:{c}" for c in COLONNES)
                       + ", modifie_le=datetime('now') WHERE id=:id", d)
            db.commit()
            flash("Fiche mise à jour.", "succes")
            suivant = request.form.get("retour") or ""
            if suivant.startswith("/") and not suivant.startswith("//"):
                return redirect(suivant)
            return redirect(url_for("enseignants.fiche", ident=ident))
        return render_template("enseignants/form.html", ens=d, ecoles=liste_ecoles(), titre="Modifier la fiche")
    return render_template("enseignants/form.html", ens=ens, ecoles=liste_ecoles(), titre="Modifier la fiche")


@bp.route("/<int:ident>/archiver", methods=("POST",))
@role_required("saisie")
def archiver(ident):
    get_or_404("enseignants", ident)
    db = get_db()
    actif = 1 if request.form.get("restaurer") else 0
    db.execute("UPDATE enseignants SET actif = ?, modifie_le = datetime('now') WHERE id = ?", (actif, ident))
    db.commit()
    flash("Fiche restaurée." if actif else "Fiche archivée (mutation, départ…) : elle ne compte plus dans les effectifs.", "succes")
    return redirect(url_for("enseignants.fiche", ident=ident))


# ------------------------------------------------ saisie rapide des effectifs ---

@bp.route("/effectifs/<int:ecole_id>", methods=("GET", "POST"))
@role_required("saisie")
def effectifs(ecole_id):
    """Grille de saisie en masse : une ligne par enseignant de l'école, une colonne par niveau."""
    ecole = get_or_404("ecoles", ecole_id)
    db = get_db()
    lignes, _ = personnels_ecole(ecole_id)
    if request.method == "POST":
        erreurs = 0
        for l in lignes:
            valeurs = {}
            for c in COLS_EFF:
                v = request.form.get(f"{c}_{l['id']}", "").strip()
                if v and not v.isdigit():
                    erreurs += 1
                    v = "0"
                valeurs[c] = int(v or 0)
            valeurs["dispositif"] = request.form.get(f"dispositif_{l['id']}", "")
            if valeurs["dispositif"] not in DISPOSITIFS_CLASSE:
                valeurs["dispositif"] = ""
            valeurs["salle"] = (request.form.get(f"salle_{l['id']}") or "").strip()
            valeurs["id"] = l["id"]
            db.execute(
                "UPDATE enseignants SET " + ", ".join(f"{c}=:{c}" for c in COLS_EFF)
                + ", dispositif=:dispositif, salle=:salle, modifie_le=datetime('now') WHERE id=:id", valeurs)
        db.execute("UPDATE ecoles SET date_maj = date('now'), modifie_le = datetime('now') WHERE id = ?", (ecole_id,))
        db.commit()
        if erreurs:
            flash(f"{erreurs} valeur(s) non numérique(s) ont été remplacées par 0.", "erreur")
        flash("Effectifs enregistrés.", "succes")
        return redirect(url_for("ecoles.fiche", ident=ecole_id))
    return render_template("enseignants/effectifs.html", ecole=ecole, lignes=lignes)


# ---------------------------------------------------------------- suivis ---

def _lire_suivi():
    debut_validation()
    return {
        "date": champ_date("date", obligatoire=True),
        "type": valider_choix(champ("type"), TYPES_SUIVI_ENSEIGNANT, "type de suivi"),
        "objet": champ("objet"),
        "compte_rendu": champ("compte_rendu"),
        "points_forts": champ("points_forts"),
        "axes_progres": champ("axes_progres"),
        "actions_prevues": champ("actions_prevues"),
        "echeance": champ_date("echeance"),
        "statut": valider_choix(champ("statut", "Réalisé"), STATUTS_SUIVI, "statut"),
    }


@bp.route("/<int:ident>/suivis/nouveau", methods=("GET", "POST"))
@role_required("saisie")
def suivi_creer(ident):
    ens = get_or_404("enseignants", ident)
    if request.method == "POST":
        d = _lire_suivi()
        if not erreurs_flash():
            d.update(enseignant_id=ident, auteur_id=g.user["id"])
            db = get_db()
            db.execute(
                """INSERT INTO suivis_enseignants (enseignant_id, date, type, objet, compte_rendu, points_forts,
                   axes_progres, actions_prevues, echeance, statut, auteur_id)
                   VALUES (:enseignant_id, :date, :type, :objet, :compte_rendu, :points_forts,
                   :axes_progres, :actions_prevues, :echeance, :statut, :auteur_id)""", d)
            db.commit()
            flash("Suivi enregistré.", "succes")
            return redirect(url_for("enseignants.fiche", ident=ident))
        return render_template("enseignants/suivi_form.html", ens=ens, suivi=d, titre="Nouveau suivi")
    return render_template("enseignants/suivi_form.html", ens=ens, suivi=None, titre="Nouveau suivi")


@bp.route("/suivis/<int:sid>/modifier", methods=("GET", "POST"))
@role_required("saisie")
def suivi_modifier(sid):
    suivi = get_or_404("suivis_enseignants", sid)
    ens = get_or_404("enseignants", suivi["enseignant_id"])
    if request.method == "POST":
        d = _lire_suivi()
        if not erreurs_flash():
            d["id"] = sid
            db = get_db()
            db.execute(
                """UPDATE suivis_enseignants SET date=:date, type=:type, objet=:objet, compte_rendu=:compte_rendu,
                   points_forts=:points_forts, axes_progres=:axes_progres, actions_prevues=:actions_prevues,
                   echeance=:echeance, statut=:statut, modifie_le=datetime('now') WHERE id=:id""", d)
            db.commit()
            flash("Suivi mis à jour.", "succes")
            return redirect(url_for("enseignants.fiche", ident=ens["id"]))
        return render_template("enseignants/suivi_form.html", ens=ens, suivi=d, titre="Modifier le suivi")
    return render_template("enseignants/suivi_form.html", ens=ens, suivi=suivi, titre="Modifier le suivi")


@bp.route("/suivis/<int:sid>/supprimer", methods=("POST",))
@role_required("saisie")
def suivi_supprimer(sid):
    suivi = get_or_404("suivis_enseignants", sid)
    db = get_db()
    db.execute("DELETE FROM suivis_enseignants WHERE id = ?", (sid,))
    db.commit()
    flash("Suivi supprimé.", "succes")
    return redirect(url_for("enseignants.fiche", ident=suivi["enseignant_id"]))
