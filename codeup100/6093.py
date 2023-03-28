n = int(input())
a = input().split()
# for i in range(n-1, -1,-1):
#     print(a[i], end=' ')

for i in reversed(range(n)):
    print(a[i], end=' ')