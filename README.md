# 🧠 AI-Powered Alzheimer's Drug Discovery

### Transforming PhD research into an AI-powered scientific knowledge and drug discovery platform

This project combines **natural product chemistry, Alzheimer's disease research, data science, and Generative AI** to explore medicinal plants and bioactive compounds with potential relevance to Alzheimer's drug discovery.

The project is built around research from my PhD in **Natural Product Chemistry**, where I investigated South African medicinal plants for their ability to reduce **amyloid-beta 42 (Aβ42)** levels and isolated bioactive natural products.

Rather than leaving this research only in a traditional thesis format, I am transforming it into a structured, searchable, and AI-assisted research platform.

The project currently combines:

* 🧪 Natural product and Alzheimer's research
* 🗄️ Relational scientific database design
* 📊 Exploratory data analysis
* 📄 Scientific document processing
* 🧠 Sentence-transformer embeddings
* 🔎 FAISS semantic search
* 🤖 Retrieval-Augmented Generation (RAG)
* 💬 LLM-powered scientific question answering

---

## 🎯 Project Goal

Scientific knowledge is often distributed across theses, publications, experimental datasets, tables, and supplementary documents.

This makes it difficult to quickly answer questions such as:

* Which medicinal plants showed the strongest activity?
* Which compounds were isolated from active extracts?
* What experimental evidence supports a particular compound?
* Which plants or compounds affected Aβ42 levels?
* What conclusions were reported in the original research?
* Where exactly in the thesis is a particular result discussed?

The goal of this project is to build a system that can transform this scientific information into a structured knowledge base and allow researchers to explore it using both **data analysis and natural-language questions**.

---

# 🔬 Scientific Background

Alzheimer's disease is a progressive neurodegenerative disorder and one of the major causes of dementia worldwide.

One important pathological feature associated with Alzheimer's disease is the accumulation of **amyloid-beta (Aβ) peptides**, particularly **Aβ42**.

My PhD research investigated **South African medicinal plants** as potential sources of compounds capable of influencing Aβ42 levels.

The research involved:

* medicinal plant screening
* biological activity assays
* extraction and fractionation
* chromatographic separation
* compound isolation
* structural characterization
* mass spectrometry
* NMR spectroscopy
* analysis of Aβ42-related biological activity

This project brings that scientific research into a modern computational workflow.

---

# 💡 From PhD Thesis to AI Research Assistant

A traditional thesis contains a large amount of valuable scientific information, but finding a specific result may require manually searching hundreds of pages.

This project explores a different approach:

```text
PhD Research
     │
     ▼
Scientific Data
     │
     ├──────────────► SQLite Database
     │                     │
     │                     ▼
     │               Data Analysis
     │
     ▼
PhD Thesis
     │
     ▼
Text Extraction
     │
     ▼
Text Chunking
     │
     ▼
Sentence Embeddings
     │
     ▼
FAISS Vector Database
     │
     ▼
Semantic Retrieval
     │
     ▼
Relevant Scientific Context
     │
     ▼
Large Language Model
     │
     ▼
Grounded Scientific Answer
```

The result is an AI-assisted system that can retrieve relevant sections of the original research before generating an answer.

---

# 🤖 Retrieval-Augmented Generation (RAG)

A major component of this project is a **Retrieval-Augmented Generation pipeline** built using my PhD thesis as the primary knowledge source.

Instead of asking an LLM to answer directly from its general training knowledge, the system first searches the thesis for relevant scientific information.

### RAG workflow

```text
User Question
      │
      ▼
Question Embedding
      │
      ▼
FAISS Similarity Search
      │
      ▼
Top Relevant Thesis Chunks
      │
      ▼
Context + Question
      │
      ▼
LLM
      │
      ▼
Research-Grounded Answer
```

### Current RAG pipeline

The thesis is processed and divided into approximately **540 searchable text chunks**.

Semantic embeddings are generated using:

`all-MiniLM-L6-v2`

The embeddings are stored in a **FAISS vector index**, allowing the system to retrieve thesis sections based on semantic similarity rather than only exact keyword matching.

The retrieved scientific context is then provided to an LLM together with the user's question.

This allows the model to generate answers grounded in the underlying research.

---

