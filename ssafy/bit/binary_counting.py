arr = [3, 6, 7, 1, 5, 4]
n = len(arr)

for i in range(1, 1 << n):
    for j in range(n):
        if i & (1 << j):
            print(arr[j], end=' ')
    print()

print()
print()

nums = [1, 2, 3, 4, 5]
visited = [0, 0, 0, 0, 0]
ans_list = []


def nCr(n, r, cnt):
    if n == len(nums):
        if cnt == r:
            ans_list.append([nums[i] for i in range(5) if visited[i]])
        return
    visited[n] = 1
    nCr(n + 1, r, cnt + 1)
    visited[n] = 0
    nCr(n + 1, r, cnt)


nCr(0, 3, 0)
print(ans_list)
