
def solution(N, stages):
    answer = []

    for i in range(1, N+1):
        a = 0
        b = 0
        for j in stages:
            if j == i:
                a += 1
            if j >= i:
                b += 1
        if b == 0:
            answer.append([i, 0])
        else:
            answer.append([i, float(a/b)])

    a = sorted(answer, key=lambda x: x[1], reverse=True)
    final = []
    for i in a:
        final.append(i[0])

    return final
