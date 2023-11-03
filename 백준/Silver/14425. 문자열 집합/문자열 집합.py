N, M = map(int, input().split())

S = set()
count = 0

for i in range(N):
    s = str(input()).strip()
    S.add(s)

for j in range(M):
    m = str(input()).strip()
    if m in S:
        count += 1

print(count)
