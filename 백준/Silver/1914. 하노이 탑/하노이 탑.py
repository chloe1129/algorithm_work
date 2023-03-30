# a: 옮길 원반이 있는 출발점
# b: 원반을 옮길 도착점
# c: 옮길 때 사용할 보조 기둥

def f(n, a, b, c):
  if(n == 1):
    print(a, b, sep = " ")
    return
  else:
    # 원반 n-1개를 보조 기둥으로
    f(n-1, a, c, b)
    print(a, b, sep = " ")
    
    # 보조 기둥의 원반 n-1을 목적지로 이동
    f(n-1, c,b,a)

n = int(input())
print(2**n-1)
if(n <= 20):
  f(n, 1, 3,2)
