from question_bank import QuestionBank


def test_question_bank_loads_questions():
    bank = QuestionBank("data/questions.json")

    questions = bank.get_all()

    assert len(questions) == 24


def test_get_by_difficulty():
    bank = QuestionBank("data/questions.json")

    hard_questions = bank.get_by_difficulty("hard")

    assert len(hard_questions) > 0
    assert all(q.difficulty == "hard" for q in hard_questions)

def test_question_generator():
    bank = QuestionBank("data/questions.json")

    questions = list(bank.iter_questions())

    assert len(questions) == 24


def test_unit_generator():
    bank = QuestionBank("data/questions.json")

    questions = list(bank.iter_by_unit(1))

    assert len(questions) > 0
    assert all(q.unit == 1 for q in questions)