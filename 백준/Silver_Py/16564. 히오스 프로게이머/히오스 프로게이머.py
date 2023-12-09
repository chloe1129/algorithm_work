import sys

n, k = map(int, sys.stdin.readline().split())
lvl = [int(sys.stdin.readline()) for i in range(n)]
lvl.sort()
# print(lvl)

start = lvl[0]
end = lvl[0]+k

result = 0
while (start <= end):
    mid = (start+end)//2

    h = 0
    for i in lvl:
        if mid > i:
            h += (mid - i)  # 기준 값보다 레벨이 낮은 경우, 기준 값이 되기 위해 필요한 값을 구하기
    if h <= k:
        start = mid+1
        result = mid
    else:
        end = mid - 1
print(result)
