from largest import largest_element

def test_find_largest():
    assert largest_element.find_largest([1, 5, 2, 8, 3]) == 8
    assert largest_element.find_largest([]) is None
    assert largest_element.find_largest([-1, -5, -2, -8, -3]) == -1