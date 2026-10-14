from models import PaperSpecification, Question


class PaperValidator:

    @staticmethod
    def validate_total_marks(
        questions: list[Question],
        expected_marks: int
    ) -> bool:

        total = sum(q.marks for q in questions)
        return total == expected_marks

    @staticmethod
    def has_duplicates(
        questions: list[Question]
    ) -> bool:

        ids = [q.id for q in questions]

        return len(ids) != len(set(ids))

    @staticmethod
    def validate_difficulty(
        questions: list[Question],
        specification: PaperSpecification
    ) -> bool:

        easy = sum(
            q.difficulty.lower() == "easy"
            for q in questions
        )

        medium = sum(
            q.difficulty.lower() == "medium"
            for q in questions
        )

        hard = sum(
            q.difficulty.lower() == "hard"
            for q in questions
        )

        return (
            easy == specification.easy_count
            and medium == specification.medium_count
            and hard == specification.hard_count
        )

    @staticmethod
    def validate(
        questions: list[Question],
        specification: PaperSpecification
    ) -> bool:

        if not PaperValidator.validate_total_marks(
            questions,
            specification.total_marks
        ):
            return False

        if PaperValidator.has_duplicates(questions):
            return False

        return PaperValidator.validate_difficulty(
            questions,
            specification
        )