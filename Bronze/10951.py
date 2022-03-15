while True:
    try:
        A,B = map(int, input().split())
        print(A+B)
    except:
        break

# 테스트 케이스의 개수가 정해지지 않음
# try 에는 변수에 int형이 들어가면 출력
# except 는 try 에 대한 에러가 발생하면 break를 해준다