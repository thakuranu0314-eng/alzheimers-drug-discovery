# Module 6 – RAG Evaluation

## Objective

This module evaluates the performance of the Alzheimer's Thesis RAG system using a manually curated benchmark dataset.

The objective is to measure how well the RAG pipeline:

- Retrieves relevant information from the thesis.
- Generates accurate, evidence-based answers.
- Avoids hallucinations.
- Provides useful citations.
- Identifies failure cases for future improvements.

Rather than relying on subjective impressions, this module provides a reproducible baseline that can be used to compare future versions of the RAG system.

---

# Benchmark IDs

The benchmark questions are grouped into categories that evaluate different capabilities of the RAG pipeline.

| Benchmark ID | Category | Purpose |
|--------------|----------|---------|
| **B** | Basic Retrieval | Evaluates retrieval of general thesis information, research objectives, and factual content. |
| **E** | Experimental Methods | Evaluates laboratory methods, extraction procedures, solvents, cell lines, and assay protocols. |
| **C** | Chemical Profiling | Evaluates compound identification, UPLC-QTOF-MS analysis, and phytochemical characterization. |
| **M** | Multi-hop Reasoning | Evaluates the ability to combine information from multiple sections of the thesis to answer more complex scientific questions. |

### Example

- **B001** → Basic Retrieval Question 1
- **E002** → Experimental Methods Question 2
- **C001** → Chemical Profiling Question 1
- **M001** → Multi-hop Reasoning Question 1

---

# Module Files

## benchmark_questions.md

Contains the benchmark dataset used to evaluate the RAG system.

Each benchmark question includes:

- Benchmark ID
- Category
- Difficulty
- Question
- Expected answer
- Key concepts
- Expected thesis pages
- Evaluation criteria

The current benchmark contains representative questions covering:

- Basic retrieval
- Experimental methods
- Experimental results
- Chemical profiling
- Multi-hop reasoning

---

## evaluation_results.md

Stores the manually reviewed benchmark results for RAG v1.0.

Each benchmark question is evaluated using the following criteria:

- Retrieval quality
- Answer correctness
- Hallucination detection
- Citation quality
- Overall score
- Root cause (when applicable)
- Evaluation notes

---

## evaluate_rag.py

Summarizes the benchmark evaluation by calculating performance statistics from the manually reviewed results.

Current metrics include:

- Number of benchmark questions
- Average benchmark score
- Correct answers
- Partially correct answers
- Incorrect answers
- Retrieval performance
- Hallucination rate

This script provides a reproducible numerical summary of the RAG system's performance.

---

# Current Benchmark Results (RAG v1.0)

| Metric | Result |
|---------|-------:|
| Benchmark Questions | 7 |
| Average Score | 8.71 / 10 |
| Correct Answers | 5 / 7 |
| Partially Correct Answers | 1 / 7 |
| Incorrect Answers | 1 / 7 |
| Hallucinations | 0 |

---

# Evaluation Criteria

Each benchmark question is evaluated using the following dimensions.

| Criterion | Description |
|-----------|-------------|
| Retrieval | Were the correct thesis sections retrieved? |
| Answer | Was the generated answer factually correct? |
| Hallucination | Did the model introduce unsupported information? |
| Citation | Were the retrieved sources appropriate and relevant? |
| Root Cause | If the answer failed, what was the primary reason? |

---

# Key Findings

## Strengths

- Strong retrieval of factual scientific information.
- Excellent performance on experimental methods and results.
- Accurate grounded responses using retrieved evidence.
- No hallucinations observed during benchmarking.
- Consistent citation of relevant thesis pages.
- Appropriate refusal behaviour when sufficient evidence was unavailable.

---

## Current Limitations

The evaluation identified several opportunities for improvement.

- Retrieval occasionally prioritizes chapter introductions instead of experimental sections.
- Compound identification questions require more precise retrieval.
- Multi-hop scientific reasoning remains challenging because evidence may be distributed across multiple sections.

---

# Future Improvements

Future versions of the RAG system may include:

- Improved chunking strategy
- Metadata-aware retrieval
- Hybrid semantic + keyword search
- Cross-encoder reranking
- Expanded benchmark dataset
- Automatic benchmark execution

After each major improvement, the same benchmark will be executed again to measure performance changes against the RAG v1.0 baseline.

---

# Why Evaluation Matters

Building a RAG system is not only about generating answers.

A reliable RAG system should also demonstrate that it can:

- retrieve the correct evidence,
- generate answers supported by that evidence,
- avoid hallucinations,
- expose its weaknesses,
- and provide measurable improvements over time.

The benchmark developed in this module serves as the evaluation baseline for future versions of the Alzheimer's Thesis RAG system.
