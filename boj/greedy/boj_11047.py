N, K = map(int, input().strip().split())

coins = []
for i in range(N):
    coins.append(int(input().strip()))

cnt = 0
for i in range(N - 1, -1, -1):
    cnt += K // coins[i]
    K %= coins[i]

print(cnt)
