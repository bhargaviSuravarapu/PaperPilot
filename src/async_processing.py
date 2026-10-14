import asyncio

from models import Question


async def process_question_async(question: Question) -> str:
    await asyncio.sleep(0)
    return f"{question.topic}: {question.marks} marks"


async def process_questions_async(
    questions: list[Question]
) -> list[str]:

    tasks = [
        process_question_async(question)
        for question in questions
    ]

    return await asyncio.gather(*tasks)


def run_async_processing(
    questions: list[Question]
) -> list[str]:
    return asyncio.run(
        process_questions_async(questions)
    )