def solution(participant, completion):
    temp = {}
    for i in participant:
        if i in temp:
            temp[i] += 1
        else:
            temp[i] = 1

    for j in completion:
        if j in temp:
            temp[j] -= 1

    for k in temp:
        if temp[k] == 1:
            return k