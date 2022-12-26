S, P = map(int, input().strip().split())
dna = input().strip()
counts = list(map(int, input().strip().split()))

min_dna = dict(
    A=counts[0],
    C=counts[1],
    G=counts[2],
    T=counts[3],
)

count_dna = dict(
    A=0,
    C=0,
    G=0,
    T=0,
)

for d in dna[:P]:
    count_dna[d] += 1

start = 0
end = P

result = 0
while True:
    count = 0
    for key in ['A', 'C', 'G', 'T']:
        if count_dna.get(key) >= min_dna.get(key):
            count += 1
    if count == 4:
        result += 1

    if end >= len(dna):
        break

    count_dna[dna[start]] -= 1
    count_dna[dna[end]] += 1
    start += 1
    end += 1

print(result)
