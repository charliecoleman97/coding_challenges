from min_cost_to_move_chips import minCostToMoveChips

def test_small_list_small_numbers():
    ''' Test to see if script works with a small script with small numbers'''
    small_list = [1,1,2,3]
    assert minCostToMoveChips(small_list) == 1

def test_large_list_repeated_numbers():
    ''' Test to see if large list with repeated numbers work as well'''
    repeated_list = [1, 1, 2, 2, 2, 2, 3, 3]
    assert minCostToMoveChips(repeated_list) == 4

def test_no_repeats():
    ''' Test to see if no repeated numbers work'''
    no_repeat_list = [1, 2, 3, 4, 5]
    assert minCostToMoveChips(no_repeat_list) == 2

def test_huge_list():
    '''Test to see if it works with a huge list'''
    huge_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,
    16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    assert minCostToMoveChips(huge_list) == 15

