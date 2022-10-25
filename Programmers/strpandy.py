def solution(s):
    test = s.lower()
    nump = test.count("p")
    numy = test.count("y")
    
    if nump != numy:
        return False
    return True

asw=solution("pPoooyY")
print(asw)