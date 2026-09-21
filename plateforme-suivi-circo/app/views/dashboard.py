"""Tableau de bord de la circonscription (feuille « BORD ») + alertes de suivi."""
from datetime import date, timedelta

from flask import Blueprint, render_template

from .. import annee_scolaire_courante
from ..db import get_db
from ..referentiels import STATUTS_A_VISITER
from ..stats import synthese_circonscription
from .helpers import login_required

bp = Blueprint("dashboard", __name__)


@bp.route("/")
@login_required
def index():
    db = get_db()
    annee = annee_scolaire_courante()
    dans_30j = (date.today() + timedelta(days=30)).isoformat()
    synthese = synthese_circonscription()

    eleves_suivis = db.execute(
        "SELECT COUNT(*) FROM eleves WHERE actif = 1 AND "
        "(ppre OR pap OR pai OR pps OR rased OR aesh != 'Non' OR mdph != 'Aucun dossier')").fetchone()[0]
    suivis_annee = db.execute(
        "SELECT (SELECT COUNT(*) FROM suivis_enseignants WHERE date BETWEEN ? AND ?) + "
        "(SELECT COUNT(*) FROM suivis_eleves WHERE date BETWEEN ? AND ?)",
        (annee["debut"], annee["fin"], annee["debut"], annee["fin"])).fetchone()[0]

    statuts = db.execute(
        "SELECT statut, COUNT(*) AS nb, SUM(sexe = 'H') AS hommes, SUM(sexe = 'F') AS femmes "
        "FROM enseignants WHERE actif = 1 GROUP BY statut ORDER BY nb DESC").fetchall()

    marqueurs = ",".join("?" * len(STATUTS_A_VISITER))
    a_visiter = db.execute(
        f"""SELECT e.id, e.nom, e.prenom, e.statut, ec.nom AS ecole
            FROM enseignants e LEFT JOIN ecoles ec ON ec.id = e.ecole_id
            WHERE e.actif = 1 AND (e.statut IN ({marqueurs}) OR e.accompagnement = 1)
              AND NOT EXISTS (SELECT 1 FROM suivis_enseignants s
                              WHERE s.enseignant_id = e.id AND s.statut = 'Réalisé'
                                AND s.date BETWEEN ? AND ?)
            ORDER BY e.nom, e.prenom""",
        (*STATUTS_A_VISITER, annee["debut"], annee["fin"])).fetchall()

    echeances = db.execute(
        """SELECT * FROM (
             SELECT 'enseignant' AS cible, s.id, s.enseignant_id AS cible_id, s.date, s.type,
                    s.objet, s.echeance, s.statut, e.nom || ' ' || e.prenom AS personne
             FROM suivis_enseignants s JOIN enseignants e ON e.id = s.enseignant_id
             WHERE s.echeance != '' AND s.statut IN ('À planifier', 'À suivre')
             UNION ALL
             SELECT 'eleve', s.id, s.eleve_id, s.date, s.type, s.objet, s.echeance, s.statut,
                    e.nom || ' ' || e.prenom
             FROM suivis_eleves s JOIN eleves e ON e.id = s.eleve_id
             WHERE s.echeance != '' AND s.statut IN ('À planifier', 'À suivre')
           ) WHERE echeance <= ? ORDER BY echeance LIMIT 20""", (dans_30j,)).fetchall()

    recents = db.execute(
        """SELECT * FROM (
             SELECT 'enseignant' AS cible, s.id, s.enseignant_id AS cible_id, s.date, s.type,
                    s.objet, s.cree_le, e.nom || ' ' || e.prenom AS personne, u.nom AS auteur
             FROM suivis_enseignants s JOIN enseignants e ON e.id = s.enseignant_id
             LEFT JOIN utilisateurs u ON u.id = s.auteur_id
             UNION ALL
             SELECT 'eleve', s.id, s.eleve_id, s.date, s.type, s.objet, s.cree_le,
                    e.nom || ' ' || e.prenom, u.nom
             FROM suivis_eleves s JOIN eleves e ON e.id = s.eleve_id
             LEFT JOIN utilisateurs u ON u.id = s.auteur_id
           ) ORDER BY cree_le DESC LIMIT 8""").fetchall()

    ecoles_incoherentes = [e for e in synthese["ecoles"] if e["nb_classes"] != e["nb_classes_calc"] or e["total"] == 0]

    return render_template(
        "dashboard.html", s=synthese, eleves_suivis=eleves_suivis, suivis_annee=suivis_annee,
        statuts=statuts, a_visiter=a_visiter, echeances=echeances, recents=recents,
        ecoles_incoherentes=ecoles_incoherentes, aujourdhui=date.today().isoformat(),
    )
