def solution(n, edge):
    def bfs(k):
        queue = [k]
        visited[k] = 1
        while queue:
            v = queue.pop(0)
            for adj in graph[v]:
                if not visited[adj]:
                    visited[adj] = visited[v] + 1
                    queue.append(adj)

    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    bfs(1)

    answer = visited.count(max(visited))
    return answer


n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, vertex))
