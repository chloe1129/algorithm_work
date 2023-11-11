import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
lst = []
for i in range(1, n+1):
    lst.append(i)

combi = list(combinations(lst, m))
combi = list(map(list, combi))
# print(combi)
for i in (combi):
    temp = list(map(str, i))
    temp = ' '.join(temp)
    print(temp)
