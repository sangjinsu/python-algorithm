test_cases = int(input())

for t in range(1, test_cases + 1):
    n = int(input())
    prices = list(map(int, input().strip().split()))

    result = 0
    last_price = prices[-1]
    for i in range(len(prices) - 1, -1, -1):
        if last_price > prices[i]:
            result += last_price - prices[i]
        else:
            last_price = prices[i]

    print('#{} {}'.format(t, result))
