import sys

n, m = map(int, sys.stdin.readline().strip().split())


def count_divisor(n, divisor):
    cnt = 0
    while n != 0:
        n //= divisor
        cnt += n
    return cnt


five = count_divisor(n, 5) - count_divisor(m, 5) - count_divisor(n - m, 5)
two = count_divisor(n, 2) - count_divisor(m, 2) - count_divisor(n - m, 2)
sys.stdout.write(str(min(five, two)))
