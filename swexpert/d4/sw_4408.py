test_cases = int(input())


def max_num(nums):
    m = 0
    for n in nums:
        if m < n:
            m = n
    return m


for t in range(1, test_cases + 1):
    n = int(input())
    students = [list(map(int, input().strip().split())) for _ in range(n)]

    rooms = [0] * 200

    for s in students:
        if s[0] > s[1]:
            s[0], s[1] = s[1], s[0]
        if s[0] % 2 == 0:
            s[0] -= 1
        if s[1] % 2 == 0:
            s[1] -= 1

        for i in range(s[0] // 2, s[1] // 2 + 1):
            rooms[i] += 1

    print('#{} {}'.format(t, max_num(rooms)))
