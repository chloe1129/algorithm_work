def solution(n, lost, reserve):
    answer = 0
    lost = sorted(lost)
    reserve = sorted(reserve)

    real_lost = []
    for i in lost:
        real_lost.append(i)

    for i in range(len(lost)):
        if lost[i] in reserve:
            reserve.remove(lost[i])
            real_lost.remove(lost[i])
            answer += 1

    for i in real_lost:
        if i-1 in reserve:
            reserve.remove(i-1)
            answer += 1
        elif i+1 in reserve:
            reserve.remove(i+1)
            answer += 1
    return answer + (n-len(lost))