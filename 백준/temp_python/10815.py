import sys

n = int(input())
nums = list(map(int, sys.stdin.readline().split()))
nums = set(nums)

m = int(input())
find = list(map(int, sys.stdin.readline().split()))

result = []

for i in find:
    if i in nums:
        result.append('1')
    else:
        result.append('0')

print(' '.join(result))
