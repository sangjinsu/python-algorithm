import bisect
import sys


def main():
    _ = int(sys.stdin.readline())
    datas: list[int] = sorted(list(map(int, sys.stdin.readline().split())))
    m: int = int(sys.stdin.readline())
    nums: list[int] = list(map(int, sys.stdin.readline().split()))
    for num in nums:
        result = 1
        if bisect.bisect_left(datas, num) - bisect.bisect_right(datas, num) == 0:
            result = 0

        sys.stdout.write(str(result) + '\n')


if __name__ == '__main__':
    main()
