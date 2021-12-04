_input = ["apple", "pear", "lemon", "orange"]
 
def fruit_list_order(input_array, n):
   forward = True
   count = 0
   index = 0
   output_array = []
   while count < n:
       output_array.append(input_array[index])
       if len(input_array) - 1 == index:
           forward = False
       elif index == 0:
           forward = True
       if forward:
           index += 1
       else:
           index -= 1
       count += 1
   return output_array
 
 
print(fruit_list_order(_input, 28))

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

test_list = ["apple", "pear", "lemon", "orange"]
fruit_list_order(test_list, 15)


test_outcome()
test_outcome_reverse()