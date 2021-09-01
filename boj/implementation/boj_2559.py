n, k = map(int, input().split())

temp = list(map(int, input().split()))

start = 0
end = k
tot = sum(temp[:k])
max_temp = tot
for i in range(n - k):
    tot = tot - temp[start + i] + temp[end + i]
    max_temp = max(max_temp, tot)

print(max_temp)
