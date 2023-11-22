import sys

N = int(sys.stdin.readline())

consult = {}
maxmon = float('-inf')


for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    consult[i+1] = temp  # [걸리는 시간, 금액]


for j in range(1, N+1):
    point = j
    remain = N-j+1
    money = 0
    while (True):
        if remain - consult[point][0] >= 0:
            print('now', point, consult[point])
            print('remain', remain)
            remain -= consult[point][0]
            money += consult[point][1]
            point += consult[point][0]
        else:
            break
        print('current money', money)
        if point >= N:
            break

    maxmon = max(maxmon, money)
    print('============')
print(maxmon)