# 🧠 Why RAG?

A general-purpose LLM may know about Alzheimer's disease, medicinal plants, or amyloid-beta biology.

However, it does not automatically know the detailed experimental findings contained in a specific PhD thesis.

For example:

> Which medicinal plants in this research showed the strongest reduction in Aβ42?

Without access to the thesis, an LLM may provide a general answer or potentially generate unsupported information.

With RAG:

```text
Question
   ↓
Search the thesis
   ↓
Retrieve relevant experiments
   ↓
Provide evidence to the LLM
   ↓
Generate an answer based on the research
```

This makes the system more useful for **domain-specific scientific question answering**.

---

# 🔎 Semantic Search

Traditional keyword search looks for exact words.

Semantic search instead attempts to retrieve text based on **meaning**.

For example, a researcher might ask:

> Which extracts were most effective at lowering amyloid-beta?

The thesis might describe this using terms such as:

> significant reduction in Aβ42 levels

Even though the wording is different, embeddings can place these sentences close together in vector space.

This allows the system to retrieve scientifically relevant information even when the user's wording differs from the original thesis.

---

# 🗄️ Scientific Database

Another component of the project converts experimental information into a structured **SQLite relational database**.

The current database uses a **9-table schema** designed to represent the relationships between the scientific entities in the research.

The structured database makes it possible to query experimental information systematically rather than relying entirely on unstructured thesis text.

Example research relationships include:

```text
Plant
  │
  ▼
Extract
  │
  ▼
Bioactivity
  │
  ▼
Fraction
  │
  ▼
Compound
  │
  ▼
Experimental Evidence
```

This structured-data layer complements the unstructured RAG knowledge base.

---

# 📊 Exploratory Data Analysis

The repository also contains exploratory analysis of the structured scientific data.

The analysis is designed to investigate questions such as:

* Which plants showed the highest biological activity?
* How does activity vary across extracts?
* Which compounds are associated with promising experimental results?
* What patterns exist across the experimental dataset?

The analysis is available in:

```text
notebooks/
└── 01_exploratory_analysis.ipynb
```

---

# 🏗️ Repository Structure

```text
alzheimers-drug-discovery/
│
├── database/
│   ├── schema.sql
│   └── load_data.sql
│
├── docs/
│   ├── 01_project_overview.md
│   ├── 02_database_design.md
│   └── 03_setup_notes.md
│
├── notebooks/
│   └── 01_exploratory_analysis.ipynb
│
├── rag/
│   ├── 01_ingestion/
│   ├── 02_embedding/
│   ├── 03_vectorstore/
│   ├── 04_retrieval/
│   ├── 05_generation/
│   └── 06_evaluation/
│
├── .gitignore
│
└── README.md
```

The RAG directory intentionally follows the complete pipeline:

```text
Ingestion
   ↓
Embedding
   ↓
Vector Store
   ↓
Retrieval
   ↓
Generation
   ↓
Evaluation
```

This modular structure makes each stage easier to understand, test, and improve independently.

---

# ⚙️ RAG Pipeline Components

## 1. Document Ingestion

The thesis is loaded and converted into machine-readable text.

The extracted content is cleaned and divided into smaller chunks suitable for semantic retrieval.

```text
Thesis
  ↓
Text extraction
  ↓
Cleaning
  ↓
Chunking
```

---

## 2. Embedding Generation

Each text chunk is converted into a numerical vector using a sentence-transformer embedding model.

Current embedding model:

```text
all-MiniLM-L6-v2
```

Embeddings capture semantic information about each piece of text.

---

## 3. Vector Store

The generated embeddings are indexed using **FAISS (Facebook AI Similarity Search)**.

FAISS allows efficient similarity searches across the thesis embeddings.

---

## 4. Retrieval

When a user asks a question:

1. The question is converted into an embedding.
2. FAISS compares it with stored thesis embeddings.
3. The most semantically similar chunks are retrieved.
4. These chunks become the context for answer generation.

---

## 5. Answer Generation

The retrieved thesis passages and the user's question are combined into a prompt.

```text
Retrieved Context
       +
User Question
       ↓
Prompt
       ↓
LLM
       ↓
Grounded Answer
```

The objective is to encourage the model to answer from retrieved scientific evidence rather than relying only on general model knowledge.

