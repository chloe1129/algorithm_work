import sys

# n : 회의실 수
# m : 예약된 회의의 수
n, m = map(int, sys.stdin.readline().split())

# room : 회의실의 이름
room = [sys.stdin.readline().strip() for i in range(n)]
room = sorted(room)

data = {}
for i in range(n):
    data[room[i]] = [9, 10, 11, 12, 13, 14, 15, 16, 17]

for i in range(m):
    rroom, st, et = map(str, sys.stdin.readline().split())

    for j in range(int(st), int(et)):
        if j in data[rroom]:
            data[rroom][data[rroom].index(j)] = str(j).replace(str(j), ' ')

data = dict(sorted(data.items()))
for i in range(len(data)):
    print('Room ' + room[i] + ':')
    pp = []
    cnt = 0
    print('What is in this room', data[room[i]])
    j = 0
    while (j < 9):

        print('datadata', j)
        if data[room[i]][j] == ' ' and j != 0:
            print('yes', data[room[i]][:j])
            pp[cnt] = data[room[i]][:j]
            data[room[i]] = data[room[i]][j+1:]
            cnt += 1
            j += 1
        elif data[room[i]][j] == ' ' and j == 0:
            print('no', data[room[i]][j+1:])
            data[room[i]] = data[room[i]][j+1:]
        elif data[room[i]][j] != ' ':
            pp[cnt].append(data[room[i]][j])
            j += 1

    if cnt == 0:
        print('Not available')
    else:
        print(str(cnt)+'available')
        for i in range(len(cnt)):
            print(str(pp[i][0]) + '-' + str(pp[i][len(pp[i])]))


# 3 7
# grandeur
# avante
# sonata
# sonata 14 16
# grandeur 11 12
# avante 15 18
# sonata 10 11
# avante 9 12
# grandeur 16 18
# avante 12 15
