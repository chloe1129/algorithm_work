def solution(s):
    answer = 0
    s = str(s)
    if s[0] == '-':
        answer = int(s)
    else:
        answer = int(s)
    return answer

#int 형으로 바꿀떄 알아서 +,- 기호를 인식해서 if문을 사용해 나눠줄 필요가 없다!
a = solution(+1234)
print(a)