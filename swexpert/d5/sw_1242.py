# 1일차 - 암호코드 스캔


def hexa_to_bin(hexa):
    binary = ''
    for h in hexa:
        binary += str(bin(int(h, 16)))[2:].zfill(4)
    return binary


hashed = {
    (3, 2, 1, 1): 0,
    (2, 2, 2, 1): 1,
    (2, 1, 2, 2): 2,
    (1, 4, 1, 1): 3,
    (1, 1, 3, 2): 4,
    (1, 2, 3, 1): 5,
    (1, 1, 1, 4): 6,
    (1, 3, 1, 2): 7,
    (1, 2, 1, 3): 8,
    (3, 1, 1, 2): 9,
}

test_cases = int(input().strip())
for t in range(1, test_cases + 1):
    N, M = map(int, input().strip().split())

    lines = [input().strip() for _ in range(N)]
    lines = list(set(lines))

    nums = []
    for line in lines:
        code = hexa_to_bin(line).rstrip('0')

        i = len(code) - 1
        num = []
        while i >= 0:
            if code[i] == '0':
                i -= 1
            else:
                a, b, c, d = 0, 0, 0, 0
                while code[i] == '1':
                    d += 1
                    i -= 1
                while code[i] == '0':
                    c += 1
                    i -= 1
                while code[i] == '1':
                    b += 1
                    i -= 1
                k = min(b, c, d)
                a = k * 7 - (b + c + d)
                i -= a

                num.insert(0, hashed[(a // k, b // k, c // k, d // k)])
                if len(num) == 8:
                    if num not in nums:
                        nums.append(num)
                    num = []

    result = 0
    for num in nums:
        check = (num[0] + num[2] + num[4] + num[6]) * 3 + (num[1] + num[3] + num[5]) + num[7]
        if check % 10 == 0:
            result += sum(num)

    print('#{} {}'.format(t, result))
