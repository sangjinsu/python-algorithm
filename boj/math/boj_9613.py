import sys
from itertools import combinations


def gcd(n, m):
    while n != 0:
        m, n = n, m % n
    return m


n = int(sys.stdin.readline().strip())
for i in range(n):
    nums = list(map(int, sys.stdin.readline().strip().split()))
    couples = list(combinations(nums[1:], r=2))
    total = 0
    for couple in couples:
        v = gcd(couple[1], couple[0])
        total += v

    sys.stdout.write(str(total) + '\n')
