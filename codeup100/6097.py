h,w = map(int, input().split())

b = []
for i in range(h):
    b.append([])
    for j in range(w):
        b[i].append(0)

n = int(input())

for i in range(n):
    l,d,x,y = map(int, input().split())
    x=x-1
    y=y-1

    if d == 0:
        for i in range(l):
            b[x][y+i] = 1
    else:
        for i in range(l):
            b[x+i][y] = 1


for i in range(len(b)) :
  for j in range(len(b[i])) :
    print(b[i][j], end=' ')
  print()