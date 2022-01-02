def solution(genres, plays):
    answer = []

    genre_play_lists = dict()
    genre_scores = dict()
    for i in range(len(genres)):
        genre_play_lists.setdefault(genres[i], []).append((i, plays[i]))
        genre_scores.setdefault(genres[i], 0)
        genre_scores[genres[i]] += plays[i]

    sorted_genre_scores = list(
        map(lambda score: score[0],
            sorted(
                list(genre_scores.items()),
                key=lambda score: score[1],
                reverse=True)))

    for genre in sorted_genre_scores:
        for songs in sorted(genre_play_lists[genre],
                            key=lambda play: play[1],
                            reverse=True)[:2]:
            answer.append(songs[0])

    return answer
