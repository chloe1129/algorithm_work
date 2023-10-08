import sys

n, m = map(int, sys.stdin.readline().split())

slimit = {}
real = {}
for i in range(n):
    slimit[i] = list(map(int, sys.stdin.readline().split()))
for i in range(m):
    real[i] = list(map(int, sys.stdin.readline().split()))

l = 0
r = 0
diff = 0
while (l < n and r < m):
    # 실제 거리가 기준 거리보다 짧을 때
    if real[r][0] < slimit[l][0]:
        slimit[l][0] -= real[r][0]
        diff = max(diff, real[r][1]-slimit[l][1])
        r += 1
    # 실제 거리가 기준 거리와 같을 때
    elif real[r][0] == slimit[l][0]:
        diff = max(diff, real[r][1]-slimit[l][1])
        r += 1
        l += 1
    elif real[r][0] > slimit[l][0]:
        real[r][0] -= slimit[l][0]
        diff = max(diff, real[r][1]-slimit[l][1])
        l += 1

print(diff)
