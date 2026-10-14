from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Question:
    id: int
    question: str
    unit: int
    difficulty: str
    marks: int
    topic: str


class QuestionType(ABC):

    @abstractmethod
    def display(self, question: Question) -> str:
        pass


class MCQQuestion(QuestionType):

    def display(self, question: Question) -> str:
        return f"[MCQ] {question.question}"


class DescriptiveQuestion(QuestionType):

    def display(self, question: Question) -> str:
        return f"[Descriptive] {question.question}"

@dataclass
class PaperSpecification:
    total_marks: int
    easy_count: int
    medium_count: int
    hard_count: int

class PaperFormatter:

    def format_question(self, question: Question) -> str:
        return f"{question.question} [{question.marks} Marks]"


class PaperPrinter:

    def __init__(self, formatter: PaperFormatter):
        self.formatter = formatter

    def format_paper(self, questions: list[Question]) -> list[str]:
        return [
            self.formatter.format_question(question)
            for question in questions
        ]
from typing import Generic, TypeVar

T = TypeVar("T")


class ResultContainer(Generic[T]):

    def __init__(self, items: list[T]):
        self.items = items

    def get_items(self) -> list[T]:
        return self.items