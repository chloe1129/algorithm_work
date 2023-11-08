T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    t = int(input())

    v = 0  # 속도
    m = 0  # 거리
    for _ in range(t):
        temp = list(map(int, input().split()))  # temp[1] 가속도의 값
        # 0: 속도 유지, 1: 가속, 2: 감속
        if temp[0] == 0:
            m += v
        elif temp[0] == 1:
            v += temp[1]
            m += v
        elif temp[0] == 2:
            v -= temp[1]
            if v < 0:
                v = 0
            m += v

    print(f'#{test_case} {m}')
