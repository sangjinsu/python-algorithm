import sys


def solve(ps: str):
    left = 0
    for p in ps:
        if p == '(':
            left += 1
        elif p == ')':
            if left == 0:
                sys.stdout.write('NO\n')
                return
            left -= 1

    if left == 0:
        sys.stdout.write('YES\n')
        return
    sys.stdout.write('NO\n')


if __name__ == '__main__':
    tests: int = int(sys.stdin.readline().strip())
    for test in range(tests):
        ps: str = sys.stdin.readline().strip()
        solve(ps)
