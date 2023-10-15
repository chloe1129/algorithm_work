def solution(s):
    cntz = 0
    cntn = 0   
    
    while s != '1':
        num = s.count('1')
        cntz += len(s)-num
        
        s=str(bin(num))[2:]
        cntn+=1
    
    return [cntn,cntz]
    
