a1 = [1, 4, 9]
a2 = [9, 9, 9]

def increment(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] +=1
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A

# print(increment(a2))

A1 = [-2, 1, 2, 4, 7, 11]
target1 = 13

def two_sum(A, target):
    i = 0
    j = len(A)-1
    while i < j:
        if A[i] + A[j] == target:
            return (A[i], A[j])
        if A[i] + A[j] < target:
            i += 1
        else:
            j -= 1
    
# print(two_sum(A1, target1))

def stock(A):
    max_price = 0
    min_price = A[0]
    for price in A:
        min_price = min(min_price, price)
        compare_price = price - min_price
        max_price = max(max_price, compare_price)
    return max_price


A2 = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
print(stock(A2))

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
# print(array_advance(A2))
# print(array_advance(A2))