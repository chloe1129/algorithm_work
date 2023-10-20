def solution(n):
    answer = 0
    jump = [0,1,2]
    if n < 3:
        return jump[n]
    
    for i in range(3,n+1):
        jump.append(jump[i-1]+jump[i-2])
        
    return jump[-1]%1234567