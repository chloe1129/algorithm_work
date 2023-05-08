def solution(food):
    answer = ''
    for i in range(1,len(food)):
        if food[i]>1:
            answer+=(str(i)*(food[i]//2))
    return answer + '0' + answer[::-1]