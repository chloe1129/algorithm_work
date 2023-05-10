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

print(solution(["may", "kein", "kain", "radi"],
               [5, 10, 1, 3],
               [["may", "kein", "kain", "radi"],
                ["may", "kein", "brin", "deny"], 
                ["kon", "kain", "may", "coni"]]))