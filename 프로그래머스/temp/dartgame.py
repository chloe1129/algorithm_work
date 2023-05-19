import re


def solution(dartResult):
    answer = []
    indics = []
    choice = []

    p = re.compile('[0-9]+')
    result = p.finditer(dartResult)

    for i in result:
        indics.append(i.start())

    for i in range(3):
        if i == 2:
            choice.append(dartResult[indics[i]:])
        else:
            choice.append(dartResult[indics[i]:indics[i+1]])
    print(choice)

    for i in range(3):
        if choice[i].find("*") > 0:
            if i == 0:
                answer.append(score(choice[i])*(2))
            else:
                answer.append(score(choice[i])*(2))
                answer[i-1] = answer[i-1]*(2)
        elif choice[i].find("#") > 0:
            answer.append(score(choice[i])*(-1))
        else:
            answer.append(score(choice[i]))
    return sum(answer)


def score(score):
    digit = ''
    p = re.compile('[0-9]+')
    result = p.finditer(score)

    for i in result:
        digit = (i.group())

    if score.find("S") > 0:
        return int(digit)**1
    elif score.find("D") > 0:
        return int(digit)**2
    elif score.find("T") > 0:
        return int(digit)**3


print(solution("1D2S#10S"))
