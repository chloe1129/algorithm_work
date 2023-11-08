T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    t = int(input())
    n = list(map(int, input().split()))
    n.sort()
    temp = ' '.join(list(map(str, n)))
    print(f'#{test_case} {temp}')
