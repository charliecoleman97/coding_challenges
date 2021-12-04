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



def test_outcome():
    fruit_list = ["apple", "pear", "lemon", "orange"]
    x = 2
    answer_list = ["apple", "pear"]
    assert answer_list == fruit_list_order(fruit_list, x)
    print("Test 1 passed")

# test if script works when x<n 


def test_outcome_reverse():
# test if script works when x > n 
    fruit_list = ["apple", "pear", "lemon", "orange"]
    x = 6
    answer_list = ["apple", "pear", "lemon", "orange", "lemon", "pear"]
    assert answer_list == fruit_list_order(fruit_list, x)
    print("Test 2 passed")

def fruit_list_order(fruit_list, x):
    new_list = []
    list_index = 0
    forwards = False
    for i in range(0, x):
        new_list.append(fruit_list[list_index])
        if i % len(fruit_list) == 1:
            forwards = not forwards 
        if forwards:
            list_index += 1
        else:
            list_index -= 1
        print(i, forwards, list_index)

    return output_list


    
test_list = ["apple", "pear", "lemon", "orange"]
fruit_list_order(test_list, 15)

test_outcome()
test_outcome_reverse()