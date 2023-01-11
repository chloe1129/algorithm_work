def solution(n):
    answer = ''
    a = 0
    if n<3:
        a = n
    else:   
        while(True):
            answer += str(n%3)
            n=n//3
            if n<3:
                answer+=str(n)
                break
        
        for i in range(len(list(answer))):
            if int(list(answer)[i]) == 0:
                a += 0
            else:
                a += int(list(answer)[i]) * (3 ** (len(list(answer))-1-i))
    return a

print(solution(1))

'''
int('숫자(혹은 16진법의 문자와 같은 문자)로 이루어진 문자열',해당 진법) -> 10진법의 수로 변환
'''
