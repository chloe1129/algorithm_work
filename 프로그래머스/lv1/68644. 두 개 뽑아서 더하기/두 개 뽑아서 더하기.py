from itertools import combinations
def solution(numbers):
    answer = []
    a = set(list(combinations(numbers,2)))
    for i in a:
        answer.append(sum(list(i)))

    return sorted(list(set(answer)))