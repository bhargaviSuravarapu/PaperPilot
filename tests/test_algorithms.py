from algorithms import dynamic_programming_select, greedy_select
from models import Question


def create_questions():
    return [
        Question(1, "Q1", 1, "easy", 2, "Python"),
        Question(2, "Q2", 1, "medium", 5, "Python"),
        Question(3, "Q3", 2, "hard", 10, "DSA"),
        Question(4, "Q4", 2, "medium", 5, "Python"),
    ]


def test_greedy_select():
    questions = create_questions()

    result = greedy_select(questions, 10)

    assert sum(q.marks for q in result) <= 10


def test_dynamic_programming_select():
    questions = create_questions()

    result = dynamic_programming_select(questions, 12)

    assert sum(q.marks for q in result) == 12

from algorithms import backtracking_select, branch_and_bound_select


def test_backtracking_select():
    questions = create_questions()

    result = backtracking_select(questions, 12)

    assert sum(q.marks for q in result) == 12


def test_branch_and_bound_select():
    questions = create_questions()

    result = branch_and_bound_select(questions, 12)

    assert sum(q.marks for q in result) == 12

from algorithms import calculate_total_marks, filter_by_difficulty, get_question_summary


def test_filter_by_difficulty():
    questions = create_questions()

    result = filter_by_difficulty(questions, "hard")

    assert len(result) == 1
    assert result[0].difficulty == "hard"


def test_calculate_total_marks():
    questions = create_questions()

    result = calculate_total_marks(questions)

    assert result == 22


def test_question_summary():
    questions = create_questions()

    result = get_question_summary(questions)

    assert len(result) == 4
    assert "Python - 2 marks" in result

from algorithms import merge_sort


def test_merge_sort():
    questions = create_questions()

    result = merge_sort(questions)

    marks = [q.marks for q in result]

    assert marks == sorted(marks)