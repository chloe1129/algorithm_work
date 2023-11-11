T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range(1, T + 1):
    n = int(input())
    lst = []
    for i in range(n):
        lst.append(list(map(str, input().split())))

    re90 = [[0]*n for _ in range(n)]
    re180 = [[0]*n for _ in range(n)]
    re270 = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            re90[j][n-1-i] = lst[i][j]

    for i in range(n):
        for j in range(n):
            re180[j][n-1-i] = re90[i][j]

    for i in range(n):
        for j in range(n):
            re270[j][n-1-i] = re180[i][j]

    print(f'#{test_case}')

    for i in range(n):
        print(''.join(re90[i]) + ' ' + ''.join(re180[i])+' '+''.join(re270[i]))
