import sys
from collections import deque

a = deque()
a = [1, 2, 3, 4, 5]
print(a.pop(0))

'''
data1 = []
n = int(sys.stdin.readline())

for i in range(n):
    data1.append(list(map(int, sys.stdin.readline().split())))

data2 = [sys.stdin.readline().strip() for i in range(n)]

print('data1: ', data1)
print('data2: ', data2)
'''

'''
n = 4
input 1 : 
1 2 3 4
output 1 : [[1], [2], [3], [4]]

input 2 : 
안녕 나는 이채현 취업하고싶어

output 2 : ['안녕', '나는', '이채현', '취업하고싶어']
'''
