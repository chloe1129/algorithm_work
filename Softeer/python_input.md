# Python 입력받기, sys.stdin.readline

> input() 대신 sys.stdin.readlind()을 사용하는 이유
> 한 두줄 입력받는 문제와 다르게 반복문으로 여러줄 입력 받아야 할 때는 input()으로 입력받으면 시간초과가 발생할 수 있다.

## sys.stdin.readline() 사용법

### 정수 한 개 입력받을 때

```
import sys
a = int(sys.stdin.readline())
```

### 정해진 개수의 정수를 한줄에 입력받을 때

```
import sys
a,b,c = map(int,sys.stdin.readline().split())
```

### 임의의 개수의 정수를 한줄에 입력받아 리스트에 저장할 때

```
import sys
data = list(map(int,sys.stdin.readline().split()))
```

<split()>은 문자열을 나눠주는 함수이다.
괄호 안에 특정 값을 넣어주면 그 값을 기준으로 문자열을 나누고 아무것도 넣지 않으면 공백(스페이스,탭,엔터 등)을 기준으로 나눈다.

<list()>는 자료형을 리스트형으로 변환해주는 함수

<map()>은 맵 객체를 만들기 때문에 리스트로 바꿔줘야해 <list()>로 바꿔줬다.

### 임의의 개수의 정수를 n줄 입력받아 2차원 리스트에 저장할 때

```
import sys
data = []
n = int(sys.stdin.readline())

for i in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))
```

### 문자열 n줄을 입력받아 리스트에 저장할 때

```
import sys
n = int(sys.stdin.readlind())
data = [sys.stdin.readline().strip() for i in range (n)]
```

<strip()>은 문자열 맨 앞과 맨 끝의 공백문자를 제거한다.
