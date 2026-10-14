from concurrency import process_questions, process_questions_multiprocessing
from models import Question


def test_process_questions():
    questions = [
        Question(1, "Q1", 1, "easy", 2, "Python"),
        Question(2, "Q2", 2, "medium", 5, "DSA"),
        Question(3, "Q3", 3, "hard", 10, "OOP"),
    ]

    result = process_questions(questions)

    assert len(result) == 3
    assert result[0] == "Python: 2 marks"
    assert result[1] == "DSA: 5 marks"
    assert result[2] == "OOP: 10 marks"

def test_process_questions_multiprocessing():
    questions = [
        Question(1, "Q1", 1, "easy", 2, "Python"),
        Question(2, "Q2", 2, "medium", 5, "DSA"),
        Question(3, "Q3", 3, "hard", 10, "OOP"),
    ]

    result = process_questions_multiprocessing(questions)

    assert len(result) == 3
    assert result[0] == "Processed: Q1"
    assert result[1] == "Processed: Q2"
    assert result[2] == "Processed: Q3"