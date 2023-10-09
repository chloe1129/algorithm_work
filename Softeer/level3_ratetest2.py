import sys
sys.setrecursionlimit(1000000)  # 1000000번 재귀가 가능하도록 변경하기


def merge_sort(arr):  # 병합 정렬 이중으로 말고 이렇게 구현하기
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] > high_arr[h]:  # 내림차순이므로 부등호 방향 변경
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr


def saverank(s: list):
    each = {}  # 점수별 사람수를 저장할 딕셔너리
    rank = {}  # 점수별로 등수를 저장할 배열
    final = [0]*len(s)  # 입력받은 순서대로 등수를 저장할 배열
    i = 1  # 현재 등수

    sorted_s = merge_sort(s)
    for j in range(n):
        each[sorted_s[j]] = 0  # i번째 시험 점수를 순서대로 저장
        rank[sorted_s[j]] = 0  # i번째 시험 점수의 둥수 순서대로 저장

    for k in range(n):
        each[s[k]] += 1  # 각 점수에 분포한 사람들 넣어주기

    sorted_set = list(set(sorted_s))
    for l in range(len(each)):  # sorted_s 순서대로 [20,10,10] rank 저장
        # print(each[sorted_s[l]])
        if each[sorted_set[l]] == 1:
            rank[sorted_set[l]] = i
            i += 1
        else:
            rank[sorted_set[l]] = i
            i += each[sorted_set[l]]

    for m in range(n):
        # print(rank[s[m]])
        final[m] = str(rank[s[m]])
    return final


n = int(sys.stdin.readline())  # 사람 수
iput = []
total = [0]*n  # 사람별 총 합 점수
for a in range(n):
    total[a] = 0

for i in range(3):  # 3번의 시험
    # 시험 i의 점수들들, len(사람수)
    iput.append(list(map(int, sys.stdin.readline().split())))
    for f in range(n):
        total[f] += iput[i][f]  # 순서대로 점수의의 총합 저장

for i in iput:
    real = saverank(i)
    print(' '.join(real))

real = saverank(total)
print(' '.join(real))
