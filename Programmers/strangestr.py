def solution(s):
    answer = ""
    count = 0
    s = s.lower()
    for a in s:
        if a == " ":
            answer += " "
            count = 0
        else:
            if count % 2 == 0:
                answer += a.upper()
            else:
                answer += a
            count +=1
    return answer

print(solution("  tRy hello  WORLD    "))