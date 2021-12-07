'''
Doesn't really need a test as it's really simple but might fancied doing one anyway
'''

from is_palindrome import is_palindrome

def test_detects_palindrome():
    x = 1234321
    assert is_palindrome(x) == True 

def test_detects_non_palindrome():
    x = 12 
    assert is_palindrome(x) == False

def test_works_with_negatives():
    x = -252
    assert is_palindrome(x) == False