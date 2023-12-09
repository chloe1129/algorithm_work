import sys
from collections import deque


T = int(sys.stdin.readline())

for i in range(T):
    p = sys.stdin.readline().strip()  # R or D
    n = int(sys.stdin.readline())  # length of list
    test = (sys.stdin.readline().strip()).strip('[]').split(',')
    if n == 0:
        test = deque()
    else:
        test = deque(test)

    re = 0
    error = False
    for j in range(len(p)):
        if p[j] == 'R':
            re += 1
        elif p[j] == 'D':
            if len(test) > 0:
                if re % 2 == 0:
                    test.popleft()
                else:
                    test.pop()
            else:
                error = True

    if error == True:
        print('error')
    else:
        if re % 2 == 0:
            print('['+','.join(list(test))+']')
        else:
            print('['+','.join(list(test)[::-1])+']')
