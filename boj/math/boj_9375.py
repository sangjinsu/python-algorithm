test_case = int(input())
for t in range(test_case):
    N = int(input())
    clothes = dict()
    for i in range(N):
        _, wear_type = input().split()
        clothes.setdefault(wear_type, 0)
        clothes[wear_type] += 1

    result = 1
    for item in clothes.values():
        result *= item + 1
    result -= 1

    print(result)
