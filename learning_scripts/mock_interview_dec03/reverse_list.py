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

def reverse_list(n_list: list, x: int)->list:
    output_list = []
    count = 0
    index = 0
    forwards = True
    while count < x:
        output_list.append(n_list[index])
        if index == len(n_list)-1:
            forwards = False
        elif index == 0:
            forwards = True 
        if forwards:
            index += 1
        else:
            index -= 1
        count += 1
    return output_list
    



print(reverse_list(["apple", "pear", "lemon", "orange"], 9))
