import sys

n, c = map(int, sys.stdin.readline().split())

arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort()

start = 0
end = arr[-1]-arr[0]
count = 1
while (start <= end):
    start = 0
    end = arr[-1]-arr[0]
    count = 1
    mid = (start+end)//2  # 처음과 끝의 중간으로 처음 공유기 사이의 거리 예측
    current = arr[0]
    for i in range(1, len(arr)):

        # 마지막으로 설치한 공유기 + 예측한 공유기 사이의 거리 <= 주어진 i번 째의 집
        if current + mid <= arr[i]:
            count += 1
            current = arr[i]

    # 만약 설치한 공유기 수가 주어진 공유기보다 많거나 같다면?
    if count >= c:
        global answer
        # mid 값을 늘리기
        start = mid+1
        answer = mid
    else:
        # 설치한 공유기 수가 주어진 공유기보다 적다면?
        # mid 값을 줄이기
        end = mid-1

print(answer)
