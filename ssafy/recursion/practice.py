nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
visited = [False] * 10


def recursion(idx):
    if idx >= 10:
        tot = 0
        for v in range(10):
            if visited[v]:
                tot += nums[v]
                if tot > 10:
                    return
        if tot == 10:
            for v in range(10):
                if visited[v]:
                    print(nums[v], end=' ')
            print()
        return
    visited[idx] = True
    recursion(idx + 1)
    visited[idx] = False
    recursion(idx + 1)


recursion(0)
