def solution(n):
    answer = 0
    a = str(bin(n))[2:]
    num = a.count('1')
    i=1
    while(True):
        n+=i
        if str(bin(n))[2:].count('1') == num:
            break
    return n