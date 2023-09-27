def solution(ingredient):
    answer = 0
    ham = []
    # [1-2-3-1]
    for i in ingredient:
        ham.append(i)
        if ham[-4:] == [1, 2, 3, 1]:
            answer += 1
            for _ in range(4):
                ham.pop()

    return answer