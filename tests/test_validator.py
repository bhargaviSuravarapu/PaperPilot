from models import PaperSpecification, Question
from validator import PaperValidator


def test_total_marks():
    questions = [
        Question(1, "Q1", 1, "easy", 2, "Python"),
        Question(2, "Q2", 1, "medium", 5, "Python"),
    ]

    specification = PaperSpecification(
        total_marks=7,
        easy_count=1,
        medium_count=1,
        hard_count=0
    )

    assert PaperValidator.validate_total_marks(
        questions,
        specification.total_marks
    )


def test_no_duplicates():
    questions = [
        Question(1, "Q1", 1, "easy", 2, "Python"),
        Question(1, "Q1", 1, "easy", 2, "Python"),
    ]

    assert PaperValidator.has_duplicates(questions)

def test_difficulty_distribution():
    questions = [
        Question(1, "Q1", 1, "easy", 2, "Python"),
        Question(2, "Q2", 1, "medium", 5, "Python"),
        Question(3, "Q3", 1, "hard", 10, "Python"),
    ]

    specification = PaperSpecification(
        total_marks=17,
        easy_count=1,
        medium_count=1,
        hard_count=1
    )

    assert PaperValidator.validate_difficulty(
        questions,
        specification
    )
def test_complete_validation():
    questions = [
        Question(1, "Q1", 1, "easy", 2, "Python"),
        Question(2, "Q2", 1, "medium", 5, "Python"),
        Question(3, "Q3", 1, "hard", 10, "Python"),
    ]

    specification = PaperSpecification(
        total_marks=17,
        easy_count=1,
        medium_count=1,
        hard_count=1
    )

    assert PaperValidator.validate(
        questions,
        specification
    )


def test_invalid_paper():
    questions = [
        Question(1, "Q1", 1, "easy", 2, "Python"),
        Question(2, "Q2", 1, "medium", 5, "Python"),
    ]

    specification = PaperSpecification(
        total_marks=20,
        easy_count=1,
        medium_count=1,
        hard_count=1
    )

    assert not PaperValidator.validate(
        questions,
        specification
    )