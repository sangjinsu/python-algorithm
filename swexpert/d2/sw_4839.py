# 이진탐색

test_cases = int(input())


# def binary_search(item, start, end, cnt):
#     if start > end:
#         return -1
#     middle = (start + end) // 2
#     cnt += 1
#     if middle == item:
#         return cnt
#     else:
#         if middle < item:
#             return binary_search(item, middle, end, cnt + 1)
#         else:
#             return binary_search(item, start, middle, cnt + 1)


def binary_search(item, page):
    start, end = 1, page
    cnt = 0
    while start <= end:
        cnt += 1
        middle = (start + end) // 2
        if middle == item:
            return cnt
        else:
            if middle < item:
                start = middle
            else:
                end = middle
    return -1


for t in range(1, test_cases + 1):
    p, pa, pb = map(int, input().strip().split())

    a = binary_search(pa, p)
    b = binary_search(pb, p)

    # a = binary_search(pa, 1, p, 0)
    # b = binary_search(pb, 1, p, 0)

    result = 0
    if b == -1 or a < b:
        result = 'A'
    elif a == -1 or a > b:
        result = 'B'

    print('#{} {}'.format(t, result))
