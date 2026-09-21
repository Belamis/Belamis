"""Récapitulatif écoles × niveaux (feuille « EFFECTIFS PAR NIVEAUX »)."""
from flask import Blueprint, render_template

from ..stats import effectifs_par_ecole
from .helpers import login_required

bp = Blueprint("effectifs", __name__, url_prefix="/effectifs")


@bp.route("/")
@login_required
def tableau():
    ecoles, totaux = effectifs_par_ecole()
    return render_template("effectifs.html", ecoles=ecoles, totaux=totaux)
