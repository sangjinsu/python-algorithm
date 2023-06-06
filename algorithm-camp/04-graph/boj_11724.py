import sys


def dfs(graph: list[list[int]], visited: list[bool], v: int):
    visited[v] = True
    for vertex in graph[v]:
        if not visited[vertex]:
            dfs(graph, visited, vertex)


def dfs_mat(mat: list[list[int]], visited: list[bool], v: int):
    visited[v] = True
    for i in range(1, len(mat[v])):
        if mat[v][i] == 1 and not visited[i]:
            dfs(graph, visited, i)


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N + 1)]
    mat = [[0] * (N + 1) for _ in range(N + 1)]

    visited = [0] * (N + 1)

    for _ in range(M):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

        mat[u][v] = 1
        mat[v][u] = 1

    result = 0
    for i in range(1, N + 1):
        if not visited[i]:
            result += 1
            dfs_mat(mat, visited, i)

    sys.stdout.write(str(result))
