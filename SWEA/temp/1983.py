import math
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    score = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    grade = {}
    for i in range(n):
        mid, final, asmt = list(map(int, input().split()))
        grade[i+1] = (mid*(0.35) + final*(0.45) + asmt*(0.2))

    grade = dict(sorted(grade.items(), key=lambda x: x[1]))

    for i in range(n):
        grade[list(grade.keys())[i]] = n-i
    # print(grade)
    # print(grade[k], k/(n//10), round(k/(n//10))-1, math.ceil(k/(n//10))-1)
    print(f'#{test_case} {score[math.ceil(grade[k]/(n//10))-1]}')
