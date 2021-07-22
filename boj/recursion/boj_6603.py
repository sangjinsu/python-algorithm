import sys


def lotto(nums, cnt, index, k, result):
    cnt += 1
    if cnt == 7:
        sys.stdout.write(result + '\n')
    else:
        result += nums[index] + ' '
        if cnt < 6:
            for i in range(index + 1, int(k) - (6 - cnt) + 1):
                lotto(nums, cnt, i, k, result)
        else:
            lotto(nums, cnt, 0, k, result)


while True:
    test_case = sys.stdin.readline().strip()
    if test_case == '0':
        break
    k, *s = test_case.split(' ')

    answer = ''
    for i in range(int(k) - 5):
        lotto(s, 0, i, k, answer)
    sys.stdout.write('\n')
