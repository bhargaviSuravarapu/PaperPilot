import json

from models import Question


class QuestionBank:

    def __init__(self, filename: str):
        self.filename = filename
        self.questions = self._load_questions()

    def _load_questions(self):
        with open(self.filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        return [Question(**item) for item in data]

    def get_all(self):
        return self.questions

    def get_by_unit(self, unit: int):
        return [q for q in self.questions if q.unit == unit]

    def get_by_difficulty(self, difficulty: str):
        return [
            q for q in self.questions
            if q.difficulty.lower() == difficulty.lower()
        ]

    def iter_questions(self):
        """Generator for questions."""
        yield from self.questions

    def iter_by_unit(self, unit: int):
        """Generator for questions from a specific unit."""
        for question in self.questions:
            if question.unit == unit:
                yield question