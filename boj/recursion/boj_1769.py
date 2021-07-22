import sys

X = sys.stdin.readline().strip()


def is_multiple_of_three(x, cnt=0):
    if len(x) == 1:
        return cnt, 'YES' if int(x) % 3 == 0 else "NO"
    else:
        total = sum(map(int, x))
        cnt += 1
        return is_multiple_of_three(str(total), cnt)


count, answer = is_multiple_of_three(X)
sys.stdout.write(str(count) + '\n')
sys.stdout.write(answer + '\n')
