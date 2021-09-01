test_cases = int(input())

for t in range(1, test_cases + 1):
    n = int(input())
    cards = list(input().split())

    deck = []

    if len(cards) % 2 == 0:
        mid = len(cards) // 2
        for i in range(mid):
            deck.append(cards[i])
            deck.append(cards[i + mid])
    else:
        mid = len(cards) // 2
        for i in range(mid):
            deck.append(cards[i])
            deck.append(cards[i + mid + 1])
        deck.append(cards[mid])

    print('#{} {}'.format(t, ' '.join(deck)))