import sys

n = int(sys.stdin.readline())

for i in range(n):
    pstr = list(sys.stdin.readline().strip())
    check = []
    for j in range(len(pstr)):
        check.append(pstr.pop())
        if len(check) > 1 and [check[-1], check[-2]] == ['(', ')']:
            check.pop()
            check.pop()

    if len(check) == 0:
        print('YES')
    else:
        print('NO')
