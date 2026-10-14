from generator import BranchBoundStrategy, ExamPaperGenerator
from models import PaperSpecification
from question_bank import QuestionBank
from validator import PaperValidator


def test_complete_exam_paper_workflow():
    bank = QuestionBank("data/questions.json")

    specification = PaperSpecification(
        total_marks=36,
        easy_count=3,
        medium_count=4,
        hard_count=1
    )

    generator = ExamPaperGenerator(BranchBoundStrategy())

    paper = generator.generate(
        bank.get_all(),
        specification
    )

    assert len(paper) == 8
    assert sum(q.marks for q in paper) == 36
    assert PaperValidator.validate(
        paper,
        specification
    )