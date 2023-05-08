def solution(food):
    answer = ''
    for i in range(1,len(food)):
        if food[i]>1:
            answer+=(str(i)*(food[i]//2))
    return answer + '0' + answer[::-1]

print(solution([1, 7, 1, 2]))