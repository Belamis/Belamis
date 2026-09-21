"""Gestion des comptes (administrateur uniquement)."""
from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.security import generate_password_hash

from ..db import get_db
from ..referentiels import ROLES
from .helpers import champ, get_or_404, role_required

bp = Blueprint("utilisateurs", __name__, url_prefix="/utilisateurs")


@bp.route("/")
@role_required()
def liste():
    users = get_db().execute("SELECT * FROM utilisateurs ORDER BY actif DESC, nom").fetchall()
    return render_template("utilisateurs/liste.html", users=users)


def _valider(nouveau):
    erreurs = []
    d = {
        "login": champ("login").lower(),
        "nom": champ("nom"),
        "fonction": champ("fonction"),
        "role": champ("role", "saisie"),
        "actif": 1 if request.form.get("actif") else 0,
        "mot_de_passe": request.form.get("mot_de_passe") or "",
    }
    if not d["login"] or " " in d["login"]:
        erreurs.append("L'identifiant est obligatoire et ne doit pas contenir d'espace.")
    if not d["nom"]:
        erreurs.append("Le nom est obligatoire.")
    if d["role"] not in ROLES:
        erreurs.append("Rôle inattendu.")
    if nouveau and len(d["mot_de_passe"]) < 8:
        erreurs.append("Le mot de passe doit contenir au moins 8 caractères.")
    if not nouveau and d["mot_de_passe"] and len(d["mot_de_passe"]) < 8:
        erreurs.append("Le nouveau mot de passe doit contenir au moins 8 caractères.")
    for e in erreurs:
        flash(e, "erreur")
    return d, bool(erreurs)


@bp.route("/nouveau", methods=("GET", "POST"))
@role_required()
def creer():
    if request.method == "POST":
        d, err = _valider(nouveau=True)
        if not err:
            db = get_db()
            if db.execute("SELECT 1 FROM utilisateurs WHERE login = ?", (d["login"],)).fetchone():
                flash("Cet identifiant existe déjà.", "erreur")
            else:
                db.execute(
                    "INSERT INTO utilisateurs (login, nom, fonction, mot_de_passe, role, actif) VALUES (?,?,?,?,?,?)",
                    (d["login"], d["nom"], d["fonction"], generate_password_hash(d["mot_de_passe"]),
                     d["role"], d["actif"]))
                db.commit()
                flash("Compte créé.", "succes")
                return redirect(url_for("utilisateurs.liste"))
        return render_template("utilisateurs/form.html", user=d, titre="Nouveau compte", nouveau=True)
    return render_template("utilisateurs/form.html", user={"actif": 1, "role": "saisie"},
                           titre="Nouveau compte", nouveau=True)


@bp.route("/<int:ident>/modifier", methods=("GET", "POST"))
@role_required()
def modifier(ident):
    user = get_or_404("utilisateurs", ident)
    if request.method == "POST":
        d, err = _valider(nouveau=False)
        if ident == g.user["id"] and (d["role"] != "admin" or not d["actif"]):
            flash("Vous ne pouvez pas retirer vos propres droits d'administration ni désactiver votre compte.", "erreur")
            err = True
        if not err:
            db = get_db()
            doublon = db.execute("SELECT 1 FROM utilisateurs WHERE login = ? AND id != ?",
                                 (d["login"], ident)).fetchone()
            if doublon:
                flash("Cet identifiant existe déjà.", "erreur")
            else:
                db.execute("UPDATE utilisateurs SET login=?, nom=?, fonction=?, role=?, actif=? WHERE id=?",
                           (d["login"], d["nom"], d["fonction"], d["role"], d["actif"], ident))
                if d["mot_de_passe"]:
                    db.execute("UPDATE utilisateurs SET mot_de_passe=? WHERE id=?",
                               (generate_password_hash(d["mot_de_passe"]), ident))
                db.commit()
                flash("Compte mis à jour.", "succes")
                return redirect(url_for("utilisateurs.liste"))
        d["id"] = ident
        return render_template("utilisateurs/form.html", user=d, titre="Modifier le compte", nouveau=False)
    return render_template("utilisateurs/form.html", user=user, titre="Modifier le compte", nouveau=False)
