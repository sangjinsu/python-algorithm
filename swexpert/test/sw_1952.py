test_cases = int(input())


def recursion(n, price):
    global min_price
    if n >= 12:
        min_price = min(min_price, price)
        return
    if plan[n] == 0:
        recursion(n + 1, price)
    else:
        recursion(n + 1, min(price + prices[0] * plan[n], price + prices[1]))
        recursion(n + 3, price + prices[2])


for t in range(1, test_cases + 1):
    prices = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    min_price = 999999
    recursion(0, 0)
    min_price = min(min_price, prices[3])
    print('#{} {}'.format(t, min_price))
