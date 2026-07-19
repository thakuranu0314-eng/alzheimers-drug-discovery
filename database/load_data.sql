PRAGMA foreign_keys = ON;
DELETE FROM assay_results;
DELETE FROM bioassays;
DELETE FROM extracts;
DELETE FROM plants;
DELETE FROM plant_parts;

INSERT INTO plant_parts (part_id, part_name) VALUES
    (1,'leaf'),(2,'stem'),(3,'leaf + stalk'),(4,'stalk + flower'),
    (5,'stem + thorn'),(6,'seed'),(7,'seed pod');

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
    (1,1,3,13.9),(2,2,1,8.7),(3,3,1,10.3),(4,3,2,7.6),(5,4,2,12.5),
    (6,4,6,23.3),(7,4,7,3.1),(8,5,1,13.0),(9,6,4,7.6),(10,7,1,20.9),
    (11,7,2,6.0),(12,8,1,5.7),(13,8,2,7.7),(14,9,1,24.5),(15,10,1,13.0),
    (16,10,2,6.9),(17,11,1,11.2),(18,12,1,2.2),(19,12,2,6.1),(20,13,1,9.2),
    (21,14,1,12.5),(22,14,2,5.4),(23,15,1,9.9),(24,15,2,6.8),(25,16,1,19.3),
    (26,16,2,7.1),(27,17,3,10.5),(28,18,1,22.8),(29,18,2,10.5),(30,19,1,7.2),
    (31,19,5,9.1),(32,20,1,10.5),(33,20,2,6.0),(34,21,2,9.6);

INSERT INTO bioassays (bioassay_id, assay_name, target, cell_line, incubation_hours, method, result_unit) VALUES
    (1, 'Ab42 production screen', 'Ab42', 'APPsw-HeLa', 8, 'ELISA', 'percent reduction');

INSERT INTO assay_results (result_id, bioassay_id, extract_id, concentration, concentration_unit, result_pct, std_dev, notes) VALUES
    (1,1,1,50,'ug/mL',NULL,NULL,'significant; exact % to confirm from Fig 2.5-2.8'),
    (2,1,2,50,'ug/mL',68.63,0.2,'significant; exact % from thesis prose'),
    (3,1,3,50,'ug/mL',11.1,0.1,'significant; exact % from thesis prose'),
    (4,1,4,50,'ug/mL',17.9,0.6,'significant; exact % from thesis prose'),
    (5,1,5,50,'ug/mL',NULL,NULL,'tested, not significant'),
    (6,1,6,50,'ug/mL',NULL,NULL,'tested, not significant'),
    (7,1,7,50,'ug/mL',NULL,NULL,'tested, not significant'),
    (8,1,8,50,'ug/mL',NULL,NULL,'tested, not significant'),
    (9,1,9,50,'ug/mL',76.9,1.0,'significant; exact % from thesis prose; most active'),
    (10,1,10,50,'ug/mL',NULL,NULL,'tested, not significant'),
    (11,1,11,50,'ug/mL',NULL,NULL,'tested, not significant'),
    (12,1,12,50,'ug/mL',57.5,1.3,'significant; exact % from thesis prose'),
    (13,1,13,50,'ug/mL',NULL,NULL,'tested, not significant'),
    (14,1,14,50,'ug/mL',NULL,NULL,'tested, not significant'),
    (15,1,15,50,'ug/mL',NULL,NULL,'significant; exact % to confirm from Fig 2.5-2.8'),
    (16,1,16,50,'ug/mL',NULL,NULL,'tested, not significant'),
    (17,1,17,50,'ug/mL',NULL,NULL,'significant; exact % to confirm from Fig 2.5-2.8');

