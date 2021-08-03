import sys

test_cases = int(sys.stdin.readline().strip())

for i in range(test_cases):
    num1, num2 = tuple(map(int, sys.stdin.readline().strip().split(' ')))

    m = max(num1, num2)
    n = min(num1, num2)
    while True:
        temp = m % n
        if temp == 0:
            break
        m, n = n, temp

    lcm = n * (num1 // n) * (num2 // n)
    sys.stdout.write(str(lcm) + '\n')
