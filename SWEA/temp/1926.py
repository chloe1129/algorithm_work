T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
result = []
for test_case in range(1, T + 1):
    time = 0
    for i in range(len(str(test_case))):
        if '3' in str(test_case)[i]:
            time += 1
        if '6' in str(test_case)[i]:
            time += 1
        if '9' in str(test_case)[i]:
            time += 1

    if time == 0:
        result.append(str(test_case))
    else:
        result.append(str('-'*time))

print(' '.join(result))
