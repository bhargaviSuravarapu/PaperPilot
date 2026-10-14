from generator import BranchBoundStrategy, ExamPaperGenerator
from models import PaperSpecification
from question_bank import QuestionBank
from validator import PaperValidator


def main():
    bank = QuestionBank("data/questions.json")
    questions = bank.get_all()

    specification = PaperSpecification(
        total_marks=36,
        easy_count=3,
        medium_count=4,
        hard_count=1
    )

    strategy = BranchBoundStrategy()
    generator = ExamPaperGenerator(strategy)

    paper = generator.generate(
        questions,
        specification
    )

    is_valid = PaperValidator.validate(
        paper,
        specification
    )

    easy = sum(q.difficulty == "easy" for q in paper)
    medium = sum(q.difficulty == "medium" for q in paper)
    hard = sum(q.difficulty == "hard" for q in paper)

    total = sum(q.marks for q in paper)

    print("\n========================================")
    print("       SMART EXAM QUESTION PAPER")
    print("========================================")

    print("Algorithm       : Branch & Bound")
    print("Required Marks  :", specification.total_marks)
    print("Generated Marks :", total)

    print("\nDifficulty Distribution")
    print("-----------------------")
    print("Easy   :", easy)
    print("Medium :", medium)
    print("Hard   :", hard)

    print("\nQuestions")
    print("----------------------------------------")

    for number, question in enumerate(paper, start=1):
        print(
            f"{number}. {question.question}"
            f" [{question.marks} Marks]"
        )

    print("----------------------------------------")

    if is_valid:
        print("Paper Status    : VALID")
    else:
        print("Paper Status    : INVALID")

    print("========================================")


if __name__ == "__main__":
    main()