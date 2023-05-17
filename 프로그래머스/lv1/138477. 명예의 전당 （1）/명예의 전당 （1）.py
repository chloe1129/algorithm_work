def solution(k, score):
    answer = []
    day = []
    for i in score:
        if len(day) < k:
            day.append(i)
        else:
            day.append(i)
            day.remove(min(day))

        answer.append(min(day))
    return answer