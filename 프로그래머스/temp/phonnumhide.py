def solution(phone_number):
    answer = list(phone_number)
    for i in range(len(phone_number)-4):
        answer[i]="*"  
    return ''.join(s for s in answer)


#모범답만 후덜덜,,, * 찍는거 말고 문자열 곱하기 사용
def hide_numbers(s):
    return "*"*(len(s)-4) + s[-4:]

print(solution("01033334444"))

