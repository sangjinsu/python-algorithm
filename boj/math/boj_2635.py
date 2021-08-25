import sys

n = int(sys.stdin.readline().strip())

max_nums = []
max_cnt = 0
for second in range(n // 2, n + 1):
    nums = []
    cnt = 0
    first = n
    while first >= 0:
        nums.append(first)
        first, second = second, first - second
        cnt += 1

    if max_cnt < cnt:
        max_cnt = cnt
        max_nums = nums

sys.stdout.write(str(max_cnt) + '\n')
sys.stdout.write(' '.join(map(str, max_nums)))
