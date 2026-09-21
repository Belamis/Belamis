PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS parametres (
    cle    TEXT PRIMARY KEY,
    valeur TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS utilisateurs (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    login         TEXT NOT NULL UNIQUE,
    nom           TEXT NOT NULL,
    fonction      TEXT NOT NULL DEFAULT '',
    mot_de_passe  TEXT NOT NULL,
    role          TEXT NOT NULL DEFAULT 'saisie' CHECK (role IN ('admin', 'saisie', 'lecture')),
    actif         INTEGER NOT NULL DEFAULT 1,
    cree_le       TEXT NOT NULL DEFAULT (datetime('now'))
);

-- Fiche signalétique de l'école (reprend la feuille « fiche école » du classeur).
CREATE TABLE IF NOT EXISTS ecoles (
    id                    INTEGER PRIMARY KEY AUTOINCREMENT,
    nom                   TEXT NOT NULL,
    type                  TEXT NOT NULL DEFAULT 'Primaire',
    rne                   TEXT NOT NULL DEFAULT '',
    commune               TEXT NOT NULL DEFAULT '',
    adresse               TEXT NOT NULL DEFAULT '',
    telephone             TEXT NOT NULL DEFAULT '',
    email                 TEXT NOT NULL DEFAULT '',
    horaires              TEXT NOT NULL DEFAULT '',
    apc                   TEXT NOT NULL DEFAULT '',
    directeur             TEXT NOT NULL DEFAULT '',
    secretaire            TEXT NOT NULL DEFAULT '',
    ots                   TEXT NOT NULL DEFAULT '',
    faex_nom              TEXT NOT NULL DEFAULT '',
    faex_telephone        TEXT NOT NULL DEFAULT '',
    faex_email            TEXT NOT NULL DEFAULT '',
    faex_pct              TEXT NOT NULL DEFAULT '',
    education_prioritaire TEXT NOT NULL DEFAULT 'Hors EP',
    nb_salles             INTEGER NOT NULL DEFAULT 0,
    nb_classes            INTEGER NOT NULL DEFAULT 0,
    decharge_direction    INTEGER NOT NULL DEFAULT 0,
    date_maj              TEXT NOT NULL DEFAULT '',
    notes                 TEXT NOT NULL DEFAULT '',
    cree_le               TEXT NOT NULL DEFAULT (datetime('now')),
    modifie_le            TEXT NOT NULL DEFAULT (datetime('now'))
);

-- Personnels : chaque ligne « dans l'organisation pédagogique » porte une classe et ses effectifs.
CREATE TABLE IF NOT EXISTS enseignants (
    id                INTEGER PRIMARY KEY AUTOINCREMENT,
    nom               TEXT NOT NULL,
    prenom            TEXT NOT NULL DEFAULT '',
    sexe              TEXT NOT NULL DEFAULT '',
    email             TEXT NOT NULL DEFAULT '',
    telephone         TEXT NOT NULL DEFAULT '',
    ecole_id          INTEGER REFERENCES ecoles(id) ON DELETE SET NULL,
    statut            TEXT NOT NULL DEFAULT 'PE',
    fonction          TEXT NOT NULL DEFAULT '',
    anciennete        INTEGER,
    dans_organisation INTEGER NOT NULL DEFAULT 1,
    dispositif        TEXT NOT NULL DEFAULT '',
    salle             TEXT NOT NULL DEFAULT '',
    eff_ps            INTEGER NOT NULL DEFAULT 0,
    eff_ms            INTEGER NOT NULL DEFAULT 0,
    eff_gs            INTEGER NOT NULL DEFAULT 0,
    eff_cp            INTEGER NOT NULL DEFAULT 0,
    eff_ce1           INTEGER NOT NULL DEFAULT 0,
    eff_ce2           INTEGER NOT NULL DEFAULT 0,
    eff_cm1           INTEGER NOT NULL DEFAULT 0,
    eff_cm2           INTEGER NOT NULL DEFAULT 0,
    eff_ulis          INTEGER NOT NULL DEFAULT 0,
    accompagnement    INTEGER NOT NULL DEFAULT 0,
    observations      TEXT NOT NULL DEFAULT '',
    actif             INTEGER NOT NULL DEFAULT 1,
    cree_le           TEXT NOT NULL DEFAULT (datetime('now')),
    modifie_le        TEXT NOT NULL DEFAULT (datetime('now'))
);

-- Suivi nominatif des élèves à besoins particuliers (facultatif : les effectifs
-- viennent des lignes de classe ci-dessus, source ONDE).
CREATE TABLE IF NOT EXISTS eleves (
    id               INTEGER PRIMARY KEY AUTOINCREMENT,
    nom              TEXT NOT NULL,
    prenom           TEXT NOT NULL DEFAULT '',
    date_naissance   TEXT NOT NULL DEFAULT '',
    sexe             TEXT NOT NULL DEFAULT '',
    ecole_id         INTEGER REFERENCES ecoles(id) ON DELETE SET NULL,
    enseignant_id    INTEGER REFERENCES enseignants(id) ON DELETE SET NULL,
    niveau           TEXT NOT NULL DEFAULT '',
    ppre             INTEGER NOT NULL DEFAULT 0,
    pap              INTEGER NOT NULL DEFAULT 0,
    pai              INTEGER NOT NULL DEFAULT 0,
    pps              INTEGER NOT NULL DEFAULT 0,
    rased            INTEGER NOT NULL DEFAULT 0,
    aesh             TEXT NOT NULL DEFAULT 'Non',
    mdph             TEXT NOT NULL DEFAULT 'Aucun dossier',
    situation        TEXT NOT NULL DEFAULT '',
    notes            TEXT NOT NULL DEFAULT '',
    actif            INTEGER NOT NULL DEFAULT 1,
    cree_le          TEXT NOT NULL DEFAULT (datetime('now')),
    modifie_le       TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS suivis_enseignants (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    enseignant_id   INTEGER NOT NULL REFERENCES enseignants(id) ON DELETE CASCADE,
    date            TEXT NOT NULL,
    type            TEXT NOT NULL,
    objet           TEXT NOT NULL DEFAULT '',
    compte_rendu    TEXT NOT NULL DEFAULT '',
    points_forts    TEXT NOT NULL DEFAULT '',
    axes_progres    TEXT NOT NULL DEFAULT '',
    actions_prevues TEXT NOT NULL DEFAULT '',
    echeance        TEXT NOT NULL DEFAULT '',
    statut          TEXT NOT NULL DEFAULT 'Réalisé',
    auteur_id       INTEGER REFERENCES utilisateurs(id) ON DELETE SET NULL,
    cree_le         TEXT NOT NULL DEFAULT (datetime('now')),
    modifie_le      TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS suivis_eleves (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    eleve_id        INTEGER NOT NULL REFERENCES eleves(id) ON DELETE CASCADE,
    date            TEXT NOT NULL,
    type            TEXT NOT NULL,
    objet           TEXT NOT NULL DEFAULT '',
    compte_rendu    TEXT NOT NULL DEFAULT '',
    decisions       TEXT NOT NULL DEFAULT '',
    participants    TEXT NOT NULL DEFAULT '',
    echeance        TEXT NOT NULL DEFAULT '',
    statut          TEXT NOT NULL DEFAULT 'Réalisé',
    auteur_id       INTEGER REFERENCES utilisateurs(id) ON DELETE SET NULL,
    cree_le         TEXT NOT NULL DEFAULT (datetime('now')),
    modifie_le      TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_enseignants_ecole ON enseignants(ecole_id);
CREATE INDEX IF NOT EXISTS idx_eleves_ecole ON eleves(ecole_id);
CREATE INDEX IF NOT EXISTS idx_eleves_enseignant ON eleves(enseignant_id);
CREATE INDEX IF NOT EXISTS idx_suivis_ens ON suivis_enseignants(enseignant_id, date);
CREATE INDEX IF NOT EXISTS idx_suivis_elv ON suivis_eleves(eleve_id, date);
