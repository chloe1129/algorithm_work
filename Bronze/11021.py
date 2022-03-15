T=int(input())
for i in range(1,T+1):
    A,B=map(int, input().split())
    print(f'Case #{i}: {A+B}')

# print 함수 안에서 문자열으 작성하기 위해 '' 앞에 f 를 붙여야한다
# 변수는 {} 안에 값을 입력해야한다