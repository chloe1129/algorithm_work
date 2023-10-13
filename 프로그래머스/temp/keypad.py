def solution(numbers, hand):
    answer = ''

    keypad = {1: 0, 2: 0, 3: 0,
              4: 1, 5: 1, 6: 1,
              7: 2, 8: 2, 9: 2,
              '*': 3, 0: 3, '#': 3}
    left = '*'
    right = '#'
    # print('first!!!',keypad[left],keypad[right])
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            left = i
            answer += 'L'
        elif i == 3 or i == 6 or i == 9:
            right = i
            answer += 'R'
        else:
            # print('now', i)
            dis_l = abs(keypad[i]-keypad[left])
            dis_r = abs(keypad[i]-keypad[right])
            # print(left, dis_l, right, dis_r)
            if left == 1 or left == 4 or left == 7 or left == '*':
                dis_l += 1
            if right == 3 or right == 6 or right == 9 or right == '#':
                dis_r += 1

            if dis_l > dis_r:
                right = i
                # print('R')
                answer += 'R'
            elif dis_l < dis_r:
                left = i
                # print('L')
                answer += 'L'
            else:
                if hand == 'left':
                    left = i
                    # print('L')
                    answer += 'L'
                elif hand == 'right':
                    right = i
                    # print('R')
                    answer += 'R'

    return answer


print(solution([2, 1], "right"))
