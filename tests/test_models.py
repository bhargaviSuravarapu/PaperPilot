from models import (
    DescriptiveQuestion,
    MCQQuestion,
    PaperFormatter,
    PaperPrinter,
    Question,
    ResultContainer,
)


def sample_question():
    return Question(
        id=1,
        question="Test question",
        unit=1,
        difficulty="easy",
        marks=2,
        topic="Python",
    )


def test_mcq_question():
    question = sample_question()
    result = MCQQuestion().display(question)
    assert "[MCQ]" in result


def test_descriptive_question():
    question = sample_question()
    result = DescriptiveQuestion().display(question)
    assert "[Descriptive]" in result


def test_paper_formatter():
    question = sample_question()
    formatter = PaperFormatter()
    assert "2 Marks" in formatter.format_question(question)


def test_paper_printer():
    question = sample_question()
    printer = PaperPrinter(PaperFormatter())
    result = printer.format_paper([question])
    assert len(result) == 1


def test_result_container():
    question = sample_question()
    container = ResultContainer([question])
    assert container.get_items() == [question]