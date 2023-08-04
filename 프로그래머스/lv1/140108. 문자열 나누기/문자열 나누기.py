def solution(s):
    answer = 0
    same = 0
    diff = 0
    a = s[0]
    for i in s:
        if same == diff:
            a = i
            same = 0
            diff = 0
            answer += 1
        if a == i:

            same += 1
        else:

            diff += 1

    return answer