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
