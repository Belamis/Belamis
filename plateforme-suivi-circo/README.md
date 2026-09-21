# Plateforme de suivi de circonscription

Application web de saisie et de suivi pour une circonscription du premier degré :
**écoles, personnels (enseignants, remplaçants, AESH), effectifs par niveau, élèves à
besoins particuliers et suivis** (visites conseil, rendez-vous de carrière, équipes
éducatives…).

Elle reprend la logique du classeur Excel « Tableau de bord / fiche école » de la
circonscription et l'améliore :

| Classeur Excel | Plateforme |
|---|---|
| Feuille **BORD** (écoles, élèves, classes, enseignants, par cycle, par niveau) | **Tableau de bord** recalculé en direct, avec alertes (enseignants à accompagner, échéances, écarts de cohérence) |
| Feuille **EFFECTIFS PAR NIVEAUX** | Page **Effectifs** (écoles × niveaux, cycles, classes, élèves/classe) |
| Une feuille **fiche école** par école | **Fiche école** : signalétique, informations générales, organisation pédagogique, personnels hors organisation, statistiques automatiques, contrôles de cohérence |
| Saisie cellule par cellule | **Grille de saisie des effectifs** par école (totaux en direct) et formulaires guidés |
| — | **Suivi des enseignants** : visites, entretiens, formations, points forts / axes de progrès, échéances |
| — | **Suivi nominatif des élèves** à besoins particuliers : PPRE, PAP, PAI, PPS, RASED, AESH, MDPH, équipes éducatives, signalements |
| — | **Journal** de tous les suivis, comptes utilisateurs à rôles, historique de saisie |
| Fichier partagé par mail | **Import** du classeur existant et **export** d'un classeur au même format, exports CSV |

## Installation

Prérequis : Python 3.10 ou plus.

```bash
cd plateforme-suivi-circo
python3 -m venv .venv
source .venv/bin/activate          # Windows : .venv\Scripts\activate
pip install -r requirements.txt
flask --app app run                # http://127.0.0.1:5000
```

Au premier lancement la base SQLite est créée dans `instance/circo.sqlite` avec un
compte **admin / admin**. Changez ce mot de passe dès la première connexion
(menu *Mon compte*), puis créez les comptes de l'équipe (*Administration*).

### Reprendre les données du classeur Excel

Deux possibilités :

- *Administration → Importer un classeur Excel* (connecté en administrateur) ;
- en ligne de commande : `flask --app app import-excel TABLEAU_DE_BORD_FICHE_ECOLE.xlsx`.

L'import lit chaque feuille « fiche école » (signalétique, organisation pédagogique,
personnels non comptabilisés). Les écoles sont reconnues par RNE puis par nom, les
personnels par nom + prénom dans l'école : on peut ré-importer sans créer de doublons.
Les feuilles de synthèse sont ignorées car recalculées.

Pensez ensuite à renseigner *Administration → Paramètres* (académie,
circonscription, année scolaire, IEN) : ces valeurs apparaissent dans les en-têtes et
dans le classeur exporté.

### Rôles

| Rôle | Droits |
|---|---|
| Administrateur (IEN) | tout, plus comptes, paramètres, import |
| Saisie (CPC, secrétariat, ERUN) | créer et modifier écoles, personnels, élèves, suivis |
| Consultation | lecture et exports |

## Mise en production

- Servez l'application derrière un serveur WSGI (`gunicorn "app:create_app()"`) et un
  reverse proxy HTTPS ; l'application ne doit jamais être exposée en HTTP clair.
- Variables d'environnement : `DATABASE` (chemin du fichier SQLite), `SECRET_KEY`
  (sinon générée dans `instance/secret_key`), `ADMIN_INITIAL_PASSWORD`.
- Sauvegardez régulièrement le fichier `instance/circo.sqlite` (une simple copie suffit).

## Protection des données

La plateforme traite des **données à caractère personnel** (personnels et élèves,
dont des informations de santé ou de handicap). Elle doit être hébergée sur une
infrastructure de l'académie ou approuvée par elle, inscrite au registre des
traitements, réservée aux personnels habilités, et les données doivent être purgées à
la fin de leur durée de conservation. Ne stockez que ce qui est nécessaire au suivi.

## Développement

```bash
pip install pytest
python3 -m pytest tests
```

Structure :

```
app/
├── __init__.py        Fabrique Flask, CSRF, filtres de gabarit
├── schema.sql         Tables SQLite
├── db.py              Connexion, initialisation, commande init-db
├── referentiels.py    Listes de valeurs (statuts, niveaux, types de suivi…)
├── stats.py           Calculs (effectifs, statistiques d'école, synthèse circo)
├── excel.py           Export du classeur Excel
├── importer.py        Import du classeur « fiches école »
├── views/             Pages (auth, tableau de bord, écoles, personnels, élèves, suivis…)
├── templates/         Gabarits Jinja
└── static/            Feuille de style et script
tests/                 Tests pytest
```
