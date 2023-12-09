def backtrack(x):
    for i in range(x):
        # 열 or 대각선이 같으면 false
        # 대각선이 같은 경우는 두 좌표에서 행-행 = 열-열 이 같으면 같은 선상
        if row[x] == row[i] or (abs(row[x]-row[i]) == x -i):
            return False
    return True

def dfs(x):
    global result

    if x == n:
        result += 1
        return
    else:
        # 각 행에 퀸을 두기
        for i in range(n):
            row[x] = i

            # 행, 열, 대각선을 확인하는 함수
            # true면 계속 진행
            if backtrack(x):
                dfs(x+1)

n = int(input())
row = [0]*n
result = 0
dfs(0)
print(result)