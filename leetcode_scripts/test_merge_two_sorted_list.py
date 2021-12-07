from merge_two_sorted_list import merge_two_lists

def test_two_equal_length_lists():
    list1 = [1,2,4]
    list2 = [1,3,4]
    assert merge_two_lists(list1, list2) == [1, 1, 2, 3, 4, 4]

def test_two_empty_lists():
    list1 = []
    list2 = []
    assert merge_two_lists(list1, list2) == []

def test_one_empty_list():
    list1 = []
    list2 = [0]
    assert merge_two_lists(list1, list2) == [0]

def test_negative_values():
    list1 = [-73, 12, 44, -51]
    list2 = [42, 13, -13, -24, 5]
    assert merge_two_lists(list1, list2) == [-73, -51, -24, -13, 5, 12, 13, 42, 44]
