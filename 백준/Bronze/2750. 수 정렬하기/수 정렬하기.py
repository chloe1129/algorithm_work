n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

for i in range(len(a)):
    a = sorted(a)
    print(a[i])