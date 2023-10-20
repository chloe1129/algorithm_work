def solution(n):
    ans = 0
    if n == 0:
        ans+= 0
    elif n == 1 or n == 2:
        ans+= 1
    elif n==3 or n==4 or n==5 or n== 6:
        ans+= 2
    else:
        while(n>0):
            if n%2 == 0:
                # print('n is even',n,ans)
                n=int(n/2)
            else:
                # print('n is odd',n,ans)
                n=int((n-1)/2)
                ans+=1
    return ans