---

## 6. Evaluation

The final stage of the RAG pipeline focuses on evaluating retrieval and answer quality.

Important areas include:

* relevance of retrieved chunks
* scientific accuracy
* faithfulness to source material
* answer completeness
* hallucination reduction

Evaluation is particularly important for scientific RAG applications because a fluent answer is not necessarily a scientifically correct answer.

---

# 🧰 Technology Stack

| Area                | Technologies                     |
| ------------------- | -------------------------------- |
| Programming         | Python, SQL                      |
| Database            | SQLite                           |
| Data Analysis       | Pandas, NumPy                    |
| Visualization       | Matplotlib                       |
| Document Processing | Python-based PDF/text processing |
| Embeddings          | Sentence Transformers            |
| Embedding Model     | all-MiniLM-L6-v2                 |
| Vector Search       | FAISS                            |
| Generative AI       | Large Language Models            |
| AI Architecture     | Retrieval-Augmented Generation   |
| Development         | Jupyter Notebook, VS Code        |
| Version Control     | Git, GitHub                      |

---

# 🚧 Project Status

This is an actively developing portfolio and research project.

### Completed / in development

* ✅ Scientific database architecture
* ✅ 9-table SQLite schema
* ✅ Initial data loading workflow
* ✅ Exploratory data analysis
* ✅ Thesis document ingestion
* ✅ Text chunking
* ✅ Sentence-transformer embeddings
* ✅ FAISS vector store
* ✅ Semantic retrieval
* ✅ RAG answer-generation workflow
* 🔄 RAG evaluation and optimization
* 🔄 Interactive research interface
* 🔄 Additional scientific analytics

---

# 🗺️ Future Development

The long-term goal is to evolve this repository from a thesis-based RAG experiment into a broader **AI-assisted drug discovery research platform**.

Potential future developments include:

### 🧬 Molecular Informatics

Integrate **RDKit** for:

* molecular structure processing
* molecular descriptors
* chemical fingerprints
* compound similarity
* structure visualization

### 🤖 Machine Learning

Develop models for exploring relationships between molecular properties and biological activity.

Potential approaches include:

* Random Forest
* XGBoost
* LightGBM
* molecular fingerprint-based models

### 🔍 Explainable AI

Use techniques such as **SHAP** to investigate which molecular or experimental features contribute most strongly to model predictions.

### 💻 Interactive Application

Develop a **Streamlit dashboard** where users can:

* explore medicinal plants
* inspect compounds
* analyze biological activity
* search experimental results
* ask questions about the thesis
* interact with the RAG research assistant

### ☁️ Deployment

Deploy the final application so that the research platform can be explored through a web interface.

---

# 🌱 Why This Project Matters

This project is also an exploration of how **domain expertise and artificial intelligence can complement each other**.

Scientific AI systems need more than models and algorithms. Understanding experimental design, biological assays, chemical structures, analytical techniques, and the limitations of scientific evidence is equally important.

By combining my background in **natural product chemistry and Alzheimer's research** with **data science and Generative AI**, this project explores how modern computational tools can help organize, retrieve, analyze, and communicate complex scientific knowledge.

---

# 👩‍🔬 About the Author

**Dr. Anuradha Thakur**

Ph.D. in Natural Product Chemistry | Data Science & AI

My background combines scientific research with data science and artificial intelligence.

My research experience includes natural product chemistry, Alzheimer's disease research, medicinal plants, bioactivity screening, chromatography, mass spectrometry, NMR, and experimental data analysis.

More recently, I have been expanding this expertise into:

* Machine Learning
* Data Analytics
* Generative AI
* Large Language Models
* Retrieval-Augmented Generation
* Scientific AI applications

This project represents the intersection of these two areas:

**Scientific domain expertise × Data Science × Generative AI**

---

## ⚠️ Disclaimer

This repository is a research and portfolio project based on academic research.

The information and AI-generated outputs are intended for research, educational, and demonstration purposes only and should not be interpreted as medical advice or clinical recommendations.

---

## ⭐ Project Vision

> Turn static scientific research into an interactive AI-powered knowledge system that helps researchers explore experimental evidence, compounds, and scientific insights more efficiently.
