def solution(price, money, count):
    n=0
    for i in range(1,count+1):
        n+=(i*price)

    return 0 if money-n >= 0 else n - money

'''
impressive answer

def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)
'''

print(solution(3,20,4))