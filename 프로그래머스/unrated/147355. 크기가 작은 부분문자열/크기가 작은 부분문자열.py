def solution(t, p):
    answer = []
    a = 0
    for i in range(len(t)-len(p)+1):
        answer.append(t[i:i+len(p)])
    for i in answer:
        if int(i)<=int(p):
            a+=1
    return a