import math

def checknext(n):
    if n%2>0:
        n=int(n//2)+1
    elif n%2 == 0:
        n = int(n/2)
    return n

def solution(n,a,b):
    answer = 0
    round = int(math.log2(n))
    # nums = [min(a,b), max(a,b)]
    
    while(answer<round):
        nums = [min(a,b), max(a,b)]
        if nums[0]%2 == 1 and nums[1]%2 == 0 and nums[0]+1 == nums[1]:
            return answer + 1
        else:
            a = checknext(a)
            b = checknext(b)
            answer+=1
        
    return answer