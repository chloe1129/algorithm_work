import sys

N = int(sys.stdin.readline())
num = 1
cnt = 0

while (True):
    # print(num)
    if '666' in str(num):
        cnt += 1
    num += 1
    if cnt == N:
        break

print(num-1)
