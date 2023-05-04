def solution(n):
    answer = []
    num = str(n)

    for i in range(len(num)):
        a=num[len(num)-i-1]
        answer.append(int(a))
    return answer


b = solution(12345)
print(b)