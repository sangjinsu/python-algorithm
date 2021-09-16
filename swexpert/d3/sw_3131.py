n = 1000000

check = [True] * (n + 1)
check[0] = False
check[1] = False

m = int(n ** 0.5)
for i in range(2, m+1):
    if check[i]:
        for j in range(i + i, n, i):
            check[j] = False

for i in range(2, n):
    if check[i]:
        print(i, end=' ')
