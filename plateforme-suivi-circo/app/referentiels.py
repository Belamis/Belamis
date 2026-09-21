"""Listes de valeurs utilisées dans les formulaires (référentiels métier)."""

TYPES_ECOLE = ["Maternelle", "Élémentaire", "Primaire"]

EDUCATION_PRIORITAIRE = ["Hors EP", "REP", "REP+"]

# Niveaux portés par une classe (colonnes d'effectifs). (clé colonne, libellé, cycle)
NIVEAUX_EFFECTIFS = [
    ("eff_ps", "PS", 1), ("eff_ms", "MS", 1), ("eff_gs", "GS", 1),
    ("eff_cp", "CP", 2), ("eff_ce1", "CE1", 2), ("eff_ce2", "CE2", 2),
    ("eff_cm1", "CM1", 3), ("eff_cm2", "CM2", 3),
    ("eff_ulis", "ULIS", 0),
]
NIVEAUX = [lib for _, lib, _ in NIVEAUX_EFFECTIFS] + ["TPS", "UPE2A"]

CYCLES = {
    1: "Cycle 1 (PS-MS-GS)",
    2: "Cycle 2 (CP-CE1-CE2)",
    3: "Cycle 3 (CM1-CM2)",
}

# Statuts tels qu'utilisés dans les fiches école de la circonscription.
STATUTS_ENSEIGNANT = [
    ("PE", "PE — Professeur des écoles titulaire"),
    ("DIR", "DIR — Directeur / Directrice"),
    ("C", "C — Contractuel·le"),
    ("C/CDI", "C/CDI — Contractuel·le en CDI"),
    ("PES1", "PES1 — Stagiaire 1re année"),
    ("PES2", "PES2 — Stagiaire 2e année"),
    ("STGF", "STGF — Stagiaire en formation"),
    ("TR-ZIL", "TR-ZIL — Titulaire remplaçant·e"),
    ("BGS", "BGS — Brigade GS"),
    ("AESH", "AESH — Accompagnant·e d'élèves en situation de handicap"),
    ("AUTRE", "Autre"),
]
STATUTS_CODES = [c for c, _ in STATUTS_ENSEIGNANT]
STATUTS_LIBELLES = dict(STATUTS_ENSEIGNANT)

# Statuts qui portent normalement une classe (ligne de l'organisation pédagogique).
STATUTS_AVEC_CLASSE = ["PE", "DIR", "C", "C/CDI", "PES1", "PES2", "STGF"]

# Statuts pour lesquels un accompagnement renforcé (visites) est attendu dans l'année.
STATUTS_A_VISITER = ["C", "C/CDI", "PES1", "PES2", "STGF"]

DISPOSITIFS_CLASSE = ["", "Solo", "Duo"]

SEXES = ["", "F", "H"]

TRANCHES_ANCIENNETE = [
    ("1 an", 1, 1), ("2 ans", 2, 2), ("3 ans", 3, 3), ("4 ans", 4, 4),
    ("5 à 10 ans", 5, 10), ("10 à 15 ans", 11, 15), ("15 à 20 ans", 16, 20), ("> 20 ans", 21, 99),
]

TYPES_SUIVI_ENSEIGNANT = [
    "Visite conseil",
    "Visite d'accompagnement",
    "Rendez-vous de carrière",
    "Inspection",
    "Entretien",
    "Observation de classe",
    "Formation / animation pédagogique",
    "Autre",
]

TYPES_SUIVI_ELEVE = [
    "Équipe éducative",
    "ESS (équipe de suivi de scolarisation)",
    "Mise en place / bilan PPRE",
    "Point RASED",
    "Rencontre famille",
    "Absentéisme",
    "Information préoccupante / signalement",
    "Aménagement pédagogique",
    "Orientation / affectation",
    "Autre",
]

STATUTS_SUIVI = ["À planifier", "Réalisé", "À suivre", "Clos"]

AESH = ["Non", "Individuelle (AESH-i)", "Mutualisée (AESH-m)", "Demande en cours"]

MDPH = ["Aucun dossier", "Dossier en cours", "Notification obtenue", "Refus"]

SEXES_ELEVE = ["", "F", "M"]

ROLES = {
    "admin": "Administrateur (IEN)",
    "saisie": "Saisie (CPC, secrétariat, ERUN)",
    "lecture": "Consultation seule",
}

DISPOSITIFS_ELEVE = [
    ("ppre", "PPRE"), ("pap", "PAP"), ("pai", "PAI"), ("pps", "PPS"), ("rased", "RASED"),
]
