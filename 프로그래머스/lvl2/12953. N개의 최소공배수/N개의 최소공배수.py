import math

def solution(arr):
    answer = arr[0]
    for i in range(1,len(arr)):
        # print(type(answer*arr[i]), type(math.gcd(answer,arr[i])))
        answer = int(answer*arr[i]/int(math.gcd(answer,arr[i])))
    return answer