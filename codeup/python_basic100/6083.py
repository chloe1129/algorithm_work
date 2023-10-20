a, b, c = input().split()
count = 0
for i in range(int(a)):
    for j in range(int(b)):
        for k in range(int(c)):
            print(i,j,k)
            count+=1
print(count)