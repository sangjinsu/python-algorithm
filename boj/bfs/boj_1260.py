import sys
from collections import deque


def bfs(graph: list[list[int]], visited: list[int], v: int):
    queue = deque([v])
    visited[v] = True
    while queue:
        node = queue.popleft()
        sys.stdout.write(str(node) + ' ')
        for vertex in graph[node]:
            if not visited[vertex]:
                visited[vertex] = True
                queue.append(vertex)

def dfs(graph: list[list[int]], visited: list[int], v: int):
    sys.stdout.write(str(v) + ' ')
    visited[v] = True
    for node in graph[v]:
        if not visited[node]:
            dfs(graph, visited, node)

def main():
    n, m, v = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n + 1)]
    for i in range(m):
        s, e = map(int, sys.stdin.readline().split())
        graph[s].append(e)
        graph[e].append(s)

    for i in range(n+1):
        graph[i].sort()

    visited = [False] * (n + 1)
    dfs(graph, visited, v)
    visited = [False] * (n + 1)
    print()
    bfs(graph, visited, v)


if __name__ == "__main__":
    main()
