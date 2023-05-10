from itertools import combinations


def solution(nums):
    answer = 0
    a = [sum(i) for i in list(combinations(nums, 3))]
    for i in a:
        count = 0
        for j in range(2, i):
            if i % j == 0:
                count += 1
        if count == 0:
            answer += 1
    return answer


print(solution([1, 2, 7, 6, 4]))
