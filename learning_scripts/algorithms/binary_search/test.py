data = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
target = 28

def binary_search(data, target):
    low = 0
    high = len(data)-1

    while low < high:
        mid = (low + high)//2 
        if target == data[mid]:
            return True
        elif target > data[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return False


print(binary_search(data, target))