T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    a = W*P
    if W < R:
        b = Q
    else:
        b = Q + (W-R)*S

    result = a if a < b else b
    print(f'#{test_case} {result}')
