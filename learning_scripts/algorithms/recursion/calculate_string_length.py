string = "This string is not that long"

def string_length_interative(input_string):
    count = 0
    for i in range(len(input_string)):
        count +=1
    return count

def string_length_recursive(input_string):
    if input_string == "":
        return 0
    return 1 + string_length_recursive(input_string[1:])

print(string_length_interative(string))