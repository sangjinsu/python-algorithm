arr = input()

for i in range(0, len(arr), 7):
    bits = arr[i:i + 7]
    result = 0
    n = 1
    for b in bits[::-1]:
        result += n * int(b)
        n *= 2
    print(result)
