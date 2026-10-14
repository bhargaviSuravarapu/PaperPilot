from async_processing import run_async_processing
from models import Question


def test_async_processing():
    questions = [
        Question(1, "Q1", 1, "easy", 2, "Python"),
        Question(2, "Q2", 2, "medium", 5, "DSA"),
        Question(3, "Q3", 3, "hard", 10, "OOP"),
    ]

    result = run_async_processing(questions)

    assert len(result) == 3
    assert result[0] == "Python: 2 marks"
    assert result[1] == "DSA: 5 marks"
    assert result[2] == "OOP: 10 marks"