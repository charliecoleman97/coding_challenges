input_string1 = 'this String Has Capitals'
input_string2 = 'this string has capitals'

data = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
target = 28


def first_upper_iterative(input_string):
    for i in range(len(input_string)):
        if input_string[i].isupper():
            return input_string[i]
    return "No capital in this string"

def first_upper_recursive(input_string, idx=0):
    if input_string[idx].isupper():
        return input_string[idx]
    if idx == len(input_string) - 1:
        return "No capital in this string"
    return first_upper_recursive(input_string, idx + 1)

def binary_search_iterative(data, target):
    low = 0
    high = len(data)-1
    for i in range(len(data)):
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target > data[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return False 

def binary_search_recursive(data, target, low=0, high=len(data)-1):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target > data[mid]:
            return binary_search_recursive(data, target, mid+1, high)
        else:
            return binary_search_recursive(data, target, low, mid-1)

def calculate_string_length_iterative(input_string):
    count = 0
    for i in range(len(input_string)):
        count += 1
    return count

def calculate_string_length_recursive(input_string):
    if input_string == "":
        return 0
    return 1 + calculate_string_length_recursive(input_string[1:])










print(binary_search_recursive(data, target))
print(first_upper_recursive(input_string2))
print(calculate_string_length_iterative(input_string1))