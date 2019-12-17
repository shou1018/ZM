def binary_search(A, item):
    n = len(A)
    if n == 0:
        return False
    else:
        middle = n//2
        if A[middle] == item:
            return True
        if A[middle] > item:
            return binary_search(A[:middle], item)
        else:
            return binary_search(A[middle+1:], item)


numbers = [1,2,3,5,8,22,34,42,87,103]
print(binary_search(numbers, 42))
