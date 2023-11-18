T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    dct = {}
    for i in range(len(lst)):
        if lst[i] in dct:
            dct[lst[i]] += 1
        else:
            dct[lst[i]] = 1
    dct = dict(sorted(dct.items(), key=lambda x: x[1]))
    print(f'#{n} {list(dct.keys())[-1]}')
