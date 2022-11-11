def solution(s):
    answer = ''
    if (len(s)%2==0):
        answer=s[len(str(s))//2-1]+s[len(str(s))//2]
    else:
        answer=s[len(str(s))//2]
    return answer

print(solution("qwer"))