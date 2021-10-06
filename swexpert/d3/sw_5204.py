def mergesort(m):
    if len(m) == 1:
        return m

    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)


def merge(left, right):
    global left_first
    result = [0] * (len(left) + len(right))

    if left[-1] > right[-1]:
        left_first += 1

    lidx, ridx = 0, 0
    idx = 0
    while len(left) > lidx or len(right) > ridx:
        if len(left) > lidx and len(right) > ridx:
            if left[lidx] <= right[ridx]:
                result[idx] = left[lidx]
                lidx += 1
            else:
                result[idx] = right[ridx]
                ridx += 1
        elif lidx < len(left):
            result[idx] = left[lidx]
            lidx += 1
        elif ridx < len(right):
            result[idx] = right[ridx]
            ridx += 1
        idx += 1
    return result


test_cases = int(input().strip())
for t in range(1, test_cases + 1):
    N = int(input().strip())
    nums = list(map(int, input().strip().split()))
    left_first = 0
    result = mergesort(nums)
    print('#{} {} {}'.format(t, result[N // 2], left_first))
