from collections import deque
def solution(s):
    answer = True
    left = deque()
    s = list(s)
    for i in range(len(s)):
        left.appendleft(s.pop())
        
        if len(left)>=2:
            if [left[0],left[1]] == ['(',')']:
                left.popleft()
                left.popleft()
                
    if len(left) >0:
        answer = False
    
    return answer