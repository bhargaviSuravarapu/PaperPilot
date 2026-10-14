from generator import BranchBoundStrategy, ExamPaperGenerator
from models import PaperSpecification
from question_bank import QuestionBank
from validator import PaperValidator


def test_question_bank_generator_validator_integration():
    bank = QuestionBank("data/questions.json")

    questions = bank.get_all()

    specification = PaperSpecification(
        total_marks=36,
        easy_count=3,
        medium_count=4,
        hard_count=1
    )

    generator = ExamPaperGenerator(BranchBoundStrategy())

    paper = generator.generate(
        questions,
        specification
    )

    assert PaperValidator.validate(
        paper,
        specification
    )