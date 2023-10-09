import sys


def dfs(x, y, g):
    global cnt
    # print('same???????',g ,len(goal)-1)
    if (g == len(goal)-1):  # 목표의 마지막이라면
        # print('last>>>>>?', x, y)
        if (goal[g][0]-1 == x and goal[g][1]-1 == y):
            cnt += 1
            # print('endendendendned',cnt)
            return
    elif (goal[g][0]-1 == x and goal[g][1]-1 == y):
        # print('keep going!',x,y,g,len(goal)-1)
        dfs(x, y, g+1)
    # visited[x][y] = True

    for i in range(4):
        # print('checkcheck11', x,y)
        move_x = [0, 0, -1, 1]
        move_y = [1, -1, 0, 0]
        nx = x + move_x[i]
        ny = y + move_y[i]
        # print('checkcheck22',nx,ny)
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False and block[nx][ny] == 0:
            # print('original', x, y)
            # print('can go', nx, ny)
            visited[nx][ny] = True
            dfs(nx, ny, g)
            visited[nx][ny] = False


# n : 격자의의 크기
# m : 방문해야하는 칸의의 개수
n, m = map(int, sys.stdin.readline().split())

block = []  # 입력받은 격자 전체 n*n
goal = []  # 방문해야할 칸의 배열들
for i in range(n):
    block.append(list(map(int, sys.stdin.readline().split())))
for i in range(m):
    goal.append(list(map(int, sys.stdin.readline().split())))
print(goal)
visited = [[False for i in range(n)]for j in range(n)]  # 탐색에서 방문 여부를 체크하는 배열
# print(visited)
x, y = goal[0][0]-1, goal[0][1]-1  # 시작 위치
visited[x][y] = True
cnt = 0
dfs(x, y, 0)
print(cnt)
