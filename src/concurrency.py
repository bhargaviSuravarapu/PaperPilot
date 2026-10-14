from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool

from question_bank import Question


def process_question(question: Question) -> str:
    return f"{question.topic}: {question.marks} marks"


def process_questions(questions: list[Question]) -> list[str]:
    with ThreadPoolExecutor(max_workers=4) as executor:
        results = executor.map(process_question, questions)

    return list(results)


def process_question_cpu(question: Question) -> str:
    return f"Processed: {question.question}"


def process_questions_multiprocessing(
    questions: list[Question]
) -> list[str]:
    with Pool(processes=2) as pool:
        results = pool.map(
            process_question_cpu,
            questions
        )

    return results

# Concurrency notes:
#
# Threading is useful for I/O-bound tasks such as reading files
# or waiting for external services.
#
# Multiprocessing is useful for CPU-bound tasks because it can
# use multiple processes and avoids the limitation of the GIL.
#
# The exam paper generator mainly performs lightweight operations,
# so concurrency is demonstrated for educational purposes.