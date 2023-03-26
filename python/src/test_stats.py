from .stats import calculate_iqr, find_outliers, quartiles


def test_quartiles():
    data = [3, 7, 8, 5, 12, 14, 21, 15, 18, 14]
    expected_quartiles = {"q1": 7, "q2": 13, "q3": 15}
    assert quartiles(data) == expected_quartiles

    # Test with even number of data points
    data = [2, 4, 6, 8, 10, 12]
    assert quartiles(data) == {"q1": 4, "q2": 7, "q3": 10}

    # Test with odd number of data points
    data = [
        2,
        2,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        4,
        4,
        4,
        4,
        4,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        6,
        6,
        6,
        6,
        31,
        34,
    ]
    assert len(data) % 2 != 0
    assert quartiles(data) == {"q1": 3, "q2": 5, "q3": 5}

    # Test with repeated data points
    data = [5, 5, 5, 5, 5, 5, 5, 5, 5]
    assert quartiles(data) == {"q1": 5, "q2": 5, "q3": 5}

    # Test with negative data points
    data = [
        3,
        -18,
        16,
        16,
        5,
        -19,
        0,
        -20,
        -2,
        -4,
        2,
        7,
        -3,
        11,
        17,
        16,
        -4,
        6,
        18,
        -20,
    ]
    assert quartiles(data) == {"q1": -4, "q2": 2.5, "q3": 13.5}

    # Test with decimals
    data = [2.5, 4.1, 1.2, 3.7, 6.8, 9.9]
    assert quartiles(data) == {"q1": 2.5, "q2": 3.9, "q3": 6.8}

    data = [
        1,
        1,
        1,
        1,
        2,
        2,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        5,
        5,
        5,
        5,
        7,
        8,
        9,
        3,
        4,
        5,
        5,
    ]
    assert quartiles(data) == {"q1": 3, "q2": 4, "q3": 5}


def test_iqr():
    data = [2.5, 4.1, 1.2, 3.7, 6.8, 9.9]
    assert calculate_iqr(data) == (6.8 - 2.5)


def test_find_outliers():
    data = [2.5, 4.1, 1.2, 3.7, 6.8, 9.9, 15, 200]
    assert find_outliers(data) == [200]
