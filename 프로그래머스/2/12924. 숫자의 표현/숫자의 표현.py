def solution(n):
    i = 1
    sums = i
    seri = i
    cnt =0
    while(i<n):
        # print(i,sums,cnt)
        if sums == n:
            cnt+=1
            i+=1
            seri = i
            sums = i
        elif sums > n:
            i+=1
            seri = i
            sums = i
        else:
            seri+=1
            sums= sums+(seri)
            
    return cnt+1

        