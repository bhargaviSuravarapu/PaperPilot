from time import perf_counter

from algorithms import dynamic_programming_select, greedy_select
from models import Question


def measure_algorithm(algorithm, questions, total_marks):
    start = perf_counter()

    result = algorithm(questions, total_marks)

    end = perf_counter()

    return result, end - start


def compare_algorithms(questions: list[Question], total_marks: int):
    greedy_result, greedy_time = measure_algorithm(
        greedy_select,
        questions,
        total_marks
    )

    dp_result, dp_time = measure_algorithm(
        dynamic_programming_select,
        questions,
        total_marks
    )

    print("\nPerformance Comparison")
    print("---------------------")
    print(f"Greedy: {greedy_time:.6f} seconds")
    print(f"Dynamic Programming: {dp_time:.6f} seconds")

    return greedy_result, dp_result