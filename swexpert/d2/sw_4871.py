test_cases = int(input().strip())


def dfs(v: int, visited: [bool], graph: [[int]]):
    stack = [v]
    while stack:
        node = stack.pop()
        visited[node] = 1
        for nd in graph[node]:
            if not visited[nd]:
                stack.append(nd)


for t in range(1, test_cases + 1):
    v, e = tuple(map(int, input().strip().split()))
    graph = [[] for _ in range(v + 1)]
    for i in range(e):
        v1, v2 = tuple(map(int, input().strip().split()))
        graph[v1].append(v2)

    start, end = tuple(map(int, input().strip().split()))
    visited = [0] * (v + 1)
    dfs(start, visited, graph)

    print('#{} {}'.format(t, visited[end]))
