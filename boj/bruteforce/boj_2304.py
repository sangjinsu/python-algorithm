n = int(input())

col = [0] * 1001
for i in range(n):
    c, v = map(int, input().split())
    col[c] = v

highest = max(col)
highest_idx = col.index(highest)

result = 0
max_height = 0
for i in range(highest_idx + 1):
    if max_height < col[i]:
        max_height = col[i]
    result += max_height

max_height = 0
for i in range(1000, highest_idx, -1):
    if max_height < col[i]:
        max_height = col[i]
    result += max_height

print(result)
