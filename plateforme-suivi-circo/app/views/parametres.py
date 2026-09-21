"""Paramètres de la circonscription (nom, académie, année scolaire) — administrateur."""
from flask import Blueprint, flash, redirect, render_template, request, url_for

from ..db import get_db, lire_parametres
from .helpers import champ, role_required

bp = Blueprint("parametres", __name__, url_prefix="/parametres")

CLES = [
    ("academie", "Académie", "Académie de …"),
    ("circonscription", "Circonscription", "Circonscription de …"),
    ("annee_scolaire", "Année scolaire", "2026/2027"),
    ("ien", "IEN", "Nom de l'inspecteur·rice"),
]


@bp.route("/", methods=("GET", "POST"))
@role_required()
def editer():
    db = get_db()
    if request.method == "POST":
        for cle, _, _ in CLES:
            db.execute("INSERT INTO parametres (cle, valeur) VALUES (?, ?) "
                       "ON CONFLICT(cle) DO UPDATE SET valeur = excluded.valeur", (cle, champ(cle)))
        db.commit()
        flash("Paramètres enregistrés.", "succes")
        return redirect(url_for("parametres.editer"))
    return render_template("parametres.html", cles=CLES, valeurs=lire_parametres())
