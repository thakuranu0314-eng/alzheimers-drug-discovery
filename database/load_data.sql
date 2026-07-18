PRAGMA foreign_keys = ON;

DELETE FROM extracts;
DELETE FROM plants;
DELETE FROM plant_parts;

INSERT INTO plant_parts (part_id, part_name) VALUES
    (1, 'leaf'),
    (2, 'stem'),
    (3, 'leaf + stalk'),
    (4, 'stalk + flower'),
    (5, 'stem + thorn'),
    (6, 'seed'),
    (7, 'seed pod');

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

INSERT INTO extracts (extract_id, plant_id, part_id, yield_pct) VALUES
    (1,  1,  3, 13.9),
    (2,  2,  1, 8.7),
    (3,  3,  1, 10.3),
    (4,  3,  2, 7.6),
    (5,  4,  2, 12.5),
    (6,  4,  6, 23.3),
    (7,  4,  7, 3.1),
    (8,  5,  1, 13.0),
    (9,  6,  4, 7.6),
    (10, 7,  1, 20.9),
    (11, 7,  2, 6.0),
    (12, 8,  1, 5.7),
    (13, 8,  2, 7.7),
    (14, 9,  1, 24.5),
    (15, 10, 1, 13.0),
    (16, 10, 2, 6.9),
    (17, 11, 1, 11.2),
    (18, 12, 1, 2.2),
    (19, 12, 2, 6.1),
    (20, 13, 1, 9.2),
    (21, 14, 1, 12.5),
    (22, 14, 2, 5.4),
    (23, 15, 1, 9.9),
    (24, 15, 2, 6.8),
    (25, 16, 1, 19.3),
    (26, 16, 2, 7.1),
    (27, 17, 3, 10.5),
    (28, 18, 1, 22.8),
    (29, 18, 2, 10.5),
    (30, 19, 1, 7.2),
    (31, 19, 5, 9.1),
    (32, 20, 1, 10.5),
    (33, 20, 2, 6.0),
    (34, 21, 2, 9.6);
