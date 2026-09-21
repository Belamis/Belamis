"""Accès à la base SQLite : connexion par requête, initialisation du schéma."""
import os
import sqlite3

import click
from flask import current_app, g
from werkzeug.security import generate_password_hash


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE"], detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")
    return g.db


def close_db(_exc=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    """Crée les tables si besoin et le compte administrateur initial."""
    db = get_db()
    schema = os.path.join(os.path.dirname(__file__), "schema.sql")
    with open(schema, encoding="utf-8") as f:
        db.executescript(f.read())
    nb = db.execute("SELECT COUNT(*) FROM utilisateurs").fetchone()[0]
    if nb == 0:
        db.execute(
            "INSERT INTO utilisateurs (login, nom, fonction, mot_de_passe, role) "
            "VALUES (?, ?, ?, ?, 'admin')",
            (
                "admin",
                "Administrateur",
                "IEN",
                generate_password_hash(current_app.config["ADMIN_INITIAL_PASSWORD"]),
            ),
        )
        db.commit()
        return True
    db.commit()
    return False


@click.command("init-db")
def init_db_command():
    """Initialise la base de données (idempotent)."""
    created = init_db()
    if created:
        click.echo("Base initialisée. Compte créé : admin / "
                   + current_app.config["ADMIN_INITIAL_PASSWORD"]
                   + " (à changer dès la première connexion).")
    else:
        click.echo("Base déjà initialisée.")


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


def lire_parametres():
    """Paramètres de la circonscription sous forme de dictionnaire."""
    return {l["cle"]: l["valeur"] for l in get_db().execute("SELECT cle, valeur FROM parametres")}
