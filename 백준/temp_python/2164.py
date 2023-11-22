import sys
from collections import deque

n = int(sys.stdin.readline())
cards = [i for i in range(1, n+1)]

cards = deque(cards)

while (len(cards) > 1):
    cards.popleft()
    n = cards.popleft()
    cards.append(n)

print(cards[0])
