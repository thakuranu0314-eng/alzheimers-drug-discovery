# Setup Notes — Building the Database

Build log and command reference for Phase 1, Step 1: creating the schema.
For the *design reasoning* behind the tables, see [Database Design](02_database_design.md).

---

## What I built today

A 9-table SQLite database (`drug_discovery.db`) representing the thesis workflow:
plant → extract → fraction → compound → assay result.

Tables: `plant_parts`, `plants`, `extracts`, `fractions`, `compounds`,
`sample_compounds`, `bioassays`, `references`, `assay_results`.

Then saved the schema as a text file, committed it with git, and pushed to GitHub.

---

## The workflow (start to finish)

1. **Make a clean project folder** (separate from Le Wagon practice repo):
   ```
   cd ~
   mkdir alzheimers-drug-discovery
   cd alzheimers-drug-discovery
   mkdir database data docs notebooks dashboard models
   git init
   ```
2. **Create + open the database** (this makes the .db file AND opens the SQL prompt):
   ```
   cd database
   sqlite3 drug_discovery.db
   ```
3. **Write the 9 `CREATE TABLE` statements** at the `sqlite>` prompt (see below).
4. **Save the schema to a text file** (the shareable "recipe"):
   ```
   .quit
   sqlite3 drug_discovery.db .schema > schema.sql
   ```
5. **Commit + push to GitHub:**
   ```
   cd ..
   echo "*.db" > .gitignore          # never commit the generated .db file
   git add .
   git commit -m "Add 9-table SQLite schema for drug discovery database"
   git remote add origin https://github.com/thakuranu0314-eng/alzheimers-drug-discovery.git
   git branch -M main
   git push -u origin main
   ```

---

## Core concepts (interview-ready)

**Entity → table.** An entity is a real-world thing we store data about (plant,
extract, compound, assay). Each entity becomes one table.

**Structure vs data.** `CREATE TABLE` defines the empty container (columns + rules).
The actual rows (leaf, stem, the 21 species...) go in later with `INSERT`.

**Data types used:**
- `INTEGER` — whole numbers
- `TEXT` — words
- `REAL` — numbers with decimals (e.g. yield 7.6)

**Constraints (rules) used:**
- `PRIMARY KEY` — the column that uniquely identifies each row ("who I am")
- `FOREIGN KEY` — a pointer to a row in another table ("who I'm connected to")
- `NOT NULL` — column can never be empty
- `UNIQUE` — no duplicate values allowed
- `CHECK` — enforces a custom rule

**Primary key vs foreign key (the key idea):**
A primary key is a row's own identity. A foreign key is that same kind of number,
copied into another table to point back. *Analogy: a person is "page 2" in the
People notebook (primary key); an enrolment record writes "child on page 2" to
refer to them (foreign key).*

**Exclusive arc (the sophisticated bit):**
In `assay_results`, a measurement belongs to exactly ONE sample — an extract OR a
fraction OR a compound, never two. Enforced with:
```sql
CHECK ((extract_id IS NOT NULL) + (fraction_id IS NOT NULL) + (compound_id IS NOT NULL) = 1)
```
This keeps one results table while preserving referential integrity — chosen over a
"polymorphic" type-column approach, which can't use real foreign keys.

---

## The schema (all 9 tables)

```sql
CREATE TABLE plant_parts (
    part_id    INTEGER PRIMARY KEY,
    part_name  TEXT NOT NULL UNIQUE
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
    solvent_system  TEXT,
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

CREATE TABLE "references" (          -- quotes needed: reserved word
    reference_id  INTEGER PRIMARY KEY,
    citation      TEXT NOT NULL,
    doi           TEXT
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
    FOREIGN KEY (bioassay_id) REFERENCES bioassays(bioassay_id),
    FOREIGN KEY (extract_id)  REFERENCES extracts(extract_id),
    FOREIGN KEY (fraction_id) REFERENCES fractions(fraction_id),
    FOREIGN KEY (compound_id) REFERENCES compounds(compound_id),
    CHECK ((extract_id IS NOT NULL) + (fraction_id IS NOT NULL) + (compound_id IS NOT NULL) = 1)
);
```

---

## Command cheat-sheet

**SQLite dot-commands** (settings/inspection — start with `.`, no semicolon):
| Command | What it does |
|---|---|
| `sqlite3 file.db` | create/open a database and enter the SQL prompt |
| `.mode column` | display results in aligned columns |
| `.headers on` | show column names in results |
| `.tables` | list all tables |
| `.schema` | print every table's definition |
| `.schema tablename` | print one table's definition |
| `.quit` | exit SQLite, back to terminal |

**SQL statements** (end with `;`):
| Statement | What it does |
|---|---|
| `CREATE TABLE name (...);` | build a new table |
| `DROP TABLE name;` | delete a table entirely (used to fix a bad one) |

**Git flow:**
| Command | What it does |
|---|---|
| `git status` | show what's changed / staged / ignored |
| `git add .` | stage all changes for commit |
| `git commit -m "msg"` | save a snapshot locally |
| `git remote add origin <url>` | link local repo to GitHub |
| `git push -u origin main` | upload commits to GitHub |

---

## Next step

**Step 2 — Populate the tables:** extract the real thesis data (21 plant species,
plant parts, extracts, compounds, Aβ42 bioassay results) into CSV files under `data/`,
then load them via `etl/` scripts. This is where the empty structure becomes a
queryable database.

See also: [Project Overview](01_project_overview.md) · [Database Design](02_database_design.md)
