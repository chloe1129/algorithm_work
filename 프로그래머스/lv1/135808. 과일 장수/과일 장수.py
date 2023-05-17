def solution(k, m, score):
    answer = 0
    part = []
    if len(score) < m:
        return 0
    else:
        score.sort()
        for i in range(len(score)//m):

            part.append(score[(len(score)-(i+1)*m):(len(score)-i*m)])

    for i in part:
        answer += (min(i))*m
    return answer