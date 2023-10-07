import sys

# n : 회의실 수
# m : 예약된 회의의 수
n, m = map(int, sys.stdin.readline().split())

# room : 회의실 이름
room = [sys.stdin.readline().strip() for i in range(n)]
room = sorted(room)

data = {}
for i in range(len(room)):
    data[room[i]] = [[9, 18]]

# {'avante':[[9,18]],
# 'grandeur':[[9,18]],
# 'sonata':[[9,18]]}

# data['방이름'] -> [[9,18],[]..]

for i in range(m):
    # r : 방 이름
    r, st, et = map(str, sys.stdin.readline().split())
    l = 0
    st = int(st)
    et = int(et)

    while (l < len(data[r])):
        room_time = data[r]

        if st <= room_time[l][1]:
            if room_time[l][0] == st and room_time[l][1] == et:
                data[r].remove([st, et])

            elif room_time[l][0] < st and et < room_time[l][1]:
                data[r].append([et, room_time[l][1]])
                room_time[l] = [room_time[l][0], st]

            elif room_time[l][0] < st and room_time[l][1] == et:
                room_time[l] = [room_time[l][0], st]

            elif room_time[l][0] == st and et < room_time[l][1]:
                room_time[l] = [et, room_time[l][1]]

            break

        elif st > room_time[l][1]:
            l += 1


for i in range(len(data)):
    data[room[i]] = list(sorted(data[room[i]]))
    print('Room '+room[i]+':')
    if len(data[room[i]]) == 0:
        print('Not available')
    else:
        print(str(len(data[room[i]]))+' available:')

        for j in range(len(data[room[i]])):
            if data[room[i]][j][0] == 9:
                data[room[i]][j][0] = '09'
            print(str(data[room[i]][j][0])+'-'+str(data[room[i]][j][1]))

    if 0 <= i < len(data)-1:
        print('-----')
