import sys

# m 비밀 메뉴 조작법의 버튼 개수
# n 사용자가 누른 버튼 개수
# k 자판기의 총 버튼 개수
m, n, k = map(int, sys.stdin.readline().split())

btn_m = list(map(int, sys.stdin.readline().split()))
btn_n = list(map(int, sys.stdin.readline().split()))

ni = 0
while (ni < len(btn_n)):
    if btn_n[ni] not in btn_m:
        btn_n.remove(btn_n[ni])
    else:
        ni += 1
btn_m = ''.join(map(str, btn_m))
btn_n = ''.join(map(str, btn_n))

# print(btn_m,btn_n)
if btn_m in btn_n:
    print('secret')
else:
    print('normal')
