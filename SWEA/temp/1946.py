T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    lst = []
    temp = ''
    for i in range(n):
        c, k = map(str, input().strip().split())
        k = int(k)

        if 10-len(temp) < k:
            lst.append(temp+c*(10-len(temp)))
            if k-(10-len(temp)) > 10:
                k = k - (10-len(temp))
                for i in range(k//10):
                    lst.append(c*10)
                temp = c*(k % 10)
            else:
                temp = c*(k-(10-len(temp)))

        elif 10-len(temp) > k:
            temp += c*k
        else:
            lst.append(temp+c*(10-len(temp)))
            temp = ''

    if temp != '':
        lst.append(temp)
    print(f'#{test_case}')
    for i in range(len(lst)):
        print(lst[i])
