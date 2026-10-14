from ai_assistance import ai_development_process


def test_ai_development_process():
    steps = ai_development_process()

    assert len(steps) == 7
    assert "AI-assisted code generation" in steps
    assert "Automated testing" in steps
    assert "Human code review" in steps