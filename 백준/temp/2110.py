import sys


# n : 집의 개수, c : 공유기의 개수
n, c = map(int, sys.stdin.readline().split())

# 수직선 위에 위치하는 집의 좌표, 중복 x
house = [int(sys.stdin.readline()) for i in range(n)]

house.sort()
start = 1 # 공유기들의 최소 거리
end = house[-1]-house[0] # 공유기들의 최대 거리
answer = 0

while(start=<end):
    for i in range(n):
        mid = (start+end)//2

        if house[mid]-house[0]<house[len(house)-1]-house[mid]:



print(final)
