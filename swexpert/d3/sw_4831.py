test_cases = int(input().strip())


def is_station_front(front_road):
    for station in front_road:
        if station:
            return True
    return False


def is_bus_last_stop(road, bus, last_stop):
    return road + bus == last_stop


for t in range(1, test_cases + 1):
    k, n, m = tuple(map(int, input().strip().split()))
    stations = tuple(map(int, input().strip().split()))

    road = [False] * (n + 1)
    for station in stations:
        road[station] = True

    bus = k
    cnt = 0
    for i in range(1, len(road)):
        bus -= 1
        if road[i]:
            if not is_station_front(road[i + 1: i + bus + 1]) and not is_bus_last_stop(i, bus, n):
                bus = k
                cnt += 1
        if not bus and not is_bus_last_stop(i, bus, n):
            cnt = 0
            break

    print('#{} {}'.format(t, cnt))
