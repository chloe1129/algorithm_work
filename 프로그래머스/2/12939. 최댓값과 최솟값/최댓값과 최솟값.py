def solution(s):
    answer = ''
    lst = list(map(int, s.split()))
    return str(min(lst))+' '+str(max(lst))