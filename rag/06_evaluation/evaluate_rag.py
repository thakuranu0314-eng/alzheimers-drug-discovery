# ---------------------------------------------------------
# Alzheimer's Thesis RAG
# Evaluation Summary
# ---------------------------------------------------------


evaluation_results = [
    {
        "id": "B001",
        "score": 10,
        "answer": "correct",
        "retrieval": "excellent",
        "hallucination": False,
    },
    {
        "id": "B002",
        "score": 10,
        "answer": "correct",
        "retrieval": "excellent",
        "hallucination": False,
    },
    {
        "id": "B003",
        "score": 7,
        "answer": "partial",
        "retrieval": "partial",
        "hallucination": False,
    },
    {
        "id": "E001",
        "score": 10,
        "answer": "correct",
        "retrieval": "excellent",
        "hallucination": False,
    },
    {
        "id": "E002",
        "score": 10,
        "answer": "correct",
        "retrieval": "excellent",
        "hallucination": False,
    },
    {
        "id": "M001",
        "score": 4,
        "answer": "incorrect",
        "retrieval": "poor",
        "hallucination": False,
    },
    {
        "id": "C001",
        "score": 10,
        "answer": "correct",
        "retrieval": "excellent",
        "hallucination": False,
    },
]


def calculate_summary(results):
    """
    Calculate summary statistics for
    manually evaluated RAG benchmark results.
    """

    total = len(results)

    total_score = sum(
        result["score"]
        for result in results
    )

    average_score = total_score / total

    correct_answers = sum(
        result["answer"] == "correct"
        for result in results
    )

    partial_answers = sum(
        result["answer"] == "partial"
        for result in results
    )

    incorrect_answers = sum(
        result["answer"] == "incorrect"
        for result in results
    )

    excellent_retrieval = sum(
        result["retrieval"] == "excellent"
        for result in results
    )

    partial_retrieval = sum(
        result["retrieval"] == "partial"
        for result in results
    )

    poor_retrieval = sum(
        result["retrieval"] == "poor"
        for result in results
    )

    hallucinations = sum(
        result["hallucination"]
        for result in results
    )

    return {
        "total": total,
        "average_score": average_score,
        "correct_answers": correct_answers,
        "partial_answers": partial_answers,
        "incorrect_answers": incorrect_answers,
        "excellent_retrieval": excellent_retrieval,
        "partial_retrieval": partial_retrieval,
        "poor_retrieval": poor_retrieval,
        "hallucinations": hallucinations,
    }


def print_summary(summary):
    """
    Print evaluation metrics.
    """

    total = summary["total"]

    print("=" * 60)
    print("Alzheimer's Thesis RAG Evaluation")
    print("=" * 60)

    print(
        f"\nQuestions Evaluated: "
        f"{total}"
    )

    print(
        f"Average Score: "
        f"{summary['average_score']:.2f}/10"
    )

    print(
        f"\nCorrect Answers: "
        f"{summary['correct_answers']}/{total}"
    )

    print(
        f"Partially Correct: "
        f"{summary['partial_answers']}/{total}"
    )

    print(
        f"Incorrect Answers: "
        f"{summary['incorrect_answers']}/{total}"
    )

    print(
        f"\nExcellent Retrieval: "
        f"{summary['excellent_retrieval']}/{total}"
    )

    print(
        f"Partial Retrieval: "
        f"{summary['partial_retrieval']}/{total}"
    )

    print(
        f"Poor Retrieval: "
        f"{summary['poor_retrieval']}/{total}"
    )

    print(
        f"\nHallucinations: "
        f"{summary['hallucinations']}/{total}"
    )

    hallucination_rate = (
        summary["hallucinations"]
        / total
        * 100
    )

    print(
        f"Hallucination Rate: "
        f"{hallucination_rate:.1f}%"
    )


if __name__ == "__main__":

    summary = calculate_summary(
        evaluation_results
    )

    print_summary(
        summary
    )
