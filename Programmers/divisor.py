def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if arr[i]%divisor == 0:
            answer.append(arr[i])
    if len(answer) == 0:
        answer=[-1]
    return sorted(answer)

print(solution([2, 36, 1, 3],1))