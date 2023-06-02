def solution(n, m, section):
    answer = 0

    if m == 1:
        return len(section)
    elif m == n:
        return 1
    else:
        s = section[0]
        l = section[-1]
        while (True):
            s += m
            answer += 1
            if s >= n:
                break
            l -= m
            answer += 1
            if l < s:
                break
        return answer


print(solution(8, 4,	[2, 3, 6]))
