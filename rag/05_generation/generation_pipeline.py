from pathlib import Path
import sys
import os

from dotenv import load_dotenv
from google import genai


# ---------------------------------------------------------
# Project paths
# ---------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]
ENV_PATH = PROJECT_ROOT / ".env"

RETRIEVAL_PATH = (
    Path(__file__).resolve().parents[1]
    / "04_retrieval"
)

sys.path.append(str(RETRIEVAL_PATH))

from retrieval_pipeline import run_retrieval_pipeline


# ---------------------------------------------------------
# Environment / API key
# ---------------------------------------------------------

def load_api_key():
    """
    Load the Gemini API key from the project .env file.
    """

    load_dotenv(
        dotenv_path=ENV_PATH,
        override=True,
    )

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY was not found in the .env file."
        )

    return api_key


# ---------------------------------------------------------
# Gemini client
# ---------------------------------------------------------

def create_gemini_client(api_key):
    """
    Create and return a Gemini API client.
    """

    client = genai.Client(
        api_key=api_key
    )

    return client


# ---------------------------------------------------------
# Prompt builder
# ---------------------------------------------------------

def build_prompt(query, retrieved_chunks):
    """
    Build a grounded scientific prompt using
    the retrieved thesis chunks.
    """

    context_parts = []

    for chunk in retrieved_chunks:
        context_parts.append(
            f"Page {chunk['page']}, Chunk {chunk['chunk']}\n"
            f"{chunk['text']}"
        )

    context = "\n\n---\n\n".join(context_parts)

    prompt = f"""
You are a scientific research assistant.

Answer the user's question using ONLY the information
provided in the context below.

Do not use outside knowledge.

If the answer cannot be found in the supplied context,
say:

"I could not find the answer in the provided document."

When possible, mention the relevant page number.

Context
=======

{context}


Question
========

{query}


Answer
======
"""

    return prompt.strip()


# ---------------------------------------------------------
# Gemini generation
# ---------------------------------------------------------

def generate_answer(client, prompt):
    """
    Send the RAG prompt to Gemini and return
    the generated answer.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text


# ---------------------------------------------------------
# Complete generation pipeline
# ---------------------------------------------------------

def run_generation_pipeline(query):
    """
    Run retrieval + prompt building + Gemini generation.
    """

    print("Retrieving relevant thesis chunks...")

    retrieved_chunks = run_retrieval_pipeline(
        query
    )

    print(
        f"Retrieved chunks: "
        f"{len(retrieved_chunks)}"
    )

    print("\nBuilding prompt...")

    prompt = build_prompt(
        query=query,
        retrieved_chunks=retrieved_chunks,
    )

    print("Loading Gemini API key...")

    api_key = load_api_key()

    print("Creating Gemini client...")

    client = create_gemini_client(
        api_key
    )

    print("Generating answer...")

    answer = generate_answer(
        client=client,
        prompt=prompt,
    )

    return {
        "query": query,
        "answer": answer,
        "sources": retrieved_chunks,
    }


# ---------------------------------------------------------
# Test
# ---------------------------------------------------------

if __name__ == "__main__":

    question = (
        "Which plant extract showed the highest "
        "reduction of Aβ42?"
    )

    result = run_generation_pipeline(
        question
    )

    print("\n" + "=" * 80)
    print("QUESTION")
    print("=" * 80)
    print(result["query"])

    print("\n" + "=" * 80)
    print("ANSWER")
    print("=" * 80)
    print(result["answer"])

    print("\n" + "=" * 80)
    print("SOURCES")
    print("=" * 80)

    for source in result["sources"]:
        print(
            f"Page {source['page']} | "
            f"Chunk {source['chunk']}"
        )
