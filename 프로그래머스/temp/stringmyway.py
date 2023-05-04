def solution(strings, n):
    answer = {}
    strings = sorted(strings)
    for i in range(len(strings)):
        answer[strings[i]] = strings[i][n]
    
    a = dict(sorted(answer.items(), key=lambda item: item[1]))

    return list(a.keys())

print(solution(["sun", "bed", "car"],1))