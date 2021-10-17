arr = [3, 6, 7, 1, 5, 4]
n = len(arr)

for i in range(1, 1 << n):
    for j in range(n):
        if i & (1 << j):
            print(arr[j], end=' ')
    print()
