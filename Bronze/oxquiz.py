b = int(input())
a = [list(b) for b in input().split()]
num = [0]*b
for j in range(b):
    count = 0
    for i in range(len(a[j])):
        if a[j][i] == 'O':
            count+=1
            num[j]+=count
        else:
            count=0

print(num)