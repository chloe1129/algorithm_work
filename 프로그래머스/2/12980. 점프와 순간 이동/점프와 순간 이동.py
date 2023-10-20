def solution(n):
    ans = 0
    if n == 0:
        ans+= 0

    while(n>0):
        if n%2 == 0:
            # print('n is even',n,ans)
            n=int(n/2)
        else:
            # print('n is odd',n,ans)
            n=int((n-1)/2)
            ans+=1
    return ans