-- ============================================================
-- AI-Powered Alzheimer's Drug Discovery Dashboard
-- Phase 1, Step 2: Load data
--
-- Source: A. Thakur, PhD thesis (University of Pretoria)
--   - Table 2.2  → plant species, families, vouchers
--   - Section 2.3 → selection scores
--
-- Run with:  sqlite3 drug_discovery.db < load_data.sql
-- Safe to re-run: clears these tables first.
-- ============================================================

PRAGMA foreign_keys = ON;

-- Make the script re-runnable (children first, then parents)
DELETE FROM extracts;
DELETE FROM plants;
DELETE FROM plant_parts;

-- ---------- plant_parts ----------
-- Part names from thesis Table 2.2, normalised to singular + lowercase
-- (thesis writes 'Leaves', 'Stems'; stored here as 'leaf', 'stem').
-- NOTE: compound parts ('leaf + stalk') are a known 1NF trade-off —
-- only 4 of 34 extracts use them. See docs/02_database_design.md.
INSERT INTO plant_parts (part_id, part_name) VALUES
    (1, 'leaf'),
    (2, 'stem'),
    (3, 'leaf + stalk'),
    (4, 'stalk + flower'),
    (5, 'stem + thorn'),
    (6, 'seed'),
    (7, 'seed pod');

-- ---------- plants ----------
-- 21 species across 15 families.
-- selection_score: LOWER = higher priority (thesis Table 2.1).
-- traditional_use left NULL for now — long prose, to be added later.
INSERT INTO plants (plant_id, species_name, genus, family, selection_score, voucher_number) VALUES
    (1,  'Centella asiatica',        'Centella',        'Apiaceae',         5, 'PRU 124298'),
    (2,  'Heteromorpha arborescens', 'Heteromorpha',    'Apiaceae',         7, 'PRU 124318'),
    (3,  'Mondia whitei',            'Mondia',          'Apocynaceae',      4, 'PRU 124299'),
    (4,  'Stapelia gigantea',        'Stapelia',        'Apocynaceae',      9, 'PRU 124308'),
    (5,  'Tabernaemontana elegans',  'Tabernaemontana', 'Apocynaceae',      8, 'PRU 124300'),
    (6,  'Xysmalobium undulatum',    'Xysmalobium',     'Apocynaceae',      7, 'PRU 124301'),
    (7,  'Cussonia spicata',         'Cussonia',        'Araliaceae',       6, 'PRU 124302'),
    (8,  'Cussonia paniculata',      'Cussonia',        'Araliaceae',       6, 'PRU 124309'),
    (9,  'Bulbine natalensis',       'Bulbine',         'Asphodelaceae',    7, 'PRU 124310'),
    (10, 'Catha edulis',             'Catha',           'Celastraceae',     7, 'PRU 124303'),
    (11, 'Commelina africana',       'Commelina',       'Commelinaceae',    6, 'PRU 124311'),
    (12, 'Cotyledon orbiculata',     'Cotyledon',       'Crassulaceae',     8, 'PRU 124312'),
    (13, 'Schotia brachypetala',     'Schotia',         'Fabaceae',         4, 'PRU 124313'),
    (14, 'Tetradenia riparia',       'Tetradenia',      'Lamiaceae',        6, 'PRU 124304'),
    (15, 'Trichilia dregeana',       'Trichilia',       'Meliaceae',        5, 'PRU 124305'),
    (16, 'Plumbago auriculata',      'Plumbago',        'Plumbaginaceae',   9, 'PRU 124306'),
    (17, 'Ziziphus mucronata',       'Ziziphus',        'Rhamnaceae',       7, 'PRU 124314'),
    (18, 'Ruta graveolens',          'Ruta',            'Rutaceae',         7, 'PRU 124315'),
    (19, 'Zanthoxylum capense',      'Zanthoxylum',     'Rutaceae',         6, 'PRU 124316'),
    (20, 'Buddleja salvifolia',      'Buddleja',        'Scrophulariaceae', 7, 'PRU 124307'),
    (21, 'Cissus quadrangularis',    'Cissus',          'Vitaceae',         8, 'PRU 124317');
