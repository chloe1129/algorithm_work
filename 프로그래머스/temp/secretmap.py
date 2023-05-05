def solution(n, arr1, arr2):
    answer = []
    map1 = list(map(lambda x: bin(x)[2:].zfill(n), arr1))
    map2 = list(map(lambda x: bin(x)[2:].zfill(n), arr2))
    #print(map1, map2)

    for i in range(n):
        a = ''
        for j in range(n):
            if map1[i][j] == '0' and map2[i][j] == '0':
                a+=' '
            else:
                a+='#'
        answer.append(a)
    return answer


print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))