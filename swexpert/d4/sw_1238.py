from collections import deque


def bfs(v):
    Q = deque()
    Q.append(v)
    while Q:
        vertex = Q.popleft()
        for node in graph.get(vertex, []):
            if not visited[node]:
                visited[node] = visited[vertex] + 1
                Q.append(node)


test_cases = 10
for t in range(1, test_cases + 1):
    L, S = map(int, input().strip().split())
    data = list(map(int, input().strip().split()))
    graph = dict()
    node = 0
    for i in range(0, L, 2):
        graph.setdefault(data[i], []).append(data[i + 1])
        node = max([node, data[i], data[i + 1]])
    visited = [0] * (node + 1)

    bfs(S)
    max_value = max(visited)
    result = 0
    for i in range(len(visited)):
        if visited[i] == max_value:
            result = max(result, i)

    print('#{} {}'.format(t, result))
