def solution(scores):
    scoresLen = len(scores)

    result = ''
    for i in range(scoresLen):
        self_score = scores[i][i]
        total = 0
        max_cnt = 0
        min_cnt = 0
        for j in range(scoresLen):
            total += scores[j][i]
            if self_score >= scores[j][i]:
                max_cnt += 1
            if self_score <= scores[j][i]:
                min_cnt += 1

        if max_cnt == 1 or min_cnt == 1:
            total -= scores[i][i]
            average = total / (scoresLen - 1)
        else:
            average = total / scoresLen

        if average >= 90:
            result += 'A'
        elif average >= 80:
            result += 'B'
        elif average >= 70:
            result += 'C'
        elif average >= 50:
            result += 'D'
        else:
            result += 'F'
    return result


scores = [
    [100, 90, 98, 88, 65],
    [50, 45, 99, 85, 77],
    [47, 88, 95, 80, 67],
    [61, 57, 100, 80, 65],
    [24, 90, 94, 75, 65]
]

solution(scores)
