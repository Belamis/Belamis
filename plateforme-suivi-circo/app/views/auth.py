"""Connexion, déconnexion, changement de mot de passe."""
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from ..db import get_db
from .helpers import login_required

bp = Blueprint("auth", __name__)


@bp.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        login_ = (request.form.get("login") or "").strip().lower()
        mdp = request.form.get("mot_de_passe") or ""
        user = get_db().execute(
            "SELECT * FROM utilisateurs WHERE login = ? AND actif = 1", (login_,)
        ).fetchone()
        if user is None or not check_password_hash(user["mot_de_passe"], mdp):
            flash("Identifiant ou mot de passe incorrect.", "erreur")
        else:
            session.clear()
            session["user_id"] = user["id"]
            suivant = request.args.get("next") or ""
            if not suivant.startswith("/") or suivant.startswith("//"):
                suivant = url_for("dashboard.index")
            return redirect(suivant)
    return render_template("login.html")


@bp.route("/logout", methods=("POST",))
def logout():
    session.clear()
    flash("Vous êtes déconnecté·e.", "info")
    return redirect(url_for("auth.login"))


@bp.route("/mon-compte", methods=("GET", "POST"))
@login_required
def mon_compte():
    if request.method == "POST":
        actuel = request.form.get("actuel") or ""
        nouveau = request.form.get("nouveau") or ""
        confirmation = request.form.get("confirmation") or ""
        if not check_password_hash(g.user["mot_de_passe"], actuel):
            flash("Le mot de passe actuel est incorrect.", "erreur")
        elif len(nouveau) < 8:
            flash("Le nouveau mot de passe doit contenir au moins 8 caractères.", "erreur")
        elif nouveau != confirmation:
            flash("La confirmation ne correspond pas.", "erreur")
        else:
            db = get_db()
            db.execute(
                "UPDATE utilisateurs SET mot_de_passe = ? WHERE id = ?",
                (generate_password_hash(nouveau), g.user["id"]),
            )
            db.commit()
            flash("Mot de passe modifié.", "succes")
            return redirect(url_for("dashboard.index"))
    return render_template("mon_compte.html")
