T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    stoku = []
    result = True
    for i in range(9):
        stoku.append(list(map(int, input().split())))

    # 가로 검사
    for i in range(9):
        print('가로검사', sorted(stoku[i]))
        if sorted(stoku[i]) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            result = False
            break
    # 세로 검사
    for i in range(9):
        temp = []
        for j in range(9):
            temp.append(stoku[j][i])
        print('세로검사', sorted(temp))
        if sorted(temp) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            result = False
            break

    a = 0
    # 3*3 검사
    while (a <= 6):
        temp1 = []
        for i in range(a, a+3):
            for j in range(0, 3):
                temp1.append(stoku[i][j])
        print('3*3검사1', sorted(temp1))
        if sorted(temp1) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            result = False
            break

        temp2 = []
        for i in range(a, a+3):
            for j in range(3, 6):
                temp2.append(stoku[i][j])
        print('3*3검사2', sorted(temp2))
        if sorted(temp2) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            result = False
            break

        temp3 = []
        for i in range(a, a+3):
            for j in range(6, 9):
                temp3.append(stoku[i][j])
        print('3*3검사3', sorted(temp3))
        if sorted(temp3) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            result = False
            break

        a += 3

    if result == True:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')
