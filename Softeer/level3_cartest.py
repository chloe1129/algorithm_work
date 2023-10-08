import sys
import bisect
# n : 자동차차 개수수
# q : 구해야 할 값의 개수
n, q = map(int, sys.stdin.readline().split())

car = list(map(int, sys.stdin.readline().split()))
car.sort()
# print(car)

carset = set(car)
for i in range(q):
    a = int(sys.stdin.readline())
    # print(a,car.index(a))
    if a not in carset:
        print(0)
    else:
        # print(a,car.index(a))
        idx = bisect.bisect_left(car, a)
        print(idx*(n-idx-1))
