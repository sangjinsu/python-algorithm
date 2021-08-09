import sys


n = int(sys.stdin.readline().strip())

num = 1
for i in range(1, n+1):
    num *= i

cnt = 0
for i in str(num)[::-1]:
    if i != '0':
        break
    cnt += 1

sys.stdout.write(str(cnt))
