import sys

N = int(sys.stdin.readline().strip())
num = 1
total = 0

while True:
    total += num
    if total > N:
        num -= 1
        break
    num += 1

sys.stdout.write(str(num))
