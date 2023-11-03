import heapq
import sys

N = int(sys.stdin.readline())

heap = []
heapq.heapify(heap)

for i in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            a = heapq.heappop(heap)
            print(a)
    else:
        heapq.heappush(heap, x)
