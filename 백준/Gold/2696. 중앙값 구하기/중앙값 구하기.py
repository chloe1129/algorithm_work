import sys
# import heapq
import math
from collections import deque

T = int(sys.stdin.readline())

for i in range(T):
    m = int(sys.stdin.readline())
    middle = []
    temp = []
    if m > 10:
        for _ in range(math.ceil(m/10)):
            su = deque(list(map(int, sys.stdin.readline().split())))
            for j in range(len(su)):
                val = su.popleft()
                temp.append(val)
                temp.sort()
                if j % 2 == 0:
                    middle.append(temp[len(temp)//2])

    else:
        su = deque(list(map(int, sys.stdin.readline().split())))
        for j in range(len(su)):
            val = su.popleft()
            temp.append(val)
            temp.sort()
            if j % 2 == 0:
                middle.append(temp[len(temp)//2])

    print(len(middle))
    if len(middle) > 10:
        for j in range(math.ceil(len(middle)/10)):
            print(' '.join(list(map(str, middle[10*j:10+10*j]))))
    else:
        print(' '.join(list(map(str, middle))))

# for i in range(T):
#     m = int(sys.stdin.readline())
#     su = []
#     heapq.heapify(su)

#     middle = []

#     if m > 10:
#         for _ in range(math.ceil(m/10)):
#             temp = list(map(int, sys.stdin.readline().split()))
#             for j in range(len(temp)):
#                 heapq.heappush(su, temp[j])
#                 if j % 2 == 0:
#                     save = heapq.nlargest(len(su)//2 + 1, su)
#                     middle.append(save[-1])
#     else:
#         temp = list(map(int, sys.stdin.readline().split()))
#         for j in range(len(temp)):
#             heapq.heappush(su, temp[j])
#             if j % 2 == 0:
#                 save = heapq.nlargest(len(su)//2 + 1, su)
#                 middle.append(save[-1])

#     print(len(middle))
#     if len(middle) > 10:
#         for j in range(math.ceil(len(middle)/10)):
#             print(' '.join(list(map(str, middle[10*j:10+10*j]))))
#     else:
#         print(' '.join(list(map(str, middle))))
