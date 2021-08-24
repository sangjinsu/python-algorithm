test_cases = int(input())


def n_qeens(k):
    if k == n:
        return 1
    cnt = 0
    for i in range(n):
        ko = 1
        for j in range(k):
            if rows[j] == i or k - j == abs(i - rows[j]):
                ko = 0
                break
        if ko:
            rows[k] = i
            cnt += n_qeens(k + 1)
    return cnt


# def n_qeens(k):
#     global cnt
#     if k == n:
#         cnt += 1
#     for i in range(n):
#         ko = 1
#         for j in range(k):
#             if rows[j] == i or k - j == abs(i - rows[j]):
#                 ko = 0
#                 break
#         if ko:
#             rows[k] = i
#             n_qeens(k + 1)


for t in range(1, test_cases + 1):
    n = int(input())
    rows = [0] * n
    result = n_qeens(0)
    print('#{} {}'.format(t, result))
