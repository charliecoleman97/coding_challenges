''''
1. Given a string composed of the characters A, C, G and T, count the frequencies of all three-letter substrings. 
Note that these substrings may intersect:

>>> string = “ACATCACA”
>>> frequencies(string)
>>> {
            “ACA”: 2,
            “CAT”: 1,
            “ATC”: 1,
            “CAC”: 1,
       }

'''

def count_three(input_str: str) -> dict:
    """Returns the frequency of all three-letter substrings as dict"""
    output_dict = {}
    for i in range(0, len(input_str)-2):
        substring = ''
        for j in range(3):
            substring += input_str[i+j]
        if substring in output_dict:
            output_dict[substring] += 1
        else:
            output_dict[substring] = 1
    return output_dict

test_string = 'ACATCACA'
print(test_string)


# print(count_three(test_string))



