def solution(n,k):
    answer=0
    while True:
        if n % k == 0:
            answer+=1
            n=n/k
            
        else:
            answer+=1
            n-=1
            
        if n == 1:
            break
    return answer

    '''
    ideal answer
    while True:
        target = (n//k)*k
        result += (n-target)
        n = target

        if n<k:
            break

        result +=1
        n//=k
    
    result += (n-1)
    '''
    


a = solution(25,3)
print(a)

