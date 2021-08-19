test_cases = 10


# def dfs(v: int, visited: [int], graph: [[int]]):
#     visited[v] = 1
#     for node in graph[v]:
#         if not visited[node]:
#             dfs(node, visited, graph)

def dfs(v: int, visited: [bool], graph: [[int]]):
    stack = [v]
    while stack:
        node = stack.pop()
        visited[node] = 1
        for nd in graph[node]:
            if not visited[nd]:
                stack.append(nd)


for t in range(1, test_cases + 1):
    test_num, edge_num = tuple(map(int, input().strip().split()))
    graph = [[] for _ in range(100)]
    edges = list(map(int, input().strip().split()))

    i = 0
    while i < edge_num * 2:
        graph[edges[i]].append(edges[i + 1])
        i += 2

    visited = [0] * 100
    start, end = 0, 99
    dfs(start, visited, graph)
    print('#{} {}'.format(t, visited[end]))
