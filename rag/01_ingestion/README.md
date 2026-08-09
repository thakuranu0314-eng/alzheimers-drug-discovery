# Module 1 – PDF Ingestion Pipeline

## Objective

The ingestion pipeline is the first stage of the RAG (Retrieval-Augmented Generation) system.

Its purpose is to convert an unstructured PDF document into clean, structured, and searchable text chunks while preserving page information for future retrieval.

---

## Input

```
data/thesis/anuradha_thakur_phd_thesis.pdf
```

---

## Output

```
data/processed/thesis_chunks.json
```

Each record contains:

```json
{
  "page": 25,
  "chunk": 2,
  "text": "..."
}
```

---

## Pipeline

```text
               PDF Thesis
                    │
                    ▼
             Load PDF Pages
                    │
                    ▼
              Clean Text
                    │
                    ▼
        Smart Text Chunking
                    │
                    ▼
        Preserve Page Metadata
                    │
                    ▼
        Save Chunks as JSON
```

---

## Project Structure

```
01_ingestion/
│
├── ingestion_pipeline.py
└── README.md
```

---

## Functions

### load_pdf()

Reads the PDF document page by page and extracts text.

Returns:

- List of pages
- Page number
- Raw text

---

### clean_text()

Removes unnecessary whitespace and formatting artifacts generated during PDF extraction.

---

### chunk_text()

Splits long text into overlapping chunks.

Features:

- Approximate chunk size of 1000 characters
- 200-character overlap
- Prefers sentence boundaries
- Avoids creating very small chunks

---

### prepare_chunks()

Processes every page by:

- Cleaning text
- Chunking text
- Attaching page metadata

Returns a list of structured chunks.

---

### save_chunks()

Stores processed chunks as JSON for later use.

---

### run_ingestion_pipeline()

Runs the complete ingestion workflow from PDF to JSON.

---

## Output Statistics

Current thesis:

- Total pages: **255**
- Total chunks: **540**
- Average chunk length: **~822 characters**
- Median chunk length: **890 characters**

---

## Why Chunking?

Large Language Models cannot process an entire thesis at once.

Instead, the document is divided into manageable chunks.

Later, semantic search retrieves only the most relevant chunks instead of the entire document.

---

## Why Preserve Page Numbers?

Each chunk keeps its original page number.

Example:

```json
{
    "page": 87,
    "chunk": 2,
    "text": "..."
}
```

This allows the RAG system to:

- trace answers back to the original source
- display citations
- improve explainability

---

## Skills Demonstrated

- PDF text extraction
- Data preprocessing
- Text cleaning
- Intelligent chunking
- Metadata management
- JSON serialization
- Modular pipeline design

---

## Next Module

```
02_embedding/
```

The processed chunks are converted into semantic vector embeddings using Sentence Transformers.
