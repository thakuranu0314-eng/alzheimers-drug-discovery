# Alzheimer's Thesis RAG Benchmark Dataset

This benchmark dataset is used to evaluate the Alzheimer's Thesis RAG system.

Each benchmark question includes:

- Difficulty
- Expected answer
- Key concepts
- Expected pages
- Evaluation criteria

---

# B001

## Category
Basic Retrieval

## Difficulty
⭐ Easy

## Question
What was the main objective of this PhD research?

## Expected Answer
The main objective of this PhD research was to identify, characterize, and develop new natural ingredients from South African medicinal plants for the treatment of Alzheimer's disease by reducing Aβ42 levels, thereby decreasing beta-amyloid plaque formation.

## Key Concepts

- Alzheimer's disease
- South African medicinal plants
- Aβ42 reduction
- Natural product drug discovery

## Expected Pages

Page 4–5

## Evaluation Criteria

A correct answer should mention:

- South African medicinal plants
- Alzheimer's disease
- Reduction of Aβ42
- Development of natural therapeutic ingredients

---

# B002

## Category
Experimental Results

## Difficulty
⭐⭐ Easy

## Question
Which four plant extracts showed significant Aβ42 reduction?

## Expected Answer

- Heteromorpha arborescens (stem extract)
- Xysmalobium undulatum (leaf extract)
- Cussonia paniculata (leaf extract)
- Schotia brachypetala (leaf extract)

## Key Concepts

- Four active plant extracts
- Experimental screening
- Aβ42 reduction

## Expected Pages

Page 79

Page 215–216

## Evaluation Criteria

A correct answer should:

- List all four plant extracts.
- Correctly identify stem vs leaf.
- Not omit any plant.
- Not introduce additional plants.

---

# B003

## Category
Chemical Profiling

## Difficulty
⭐⭐⭐ Medium

## Question

Which compounds were identified from Schotia brachypetala?

## Expected Answer

Major flavonoids identified include:

- Myricetin-3-O-α-L-rhamnopyranoside
- Isoquercetin
- Quercetin-3-O-rhamnoside
- Quercetin

Isoquercetin was confirmed using a pure standard.

## Key Concepts

- UPLC-QTOF-MS
- Schotia brachypetala
- Flavonoids
- Compound identification

## Expected Pages

Page 141

Page 216

## Evaluation Criteria

The answer should retrieve the experimental compound identification results rather than only background phytochemistry.

# E001

## Category
Experimental Methods

## Difficulty
⭐⭐ Easy–Medium

## Question
What extraction solvent was used to prepare the plant extracts?

## Expected Answer

The plant extracts were prepared using a mixture of dichloromethane and methanol (DCM:MeOH) in a 1:1 ratio.

## Key Concepts

- Dichloromethane
- Methanol
- DCM:MeOH
- 1:1 ratio
- Plant extraction

## Expected Pages

- Page 59
- Page 207

## Evaluation Criteria

A correct answer should:
- Identify dichloromethane and methanol.
- State the 1:1 ratio.
- Not introduce a different extraction solvent.

# E002

## Category
Experimental Methods

## Difficulty
⭐⭐ Easy–Medium

## Question

Which cell line was used for the Aβ42 bioassay?

## Expected Answer

The Aβ42 bioassay was performed using APPsw-transfected HeLa cells.

## Key Concepts

- APPsw-transfected HeLa cells
- Aβ42 bioassay
- Cell culture
- Biological assay

## Expected Pages

- Page 75
- Page 171
- Page 197–198

## Evaluation Criteria

A correct answer should:

- Identify APPsw-transfected HeLa cells.
- Clearly state that this cell line was used for the Aβ42 bioassay.
- Avoid mentioning unrelated cell lines.

# M001

## Category
Multi-hop Reasoning

## Difficulty
⭐⭐⭐⭐ Hard

## Question

Why were the four most active plant extracts selected for further investigation?

## Expected Answer

The four plant extracts were selected because they showed the most significant reduction in Aβ42 levels during the screening experiments. They were therefore chosen for dose-dependent studies and UPLC-QTOF-MS analysis to identify the active compounds responsible for the observed biological activity.

## Key Concepts

- Aβ42 reduction
- Selection criteria
- Dose-dependent studies
- UPLC-QTOF-MS
- Active compound identification

## Expected Pages

- Page 79
- Page 216

## Evaluation Criteria

A correct answer should explain:

- They produced the greatest reduction in Aβ42.
- They were selected for further biological evaluation.
- They were analyzed by UPLC-QTOF-MS to identify active compounds.

# C001

## Category
Chemical Profiling

## Difficulty
⭐⭐⭐ Medium

## Question

Why was ESI negative mode used during the UPLC-QTOF-MS analysis?

## Expected Answer

ESI negative mode was used because it produced higher intensity peaks than the positive mode, making it more suitable for identifying the compounds during UPLC-QTOF-MS analysis.

## Key Concepts

- ESI negative mode
- UPLC-QTOF-MS
- Higher intensity peaks
- Compound identification

## Expected Pages

- Page 208–209

## Evaluation Criteria

A correct answer should:

- Explain that the negative mode produced higher intensity peaks.
- State that this was the reason it was selected.
- Avoid introducing unsupported explanations.
