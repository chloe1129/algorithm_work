def solution(arr):
    answer = []
    for i in range(0,len(arr)-1):
        if arr[i] != arr[i+1]:
            answer.append(arr[i])
        else:
            pass
    answer.append(arr[len(arr)-1])

    return answer

print(solution([1,1,3,3,0,1,1,1]))