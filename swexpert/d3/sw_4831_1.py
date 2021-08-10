test_cases = int(input().strip())

for t in range(1, test_cases + 1):
    k, n, m = tuple(map(int, input().strip().split()))
    stations = list(map(int, input().strip().split()))

    bus = k
    cnt = 0

    stations.insert(0, 0)
    stations.append(n)
    bus = 0
    for i in range(1, len(stations)):
        if stations[i] - stations[i - 1] > k:
            cnt = 0
            break

        if bus + k < stations[i]:
            bus = stations[i - 1]
            cnt += 1

    print('#{} {}'.format(t, cnt))
