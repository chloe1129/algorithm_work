import sys

k, p, n = map(int, sys.stdin.readline().split())

for i in range(n):
    k = k * p
    k = k % 1000000007

print(k % 1000000007)
