from complexity import algorithm_complexities


def test_algorithm_complexities():
    complexities = algorithm_complexities()

    assert "Merge Sort" in complexities
    assert "Dynamic Programming" in complexities
    assert "Backtracking" in complexities
    assert "Branch and Bound" in complexities

    for details in complexities.values():
        assert "Time" in details
        assert "Space" in details
        assert "Amortized" in details
        assert "Expected" in details