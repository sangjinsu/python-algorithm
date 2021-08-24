# 토너먼트 카드 게임
test_cases = int(input().strip())


def rock_scissor_paper(cards, s1, s2):
    card1 = cards[s1]
    card2 = cards[s2]

    if card1 == card2:
        return s1

    if card1 == 1:
        if card2 == 2:
            return s2
        else:
            return s1
    elif card1 == 2:
        if card2 == 1:
            return s1
        else:
            return s2
    else:
        if card2 == 1:
            return s2
        else:
            return s1


def tournament(cards, students):
    if len(students) <= 1:
        return students[0]

    start = 0
    end = len(students) - 1
    mid = (start + end) // 2
    s1 = tournament(cards, students[:mid + 1])
    s2 = tournament(cards, students[mid + 1:])
    return rock_scissor_paper(cards, s1, s2)


for t in range(1, test_cases + 1):
    n = int(input().strip())
    cards = list(map(int, input().strip().split()))
    students = [i for i in range(n)]
    result = tournament(cards, students)
    print('#{} {}'.format(t, result + 1))
