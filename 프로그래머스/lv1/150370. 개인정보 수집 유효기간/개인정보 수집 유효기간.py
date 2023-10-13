def solution(today, terms, privacies):
    answer = []
    tY,tM,tD = map(int,today.split('.'))
    termlist = {}
    for i in range(len(terms)):
        a,b = terms[i].split(' ')
        termlist[a]=int(b)
    
    for i in range(len(privacies)):
        date, term = privacies[i].split(' ')
        pY,pM,pD = map(int,date.split('.'))
        
        if termlist[term]>=12:
            pY+=(termlist[term])//12
            pM += (termlist[term])%12
        else:
            pM += (termlist[term])
        
        if pM>12:
            pY+=(pM)//12
            pM = pM%12
        
        print(pY,pM,pD)    
        
        if tY > pY:
            answer.append(i+1)
        elif tY == pY:
            if tM > pM:
                answer.append(i+1)
            elif tM == pM:
                if tD>=pD:
                    answer.append(i+1)
                
            
    return answer