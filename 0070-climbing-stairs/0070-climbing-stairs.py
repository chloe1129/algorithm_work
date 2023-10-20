class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        fibo = [1,2]
        for i in range(2,n):
            fibo.append(fibo[i-1]+fibo[i-2])
        
        return fibo[-1]