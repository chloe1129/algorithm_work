def solution(numbers, hand):
    answer = ''
    keypad = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              ['*', 0, '#']]

    rh = 0
    lh = 0

    for i in numbers:
        for a, b in enumerate(keypad):
            if i in b:
                print(a, b.index(i))
    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
