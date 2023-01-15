import sys
from collections import deque


def bfs(tree, distance, visited, v):
    queue = deque([v])
    visited[v] = True
    while queue:
        node = queue.popleft()
        for vertex, cost in tree[node]:
            if not visited[vertex]:
                visited[vertex] = True
                queue.append(vertex)
                distance[vertex] = distance[node] + cost


def main():
    n = int(sys.stdin.readline())
    tree = [list() for _ in range(n + 1)]
    for i in range(n):
        data = list(map(int, sys.stdin.readline().split()))
        start = data[0]
        index = 1
        while True:
            vertex = data[index]
            if vertex == -1:
                break
            tree[start].append((vertex, data[index + 1]))
            index += 2

    visited = [False] * (n + 1)
    distance = [0] * (n + 1)

    bfs(tree, distance, visited, 1)
    max_index = 1
    for i in range(2, n + 1):
        if distance[max_index] < distance[i]:
            max_index = i

    visited = [False] * (n + 1)
    distance = [0] * (n + 1)
    bfs(tree, distance, visited, max_index)

    sys.stdout.write(str(max(distance)))


if __name__ == "__main__":
    main()
