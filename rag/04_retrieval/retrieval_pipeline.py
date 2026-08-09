import json
from pathlib import Path

import faiss
from sentence_transformers import SentenceTransformer


# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------

CHUNKS_PATH = Path(
    "data/processed/thesis_chunks.json"
)

INDEX_PATH = Path(
    "vectorstore/thesis.index"
)

MODEL_NAME = "all-MiniLM-L6-v2"

TOP_K = 5
NEIGHBOR_WINDOW = 1


# ---------------------------------------------------------
# Load chunks
# ---------------------------------------------------------

def load_chunks(chunks_path):
    """
    Load processed thesis chunks from JSON.
    """

    with open(
        chunks_path,
        "r",
        encoding="utf-8",
    ) as file:
        chunks = json.load(file)

    return chunks


# ---------------------------------------------------------
# Load FAISS index
# ---------------------------------------------------------

def load_faiss_index(index_path):
    """
    Load the saved FAISS vector index.
    """

    index = faiss.read_index(
        str(index_path)
    )

    return index


# ---------------------------------------------------------
# Load embedding model
# ---------------------------------------------------------

def load_embedding_model(model_name):
    """
    Load the same embedding model used
    to embed the thesis chunks.
    """

    model = SentenceTransformer(
        model_name
    )

    return model


# ---------------------------------------------------------
# Embed query
# ---------------------------------------------------------

def embed_query(query, model):
    """
    Convert the user question into
    a normalized embedding.
    """

    query_embedding = model.encode(
        [query],
        normalize_embeddings=True,
    )

    return query_embedding.astype(
        "float32"
    )


# ---------------------------------------------------------
# Search FAISS
# ---------------------------------------------------------

def search_index(
    query_embedding,
    index,
    top_k=TOP_K,
):
    """
    Search the FAISS index.

    Because the index uses IndexFlatIP and
    normalized vectors, higher scores mean
    greater semantic similarity.
    """

    scores, indices = index.search(
        query_embedding,
        top_k,
    )

    return scores[0], indices[0]


# ---------------------------------------------------------
# Retrieve top FAISS matches
# ---------------------------------------------------------

def retrieve_chunks(
    query,
    chunks,
    model,
    index,
    top_k=TOP_K,
):
    """
    Retrieve the top matching thesis chunks.
    """

    query_embedding = embed_query(
        query=query,
        model=model,
    )

    scores, indices = search_index(
        query_embedding=query_embedding,
        index=index,
        top_k=top_k,
    )

    results = []

    for rank, (score, chunk_index) in enumerate(
        zip(scores, indices),
        start=1,
    ):

        chunk = chunks[chunk_index]

        results.append(
            {
                "rank": rank,
                "score": float(score),
                "chunk_index": int(chunk_index),
                "page": chunk["page"],
                "chunk": chunk["chunk"],
                "text": chunk["text"],
            }
        )

    return results


# ---------------------------------------------------------
# Neighbor expansion
# ---------------------------------------------------------

def expand_with_neighbors(
    results,
    chunks,
    neighbor_window=NEIGHBOR_WINDOW,
):
    """
    Expand each retrieved chunk with neighboring
    chunks from the ordered thesis chunk list.

    neighbor_window=1 means:

        previous chunk
        retrieved chunk
        next chunk
    """

    expanded_results = []
    seen_indices = set()

    for result in results:

        center_index = result["chunk_index"]

        start_index = max(
            0,
            center_index - neighbor_window,
        )

        end_index = min(
            len(chunks),
            center_index + neighbor_window + 1,
        )

        for index in range(
            start_index,
            end_index,
        ):

            if index in seen_indices:
                continue

            chunk = chunks[index]

            expanded_results.append(
                {
                    "page": chunk["page"],
                    "chunk": chunk["chunk"],
                    "text": chunk["text"],
                    "chunk_index": index,
                    "source_type": (
                        "retrieved"
                        if index == center_index
                        else "neighbor"
                    ),
                }
            )

            seen_indices.add(index)

    return expanded_results


# ---------------------------------------------------------
# Complete retrieval pipeline
# ---------------------------------------------------------

def run_retrieval_pipeline(query):
    """
    Run semantic retrieval and
    neighboring-context expansion.
    """

    print("Loading chunks...")

    chunks = load_chunks(
        CHUNKS_PATH
    )

    print(
        f"Chunks loaded: "
        f"{len(chunks)}"
    )


    print("\nLoading FAISS index...")

    index = load_faiss_index(
        INDEX_PATH
    )

    print(
        f"Vectors in FAISS index: "
        f"{index.ntotal}"
    )


    print("\nLoading embedding model...")

    model = load_embedding_model(
        MODEL_NAME
    )

    print(
        f"Model loaded: "
        f"{MODEL_NAME}"
    )


    print("\nSearching thesis...")

    results = retrieve_chunks(
        query=query,
        chunks=chunks,
        model=model,
        index=index,
        top_k=TOP_K,
    )

    print(
        f"FAISS results: "
        f"{len(results)}"
    )


    print("\nTop FAISS matches:")

    for result in results:
        print(
            f"Rank {result['rank']} | "
            f"Similarity {result['score']:.4f} | "
            f"Page {result['page']} | "
            f"Chunk {result['chunk']}"
        )


    print("\nExpanding retrieved context...")

    expanded_results = expand_with_neighbors(
        results=results,
        chunks=chunks,
        neighbor_window=NEIGHBOR_WINDOW,
    )

    print(
        f"Chunks after context expansion: "
        f"{len(expanded_results)}"
    )

    return expanded_results


# ---------------------------------------------------------
# Test
# ---------------------------------------------------------

if __name__ == "__main__":

    query = (
        "Which plant extract showed the "
        "highest reduction of Aβ42?"
    )

    print("\nQuestion:")
    print(query)

    results = run_retrieval_pipeline(
        query
    )

    print("\nExpanded Context:")

    for result in results:

        print("\n" + "=" * 80)

        print(
            f"Page        : "
            f"{result['page']}"
        )

        print(
            f"Chunk       : "
            f"{result['chunk']}"
        )

        print(
            f"Source Type : "
            f"{result['source_type']}"
        )

        print("\nText:")
        print(result["text"])
