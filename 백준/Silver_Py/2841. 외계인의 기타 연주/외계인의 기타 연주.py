import sys
from bisect import bisect_left

# N: 멜로디의 수, P: 프랫의 수
N, P = sys.stdin.readline().split()
N = int(N)
P = int(P)
count = 0
save = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
for i in range(N):
    # m: 멜로디 음, prat: 해당 프랫
    m, prat = sys.stdin.readline().split()
    m = int(m)
    prat = int(prat)
    # print('save??', save)
    # print('add',  m, prat)
    if prat not in set(save[m]):
        if len(save[m]) == 0:  # 저장된 prat이 아무것도 없을 때
            # print('nothing in save')
            save[m].append(prat)
            save[m].sort()
            count += 1
        else:  # 저장된 prat이 있을 때
            # print('something in prat')
            idx = bisect_left(save[m], prat)
            count += (len(save[m])-idx+1)
            # print(f'index:{idx} ====== count:{count}')
            save[m] = save[m][:idx]
            save[m].append(prat)
    else:
        # 있을 때
        # print('same in prat')
        idx = bisect_left(save[m], prat)
        count += (len(save[m])-idx-1)
        # print(f'index:{idx} ====== count:{count}')
        save[m] = save[m][:idx+1]
    # print('save?? result', save, m, prat)
    # print('====================')

print(count)
