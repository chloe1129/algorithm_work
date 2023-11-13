T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    left = n
    for i in range(len(money)):
        if left // money[i] > 0:
            temp = left // money[i]
            left = (left) % money[i]
            money[i] = str(temp)
        else:
            money[i] = '0'

    print(f'#{test_case}')
    print(' '.join(money))
