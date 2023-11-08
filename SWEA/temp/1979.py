T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # n x n 크기의 단어 퍼즐, k 길이의 단어
    n, k = map(int, input().split())
    table = []
    cnt = 0
    for _ in range(n):
        table.append(list(map(str, input().split())))

    # print(table)

    # 가로로 한번 쭉 읽기
    for i in range(n):
        temp = ''.join(table[i])
        if '1'*k in temp:
            print(temp)
            save1 = 0
            for j in range(n):
                if table[i][j] == '1':
                    save1 += 1
                elif table[i][j] == '0':
                    save1 = 0

                if save1 == k and j < n-1:
                    if table[i][j+1] != '1':
                        cnt += 1
                        save1 = 0
                elif save1 == k and j == n-1:
                    cnt += 1
                    save1 = 0
    # print('가로에서', cnt)
    # 세로로 한번 쭉 읽기
    for i in range(n):
        save1 = 0
        for j in range(n):
            # print(table[j][i])
            if table[j][i] == '1':
                save1 += 1
            elif table[j][i] == '0':
                save1 = 0
            # print('save in here', save1)
            if save1 == k and j < n-1:
                if table[j+1][i] != '1':
                    cnt += 1
                    save1 = 0
            elif save1 == k and j == n-1:
                cnt += 1
                save1 = 0
        # print('count in here', cnt)
    print(f'#{test_case} {cnt}')
