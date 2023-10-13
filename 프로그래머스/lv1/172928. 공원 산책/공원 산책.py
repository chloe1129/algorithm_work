def solution(park, routes):
    x, y = 0, 0
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                x = i
                y = j

    # print('start', x, y)
    for i in range(len(routes)):
        d, m = routes[i].split()
        m = int(m)
        # print('this rout!!', d, m)
        # print('now x y', x, y)
        yes = True
        if d == 'E':  # 오른쪽
            if y+m < len(park[0]):
                for j in range(y, y+m+1):
                    # print('nonononononononon', park[x][j])
                    if park[x][j] == 'X':
                        yes = False
                        break
                if yes == True:
                    # print('YES E')
                    y += m

        elif d == 'W':  # 왼쪽
            if y-m >= 0:
                for j in range(y-m, y):
                    if park[x][j] == 'X':
                        yes = False
                        break
                if yes == True:
                    # print('YES W')
                    y -= m
        elif d == 'S':  # 아래
            if x+m < len(park):
                for j in range(x, x+m+1):
                    # print('checkchekc', j, park[j][y])
                    if park[j][y] == 'X':
                        yes = False
                        break
                if yes == True:
                    # print('YES S')
                    x += m
        elif d == 'N':  # 위
            if x-m >= 0:
                for j in range(x-m, x):
                    if park[j][y] == 'X':
                        yes = False
                        break
                if yes == True:
                    # print('YES N')
                    x -= m
    return [x, y]


