from pathlib import Path

import faiss
import numpy as np


EMBEDDINGS_PATH = Path("data/processed/thesis_embeddings.npy")
INDEX_PATH = Path("vectorstore/thesis.index")


def load_embeddings(embeddings_path):
    """
    Load saved embeddings from a NumPy file.
    """
    embeddings = np.load(embeddings_path)

    return embeddings


def build_faiss_index(embeddings):
    """
    Build a FAISS index using L2 distance.
    """

    embedding_dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(embedding_dimension)

    index.add(
        embeddings.astype("float32")
    )

    return index


def save_faiss_index(index, output_path):
    """
    Save the FAISS index to disk.
    """
    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    faiss.write_index(
        index,
        str(output_path),
    )


def load_faiss_index(index_path):
    """
    Load a previously saved FAISS index.
    """
    index = faiss.read_index(
        str(index_path)
    )

    return index


def run_vectorstore_pipeline():
    """
    Run the complete vector store pipeline.
    """

    print("Loading embeddings...")

    embeddings = load_embeddings(
        EMBEDDINGS_PATH
    )

    print(
        f"Embedding shape: "
        f"{embeddings.shape}"
    )

    print("\nBuilding FAISS index...")

    index = build_faiss_index(
        embeddings
    )

    print(
        f"Vectors stored in index: "
        f"{index.ntotal}"
    )

    print("\nSaving FAISS index...")

    save_faiss_index(
        index,
        INDEX_PATH,
    )

    print(
        f"FAISS index saved to: "
        f"{INDEX_PATH}"
    )

    return index


if __name__ == "__main__":
    index = run_vectorstore_pipeline()

    print("\nTesting saved index...")

    loaded_index = load_faiss_index(
        INDEX_PATH
    )

    print(
        f"Loaded index vectors: "
        f"{loaded_index.ntotal}"
    )
