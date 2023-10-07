import sys

info = []
e = 0

w, n = map(int, sys.stdin.readline().split())
for i in range(n):
    # m : 금속의 무게
    # p : 무게 1당 가격
    m, p = map(int, sys.stdin.readline().split())
    info.append([p, m])


print(info)
