import json
from pathlib import Path

import numpy as np
from sentence_transformers import SentenceTransformer


CHUNKS_PATH = Path("data/processed/thesis_chunks.json")
EMBEDDINGS_PATH = Path("data/processed/thesis_embeddings.npy")

MODEL_NAME = "all-MiniLM-L6-v2"


def load_chunks(chunks_path):
    """
    Load processed text chunks from JSON.
    """
    with open(chunks_path, "r", encoding="utf-8") as file:
        chunks = json.load(file)

    return chunks


def load_embedding_model(model_name):
    """
    Load the Sentence Transformers embedding model.
    """
    model = SentenceTransformer(model_name)

    return model


def create_embeddings(chunks, model):
    """
    Convert chunk text into numerical embeddings.
    """
    texts = [chunk["text"] for chunk in chunks]

    embeddings = model.encode(
    texts,
    show_progress_bar=True,
    normalize_embeddings=True,
)

    return embeddings


def save_embeddings(embeddings, output_path):
    """
    Save embeddings as a NumPy .npy file.
    """
    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    np.save(
        output_path,
        embeddings,
    )


def load_embeddings(embeddings_path):
    """
    Load previously saved embeddings.
    """
    embeddings = np.load(embeddings_path)

    return embeddings


def run_embedding_pipeline():
    """
    Run the complete embedding pipeline.
    """

    print("Loading chunks...")
    chunks = load_chunks(CHUNKS_PATH)

    print(f"Chunks loaded: {len(chunks)}")

    print("\nLoading embedding model...")
    model = load_embedding_model(MODEL_NAME)

    print(f"Model loaded: {MODEL_NAME}")

    print("\nCreating embeddings...")
    embeddings = create_embeddings(
        chunks,
        model,
    )

    print("\nEmbedding generation complete.")

    print(
        f"Number of embeddings: "
        f"{embeddings.shape[0]}"
    )

    print(
        f"Embedding dimensions: "
        f"{embeddings.shape[1]}"
    )

    print("\nSaving embeddings...")

    save_embeddings(
        embeddings,
        EMBEDDINGS_PATH,
    )

    print(
        f"Embeddings saved to: "
        f"{EMBEDDINGS_PATH}"
    )

    return chunks, embeddings


if __name__ == "__main__":
    chunks, embeddings = run_embedding_pipeline()

    print("\nExample chunk:")
    print("-" * 60)

    print(chunks[0]["text"][:300])

    print("\nFirst 10 embedding values:")
    print(embeddings[0][:10])

    print("\nTesting saved embeddings...")

    saved_embeddings = load_embeddings(
        EMBEDDINGS_PATH
    )

    print(
        f"Saved embedding shape: "
        f"{saved_embeddings.shape}"
    )
