# 노드의 거리
test_cases = int(input().strip())


def bfs(graph, start, end):
    visited = [0] * (v + 1)

    visited[start] = 1
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        for adj in graph[vertex]:
            if not visited[adj]:
                queue.append(adj)
                visited[adj] = visited[vertex] + 1
    if not visited[end]:
        return 0
    else:
        return visited[end] - 1


for t in range(1, test_cases + 1):
    v, e = map(int, input().strip().split())
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        v1, v2 = map(int, input().strip().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    start, end = map(int, input().strip().split())
    result = bfs(graph, start, end)

    print('#{} {}'.format(t, result))
