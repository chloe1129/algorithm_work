import sys

info = []

w, n = map(int, sys.stdin.readline().split())
for i in range(n):
    # m : 금속의 무게
    # p : 무게 1당 가격
    m, p = map(int, sys.stdin.readline().split())
    info.append([p, m])

info.sort(key=lambda x: x[1], reverse=True)
# print(info)
total = w
m = 0
for i in range(len(info)):
    # print('what is i :',i)
    # print('info!!', m,info[i],total)
    if info[i][1] >= total:
        m += total*info[i][0]
        total -= total
    elif info[i][1] < total:
        m += (info[i][1]*info[i][0])
        total -= info[i][1]
print(m)
