def fact(num):
    if num==0:
        return 1
    return num*fact(num-1)
N=int(input())
print(fact(N))