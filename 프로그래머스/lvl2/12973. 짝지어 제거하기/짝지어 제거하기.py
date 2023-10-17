def solution(s):
    check = []
    s=list(s)
    while(len(s)>0):
        check.append(s.pop())
        # print(check)
        if len(check)>1 and check[-1] == check[-2]:
            # print('same??',check[-1], check[-2])
            check.pop()
            check.pop()
            
    if len(check)>0:
        return 0
    else:
        return 1