test_cases = 10


def find_highest(*args):
    max_num = args[0]
    for num in args:
        if max_num < num:
            max_num = num
    return max_num


for t in range(1, test_cases + 1):
    n = int(input())
    buildings = list(map(int, input().strip().split()))

    cnt = 0
    for i in range(2, n - 2):
        highest = find_highest(buildings[i - 2], buildings[i - 1], buildings[i + 1], buildings[i + 2])
        if buildings[i] > highest:
            cnt += buildings[i] - highest

    print(f'#{t} {cnt}')
