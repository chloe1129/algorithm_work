T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    result = [[0] * n for _ in range(n)]
    cnt = 2

    i = 0  # 방향 인덱스
    # 우 하 좌 상
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    x, y = 0, 0
    result[0][0] = '1'
    while (cnt <= n*n):
        if 0 <= x+dx[i] < n and 0 <= y+dy[i] < n:  # 범위 안에 속하는지
            # print('xy좌표', i, x+dx[i], y+dy[i])
            if result[x+dx[i]][y+dy[i]] == 0:
                x = x+dx[i]
                y = y+dy[i]
                result[x][y] = str(cnt)
                cnt += 1
            else:
                i += 1
        else:
            # 범위에 속하지 않으면 다음 방향으로 변경
            i += 1

        if i > 3:
            i = 0

    print(f'#{test_case}')
    for i in range(n):
        print(' '.join(result[i]))
