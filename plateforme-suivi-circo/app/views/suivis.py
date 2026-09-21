"""Journal global des suivis (enseignants + élèves)."""
from flask import Blueprint, render_template, request

from ..db import get_db
from ..referentiels import STATUTS_SUIVI, TYPES_SUIVI_ELEVE, TYPES_SUIVI_ENSEIGNANT
from .helpers import liste_ecoles, login_required

bp = Blueprint("suivis", __name__, url_prefix="/suivis")


@bp.route("/")
@login_required
def journal():
    cible = request.args.get("cible") or ""
    statut = request.args.get("statut") or ""
    ecole_id = request.args.get("ecole") or ""
    du = request.args.get("du") or ""
    au = request.args.get("au") or ""
    q = (request.args.get("q") or "").strip()

    def bloc(table, cible_nom, fk):
        return f"""SELECT '{cible_nom}' AS cible, s.id, s.{fk} AS cible_id, s.date, s.type, s.objet,
                     s.echeance, s.statut, s.cree_le, p.nom || ' ' || p.prenom AS personne,
                     ec.nom AS ecole, ec.id AS ecole_id, u.nom AS auteur
                   FROM {table} s JOIN {cible_nom}s p ON p.id = s.{fk}
                   LEFT JOIN ecoles ec ON ec.id = p.ecole_id
                   LEFT JOIN utilisateurs u ON u.id = s.auteur_id"""

    parts = []
    if cible in ("", "enseignant"):
        parts.append(bloc("suivis_enseignants", "enseignant", "enseignant_id"))
    if cible in ("", "eleve"):
        parts.append(bloc("suivis_eleves", "eleve", "eleve_id"))
    sql = "SELECT * FROM (" + " UNION ALL ".join(parts) + ") WHERE 1 = 1"
    params = []
    if statut:
        sql += " AND statut = ?"
        params.append(statut)
    if ecole_id.isdigit():
        sql += " AND ecole_id = ?"
        params.append(int(ecole_id))
    if du:
        sql += " AND date >= ?"
        params.append(du)
    if au:
        sql += " AND date <= ?"
        params.append(au)
    if q:
        sql += " AND (personne LIKE ? OR objet LIKE ? OR type LIKE ?)"
        params += [f"%{q}%"] * 3
    sql += " ORDER BY date DESC, cree_le DESC LIMIT 500"
    suivis = get_db().execute(sql, params).fetchall()
    return render_template(
        "suivis/journal.html", suivis=suivis, ecoles=liste_ecoles(), cible=cible, statut=statut,
        ecole_id=ecole_id, du=du, au=au, q=q, statuts=STATUTS_SUIVI,
        types=TYPES_SUIVI_ENSEIGNANT + TYPES_SUIVI_ELEVE,
    )
