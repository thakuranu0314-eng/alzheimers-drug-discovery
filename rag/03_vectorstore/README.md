# Module 3 – FAISS Vector Store

## Objective

The purpose of this module is to build a searchable vector database from the document embeddings.

Instead of comparing every embedding manually, FAISS indexes the vectors and enables fast semantic similarity search.

---

## Input

```
data/processed/thesis_embeddings.npy
```

---

## Output

```
vectorstore/thesis.index
```

---

## Pipeline

```
Saved Embeddings
        │
        ▼
Load Embeddings
        │
        ▼
Build FAISS Index
        │
        ▼
Store 540 Vectors
        │
        ▼
Save Index
```

---

## Project Structure

```
03_vectorstore/
│
├── vectorstore_pipeline.py
└── README.md
```

---

## Functions

### load_embeddings()

Loads the saved embedding matrix from disk.

Returns:

- NumPy array
- Shape: (540, 384)

---

### build_faiss_index()

Creates a FAISS searchable vector index.

Current implementation uses:

```
IndexFlatIP
```

for cosine similarity search.

---

### save_faiss_index()

Stores the vector index on disk.

Output:

```
vectorstore/thesis.index
```

---

### load_faiss_index()

Loads a previously saved FAISS index.

---

### run_vectorstore_pipeline()

Runs the complete vector indexing workflow.

---

## Output Statistics

Current project:

- Total vectors: **540**
- Embedding dimensions: **384**

---

## Why FAISS?

Without FAISS:

```
Question
      │
Compare against
540 vectors one-by-one
```

With FAISS:

```
Question
      │
      ▼
FAISS Index
      │
      ▼
Nearest vectors
```

FAISS is optimized for fast similarity search and scales efficiently to millions of vectors.

---

## Skills Demonstrated

- Vector indexing
- Semantic search preparation
- FAISS
- NumPy
- Modular pipeline design

---

## Next Module

```
04_retrieval/
```

The FAISS index is queried to retrieve the most relevant thesis chunks for a user question.
