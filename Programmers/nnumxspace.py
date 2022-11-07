def solution(x, n):
    answer = [0,]
    for i in range(0,n):
        answer.append(answer[i]+x)
    answer.pop(0)
    return answer

aw = solution(-2,2)
print(aw)