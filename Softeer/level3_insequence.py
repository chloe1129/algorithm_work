import sys

def dfs(x1,y1):
    #print('coor in dfs',x1,y1)
    if x1<0 or y1<0 or x1>n-1 or y1>n-1:
        return False
    if block[x1][y1] == 0:
        # 지나간간 블록 장애물로로 처리
        block[x1][y1] = 1
        dfs(x1,y1+1)
        dfs(x1,y1-1)
        dfs(x1-1,y1)
        dfs(x1+1,y1)
        return [x1,y1]
    return False

# n : 격자의의 크기
# m : 방문해야하는 칸의의 개수
n,m = map(int, sys.stdin.readline().split())

block =[]
lst = []
for i in range(n):
    block.append(list(map(int,sys.stdin.readline().split())))

print('what block look',block)
for i in range(n):
    lst.append(list(map(int,sys.stdin.readline().split())))
print('what lst look',lst)


num=0
result = 0
while(num<m-1):
    print('what go to fun',lst[num][1]-1,n-lst[num][0])
    print('fuc re',dfs(lst[num][1]-1,n-lst[num][0]))

    if dfs(lst[num][1]-1,n-lst[num][0]) == lst[num+1]:
        print('same???',dfs(lst[num][1]-1,n-lst[num][0]),lst[num+1])
        num+=1
    elif dfs(lst[num][1]-1,n-lst[num][0]) in lst:
    
    else:
        dfs(dfs(lst[num][1]-1,n-lst[num][0]))
    if num == m-1:
        result+=1

print(result)