"""Exports : CSV (Excel/LibreOffice en français) et classeur Excel complet au format de la circonscription."""
import csv
import io
from datetime import date

from flask import Blueprint, Response, request, send_file

from ..db import get_db, lire_parametres
from ..excel import construire_classeur, construire_carte_scolaire
from ..stats import COLS_EFF
from .helpers import login_required

bp = Blueprint("exports", __name__, url_prefix="/exports")


def _csv(nom, entetes, lignes):
    tampon = io.StringIO()
    w = csv.writer(tampon, delimiter=";", quoting=csv.QUOTE_MINIMAL, lineterminator="\r\n")
    w.writerow(entetes)
    for l in lignes:
        w.writerow(["Oui" if v is True else "Non" if v is False else ("" if v is None else v) for v in l])
    contenu = "﻿" + tampon.getvalue()
    return Response(
        contenu, mimetype="text/csv; charset=utf-8",
        headers={"Content-Disposition": f'attachment; filename="{nom}_{date.today().isoformat()}.csv"'},
    )


@bp.route("/classeur.xlsx")
@login_required
def classeur():
    """Classeur complet : tableau de bord, effectifs par niveaux, une feuille par école."""
    tampon = construire_classeur(lire_parametres())
    nom = f"tableau_de_bord_circonscription_{date.today().isoformat()}.xlsx"
    return send_file(tampon, as_attachment=True, download_name=nom,
                     mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")


@bp.route("/carte-scolaire.xlsx")
@login_required
def carte_scolaire():
    """Classeur de carte scolaire au format du dialogue de gestion."""
    from .carte import campagne_courante
    campagne = request.args.get("campagne") or campagne_courante()
    tampon = construire_carte_scolaire(lire_parametres(), campagne)
    nom = f"carte_scolaire_{campagne}_{date.today().isoformat()}.xlsx"
    return send_file(tampon, as_attachment=True, download_name=nom,
                     mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")


@bp.route("/ecoles.csv")
@login_required
def ecoles():
    lignes = get_db().execute(
        """SELECT ec.nom, ec.type, ec.rne, ec.commune, ec.adresse, ec.telephone, ec.email, ec.directeur, ec.secretaire,
             ec.education_prioritaire, ec.nb_salles, ec.nb_classes, ec.decharge_direction, ec.date_maj,
             (SELECT COUNT(*) FROM enseignants e WHERE e.ecole_id = ec.id AND e.actif = 1 AND e.dans_organisation = 1),
             (SELECT COALESCE(SUM(eff_ps+eff_ms+eff_gs+eff_cp+eff_ce1+eff_ce2+eff_cm1+eff_cm2), 0)
                FROM enseignants e WHERE e.ecole_id = ec.id AND e.actif = 1 AND e.dans_organisation = 1)
           FROM ecoles ec ORDER BY ec.commune, ec.nom""").fetchall()
    return _csv("ecoles", ["École", "Type", "RNE", "Commune", "Adresse", "Téléphone", "Courriel", "Direction",
                           "Secrétariat", "Éducation prioritaire", "Nb salles", "Nb classes", "Décharge direction (%)",
                           "Mise à jour", "Nb enseignants", "Nb élèves (hors ULIS)"], lignes)


@bp.route("/enseignants.csv")
@login_required
def enseignants():
    cols = ", ".join(f"e.{c}" for c in COLS_EFF)
    lignes = get_db().execute(
        f"""SELECT e.nom, e.prenom, e.sexe, ec.nom, e.statut, e.fonction, e.anciennete, e.dans_organisation = 1,
             e.dispositif, e.salle, {cols},
             e.eff_ps+e.eff_ms+e.eff_gs+e.eff_cp+e.eff_ce1+e.eff_ce2+e.eff_cm1+e.eff_cm2,
             e.email, e.telephone, e.accompagnement = 1, e.actif = 1,
             (SELECT MAX(date) FROM suivis_enseignants s WHERE s.enseignant_id = e.id AND s.statut = 'Réalisé'),
             (SELECT COUNT(*) FROM suivis_enseignants s WHERE s.enseignant_id = e.id), e.observations
           FROM enseignants e LEFT JOIN ecoles ec ON ec.id = e.ecole_id ORDER BY ec.nom, e.nom, e.prenom""").fetchall()
    return _csv("personnels", ["Nom", "Prénom", "Sexe", "École", "Statut", "Fonction", "Ancienneté (ans)",
                               "Dans l'organisation pédagogique", "Dispositif", "Salle",
                               "PS", "MS", "GS", "CP", "CE1", "CE2", "CM1", "CM2", "ULIS", "Total (hors ULIS)",
                               "Courriel", "Téléphone", "Accompagnement renforcé", "Actif",
                               "Dernière visite", "Nb suivis", "Observations"], lignes)


@bp.route("/eleves.csv")
@login_required
def eleves():
    lignes = get_db().execute(
        """SELECT el.nom, el.prenom, el.date_naissance, el.sexe, ec.nom, el.niveau,
             en.nom || ' ' || en.prenom, el.ppre = 1, el.pap = 1, el.pai = 1, el.pps = 1, el.rased = 1,
             el.aesh, el.mdph, el.situation, el.actif = 1,
             (SELECT MAX(date) FROM suivis_eleves s WHERE s.eleve_id = el.id),
             (SELECT COUNT(*) FROM suivis_eleves s WHERE s.eleve_id = el.id), el.notes
           FROM eleves el LEFT JOIN ecoles ec ON ec.id = el.ecole_id
           LEFT JOIN enseignants en ON en.id = el.enseignant_id ORDER BY el.nom, el.prenom""").fetchall()
    return _csv("eleves", ["Nom", "Prénom", "Date de naissance", "Sexe", "École", "Niveau", "Enseignant·e",
                           "PPRE", "PAP", "PAI", "PPS", "RASED", "AESH", "MDPH", "Situation", "Actif",
                           "Dernier suivi", "Nb suivis", "Notes"], lignes)


@bp.route("/suivis.csv")
@login_required
def suivis():
    lignes = get_db().execute(
        """SELECT * FROM (
             SELECT 'Enseignant' AS cible, p.nom || ' ' || p.prenom, ec.nom, s.date, s.type, s.objet,
                    s.compte_rendu, s.points_forts, s.axes_progres, s.actions_prevues, s.echeance, s.statut, u.nom
             FROM suivis_enseignants s JOIN enseignants p ON p.id = s.enseignant_id
             LEFT JOIN ecoles ec ON ec.id = p.ecole_id LEFT JOIN utilisateurs u ON u.id = s.auteur_id
             UNION ALL
             SELECT 'Élève', p.nom || ' ' || p.prenom, ec.nom, s.date, s.type, s.objet,
                    s.compte_rendu, s.participants, '', s.decisions, s.echeance, s.statut, u.nom
             FROM suivis_eleves s JOIN eleves p ON p.id = s.eleve_id
             LEFT JOIN ecoles ec ON ec.id = p.ecole_id LEFT JOIN utilisateurs u ON u.id = s.auteur_id
           ) ORDER BY date DESC""").fetchall()
    return _csv("suivis", ["Cible", "Personne", "École", "Date", "Type", "Objet", "Compte rendu",
                           "Points forts / participants", "Axes de progrès", "Actions prévues / décisions",
                           "Échéance", "Statut", "Saisi par"], lignes)
