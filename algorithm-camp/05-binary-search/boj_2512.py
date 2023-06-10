import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    budgets = list(map(int, sys.stdin.readline().split()))
    max_budget = int(sys.stdin.readline().strip())

    left = 0
    right = max(budgets)
    result = 0
    while left <= right:
        mid = (left + right) // 2
        total = 0
        for budget in budgets:
            if budget > mid:
                total += mid
            else:
                total += budget

        if total > max_budget:
            right = mid - 1
        else:
            result = mid
            left = mid + 1



    sys.stdout.write(str(result))
