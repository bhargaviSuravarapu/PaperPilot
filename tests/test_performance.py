from models import Question
from performance import compare_algorithms


def test_performance_comparison():
    questions = [
        Question(1, "Q1", 1, "easy", 2, "Python"),
        Question(2, "Q2", 1, "medium", 5, "Python"),
        Question(3, "Q3", 2, "hard", 10, "DSA"),
        Question(4, "Q4", 2, "medium", 5, "Python"),
    ]

    greedy_result, dp_result = compare_algorithms(
        questions,
        12
    )

    assert len(greedy_result) > 0
    assert sum(q.marks for q in dp_result) == 12