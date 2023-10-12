import sys


# n : 집의 개수, c : 공유기의 개수
n, c = map(int, sys.stdin.readline().split())

# 수직선 위에 위치하는 집의 좌표, 중복 x
house = [int(sys.stdin.readline()) for i in range(n)]

house.sort()

start, end = 1, house[n-1] - house[0]
# 집 사이의 최소 거리, 최대 거리
result = 0

if c == 2:
    print(house[n-1] - house[0])
    # 집이 2개라면 무조건 처음, 마지막 집 사이의 거리
else:
    while (start < end):
        mid = (start + end)//2
        print('start', start, end, mid)
        count = 1
        ts = house[0]
        # 마지막으로 설치된 공유기의 위치
        for i in range(n):
            if house[i] - ts >= mid:
                print('11111', house[i], ts, mid)
                count += 1
                ts = house[i]
        if count >= c:
            result = mid
            start = mid + 1
        elif count < c:
            end = mid
    print(result)
