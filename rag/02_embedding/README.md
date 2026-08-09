# Module 2 – Embedding Pipeline

## Objective

Convert processed text chunks into semantic vector embeddings.

## Input

- data/processed/thesis_chunks.json

## Output

- data/processed/thesis_embeddings.npy

## Embedding Model

- all-MiniLM-L6-v2 (Sentence Transformers)

## Pipeline

Chunks
↓
Load embedding model
↓
Generate embeddings
↓
Save embeddings (.npy)

## Functions

- load_chunks()
- load_embedding_model()
- create_embeddings()
- save_embeddings()
- load_embeddings()
- run_embedding_pipeline()

## Output Shape

540 chunks × 384-dimensional embeddings
