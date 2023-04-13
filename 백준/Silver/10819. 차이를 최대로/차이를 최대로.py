import itertools
n = int(input())
A = list(map(int, input().split()))
maxarr = []

def abssum(arr):
    result =[]
    for i in range(len(arr)-1):
        result.append(abs(arr[i]-arr[i+1]))
    return sum(result)

for i in itertools.permutations(A,n):
    maxarr.append(abssum(i))

print(max(maxarr))