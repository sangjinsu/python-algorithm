def solution(answers):
    supoza1 = [1, 2, 3, 4, 5]
    supoza2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supoza3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score1 = 0
    score2 = 0
    score3 = 0

    for i, v in enumerate(answers):
        if supoza1[i % 5] == v:
            score1 += 1

        if supoza2[i % 8] == v:
            score2 += 1

        if supoza3[i % 10] == v:
            score3 += 1

    scores = [score1, score2, score3]
    maxScore = max(scores)
    answer = list()
    for i, score in enumerate(scores, start=1):
        if maxScore == score:
            answer.append(i)

    return answer