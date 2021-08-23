test_cases = int(input().strip())

for t in range(1, test_cases + 1):
    n = int(input().strip())
    bus_lines = [tuple(map(int, input().strip().split())) for _ in range(n)]
    p = int(input().strip())
    stations = [int(input().strip()) for _ in range(p)]
    # counts = [0] * p
    #
    # for i in range(len(stations)):
    #     for line in bus_lines:
    #         if line[0] <= stations[i] <= line[1]:
    #             counts[i] += 1
    # result = ' '.join(map(str, counts))
    # print(f"#{t} {result}")

    start = [0] * 5001
    end = [0] * 5001

    for line in bus_lines:
        start[line[0]] += 1
        end[line[1]] += 1

    counts = [0] * 5001
    for i in range(1, 5001):
        counts[i] = start[i] + counts[i-1] - end[i-1]

    print(f"#{t}", end=' ')
    for s in stations:
        print(f'{counts[s]}', end=' ')
    print()