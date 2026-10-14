from functools import wraps
from time import perf_counter

from models import Question


def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()

        result = func(*args, **kwargs)

        end = perf_counter()

        print(
            f"{func.__name__} execution time: "
            f"{end - start:.6f} seconds"
        )

        return result

    return wrapper
@measure_time
def greedy_select(
    questions: list[Question],
    total_marks: int
) -> list[Question]:

    selected = []
    current_marks = 0

    # Select higher-mark questions first
    sorted_questions = sorted(
        questions,
        key=lambda q: q.marks,
        reverse=True
    )

    for question in sorted_questions:

        if current_marks + question.marks <= total_marks:
            selected.append(question)
            current_marks += question.marks

        if current_marks == total_marks:
            break

    return selected
@measure_time
def merge_sort(questions: list[Question]) -> list[Question]:
    if len(questions) <= 1:
        return questions

    mid = len(questions) // 2

    left = merge_sort(questions[:mid])
    right = merge_sort(questions[mid:])

    return merge(left, right)


def merge(
    left: list[Question],
    right: list[Question]
) -> list[Question]:

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i].marks <= right[j].marks:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

@measure_time
def dynamic_programming_select(
    questions: list[Question],
    total_marks: int
) -> list[Question]:

    dp: list[list[Question] | None] = [None] * (total_marks + 1)
    dp[0] = []

    for question in questions:
        for marks in range(total_marks, question.marks - 1, -1):

            previous = dp[marks - question.marks]

            if dp[marks] is None and previous is not None:
                dp[marks] = previous + [question]

    result = dp[total_marks]

    if result is None:
        return []

    return result


@measure_time
def backtracking_select(
    questions: list[Question],
    total_marks: int,
    required_count: int | None = None
) -> list[Question]:

    if required_count is None:
        required_count = len(questions)

    def backtrack(
        index: int,
        selected: list[Question],
        current_marks: int
    ) -> list[Question] | None:

        if len(selected) == required_count:
            return selected if current_marks == total_marks else None

        if current_marks >= total_marks:
            return None

        if index >= len(questions):
            return None

        # Choose the current question
        result = backtrack(
            index + 1,
            selected + [questions[index]],
            current_marks + questions[index].marks
        )

        if result is not None:
            return result

        # Skip the current question
        return backtrack(
            index + 1,
            selected,
            current_marks
        )

    return backtrack(0, [], 0) or []


@measure_time
def branch_and_bound_select(
    questions: list[Question],
    total_marks: int
) -> list[Question]:

    best_solution = []
    best_count = float("inf")

    def search(
        index: int,
        selected: list[Question],
        current_marks: int
    ):
        nonlocal best_solution, best_count

        # Exact solution found
        if current_marks == total_marks:
            if len(selected) < best_count:
                best_solution = selected.copy()
                best_count = len(selected)
            return

        # Invalid branch
        if current_marks > total_marks:
            return

        # No more questions
        if index >= len(questions):
            return

        # Bound:
        # If we already use as many or more questions
        # than our best solution, stop exploring.
        if len(selected) >= best_count:
            return

        # Branch 1: include question
        search(
            index + 1,
            selected + [questions[index]],
            current_marks + questions[index].marks
        )

        # Branch 2: exclude question
        search(
            index + 1,
            selected,
            current_marks
        )

    search(0, [], 0)

    return best_solution

from functools import reduce


def filter_by_difficulty(
    questions: list[Question],
    difficulty: str
) -> list[Question]:
    """Pure function to filter questions."""
    return list(
        filter(
            lambda q: q.difficulty.lower() == difficulty.lower(),
            questions
        )
    )


def calculate_total_marks(
    questions: list[Question]
) -> int:
    """Pure function to calculate total marks."""
    return reduce(
        lambda total, q: total + q.marks,
        questions,
        0
    )


def get_question_summary(questions: list[Question]) -> list[str]:
    """Create summaries using map."""
    return [
        f"{q.topic} - {q.marks} marks"
        for q in questions
    ]