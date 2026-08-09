from pathlib import Path
import re
import json
import pymupdf


THESIS_PATH = Path("data/thesis/anuradha_thakur_phd_thesis.pdf")
OUTPUT_PATH = Path("data/processed/thesis_chunks.json")

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200


def load_pdf(pdf_path):
    """
    Load a PDF and return page number + text for every page.
    """
    document = pymupdf.open(pdf_path)

    pages = []

    for page_number, page in enumerate(document, start=1):
        pages.append(
            {
                "page": page_number,
                "text": page.get_text(),
            }
        )

    return pages


def clean_text(text):
    """
    Clean extra whitespace from extracted PDF text.
    """
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def chunk_text(text, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    """
    Split text into overlapping chunks while trying
    to preserve sentence boundaries.
    """

    chunks = []

    start = 0
    text_length = len(text)

    while start < text_length:
        end = min(start + chunk_size, text_length)

        # If we are not at the end of the text,
        # try to stop at the last sentence boundary.
        if end < text_length:
            sentence_end = text.rfind(". ", start, end)

            if sentence_end > start:
                end = sentence_end + 1

        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        # Stop if we reached the end
        if end >= text_length:
            break

        # Keep overlap between neighboring chunks
        start = max(end - overlap, start + 1)

    return chunks


def prepare_chunks(pages):
    """
    Clean each page and convert it into page-aware chunks.
    """
    all_chunks = []

    for page in pages:
        cleaned_text = clean_text(page["text"])

        page_chunks = chunk_text(cleaned_text)

        for chunk_number, chunk in enumerate(page_chunks, start=1):
            all_chunks.append(
                {
                    "page": page["page"],
                    "chunk": chunk_number,
                    "text": chunk,
                }
            )

    return all_chunks


def save_chunks(chunks, output_path):
    """
    Save processed chunks as JSON.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(
            chunks,
            file,
            ensure_ascii=False,
            indent=2,
        )


def run_ingestion_pipeline():
    """
    Run the complete PDF ingestion pipeline.
    """
    print("Loading PDF...")
    pages = load_pdf(THESIS_PATH)

    print(f"Pages loaded: {len(pages)}")

    print("Cleaning and chunking...")
    chunks = prepare_chunks(pages)

    print(f"Chunks created: {len(chunks)}")

    print("Saving chunks...")
    save_chunks(chunks, OUTPUT_PATH)

    print(f"Saved to: {OUTPUT_PATH}")

    return chunks


if __name__ == "__main__":
    thesis_chunks = run_ingestion_pipeline()

    print("\nExample chunk:")
    print("-" * 60)
    print(thesis_chunks[0])
