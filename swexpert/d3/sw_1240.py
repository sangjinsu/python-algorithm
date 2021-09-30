test_cases = int(input().strip())

secrets = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}

for t in range(1, test_cases + 1):
    N, M = map(int, input().strip().split())

    code = ''
    for i in range(N):
        line = input().strip()
        if not code and '1' in line:
            code = line

    end_idx = 0
    for i in range(M - 1, -1, -1):
        if code[i] == '1':
            end_idx = i
            break

    nums = [0] * 8
    idx = 7
    for i in range(end_idx, -1, -7):
        nums[idx] = secrets[code[i - 6: i + 1]]
        idx -= 1
        if idx < 0:
            break

    check = (nums[0] + nums[2] + nums[4] + nums[6]) * 3 + (nums[1] + nums[3] + nums[5]) + nums[7]

    result = 0
    if check % 10 == 0:
        result = sum(nums)

    print('#{} {}'.format(t, result))
