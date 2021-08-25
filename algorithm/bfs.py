lst = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
graph = [[] for _ in range(8)]
n = 7
e = 8
for i in range(e):
    graph[lst[i * 2]].append(lst[i * 2 + 1])
    graph[lst[i * 2 + 1]].append(lst[i * 2])


def bfs(start, graph):
    visited = [0] * (n+1)
    visited[start] = 1
    queue = [start]
    while queue:
        v = queue.pop(0)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[v] + 1
    print(visited)


bfs(1, graph)
