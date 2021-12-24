string1 = "This string has vowels in it"
string2 = "BCDFGHJKLMNPQRSTVWXYZ"

vowels = "aeiou"

def count_consonants_iterative(input_string):
    count = 0
    for i in range(len(input_string)):
        if input_string[i].lower() not in vowels and input_string[i].isalpha():
            count += 1
    return count

def count_consonants_recursive(input_string):
    if input_string == "":
        return 0
    if input_string[0].lower() not in vowels and input_string[0].isalpha():
        return 1 + count_consonants_recursive(input_string[1:])
    else:
        return count_consonants_recursive(input_string[1:])

print(count_consonants_recursive(string1))