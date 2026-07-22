# Project Overview

**AI-Powered Alzheimer's Drug Discovery Dashboard**

An end-to-end data project that turns a PhD thesis on South African medicinal plants
into a queryable database, an exploratory analysis, a dashboard, and a machine
learning model.

---

## The problem

Drug discovery is slow and expensive — up to 15 years and $1–2 billion per approved
drug, with ~90% of candidates failing even after reaching phase-I trials. Alzheimer's
disease is a particularly hard target, and Aβ42 (amyloid-beta 42) accumulation is one
of its central pathological features.

Traditional ethnopharmacology screens plants for activity in the lab — slow, manual,
and the resulting data usually ends up locked inside a thesis PDF where nobody can
query it.

## What this project does

Takes the experimental results of a real PhD thesis — 21 medicinal plant species,
34 extracts, bioassay screening, compound identification by UPLC-QTOF-MS, and
dose-response data — and rebuilds them as a structured, queryable system that can
answer questions the original PDF cannot:

- Which plant families are most enriched for Aβ42-reducing activity?
- Which compounds appear in more than one active extract?
- Where does activity trade off against cytotoxicity?
- Can compound structure predict Aβ42 reduction?

## Source data

A. Thakur, *Potential of South African medicinal plants as treatments for
Alzheimer's disease through Aβ42 protein reduction*, PhD thesis, University of
Pretoria.

| | |
|---|---|
| Plant species screened | 21 |
| Extracts prepared | 34 |
| Assay | Aβ42 production, APPsw-HeLa cells |
| Key finding | cardenolide lactone ring drives **both** Aβ42 reduction and cardiotoxicity |

---

## Roadmap

| Phase | Deliverable | Status |
|---|---|---|
| 1 · Data engineering | 9-table SQLite schema | ✅ done |
| | Thesis data → CSV → loaded via ETL | ✅ done|
| 2 · Analysis | EDA + visualisations | ✅ done |
| 3 · Product | Streamlit dashboard | ✅ done (It wasn’t very informative, so I didn’t add much information about this.) |
| 4 · ML | compound activity prediction (RDKit descriptors + SHAP) | ⬜ |
| 5 · LLM | RAG assistant over thesis + literature | ⬜ |
| 6 · Deploy | hosted app + documentation | ⬜ |

## Stack

SQLite · Python (pandas, RDKit) · Streamlit · scikit-learn · git

## Repository

```
├── database/     schema.sql, load scripts
├── data/         CSVs extracted from the thesis
├── etl/          Python loaders (extract → transform → load)
├── notebooks/    exploratory analysis
├── dashboard/    Streamlit app
├── models/       machine learning
└── docs/         this documentation
```

## Documentation

1. **Project Overview** — this file
2. [Database Design](02_database_design.md) — entities, attributes, ERD, normalization
3. [Setup Notes](03_setup_notes.md) — build workflow, SQL/git command reference

---

## Why this project

It sits at the intersection of a chemistry PhD and data science: the underlying
biology was generated first-hand, and the computational layer is built on top of it.
The methods mirror those reviewed in the AI-for-drug-discovery literature (QSAR,
activity prediction, toxicity modelling) — applied here to original experimental data
rather than a public benchmark dataset.
