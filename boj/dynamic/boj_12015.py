import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().strip().split()))

stack = [nums[0]]
cnt = 1
for num in nums:
    if stack[-1] < num:
        stack.append(num)
    else:
        left = 0
        right = len(stack) - 1
        while left < right:
            mid = (left + right) // 2
            if stack[mid] < num:
                left = mid + 1
            else:
                right = mid
        stack[right] = num
sys.stdout.write(str(len(stack)))
