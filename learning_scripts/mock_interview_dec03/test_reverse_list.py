from reverse_list import reverse_list

''''Given a list of n elements and an integer x, 
output x elements from the list in order. If x > n, reverse back through the list.'''

'''' 
>>> take(["apple", "pear", "lemon", "orange"], 2)
>>> ["apple", "pear"]
'''

''''
>>> take(["apple", "pear", "lemon", "orange"], 6)
>>>["apple", "pear", "lemon", "orange", "lemon", "pear"]
'''

def test_for_empty_list_zero_int():
    '''Tests for empty list and x = 0'''
    empty_list = []
    x = 0
    assert reverse_list(empty_list, x) == []


def test_filled_list_zero_int():
    '''Test for when list is filled but x = 0'''
    filled_list = ["apple", "pear", "lemon", "orange"]
    x = 0
    assert reverse_list(filled_list, 0) == []


def test_list_length_equals_or_greater_than_x():
    ''' Test that function returns correct list without reversing'''
    filled_list = ["apple", "pear", "lemon", "orange"]
    x = 4
    assert reverse_list(filled_list, x) == filled_list


def test_list_length_less_than_x():
    ''' Test that list can reverse when x is greater than length of list'''
    filled_list = ["apple", "pear", "lemon", "orange"]
    x = 6
    expected_list = ["apple", "pear", "lemon", "orange", "lemon", "pear"]
    assert reverse_list(filled_list, x) == expected_list
