from frequency import word_frequency

def test_find_largest():
    assert word_frequency.count_frequencies([1, 5, 2, 8, 3]) == {1: 1, 2: 1, 3: 1, 5: 1, 8: 1}