INSERT INTO assay_results (result_id, bioassay_id, extract_id, concentration, concentration_unit, result_pct, std_dev, notes) VALUES
    (18,1,18,50,'ug/mL',NULL,NULL,'significant; exact % to confirm from Fig 2.5-2.8'),
    (19,1,19,50,'ug/mL',NULL,NULL,'tested, not significant'),
    (20,1,20,50,'ug/mL',44.8,0.1,'significant; exact % from thesis prose'),
    (21,1,21,50,'ug/mL',NULL,NULL,'tested, not significant'),
    (22,1,22,50,'ug/mL',NULL,NULL,'tested, not significant'),
    (23,1,23,50,'ug/mL',NULL,NULL,'tested, not significant'),
    (24,1,24,50,'ug/mL',NULL,NULL,'tested, not significant'),
    (25,1,25,50,'ug/mL',NULL,NULL,'tested, not significant'),
    (26,1,26,50,'ug/mL',NULL,NULL,'tested, not significant'),
    (27,1,27,50,'ug/mL',NULL,NULL,'tested, not significant'),
    (28,1,28,50,'ug/mL',NULL,NULL,'tested, not significant'),
    (29,1,29,50,'ug/mL',NULL,NULL,'tested, not significant'),
    (30,1,30,50,'ug/mL',NULL,NULL,'tested, not significant'),
    (31,1,31,50,'ug/mL',NULL,NULL,'tested, not significant'),
    (32,1,32,50,'ug/mL',NULL,NULL,'significant; exact % to confirm from Fig 2.5-2.8'),
    (33,1,33,50,'ug/mL',NULL,NULL,'tested, not significant'),
    (34,1,34,50,'ug/mL',NULL,NULL,'tested, not significant');

INSERT INTO compounds (compound_id, compound_name, molecular_class, id_status, id_method) VALUES
    (1,'isoquercetin','flavonoid','tentative','UPLC-QTOF-MS'),
    (2,'myricetin-3-O-alpha-L-rhamnopyranoside','flavonoid','tentative','UPLC-QTOF-MS'),
    (3,'quercetin-3-O-rhamnoside','flavonoid','tentative','UPLC-QTOF-MS'),
    (4,'quercetin','flavonoid','tentative','UPLC-QTOF-MS'),
    (5,'quinic acid','organic acid','tentative','UPLC-QTOF-MS'),
    (6,'3,5-dicaffeoylquinic acid','phenolic acid','tentative','UPLC-QTOF-MS'),
    (7,'rutin','flavonoid','tentative','UPLC-QTOF-MS'),
    (8,'valeriananoid E','saponin','tentative','UPLC-QTOF-MS'),
    (9,'acuminoside','saponin','tentative','UPLC-QTOF-MS'),
    (10,'dictamnoside D','saponin','tentative','UPLC-QTOF-MS'),
    (11,'2''''-O-beta-D-glucopyranosylsaikosaponin B2','saponin','tentative','UPLC-QTOF-MS'),
    (12,'clinoposaponin C','saponin','tentative','UPLC-QTOF-MS'),
    (13,'spinasaponin C','saponin','tentative','UPLC-QTOF-MS'),
    (14,'cynarin','phenolic acid','tentative','UPLC-QTOF-MS'),
    (15,'alternoside IX','saponin','tentative','UPLC-QTOF-MS'),
    (16,'alternoside I','saponin','tentative','UPLC-QTOF-MS'),
    (17,'saikogenin B4','saponin','tentative','UPLC-QTOF-MS'),
    (18,'acetylated glycosydated crotoxigenin','cardenolide glycoside','isolated','NMR'),
    (19,'xysmalogenin-3-beta-D-glucopyranoside','cardenolide glycoside','isolated','NMR'),
    (20,'crotoxigenin-3-O-beta-digitalopyranoside','cardenolide glycoside','isolated','NMR'),
    (21,'desglucouzarin','cardenolide glycoside','isolated','NMR');

INSERT INTO sample_compounds (id, compound_id, extract_id) VALUES
    (1,1,20),(2,2,20),(3,3,20),(4,4,20),
    (5,5,12),(6,6,12),(7,7,12),(8,8,12),(9,9,12),
    (10,10,12),(11,11,12),(12,12,12),(13,13,12),
    (14,14,2),(15,15,2),(16,16,2),(17,17,2),
    (18,18,9),(19,19,9),(20,20,9),(21,21,9);
