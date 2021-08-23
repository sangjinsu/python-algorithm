def binary_search(a, key):
    left = 0
    right = len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == key:
            return mid
        else:
            if a[mid] < key:
                left = mid + 1
            elif a[mid] > key:
                right = mid - 1


print(binary_search([2, 4, 7, 9, 11, 19, 23], 23))
