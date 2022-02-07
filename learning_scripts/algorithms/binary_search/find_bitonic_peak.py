"""
Define a bitonic sequence as a sequence of integers such that:
x_1 <= ... <= x_k >= ... >= x_n-1 for some k, 0 <= k < n.

For example:
    1, 2, 3, 4, 5, 4, 3, 2, 1

is a bitonic sequence so a bitonic peak is the largest element in 
sequence so for this example the peak is 5
"""

# Peak element is 5
A = [1, 2, 3, 4, 5, 4, 3, 2, 1]

# Peak element is 4
B = [1, 2, 3, 4, 1]

# Peak element is 6
C = [1, 6, 5, 4, 3, 2, 1]

def find_highest_number(A):
    pass