import itertools
n,m = map(int, input().split())

a =[]
for i in range(1,n+1):
    a.append(i)

for i in itertools.permutations(a, m):
    b = ''
    for j in i:
        if j == i[-1]:
            b = b+str(j)
        else:
            b = b+str(j)+' '
    print(b)