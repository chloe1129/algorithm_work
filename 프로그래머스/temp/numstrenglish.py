def solution(s):
    answer = s
    disit = {
            0:'zero',
            1:'one',
            2:'two',
            3:'three',
            4:'four',
            5:'five',
            6:'six',
            7:'seven',
            8:'eight',
            9:'nine'
            }
    for i in disit:
        if disit[i] in answer:
            answer = answer.replace(disit[i],str(i))
    
    return int(answer)

print(solution("23four5six7"))