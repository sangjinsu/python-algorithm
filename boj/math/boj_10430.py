a, b, c = map(int, input().strip().split())

value = [0, 0, 0, 0]
value[0] = (a + b) % c
value[1] = ((a % c) + (b % c)) % c
value[2] = (a * b) % c
value[3] = ((a % c) * (b % c)) % c

for v in value:
    print(v)
