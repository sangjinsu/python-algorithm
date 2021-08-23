import sys

n = int(sys.stdin.readline().strip())
packs = list(map(int, sys.stdin.readline().strip().split()))


dp = [0] + packs
packs = [0] + packs
for i in range(1, n + 1):
    for j in range(i):
        dp[i] = min(dp[i], dp[i - j] + packs[j])

sys.stdout.write(str(dp[-1]))
