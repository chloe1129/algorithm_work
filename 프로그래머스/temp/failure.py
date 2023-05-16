def solution(N, stages):
    answer = []

    for i in range(1, N+1):
        answer.append(list(map(lambda x: x-i, stages)))

    for i in answer:
        print(i)

    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
