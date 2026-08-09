# Alzheimer's Thesis RAG Evaluation Results

This document records the performance of the Alzheimer's Thesis RAG system using the benchmark dataset.

---

## Evaluation Results

| ID | Retrieval | Answer | Hallucination | Citation | Score | Root Cause | Notes |
|----|-----------|--------|---------------|----------|------:|------------|-------|
| B001 | ✅ Excellent | ✅ Correct | ❌ None | ✅ Good | 10/10 | None | Retrieved the research objective from the introduction and produced a grounded summary with page reference. |
| B002 | ✅ Excellent | ✅ Correct | ❌ None | ✅ Good | 10/10 | None | Retrieved the experimental results section and accurately listed all four active plant extracts. |
| B003 | ⚠️ Partial | ⚠️ Partially Correct | ❌ None | ⚠️ Partial | 7/10 | Retrieval | Retrieved the Schotia brachypetala chapter but prioritized background information instead of the experimental compound identification section. |
| E001 | ✅ Excellent | ✅ Correct | ❌ None | ✅ Good | 10/10 | None | Retrieved the experimental methods section and correctly identified dichloromethane:methanol (1:1) as the extraction solvent. |
| E002 | ✅ Excellent | ✅ Correct | ❌ None | ✅ Excellent | 10/10 | None | Retrieved the experimental methods section and correctly identified APPsw-transfected HeLa cells as the cell line used for the Aβ42 bioassay. |
| M001 | ❌ Poor | ❌ Incorrect | ❌ None | ❌ Missing | 4/10 | Retrieval | Failed to retrieve the discussion explaining why the four most active plant extracts were selected. Gemini correctly refused to hallucinate due to insufficient context. |
| C001 | ✅ Excellent | ✅ Correct | ❌ None | ✅ Excellent | 10/10 | None | Retrieved the analytical methods section and correctly explained that ESI negative mode was selected because it produced higher intensity peaks than the positive mode. |

---

# Evaluation Summary

## Current Version

**RAG Version:** v1.0

**Evaluation Date:** 2026-08-09

---

## Statistics

| Metric | Result |
|--------|-------:|
| Benchmark Questions | **7** |
| Average Score | **8.71 / 10** |
| Correct Answers | **5 / 7 (71.4%)** |
| Partially Correct Answers | **1 / 7 (14.3%)** |
| Incorrect Answers | **1 / 7 (14.3%)** |
| Hallucinations | **0 / 7 (0%)** |
| Excellent Retrieval | **5 / 7 (71.4%)** |
| Partial Retrieval | **1 / 7 (14.3%)** |
| Poor Retrieval | **1 / 7 (14.3%)** |

---

# Strengths

- Excellent performance on factual and objective scientific questions.
- Strong retrieval of experimental methods and experimental results.
- Accurate, grounded responses with no hallucinations observed during benchmarking.
- Consistent citation of supporting thesis pages.
- Appropriate refusal behaviour when sufficient evidence was not retrieved.

---

# Current Limitations

- Retrieval occasionally prioritizes chapter introductions or background sections over experimental findings.
- Multi-hop reasoning questions remain challenging because the required evidence is distributed across multiple sections.
- Compound identification questions would benefit from more precise retrieval of experimental result pages.

---

# Planned Improvements (Future Versions)

- Improve chunking strategy.
- Introduce metadata-aware retrieval.
- Add hybrid keyword + semantic search.
- Implement cross-encoder reranking.
- Re-run this benchmark after each major improvement and compare against the v1.0 baseline.

---

# Conclusion

The Alzheimer's Thesis RAG v1.0 demonstrates strong performance on factual scientific question answering, achieving an average benchmark score of **8.71/10** across seven representative evaluation questions. The system produced **no hallucinations** during testing, indicating that the grounding strategy is effective. The primary opportunity for improvement lies in retrieval precision for compound identification and multi-hop reasoning tasks, which will be the focus of future RAG iterations.
