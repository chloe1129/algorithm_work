n= 1260

count=0

coin_types=[500, 100,50,10]

for coin in coin_types:
    count+=n//coin # 수 = 수 + 돈 나누기 동전의 몫
    n%= coin # 왼쪽 변수를 오른쪽 값으로 나누고 그 나머지을 왼쪽 변수에 할당

print(count)

# // 연산자: 나누기 연산 후 소수점 이하의 수를 버리고 정수 부분의 수만 구함