'''
Find and return the first capital letter in an inputted string 
'''
input_string1 = 'This String Has Capitals'
input_string2 = 'this string has capitals'


def has_upper_iterative(input_str):
    for i in range(len(input_str)):
        if input_str[i].isupper():
            return input_str[i]
    return "No uppercase letters in this string"

def has_upper_recursive(input_str, idx=0):
    if input_str[idx].isupper():
        return input_str[idx]
    if idx == len(input_str) - 1:
        return "No uppercase letters in this string"
    return has_upper_recursive(input_str, idx + 1)
        

# print(has_upper_iterative(input_string1))
# print(has_upper_iterative(input_string2))

print(has_upper_recursive(input_string1))
print(has_upper_recursive(input_string2))
