def solution(sizes):
    answer = []
    a = []
    b = []

    for i in range(len(sizes)):
        answer.append((lambda x,y: x*y)(sizes[i][0], sizes[i][1]))

        if sizes[i][0] > sizes[i][1]:
            temp = sizes[i][0]
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = temp

        a.append(sizes[i][0])
        b.append(sizes[i][1])

    a = max(a)
    b = max(b)

    return a*b

print(solution([[60, 50],[30, 70],[60, 30],[80, 40]]))