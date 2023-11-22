


T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()
    result = float('-inf')
    print(lst)
    for i in range(len(lst)):
        idx = i
        temp = 0
        print('checkt', lst[i], k, lst[idx])
        print('temp', temp)
        while(True):
            if lst[idx] > lst[i]+k:
                break
            else:
                temp += 1
                idx += 1
            print('what?', idx, temp)
            if idx > len(lst)-1:
                break

        result = max(result, temp)
    print(result)


    # 표준출력(화면)으로 답안을 출력합니다.
    print(f"#{test_case} {result}")