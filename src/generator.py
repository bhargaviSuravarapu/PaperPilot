from abc import ABC, abstractmethod

from algorithms import (
    backtracking_select,
    branch_and_bound_select,
    dynamic_programming_select,
    greedy_select,
)
from models import PaperSpecification, Question


class SelectionStrategy(ABC):

    @abstractmethod
    def select(
        self,
        questions: list[Question],
        total_marks: int
    ) -> list[Question]:
        pass


class GreedyStrategy(SelectionStrategy):

    def select(self, questions, total_marks):
        return greedy_select(questions, total_marks)


class DPStrategy(SelectionStrategy):

    def select(self, questions, total_marks):
        return dynamic_programming_select(questions, total_marks)



class BacktrackingStrategy(SelectionStrategy):

    def select(
        self,
        questions,
        total_marks,
        required_count=None
    ):
        return backtracking_select(
            questions,
            total_marks,
            required_count
        )


class BranchBoundStrategy(SelectionStrategy):

    def select(self, questions, total_marks):
        return branch_and_bound_select(questions, total_marks)


class ExamPaperGenerator:

    def __init__(self, strategy: SelectionStrategy):
        self.strategy = strategy

    def generate(
        self,
        questions: list[Question],
        specification: PaperSpecification
    ) -> list[Question]:

        easy = [
            q for q in questions
            if q.difficulty.lower() == "easy"
        ]

        medium = [
            q for q in questions
            if q.difficulty.lower() == "medium"
        ]

        hard = [
            q for q in questions
            if q.difficulty.lower() == "hard"
        ]

        selected = []

        
        selected.extend(
            self.strategy.select(
                easy,
                specification.easy_count * 2
            )[:specification.easy_count]
        )

        selected.extend(
            self.strategy.select(
                medium,
                specification.medium_count * 5
            )[:specification.medium_count]
        )

        selected.extend(
            self.strategy.select(
                hard,
                specification.hard_count * 10
            )[:specification.hard_count]
        )

        return selected
