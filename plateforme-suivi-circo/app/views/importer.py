"""Import du classeur Excel : page web (administrateur) et commande en ligne."""
import click
from flask import Blueprint, flash, render_template, request

from ..importer import importer_classeur
from .helpers import role_required

bp = Blueprint("importer", __name__, url_prefix="/import")


@bp.route("/", methods=("GET", "POST"))
@role_required()
def page():
    rapport = None
    if request.method == "POST":
        fichier = request.files.get("classeur")
        if not fichier or not fichier.filename.lower().endswith((".xlsx", ".xlsm")):
            flash("Choisissez un classeur Excel (.xlsx).", "erreur")
        else:
            try:
                rapport = importer_classeur(fichier.stream)
            except Exception as exc:  # noqa: BLE001 - on affiche l'erreur à l'utilisateur
                flash(f"Import impossible : {exc}", "erreur")
            else:
                flash("Import terminé.", "succes")
    return render_template("import.html", rapport=rapport)


@click.command("import-excel")
@click.argument("chemin", type=click.Path(exists=True, dir_okay=False))
def import_excel_command(chemin):
    """Importe un classeur « fiches école » (xlsx) dans la base."""
    rapport = importer_classeur(chemin)
    click.echo(f"Écoles créées : {rapport['ecoles_creees']}, mises à jour : {rapport['ecoles_maj']}")
    click.echo(f"Personnels créés : {rapport['personnels_crees']}, mis à jour : {rapport['personnels_maj']}")
    for d in rapport["details"]:
        click.echo(f"  - {d['feuille']:<22} {d['ecole']:<32} {d['type']:<12} {d['personnels']} personnels")
    if rapport["feuilles_ignorees"]:
        click.echo("Feuilles ignorées : " + ", ".join(rapport["feuilles_ignorees"]))
