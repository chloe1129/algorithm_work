T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    numcnt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    N = int(input())
    num = 1
    while (0 in numcnt):
        # print('this is numcoujt', str(num*N), numcnt)
        for i in range(len(str(num*N))):
            # print('add num', int(str(num*N)), int(str(num*N)[i]))
            numcnt[int(str(num*N)[i])] += 1
        num += 1
    print(f'#{test_case} {str((num-1)*N)}')
