import sys

num = int(sys.stdin.readline().strip())

if not num:
    print(0)
else:
    result = ''
    while num != 0:
        k = num
        if num > 0:
            k = int(num / -2)
        elif num < 0:
            k = int(num / -2 + .5)
        m = num - k * -2
        result = str(m) + result
        num = k

    sys.stdout.write(result)
