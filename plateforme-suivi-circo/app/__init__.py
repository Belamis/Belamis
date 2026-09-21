"""Plateforme de suivi des enseignants et des élèves d'une circonscription."""
import os
import secrets
from datetime import date, datetime

from flask import Flask, abort, request, session

from . import db as database
from . import referentiels
from .referentiels import STATUTS_LIBELLES


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    os.makedirs(app.instance_path, exist_ok=True)

    app.config.from_mapping(
        SECRET_KEY=os.environ.get("SECRET_KEY") or _load_or_create_secret(app.instance_path),
        DATABASE=os.environ.get("DATABASE") or os.path.join(app.instance_path, "circo.sqlite"),
        ADMIN_INITIAL_PASSWORD=os.environ.get("ADMIN_INITIAL_PASSWORD", "admin"),
        PAR_PAGE=50,
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SAMESITE="Lax",
        MAX_CONTENT_LENGTH=2 * 1024 * 1024,
    )
    if test_config:
        app.config.update(test_config)

    database.init_app(app)

    with app.app_context():
        database.init_db()

    # --- Protection CSRF sur toutes les requêtes modifiantes ---------------
    @app.before_request
    def csrf_protect():
        if request.method in ("POST", "PUT", "PATCH", "DELETE"):
            token = session.get("_csrf")
            envoye = request.form.get("_csrf") or request.headers.get("X-CSRF-Token")
            if not token or not envoye or not secrets.compare_digest(token, envoye):
                abort(400, "Jeton de sécurité invalide. Rechargez la page et réessayez.")

    def csrf_token():
        if "_csrf" not in session:
            session["_csrf"] = secrets.token_urlsafe(32)
        return session["_csrf"]

    # --- Filtres et variables disponibles dans les gabarits ------------------
    @app.template_filter("datefr")
    def datefr(valeur):
        """'2025-09-01' -> '01/09/2025' ; laisse vide si non renseigné."""
        if not valeur:
            return ""
        try:
            return datetime.strptime(str(valeur)[:10], "%Y-%m-%d").strftime("%d/%m/%Y")
        except ValueError:
            return valeur

    @app.template_filter("datetimefr")
    def datetimefr(valeur):
        if not valeur:
            return ""
        try:
            return datetime.strptime(str(valeur)[:19], "%Y-%m-%d %H:%M:%S").strftime("%d/%m/%Y %H:%M")
        except ValueError:
            return valeur

    @app.template_filter("statut")
    def statut_libelle(code):
        return STATUTS_LIBELLES.get(code, code)

    @app.template_filter("ouinon")
    def ouinon(valeur):
        return "Oui" if valeur else "Non"

    @app.context_processor
    def inject_globals():
        return {
            "csrf_token": csrf_token,
            "ref": referentiels,
            "aujourdhui": date.today().isoformat(),
            "annee_scolaire": annee_scolaire_courante(),
            "params": database.lire_parametres(),
        }

    # --- Vues ------------------------------------------------------------------
    from .views import (auth, dashboard, ecoles, effectifs, eleves, enseignants, exports, importer,
                        parametres, suivis, utilisateurs)

    app.register_blueprint(auth.bp)
    app.register_blueprint(dashboard.bp)
    app.register_blueprint(ecoles.bp)
    app.register_blueprint(enseignants.bp)
    app.register_blueprint(eleves.bp)
    app.register_blueprint(suivis.bp)
    app.register_blueprint(exports.bp)
    app.register_blueprint(utilisateurs.bp)
    app.register_blueprint(effectifs.bp)
    app.register_blueprint(parametres.bp)
    app.register_blueprint(importer.bp)
    app.cli.add_command(importer.import_excel_command)

    return app


def annee_scolaire_courante(jour=None):
    """Retourne (debut, fin, libellé) de l'année scolaire contenant `jour`."""
    jour = jour or date.today()
    an = jour.year if jour.month >= 9 else jour.year - 1
    return {
        "debut": f"{an}-09-01",
        "fin": f"{an + 1}-08-31",
        "libelle": f"{an}-{an + 1}",
    }


def _load_or_create_secret(instance_path):
    """Clé de session persistante générée au premier lancement."""
    chemin = os.path.join(instance_path, "secret_key")
    if os.path.exists(chemin):
        with open(chemin, encoding="utf-8") as f:
            return f.read().strip()
    cle = secrets.token_hex(32)
    with open(chemin, "w", encoding="utf-8") as f:
        f.write(cle)
    return cle
