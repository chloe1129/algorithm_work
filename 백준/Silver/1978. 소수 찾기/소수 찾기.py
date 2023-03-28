n = int(input())
a = map(int, input().split())

num = 0
odd= 0
    
for i in a:
    if i == 1:
        continue
    else:
        for j in range(2,i-1):
            if i%j == 0:
                num+=1
            
        if num == 0:
            odd+=1
        num = 0

print(odd)