graph = [
    [],
    [2, 6],
    [1],
    [4, 5, 6],
    [3],
    [3],
    [1, 3]
]


def dfs1(v, visited, graph):
    stack = [v]
    while stack:
        node = stack.pop()
        visited[node] = True
        print(node)
        for nd in graph[node]:
            if not visited[nd]:
                stack.append(nd)


def dfs2(v, visited, graph):
    visited[v] = True
    print(v)
    for node in graph[v]:
        if not visited[node]:
            dfs2(node, visited, graph)


n = 6

visited = [False] * (n + 1)
dfs1(1, visited, graph)
print()
visited = [False] * (n + 1)
dfs2(1, visited, graph)
