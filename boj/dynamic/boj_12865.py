import sys

N, K = map(int, sys.stdin.readline().strip().split())
items = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
dp = [0] * (K + 1)

for i in range(N):
    for j in range(K, 0, -1):
        if items[i][0] <= j:
            dp[j] = max(dp[j], dp[j - items[i][0]] + items[i][1])

sys.stdout.write(str(dp[K]))
