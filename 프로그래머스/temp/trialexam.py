import math


def solution(answers):
    answer = []
    s = {
        1: [1, 2, 3, 4, 5],
        2: [2, 1, 2, 3, 2, 4, 2, 5],
        3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    }
    for i in range(len(s)):
        if len(s) < len(answers):
            s[i+1] = s[i+1]*(math.ceil(len(answers)/len(s[i+1])))
        count = 0
        for j in range(len(answers)):
            if s[i+1][j] == answers[j]:
                count += 1
        answer.append(count)

    m = max(answer)
    return [i+1 for i, v in enumerate(answer) if v == m]


print(solution([1, 2, 3, 4, 5]))
