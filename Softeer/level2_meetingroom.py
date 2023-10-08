import sys

# n : 회의실 수
# m : 예약된 회의의 수
n, m = map(int, sys.stdin.readline().split())

# room : 회의실 이름
room = [sys.stdin.readline().strip() for i in range(n)]
room = sorted(room)

data = {}
result = {}
for i in range(len(room)):
    data[room[i]] = [0]*18
    result[room[i]] = []

for j in range(m):
    name, st, et = map(str, sys.stdin.readline().strip().split())
    st, et = int(st), int(et)
    for k in range(st, et):
        data[name][k] = 1

# print(result)
# print(data)

i = 9
r = 0
temp = []
while (i < 18 and r < len(room)):
    # print('now info', room[r], i, data[room[r]][i])
    if data[room[r]][i] == 0:
        # print('what is in here', i, data[room[r]][i])
        temp.append(i)
    else:
        if len(temp) > 0:
            result[room[r]].append(temp)
            temp = []
    if i == 17 and len(temp) > 0:
        result[room[r]].append(temp)
        temp = []
    i += 1
    if i == 18:
        i = 9
        r += 1

# print(result)

for i in range(len(result)):
    print('Room '+room[i]+':')
    if len(result[room[i]]) == 0:
        print('Not available')
    else:
        print(str(len(result[room[i]])) + " available:")
        for j in range(len(result[room[i]])):
            # print(result[room[i]][j])

            if len(result[room[i]][j]) == 1:
                if result[room[i]][j][0] == 9:
                    print('09-' +
                          str(result[room[i]][j][0]+1))
                else:
                    print(str(result[room[i]][j][0]) + '-' +
                          str(result[room[i]][j][0]+1))
            else:
                if result[room[i]][j][0] == 9:
                    print('09-' +
                          str(result[room[i]][j][0]+1))
                else:
                    print(str(result[room[i]][j][0]) + '-' +
                          str(result[room[i]][j][len(result[room[i]][j])-1]+1))
    if i < len(result)-1:
        print('-----')
