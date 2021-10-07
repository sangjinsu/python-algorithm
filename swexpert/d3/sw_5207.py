# 이진 탐색
def binary_search(arr, key):
    left, right = 0, len(arr) - 1

    visited = ''
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return 1
        elif arr[mid] > key:
            right = mid - 1
            if visited == 'L':
                return 0
            visited = 'L'
        elif arr[mid] < key:
            left = mid + 1
            if visited == 'R':
                return 0
            visited = 'R'
    return 0


test_cases = int(input().strip())
for t in range(1, test_cases + 1):
    N, M = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))
    B = list(map(int, input().strip().split()))
    A.sort()

    cnt = 0
    for b in B:
        cnt += binary_search(A, b)
    print('#{} {}'.format(t, cnt))
