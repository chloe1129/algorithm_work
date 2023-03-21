
def solution(n):
    answer = list(map(str, str(n)))
    s = ''.join(sorted(answer, reverse=True))
    return int(s)


print(solution(118372))