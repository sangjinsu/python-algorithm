# 베이비진 게임
test_cases = int(input().strip())


def baby_gin(cards):
    tri, run = 0, 0
    nums = [0] * 10
    for card in cards:
        nums[card] += 1
    i = 0
    while i < 10:
        if nums[i] >= 3:
            nums[i] -= 3
            tri += 1
            continue
        if i < 8 and nums[i] >= 1 and nums[i + 1] >= 1 and nums[i + 2] >= 1:
            nums[i] -= 1
            nums[i + 1] -= 1
            nums[i + 2] -= 1
            run += 1
            continue
        i += 1
    return run + tri


for t in range(1, test_cases + 1):
    cards = list(map(int, input().strip().split()))

    player_one = []
    player_two = []

    result = 0
    for i in range(12):
        if i % 2:
            player_two.append(cards[i])
            if baby_gin(player_two):
                result = 2
                break
        else:
            player_one.append(cards[i])
            if baby_gin(player_one):
                result = 1
                break
    print('#{} {}'.format(t, result))
