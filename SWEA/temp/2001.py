T = int(input())


def maxsum(x, y):
    result = 0
    for i in range(m):
        for j in range(m):
            result += lst[x+i][y+j]
    return result


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    lst = []
    for _ in range(n):
        lst.append(list(map(int, input().split())))
    # 배열에서 가장 합이 큰 m*m을 구하라

    result = float('-inf')
    if n-m == 0:
        result = 0
        for i in range(n):
            result += sum(lst[i])
    else:
        for i in range(n-m+1):
            for j in range(n-m+1):
                result = max(result, maxsum(i, j))

    print(f'#{test_case} {result}')
