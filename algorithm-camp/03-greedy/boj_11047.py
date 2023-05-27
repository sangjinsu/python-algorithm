import sys

if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().strip().split())
    coins = [int(sys.stdin.readline().strip()) for _ in range(N)]
    coins = reversed(coins)

    result = 0
    for coin in coins:
        if coin <= K:
            cnt = K // coin
            K %= coin
            result += cnt
        if K == 0:
            break

    sys.stdout.write(str(result))
