import sys

ww = 0
for i in range(5):
    stime, etime = map(str, sys.stdin.readline().split())
    shour, smin = map(int, stime.split(':'))
    ehour, emin = map(int, etime.split(':'))

    if emin-smin < 0:
        ehour = ehour-1
        emin = emin+60

    ww += (ehour-shour)*60 + emin-smin

print(ww)
