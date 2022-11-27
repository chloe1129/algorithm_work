def solution(n):
    answer = 0
    k=list(map(int, n))
    print(k)
    for i in range(len(k)):
        if k[i] == 0:
            print(k[i])
            answer+=0
        else:
            answer*=k[i]

    return answer

print(solution("20984"))