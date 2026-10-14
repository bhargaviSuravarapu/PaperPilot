from generator import (
    BacktrackingStrategy,
    BranchBoundStrategy,
    DPStrategy,
    GreedyStrategy,
)
from models import Question


def create_questions():
    return [
        Question(1, "Q1", 1, "easy", 2, "Python"),
        Question(2, "Q2", 1, "medium", 5, "Python"),
        Question(3, "Q3", 2, "hard", 10, "DSA"),
        Question(4, "Q4", 2, "medium", 5, "Python"),
    ]


def test_greedy_strategy():
    result = GreedyStrategy().select(create_questions(), 10)
    assert sum(q.marks for q in result) <= 10


def test_dp_strategy():
    result = DPStrategy().select(create_questions(), 12)
    assert sum(q.marks for q in result) == 12


def test_backtracking_strategy():
    result = BacktrackingStrategy().select(create_questions(), 12)
    assert sum(q.marks for q in result) == 12


def test_branch_bound_strategy():
    result = BranchBoundStrategy().select(create_questions(), 12)
    assert sum(q.marks for q in result) == 12

from generator import ExamPaperGenerator
from models import PaperSpecification


def test_complete_paper_generation():
    questions = create_questions()

    specification = PaperSpecification(
        total_marks=12,
        easy_count=1,
        medium_count=2,
        hard_count=0
    )

    generator = ExamPaperGenerator(DPStrategy())

    paper = generator.generate(
        questions,
        specification
    )

    assert sum(q.marks for q in paper) == 12