test_cases = int(input().strip())

for t in range(1, test_cases + 1):
    line = input().strip()
    cards = []
    for i in range(0, len(line), 3):
        cards.append(line[i:i + 3])

    if len(cards) != len(set(cards)):
        print('#{} ERROR'.format(t))
    else:
        deck = dict(
            S=13,
            D=13,
            H=13,
            C=13
        )
        for card in cards:
            deck[card[0]] -= 1
        print('#{} {} {} {} {}'.format(t, deck['S'], deck['D'], deck['H'], deck['C']))
