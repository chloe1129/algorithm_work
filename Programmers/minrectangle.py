def solution(sizes):
    a = []
    b = []

    for i in range(len(sizes)):
        if sizes[i][0] > sizes[i][1]:
            temp = sizes[i][0]
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = temp

        '''
        이렇게 이차원 배열에서의 for 문 활용
        for a,b in sizes:
            if a< b:
                a,b = b,a
        '''

        a.append(sizes[i][0])
        b.append(sizes[i][1])

    a = max(a)
    b = max(b)

    return a*b

    

print(solution([[60, 50],[30, 70],[60, 30],[80, 40]]))