PRAGMA foreign_keys = ON;

CREATE TABLE plant_parts (
    part_id    INTEGER PRIMARY KEY,
    part_name  TEXT NOT NULL UNIQUE
);

CREATE TABLE "references" (
    reference_id  INTEGER PRIMARY KEY,
    citation      TEXT NOT NULL,
    doi           TEXT
);

CREATE TABLE plants (
    plant_id         INTEGER PRIMARY KEY,
    species_name     TEXT NOT NULL UNIQUE,
    genus            TEXT,
    family           TEXT,
    traditional_use  TEXT,
    selection_score  INTEGER,
    voucher_number   TEXT
);

CREATE TABLE extracts (
    extract_id      INTEGER PRIMARY KEY,
    plant_id        INTEGER,
    part_id         INTEGER,
    solvent_system  TEXT DEFAULT 'DCM:MeOH (1:1)',
    extract_code    TEXT,
    yield_pct       REAL,
    FOREIGN KEY (plant_id) REFERENCES plants(plant_id),
    FOREIGN KEY (part_id)  REFERENCES plant_parts(part_id)
);

CREATE TABLE fractions (
    fraction_id    INTEGER PRIMARY KEY,
    extract_id     INTEGER,
    fraction_code  TEXT,
    is_active      INTEGER,
    FOREIGN KEY (extract_id) REFERENCES extracts(extract_id)
);

CREATE TABLE compounds (
    compound_id        INTEGER PRIMARY KEY,
    compound_name      TEXT NOT NULL,
    molecular_formula  TEXT,
    molecular_class    TEXT,
    smiles             TEXT,
    id_status          TEXT,
    id_method          TEXT
);

CREATE TABLE sample_compounds (
    id                  INTEGER PRIMARY KEY,
    compound_id         INTEGER NOT NULL,
    extract_id          INTEGER,
    fraction_id         INTEGER,
    reference_id        INTEGER,
    retention_time_min  REAL,
    acquired_mz         REAL,
    mass_error_ppm      REAL,
    FOREIGN KEY (compound_id) REFERENCES compounds(compound_id),
    FOREIGN KEY (extract_id)  REFERENCES extracts(extract_id),
    FOREIGN KEY (fraction_id) REFERENCES fractions(fraction_id),
    CHECK ((extract_id IS NOT NULL) + (fraction_id IS NOT NULL) = 1)
);

CREATE TABLE bioassays (
    bioassay_id       INTEGER PRIMARY KEY,
    assay_name        TEXT NOT NULL,
    target            TEXT,
    cell_line         TEXT,
    incubation_hours  REAL,
    method            TEXT,
    result_unit       TEXT
);

CREATE TABLE assay_results (
    result_id           INTEGER PRIMARY KEY,
    bioassay_id         INTEGER NOT NULL,
    extract_id          INTEGER,
    fraction_id         INTEGER,
    compound_id         INTEGER,
    concentration       REAL,
    concentration_unit  TEXT,
    result_pct          REAL,
    std_dev             REAL,
    n_replicates        INTEGER,
    p_value             REAL,
    notes               TEXT,
    FOREIGN KEY (bioassay_id) REFERENCES bioassays(bioassay_id),
    FOREIGN KEY (extract_id)  REFERENCES extracts(extract_id),
    FOREIGN KEY (fraction_id) REFERENCES fractions(fraction_id),
    FOREIGN KEY (compound_id) REFERENCES compounds(compound_id),
    CHECK ((extract_id IS NOT NULL) + (fraction_id IS NOT NULL) + (compound_id IS NOT NULL) = 1)
);
