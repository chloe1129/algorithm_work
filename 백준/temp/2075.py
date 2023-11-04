import heapq
import sys

N = int(sys.stdin.readline())

heap = []

heapq.heapify(heap)

for i in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    if len(heap) < N:
        for j in range(N):
            heapq.heappush(heap, lst[j])
    elif len(heap) == N:
        for j in range(N):
            a = heapq.heappop(heap)
            if lst[j] > (a):
                heapq.heappush(heap, lst[j])
            else:
                heapq.heappush(heap, a)

print(heap)
print(heapq.heappop(heap))
