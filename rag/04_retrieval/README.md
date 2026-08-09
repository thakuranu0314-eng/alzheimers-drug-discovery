# Module 4 – Semantic Retrieval

## Objective

The retrieval module searches the thesis using semantic similarity.

A user's question is converted into an embedding, compared against the FAISS vector index, and the most relevant thesis chunks are returned.

No Large Language Model (LLM) is used at this stage.

---

## Input

```
Question
```

Example:

```
Which plant extract showed the highest reduction of Aβ42?
```

---

## Resources Used

```
data/processed/thesis_chunks.json
vectorstore/thesis.index
```

---

## Output

Top-K relevant thesis chunks.

Example:

```
Page 79

Among them, four plant extracts...
```

---

## Pipeline

```
User Question
        │
        ▼
Embedding Model
        │
        ▼
Query Embedding
        │
        ▼
FAISS Search
        │
        ▼
Top K Similar Chunks
```

---

## Project Structure

```
04_retrieval/
│
├── retrieval_pipeline.py
├── retrieval_demo.py
└── README.md
```

---

## Functions

### load_chunks()

Loads processed thesis chunks.

---

### load_faiss_index()

Loads the saved FAISS vector database.

---

### load_embedding_model()

Loads the Sentence Transformers embedding model.

Current model:

```
all-MiniLM-L6-v2
```

---

### embed_query()

Converts the user's question into a numerical embedding.

---

### search_index()

Searches the FAISS vector database for the most similar embeddings.

---

### retrieve_chunks()

Returns the corresponding thesis chunks.

---

### run_retrieval_pipeline()

Runs the complete retrieval workflow.

---

## Retrieval Workflow

```
Question
     │
     ▼
Embedding
     │
     ▼
FAISS Search
     │
     ▼
Chunk IDs
     │
     ▼
Original Thesis Text
```

---

## Current Performance

The retrieval system successfully identifies semantically relevant sections for many scientific questions.

Some highly specific scientific queries may not return the exact answer in the top result because retrieval quality depends on:

- embedding model
- chunking strategy
- query wording

Future improvements may include:

- domain-specific embedding models
- reranking
- hybrid search
- metadata filtering

---

## Skills Demonstrated

- Sentence Transformers
- Query embedding
- Semantic search
- FAISS retrieval
- Information retrieval
- Modular pipeline design

---

## Next Module

```
05_llm/
```

The retrieved thesis chunks are provided to a Large Language Model (LLM) to generate grounded answers.
