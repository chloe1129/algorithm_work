t=int(input())
for i in range(1,t):
    h, w, n = map(int, input().split())
    if n%h == 0:
        print(n/h,h)
    elif n/h<0:
        print(1)