a = int(input())
for i in range(a):
    sum = 0
    b = input().split()
    for j in range(1,len(b)):
        sum+=int(b[j])

    avg = sum/int(b[0])
    count = 0 
    for j in range(1,len(b)):
        if int(b[j]) - avg > 0:
            count+=1
    print(f"{count/int(b[0])*100:.3f}%")
