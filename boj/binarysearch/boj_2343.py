import sys


def main():
    n, m = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))
    start = max(nums)
    end = sum(nums)

    while start <= end:
        mid = (start + end) // 2
        total, count = 0, 0
        for i in range(n):
            if total + nums[i] > mid:
                count += 1
                total = 0
            total += nums[i]
        if total != 0:
            count += 1
        if count > m:
            start = mid + 1
        else:
            end = mid - 1

    sys.stdout.write(str(start))


if __name__ == '__main__':
    main()
