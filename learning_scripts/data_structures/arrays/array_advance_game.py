'''
Given an array of non-negative integers. For example:
            [3, 3, 1, 0, 2, 0, 1]
Each number represenets the maximum you can advance in the array
Question:
Is it possible to advance from the start of the array to the last element?
[3, 3, 1, 0, 2, 0, 1]<-- Success
[3, 2, 0, 0, 2, 0, 1]<-- Failure

Approach 1 - Greedy
Advance as much as possible for each number 
[2, 4, 1, 1, 0, 2, 3]<-- This approach wouldn't work here but it is solvable 

Approach 2 
Iterate through each entry in the array
Track the furthest we can reach from entry (A[i] + i)
Furthest possible to advance from "i": A[i] + i
'''

def array_advance(A):
    furthest_reached = 0
    last_idx = len(A) - 1
    i = 0
    while i <= furthest_reached and furthest_reached < last_idx:
        furthest_reached = max(furthest_reached, A[i] + i)
        i += 1
    return furthest_reached >= last_idx

A1 = [3, 3, 1, 0, 2, 0, 1]
A2 = [3, 2, 0, 0, 2, 0, 1]
print(array_advance(A1))
print(array_advance(A2))




