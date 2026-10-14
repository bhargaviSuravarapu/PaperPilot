from hypothesis import given
from hypothesis import strategies as st

from models import Question
from validator import PaperValidator


@given(
    marks=st.integers(min_value=1, max_value=100)
)
def test_total_marks_property(marks):
    question = Question(
        1,
        "Test Question",
        1,
        "easy",
        marks,
        "Python"
    )

    assert PaperValidator.validate_total_marks(
        [question],
        marks
    )