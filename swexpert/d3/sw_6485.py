test_cases = int(input().strip())

for t in range(1, test_cases + 1):
    n = int(input().strip())
    bus_lines = [tuple(map(int, input().strip().split())) for _ in range(n)]
    p = int(input().strip())
    stations = [int(input().strip()) for _ in range(p)]
    counts = [0] * p

    for i in range(len(stations)):
        for line in bus_lines:
            if line[0] <= stations[i] <= line[1]:
                counts[i] += 1
    result = ' '.join(map(str, counts))
    print(f"#{t} {result}")
