def solution(n):
    fibo = [0,1]
    for i in range(2,n+1):
        # print(fibo[n-1], fibo[n-2])
        fibo.append(fibo[i-1]+fibo[i-2])
    return fibo[-1]%1234567