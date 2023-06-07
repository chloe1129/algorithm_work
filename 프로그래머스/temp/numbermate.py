def solution(X, Y):
    answer = ''
    x = {}
    y = {}
    for i in range(0, 9):
        x[str(i)] = 0
        y[str(i)] = 0

    for i in list(X):
        x[i] += 1
    for i in list(Y):
        y[i] += 1
    print(x, y)

    for k in range(9, -1, -1):
        k = str(k)
        iternum = min(x[k], y[k])

        if answer == '' and k == '0' and iternum != 0:
            return '0'

        answer = ''.join([answer, k*iternum])

    if answer == '':
        return '-1'
    else:
        return answer


print(solution("5525", "1255"))
