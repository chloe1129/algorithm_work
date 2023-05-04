import itertools

def solution(number):
    answer = 0
    a = [' '.join(str(i)) for i in number]
    b = list(itertools.combinations(number, 3))

    for i in b:
        c = list(map(int, i))
        if sum(c) == 0:
            answer+=1
    return answer