T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for test_case in range(1, T + 1):
    month1, day1, month2, day2 = map(int, input().split())
    if month2-month1 == 0:
        # print('1111111111111')
        print(f'#{str(test_case)} {str(day2-day1+1)}')
    else:
        if month2-month1 == 1:
            # print('222222222222222')
            print(f'#{str(test_case)} {str((month[month1-1]-day1+1)+day2)}')
        else:
            temp = 0
            # print('333333333333')
            for i in range(month1+1, month2):
                # print('whole month', i)
                temp += month[i-1]
            print(
                f'#{str(test_case)} {str(temp+(month[month1-1]-day1+1)+day2)}')
