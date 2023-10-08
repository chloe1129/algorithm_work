import sys


def dfs(x, y):
    if x < 0 or y < 0 or x > n-1 or y > n-1:
        return False

    if block[x][y] == '1':
        # print('is here 1? ',block[x][y],x,y)
        # 1이면 방문 처리 해주기
        block[x][y] = '0'
        result.append(1)

        # 상하좌우 체크
        dfs(x, y+1)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x-1, y)
        return True
    return False


n = int(sys.stdin.readline())
block = []
result = []
result_list = []
for _ in range(n):
    block.append(list(map(str, sys.stdin.readline().strip())))

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            result_list.append(len(result))
            result = []

print(len(result_list))
result_list.sort()

for i in range(len(result_list)):
    print(result_list[i])
