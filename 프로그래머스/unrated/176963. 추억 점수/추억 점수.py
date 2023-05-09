def solution(name, yearning, photo):
    answer = []
    
    p = dict(zip(name, yearning))
    for i in photo:
        a=0
        for j in i:
            if j in p:
                a+=p[j]
        answer.append(a)
    return answer