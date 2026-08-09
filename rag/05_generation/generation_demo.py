from generation_pipeline import run_generation_pipeline


def main():

    print("=" * 80)
    print("Alzheimer's Thesis RAG Chat")
    print("=" * 80)

    while True:

        query = input("\nAsk a question (type 'exit' to quit): ")

        if query.lower() == "exit":
            print("\nGoodbye!")
            break

        result = run_generation_pipeline(query)

        print("\n" + "=" * 80)
        print("ANSWER")
        print("=" * 80)
        print(result["answer"])


if __name__ == "__main__":
    main()
