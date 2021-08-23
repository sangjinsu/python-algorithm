test_cases = int(input())


def div(n: str):
    return (int(n) - 1) // 2


def max_num(nums: [int]):
    m = 0
    for num in nums:
        if m < num:
            m = num
    return m


for t in range(1, test_cases + 1):
    n = int(input())
    students = [list(map(div, input().strip().split())) for _ in range(n)]

    rooms = [0] * 200

    for s in students:
        if s[0] > s[1]:
            s[0], s[1] = s[1], s[0]
        for i in range(s[0], s[1] + 1):
            rooms[i] += 1

    print('#{} {}'.format(t, max_num(rooms)))
