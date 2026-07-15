# Database Design

How a 255-page PhD thesis becomes a queryable relational database.

**Source:** A. Thakur, *Potential of South African medicinal plants as treatments for
Alzheimer's disease through Aβ42 protein reduction* (University of Pretoria).

---

## 1. Entities

An **entity** is a real-world thing we want to store data about. Each entity becomes
a table. The entities here come directly from the experimental workflow of the thesis:

> plant → plant part → extract → fraction → compound → assay result

| Entity | One row represents | Why it's separate |
|---|---|---|
| `plants` | one medicinal plant species | 21 species; one plant yields many extracts |
| `plant_parts` | one type of plant material (leaf, stem…) | controlled vocabulary — prevents "leaf"/"Leaves"/"leaf material" |
| `extracts` | one prep from one plant part + solvent | 34 extracts; one plant → many extracts |
| `fractions` | one chromatographic fraction of an extract | *X. undulatum* extract → 15 fractions, 2 active |
| `compounds` | one unique chemical compound | a compound can appear in several plants |
| `sample_compounds` | one detection of a compound in a sample | junction table (see §3) |
| `bioassays` | one assay *protocol* | the definition, stored once |
| `assay_results` | one *measurement* | the numbers; powers all downstream analysis |
| `references` | one literature citation | supports compound identifications |

**Design note — why not one big table?** Storing everything flat would repeat
"*Xysmalobium undulatum*, Apocynaceae" on every row mentioning one of its compounds.
Fixing a typo would mean fixing it in fifty places. Each fact should live in exactly
one place; that's normalization (§4).

---

## 2. Attributes

Columns per entity, with types and constraints.

**`plants`** — `plant_id` (PK), `species_name` (TEXT NOT NULL UNIQUE), `genus`,
`family`, `traditional_use`, `selection_score` (INTEGER, from thesis Table 2.1),
`voucher_number`

**`plant_parts`** — `part_id` (PK), `part_name` (TEXT NOT NULL UNIQUE)

**`extracts`** — `extract_id` (PK), `plant_id` (FK), `part_id` (FK),
`solvent_system`, `extract_code`, `yield_pct` (REAL)

**`fractions`** — `fraction_id` (PK), `extract_id` (FK), `fraction_code`,
`is_active` (INTEGER, 1 = reduced Aβ42)

**`compounds`** — `compound_id` (PK), `compound_name` (TEXT NOT NULL),
`molecular_formula`, `molecular_class`, `smiles`, `id_status`, `id_method`

**`sample_compounds`** — `id` (PK), `compound_id` (FK), `extract_id` (FK, nullable),
`fraction_id` (FK, nullable), `reference_id` (FK), `retention_time_min`,
`acquired_mz`, `mass_error_ppm` (all REAL)

**`bioassays`** — `bioassay_id` (PK), `assay_name` (TEXT NOT NULL), `target`,
`cell_line`, `incubation_hours` (REAL), `method`, `result_unit`

**`assay_results`** — `result_id` (PK), `bioassay_id` (FK), `extract_id` /
`fraction_id` / `compound_id` (FK, nullable — see §3), `concentration` (REAL),
`concentration_unit`, `result_pct` (REAL), `std_dev`, `n_replicates`, `p_value`

**`references`** — `reference_id` (PK), `citation` (TEXT NOT NULL), `doi`

**Types:** `INTEGER` (whole numbers) · `TEXT` (words) · `REAL` (decimals)
**Constraints:** `PRIMARY KEY` · `FOREIGN KEY` · `NOT NULL` · `UNIQUE` · `CHECK`

**Note on units:** extracts are dosed in µg/mL, pure compounds in µM — hence
`concentration_unit` rather than assuming one scale.

**Note on `smiles`:** carried now (even though unpopulated) because it's the hook for
a future QSAR / RDKit project on the same data.

---

## 3. Relationships and the ER diagram

```
plant_parts ─┐
             ├──< extracts ──< fractions
plants ──────┘        │            │
                      └──────┬─────┘
                             │
                    sample_compounds >── compounds
                             
bioassays ──< assay_results >── (extract | fraction | compound)
```

**Primary key vs foreign key.** A primary key is a row's own identity ("who I am").
A foreign key is that identity copied into another table to point back ("who I'm
connected to").

> *Analogy:* a person is page 2 in the People notebook (primary key). An enrolment
> record writes "child on page 2" to refer to them (foreign key). Same number, two
> roles depending on which notebook it sits in.

**One-to-many:** one plant → many extracts; one extract → many fractions; one
bioassay → many results.

**Many-to-many:** one extract contains many compounds, *and* one compound (rutin,
quercetin) appears in many extracts. Two tables can't express this directly, so
`sample_compounds` sits between them — one row per "compound X detected in sample Y",
carrying the UPLC-QTOF-MS evidence for that specific detection (RT, m/z, mass error).

**The exclusive arc.** An `assay_result` measures exactly one thing — an extract, *or*
a fraction, *or* a compound. Never two. Two ways to model this:

| Approach | How | Trade-off |
|---|---|---|
| Polymorphic | `sample_type` + generic `sample_id` | flexible, but `sample_id` **can't be a real FK** — no integrity |
| **Exclusive arc** ✅ | three nullable FKs + `CHECK` | one results table *and* every row verifiably points at a real sample |

```sql
CHECK ((extract_id IS NOT NULL) + (fraction_id IS NOT NULL) + (compound_id IS NOT NULL) = 1)
```

Counts how many sample columns are filled; demands exactly one. Chosen because
referential integrity is the main reason to use a relational database at all.

---

## 4. Normalization

Each fact stored once, in the table it belongs to.

**1NF** — atomic values, no repeating groups. Not `compound_1`, `compound_2`,
`compound_3` columns; instead one row per compound in `sample_compounds`.

**2NF** — non-key columns depend on the *whole* key. `yield_pct` belongs to the
extract, not to the plant.

**3NF** — no transitive dependencies. `family` lives on `plants`, not repeated on
every extract or assay result that happens to involve that plant.

**Deliberate denormalization:** none currently. If dashboard queries get slow, a
materialized summary view is the first thing to reach for — but not before measuring.

**Lookup tables** (`plant_parts`) enforce controlled vocabulary at the database level:
you physically cannot enter a part that isn't in the list.

---

## 5. Open questions

- `traditional_use` is free text — may want its own lookup/tag table if it becomes
  something to filter on.
- `molecular_class` likewise (flavonoid / cardenolide glycoside / saponin) — a
  candidate lookup table once the real value list is known.
- No `collection_date` / `collection_location` on `plants` yet — add if the thesis
  records them and they matter for analysis.

---

## Implementation

Schema: [`database/schema.sql`](../database/schema.sql) · SQLite 3
Build: `sqlite3 drug_discovery.db < database/schema.sql`
