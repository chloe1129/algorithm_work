import re

def solution(s):
    answer = []
    for i in range(len(s)):
        object = re.finditer(pattern=s[i], string=s)
        indices = [index.start() for index in object]
        if indices == [0]:
            answer.append(-1)
        else:
            if i==indices[0]:
                answer.append(-1)
            else:
                answer.append(indices[indices.index(i)]-indices[indices.index(i)-1])
            
    return answer

print(solution("foobar"))