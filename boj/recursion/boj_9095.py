test_cases = int(input().strip())


def recursion(value):
    global result
    if value > n:
        return
    if value == n:
        result += 1
        return
    for i in [1, 2, 3]:
        recursion(value + i)


for t in range(1, test_cases + 1):
    n = int(input().strip())
    result = 0
    recursion(0)
    print(result)
