from retrieval_pipeline import run_retrieval_pipeline


def print_results(results):
    """
    Print retrieved chunks in a readable format.
    """

    print("\nTop Retrieved Chunks")

    for result in results:

        print("\n" + "=" * 80)

        print(f"Rank     : {result['rank']}")
        print(f"Distance : {result['distance']:.4f}")
        print(f"Page     : {result['page']}")
        print(f"Chunk    : {result['chunk']}")

        print("\nText:")
        print(result["text"])


def main():

    print("=" * 80)
    print("Alzheimer's Thesis RAG Demo")
    print("=" * 80)

    while True:

        query = input("\nAsk a question (or type 'exit'): ")

        if query.lower() == "exit":
            print("\nGoodbye!")
            break

        results = run_retrieval_pipeline(query)

        print_results(results)


if __name__ == "__main__":
    main()
