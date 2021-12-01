import sys


def make_team(idx, team):
    if len(team) == N // 2:
        teams.append(team[:])
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            team.append(i)
            make_team(i, team)
            team.pop()
            visited[i] = False


def cal_score(teamA, teamB):
    teamA_score = 0
    teamB_score = 0
    for i in range(len(teamA) - 1):
        for j in range(i + 1, len(teamA)):
            teamA_score += mat[teamA[i]][teamA[j]] + mat[teamA[j]][teamA[i]]

    for i in range(len(teamB) - 1):
        for j in range(i + 1, len(teamB)):
            teamB_score += mat[teamB[i]][teamB[j]] + mat[teamB[j]][teamB[i]]

    result = abs(teamA_score - teamB_score)
    return result


N = int(sys.stdin.readline().strip())
mat = [list(map(int, input().strip().split())) for _ in range(N)]
visited = [False] * N

teams = []
make_team(0, [])
teamA = teams[:len(teams) // 2]
teamB = list(reversed(teams[len(teams) // 2:]))

result = 9999
for i in range(len(teamA)):
    result = min(result, cal_score(teamA[i], teamB[i]))

sys.stdout.write(str(result))