def solution(participants, completions):
    p = dict()
    for participant in participants:
        if p.get(participant) is not None:
            p[participant] += 1
        else:
            p[participant] = 1

    for completion in completions:
        p[completion] -= 1

    for participant in participants:
        if p.get(participant) == 1:
            return participant
