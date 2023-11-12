T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    pascal = [[1]]
    i = 1
    while (i < n):
        pascal.append([0]*(i+1))
        print('this is pascal', pascal)
        for j in range(i+1):
            if j == 0:
                pascal[i][j] = pascal[i-1][0]
            elif j == i:
                pascal[i][j] = pascal[i-1][-1]
            else:
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        i += 1
    print(f'#{test_case}')
    for i in range(len(pascal)):
        print(' '.join(list(map(str, pascal[i]))))
