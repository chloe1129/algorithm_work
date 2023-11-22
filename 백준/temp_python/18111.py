import sys
n, m, b = map(int, sys.stdin.readline().split())
data = []
for _ in range(n):
    data += list(map(int, sys.stdin.readline().split()))

min_h = min(data)
max_h = max(data)

result_sec = float('inf')
result_h = 0
for h in range(min_h, max_h+1):
    tmp_sec = 0
    tmp_h = b
    for i in range((n*m)):
        if data[i] > h:
            tmp_sec += (data[i] - h) * 2
            tmp_h += (data[i] - h)
        else:  # data[i] < h
            tmp_sec += (h - data[i])
            tmp_h -= (h - data[i])
    if tmp_h >= 0:
        if result_sec >= tmp_sec:
            result_sec = tmp_sec
            result_h = h

print(result_sec, result_h)


# import sys

# # n: 가로길이, m: 세로길이, b: 추가할 수 있는 블록의 수
# n, m, bs = map(int, sys.stdin.readline().split())

# # 최소시간, 그 중 가장 높은 땅의 높이
# # 블록 제거: 2초, 블록 추가: 1초

# ground = []
# for i in range(n):
#     temp = list(map(int, sys.stdin.readline().split()))
#     ground += temp

# min_h = min(ground)
# max_h = max(ground)

# totaltime = float('inf')
# finalb = 0
# for i in range(min_h, max_h+1):
#     time = 0
#     inputblock = bs
#     works = True
#     # print('===========기준 높이', i)
#     for j in range(n*m):
#         # print('검사하는', ground[j])
#         if i < ground[j]:  # 기준이 높이보다 작을 때, 제거 필요
#             time += (ground[j]-i)*2
#             inputblock += (ground[j]-i)
#             # print('< 일때 시간', (ground[j]-i)*2)
#         elif i > ground[j]:  # 기준이 높이보다 클 때, 추가 필요
#             if inputblock >= i-ground[j]:  # 인벤토리에 추가 할만큼의 블럭이 있는지?
#                 time += i-ground[j]
#                 inputblock -= i-ground[j]
#                 # print('> 일때 시간', (i-ground[j]), i-ground[j])
#             else:
#                 # print('안됨!!!!!!!', inputblock)
#                 works = False

#     if totaltime >= time and i >= finalb and works == True:
#         # print('저장할때', time, i)
#         totaltime = time
#         finalb = i

# print(totaltime, finalb)
