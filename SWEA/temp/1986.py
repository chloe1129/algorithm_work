T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    i = 1
    sums = 0
    while (i <= N):
        if i % 2 == 0:
            sums += (-i)
        else:
            sums += i
        i += 1
    print('#'+str(test_case)+' '+str(sums))
