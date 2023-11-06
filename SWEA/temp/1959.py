T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    listn = list(map(int, input().split()))
    listm = list(map(int, input().split()))

    # n이 m보다 무조건 작게, n<m
    if n > m:
        n, m = m, n
        listn, listm = listm, listn

    maxmul = float('-inf')
    for idx in range(m-n+1):
        i = 0  # n의 인덱스
        j = idx  # m의 인덱스
        temp = 0
        while (i < n and j < j+n):
            temp += listn[i]*listm[j]
            i += 1
            j += 1
        maxmul = max(maxmul, temp)

    print(f'#{test_case} {maxmul}')
