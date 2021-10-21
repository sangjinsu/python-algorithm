from pprint import pprint

test_cases = int(input().strip())

for t in range(1, test_cases + 1):
    A, B = input().strip().split()
    A = 'X' + A
    B = 'X' + B
    dp = [[0] * len(A) for _ in range(len(B))]

    for i in range(1, len(A)):
        for j in range(1, len(B)):
            if A[i] == B[j]:
                dp[j][i] = dp[j - 1][i - 1] + 1
            else:
                dp[j][i] = max(dp[j - 1][i], dp[j][i - 1])
    print('#{} {}'.format(t, dp[len(B) - 1][len(A) - 1]))
    pprint(dp)
"""
    '' a  c  a  y  k  p
''[[0, 0, 0, 0, 0, 0, 0],
c  [0, 0, 1, 1, 1, 1, 1],
a  [0, 1, 1, 2, 2, 2, 2],
p  [0, 1, 1, 2, 2, 2, 3],
c  [0, 1, 2, 2, 2, 2, 3],
a  [0, 1, 2, 3, 3, 3, 3],
k  [0, 1, 2, 3, 3, 4, 4]]
a    ''
cap  capa
"""
