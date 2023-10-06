import sys

n = int(sys.stdin.readline())

data = []
for i in range(n):
    print(i)
    a, b = map(int, sys.stdin.readline().split())
    data.append(a+b)

for j in range(n):
    print('Case #'+str(j+1)+': '+str(data[j]))
