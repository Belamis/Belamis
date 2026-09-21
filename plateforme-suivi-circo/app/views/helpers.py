"""Fonctions utilitaires partagées par les vues."""
import functools
from datetime import datetime

from flask import abort, flash, g, redirect, request, session, url_for

from ..db import get_db


def charger_utilisateur():
    uid = session.get("user_id")
    if uid is None:
        g.user = None
    else:
        g.user = get_db().execute(
            "SELECT * FROM utilisateurs WHERE id = ? AND actif = 1", (uid,)
        ).fetchone()
        if g.user is None:
            session.clear()


def login_required(vue):
    @functools.wraps(vue)
    def wrapper(*args, **kwargs):
        charger_utilisateur()
        if g.user is None:
            return redirect(url_for("auth.login", next=request.full_path))
        return vue(*args, **kwargs)
    return wrapper


def role_required(*roles):
    """Restreint une vue à certains rôles (admin passe toujours)."""
    def decorateur(vue):
        @functools.wraps(vue)
        @login_required
        def wrapper(*args, **kwargs):
            if g.user["role"] != "admin" and g.user["role"] not in roles:
                abort(403)
            return vue(*args, **kwargs)
        return wrapper
    return decorateur


def peut_saisir():
    return g.user is not None and g.user["role"] in ("admin", "saisie")


def champ(nom, defaut=""):
    """Valeur d'un champ de formulaire, nettoyée."""
    return (request.form.get(nom) or defaut).strip()


def champ_int(nom, defaut=0):
    v = request.form.get(nom, "")
    try:
        return int(v)
    except (TypeError, ValueError):
        return defaut


def champ_bool(nom):
    return 1 if request.form.get(nom) else 0


def champ_id(nom):
    """Clé étrangère optionnelle : None si vide."""
    v = request.form.get(nom, "")
    try:
        return int(v) if v else None
    except ValueError:
        return None


def champ_date(nom, obligatoire=False):
    """Date au format ISO (YYYY-MM-DD) ou '' ; ajoute une erreur si invalide."""
    v = champ(nom)
    if not v:
        if obligatoire:
            g.erreurs.append(f"Le champ « {nom} » est obligatoire.")
        return ""
    try:
        datetime.strptime(v, "%Y-%m-%d")
    except ValueError:
        g.erreurs.append(f"La date « {v} » n'est pas valide.")
        return ""
    return v


def valider_choix(valeur, choix, libelle):
    if valeur not in choix:
        g.erreurs.append(f"Valeur inattendue pour « {libelle} ».")
    return valeur


def debut_validation():
    g.erreurs = []


def erreurs_flash():
    for e in g.erreurs:
        flash(e, "erreur")
    return bool(g.erreurs)


def get_or_404(table, ident):
    ligne = get_db().execute(f"SELECT * FROM {table} WHERE id = ?", (ident,)).fetchone()
    if ligne is None:
        abort(404)
    return ligne


def liste_ecoles():
    return get_db().execute("SELECT id, nom, commune, type FROM ecoles ORDER BY nom").fetchall()


def pagination(page, total, par_page):
    nb_pages = max(1, (total + par_page - 1) // par_page)
    page = min(max(1, page), nb_pages)
    return {"page": page, "nb_pages": nb_pages, "total": total, "offset": (page - 1) * par_page}
