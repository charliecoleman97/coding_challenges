"""
Problem: Given an array of integers, return indices of the two numbers such that they add up to a specific target. 
You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""

A1 = [-2, 1, 2, 4, 7, 11]
target1 = 13

# Approach 1 - Brute force do every two sum combination and then check if it's equal to the target
def two_sum_brute_force(A, target):
    for i in range(0, len(A)-1):
        for j in range(i+1, len(A)):
            if A[i] + A[j] == target:
                print(A[i], A[j])
                return True
    return False

print(two_sum_brute_force(A1, target1))

A2 = [2, 4, 6]
target2 = 10

def two_sum_hash_table(A, target):
    ht = dict()
    for i in range(len(A)):
        if A[i] in ht:
            print(ht[A[i]], A[i])
            return True
        else:
            ht[target - A[i]] = A[i]
    return False

print(two_sum_hash_table(A2, target2))

# Pincer move
# Can do this since the list is sorted
# If A[i] + A[j] is less than the target we move i up one 
# If A[i] + A[j] is greater than the target we move i down one
def two_sum(A, target):
    i = 0
    j = len(A) - 1
    while i < j:
        if A[i] + A[j] == target:
            print(A[i], A[j])
            return True
        elif A[i] + A[j] < target:
            i += 1
        else: #A[i] + A[j] > target
            j -= 1
    return True
            
print(two_sum(A1, target1))
