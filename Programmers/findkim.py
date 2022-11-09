def solution(seoul):
    answer = "김서방은 num에 있다"
    num = seoul.index('Kim')
    answer = answer.replace("num", str(num))
    return answer


#index 함수 이용
def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))

print(solution(["Jane", "Kim"]))