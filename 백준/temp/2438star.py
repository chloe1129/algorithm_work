n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print("*", end="")
    print()

    ## end 를 사용하면 뒤의 출력값과 이어서 출력한다