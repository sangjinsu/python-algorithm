def solution(n, computers):
    answer = 0
    visited = [False] * n

    def dfs(idx):
        for i in range(len(computers[idx])):
            if not visited[i] and i != idx and computers[idx][i] == 1:
                visited[i] = True
                dfs(i)

    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1

    return answer
