T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    h1, m1, h2, m2 = map(int, input().split())
    reh, rem = 0, 0
    if m1 + m2 > 60:
        reh += 1
        rem = m1+m2-60
    else:
        rem = m1+m2

    if reh+h1+h2 > 12:
        reh = int((reh + h1+h2) % 12)
    else:
        reh = reh + h1+h2

    if reh == 0:
        reh = 12
    print(f'#{test_case} {str(reh)} {str(rem)}')
